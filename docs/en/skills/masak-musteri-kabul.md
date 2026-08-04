# AML customer acceptance (MASAK)

<span class="bts-skill-kicker">Financial crime prevention</span>

For **AML, compliance, and onboarding teams**. Routes identity, beneficial-owner, and source-of-funds gaps to human review.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>20</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>8/8</b><span>rule citations</span></li>
  <li><b>12</b><span>locked scenarios</span></li>
</ul>

## What the skill added

The control answer cited 0/8 rule identifiers; the skill answer cited 8/8. The value is not a longer answer. It is a decision record that exposes company policy, evidence gaps, and the human authority boundary together.

Copilot cannot approve, publish, or execute an operational action.

## Decision contract

| Locked expectation | Value |
| --- | --- |
| Decision class | `enhanced-review` |
| Option | `hold-onboarding` |
| Required rules | 8 identifiers |
| Human route | AML Officer · Compliance |

These values are never shown to the model; only the locked scenario and the deterministic scorer use them.

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

[Control answer](../../assets/skills/masak-musteri-kabul/outputs/control-1.txt) · [Skill answer](../../assets/skills/masak-musteri-kabul/outputs/treatment-1.txt) · [Scorecard](../../assets/skills/masak-musteri-kabul/scorecard.json)

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

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Use boundary

This synthetic demo is not professional advice or a production control. Verify the result against the official source and with the authorized human. [Safety & source](../safety.md) explains the data, source, licence, evaluation, and human-authority boundaries.
