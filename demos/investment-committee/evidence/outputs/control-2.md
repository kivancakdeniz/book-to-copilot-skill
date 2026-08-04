# Control 2

- Host: Microsoft 365 Copilot Cowork
- Model shown by host: Claude Opus 4.8
- Condition: custom Investment Committee skill absent
- Attachment: `investment-committee-brief.md` only
- Prompt: `evaluation/chat-only-prompt.md`
- Run ID: `control-2`
- Run started: 2026-08-04 01:12 (Cowork UI)
- Artifact creation: prohibited by prompt; none created

## Raw response

Decision Card — IC-0247, Asteria Distribution Group

Recommended decision class (judgement): Approve a different option. Recommended option (judgement): Phased automation (EUR 3.2m), conditional. Do not approve Full automation as requested; hold it pending evidence rather than reject.

### 1. Objectives & decision gates — pass / fail / unknown

Supplied results: Do minimum fails throughput, accuracy, and safety objectives; phased automation meets all quantified objectives; full automation meets quantified objectives but its required cyber assessment is absent.

| Gate | Do min | Phased | Full |
|---|---|---|---|
| Quantified objectives (throughput/accuracy/safety) | Fail | Pass | Pass |
| Cyber assessment | Pass (complete) | Pass (complete) | Fail (absent) |
| Tested manual fallback | — | Pass (retained) | Fail (none) |
| Approved policy exception | — | n/a | Fail (none) |
| Workforce-training sign-off | — | Unknown (pending) | — |
| NPV hurdle / payback target / safety-incident target / supplier-concentration limit / downside risk appetite | Unknown — no thresholds supplied | | |

Supplied facts behind “unknown”: phased's final workforce-training sign-off is pending before go-live, and full automation has no tested manual fallback and no approved policy exception. The brief supplies no NPV hurdle, payback target, incident target value, or concentration limit, so those gates cannot be scored.

### 2. Evidence supporting the recommendation (supplied facts)

Phased: EUR 3.2m, NPV EUR 1.1m, payback 4.2y, downside NPV EUR 0.2m, largest supplier 45%, cyber evidence complete, meets all quantified objectives — the only option meeting all objectives with complete cyber evidence, a positive downside NPV, and a retained fallback.

Full: EUR 4.8m, NPV EUR 1.6m, downside NPV EUR -0.7m, largest supplier 72%, required cyber assessment absent — the only negative downside NPV, highest supplier concentration, missing cyber evidence and policy exception.

Context: Northstar is forecast to exceed peak capacity in late 2027; order accuracy is 98.9%, manual-handling incidents remain above target, and seasonal labour is volatile. (Judgement: the late-2027 horizon leaves time for a phased path; it does not justify accepting Full's open gates.)

### 3. Information / approvals still required (human action)

- For Phased (before go-live): obtain the pending workforce-training sign-off.
- Before Full could be reconsidered: the completed cyber assessment, an approved policy exception for removing manual fallback, and a tested fallback or explicitly accepted risk.
- IC to confirm against policy (not supplied here): NPV hurdle rate, payback target, safety-incident target, supplier-concentration limit, and appetite for a negative downside NPV.
- IC decision authority to approve the substituted option.

### 4. Conditions, mitigations, monitoring, stop/review

Conditions precedent (Phased): no go-live until the training sign-off is secured.

Mitigations (judgement): retain and periodically exercise the tested manual fallback; keep supplier concentration at the phased level; do not remove fallback without an approved policy exception.

Monitoring measures: throughput against the late-2027 capacity forecast; order accuracy against the 98.9% baseline; manual-handling incidents against target; realised vs. downside NPV; supplier-concentration level.

Stop / review points: (a) if training sign-off is not obtained by a date the IC sets; (b) if incidents rise or accuracy falls after cutover; (c) at the capacity-forecast checkpoint approaching late 2027; (d) re-open Full only once the cyber assessment and policy exception are delivered.

Facts vs. judgement: Sections marked “supplied” and all table figures are from IC-0247. The choice of decision class and option, the mitigations, and the reading that Full's gaps are open are my judgement. I have not invented any calculation, threshold, policy, evidence, or authority; where the brief gives no threshold, the gate is marked unknown for the IC to resolve.
