# Scenario Guide

## Baseline scope

The baseline is Investment Committee Brief IC-0247 and the three options in Northstar Warehouse Automation Options. These are synthetic scenario facts, not reusable thresholds.

- **Requested option:** full automation, EUR 4.8 million.
- **Do minimum:** EUR 0.8m commitment; EUR 0.3m risk-adjusted NPV; 3.5-year payback; EUR 0.0m downside NPV; 30% largest-supplier share; cyber complete; fails the throughput, accuracy, and incident-reduction objectives.
- **Phased automation:** EUR 3.2m commitment; EUR 1.1m risk-adjusted NPV; 4.2-year payback; EUR 0.2m downside NPV; 45% largest-supplier share; cyber complete; meets quantified objectives; tested manual fallback and assigned benefit owners; final COO training sign-off pending before go-live.
- **Full automation:** EUR 4.8m commitment; EUR 1.6m risk-adjusted NPV; 5.4-year payback; EUR -0.7m downside NPV; 72% largest-supplier share; required OT cyber assessment absent; no tested manual fallback; no approved policy exception.
- Base and downside assumptions use the same five-year horizon. Supplied sensitivity evidence covers volume, labour availability, implementation delay, and uptime.

Expected baseline behavior is to evaluate all three options against the same objectives and all ACP rules, recommend one class and one option, and state the original full-automation request's disposition separately. A larger NPV must not override objective, downside, payback, cyber, concentration, or evidence results. A pending implementation sign-off may be a condition only where ACP-4.2 permits it.

## Missing facts

When a mandatory fact is absent:

1. Label it `Missing fact`; do not infer it from narrative tone or another metric.
2. Mark the affected gate `unknown`.
3. Cite the evidence rule and explain why the fact is decision-relevant.
4. Name the human role that must supply or validate it when the source identifies that role; otherwise say the owner is not supplied.
5. Use `insufficient-evidence` when the missing fact prevents a defensible class. Do not downgrade mandatory evidence to a post-approval condition.

Missing NPV or payback is never a request to calculate it. Ask for the approved, precomputed value and its evidence.

## Conflicting facts

Do not choose the more convenient value. Show both claims with their sources, mark the affected gate `unknown`, and identify the human owner needed to reconcile the conflict. If the conflict affects a mandatory gate or authority route, abstain with `insufficient-evidence` or use `escalate` only where ACP-4.2 explicitly requires higher review for the unresolved conflict.

## Abstention discipline

Abstention is a governed outcome, not a failure to answer. Use `insufficient-evidence` only when absent or contradictory mandatory evidence blocks classification. Still provide the known pass/fail/unknown gates, the unresolved facts, the evidence needed, and the human route. Do not use abstention to avoid an evidenced reject or escalation.

## What-if discipline

- Change only facts explicitly changed by the user; carry all other supplied facts forward.
- Label changed inputs as `What-if assumption`, not as source facts.
- Do not recalculate NPV, payback, downside NPV, supplier share, or benefits unless the changed value itself is supplied.
- Re-evaluate every affected objective, gate, decision class, authority route, condition, and monitoring implication.
- If a changed fact creates an internal conflict, surface it rather than selecting one version.
- Do not treat a what-if result as approval or as an amendment to company policy.

## Preserve request and recommendation

Always retain the sponsor's original requested option and commitment in the memo. If another option is recommended, report two separate outcomes:

1. the recommendation class and recommended option; and
2. the requested option's disposition with its failed, unknown, or escalated gates.

Never silently transform the requested full option into a phased design, transfer the requested option's financial values to an alternative, or imply that recommending an alternative authorises it. The applicable human authority must decide.