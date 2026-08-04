# OHS risk assessment: from change to commissioning gate

<span class="bts-skill-kicker">Occupational health and safety</span>

For **OHS, operations, maintenance, and engineering teams**. Makes change risk visible through participation, control, and commissioning evidence.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>40</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>7/7</b><span>rule citations</span></li>
  <li><b>12</b><span>locked scenarios</span></li>
</ul>

## What the skill added

The control answer cited 0/7 rule identifiers; the skill answer cited 7/7. The value is not a longer answer. It is a decision record that exposes company policy, evidence gaps, and the human authority boundary together.

Copilot cannot approve, publish, or execute an operational action.

## Decision contract

| Locked expectation | Value |
| --- | --- |
| Decision class | `renew-assessment` |
| Option | `hold-commissioning` |
| Required rules | 7 identifiers |
| Human route | İşveren · İSG profesyonelleri · çalışan temsilcileri |

These values are never shown to the model; only the locked scenario and the deterministic scorer use them.

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

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `ISG-01`

[Control answer](../../assets/skills/isg-risk-degerlendirme/outputs/control-1.txt) · [Skill answer](../../assets/skills/isg-risk-degerlendirme/outputs/treatment-1.txt) · [Scorecard](../../assets/skills/isg-risk-degerlendirme/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/isg-risk-degerlendirme
```

The control run cited 0 of 7 policy rules and the skill run cited 7. Only the skill run stated the exact decision class (`renew-assessment`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/isg-risk-degerlendirme/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [İş Sağlığı ve Güvenliği Risk Değerlendirmesi Yönetmeliği](https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm) — T.C. Resmî Gazete |
| Public method summary | `demos/isg-risk-degerlendirme/skill/public-method.md` |
| Synthetic company policy | `demos/isg-risk-degerlendirme/sources/company-policy.md` |
| Synthetic case | `demos/isg-risk-degerlendirme/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/isg-risk-degerlendirme/evaluation/` |
| Portable skill | `demos/isg-risk-degerlendirme/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Use boundary

This synthetic demo is not professional advice or a production control. Verify the result against the official source and with the authorized human. [Safety & source](../safety.md) explains the data, source, licence, evaluation, and human-authority boundaries.
