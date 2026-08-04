<p align="center">
  <img src="docs/assets/logo.svg" alt="book-to-copilot-skill" width="88">
</p>

<h1 align="center">book-to-copilot-skill</h1>

<p align="center">
  Convert books, PDFs, regulations, and document collections into Agent Skills.<br>
  Test the skill against an LLM-only control. Package it for the Copilot ecosystem.
</p>

<p align="center">
  <a href="https://kivancakdeniz.github.io/book-to-copilot-skill/">Documentation</a> ·
  <a href="https://kivancakdeniz.github.io/book-to-copilot-skill/skills/">12 examples</a> ·
  <a href="LICENSE.md">MIT license</a>
</p>

<p align="center">
  <img src="docs/assets/book-to-copilot-skill-cover.webp" alt="Books, documents, regulations, and institutional guidance transform into a structured Agent Skill, pass through a control-versus-skill evaluation, and branch into five portable Copilot packages." width="1200">
</p>

## What this repository adds

This public downstream turns the original document-to-skill converter into a
repeatable Copilot workflow:

1. **Convert** a file, folder, glob, or collection of sources into a structured
   Agent Skill.
2. **Prove** whether the skill changes the answer by comparing LLM-only and
   LLM + skill runs against a locked expectation.
3. **Ship** the reviewed skill to Microsoft 365 Copilot Cowork, GitHub Copilot
   for VS Code, Microsoft Scout, or Copilot Studio.

The repository includes 12 public examples at the intersection of Türkiye
regulation and enterprise operations. They are templates and evidence for the
workflow, not the limit of the converter.

## Supported source material

- PDF, including technical PDFs with tables and code
- EPUB
- DOCX
- Markdown and plain text
- HTML
- RTF
- MOBI / AZW / AZW3 through Calibre
- one file, several files, a folder, or a glob

Useful source types include books, regulations, internal policies, runbooks,
architecture decisions, research collections, product guidance, and documents
your organization owns.

## Install as an Agent Skill

Clone the repository into a supported skills directory. For GitHub Copilot CLI:

```bash
git clone https://github.com/kivancakdeniz/book-to-copilot-skill.git \
  ~/.copilot/skills/book-to-skill
```

Other user-level locations include:

- `~/.agents/skills/book-to-skill` for Copilot CLI or Amp
- `~/.claude/skills/book-to-skill` for Claude Code

Review the repository before granting shell and file access.

## Convert a document

```text
/book-to-skill <path-or-glob>... [skill-name]
```

```bash
# One PDF
/book-to-skill ~/books/operating-model.pdf operating-model

# Regulation plus internal policy
/book-to-skill ~/policy/regulation.pdf ~/policy/internal-policy.docx compliance-guide

# A folder of runbooks
/book-to-skill ~/workspace/runbooks/ operations-runbook

# A research collection
/book-to-skill "~/papers/*.pdf" research-methods
```

The full Agent Skill selects an extractor, analyzes the source structure, and
writes the generated skill to a host-compatible skill directory.

Check local extractor dependencies:

```bash
python3 scripts/extract.py --check
```

## Validate a generated skill

```bash
python tools/validate_skill.py --lens copilot path/to/skill/SKILL.md
python tools/validate_skill.py --lens claude path/to/skill/SKILL.md
python tools/scan_generated_skill.py path/to/skill
```

Package any reviewed skill for Cowork:

```bash
python tools/package_cowork_skill.py path/to/skill dist/my-skill.skill
```

## Test whether the skill helps

Use the same case and prompt twice: once without the skill and once with it.
Define the expected behavior before reading the answers, then compare
correctness, rule use, evidence, omissions, and unsafe authority.

The 12 examples publish raw answers and recomputable scorecards. Across those
examples:

| Result | LLM only | LLM + skill |
| --- | ---: | ---: |
| Mean trace score | 33 / 100 | 95 / 100 |
| Examples citing no policy rules | 12 / 12 | 0 / 12 |
| Exact expected decision class | 0 / 12 | 9 / 12 |

These are one-scenario, one-host comparisons, not production benchmarks. Three
skill runs selected a more cautious class than the locked expectation; those
results remain public.

## 12 reusable examples

Each directory under `demos/<slug>/` contains:

```text
sources/       source manifest, synthetic policy, synthetic case
evaluation/    12 locked scenarios, rubric, prompts, answer key
skill/         generated six-file Agent Skill
evidence/      raw control/skill answers, run metadata, scorecard
presenter/     demo setup and checkpoints
```

The release factory validates the catalog and creates five packages per example:
Cowork, GitHub Copilot for VS Code, Scout, Copilot Studio GitHub harness, and
Copilot Studio classic setup. All 60 packages are verified byte-identical after
a clean rebuild.

[Browse the examples and downloads](https://kivancakdeniz.github.io/book-to-copilot-skill/skills/).

## Standalone extractor

If you need extraction without agent-driven skill generation:

```bash
python3 -m venv .venv
.venv/bin/pip install -e '.[pdf,epub,docx,rtf]'
.venv/bin/book-to-skill ~/books/source.pdf --mode text
```

The CLI extracts text and metadata. It does not register the Agent Skill or
write the final skill by itself.

## Development

```bash
python3 -m venv .venv
.venv/bin/pip install -e . pytest ruff
.venv/bin/python -m pytest -q
.venv/bin/ruff check .
```

Build and validate the public example release:

```bash
python tools/build_skill_release.py validate --root .
python tools/build_skill_release.py build --root . --output-dir release/skills
python tools/build_skill_release.py verify-release --root . --output-dir release/skills
```

## Safety and source rights

Use material you are allowed to process. Extraction runs locally, but text sent
to a hosted agent model follows that provider's data terms. Keep skills derived
from copyrighted or confidential sources private unless you have permission to
share them. Review every generated file before installing it.

See the [Safety & reuse](https://kivancakdeniz.github.io/book-to-copilot-skill/safety/)
page and [SECURITY.md](SECURITY.md).

## Upstream credit

This is an independent downstream of
[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill),
reused under the MIT license. It preserves the extraction foundation and adds
Copilot packaging, repeatable evaluation, 12 enterprise examples, and release
hardening. The upstream author has not endorsed this downstream.

See [NOTICE.md](NOTICE.md), [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), and
[LICENSE.md](LICENSE.md).
