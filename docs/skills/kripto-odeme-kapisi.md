# Crypto payment gateway

[Türkçe](../tr/skills/kripto-odeme-kapisi.md)

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 6 | 6 / 6 |
| Exact decision class stated | no | yes |
| Named option stated | yes | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **40 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `KRP-01`

[Control answer](../assets/skills/kripto-odeme-kapisi/outputs/control-1.txt) · [Skill answer](../assets/skills/kripto-odeme-kapisi/outputs/treatment-1.txt) · [Scorecard](../assets/skills/kripto-odeme-kapisi/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/kripto-odeme-kapisi
```

The control run cited 0 of 6 policy rules and the skill run cited 6. Only the skill run stated the exact decision class (`reject-payment-flow`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/kripto-odeme-kapisi/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Ödemelerde Kripto Varlıkların Kullanılmamasına Dair Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210416-4.htm) — Türkiye Cumhuriyet Merkez Bankası / T.C. Resmî Gazete |
| Public method summary | `demos/kripto-odeme-kapisi/skill/public-method.md` |
| Synthetic company policy | `demos/kripto-odeme-kapisi/sources/company-policy.md` |
| Synthetic case | `demos/kripto-odeme-kapisi/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/kripto-odeme-kapisi/evaluation/` |
| Portable skill | `demos/kripto-odeme-kapisi/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## At a glance

| Field | Value |
|---|---|
| Review question | Assess the product boundary of a checkout flow in which USDT directly completes a merchant purchase |
| Baseline evidence | Crypto is used directly for payment, a payment-service intermediary participates in the flow, and launch has been requested |
| Expected class | `reject-payment-flow` - do not proceed with the payment flow as described |
| Expected option | `remove-crypto-checkout` - remove crypto from the checkout path before reconsidering launch |
| Human decision | Payments Counsel + Compliance + Product |

## Code guide

Scenario IDs such as `KRP-01` are stable evaluation-case identifiers. A
decision class records the review outcome; an option records the permitted
product path that accompanies that outcome.

| Code | Plain-English meaning |
|---|---|
| `reject-payment-flow` | Reject the payment flow as currently described |
| `approve-nonpayment-service` | Permit review to proceed only for a service that does not perform a payment function |
| `revise-product-boundary` | Change the product boundary before another launch review |
| `hold-for-flow-evidence` | Pause the review until the transaction flow is documented |
| `escalate-payments-counsel` | Send the unresolved scope question to Payments Counsel |
| `remove-crypto-checkout` | Remove crypto from checkout |
| `launch-current-flow` | Allow the documented non-payment flow to follow the human launch process |
| `redesign-nonpayment-service` | Redesign the feature so that it remains outside the payment flow |

## Business targets and metrics to measure

The demo is designed to turn a fragmented product discussion into a traceable
record of the asset, function, intermediary, settlement path, decision, and
launch gate. These are targets, not measured outcomes.

| Target | Metric to measure |
|---|---|
| Identify product-boundary issues earlier | Review stage at which the relevant flow issue is first recorded |
| Reduce late product rework | Number and timing of flow changes requested after launch review begins |
| Give human decision-makers a consistent evidence packet | Required evidence fields completed, missing fields marked `unknown`, and source-to-rule traceability |
| Keep the system within its delegated role | Unsupported claims and actions attempted outside the human authority boundary |

## Sources and safety

The public method source is the TCMB regulation published in the Official
Gazette of the Republic of Turkiye. The package does not redistribute the
official text. It carries only the official URL, publisher, access date of
2026-08-04, SHA-256 digest, and reuse notice. The skill uses a short, cited
method summary rather than copying the regulation. Decision classes and options
come from the synthetic, MIT-licensed Kurgusal Odeme policy.

## Human and scope boundary

This skill does not provide legal advice or make a legal determination.
Payments Counsel, Compliance, and Product decide whether and how the product may
proceed. Copilot does not approve a launch, initiate a payment or transfer,
change the product, or stop a service. The review is limited to the supplied
checkout flow; it does not reach conclusions about investment or transfer
questions outside that evidence.

## 12 locked scenarios - evaluation pending

| ID | Focus | Expected class | Expected option |
|---|---|---|---|
| KRP-01 | Direct USDT merchant payment | `reject-payment-flow` | `remove-crypto-checkout` |
| KRP-02 | Non-payment market-information display | `approve-nonpayment-service` | `launch-current-flow` |
| KRP-03 | Crypto removed from checkout | `revise-product-boundary` | `remove-crypto-checkout` |
| KRP-04 | Missing settlement or conversion evidence | `hold-for-flow-evidence` | `remove-crypto-checkout` |
| KRP-05 | Unknown intermediary role | `hold-for-flow-evidence` | `redesign-nonpayment-service` |
| KRP-06 | Transfer separated from merchant purchase | `escalate-payments-counsel` | `redesign-nonpayment-service` |
| KRP-07 | Static educational content | `approve-nonpayment-service` | `redesign-nonpayment-service` |
| KRP-08 | Direct merchant transfer without an intermediary | `reject-payment-flow` | `remove-crypto-checkout` |
| KRP-09 | Request for an investment-suitability view | `escalate-payments-counsel` | `redesign-nonpayment-service` |
| KRP-10 | Conflicting versions of the transaction flow | `hold-for-flow-evidence` | `remove-crypto-checkout` |
| KRP-11 | TRY checkout with separate analytics | `revise-product-boundary` | `redesign-nonpayment-service` |
| KRP-12 | Payment functionality added again | `reject-payment-flow` | `remove-crypto-checkout` |

These scenarios define the expected answer key. They have not yet produced
comparative performance results.

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.
