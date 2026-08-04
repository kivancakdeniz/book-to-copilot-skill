# Presenter setup

## Requirements

- Microsoft 365 Copilot licence with Cowork access
- Permission to upload a custom skill
- A clean demo browser profile or window
- The versioned `investment-committee-copilot.skill` release artifact
- `case-brief.md`
- The control prompt from `evaluation/chat-only-prompt.md`
- The treatment prompt from `evaluation/chat-only-treatment-prompt.md`

No repository clone, Python installation, connector, or Azure resource is
required for the live Cowork demo.

## Upload the skill

1. Open Microsoft 365 Copilot Cowork.
2. Select **+ → Customize → Skills**.
3. Select the arrow beside **Add**, then **Upload skill**.
4. Choose `investment-committee-copilot.skill`.
5. Review the trusted-source reminder.
6. Keep sharing set to **Only you** during rehearsal.
7. Open the skill detail page and confirm:
   - name: Investment Committee Copilot;
   - description mentions capital allocation and investment appraisal;
   - five companion reference files are present.
8. Start a new conversation after upload or update.

Cowork stores uploaded custom skills in OneDrive. Do not upload a skill from an
untrusted source.

## Prepare the control conversation

1. Start a fresh Cowork conversation.
2. Confirm that `investment-committee-copilot` is absent from the conversation.
3. Attach only `case-brief.md`.
4. Paste `chat-only-prompt.md` without editing it.
5. Save the first complete response as the control output.

## Prepare the treatment conversation

1. Start a second fresh Cowork conversation.
2. Attach the same `case-brief.md`.
3. Paste `chat-only-treatment-prompt.md` without editing it.
4. Confirm that the custom skill appears under **Workspace → Skills & Plugins**.
5. Save the first complete response as the treatment output.

Do not rerun until a preferred answer appears. Record every run or declare the
run invalid for a documented operational reason.

Record every attempt in `evidence/metadata/cowork-runs.json`. Host conversation
IDs stay in ignored local audit data and are not published.

## Teardown

1. Return skill sharing to **Only you** if changed.
2. Delete the custom skill after a one-off external demonstration.
3. Remove synthetic demo files from the Cowork conversation and OneDrive if the
   presenter does not need them.
4. Never use a real customer policy or proposal in the public demo.