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
[Investment Committee demo](INVESTMENT-COMMITTEE-DEMO.md){ .md-button }
[Marketing Claims Review demo](MARKETING-CLAIMS-REVIEW-DEMO.md){ .md-button }
[10-skill catalog](skills/index.md){ .md-button }

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

## LLM only vs compiled skill

| At a glance | LLM only | LLM + compiled skill |
|---|---|---|
| Business direction | Often sensible | Usually the same sensible direction |
| Decision form | Free prose | Controlled decision class and structured rows |
| Rules and evidence | Brief-level references | Rule IDs, evidence IDs, and method sources |
| Human authority | Generic or inferred | Named roles and explicit approval gates |

## Current proof

The [Investment Committee demo](INVESTMENT-COMMITTEE-DEMO.md) retains two
brief-only controls and two explicit-skill treatments. All four chose phased
automation; the treatments added the exact decision class, policy gates,
authority route, and traceable sources.

The [Marketing Claims Review demo](MARKETING-CLAIMS-REVIEW-DEMO.md) retains a
model-matched Claude Opus 4.8 control/treatment pair plus a separate Auto
treatment. Both sides chose the evidence-bounded campaign; skill-assisted runs
added the exact class, seven auditable rows, rule/evidence mapping, and release
controls.

!!! warning "What this proves"

    These are signed-in Cowork UX observations, not causal A/B evidence. The
    treatment prompts explicitly invoked skills and included references that the
    controls did not receive. Raw first responses, screenshots, manifests, and
    preliminary rubric rehearsals are published; fixed-model evaluation and
    blinded human review remain pending.

## Catalog status

The [Türkiye enterprise catalog](skills/index.md) contains **10 new,
evaluation-ready demos** across privacy, marketing, finance, safety, health,
payments, and telecom. Their **50 host packages are ready**: five deterministic,
byte-identical package formats per skill. No Cowork A/B has been run for these 10
demos, so the catalog makes no claim about model effect, production performance,
or ROI.

## Reference

[Architecture](ARCHITECTURE.md) · [Performance](PERFORMANCE.md) ·
[Skill reference](skill-reference.md) ·
[Enterprise demo plan](ENTERPRISE-DEMO-PLAN.md)
