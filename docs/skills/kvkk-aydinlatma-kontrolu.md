# KVKK Notice Review

[Türkçe](../tr/skills/kvkk-aydinlatma-kontrolu.md)

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 5 | 5 / 5 |
| Exact decision class stated | no | yes |
| Named option stated | no | yes |
| Human approval route named | no | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **10 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `KVK-E01`

[Control answer](../assets/skills/kvkk-aydinlatma-kontrolu/outputs/control-1.txt) · [Skill answer](../assets/skills/kvkk-aydinlatma-kontrolu/outputs/treatment-1.txt) · [Scorecard](../assets/skills/kvkk-aydinlatma-kontrolu/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/kvkk-aydinlatma-kontrolu
```

The control run cited 0 of 5 policy rules and the skill run cited 5. Only the skill run stated the exact decision class (`revise-before-launch`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/kvkk-aydinlatma-kontrolu/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [6698 sayılı Kişisel Verilerin Korunması Kanunu](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf) — Mevzuat Bilgi Sistemi |
| Official source (metadata only) | [Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ](https://www.resmigazete.gov.tr/eskiler/2018/03/20180310-5.htm) — Resmî Gazete |
| Public method summary | `demos/kvkk-aydinlatma-kontrolu/skill/public-method.md` |
| Synthetic company policy | `demos/kvkk-aydinlatma-kontrolu/sources/company-policy.md` |
| Synthetic case | `demos/kvkk-aydinlatma-kontrolu/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/kvkk-aydinlatma-kontrolu/evaluation/` |
| Portable skill | `demos/kvkk-aydinlatma-kontrolu/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Business question at a glance

Can a synthetic B2B SaaS lead form go live with its current notice draft and
bundled marketing consent?

## Starting facts

- The form collects a name, business email address, phone number, IP address,
  and campaign source.
- An overseas processor is used; the transfer route and safeguard details are
  missing.
- The draft identifies the data controller, purposes, and collection method.
- Recipient groups, transfer context, legal-basis mapping, and the data
  subject's rights/contact route are missing.
- Marketing consent is tied to acceptance of the notice.

## Expected decision

For the starting case, the decision is `revise-before-launch` and the option is
`separate-notice-and-consent`. The human route is Privacy Counsel + Data
Protection/Compliance + Product Owner.

## Business impact

The demo turns the product team's “do we have text?” check into a traceable
decision based on the data inventory, completeness of the notice, separation of
consent, transfer evidence, and a signed publication gate. The expected impact
is qualitative: earlier visibility of gaps, clearer decision ownership, and
repeatable assessments under the same contract. No measured ROI or financial
gain is claimed.

## Source and licensing boundary

6698 sayılı KVKK and Aydınlatma Tebliği are publicly available official source
materials. The manifest records the official URL, publisher, and SHA-256
metadata retrieved on 2026-08-04; official files are not redistributed under
the `metadata-only` approach, and long passages are not copied. The synthetic
policy and case are MIT-licensed. Human Legal must verify currency, reuse, and
application.

## Safety and human boundary

This content is not legal advice or a final legal conclusion. Human
Legal/Compliance owns the decision. The skill only analyzes, identifies gaps,
and routes the matter; it does not publish, collect consent, transfer data,
change records, or take any other autonomous action. Real personal data must
not be used as demo input.

## 12-scenario readiness

Twelve unique scenarios are ready: they are locked with answer keys and tied to
a 14-point rubric. The scenarios are not presented as run or concluded in this
article; formal execution and human review are still pending.

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.
