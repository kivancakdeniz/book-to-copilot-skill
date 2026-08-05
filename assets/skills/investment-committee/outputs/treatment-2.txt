# Treatment 2

- Host: Microsoft 365 Copilot Cowork
- Model shown by host: Claude Opus 4.8
- Condition: `investment-committee-copilot` explicitly invoked and shown as loaded
- Attachment: `investment-committee-brief.md`
- Prompt: `evaluation/chat-only-treatment-prompt.md`
- Run ID: `treatment-2`
- Run started: 2026-08-04 02:06 (Cowork UI)
- Artifact creation: prohibited by prompt; none created

## Raw response

Executive Decision Memo

Recommendation for human decision only — Copilot cannot approve, release funds, select a supplier or sign a contract.

### Decision

`conditional-approval` — core strategic, financial, downside, concentration and cyber gates pass for phased automation; only remediable implementation items remain [Decision classes; ACP-4.2].

### Recommended Option

Phased automation (EUR 3.2m). It meets all quantified objectives with EUR 1.1m risk-adjusted NPV, 4.2-year payback, EUR 0.2m downside NPV and 45% largest-supplier share, with complete cyber evidence, and retains a tested manual fallback. It clears every mandatory financial, evidence, concentration and cyber gate; the open items are remediable before go-live (Judgement).

### Requested Option Disposition

Full automation, EUR 4.8m (as requested) — not recommended, retained unchanged. It has a 5.4-year payback, EUR -0.7m downside NPV, 72% supplier share and an absent required cyber assessment, with no tested manual fallback and no approved policy exception. It fails ACP-F02 and ACP-F03 (reject grounds absent an escalated exception), exceeds 65% concentration (escalate) and lacks the mandatory cyber assessment (insufficient evidence). It cannot be approved as presented.

### Objectives and Gate Results (Phased / Full)

| Item | Phased | Full | Basis |
|---|---|---|---|
| Throughput, accuracy, incident-reduction objectives | pass | pass | Both meet quantified objectives; do-minimum fails all three [IC-0247, Options and supplied facts] |
| ACP-F01 NPV>0 | pass (1.1m) | pass (1.6m) | [ACP-F01; ACP-4.2, Gates] |
| ACP-F02 payback ≤5.0y | pass (4.2y) | fail (5.4y) | [ACP-F02; ACP-4.2, Gates] |
| ACP-F03 downside ≥0 | pass (0.2m) | fail (-0.7m) | [ACP-F03; ACP-4.2, Gates] |
| ACP-E01 base/downside/sensitivity present | pass | pass | Sensitivity covers volume, labour, delay, uptime [ACP-E01; ACP-4.2, Gates] |
| ACP-O01 three options compared | pass | pass | [ACP-O01; ACP-4.2, Gates] |
| ACP-S01 supplier ≤50% | pass (45%) | escalate (72%) | >65% and no mitigation plan [ACP-S01; ACP-4.2, Gates] |
| ACP-C01 OT cyber assessment | pass (complete) | insufficient (absent) | [ACP-C01; ACP-4.2, Gates] |
| ACP-R01 workforce/continuity | condition (sign-off pending; fallback tested) | fail (no tested fallback) | [ACP-R01; ACP-4.2, Gates] |
| ACP-M01 benefit owners/measures | condition (owners assigned; measures, baselines, targets, reviews, triggers not supplied = unknown) | unknown | [ACP-M01; ACP-4.2, Gates] |

### Evidence

Supplied facts: the option comparison table [IC-0247, Options and supplied facts]; phased final training sign-off pending before go-live; assigned benefit owners. Method: balanced value-for-money, not NPV alone [Green Book 2026, ch. 6, paras. 6.93-6.105] — phasing has value under irreversibility [ch. 6, paras. 6.60-6.77].

### Missing Information

- Full-automation OT cyber assessment — absent; blocks ACP-C01; CISO to supply.
- Full-automation 72% supplier mitigation plan — absent; ACP-S01; Procurement/sponsor.
- Phased ACP-M01 detail — measures, baselines, targets, review dates, stop/review triggers not supplied; benefit owners to complete.
- Documented strategic exception for full automation — not supplied.

### Required Human Approvers

Phased EUR 3.2m sits in the EUR 1.0-5.0m band, so Investment Committee: CFO, COO and CIO [Authority matrix]. No CISO/Procurement trigger for phased. Copilot has no approval authority.

### Conditions and Mitigations (phased)

- Final workforce-training sign-off — owner COO, before go-live; signed record [ACP-R01].
- Complete ACP-M01 benefit framework — owner benefit owners, before commitment [ACP-M01].

### Monitoring Plan and Stop/Review Points

Supplied: benefit owners assigned; sensitivity covers volume, labour, delay, uptime. Missing (not invented): measures, baselines, targets, review cadence, stop/review triggers — required by ACP-M01 before go-live. Retain the tested manual fallback as the stop safeguard.

### Limits

Uses supplied values without recalculation; identifies rather than fills gaps; advisory only. Approval, budget release, supplier selection and contracting remain human actions.

### Compact decision card

| Field | Entry |
|---|---|
| Decision | conditional-approval (human recommendation only) |
| Recommended option | Phased automation, EUR 3.2m |
| Requested option | Full automation, EUR 4.8m — not recommended |
| Decisive gates | Phased: F01/F02/F03/E01/O01/S01/C01 pass, R01+M01 conditions. Full: F02 fail, F03 fail, S01 escalate, C01 insufficient |
| Key evidence | [IC-0247, Options and supplied facts]; ACP-4.2 Gates |
| Missing facts | Full cyber assessment; full mitigation plan; phased M01 detail; strategic exception |
| Human route | CFO, COO, CIO (Investment Committee) |
| Conditions | COO training sign-off before go-live; benefit owners complete M01 before commitment |
| Review/stop | M01 measures/targets/triggers to be set; manual fallback retained as stop safeguard |