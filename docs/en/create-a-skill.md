# Create a skill from your own source

Use the full repository as an Agent Skill when you want an agent to extract,
analyze, and write the generated skill. Use the standalone CLI only when you
need the local text-extraction engine.

## Install the Agent Skill

Clone this public downstream into a supported skills directory. For GitHub
Copilot CLI:

```bash
git clone https://github.com/kivancakdeniz/book-to-copilot-skill.git \
  ~/.copilot/skills/book-to-skill
```

Equivalent user-level locations include `~/.agents/skills/book-to-skill` for
Copilot CLI or Amp and `~/.claude/skills/book-to-skill` for Claude Code. Review
the repository before granting shell and file access.

## Convert a source

Call the installed skill with one or more paths and an optional output slug:

```text
/book-to-skill <path-or-glob>... [skill-name]
```

Examples:

```bash
# One PDF
/book-to-skill ~/books/operating-model.pdf operating-model

# Several sources merged into one skill
/book-to-skill ~/policy/regulation.pdf ~/policy/internal-policy.docx compliance-guide

# Every supported document in a folder
/book-to-skill ~/workspace/runbooks/ operations-runbook

# A glob of related research
/book-to-skill "~/papers/*.pdf" research-methods
```

The full Agent Skill asks whether the material is technical or text-heavy,
selects an extractor, analyzes the structure, and writes the generated skill to
a host-compatible skill directory.

## Supported inputs

| Input | Extraction path |
| --- | --- |
| PDF, text-heavy | `pdftotext`, then `pypdf` or `pdfminer.six` |
| PDF, technical | Docling for tables and code blocks |
| EPUB | `ebooklib`, with a standard-library fallback |
| DOCX | `python-docx`, with ZIP/XML fallback |
| HTML | Beautiful Soup, with standard-library fallback |
| RTF | `striprtf`, with regex fallback |
| MOBI / AZW / AZW3 | Calibre `ebook-convert` |
| Markdown, TXT, reStructuredText, AsciiDoc | Built in |

Run the dependency check from the cloned repository:

```bash
python3 scripts/extract.py --check
```

## What gets generated

A full book conversion normally produces:

```text
<skill-name>/
├── SKILL.md
├── chapters/
├── glossary.md
├── patterns.md
└── cheatsheet.md
```

The root `SKILL.md` carries the mental models and topic index. Supporting files
load only when the request needs them. For the regulated decision examples in
this repository, the six-file template instead separates public method, company
policy, evidence map, output schema, and scenario guidance.

## Validate the result

Run host compatibility and prompt-injection checks before installing or sharing
a generated skill:

```bash
python tools/validate_skill.py --lens copilot path/to/skill/SKILL.md
python tools/validate_skill.py --lens claude path/to/skill/SKILL.md
python tools/scan_generated_skill.py path/to/skill
```

Treat the source as untrusted input. Review generated commands, links,
frontmatter, and claims before loading the skill into an agent.

## Test whether it helps

Use the same case and prompt twice:

1. Run the model without the generated skill.
2. Install the skill and repeat the same request.
3. Define the expected behavior before reading either answer.
4. Compare correctness, rule use, evidence, omissions, and unsafe authority.
5. Publish the raw answers and scoring method if you make a performance claim.

The 12 examples in this repository include reusable fixtures under
`demos/<slug>/evaluation/` and recomputable scorecards under
`demos/<slug>/evidence/`.

## Package for Cowork

Create a deterministic Microsoft 365 Copilot Cowork archive from any skill
directory that contains `SKILL.md`:

```bash
python tools/package_cowork_skill.py path/to/skill dist/my-skill.skill
```

For GitHub Copilot or Scout, place the reviewed skill under the host's expected
skill directory. The 12 examples also show the GitHub harness and classic setup
formats for Copilot Studio.

## Standalone extractor

If you need extraction without agent-driven skill generation, install the local
CLI from the clone:

```bash
python3 -m venv .venv
.venv/bin/pip install -e '.[pdf,epub,docx,rtf]'
.venv/bin/book-to-skill ~/books/source.pdf --mode text
```

The CLI extracts text and metadata. It does not register the `/book-to-skill`
Agent Skill or write the final skill by itself.

## Next

[Inspect the public examples](skills/index.md) to see source manifests, control
and skill answers, scorecards, and ready-to-use Copilot packages.
