"""Tests for deterministic Cowork custom-skill packaging."""

import importlib.util
import sys
import zipfile
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parent.parent / "tools"
spec = importlib.util.spec_from_file_location(
    "package_cowork_skill",
    TOOLS_DIR / "package_cowork_skill.py",
)
packager = importlib.util.module_from_spec(spec)
sys.modules["package_cowork_skill"] = packager
spec.loader.exec_module(packager)


def _write_skill(root: Path) -> Path:
    references = root / "references"
    references.mkdir(parents=True)
    (root / "SKILL.md").write_text(
        """---
name: test-skill
description: A test Cowork skill.
---

# Test

Read [policy](./references/policy.md).
""",
        encoding="utf-8",
    )
    (references / "policy.md").write_text("# Policy\n", encoding="utf-8")
    return root


def test_archive_is_deterministic_and_rooted_at_skill(tmp_path: Path):
    skill = _write_skill(tmp_path / "skill")
    first = packager.build_archive(skill, tmp_path / "first.skill")
    second = packager.build_archive(skill, tmp_path / "second.skill")

    assert first.read_bytes() == second.read_bytes()
    with zipfile.ZipFile(first) as archive:
        assert archive.namelist() == ["SKILL.md", "references/policy.md"]
        assert archive.getinfo("SKILL.md").date_time == packager.ZIP_TIMESTAMP


def test_package_rejects_missing_frontmatter_field(tmp_path: Path):
    skill = tmp_path / "invalid"
    skill.mkdir()
    (skill / "SKILL.md").write_text("---\nname: invalid\n---\n", encoding="utf-8")

    try:
        packager.collect_skill_files(skill)
    except packager.PackageError as exc:
        assert "missing description" in str(exc)
    else:
        raise AssertionError("missing description should fail packaging")


def test_package_rejects_symbolic_links(tmp_path: Path):
    skill = _write_skill(tmp_path / "skill")
    outside = tmp_path / "outside.md"
    outside.write_text("# Outside\n", encoding="utf-8")
    link = skill / "references" / "outside.md"
    try:
        link.symlink_to(outside)
    except OSError:
        return

    try:
        packager.collect_skill_files(skill)
    except packager.PackageError as exc:
        assert "symbolic links are not allowed" in str(exc)
    else:
        raise AssertionError("symbolic links should fail packaging")


def test_package_rejects_more_than_cowork_file_limit(tmp_path: Path, monkeypatch):
    skill = _write_skill(tmp_path / "skill")
    monkeypatch.setattr(packager, "MAX_FILES", 1)

    try:
        packager.collect_skill_files(skill)
    except packager.PackageError as exc:
        assert "maximum is 1" in str(exc)
    else:
        raise AssertionError("file-count overflow should fail packaging")