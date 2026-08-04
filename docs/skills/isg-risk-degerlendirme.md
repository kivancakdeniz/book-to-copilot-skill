# Occupational health and safety risk assessment: from change to commissioning gate

[Türkçe](../tr/skills/isg-risk-degerlendirme.md)

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

[Control answer](../assets/skills/isg-risk-degerlendirme/outputs/control-1.txt) · [Skill answer](../assets/skills/isg-risk-degerlendirme/outputs/treatment-1.txt) · [Scorecard](../assets/skills/isg-risk-degerlendirme/scorecard.json)

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

## Scenario

A fictional warehouse plans to add a robot to an existing palletising cell. The
current risk assessment predates the change, and the record does not provide
evidence of operator or maintenance participation, guarding verification, or
energy-isolation controls. The business nevertheless requests production
commissioning.

The skill prepares a traceable review for human decision-makers rather than
automating the decision. The locked baseline result is `renew-assessment`, and
the recommended option is `hold-commissioning`.

## Business impact

The review turns an informal request to start production into an evidence-led
commissioning gate. It makes unresolved hazards, missing participation,
unverified controls, accountable owners, and follow-up triggers visible before
authorised people decide whether work may proceed. The expected value is better
decision consistency and earlier identification of gaps; it is not a measured
financial benefit or ROI claim.

## Metrics to measure

- Exact match for the required decision class and option.
- Recall of the rule IDs required by the scenario.
- Number of unsupported factual or authority claims.
- Correct preservation of human decision and action boundaries.
- Coverage of participation, control, ownership, commissioning, and monitoring gates.
- Response length, measured alongside completeness rather than as a standalone success metric.

## What is reviewed

- Whether the proposed change is within the scope of the current risk assessment.
- Whether operator, maintenance, and worker-representative participation is evidenced.
- Whether guarding, access, and lockout/tagout controls have been verified.
- Whether each open finding has a named human owner, action, and due date.
- Whether the commissioning gate and incident or change-monitoring triggers are explicit.

## Human authority and use boundary

The output is not legal, engineering, or medical advice, and it is not an
engineering certification. Copilot does not approve the assessment, make the
committee decision, commission equipment, or stop work. Authorised people own
the final decision and carry out every operational action.

## Source approach

The public method source is the
[Occupational Health and Safety Risk Assessment Regulation](https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm)
published in the Official Gazette of the Republic of Türkiye. The snapshot
SHA-256 is
`a1ab5bfc1ea7c305393d7fa75f33d7a7debaf97fe3a6e46cc5d4dfb9276a31dc`,
accessed on `2026-08-04`. The external source is distributed as metadata only;
the skill contains a short, cited method summary rather than long copied
passages. A human must verify the current text and reuse conditions against the
official source.

The company policy, case, roles, and all operational records are synthetic.

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.

## Evaluation status

The demo defines exactly 12 locked scenarios, five decision classes, three
options, and a maximum 14-point rubric with every score level anchored. Formal
scenario execution and human review are still pending; no evaluation result is
claimed. The frozen prompt prohibits inventing evidence, people, dates,
thresholds, or authority, and prohibits producing out-of-chat artefacts or
performing operational actions.
