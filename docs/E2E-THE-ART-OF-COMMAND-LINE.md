# E2E: The Art of Command Line

Date: 2026-08-03

## Goal

Exercise the complete downstream path with a relevant, openly licensed source:

1. pin and verify a source;
2. extract structure and metadata;
3. generate a progressive Agent Skill;
4. run Copilot compatibility and security gates;
5. register the skill in GitHub Copilot CLI;
6. test explicit, automatic, and source-bounded invocation.

## Source

- Title: The Art of Command Line
- Primary author/original maintainer: Joshua Levy (`jlevy`), with contributors
- License: CC BY-SA 4.0
- Commit: `6b50745d2e788add2e8f1ed29010e72659a9a074`
- SHA-256: `4d2d70679c81a99e0dd2bcc1ee4f56530e3d0810c9cd3c24dcff20da7b817001`
- Input: pinned English `README.md`

The source and generated derivative were created under the Git-ignored
`.local/e2e/` workspace. No source book text or generated derivative was
committed, and all temporary E2E artifacts and the Copilot CLI skill registration
were removed after the experiment.

## Extraction

| Measure | Result |
|---|---:|
| Source lines | 624 |
| Source words | 5,961 |
| Extracted words | 5,966 |
| Estimated tokens | 7,954 |
| Detected sections | 12 |
| Extraction method | plain-text Markdown |

The first run reported `has_toc=false` even though the source starts with a
Markdown list of local links to its sections. The extractor only recognized
named headers such as "Table of Contents". The E2E test produced a regression
test and a bounded fix: three or more local list anchors must match real ATX
heading slugs. External-link lists remain negative. The real source now reports
`has_toc=true` while preserving the 12-section count.

## Generated Skill

The reference-depth output contains:

- one `SKILL.md` with core frameworks, chapter index, topic index, limits, and provenance;
- 10 on-demand chapter files;
- `glossary.md`, `patterns.md`, and `cheatsheet.md`;
- explicit CC BY-SA 4.0 attribution, pinned commit, and source hash.

| Gate | Result |
|---|---|
| GitHub Copilot lens | Pass, 0 warnings |
| Claude lens | Pass, 0 warnings |
| Generated-skill security scan | Pass |
| Markdown links | 0 broken, 0 escaping |
| Long source overlap | No 24-word overlap |
| Main body budget | About 2,409 tokens, below 4,000 |
| Supporting budgets | Pass |

## GitHub Copilot CLI

Host: GitHub Copilot CLI 1.0.77.

The generated directory was registered with `copilot skill add`. `copilot skill
list` discovered `the-art-of-command-line` as a custom skill with the expected
description.

### Explicit invocation

Prompt: safely preview processing every JSON file on macOS when names can contain
spaces or newlines.

Result: Pass. The response used NUL-delimited `find -print0 | xargs -0`, replaced
the action with `echo` for preview, warned about BSD/GNU differences, and cited
chapters 3, 4, and 8.

### Automatic invocation

Prompt: investigate `df` showing a full filesystem while `du` reports less,
without naming the skill.

Result: Pass with a grounding note. Copilot selected the skill automatically,
cited chapter 5, and correctly surfaced deleted-but-open files through `lsof`.
It also supplemented the skill with reasonable general knowledge such as
`findmnt` and `journalctl`. Future evaluations should distinguish useful
augmentation from strict source grounding.

### Source-bounded invocation

Prompt: explain whether `set -euo pipefail` is universally safe, using only the
skill.

Result: Pass. The response treated strict mode as conditional, called out
control-flow subtleties, supplied a defensive skeleton, recommended leaving the
shell when quoting, portability, state, or error handling become difficult, and
cited chapters 3 and 1.

The isolated host workspace remained empty; no test prompt modified files.

## Findings

1. The deterministic extractor and agent-driven generator work end to end on a
   concise technical Markdown source.
2. Copilot host discovery works with the generated frontmatter and custom skill
   directory.
3. Progressive chapter routing is visible in real responses.
4. Markdown anchor indexes need first-class ToC detection; this test added it.
5. Host evaluation needs two grounding modes: skill-guided augmentation and
   strict source-only answering.
6. Generation remains agent-driven rather than deterministic. Future fixtures
   should score structure, provenance, coverage, and answer behavior rather than
   byte-for-byte output.