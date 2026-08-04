"""Regression checks for the downstream GitHub Copilot compatibility gate."""

import importlib.util
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
VALIDATOR_PATH = ROOT_DIR / "tools" / "validate_skill.py"
spec = importlib.util.spec_from_file_location("validate_skill", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def test_converter_skill_passes_copilot_validation():
    errors, _warnings = validator.audit(ROOT_DIR / "SKILL.md", lens="copilot")

    assert errors == []


def test_generation_workflow_validates_before_security_scan():
    skill = (ROOT_DIR / "SKILL.md").read_text(encoding="utf-8")
    validate_command = 'tools/validate_skill.py" --lens copilot'
    scan_command = 'tools/scan_generated_skill.py"'

    assert validate_command in skill
    assert scan_command in skill
    assert skill.index(validate_command) < skill.index(scan_command)