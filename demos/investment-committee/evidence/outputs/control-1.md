# Control 1

- Host: Microsoft 365 Copilot Cowork
- Model shown by host: Claude Opus 4.8
- Condition: custom Investment Committee skill absent
- Attachment: `investment-committee-brief.md` only
- Prompt: `evaluation/chat-only-prompt.md`
- Run ID: `control-1`
- Run started: 2026-08-04 01:07 (Cowork UI)
- Artifact creation: prohibited by prompt; none created

## Raw response

Executive Decision Card — IC-0247, Asteria Distribution Group

Requested: Approve EUR 4.8 million for full warehouse automation, sponsored by the Chief Operations Officer, decision date 2026-09-15.

Recommended decision class (judgement): Approve a different option — not as requested. Recommended option (judgement): Phased automation, approved conditionally pending one outstanding sign-off.

### 1. Objectives & decision gates

| Gate | Do minimum | Phased | Full |
|---|---|---|---|
| Quantified objectives (throughput, accuracy, safety) | Fail (supplied) | Pass (supplied) | Pass (supplied) |
| Cyber-security evidence | Pass | Pass | Fail — absent |
| Tested manual fallback / continuity | n/a | Pass | Fail — none |
| Policy exception (for removing fallback) | n/a | n/a | Fail — none approved |
| Downside NPV | EUR 0.0m | EUR +0.2m | EUR -0.7m |
| Workforce-training sign-off | — | Unknown — pending | — |

Supplied basis: Do minimum fails throughput, accuracy and safety objectives; phased automation meets all quantified objectives with cyber evidence complete; full automation meets quantified objectives but its required cyber assessment is absent, with downside NPV of EUR -0.7m and a 72% largest-supplier share. Phased retains a tested manual fallback but its final workforce-training sign-off is pending before go-live; full automation has no tested manual fallback and no approved policy exception.

Full automation cannot pass its gates as submitted (judgement): the cyber assessment, the fallback, and the policy exception are all absent, and its downside NPV is the only negative one.

### 2. Evidence supporting the recommendation

All supplied facts:

- Phased automation meets all quantified objectives, NPV EUR 1.1m, payback 4.2y, downside NPV EUR 0.2m, largest supplier 45%, cyber evidence complete.
- Phased automation retains a tested manual fallback.
- Northstar is forecast to exceed current peak capacity in late 2027, order accuracy is 98.9%, manual-handling incidents remain above target, and the full-automation proposal concentrates delivery with one supplier and removes most manual fallback.

Judgement: Phased is the only option that both clears every stated gate and delivers positive value under the downside case, while preserving continuity and lower supplier concentration ahead of the late-2027 capacity constraint.

### 3. Information / approvals still required

To proceed with Phased (condition): final workforce-training sign-off before go-live (supplied as pending).

Only if the Committee still wishes to pursue Full: the required cyber-security assessment, an approved policy exception for removing manual fallback, and a re-examination of the negative downside NPV — all currently absent (supplied). Judgement: obtaining these is prerequisite; it is not within my authority to waive them.

### 4. Conditions, mitigations, monitoring, stop/review

Conditions (judgement, anchored to supplied facts):

- Withhold go-live until the pending workforce-training sign-off is obtained.
- Retain and periodically test the manual fallback throughout ramp-up.

Mitigations (judgement):

- Maintain the 45% supplier position rather than accepting 72% concentration.
- Preserve manual-handling capacity to protect the 98.9% accuracy baseline during transition.

Monitoring (judgement):

- Track throughput against the late-2027 capacity forecast, order accuracy against the 98.9% baseline, and manual-handling incidents against target.
- Confirm cyber evidence remains current.

Stop / review points (judgement):

- Stop go-live if training sign-off is not secured.
- Review if the capacity forecast, downside NPV, or supplier concentration deteriorate, or if a fallback test fails.

### Required human action

The Investment Committee — with CFO, COO and CIO — must (a) approve phased automation subject to the training sign-off, or (b) if full automation is still preferred, formally direct that the missing cyber assessment and policy exception be produced and re-tabled. I have not invented any figure, threshold, policy, or approval; the recommendation above is judgement, and everything cited is supplied in the brief.
