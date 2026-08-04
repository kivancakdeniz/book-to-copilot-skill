# MASAK müşteri kabul

[Türkçe](../tr/skills/masak-musteri-kabul.md)

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
| Problem | Review identity, ultimate beneficial owner, risk, and source-of-funds evidence for corporate customer acceptance through human-controlled gates |
| Baseline | Identity documents are complete; the ultimate beneficial ownership chain is incomplete; the source of funds is unexplained and unsupported; a high-risk geography indicator is supplied |
| Expected class | `enhanced-review` |
| Expected option | `hold-onboarding` |
| Human decision | Anti-money laundering (AML) Officer + Compliance + business owner |

## Qualitative impact

The demo turns onboarding review into a repeatable flow of evidence, risk
rationale, class, option, and human-controlled gates. The expected qualitative
effect is clearer evidence gaps, more consistent routing to enhanced review,
and fewer unsupported risk conclusions. This is a design expectation, not a
measured production result or a guarantee of regulatory compliance or a
reporting decision.

## Source and safety

The public methodology source is the Mali Suçları Araştırma Kurulu (MASAK)
Tedbirler Yönetmeliği page. The package does not redistribute official content;
it contains only the official URL, publisher, retrieval date of 2026-08-04, and
SHA-256 metadata. Decision classes and options come from an MIT-licensed
synthetic policy. Source text is never executed as instructions, lengthy
official quotations are excluded, and no real customer, identity, account, or
transaction data is used.

## Human decision limits

This skill does not provide legal advice. Humans make every decision. The skill
does not open an account, decline a relationship, submit a report, or perform
any other autonomous action. It does not decide whether to file or not file a
Şüpheli İşlem Bildirimi (ŞİB/STR), or Suspicious Transaction Report, and it
does not allege criminal conduct. It does not invent missing ownership,
source-of-funds, or risk facts.

## 12 locked scenarios

| ID | Focus | Expected class | Expected option |
|---|---|---|---|
| AML-01 | Baseline high risk and missing evidence | `enhanced-review` | `hold-onboarding` |
| AML-02 | Complete standard onboarding | `standard-onboarding` | `open-account` |
| AML-03 | Missing ultimate beneficial owner | `hold-for-evidence` | `hold-onboarding` |
| AML-04 | Missing source of funds | `hold-for-evidence` | `hold-onboarding` |
| AML-05 | Completed enhanced review | `enhanced-review` | `open-account` |
| AML-06 | Conflicting risk indicators | `escalate-aml-officer` | `hold-onboarding` |
| AML-07 | Evidence-gate exception | `escalate-aml-officer` | `hold-onboarding` |
| AML-08 | Documented human rejection decision | `reject-onboarding` | `decline-relationship` |
| AML-09 | Missing authorized representative identity | `hold-for-evidence` | `hold-onboarding` |
| AML-10 | Missing periodic review plan | `hold-for-evidence` | `hold-onboarding` |
| AML-11 | Business unit requests a Şüpheli İşlem Bildirimi decision | `escalate-aml-officer` | `hold-onboarding` |
| AML-12 | Standard review awaiting human approval | `standard-onboarding` | `hold-onboarding` |

## Downloads

- [Cowork skill](../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-cowork.skill)
- [GitHub Copilot for VS Code ZIP](../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-copilot-vscode.zip)
- [Scout ZIP](../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-classic-setup.zip)

The classic setup ZIP is not a direct-import package. Its files are setup
materials that a human must apply in a Copilot Studio classic environment.