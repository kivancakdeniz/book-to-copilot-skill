"""Contracts for the public Investment Committee Cowork demo."""

import importlib.util
import hashlib
import json
import re
import struct
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEMO = ROOT / "demos" / "investment-committee"
SKILL = DEMO / "skill"

spec = importlib.util.spec_from_file_location(
    "package_cowork_skill",
    ROOT / "tools" / "package_cowork_skill.py",
)
packager = importlib.util.module_from_spec(spec)
sys.modules["package_cowork_skill"] = packager
spec.loader.exec_module(packager)


def _json(relative: str):
    return json.loads((DEMO / relative).read_text(encoding="utf-8"))


def _png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as image:
        assert image.read(8) == b"\x89PNG\r\n\x1a\n"
        assert image.read(4) == b"\x00\x00\x00\r"
        assert image.read(4) == b"IHDR"
        return struct.unpack(">II", image.read(8))


def test_demo_sources_and_evaluation_contract():
    manifest = _json("sources/source-manifest.json")
    scenario_set = _json("evaluation/scenarios.json")
    scenarios = scenario_set["scenarios"]
    rubric = _json("evaluation/rubric.json")
    policy = (DEMO / "sources" / "company-policy.md").read_text(
        encoding="utf-8"
    )

    assert len(manifest["sources"]) == 4
    green_book = next(source for source in manifest["sources"] if source["id"] == "green-book-2026")
    assert re.fullmatch(r"[a-f0-9]{64}", green_book["sha256"])
    assert "Open Government Licence v3.0" in green_book["attribution"]
    assert green_book["redistribution"] == "metadata-only"
    assert "path" not in green_book

    synthetic = [source for source in manifest["sources"] if source.get("synthetic")]
    assert len(synthetic) == 3
    for source in synthetic:
        path = DEMO / "sources" / source["path"]
        assert path.is_file()
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"]
        assert source["type"].startswith("synthetic-")

    assert len(scenarios) == 12
    assert len({scenario["id"] for scenario in scenarios}) == 12
    assert scenarios[0]["expectedDecision"] == "conditional-approval"
    assert scenarios[0]["expectedOption"] == "phased-automation"
    allowed = {"approve", "conditional-approval", "escalate", "reject", "insufficient-evidence"}
    assert set(scenario_set["allowedDecisionClasses"]) == allowed
    assert set(scenario_set["allowedOptions"]) == {"none", "phased-automation"}
    for scenario in scenarios:
        assert scenario["expectedDecision"] in allowed
        assert scenario["expectedOption"] in scenario_set["allowedOptions"]
        for rule in scenario.get("requiredRules", []):
            assert rule in policy

    no_viable_option = next(scenario for scenario in scenarios if scenario["id"] == "IC-12")
    assert no_viable_option["expectedDecision"] == "reject"
    assert no_viable_option["expectedOption"] == "none"

    assert len(rubric["dimensions"]) == 8
    assert rubric["maximumPositiveScore"] == 14
    assert sum(dimension["max"] for dimension in rubric["dimensions"]) == rubric[
        "maximumPositiveScore"
    ]
    release_controls = next(
        dimension for dimension in rubric["dimensions"] if dimension["id"] == "release-controls"
    )
    assert release_controls["max"] == 1
    for dimension in rubric["dimensions"]:
        assert set(dimension["anchors"]) == {
            str(score) for score in range(dimension["max"] + 1)
        }


def test_cowork_skill_structure_and_links():
    files = sorted(path.relative_to(SKILL).as_posix() for path in SKILL.rglob("*") if path.is_file())
    assert files == [
        "SKILL.md",
        "company-policy.md",
        "evidence-map.md",
        "output-schema.md",
        "public-method.md",
        "scenario-guide.md",
    ]

    master = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert "name: investment-committee" in master
    assert "allowed-tools" not in master
    for relative in files[1:]:
        assert f"./{relative}" in master

    for path in SKILL.rglob("*.md"):
        for target in re.findall(r"\[[^]]+\]\(([^)]+\.md)\)", path.read_text(encoding="utf-8")):
            resolved = (path.parent / target).resolve()
            resolved.relative_to(SKILL.resolve())
            assert resolved.is_file()


def test_cowork_skill_packages_deterministically(tmp_path: Path):
    first = packager.build_archive(SKILL, tmp_path / "first.skill")
    second = packager.build_archive(SKILL, tmp_path / "second.skill")

    assert first.read_bytes() == second.read_bytes()
    assert first.stat().st_size < packager.MAX_COMPRESSED_BYTES
    with zipfile.ZipFile(first) as archive:
        assert archive.namelist()[0] == "SKILL.md"
        assert len(archive.namelist()) == 6


