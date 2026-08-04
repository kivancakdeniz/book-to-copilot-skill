# Occupational health and safety risk assessment: from change to commissioning gate

[Türkçe](../tr/skills/isg-risk-degerlendirme.md)

## LLM only vs LLM + skill: expected difference

| Brief-only LLM | Compiled skill |
|---|---|
| May produce an open-ended narrative or an incomplete checklist | Structures the review around the allowed decision classes, three options, and rule IDs |
| May fill evidence gaps with assumptions | Keeps unsupported facts `bilinmiyor` and routes them to the human decision owner |
| May offer a general compliance or operational recommendation | Applies an explicit commissioning, operation, or closure gate |

This comparison is a design hypothesis only. Cowork A/B evaluation has not yet
been run for these 10 new skills. No ROI, production-performance, or model-impact
claim is made.

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

- [Microsoft 365 Copilot Cowork skill](../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [GitHub Copilot for VS Code package](../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Scout package](../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub harness package](../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup package](../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

!!! warning "Copilot Studio classic setup"

    The classic setup ZIP is guided manual setup material, not a directly
    importable skill, agent, or solution, and it does not lock runtime behaviour.
    A human must review and configure its instructions, knowledge sources,
    connections, permissions, and publishing settings separately in the target
    environment.

## Evaluation status

The demo defines exactly 12 locked scenarios, five decision classes, three
options, and a maximum 14-point rubric with every score level anchored. Formal
scenario execution and human review are still pending; no evaluation result is
claimed. The frozen prompt prohibits inventing evidence, people, dates,
thresholds, or authority, and prohibits producing out-of-chat artefacts or
performing operational actions.
