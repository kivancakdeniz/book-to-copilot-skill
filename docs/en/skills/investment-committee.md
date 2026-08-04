# Investment committee appraisal

<span class="bts-skill-kicker">Capital allocation</span>

For **CFO, COO, CIO, and investment committee members**. Turns a capital brief into a gated, evidence-cited committee decision card.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>40</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>6/6</b><span>rule citations</span></li>
  <li><b>12</b><span>locked scenarios</span></li>
</ul>

## What the skill added

The control answer cited 0/6 rule identifiers; the skill answer cited 6/6. The value is not a longer answer. It is a decision record that exposes company policy, evidence gaps, and the human authority boundary together.

Copilot cannot approve, publish, or execute an operational action.

## Decision contract

| Locked expectation | Value |
| --- | --- |
| Decision class | `conditional-approval` |
| Option | `phased-automation` |
| Required rules | 6 identifiers |
| Human route | Investment Committee |

These values are never shown to the model; only the locked scenario and the deterministic scorer use them.

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

Host: Microsoft 365 Copilot Cowork · Model: Claude Opus 4.8 · Captured: 2026-08-04 · Scenario: `IC-01`

[Control answer](../../assets/skills/investment-committee/outputs/control-1.txt) · [Skill answer](../../assets/skills/investment-committee/outputs/treatment-1.txt) · [Scorecard](../../assets/skills/investment-committee/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/investment-committee
```

The control run cited 0 of 6 policy rules and the skill run cited 6. Only the skill run stated the exact decision class (`conditional-approval`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/investment-committee/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [The Green Book - UK government guidance on appraisal](https://assets.publishing.service.gov.uk/media/698dbcd17da91680ad7f4308/The_Green_Book_2026.pdf) — HM Treasury and Government Finance Function |
| Public method summary | `demos/investment-committee/skill/public-method.md` |
| Synthetic company policy | `demos/investment-committee/sources/company-policy.md` |
| Synthetic case | `demos/investment-committee/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/investment-committee/evaluation/` |
| Portable skill | `demos/investment-committee/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../../downloads/skills/investment-committee/investment-committee-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/investment-committee/investment-committee-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/investment-committee/investment-committee-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/investment-committee/investment-committee-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/investment-committee/investment-committee-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Use boundary

This synthetic demo is not professional advice or a production control. Verify the result against the official source and with the authorized human. [Safety & source](../safety.md) explains the data, source, licence, evaluation, and human-authority boundaries.