def test_cowork_evidence_manifest_contract():
    metadata = DEMO / "evidence" / "metadata"
    manifest = _json("evidence/metadata/cowork-runs.json")
    attempts = manifest["attempts"]
    included = [attempt for attempt in attempts if attempt["status"] == "included"]
    excluded = [attempt for attempt in attempts if attempt["status"] == "excluded"]

    assert manifest["evidenceKind"] == "cowork-ux-observation"
    assert manifest["coworkVersionShownByHost"] is None
    assert re.fullmatch(r"[a-f0-9]{64}", manifest["skillPackage"]["sha256"])
    assert len(attempts) == 6
    assert len(included) == 4
    assert len(excluded) == 2
    assert len({attempt["runId"] for attempt in attempts}) == len(attempts)
    assert {attempt["blindLabel"] for attempt in included} == {"A", "B", "C", "D"}
    assert [attempt["assignedCondition"] for attempt in included].count("control") == 2
    assert [attempt["assignedCondition"] for attempt in included].count("treatment") == 2

    installation = (metadata / manifest["installationScreenshotPath"]).resolve()
    assert installation.is_file()
    assert _png_size(installation) == (1600, 900)

    for attempt in attempts:
        prompt = (metadata / attempt["promptPath"]).resolve()
        prompt.relative_to(DEMO.resolve())
        assert prompt.is_file()
        for relative in attempt["attachmentPaths"]:
            attachment = (metadata / relative).resolve()
            attachment.relative_to(DEMO.resolve())
            assert attachment.is_file()

        if attempt["status"] == "included":
            assert attempt["exclusionReason"] is None
            assert re.fullmatch(r"[a-f0-9]{64}", attempt["promptBodySha256"])
            output = (metadata / attempt["outputPath"]).resolve()
            assert output.is_file()
            output_text = output.read_text(encoding="utf-8")
            assert f"Run ID: `{attempt['runId']}`" in output_text
            assert "Conversation ID:" not in output_text
            if attempt.get("outputSha256"):
                assert hashlib.sha256(output.read_bytes()).hexdigest() == attempt[
                    "outputSha256"
                ]
            for relative in attempt["screenshotPaths"]:
                screenshot = (metadata / relative).resolve()
                width, height = _png_size(screenshot)
                assert width * 9 == height * 16
                if attempt.get("screenshotSha256"):
                    assert hashlib.sha256(screenshot.read_bytes()).hexdigest() == attempt[
                        "screenshotSha256"
                    ][relative]
        else:
            assert attempt["blindLabel"] is None
            assert attempt["outputPath"] is None
            assert attempt["exclusionReason"]


def test_preliminary_review_contract():
    review = _json("evidence/metadata/preliminary-review.json")
    rubric = _json("evaluation/rubric.json")
    scorecard = _json("evaluation/ic-01-scorecard.json")
    maximums = {dimension["id"]: dimension["max"] for dimension in rubric["dimensions"]}
    penalties = {penalty["id"]: penalty["score"] for penalty in rubric["penalties"]}

    assert review["status"] == "not-a-formal-benchmark"
    assert review["method"]["humanReviewCompleted"] is False
    assert scorecard["scenarioId"] == review["scenarioId"]
    # The rehearsal predates the release-controls dimension, so it scores a rubric subset.
    scored = {dimension["id"] for dimension in scorecard["dimensions"]}
    assert scored and scored <= set(maximums)
    for dimension in scorecard["dimensions"]:
        expected_anchors = {str(score) for score in range(maximums[dimension["id"]] + 1)}
        assert set(dimension["anchors"]) == expected_anchors
    assert {result["blindLabel"] for result in review["results"]} == {"A", "B", "C", "D"}

    for result in review["results"]:
        assert set(result["dimensions"]) == scored
        for dimension_id, score in result["dimensions"].items():
            assert 0 <= score <= maximums[dimension_id]
        assert result["positiveScore"] == sum(result["dimensions"].values())
        assert result["metrics"]["unsupportedClaimCount"] == result["penaltyCounts"][
            "unsupported-rule"
        ]
        assert len(result["penalties"]) == sum(result["penaltyCounts"].values())
        expected = result["positiveScore"] + sum(
            penalties[penalty_id] * count
            for penalty_id, count in result["penaltyCounts"].items()
        )
        assert result["totalScore"] == expected


def test_demo_page_makes_the_observed_skill_difference_explicit():
    page = (ROOT / "docs" / "en" / "skills" / "investment-committee.md").read_text(
        encoding="utf-8"
    )
    normalized = " ".join(page.split())
    assert "## Source converted" in normalized
    assert "## Skill generated" in normalized
    assert "## LLM only vs LLM + skill" in normalized
    assert "## Copilot packages" in normalized
    assert "| Policy rules cited | 0 / 6 | 6 / 6 |" in normalized
    assert (
        "The locked evaluation expects decision class `conditional-approval`"
        in normalized
    )
    assert "This is a one-scenario, one-host comparison" in normalized