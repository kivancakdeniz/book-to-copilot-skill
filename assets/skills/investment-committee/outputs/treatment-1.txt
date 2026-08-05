# Treatment 1

- Host: Microsoft 365 Copilot Cowork
- Model shown by host: Claude Opus 4.8
- Condition: `investment-committee-copilot` explicitly invoked and shown as loaded
- Attachment: `investment-committee-brief.md`
- Prompt: `evaluation/chat-only-treatment-prompt.md`
- Run ID: `treatment-1`
- Run started: 2026-08-04 01:19 (Cowork UI)
- Artifact creation: prohibited by prompt; none created

## Raw response

Executive Decision Memo — IC-0247, Asteria Distribution Group

### Decision

`conditional-approval` — of phased automation, not the requested full automation. Core strategic, financial, downside, concentration, and cyber gates pass; only remediable implementation conditions remain. This is a recommendation for human decision; Copilot has no approval authority.

### Recommended Option

Phased automation (EUR 3.2m). Supplied facts: meets all quantified objectives; NPV EUR 1.1m; payback 4.2y; downside NPV EUR 0.2m; 45% supplier share; cyber complete; tested manual fallback; benefit owners assigned [IC-0247, Options and supplied facts]. Judgement: per balanced value-for-money, full automation's larger NPV (EUR 1.6m) does not override its failed downside/payback gates or absent cyber evidence [Green Book 2026, ch. 6, paras. 6.93-6.105]; the tested fallback adds flexibility value where change is hard to reverse [ch. 6, paras. 6.60-6.77]. Do-minimum is excluded — it fails throughput, accuracy, and safety objectives.

### Requested Option Disposition

Original request: full automation, EUR 4.8m — reject as requested. Policy application: fails ACP-F02 (payback 5.4y > 5.0y) and ACP-F03 (downside NPV -EUR 0.7m < 0) with no approved strategic exception; OT cyber assessment absent (ACP-C01 → insufficient evidence); 72% supplier share > 65% (ACP-S01 → escalate); no tested manual fallback. Not converted to phased; only the Committee/Board may authorise any exception.

### Objectives and Gate Results — phased (recommended)

| Item | Status | Supplied fact | Application | Citation |
|---|---|---|---|---|
| Throughput / accuracy / incident objectives | pass | “Meets all quantified objectives” | Mandatory objectives met | [IC-0247, Options] |
| ACP-F01 NPV>0 | pass | EUR 1.1m | Positive | [ACP-F01; ACP-4.2 Gates] |
| ACP-F02 payback ≤5.0y | pass | 4.2y | Within limit | [ACP-F02; Gates] |
| ACP-F03 downside ≥0 | pass | EUR 0.2m | Non-negative | [ACP-F03; Gates] |
| ACP-E01 evidence present/consistent | pass | base, downside, sensitivity supplied | Internally consistent | [ACP-E01; Gates] |
| ACP-O01 3 options vs same objectives | pass | do-min/phased/full | Satisfied | [ACP-O01; Gates] |
| ACP-S01 supplier ≤50% | pass | 45% | Below threshold | [ACP-S01; Gates] |
| ACP-C01 OT cyber assessment | pass | “Complete” | Documented | [ACP-C01; Gates] |
| ACP-R01 workforce/cutover/continuity | condition | training sign-off pending; fallback tested; owners assigned | Remediable gap → condition | [ACP-R01; Gates] |
| ACP-M01 benefit measures/baselines/targets/reviews/stops | unknown (detail) | owners assigned; rest not supplied | Conditional until completed | [ACP-M01; Gates] |

Full-automation contrast: F02 fail, F03 fail, C01 unknown/absent, S01 escalate.

### Evidence

Supplied: per-option NPV, payback, downside, supplier share, cyber status, objective results, and fallback/training notes [IC-0247, Options]. Policy: ACP-4.2 Gates and Authority matrix. Method: NPV is one input, not the rule [Green Book 2026, ch. 6, 6.93-6.105].

### Missing Information / Approvals Required

- M01 monitoring detail — measures, baselines, targets, review dates, stop/review triggers not supplied; owner: assigned benefit owners (names not supplied).
- Phased benefit-owner names not supplied.
- Full option only: OT cyber assessment (CISO), an approved strategic exception for F02/F03, and a manual-fallback plan — all absent.

### Required Human Approvers

Phased EUR 3.2m → Investment Committee: CFO, COO, CIO [ACP-4.2, Authority matrix]. Procurement, CISO, Legal not triggered for phased (45% share, cyber complete, standard terms). Any pursuit of full automation additionally requires CISO (C01), Procurement (>50%), and escalation for >65% concentration. Copilot cannot approve, release budget, select a supplier, or contract.

### Conditions, Mitigations, Monitoring & Stop/Review (phased)

- Condition 1 [ACP-R01]: complete final workforce-training sign-off before go-live — owner COO (per supplied facts) — evidence: signed sign-off.
- Condition 2 [ACP-M01]: complete benefits monitoring pack (measures, baselines, targets, review dates, stop/review triggers) before commitment/go-live — owner: assigned benefit owners — evidence: approved monitoring plan.
- Mitigation: retain the tested manual fallback as continuity/reversibility safeguard.
- Monitoring/stop points: benefit owners assigned (names missing); measures, baselines, targets, cadence, and numeric stop/review triggers not supplied — missing and must be set under Condition 2; none invented here.

### Limits

Uses supplied values without recalculation; identifies rather than fills evidence gaps; advisory only. Approval, budget release, supplier selection, and contracting remain human actions.

### Compact Decision Card

| Field | Entry |
|---|---|
| Decision | conditional-approval — human recommendation only |
| Recommended option | Phased automation (EUR 3.2m) |
| Requested option | Full automation (EUR 4.8m) — reject as requested |
| Decisive gates | Phased: F01/F02/F03/E01/O01/S01/C01 pass; R01, M01 conditions. Full: F02 fail, F03 fail, C01 unknown, S01 escalate |
| Key evidence | [IC-0247, Options and supplied facts]; NPV 1.1m, payback 4.2y, downside 0.2m, 45%, cyber complete, tested fallback |
| Missing facts | M01 monitoring detail; benefit-owner names; (full) cyber assessment, strategic exception, fallback plan |
| Human route | Investment Committee — CFO, COO, CIO |
| Conditions | R01 training sign-off (COO, pre-go-live); M01 monitoring pack (benefit owners, pre-commitment) |
| Review/stop | Owners assigned; measures/targets/triggers not supplied — set under M01 |
