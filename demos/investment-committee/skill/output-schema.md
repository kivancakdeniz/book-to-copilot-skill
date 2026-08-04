# Output Schema

Use the headings below exactly and in this order. Keep facts, policy application, judgement, and missing information visibly distinct.

# Executive Decision Memo

## Decision

State exactly one class: `approve`, `conditional-approval`, `escalate`, `reject`, or `insufficient-evidence`. Give a one-sentence rationale and make clear that this is a recommendation for human decision.

## Recommended Option

Name exactly one option: `do minimum`, `phased`, or the named `requested option`. Summarise why it is preferred across objectives, value, risk, and evidence.

## Requested Option Disposition

Restate the original requested option and commitment. State whether it is recommended, rejected, escalated, or cannot be decided, and why. Do not rewrite the request to match an alternative.

## Objectives and Gate Results

Use a table:

| Objective or gate | Status | Supplied fact | Policy or method application | Citation |
|---|---|---|---|---|
| Named objective or ACP rule | pass / fail / unknown / not applicable | Value or evidence supplied | Consequence or judgement | Rule ID and source reference |

Include every objective and ACP-F01, F02, F03, E01, O01, S01, C01, R01, and M01. Explain any `unknown` or `not applicable` status.

## Evidence

List the decisive supplied facts and their exact source sections. Separate public-method support from synthetic-policy support.

## Missing Information

List each absent or conflicting fact, why it matters, the affected rule, and who must provide or resolve it. Write `None identified from supplied materials` only when justified.

## Required Human Approvers

Name the minimum authority roles from the commitment matrix and any required CISO, Procurement, or Legal participants. State that Copilot has no approval authority.

## Conditions and Mitigations

For each valid condition, state the action, human owner, due date or timing boundary, evidence of completion, and affected rule. Do not convert failed financial/downside gates or missing mandatory evidence into conditions.

## Monitoring Plan and Stop/Review Points

List benefit owner, measure, baseline, target, review date or cadence, and stop/review trigger using supplied facts. Mark unsupplied elements as missing; do not invent numeric triggers or dates.

## Limits

State that the memo uses supplied values without recalculation, identifies rather than fills evidence gaps, and is advisory only. Approval, budget release, supplier selection, and contracting remain human actions.

## Compact decision card

Use this after the memo when a short summary is requested:

| Field | Entry |
|---|---|
| Decision | One permitted class; human recommendation only |
| Recommended option | One option |
| Requested option | Original option and separate disposition |
| Decisive gates | Rule IDs with pass/fail/unknown |
| Key evidence | Supplied values and exact source sections |
| Missing facts | Required unresolved facts or `None identified` |
| Human route | Minimum authority plus required participants |
| Conditions | Owner, timing boundary, completion evidence |
| Review/stop | Supplied measures, review points, and triggers |