# Discount price claim review

<span class="bts-skill-kicker">E-commerce and consumer law</span>

For **E-commerce, pricing, and compliance teams**. Meets price history and campaign claims in a traceable release decision.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>20</b><span>LLM only</span></li>
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
| Decision class | `revise-price-claim` |
| Option | `advertise-25-percent` |
| Required rules | 7 identifiers |
| Human route | E-commerce Owner · Pricing Owner · Compliance · Legal |

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
| Named option stated | no | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **20 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `FYT-01`

[Control answer](../../assets/skills/indirimli-fiyat-denetimi/outputs/control-1.txt) · [Skill answer](../../assets/skills/indirimli-fiyat-denetimi/outputs/treatment-1.txt) · [Scorecard](../../assets/skills/indirimli-fiyat-denetimi/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/indirimli-fiyat-denetimi
```

The control run cited 0 of 7 policy rules and the skill run cited 7. Only the skill run stated the exact decision class (`revise-price-claim`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/indirimli-fiyat-denetimi/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Fiyat bilgisi içeren reklamlar ile indirimli satış reklamları ve ticari uygulamaları hakkında kılavuz](https://tuketici.ticaret.gov.tr/haberler/fiyat-bilgisi-iceren-reklamlar-ile-indirimli-satis-reklamlari-ve-ticari-uygulamalari-hakkinda-kilavuz-guncellendi) — Ticaret Bakanlığı |
| Public method summary | `demos/indirimli-fiyat-denetimi/skill/public-method.md` |
| Synthetic company policy | `demos/indirimli-fiyat-denetimi/sources/company-policy.md` |
| Synthetic case | `demos/indirimli-fiyat-denetimi/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/indirimli-fiyat-denetimi/evaluation/` |
| Portable skill | `demos/indirimli-fiyat-denetimi/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Use boundary

This synthetic demo is not professional advice or a production control. Verify the result against the official source and with the authorized human. [Safety & source](../safety.md) explains the data, source, licence, evaluation, and human-authority boundaries.
