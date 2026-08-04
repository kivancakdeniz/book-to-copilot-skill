# BRSA remote customer onboarding

[Türkçe](../tr/skills/bddk-uzaktan-musteri-edinimi.md)

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

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Captured: 2026-08-04 · Scenario: `BDK-01`

[Control answer](../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/control-1.txt) · [Skill answer](../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/treatment-1.txt) · [Scorecard](../assets/skills/bddk-uzaktan-musteri-edinimi/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/bddk-uzaktan-musteri-edinimi
```

The control run cited 0 of 7 policy rules and the skill run cited 7. The skill run chose a more cautious class than the locked expectation (`reject-flow`), so the class call stays with the human reviewer.

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/bddk-uzaktan-musteri-edinimi/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Bankalarca Kullanılacak Uzaktan Kimlik Tespiti Yöntemlerine ve Elektronik Ortamda Sözleşme İlişkisinin Kurulmasına İlişkin Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210401-7.htm) — Resmî Gazete |
| Public method summary | `demos/bddk-uzaktan-musteri-edinimi/skill/public-method.md` |
| Synthetic company policy | `demos/bddk-uzaktan-musteri-edinimi/sources/company-policy.md` |
| Synthetic case | `demos/bddk-uzaktan-musteri-edinimi/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/bddk-uzaktan-musteri-edinimi/evaluation/` |
| Portable skill | `demos/bddk-uzaktan-musteri-edinimi/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Business impact at a glance

| Question | Impact |
|---|---|
| What decision is required? | `reject-flow` in the base case; `manual-onboarding-fallback` is the recommended fallback option |
| What risk becomes visible? | Evidence gaps concerning live or video interaction, liveness and process integrity, records, and monitoring |
| Who decides? | Human Security, Compliance, and Legal authorities |
| What does the skill add? | Consistent use of five classes, three options, rule traceability, and an output designed for a 14-point rubric whose execution is pending |
| What does the skill not do? | Provide legal advice, official compliance certification, technical certification, go-live approval, or customer transactions |

## How it works

The skill limits the Official Gazette source through a metadata-only manifest;
it neither redistributes nor reproduces the official text. It separates concise
questions about the public method from the synthetic UME-1.0 company policy and
the synthetic UME-2408 case evidence. The output provides one exact decision
class, one exact option, evidence gates, and the required route to human review.

In the base flow, there is no evidence of live or video interaction, liveness
and process integrity, control logs, a monitoring plan, or human approvals.
Direct go-live is therefore not recommended. Every missing field remains
explicitly `unknown`, and the skill does not infer technical certification from
a selfie. Humans make the final decision and authorize every implementation
action.

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Evaluation

The demo contains exactly 12 locked scenarios, with the answer key kept
separate from the prompt, and a 14-point rubric with explicit anchors for every
dimension. Execution is pending. The rubric is designed to measure the method
inventory, evidence discipline, source traceability, human authority, and
go-live and monitoring gates, as well as the correct class and option.

This material is for education and governance design. It is not legal advice,
official certification, or authorization to proceed. Authorized humans retain
the final decision and all implementation authority.