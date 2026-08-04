# İndirimli fiyat denetimi

[Türkçe](../tr/skills/indirimli-fiyat-denetimi.md)

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 7 | 7 / 7 |
| Exact decision class stated | no | yes |
| Named option stated | no | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **20 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `FYT-01`

[Control answer](../assets/skills/indirimli-fiyat-denetimi/outputs/control-1.txt) · [Skill answer](../assets/skills/indirimli-fiyat-denetimi/outputs/treatment-1.txt) · [Scorecard](../assets/skills/indirimli-fiyat-denetimi/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/indirimli-fiyat-denetimi
```

The control run cited 0 of 7 policy rules and the skill run cited 7. Only the skill run stated the exact decision class (`revise-price-claim`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/indirimli-fiyat-denetimi/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Fiyat bilgisi içeren reklamlar ile indirimli satış reklamları ve ticari uygulamaları hakkında kılavuz](https://tuketici.ticaret.gov.tr/haberler/fiyat-bilgisi-iceren-reklamlar-ile-indirimli-satis-reklamlari-ve-ticari-uygulamalari-hakkinda-kilavuz-guncellendi) — Ticaret Bakanlığı |
| Public method summary | `demos/indirimli-fiyat-denetimi/skill/public-method.md` |
| Synthetic company policy | `demos/indirimli-fiyat-denetimi/sources/company-policy.md` |
| Synthetic case | `demos/indirimli-fiyat-denetimi/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/indirimli-fiyat-denetimi/evaluation/` |
| Portable skill | `demos/indirimli-fiyat-denetimi/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## At a glance

| Field | Value |
|---|---|
| Problem | Review whether a campaign creative's reference price and discount rate are consistent with the supplied price history |
| Baseline | Lowest price: 800 TL; sale price: 600 TL; supplied result: 25%; creative: 1,000 TL and 40% |
| Expected class | `revise-price-claim` |
| Expected option | `advertise-25-percent` |
| Human decision | E-commerce Owner + Pricing Owner + Compliance; Legal for an exception |

## Qualitative impact

The demo turns an interpretation-dependent creative approval review into a
repeatable flow of evidence, rules, decisions, and publication gates. The
expected qualitative effect is faster human review, clearer traceability to
price history, and fewer unsupported percentage claims. This is a design
expectation, not a measured production result or a guarantee of legal
compliance.

## Source and safety

The public methodology source is the Ticaret Bakanlığı 2024 fiyat reklamları
kılavuz page. The package does not redistribute official content; it contains
only the official URL, publisher, retrieval date of 2026-08-04, and SHA-256
metadata. Decision classes and options come from an MIT-licensed synthetic
policy. Source text is never executed as instructions, lengthy official
quotations are excluded, and no real customer or trade-secret data is used.

## Human decision limits

This skill does not provide legal advice. Humans make every decision. The skill
does not approve or publish a campaign, change a price, or perform any other
autonomous action. It does not calculate missing prices or rates. Legal becomes
involved only for a documented exception or when legal interpretation is
required.

## 12 locked scenarios

| ID | Focus | Expected class | Expected option |
|---|---|---|---|
| FYT-01 | Baseline creative mismatch | `revise-price-claim` | `advertise-25-percent` |
| FYT-02 | Compliant 25% creative | `approve` | `advertise-25-percent` |
| FYT-03 | Missing price history | `hold-for-price-history` | `no-promotion` |
| FYT-04 | Ambiguous comparison window | `hold-for-price-history` | `no-promotion` |
| FYT-05 | Missing supplied calculation result | `hold-for-price-history` | `no-promotion` |
| FYT-06 | Conflicting historical results | `hold-for-price-history` | `no-promotion` |
| FYT-07 | Correct rate, ambiguous creative | `revise-price-claim` | `advertise-25-percent` |
| FYT-08 | Documented exception | `escalate-consumer-law` | `no-promotion` |
| FYT-09 | Refusal to make the correction | `reject` | `no-promotion` |
| FYT-10 | Live price mismatch | `revise-price-claim` | `advertise-25-percent` |
| FYT-11 | Refusal to accept monitoring responsibility | `reject` | `no-promotion` |
| FYT-12 | Comparative claim removed | `approve` | `no-promotion` |

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.
