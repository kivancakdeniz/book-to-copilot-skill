# Lumena Marketing Claims Standard MCS-2.1

> Fictional synthetic company policy for the Marketing Claims Review demo. It is
> not legal advice and does not state the law.

## Scope and rules

- **MCS-C01 - Claim inventory.** Inventory every express, implied, and material
  claim in each channel and format before review.
- **MCS-S01 - Evidence basis.** Every objective claim needs a reasonable evidence
  basis before release. Record the evidence owner and exact source.
- **MCS-Q01 - Quantified claims.** A quantified claim must match the evidence's
  metric, population, denominator, time period, conditions, and result. Do not
  extrapolate beyond the measured result.
- **MCS-U01 - Universal and absolute claims.** A universal or absolute claim
  requires evidence covering the represented universe. Otherwise narrow or
  remove it.
- **MCS-D01 - Qualifying disclosures.** A qualifying disclosure must be clear,
  conspicuous, close or unavoidable, and in the same language and modality where
  relevant. It cannot contradict the headline claim.
- **MCS-I01 - Endorsements.** Paid or free-product material connections must be
  disclosed clearly in each endorsement. An endorser cannot exceed the approved
  claim scope.
- **MCS-A01 - Authority.** A subjective communication with no objective claim
  requires the Marketing Director. Objective performance claims require the
  Marketing Director, Product Evidence Owner, and Compliance. Quantified,
  universal, comparative, superlative, and paid-endorsement claims require Legal
  and Compliance participation. Health or safety claims require mandatory Legal
  escalation.
- **MCS-R01 - Release control.** Do not release before the claim register is
  approved and final creative matches it. Copilot cannot approve or publish.
- **MCS-M01 - Monitoring.** Campaign monitoring needs an owner, channel
  inventory, review date, and correction or stop trigger. Missing details remain
  `unknown`; do not invent them.

## Decision classes

Use exactly one class:

- `approve`: supplied materials support the final claims and disclosures, final
  creative matches the approved register, and required human reviewers approve.
- `approve-with-edits`: supported narrower claims exist and every mandatory edit
  is objectively verifiable before release.
- `hold-for-substantiation`: an objective claim may be supportable, but required
  evidence is absent, incomplete, or contradictory.
- `escalate-legal`: a health or safety claim, mandatory legal issue, live-campaign
  risk, or authority route requires Legal determination.
- `reject`: no supportable campaign claim or objectively verifiable revision is
  available, or the proposal depends on a claim contradicted by supplied facts.

Conditions are allowed only when supported narrower claims exist and all
mandatory edits can be verified objectively before release. The approved human
reviewers decide; Copilot provides advisory analysis only and cannot approve,
publish, pause, correct, or withdraw campaign content.
