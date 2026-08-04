# TİTCK medicinal product promotion: audience and publication gate

[Türkçe](../tr/skills/titck-ilac-tanitimi.md)

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 7 | 7 / 7 |
| Exact decision class stated | no | yes |
| Named option stated | yes | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **40 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `TTK-01`

[Control answer](../assets/skills/titck-ilac-tanitimi/outputs/control-1.txt) · [Skill answer](../assets/skills/titck-ilac-tanitimi/outputs/treatment-1.txt) · [Scorecard](../assets/skills/titck-ilac-tanitimi/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/titck-ilac-tanitimi
```

The control run cited 0 of 7 policy rules and the skill run cited 7. Only the skill run stated the exact decision class (`do-not-publish`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/titck-ilac-tanitimi/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik](https://www.titck.gov.tr/mevzuat/beseri-tibbi-urunlerin-tanitim-faaliyetleri-hakkinda-yonetmelik-27122018172726) — Türkiye İlaç ve Tıbbî Cihaz Kurumu (TİTCK) |
| Official source (metadata only) | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik - Resmî Gazete yayımı](https://www.resmigazete.gov.tr/eskiler/2015/07/20150703-2.htm) — T.C. Resmî Gazete |
| Public method summary | `demos/titck-ilac-tanitimi/skill/public-method.md` |
| Synthetic company policy | `demos/titck-ilac-tanitimi/sources/company-policy.md` |
| Synthetic case | `demos/titck-ilac-tanitimi/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/titck-ilac-tanitimi/evaluation/` |
| Portable skill | `demos/titck-ilac-tanitimi/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Scenario

A consumer-facing Instagram creative is proposed for a fictional prescription
product. It contains the product name, a benefit statement, and a "Ask your
doctor now" call to action. The account is public and has no access control
restricted to healthcare professionals.

The skill prepares a traceable draft for human Medical, Regulatory, and Legal
review instead of taking a publication action. The locked baseline result is
`do-not-publish`, and the recommended option is
`professional-channel-review`. That option does not approve separate
professional material or authorise its publication.

## What is reviewed

- The source supporting the product and prescription status.
- The material's actual audience and channel access, rather than its stated intent.
- Whether product-name, benefit, and call-to-action claims match the supplied approved scope.
- Whether any professional channel is restricted through genuine role verification.
- Whether Medical, Regulatory, and Legal review and the publication gate are recorded.
- Whether the version, channel, human owner, review cycle, and withdrawal triggers are explicit.

## Human authority and use boundary

The output is not legal or medical advice. Copilot does not approve, publish,
target, or remove content, and it does not stop a campaign. Authorised Medical,
Regulatory, Legal, and business owners make the final decision and carry out
every publication or operational action.

## Source approach

The public method is based on two official sources:

- [TİTCK - Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik](https://www.titck.gov.tr/mevzuat/beseri-tibbi-urunlerin-tanitim-faaliyetleri-hakkinda-yonetmelik-27122018172726),
  SHA-256 `552ce8f77c365599105d387e5d9d312998f26df634131faad66201a35ad027d1`.
- [T.C. Resmî Gazete yayımı](https://www.resmigazete.gov.tr/eskiler/2015/07/20150703-2.htm),
  SHA-256 `c23a03d934063bec7abd0a678cf947d2044af82f63d404a59028aaa5421191cf`.

Both sources were accessed on `2026-08-04`. External sources are distributed as
metadata only; the skill contains a short, cited method summary rather than
long copied passages. A human must verify the current text and reuse conditions
against the official sources. The company policy, product, creative, roles, and
all records are synthetic.

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Evaluation status

The demo defines exactly 12 locked scenarios, five decision classes, three
options, and a maximum 14-point rubric with every score level anchored. Formal
scenario execution and human review are still pending; no evaluation result is
claimed. The frozen prompt prohibits inventing product status, medical evidence,
scope, targeting, access, dates, or authority, and prohibits producing
out-of-chat artefacts or performing publication or operational actions.
