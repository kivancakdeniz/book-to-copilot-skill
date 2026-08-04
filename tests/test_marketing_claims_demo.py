"""Contracts for the fictional Marketing Claims Review Cowork demo."""

import importlib.util
import hashlib
import json
import re
import struct
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEMO = ROOT / "demos" / "marketing-claims-review"
SKILL = DEMO / "skill"
PACKAGE_MANIFEST = "evidence/metadata/cowork-package-manifest.json"

spec = importlib.util.spec_from_file_location(
    "package_cowork_skill",
    ROOT / "tools" / "package_cowork_skill.py",
)
packager = importlib.util.module_from_spec(spec)
sys.modules["package_cowork_skill"] = packager
spec.loader.exec_module(packager)

renderer_spec = importlib.util.spec_from_file_location(
    "render_marketing_claims_scenarios",
    DEMO / "evaluation" / "render_scenarios.py",
)
renderer = importlib.util.module_from_spec(renderer_spec)
sys.modules["render_marketing_claims_scenarios"] = renderer
renderer_spec.loader.exec_module(renderer)


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
    policy = (
        DEMO / "sources" / "company-policy.md"
    ).read_text(encoding="utf-8")

    assert manifest["demoId"] == "marketing-claims-review"
    assert len(manifest["sources"]) == 6
    public_hashes = {
        "ftc-rules-road-pdf": (
            "d000f004d9c28b66dd81a590e6ecdacc5f9d08caf7b6af626407436abebe336a"
        ),
        "ftc-dot-com-disclosures-2013": (
            "b189fd2c01b21309021c9cba5ae2d5cb8abb55a555bde412e11f124c420a142e"
        ),
        "ftc-endorsement-guides-2023-07-26": (
            "feb1c8cfee82158c16c4210ef320bc93ffb2f414aa2bdce6e6772a77064180ea"
        ),
    }
    for source_id, expected_hash in public_hashes.items():
        source = next(
            item for item in manifest["sources"] if item["id"] == source_id
        )
        assert source["sha256"] == expected_hash
        assert source["redistribution"] == "metadata-only"
        assert "path" not in source
        assert "17 U.S.C. 105" in source["reuseCaveat"]
        assert "third-party" in source["reuseCaveat"].lower()

    synthetic = [source for source in manifest["sources"] if source.get("synthetic")]
    assert len(synthetic) == 3
    for source in synthetic:
        path = DEMO / "sources" / source["path"]
        assert path.is_file()
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"]
        assert source["type"].startswith("synthetic-")

    assert len(scenarios) == 12
    assert len({scenario["id"] for scenario in scenarios}) == 12
    assert len({scenario["title"] for scenario in scenarios}) == 12
    allowed = {
        "approve",
        "approve-with-edits",
        "hold-for-substantiation",
        "escalate-legal",
        "reject",
    }
    assert set(scenario_set["allowedDecisionClasses"]) == allowed
    assert set(scenario_set["allowedOptions"]) == set(
        scenario_set["allowedCampaignOptions"]
    )
    for scenario in scenarios:
        assert scenario["expectedDecision"] in allowed
        assert scenario["expectedOption"] in scenario_set["allowedOptions"]
        for rule in scenario.get("requiredRules", []):
            assert re.fullmatch(r"MCS-[A-Z]\d{2}", rule)
            assert rule in policy

    baseline = scenarios[0]
    assert baseline["id"] == "MC-01"
    assert baseline["expectedDecision"] == "approve-with-edits"
    assert baseline["expectedOption"] == "evidence-bounded-campaign"
    assert set(baseline["requiredFindings"]) == {
        "bill-savings-unsupported",
        "payback-unsupported",
        "universal-compatibility-unsupported",
        "independence-misrepresented",
        "influencer-result-unsupported",
        "disclosures-inadequate",
    }
    assert {
        "MCS-Q01",
        "MCS-U01",
        "MCS-D01",
        "MCS-I01",
        "MCS-A01",
        "MCS-R01",
    }.issubset(baseline["requiredRules"])
    assert scenario_set["mutationSemantics"]
    assert scenario_set["promptPath"] == "evaluation/frozen-prompt.md"
    formal_prompt = DEMO / scenario_set["promptPath"]
    assert hashlib.sha256(formal_prompt.read_bytes()).hexdigest() == scenario_set[
        "promptFileSha256"
    ]
    assert set(scenario_set["allowedCampaignOptions"]) == {
        scenario["expectedOption"] for scenario in scenarios
    }

    campaign_brief = (DEMO / "sources" / "case-brief.md").read_text(
        encoding="utf-8"
    )
    assert "## Baseline answer key" not in campaign_brief
    assert "product page" in campaign_brief
    assert "no typical-results analysis" in campaign_brief

    scenario_guide = (SKILL / "scenario-guide.md").read_text(encoding="utf-8")
    assert "Expected baseline behavior" not in scenario_guide
    assert "six decisive baseline defects" not in scenario_guide
    comparative = next(scenario for scenario in scenarios if scenario["id"] == "MC-06")
    assert comparative["expectedDecision"] == "reject"

    assert rubric["maximumPositiveScore"] == 14
    assert len(rubric["dimensions"]) == 8
    assert sum(item["max"] for item in rubric["dimensions"]) == 14
    assert rubric["reportedMetrics"] == [
        "totalScore",
        "unsupportedClaimCount",
        "abstentionCorrect",
        "responseWords",
        "evidenceReferenceCount",
    ]
    assert set(rubric["metricDefinitions"]) == set(rubric["reportedMetrics"])
    for dimension in rubric["dimensions"]:
        assert set(dimension["anchors"]) == {
            str(score) for score in range(dimension["max"] + 1)
        }

    for name in (
        "frozen-prompt.md",
        "chat-only-prompt.md",
        "chat-only-treatment-prompt.md",
        "chat-only-treatment-installed-prompt.md",
    ):
        prompt = (DEMO / "evaluation" / name).read_text(encoding="utf-8")
        normalized = " ".join(prompt.split())
        assert "Respond only in this chat" in normalized
        assert "at most 700 words" in normalized
        assert "Do not create, edit, render, or attach" in normalized


