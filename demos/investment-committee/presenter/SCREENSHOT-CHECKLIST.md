# Screenshot and recording checklist

## Privacy setup

- Use only the fictional Asteria corpus.
- Use a clean browser profile or dedicated demo account.
- Hide tenant, account, email, avatar, notification, recent-file, and chat-history details.
- Close unrelated Microsoft 365 panels and browser tabs.
- Disable OS notification banners.
- Review every image at full resolution before committing or publishing it.

## Required screenshots

1. Customize → Skills before upload
2. Upload skill picker showing only the package filename
3. Skill detail page with name and description
4. Control Workspace with only the brief and no custom skill
5. Frozen investment brief attachment
6. Complete control response
7. Treatment Workspace with the custom skill under Skills & Plugins
8. Loaded-skill panel visible during treatment
9. Treatment decision card and gate table
10. Evidence/provenance section
11. What-if response
12. One-page Word memo preview
13. Human action/approval boundary

## Capture rules

- Keep viewport and zoom consistent between control and treatment.
- Capture the full response as text in addition to screenshots.
- Do not crop away warnings, missing-information sections, citations, or limits.
- Record timestamp, Cowork version/availability state, enabled sources/skills,
  package SHA-256, and run ID in a separate evidence manifest.
- Screenshots illustrate UX; scored raw outputs provide quality evidence.

The canonical manifest is `evidence/metadata/cowork-runs.json`. Host conversation
IDs belong only in ignored local audit data.