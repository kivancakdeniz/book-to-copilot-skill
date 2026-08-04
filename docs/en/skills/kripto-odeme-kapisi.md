# Crypto payment gateway review

<span class="bts-skill-kicker">Payment services and crypto assets</span>

For **Payments, compliance, legal, and product teams**. Reviews the role of crypto in a payment flow against product and launch gates.

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
| Decision class | `reject-payment-flow` |
| Option | `remove-crypto-checkout` |
| Required rules | 6 identifiers |
| Human route | Payments Counsel · Compliance · Product |

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

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `KRP-01`

[Control answer](../../assets/skills/kripto-odeme-kapisi/outputs/control-1.txt) · [Skill answer](../../assets/skills/kripto-odeme-kapisi/outputs/treatment-1.txt) · [Scorecard](../../assets/skills/kripto-odeme-kapisi/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/kripto-odeme-kapisi
```

The control run cited 0 of 6 policy rules and the skill run cited 6. Only the skill run stated the exact decision class (`reject-payment-flow`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/kripto-odeme-kapisi/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Ödemelerde Kripto Varlıkların Kullanılmamasına Dair Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210416-4.htm) — Türkiye Cumhuriyet Merkez Bankası / T.C. Resmî Gazete |
| Public method summary | `demos/kripto-odeme-kapisi/skill/public-method.md` |
| Synthetic company policy | `demos/kripto-odeme-kapisi/sources/company-policy.md` |
| Synthetic case | `demos/kripto-odeme-kapisi/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/kripto-odeme-kapisi/evaluation/` |
| Portable skill | `demos/kripto-odeme-kapisi/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Use boundary

This synthetic demo is not professional advice or a production control. Verify the result against the official source and with the authorized human. [Safety & source](../safety.md) explains the data, source, licence, evaluation, and human-authority boundaries.
