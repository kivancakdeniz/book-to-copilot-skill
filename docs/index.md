---
hide:
  - navigation
  - toc
---

# book-to-copilot-skill

[Türkçe](tr/index.md)

<p style="font-size: 1.25rem; max-width: 42rem;">
Compile approved business guidance into governed, evaluated Copilot skills:
decision methods, enterprise rules, provenance, and human approval boundaries.
<strong>From documents to decisions, not another context dump.</strong>
</p>

[Get started](guide.md){ .md-button .md-button--primary }
[12-skill catalog](skills/index.md){ .md-button }
[How the skills are proved](#control-vs-skill-measured-on-12-skills){ .md-button }

## What this project is for

This downstream exists to answer one question with evidence: **does compiling
approved guidance into an Agent Skill actually change what an assistant produces
on a real enterprise decision?**

To answer it, the project ships twelve worked decisions at the intersection of
Türkiye regulation and enterprise operations, runs each one twice, scores both
runs with a deterministic script, and exports the result to Microsoft 365 Copilot
Cowork, GitHub Copilot, Microsoft Scout, and Copilot Studio.

## Upstream and independence

This project is an independent downstream of
[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill),
reused under its [MIT License](https://github.com/virgiliojr94/book-to-skill/blob/main/LICENSE.md).
The upstream project and its maintainers have not endorsed this downstream.
This edition adds GitHub Copilot compatibility, governed enterprise examples,
deterministic packages, and evaluation materials.

## Why compile guidance into a skill

- Sources are extracted locally with hashes and format-specific fallbacks.
- Public methods, company policy, case facts, and human authority stay separate
  and traceable.
- Agent Skills hosts load the core workflow first and supporting references only
  when needed.
- The output is a decision record with explicit gates, provenance, and human
  approval boundaries, not a larger prompt.

## Control vs skill, measured on 12 skills

Every skill in the catalog was tested the same way. The same locked case, the
same prompt, one difference: the skill was installed for the second run. Both
answers are scored by `tools/score_skill_answer.py`, which checks the answer
against the locked scenario. No model grades the result, so anyone can rerun the
scoring and get the same numbers.

| Measured across all 12 skills | LLM only | LLM + skill |
|---|---|---|
| Mean trace score | 33 / 100 | 95 / 100 |
| Skills citing zero policy rules | 12 of 12 | 0 of 12 |
| Skills stating the exact decision class | 0 of 12 | 9 of 12 |
| Raw answers published | 12 | 12 |

The control runs are not incompetent. They usually reach a sensible business
direction. What they cannot do is cite the company rule identifiers, state the
exact allowed decision class, and route the decision to the named human owner,
because none of that reaches the model without the skill.

!!! warning "What this does and does not prove"

    This is a per-skill, single-run comparison against locked scenarios, not a
    causal benchmark. Each skill has one control run and one skill run on one
    host, and the treatment run legitimately receives the company policy that
    the control never sees. Three of the twelve skill runs chose a more cautious
    decision class than the locked expectation, which is published rather than
    hidden. The two founding demos additionally carry Microsoft 365 Copilot
    Cowork screenshots and manifests as host-level UX evidence.

## Catalog status

The [catalog](skills/index.md) contains **12 skills** across privacy, messaging,
e-commerce, financial crime, banking, competition, safety, health, payments,
telecom, capital allocation, and advertising review. Each ships 12 locked
scenarios, a 14-point rubric, a synthetic company policy, official-source
metadata, a raw control answer, a raw skill answer, and a deterministic
scorecard.

**60 host packages are published**: five deterministic, byte-identical formats
per skill for Cowork, GitHub Copilot in VS Code, Microsoft Scout, and Copilot
Studio (GitHub harness and classic setup).

## Reference

[Architecture](ARCHITECTURE.md) · [Performance](PERFORMANCE.md) ·
[Skill reference](skill-reference.md) ·
[Enterprise demo plan](ENTERPRISE-DEMO-PLAN.md)
