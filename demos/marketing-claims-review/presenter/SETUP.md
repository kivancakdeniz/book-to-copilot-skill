# Presenter setup

## Requirements

- Microsoft 365 Copilot licence with signed-in Cowork access
- Permission to upload a custom skill
- A clean demo browser profile or window
- The packaged `marketing-claims-review-copilot.skill`
- The fictional `case-brief.md` attachment
- Control and treatment text from `DEMO-PROMPTS.md`

Use synthetic demo data only. Do not substitute a real campaign, influencer,
customer record, legal opinion, or confidential company policy in a public demo.

## Build and inspect the package

From the `book-to-copilot-skill` downstream repository root, use the existing
packager. From the Studio workspace root, first run
`cd projects/book-to-copilot-skill`.

```bash
.venv/bin/python tools/package_cowork_skill.py \
  demos/marketing-claims-review/skill \
  dist/cowork/marketing-claims-review-copilot.skill
```

The package must contain root `SKILL.md` plus exactly five files in `references/`.
Run `.venv/bin/python -m pytest tests/test_marketing_claims_demo.py -q` before
presentation. Do not publish the generated archive as benchmark evidence without
recording its hash.

## Upload the skill

1. Open Microsoft 365 Copilot Cowork.
2. Select **+ -> Customize -> Skills**.
3. Select the arrow beside **Add**, then **Upload skill**.
4. Choose `marketing-claims-review-copilot.skill`.
5. Keep sharing set to **Only you** during rehearsal.
6. Confirm the skill name and all five companion references.
7. Start a fresh conversation after upload or update.

Cowork stores uploaded custom skills in OneDrive. Upload only reviewed packages.

## Control conversation

1. Start a fresh signed-in Cowork conversation.
2. Confirm the custom skill is absent from the conversation workspace.
3. Attach only the fictional `case-brief.md`.
4. Paste the control prompt exactly.
5. Retain the first complete response and record the run conditions.

## Explicit-invocation treatment

1. Start a separate fresh conversation.
2. Attach the identical fictional campaign brief.
3. Paste the treatment prompt exactly.
4. Confirm the skill is visible under **Workspace -> Skills & Plugins**.
5. Retain the first complete response and record the run conditions.

Control versus explicit invocation is a Cowork UX treatment only. It is not a
causal benchmark because skill discovery, host model version, and runtime controls
may not be pinned. Do not rerun until a preferred answer appears. The locked
12-scenario formal benchmark must be run separately with declared model,
parameters, experimental arms, randomized order, and blinded human review.

## Teardown

1. Return skill sharing to **Only you** if changed.
2. Delete the uploaded skill after a one-off external demo.
3. Remove the synthetic files from Cowork and OneDrive when no longer needed.
4. Keep human Legal and Compliance review in every explanation of the workflow.
