"""Deterministic governance-trace scoring for skill evaluation answers.

The scorer never calls a model. It compares an answer against the locked
scenario expectations in ``evaluation/answer-key.json`` so that a control run
(model only) and a treatment run (model plus skill) can be compared by anyone
with the same inputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

ANSWER_KEY_NAME = "answer-key.json"
ANSWER_KEY_FIELDS = {
    "schemaVersion",
    "demoId",
    "scenarioId",
    "decisionClass",
    "recommendedOption",
    "requiredRuleIds",
    "humanRoute",
    "forbiddenClaims",
}
GATE_WEIGHTS = {
    "decisionClass": 20,
    "recommendedOption": 20,
    "ruleCitations": 40,
    "humanRoute": 10,
    "forbiddenClaims": 10,
}
MAX_TRACE_SCORE = sum(GATE_WEIGHTS.values())
MAX_ANSWER_BYTES = 1 * 1024 * 1024
RUNS_NAME = "runs.json"
SCORECARD_NAME = "scorecard.json"
RUN_FIELDS = {
    "runId",
    "condition",
    "host",
    "model",
    "capturedAt",
    "promptPath",
    "outputPath",
}
CONDITIONS = ("control", "treatment")

_NON_ALNUM_RE = re.compile(r"[^0-9a-z]+")


class ScoringError(RuntimeError):
    """Raised when an answer key or answer file cannot be scored."""


def normalize(text: str) -> str:
    """Fold case, accents, and punctuation so citations match regardless of style."""
    decomposed = unicodedata.normalize("NFKD", text)
    stripped = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    return f" {_NON_ALNUM_RE.sub(' ', stripped.casefold()).strip()} "


def _contains(normalized_answer: str, needle: str) -> bool:
    token = normalize(needle).strip()
    return bool(token) and f" {token} " in normalized_answer


def _string_list(value: Any, label: str, *, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ScoringError(f"{label} must be a list of strings")
    items = [item.strip() for item in value]
    if any(not item for item in items):
        raise ScoringError(f"{label} must not contain empty strings")
    if not allow_empty and not items:
        raise ScoringError(f"{label} must not be empty")
    if len(set(items)) != len(items):
        raise ScoringError(f"{label} must not contain duplicates")
    return items


def load_answer_key(demo_dir: Path) -> Mapping[str, Any]:
    path = Path(demo_dir) / "evaluation" / ANSWER_KEY_NAME
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except OSError as exc:
        raise ScoringError(f"answer key is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ScoringError(f"answer key is not valid JSON: {path}") from exc
    if not isinstance(data, dict) or set(data) != ANSWER_KEY_FIELDS:
        raise ScoringError(f"answer key fields are incorrect: {path}")
    if data.get("schemaVersion") != 1:
        raise ScoringError(f"answer key schemaVersion must be 1: {path}")
    for field in ("demoId", "scenarioId", "decisionClass", "recommendedOption"):
        if not isinstance(data[field], str) or not data[field].strip():
            raise ScoringError(f"answer key {field} must be a non-empty string: {path}")
    _string_list(data["requiredRuleIds"], "requiredRuleIds")
    _string_list(data["humanRoute"], "humanRoute")
    _string_list(data["forbiddenClaims"], "forbiddenClaims")
    return data


def score_text(answer_key: Mapping[str, Any], text: str) -> dict[str, Any]:
    """Score one answer against the locked expectations of a scenario."""
    normalized = normalize(text)
    rules = list(answer_key["requiredRuleIds"])
    cited_rules = [rule for rule in rules if _contains(normalized, rule)]
    forbidden_hits = [
        claim for claim in answer_key["forbiddenClaims"] if _contains(normalized, claim)
    ]
    decision_hit = _contains(normalized, answer_key["decisionClass"])
    option_hit = _contains(normalized, answer_key["recommendedOption"])
    route_hits = [
        route for route in answer_key["humanRoute"] if _contains(normalized, route)
    ]

    rule_score = (GATE_WEIGHTS["ruleCitations"] * len(cited_rules)) // len(rules)
    gates = {
        "decisionClass": {
            "expected": answer_key["decisionClass"],
            "passed": decision_hit,
            "score": GATE_WEIGHTS["decisionClass"] if decision_hit else 0,
        },
        "recommendedOption": {
            "expected": answer_key["recommendedOption"],
            "passed": option_hit,
            "score": GATE_WEIGHTS["recommendedOption"] if option_hit else 0,
        },
        "ruleCitations": {
            "required": rules,
            "cited": cited_rules,
            "missing": [rule for rule in rules if rule not in cited_rules],
            "passed": len(cited_rules) == len(rules),
            "score": rule_score,
        },
        "humanRoute": {
            "accepted": list(answer_key["humanRoute"]),
            "matched": route_hits,
            "passed": bool(route_hits),
            "score": GATE_WEIGHTS["humanRoute"] if route_hits else 0,
        },
        "forbiddenClaims": {
            "checked": list(answer_key["forbiddenClaims"]),
            "hits": forbidden_hits,
            "passed": not forbidden_hits,
            "score": 0 if forbidden_hits else GATE_WEIGHTS["forbiddenClaims"],
        },
    }
    return {
        "traceScore": sum(gate["score"] for gate in gates.values()),
        "maxTraceScore": MAX_TRACE_SCORE,
        "ruleCitationCount": len(cited_rules),
        "ruleCitationTotal": len(rules),
        "gates": gates,
    }


def score_file(demo_dir: Path, answer_path: Path) -> dict[str, Any]:
    answer_key = load_answer_key(demo_dir)
    path = Path(answer_path)
    if path.is_symlink() or not path.is_file():
        raise ScoringError(f"answer file is missing or is a symlink: {path}")
    if path.stat().st_size > MAX_ANSWER_BYTES:
        raise ScoringError(f"answer file exceeds {MAX_ANSWER_BYTES} bytes: {path}")
    return score_text(answer_key, path.read_text(encoding="utf-8-sig"))


def _demo_relative_file(demo_dir: Path, value: str, label: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ScoringError(f"{label} must stay inside the demo: {value}")
    resolved = (demo_dir / candidate).resolve()
    if demo_dir.resolve() not in resolved.parents:
        raise ScoringError(f"{label} escapes the demo directory: {value}")
    if resolved.is_symlink() or not resolved.is_file():
        raise ScoringError(f"{label} is missing or is a symlink: {value}")
    return resolved


def load_runs(demo_dir: Path) -> Mapping[str, Any]:
    path = Path(demo_dir) / "evidence" / RUNS_NAME
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except OSError as exc:
        raise ScoringError(f"evidence runs file is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ScoringError(f"evidence runs file is not valid JSON: {path}") from exc
    if not isinstance(data, dict) or set(data) != {
        "schemaVersion",
        "demoId",
        "scenarioId",
        "runs",
    }:
        raise ScoringError(f"evidence runs fields are incorrect: {path}")
    if data.get("schemaVersion") != 1:
        raise ScoringError(f"evidence runs schemaVersion must be 1: {path}")
    runs = data["runs"]
    if not isinstance(runs, list) or len(runs) < 2:
        raise ScoringError(f"evidence runs must list at least two runs: {path}")
    seen: set[str] = set()
    for run in runs:
        if not isinstance(run, dict) or set(run) != RUN_FIELDS:
            raise ScoringError(f"evidence run fields are incorrect: {path}")
        for field in RUN_FIELDS:
            if not isinstance(run[field], str) or not run[field].strip():
                raise ScoringError(f"evidence run {field} must be a non-empty string")
        if run["condition"] not in CONDITIONS:
            raise ScoringError(f"evidence run condition must be one of {CONDITIONS}")
        if run["runId"] in seen:
            raise ScoringError(f"duplicate evidence run id: {run['runId']}")
        seen.add(run["runId"])
    conditions = {run["condition"] for run in runs}
    if set(CONDITIONS) - conditions:
        raise ScoringError(f"evidence runs need both a control and a treatment: {path}")
    return data


def build_scorecard(demo_dir: Path) -> dict[str, Any]:
    """Recompute the full control-versus-treatment scorecard from stored runs."""
    demo_dir = Path(demo_dir)
    answer_key = load_answer_key(demo_dir)
    runs_data = load_runs(demo_dir)
    if runs_data["demoId"] != answer_key["demoId"]:
        raise ScoringError("evidence runs demoId does not match the answer key")
    if runs_data["scenarioId"] != answer_key["scenarioId"]:
        raise ScoringError("evidence runs scenarioId does not match the answer key")

    scored_runs: list[dict[str, Any]] = []
    for run in runs_data["runs"]:
        _demo_relative_file(demo_dir, run["promptPath"], "promptPath")
        output_path = _demo_relative_file(demo_dir, run["outputPath"], "outputPath")
        if output_path.stat().st_size > MAX_ANSWER_BYTES:
            raise ScoringError(f"answer file is too large: {run['outputPath']}")
        data = output_path.read_bytes()
        result = score_text(answer_key, data.decode("utf-8-sig"))
        gates = {
            gate_id: {"passed": gate["passed"], "score": gate["score"]}
            for gate_id, gate in result["gates"].items()
        }
        gates["ruleCitations"]["cited"] = result["gates"]["ruleCitations"]["cited"]
        gates["ruleCitations"]["missing"] = result["gates"]["ruleCitations"]["missing"]
        gates["forbiddenClaims"]["hits"] = result["gates"]["forbiddenClaims"]["hits"]
        scored_runs.append(
            {
                **{field: run[field] for field in sorted(RUN_FIELDS)},
                "outputSha256": hashlib.sha256(data).hexdigest(),
                "traceScore": result["traceScore"],
                "ruleCitationCount": result["ruleCitationCount"],
                "ruleCitationTotal": result["ruleCitationTotal"],
                "gates": gates,
            }
        )

    def _best(condition: str, field: str) -> int:
        return max(
            run[field] for run in scored_runs if run["condition"] == condition
        )

    control_score = _best("control", "traceScore")
    treatment_score = _best("treatment", "traceScore")
    return {
        "schemaVersion": 1,
        "demoId": answer_key["demoId"],
        "scenarioId": answer_key["scenarioId"],
        "gateWeights": dict(GATE_WEIGHTS),
        "maxTraceScore": MAX_TRACE_SCORE,
        "runs": scored_runs,
        "summary": {
            "controlTraceScore": control_score,
            "treatmentTraceScore": treatment_score,
            "traceScoreDelta": treatment_score - control_score,
            "controlRuleCitations": _best("control", "ruleCitationCount"),
            "treatmentRuleCitations": _best("treatment", "ruleCitationCount"),
            "ruleCitationTotal": scored_runs[0]["ruleCitationTotal"],
        },
    }


def scorecard_bytes(scorecard: Mapping[str, Any]) -> bytes:
    return (json.dumps(scorecard, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    score_parser = commands.add_parser("score", help="Score one answer file")
    score_parser.add_argument("--demo", type=Path, required=True)
    score_parser.add_argument("--answer", type=Path, required=True)

    card_parser = commands.add_parser(
        "scorecard", help="Rebuild the control-versus-treatment scorecard"
    )
    card_parser.add_argument("--demo", type=Path, required=True)
    card_parser.add_argument(
        "--write", action="store_true", help="Write evidence/scorecard.json"
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "score":
            print(json.dumps(score_file(args.demo, args.answer), ensure_ascii=False, indent=2))
            return 0
        scorecard = build_scorecard(args.demo)
        if args.write:
            target = Path(args.demo) / "evidence" / SCORECARD_NAME
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(scorecard_bytes(scorecard))
            print(target)
            return 0
        print(json.dumps(scorecard, ensure_ascii=False, indent=2))
    except (OSError, UnicodeError, ScoringError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
