# KVKK privacy notice review

<span class="bts-skill-kicker">Data protection</span>

For **Privacy, compliance, and product teams**. Connects notice, consent, and transfer gaps to a human release gate.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>10</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>5/5</b><span>rule citations</span></li>
  <li><b>12</b><span>locked scenarios</span></li>
</ul>

## What the skill added

The control answer cited 0/5 rule identifiers; the skill answer cited 5/5. The value is not a longer answer. It is a decision record that exposes company policy, evidence gaps, and the human authority boundary together.

Copilot cannot approve, publish, or execute an operational action.

## Decision contract

| Locked expectation | Value |
| --- | --- |
| Decision class | `revise-before-launch` |
| Option | `separate-notice-and-consent` |
| Required rules | 5 identifiers |
| Human route | Privacy Counsel · Data Protection/Compliance · Product Owner |

These values are never shown to the model; only the locked scenario and the deterministic scorer use them.

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

[Control answer](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/control-1.txt) · [Skill answer](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/treatment-1.txt) · [Scorecard](../../assets/skills/kvkk-aydinlatma-kontrolu/scorecard.json)

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

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Use boundary

This synthetic demo is not professional advice or a production control. Verify the result against the official source and with the authorized human. [Safety & source](../safety.md) explains the data, source, licence, evaluation, and human-authority boundaries.
