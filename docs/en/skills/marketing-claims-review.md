# Marketing claims review

<span class="bts-skill-kicker">Marketing and advertising compliance</span>

For **Marketing, legal, and compliance teams**. Checks advertising claims against substantiation, disclosure, and release controls.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>40</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>9/9</b><span>rule citations</span></li>
  <li><b>12</b><span>locked scenarios</span></li>
</ul>

## What the skill added

The control answer cited 0/9 rule identifiers; the skill answer cited 9/9. The value is not a longer answer. It is a decision record that exposes company policy, evidence gaps, and the human authority boundary together.

Copilot cannot approve, publish, or execute an operational action.

## Decision contract

| Locked expectation | Value |
| --- | --- |
| Decision class | `approve-with-edits` |
| Option | `evidence-bounded-campaign` |
| Required rules | 9 identifiers |
| Human route | Legal · Compliance |

These values are never shown to the model; only the locked scenario and the deterministic scorer use them.

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 9 | 9 / 9 |
| Exact decision class stated | no | yes |
| Named option stated | yes | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **40 / 100** | **100 / 100** |

Host: Microsoft 365 Copilot Cowork · Model: Claude Opus 4.8 · Captured: 2026-08-04 · Scenario: `MC-01`

[Control answer](../../assets/skills/marketing-claims-review/outputs/control-1.txt) · [Skill answer](../../assets/skills/marketing-claims-review/outputs/treatment-auto-1.txt) · [Scorecard](../../assets/skills/marketing-claims-review/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/marketing-claims-review
```

The control run cited 0 of 9 policy rules and the skill run cited 9. Only the skill run stated the exact decision class (`approve-with-edits`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/marketing-claims-review/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Advertising and Marketing on the Internet: Rules of the Road](https://www.ftc.gov/system/files/ftc_gov/pdf/bus28-rulesroad-2023_508.pdf) — U.S. Federal Trade Commission |
| Official source (metadata only) | [.com Disclosures: How to Make Effective Disclosures in Digital Advertising](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf) — U.S. Federal Trade Commission |
| Official source (metadata only) | [Guides Concerning the Use of Endorsements and Testimonials in Advertising (16 CFR Part 255)](https://www.ecfr.gov/api/versioner/v1/full/2023-07-26/title-16.xml?part=255) — Electronic Code of Federal Regulations |
| Public method summary | `demos/marketing-claims-review/skill/public-method.md` |
| Synthetic company policy | `demos/marketing-claims-review/sources/company-policy.md` |
| Synthetic case | `demos/marketing-claims-review/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/marketing-claims-review/evaluation/` |
| Portable skill | `demos/marketing-claims-review/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../../downloads/skills/marketing-claims-review/marketing-claims-review-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Use boundary

This synthetic demo is not professional advice or a production control. Verify the result against the official source and with the authorized human. [Safety & source](../safety.md) explains the data, source, licence, evaluation, and human-authority boundaries.
