# Turn source material into tested, reusable Agent Skills

`book-to-copilot-skill` converts books, PDFs, regulations, internal guidance,
and document collections into structured Agent Skills. It then helps you test
whether the skill changes an LLM's answer and package the result for the
Microsoft Copilot ecosystem.

![Books, documents, regulations, and institutional guidance transform into a structured Agent Skill, pass through a control-versus-skill evaluation, and branch into five portable Copilot packages.](../assets/book-to-copilot-skill-cover.webp){ loading=eager fetchpriority=high }

[Create your own skill](create-a-skill.md){ .md-button .md-button--primary }
[Explore the 12 examples](skills/index.md){ .md-button }

## What this project does

### 1. Convert

Point the Agent Skill at a file, several files, a folder, or a glob. The local
extractor supports PDF, EPUB, DOCX, Markdown, plain text, HTML, RTF, and
MOBI/AZW. The agent identifies the source structure, frameworks, rules,
techniques, and anti-patterns, then writes a reusable skill instead of a one-off
summary.

```text
book / PDF / regulation / internal docs
                    ↓
       structured Agent Skill
```

### 2. Prove

A generated skill is useful only if it changes the answer in a meaningful,
repeatable way. The repository includes a control-versus-skill evaluation
pattern: the same case and prompt are run once without the skill and once with
it. A deterministic scorer checks decision class, selected option, rule
citations, human routing, and unsafe authority claims.

Across the 12 published examples:

| Result | LLM only | LLM + skill |
| --- | ---: | ---: |
| Mean trace score | 33 / 100 | 95 / 100 |
| Examples citing no policy rules | 12 / 12 | 0 / 12 |
| Exact expected decision class | 0 / 12 | 9 / 12 |

The raw answers and scorecards are public. Three skill runs selected a more
cautious class than the locked expectation; those misses are published too.

### 3. Ship

A skill remains plain Markdown and is portable across Agent Skills hosts. The
release factory produces five deterministic packages per example:

- Microsoft 365 Copilot Cowork `.skill`
- GitHub Copilot for VS Code
- Microsoft Scout
- Copilot Studio GitHub harness
- Copilot Studio classic setup materials

The 12 examples produce 60 byte-identical packages in total.

## Use your own material

This project is not limited to the included regulatory examples. You can build a
skill from:

- a book or technical manual;
- a regulation and your own operating policy;
- internal documentation, runbooks, or architecture decisions;
- a research collection or several related papers;
- product, brand, or process guidance your organization owns.

The input stays on your machine during extraction. If the agent model is hosted,
text sent to that model follows the provider's normal data terms.

## Why the 12 examples exist

The examples show the full lifecycle with inspectable material: source metadata,
synthetic policy and case, generated skill, locked scenarios, control answer,
skill answer, scorecard, and host packages. They are proof that the workflow can
be repeated across privacy, banking, financial crime, competition, safety,
health, payments, telecom, capital allocation, and marketing review.

They are templates, not the limit of the converter.

## Open source and reusable

The repository is public under the MIT license for its code, synthetic examples,
and authored documentation. Clone it, generate your own skill, adapt the
evaluation fixture, and publish only material you have the right to share.

This project is an independent downstream of the MIT-licensed
[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)
converter. It preserves the extraction foundation and adds Copilot packaging,
repeatable evaluation, 12 enterprise examples, and release hardening. It is not
endorsed by the upstream author, Microsoft, or any public authority.

[Start with your own source](create-a-skill.md) ·
[Review safety and reuse boundaries](safety.md)