def test_cowork_skill_structure_and_links():
    files = sorted(
        path.relative_to(SKILL).as_posix()
        for path in SKILL.rglob("*")
        if path.is_file()
    )
    assert files == [
        "SKILL.md",
        "company-policy.md",
        "evidence-map.md",
        "output-schema.md",
        "public-method.md",
        "scenario-guide.md",
    ]

    master = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert "name: marketing-claims-review" in master
    assert "license: MIT" in master
    assert "allowed-tools" not in master
    for relative in files[1:]:
        assert f"./{relative}" in master

    for path in SKILL.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^]]+\]\(([^)]+\.md)\)", text):
            resolved = (path.parent / target).resolve()
            resolved.relative_to(SKILL.resolve())
            assert resolved.is_file()


def test_cowork_skill_packages_deterministically(tmp_path: Path):
    manifest = _json(PACKAGE_MANIFEST)
    first = packager.build_archive(SKILL, tmp_path / "first.skill")
    second = packager.build_archive(SKILL, tmp_path / "second.skill")

    assert (DEMO / manifest["sourcePath"]).resolve() == SKILL.resolve()
    assert first.read_bytes() == second.read_bytes()
    assert first.stat().st_size < packager.MAX_COMPRESSED_BYTES
    files = packager.collect_skill_files(SKILL)
    assert len(files) == 6
    assert all(path.stat().st_size < packager.MAX_FILE_BYTES for path in files)
    assert sum(path.stat().st_size for path in files) < (
        packager.MAX_UNCOMPRESSED_BYTES
    )
    assert len(files) == manifest["fileCount"]
    for prompt in manifest["promptFiles"].values():
        # Frozen manifest paths are relative to the original cowork/ package directory.
        path = (DEMO / prompt["path"].removeprefix("../")).resolve()
        assert hashlib.sha256(path.read_bytes()).hexdigest() == prompt["sha256"]
    with zipfile.ZipFile(first) as archive:
        assert archive.namelist()[0] == "SKILL.md"
        assert len(archive.namelist()) == 6


def test_formal_scenarios_render_deterministically_without_answer_keys():
    manifest = _json("evaluation/render-manifest.json")
    first = renderer.render_inputs(DEMO)
    second = renderer.render_inputs(DEMO)

    assert first == second
    assert len(first) == manifest["inputCount"] == 12
    assert {record["scenarioId"] for record in first} == set(manifest["inputs"])
    for record in first:
        scenario = next(
            item for item in _json("evaluation/scenarios.json")["scenarios"]
            if item["id"] == record["scenarioId"]
        )
        assert record["inputSha256"] == hashlib.sha256(
            record["modelInput"].encode("utf-8")
        ).hexdigest()
        assert f"Scenario title: {scenario['title']}" not in record["modelInput"]
        assert '"expectedDecision"' not in record["modelInput"]
        assert '"expectedOption"' not in record["modelInput"]
        assert '"requiredFindings"' not in record["modelInput"]
        assert "## Baseline answer key" not in record["modelInput"]
        assert "Expected baseline behavior" not in record["modelInput"]


