# Treatment Auto 1

- Host: Microsoft 365 Copilot Cowork
- Model shown by host: Auto
- Condition: `marketing-claims-review-copilot-3` explicitly invoked, reviewed, and shown as loaded
- Attachment: `campaign-brief.md`
- Prompt: `evaluation/chat-only-treatment-installed-prompt.md`
- Run ID: `treatment-auto-1`
- Run started: 2026-08-04 12:30 (Cowork UI)
- Artifact creation: prohibited by prompt; none created

## Raw response

### Decision

`approve-with-edits` (advisory only, for human review). The original claims fail MCS-S01/Q01/U01/D01/I01, but the supplied evidence-bounded campaign contains a supported narrower claim (the exact 12% pilot statement) and every mandatory edit is objectively verifiable before release [MCS-2.1, Decision classes; Evidence Map, Evidence-bounded option].

### Recommended Campaign Option

`evidence-bounded-campaign`.

### Requested Campaign Disposition

The requested `original-campaign` — all six assets released unchanged on 2026-10-01 [MC-0204, Request] — may not proceed as presented. Every objective and endorsement claim exceeds supplied evidence; disclosures fail proximity and modality tests.

### Claim Register

| Claim ID | Channel | Express/Implied Claim | Evidence | Rule | Status | Required Action |
|---|---|---|---|---|---|---|
| MC-0204-01 | Hero, paid social | “Save 30% on home energy bills” — express quantified; implies whole-home bills | PE-01 median 12% HVAC electricity, not bills | MCS-S01, MCS-Q01 | fail | Replace with bounded 12% pilot statement |
| MC-0204-02 | Landing page | “Pays for itself in six months” — payback/ROI | PE-01 did not measure payback | MCS-S01, MCS-Q01 | fail | Remove |
| MC-0204-03 | Display, product page | “Works in every home” — universal/absolute | PE-02 lists requirements + exclusions | MCS-U01 | fail | Remove; show compatibility near CTA |
| MC-0204-04 | Video, landing page | “Independent pilot proves the savings” — independence | PE-01 Lumena-sponsored, no independent replication | MCS-S01, MCS-D01 | fail | State sponsorship; remove “independent” |
| MC-0204-05 | Paid influencer | “My energy bill dropped 35% in eight weeks” — quantified endorsement, implies typical | PE-03 records 18% HVAC, no typical-results | MCS-Q01, MCS-I01 | fail | Remove performance claim |
| MC-0204-06 | Influencer disclosure | “#LumenaPartner” after collapsed “more”; none on image/video — material connection | MC-0204 item 5; PE-03: $5,000 + free device | MCS-D01, MCS-I01 | fail | “Paid partnership with Lumena; device provided” at start + in content |
| MC-0204-07 | Landing-page footnote | “Results vary. Based on an 8-week pilot.” at page bottom — qualification | MC-0204 item 6, placed away from headlines | MCS-D01 | fail | Place with the claim it qualifies |

### Evidence

Supplied facts: PE-01 (median 12% HVAC electricity, 120 self-selected US homes, 8 weeks, weather-adjusted baseline; Lumena-sponsored, no independent replication); PE-02 (HVAC/Wi-Fi/install requirements; oil boiler, line-voltage, multi-zone hydronic exclusions); PE-03 (Ava Reed 18% HVAC; $5,000 + free device) [Lumena Sense Pilot Evidence Register].

Synthetic policy: MCS-C01, S01, Q01, U01, D01, I01, A01, R01, M01 [MCS-2.1].

Public method (separate): FTC Rules of the Road; .com Disclosures; Endorsement Guides 16 CFR 255 — identify messages, test pre-dissemination substantiation, keep disclosures prominent/proximate/modality-matched, disclose material connections. Method only; not policy or a legal conclusion.

### Required Edits and Disclosures

Replace MC-0204-01 with the exact bounded 12% statement; remove MC-0204-02 and MC-0204-03; state Lumena sponsorship and no independent replication (MC-0204-04); show compatibility requirements/exclusions close to the CTA; remove Ava Reed's performance claim (MC-0204-05); if a non-performance endorsement remains, place “Paid partnership with Lumena; device provided” clearly at the start and in image/video content (MC-0204-06); reposition the qualification with its claim (MC-0204-07); match final creative to an approved register [Evidence Map, Evidence-bounded option; MC-0204].

### Missing Information

- Whole-home bill, payback, and every-home data — absent; blocks MC-0204-01/02/03 (MCS-Q01, U01); owner: Product Evidence Owner.
- Typical-results analysis for endorsements — absent; blocks MC-0204-05 (MCS-I01, Q01).
- Independent replication — absent; blocks MC-0204-04.
- Monitoring owner, review date, correction/stop trigger — not supplied (unknown).

### Required Human Reviewers

Under MCS-A01, quantified, universal, and paid-endorsement claims trigger the highest route: Legal and Compliance participation, plus Marketing Director and Product Evidence Owner. Copilot has no approval, publication, correction, stop, withdrawal, or legal-determination authority.

### Release Controls and Monitoring

Gates (MCS-R01): no release before an approved claim register and verified final-creative match.

Monitoring (MCS-M01): channel inventory (supplied) — paid social, influencer content, video, display, product page, landing page. Owner: unknown. Review date: unknown. Correction/stop trigger: unknown.

### Limits

This review uses only supplied evidence, invents no calculations, thresholds, or authority, and separates FTC public method from synthetic MCS-2.1 policy. It is advisory, not legal advice or a final legal conclusion; all decisions and actions remain with human reviewers.

### Compact Review Card

| Field | Entry |
|---|---|
| Decision | approve-with-edits; advisory only |
| Campaign option | evidence-bounded-campaign |
| Requested campaign | Original — may not proceed as presented |
| Failed/unknown claims | MC-0204-01–07 fail (S01, Q01, U01, D01, I01) |
| Evidence | PE-01, PE-02, PE-03; MC-0204 |
| Required edits | Bounded 12% statement; remove payback/every-home; sponsorship; compatibility at CTA; remove Ava Reed performance; endorsement disclosure at start + in content; reposition footnote |
| Human route | Legal, Compliance, Marketing Director, Product Evidence Owner |
| Release and monitoring | Register + creative-match gates; owner/review date/trigger unknown |