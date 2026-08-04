# Crypto payment gateway

[Türkçe](../tr/skills/kripto-odeme-kapisi.md)

## Expected difference: LLM only vs LLM + skill

| Brief-only LLM | Compiled skill |
|---|---|
| May produce free-form guidance or an incomplete checklist | Structures the review around permitted decision classes, three action options, and rule identifiers |
| May fill evidence gaps with assumptions | Keeps missing facts `unknown` and routes them to the authorized human decision-makers |
| May offer a general compliance or operational recommendation | Applies an explicit gate for launch, payment activity, product revision, or closure |

This comparison is an expected design hypothesis, not an evaluation result. The
Cowork A/B comparison has not been run, and all 12 locked scenarios below are
pending execution and scoring. Metrics to measure are exact decision-class and
option matches, required-rule recall, unsupported-claim count, respect for human
authority boundaries, and response length.

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

- [Cowork skill](../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-cowork.skill)
- [GitHub Copilot for VS Code ZIP](../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-vscode.zip)
- [Scout ZIP](../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-classic-setup.zip)

The classic setup ZIP is not a direct-import package. Its files are setup
materials that a human must apply in a Copilot Studio classic environment.