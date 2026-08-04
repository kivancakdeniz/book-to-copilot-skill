# MASAK müşteri kabul

[Türkçe](../tr/skills/masak-musteri-kabul.md)

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 8 | 8 / 8 |
| Exact decision class stated | no | yes |
| Named option stated | no | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **20 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `AML-01`

[Control answer](../assets/skills/masak-musteri-kabul/outputs/control-1.txt) · [Skill answer](../assets/skills/masak-musteri-kabul/outputs/treatment-1.txt) · [Scorecard](../assets/skills/masak-musteri-kabul/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/masak-musteri-kabul
```

The control run cited 0 of 8 policy rules and the skill run cited 8. Only the skill run stated the exact decision class (`enhanced-review`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/masak-musteri-kabul/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Suç gelirlerinin aklanmasının ve terörün finansmanının önlenmesine dair tedbirler hakkında yönetmelik](https://masak.hmb.gov.tr/suc-gelirlerinin-aklanmasinin-ve-terorun-finansmaninin-onlenmesine-dair-tedbirler-hakkinda-yonetmelik-3/) — MASAK |
| Public method summary | `demos/masak-musteri-kabul/skill/public-method.md` |
| Synthetic company policy | `demos/masak-musteri-kabul/sources/company-policy.md` |
| Synthetic case | `demos/masak-musteri-kabul/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/masak-musteri-kabul/evaluation/` |
| Portable skill | `demos/masak-musteri-kabul/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

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

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.
