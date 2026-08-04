# Commercial message decision (ETK/IYS)

<span class="bts-skill-kicker">Commercial electronic messaging</span>

For **CRM, compliance, and legal teams**. Reviews a campaign audience against person-channel evidence and a suppression gate.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>20</b><span>LLM only</span></li>
  <li><b>80</b><span>LLM + skill</span></li>
  <li><b>4/4</b><span>rule citations</span></li>
  <li><b>12</b><span>locked scenarios</span></li>
</ul>

## What the skill added

The control answer cited 0/4 rule identifiers; the skill answer cited 4/4. The value is not a longer answer. It is a decision record that exposes company policy, evidence gaps, and the human authority boundary together.

Copilot cannot approve, publish, or execute an operational action.

## Decision contract

| Locked expectation | Value |
| --- | --- |
| Decision class | `do-not-send` |
| Option | `suppress-unverified-audience` |
| Required rules | 4 identifiers |
| Human route | CRM Owner · Compliance · Legal |

These values are never shown to the model; only the locked scenario and the deterministic scorer use them.

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

[Control answer](../../assets/skills/etk-iys-ileti-karari/outputs/control-1.txt) · [Skill answer](../../assets/skills/etk-iys-ileti-karari/outputs/treatment-1.txt) · [Scorecard](../../assets/skills/etk-iys-ileti-karari/scorecard.json)

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

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Use boundary

This synthetic demo is not professional advice or a production control. Verify the result against the official source and with the authorized human. [Safety & source](../safety.md) explains the data, source, licence, evaluation, and human-authority boundaries.
