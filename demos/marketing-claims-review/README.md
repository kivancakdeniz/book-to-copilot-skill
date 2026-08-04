# Marketing Claims Review Copilot demo

This fictional demo asks whether Lumena Home Energy can release a US digital
launch campaign for Lumena Sense as presented, or approve an evidence-bounded
revision.

The demo is educational and operational, not legal advice. It does not make a
final legal determination. Legal, Compliance, Marketing, and Product Evidence
reviewers retain their assigned authority, and Copilot cannot approve, publish,
pause, or withdraw a campaign.

## Expected baseline behavior

For campaign MC-0204, the skill should return `approve-with-edits` and recommend
`evidence-bounded-campaign`. The original campaign is not approved as presented.
The revision must:

- replace the 30% home-energy-bill claim with the exact bounded 12% pilot result;
- remove six-month payback and every-home claims;
- identify the pilot as Lumena-sponsored;
- place compatibility requirements near the call to action;
- remove the unsupported influencer performance endorsement;
- if a non-performance endorsement remains, disclose `Paid partnership with
  Lumena; device provided` at the start and in the content; and
- match final creative to the approved claim register before release.

Required human participation is Legal, Compliance, the Marketing Director, and
the Product Evidence Owner.

## Structure

```text
sources/       Public-source manifest and fictional Lumena source pack
evaluation/    Cowork prompts, formal prompt, locked rubric, and 12 scenarios
cowork/skill/  Six-file Cowork skill source
presenter/     Setup, prompts, checkpoints, talk track, and objections
```

The FTC PDFs and date-pinned eCFR XML snapshot are not committed. Fetch them from the exact URLs
in `sources/source-manifest.json`, verify their recorded SHA-256 values, and use
only concise attributed method rules. US federal government works are generally
not copyrightable under 17 U.S.C. 105, but third-party material and assets must
be checked separately.

All Lumena names, products, policies, campaign materials, people, evidence, and
values are fictional synthetic data.

Render the 12 answer-key-free formal inputs and their per-input SHA-256 records
from the downstream repository root:

```bash
.venv/bin/python demos/marketing-claims-review/evaluation/render_scenarios.py \
  .local/marketing-claims-rendered
```

The committed `evaluation/render-manifest.json` locks the expected hashes.

Cowork package SHA-256:
`35e0642d1fdf63f3698419d5b014acab4755d9c50c8dad812d459ac86f902e9b`.
