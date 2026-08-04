# İndirimli fiyat denetimi

[Türkçe](../tr/skills/indirimli-fiyat-denetimi.md)

## Expected difference: LLM only vs LLM + skill

| Brief-only large language model (LLM) | Compiled skill |
|---|---|
| May produce free-form prose and an incomplete checklist | Structures the review around permitted decision classes, three options, and rule identifiers |
| May fill evidence gaps with assumptions | Keeps missing facts as `bilinmiyor` and routes them to a human decision-maker |
| May provide a general compliance or operational recommendation | Explicitly applies the publication, go-live, transaction, or closure gate |

This comparison is an expected design hypothesis, not an observed result. A
Cowork A/B evaluation has not yet been run for these 10 new skills. Planned
metrics are exact decision and option selection, required-rule recall,
unsupported-claim count, adherence to human authority limits, and response
length. No measured return on investment (ROI) or production-performance claim
is made.


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

- [Cowork skill](../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-cowork.skill)
- [GitHub Copilot for VS Code ZIP](../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-vscode.zip)
- [Scout ZIP](../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-classic-setup.zip)

The classic setup ZIP is not a direct-import package. Its files are setup
materials that a human must apply in a Copilot Studio classic environment.