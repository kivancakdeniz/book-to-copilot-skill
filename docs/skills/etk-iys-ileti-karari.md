# ETK/IYS Commercial Message Decision

[Türkçe](../tr/skills/etk-iys-ileti-karari.md)

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 4 | 4 / 4 |
| Exact decision class stated | no | no |
| Named option stated | no | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **20 / 100** | **80 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `ETK-E01`

[Control answer](../assets/skills/etk-iys-ileti-karari/outputs/control-1.txt) · [Skill answer](../assets/skills/etk-iys-ileti-karari/outputs/treatment-1.txt) · [Scorecard](../assets/skills/etk-iys-ileti-karari/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/etk-iys-ileti-karari
```

The control run cited 0 of 4 policy rules and the skill run cited 4. The skill run chose a more cautious class than the locked expectation (`do-not-send`), so the class call stays with the human reviewer.

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/etk-iys-ileti-karari/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6563.pdf) — Mevzuat Bilgi Sistemi |
| Official source (metadata only) | [Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2015/07/20150715-4.htm) — Resmî Gazete |
| Public method summary | `demos/etk-iys-ileti-karari/skill/public-method.md` |
| Synthetic company policy | `demos/etk-iys-ileti-karari/sources/company-policy.md` |
| Synthetic case | `demos/etk-iys-ileti-karari/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/etk-iys-ileti-karari/evaluation/` |
| Portable skill | `demos/etk-iys-ileti-karari/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Business question at a glance

Can the CRM team send a discount SMS message to 48,000 former retail customers
without providing current consent/IYS evidence?

## Starting facts

- The message includes a discount and a call to purchase; it is not a service
	notification.
- No current consent or IYS status snapshot has been provided.
- There is no evidence list at the individual-and-SMS-channel level.
- The message includes refusal/opt-out wording.
- No record supporting an exception, suppression gate, or human approval has
	been provided.

## Expected decision

For the starting case, the decision is `do-not-send` and the option is
`suppress-unverified-audience`. The human route is CRM Owner + Compliance +
Legal.

## Business impact

The demo leads the campaign team to review the communication purpose,
individual-channel evidence, refusal checks, exception facts, and the
suppression gate before considering audience size. The expected impact is
qualitative: visibility of the unverified audience, a clearer human decision
route, and repeatable campaign reviews under the same contract. No measured ROI
or financial gain is claimed.

## Source and licensing boundary

6563 sayılı ETK and Ticari İletişim Yönetmeliği are publicly available official
source materials. The manifest records the official URL, publisher, and SHA-256
metadata retrieved on 2026-08-04; official files are not redistributed under
the `metadata-only` approach, and long passages are not copied. The synthetic
policy and case are MIT-licensed. Human Legal must verify currency, reuse, and
application.

## Safety and human boundary

This content is not legal advice or a final legal conclusion. Human
Legal/Compliance owns the decision. The skill only analyzes, identifies gaps,
and routes the matter; it does not send messages, change IYS records, suppress
an audience, start or stop a campaign, or take any other autonomous action.
Real customer lists must not be used as demo input.

## 12-scenario readiness

Twelve unique scenarios are ready: they are locked with answer keys and tied to
a 14-point rubric. The scenarios are not presented as run or concluded in this
article; formal execution and human review are still pending.

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.
