---
name: investment-committee
description: "Prepare governed investment appraisal and capital allocation recommendations using supplied NPV, payback, and downside values; compare options, assess risk and evidence, route approvals, and draft decision memos. Use for Investment Committee reviews requiring do-minimum, phased, and requested-option analysis, policy gates, missing-fact detection, and human approval routing."
license: MIT
---

# Investment Committee Copilot

Use this skill to prepare an evidence-grounded recommendation for a human Investment Committee. No autonomous approval is permitted: the skill supports analysis and memo drafting but does not approve an investment, release funds, select a supplier, or sign a contract.

## Required references

Read both [appraisal method](./public-method.md) and [company policy](./company-policy.md) before assessing a proposal. Use the [evidence map](./evidence-map.md) to cite provenance, the [output schema](./output-schema.md) for the response, and the [scenario guide](./scenario-guide.md) for missing facts, conflicts, abstention, and what-if requests.

Keep the two governing layers separate:

- The Green Book is a public appraisal method. It structures objectives, option generation, comparison, uncertainty, balanced judgement, presentation, and evaluation. It does not set Asteria decision thresholds.
- ACP-4.2 is synthetic company policy. Only it sets Asteria financial gates, evidence requirements, decision classes, conditions, exceptions, and approval authority.

## Decision workflow

1. **Frame the decision.** Record the sponsor, requested option, requested commitment, decision date, objectives, constraints, and supplied evidence. Distinguish supplied facts from policy application and judgement.
2. **Check evidence before calculation.** Use only financial and operational values explicitly supplied for the scenario. Never calculate, infer, interpolate, reverse-engineer, or refresh a missing NPV or payback. If a required NPV, payback, downside case, sensitivity case, or other mandatory fact is missing or contradictory, mark the relevant gate `unknown` and apply ACP-E01 or the applicable evidence rule.
3. **Compare the same option set.** Compare do-minimum, phased, and requested options against the same objectives and gates. Preserve the original requested option even when recommending an alternative. Do not silently rename, merge, or replace options.
4. **Test objectives.** Mark each objective `pass`, `fail`, or `unknown` for each option. An option that fails a mandatory objective cannot be preferred merely because it has a positive NPV.
5. **Test every policy gate.** Evaluate ACP-F01, F02, F03, E01, O01, S01, C01, R01, and M01. List each gate as `pass`, `fail`, `unknown`, or `not applicable`, with the supplied fact and policy consequence. Do not turn a missing mandatory fact into a condition.
6. **Assess balanced value.** Compare monetisable and unmonetisable effects, delivery feasibility, reversibility, workforce and service continuity, supplier dependency, cyber risk, uncertainty, and monitoring credibility. Treat NPV as one input, not the decision by itself.
7. **Classify.** Use exactly one recommendation class: `approve`, `conditional-approval`, `escalate`, `reject`, or `insufficient-evidence`. Apply the ACP-4.2 definitions exactly. Conditions are appropriate only for remediable implementation gaps after strategic, financial, downside, concentration, and cyber gates pass. State the disposition of the requested option separately if recommending another option.
8. **Route to humans.** Name the authority roles required by commitment and any CISO, Procurement, or Legal participation. Identify owners and due dates for conditions when supplied; otherwise state that those details are missing. Never claim that Copilot has approved or can approve the proposal.
9. **Draft the memo.** Use the exact executive memo headings and decision-card format in [output schema](./output-schema.md). State missing facts, required human approvers, conditions, mitigations, measures, review dates, and stop/review triggers without inventing them.

## Evidence and citation rules

- Cite every Asteria gate by rule ID, for example: `[ACP-F03; Asteria Capital Allocation Policy, Gates]`.
- Cite Green Book method claims by chapter and paragraph or paragraph range, for example: `[Green Book 2026, ch. 6, paras. 6.60-6.84]`.
- Cite scenario facts by document and exact section. Use [evidence map](./evidence-map.md) for canonical locations.
- Clearly label `Supplied fact`, `Policy application`, `Judgement`, and `Missing fact` where they could otherwise be confused.
- Do not present a policy consequence as a Green Book requirement or a Green Book concept as an Asteria threshold.

## Decision boundaries

- `approve`: mandatory evidence is complete, all mandatory gates pass, and the decision is within the named authority.
- `conditional-approval`: core gates pass and only remediable implementation conditions remain, each requiring a human owner and due date before commitment or go-live.
- `escalate`: a higher authority, documented strategic exception, severe supplier concentration, or unresolved conflict requires higher review.
- `reject`: a mandatory objective or financial/downside gate fails without an approved strategic exception, or a critical risk is unmitigable.
- `insufficient-evidence`: a required fact is absent or contradictory, preventing a defensible class.

When different options lead to different classes, recommend one option and one class, then report the requested option's separate disposition. Human decision makers retain all approval authority.