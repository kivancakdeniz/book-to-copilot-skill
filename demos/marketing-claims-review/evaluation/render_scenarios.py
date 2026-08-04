#!/usr/bin/env python3
"""Render deterministic, answer-key-free inputs for the formal scenario set."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


DEMO = Path(__file__).resolve().parent.parent


def _json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def render_inputs(demo: Path = DEMO) -> list[dict]:
    scenario_set = _json(demo / "evaluation" / "scenarios.json")
    sources = []
    for relative in scenario_set["sourceSet"]:
        path = demo / relative
        content = path.read_text(encoding="utf-8")
        sources.append((relative, content))

    prompt_path = demo / scenario_set["promptPath"]
    prompt = prompt_path.read_text(encoding="utf-8")
    rendered = []
    for scenario in scenario_set["scenarios"]:
        sections = [
            "# Marketing Claims Review Formal Scenario",
            f"Scenario ID: {scenario['id']}",
            "",
            "## Mutation semantics",
            scenario_set["mutationSemantics"],
            "The scenario delta below is authoritative. For each named field, ignore any conflicting baseline source statement and use the delta value. A null value means the named fact is unavailable.",
            "",
            "## Scenario delta",
            _canonical(scenario.get("mutations", {})),
        ]
        for relative, content in sources:
            sections.extend(("", f"## Source: {relative}", content.rstrip()))
        sections.extend(("", f"## User prompt: {scenario_set['promptPath']}", prompt.rstrip()))
        model_input = "\n".join(sections) + "\n"
        rendered.append(
            {
                "schemaVersion": 1,
                "scenarioSetVersion": scenario_set["scenarioSetVersion"],
                "scenarioId": scenario["id"],
                "inputSha256": hashlib.sha256(model_input.encode("utf-8")).hexdigest(),
                "modelInput": model_input,
            }
        )
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for record in render_inputs():
        output = args.output_dir / f"{record['scenarioId']}.json"
        output.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())