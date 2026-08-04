# book-to-copilot-skill downstream

This public downstream adapts `book-to-skill` for the Microsoft Copilot
ecosystem while preserving the upstream extraction engine and Agent Skills
compatibility.

## Repository model

- `origin`: public downstream `kivancakdeniz/book-to-copilot-skill`
- `upstream`: public origin project `virgiliojr94/book-to-skill`
- `master`: downstream development branch

Keep broadly useful extractor and security fixes suitable for contribution to
upstream. Keep Microsoft-specific packaging, evaluation, and integration work in
this downstream unless upstream explicitly adopts it.

## Initial goals

1. Validate the converter and every generated skill against GitHub Copilot rules.
2. Test generated skills in VS Code agent mode, GitHub Copilot CLI, and Microsoft Scout.
3. Package compatible skills for Copilot Cowork.
4. Define a separate instructions, knowledge, and MCP export path for Copilot Studio.
5. Add Turkish structure detection, provenance checks, and repeatable evaluation fixtures.

## Local setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install pytest ruff
.venv/bin/python -m pytest tests/ -q
.venv/bin/python -m ruff check --select E9,F --target-version py310 \
  book_to_skill/ scripts/ tests/ tools/
```

Check host compatibility:

```bash
.venv/bin/python tools/validate_skill.py --lens claude SKILL.md
.venv/bin/python tools/validate_skill.py --lens copilot SKILL.md
```

## Upstream sync

```bash
git fetch upstream
git merge upstream/master
```

Resolve downstream conflicts locally, rerun the full test and host-validation
suite, then push the verified result to `origin`.

## Content safety

Do not commit source books, extracted full text, generated skills derived from
copyrighted material, credentials, or local model/provider state. Use synthetic,
owned, or openly licensed fixtures for repository tests.

## Recorded experiments

- [The Art of Command Line E2E](https://github.com/kivancakdeniz/book-to-copilot-skill/blob/master/docs/E2E-THE-ART-OF-COMMAND-LINE.md)
- [Enterprise demo delivery plan](https://github.com/kivancakdeniz/book-to-copilot-skill/blob/master/docs/ENTERPRISE-DEMO-PLAN.md)
- `demos/investment-committee/`: first Cowork business demo corpus, evaluation,
  custom skill, and presenter kit