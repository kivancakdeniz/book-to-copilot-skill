# Competition-law merger notification

[Türkçe](../tr/skills/rekabet-birlesme-bildirimi.md)

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

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `RKB-01`

[Control answer](../assets/skills/rekabet-birlesme-bildirimi/outputs/control-1.txt) · [Skill answer](../assets/skills/rekabet-birlesme-bildirimi/outputs/treatment-1.txt) · [Scorecard](../assets/skills/rekabet-birlesme-bildirimi/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/rekabet-birlesme-bildirimi
```

The control run cited 0 of 7 policy rules and the skill run cited 7. Only the skill run stated the exact decision class (`legal-notification-review`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/rekabet-birlesme-bildirimi/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Birleşme ve Devralma Sayılan Haller ve Kontrol Kavramı Hakkında Kılavuz](https://www.rekabet.gov.tr/Dosya/kilavuzlar/birlesme-ve-devralma-sayilan-haller-ve-kontrol-kavrami-hakkinda-kilavuz.pdf) — Rekabet Kurumu |
| Official source (metadata only) | [Birleşme ve Devralma İşlemlerinde Ciro Hesaplanmasına İlişkin Kılavuz](https://www.rekabet.gov.tr/Dosya/bd-ciro-kilavuzu-20260504120128549.pdf) — Rekabet Kurumu |
| Public method summary | `demos/rekabet-birlesme-bildirimi/skill/public-method.md` |
| Synthetic company policy | `demos/rekabet-birlesme-bildirimi/sources/company-policy.md` |
| Synthetic case | `demos/rekabet-birlesme-bildirimi/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/rekabet-birlesme-bildirimi/evaluation/` |
| Portable skill | `demos/rekabet-birlesme-bildirimi/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Business impact at a glance

| Question | Impact |
|---|---|
| What decision is required? | `legal-notification-review` in the base case; `hold-closing` is the recommended hold option |
| What risk becomes visible? | Treating the `met` indicator as a legal conclusion, the `unknown` technology-undertaking status, incomplete counsel routing, and missing version tracking |
| Who decides? | Human Competition Counsel; Finance owns only the precomputed turnover result |
| What does the skill add? | Consistent use of five classes, three options, rule traceability, and an output designed for a 14-point rubric whose execution is pending |
| What does the skill not do? | Provide legal advice or official certification; calculate turnover or thresholds; make a filing decision; file a notification; restructure, sign, or close the transaction |

## How it works

The skill limits two Turkish Competition Authority guidelines through a
metadata-only manifest; it neither redistributes the PDFs nor reproduces the
official text. It separates concise questions about the public method from the
synthetic BKP-1.0 company policy and the synthetic RKB-2608 transaction facts.

In the base case, `met` remains only Finance's precomputed indicator. It is not
a legal conclusion about whether notification is required. The technology-
undertaking status remains `unknown` pending review by human Competition
Counsel, and the closing gate does not open without recorded human direction.
Humans make the final legal and transaction decisions.

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Evaluation

The demo contains exactly 12 locked scenarios, with the answer key kept
separate from the prompt, and a 14-point rubric with explicit anchors for every
dimension. Execution is pending. The rubric is designed to measure the control-
fact inventory, discipline against recalculation, the technology-status
boundary, source traceability, human authority, and the closing gate, as well
as the correct class and option.

This material is for education and governance design. It is not legal advice,
official certification, or authorization to proceed. Authorized humans retain
the final legal decision and all transaction authority.