def test_cowork_evidence_manifest_contract():
    metadata = DEMO / "evidence" / "metadata"
    manifest = _json("evidence/metadata/cowork-runs.json")
    package = _json(PACKAGE_MANIFEST)
    attempts = manifest["attempts"]
    included = [attempt for attempt in attempts if attempt["status"] == "included"]
    excluded = [attempt for attempt in attempts if attempt["status"] == "excluded"]

    assert manifest["evidenceKind"] == "cowork-ux-observation"
    assert manifest["coworkVersionShownByHost"] is None
    assert manifest["finalSkillPackage"]["sha256"] == package["sha256"]
    assert manifest["finalPackageUploaded"] is True
    installation = (metadata / manifest["installationScreenshotPath"]).resolve()
    assert _png_size(installation) == (1920, 1080)
    assert hashlib.sha256(installation.read_bytes()).hexdigest() == manifest[
        "installationScreenshotSha256"
    ]
    assert len(included) == 3
    assert len(excluded) == 4
    assert {attempt["runId"] for attempt in included} == {
        "control-1",
        "treatment-auto-1",
        "treatment-claude-1",
    }
    claude_runs = [
        attempt for attempt in included if attempt["modelShownByHost"] == "Claude Opus 4.8"
    ]
    assert {attempt["assignedCondition"] for attempt in claude_runs} == {
        "control",
        "treatment",
    }
    assert len({attempt["runId"] for attempt in attempts}) == len(attempts)

    for attempt in attempts:
        prompt = (metadata / attempt["promptPath"]).resolve()
        prompt.relative_to(DEMO.resolve())
        assert prompt.is_file()
        if attempt.get("promptFileSha256"):
            assert hashlib.sha256(prompt.read_bytes()).hexdigest() == attempt[
                "promptFileSha256"
            ]
        for relative in attempt["attachmentPaths"]:
            attachment = (metadata / relative).resolve()
            attachment.relative_to(DEMO.resolve())
            assert attachment.is_file()
            if attempt.get("attachmentSha256"):
                assert hashlib.sha256(attachment.read_bytes()).hexdigest() == attempt[
                    "attachmentSha256"
                ]

        if attempt["status"] == "included":
            assert attempt["exclusionReason"] is None
            output = (metadata / attempt["outputPath"]).resolve()
            assert output.is_file()
            assert hashlib.sha256(output.read_bytes()).hexdigest() == attempt[
                "outputSha256"
            ]
            output_text = output.read_text(encoding="utf-8")
            assert f"Run ID: `{attempt['runId']}`" in output_text
            assert "Conversation ID:" not in output_text
            for relative in attempt["screenshotPaths"]:
                screenshot = (metadata / relative).resolve()
                assert _png_size(screenshot) == (1920, 1080)
                assert hashlib.sha256(screenshot.read_bytes()).hexdigest() == attempt[
                    "screenshotSha256"
                ][relative]
        else:
            assert attempt["outputPath"] is None
            assert attempt["exclusionReason"]


def test_preliminary_review_contract():
    review = _json("evidence/metadata/preliminary-review.json")
    rubric = _json("evaluation/rubric.json")
    maximums = {dimension["id"]: dimension["max"] for dimension in rubric["dimensions"]}
    penalties = {penalty["id"]: penalty["score"] for penalty in rubric["penalties"]}

    assert review["status"] == "not-a-formal-benchmark"
    assert review["method"]["humanReviewCompleted"] is False
    assert {result["blindLabel"] for result in review["results"]} == {"A", "B", "C"}
    assert {result["runId"] for result in review["results"]} == {
        "control-1",
        "treatment-auto-1",
        "treatment-claude-1",
    }
    scores = {result["runId"]: result["totalScore"] for result in review["results"]}
    assert scores == {
        "control-1": 7,
        "treatment-auto-1": 12,
        "treatment-claude-1": 12,
    }

    for result in review["results"]:
        assert set(result["dimensions"]) == set(maximums)
        for dimension_id, score in result["dimensions"].items():
            assert 0 <= score <= maximums[dimension_id]
        assert result["positiveScore"] == sum(result["dimensions"].values())
        assert result["metrics"]["unsupportedClaimCount"] == sum(
            result["penaltyCounts"].values()
        )
        assert len(result["penalties"]) == sum(result["penaltyCounts"].values())
        expected = result["positiveScore"] + sum(
            penalties[penalty_id] * count
            for penalty_id, count in result["penaltyCounts"].items()
        )
        assert result["totalScore"] == expected


def test_demo_page_makes_the_observed_skill_difference_explicit():
    page = (ROOT / "docs" / "en" / "skills" / "marketing-claims-review.md").read_text(
        encoding="utf-8"
    )
    normalized = " ".join(page.split())
    assert "## Control vs skill: measured" in normalized
    assert "The control run cited 0 of 9 policy rules and the skill run cited 9." in normalized
    assert (
        "Only the skill run stated the exact decision class (`approve-with-edits`)."
        in normalized
    )
    assert (
        "Limits: one run per condition, one locked scenario, and a single host."
        in normalized
    )
    lowered = normalized.lower()
    assert "copilot cannot approve, publish, or execute an operational action" in lowered