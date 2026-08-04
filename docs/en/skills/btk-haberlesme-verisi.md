# Telecom communication data review

<span class="bts-skill-kicker">Telecom and privacy</span>

For **Telecom compliance, privacy, DPO, and CRM teams**. Bounds location and traffic data use by purpose, consent, and retention gates.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>40</b><span>LLM only</span></li>
  <li><b>80</b><span>LLM + skill</span></li>
  <li><b>7/7</b><span>rule citations</span></li>
  <li><b>12</b><span>locked scenarios</span></li>
</ul>

## What the skill added

The control answer cited 0/7 rule identifiers; the skill answer cited 7/7. The value is not a longer answer. It is a decision record that exposes company policy, evidence gaps, and the human authority boundary together.

Copilot cannot approve, publish, or execute an operational action.

## Decision contract

| Locked expectation | Value |
| --- | --- |
| Decision class | `stop-processing` |
| Option | `consent-first-redesign` |
| Required rules | 7 identifiers |
| Human route | Privacy Counsel · Telecom Compliance · DPO |

These values are never shown to the model; only the locked scenario and the deterministic scorer use them.

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 7 | 7 / 7 |
| Exact decision class stated | no | no |
| Named option stated | yes | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **40 / 100** | **80 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `BTK-01`

[Control answer](../../assets/skills/btk-haberlesme-verisi/outputs/control-1.txt) · [Skill answer](../../assets/skills/btk-haberlesme-verisi/outputs/treatment-1.txt) · [Scorecard](../../assets/skills/btk-haberlesme-verisi/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/btk-haberlesme-verisi
```

The control run cited 0 of 7 policy rules and the skill run cited 7. The skill run chose a more cautious class than the locked expectation (`stop-processing`), so the class call stays with the human reviewer.

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/btk-haberlesme-verisi/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Elektronik Haberleşme Sektöründe Kişisel Verilerin İşlenmesi ve Gizliliğin Korunmasına İlişkin Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2020/12/20201204-13.htm) — Bilgi Teknolojileri ve İletişim Kurumu / T.C. Resmî Gazete |
| Public method summary | `demos/btk-haberlesme-verisi/skill/public-method.md` |
| Synthetic company policy | `demos/btk-haberlesme-verisi/sources/company-policy.md` |
| Synthetic case | `demos/btk-haberlesme-verisi/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/btk-haberlesme-verisi/evaluation/` |
| Portable skill | `demos/btk-haberlesme-verisi/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Use boundary

This synthetic demo is not professional advice or a production control. Verify the result against the official source and with the authorized human. [Safety & source](../safety.md) explains the data, source, licence, evaluation, and human-authority boundaries.
