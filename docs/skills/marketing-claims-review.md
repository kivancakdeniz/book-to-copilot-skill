# Marketing Claims Review Copilot

[Türkçe](../tr/skills/marketing-claims-review.md)

## Decision

Can fictional Lumena Home Energy release its US digital launch campaign for the
Lumena Sense smart HVAC energy controller as presented, or approve an
evidence-bounded revision?

The locked baseline answer is `approve-with-edits` with
`evidence-bounded-campaign`. The original campaign is not approved as presented.
This is an advisory governance demo, not legal advice or a final legal
conclusion. Human Legal, Compliance, Marketing, and Product Evidence reviewers
retain all authority; Copilot cannot approve or publish.

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 9 | 9 / 9 |
| Exact decision class stated | no | yes |
| Named option stated | yes | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **40 / 100** | **100 / 100** |

Host: Microsoft 365 Copilot Cowork · Model: Claude Opus 4.8 · Captured: 2026-08-04 · Scenario: `MC-01`

[Control answer](../assets/skills/marketing-claims-review/outputs/control-1.txt) · [Skill answer](../assets/skills/marketing-claims-review/outputs/treatment-auto-1.txt) · [Scorecard](../assets/skills/marketing-claims-review/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/marketing-claims-review
```

The control run cited 0 of 9 policy rules and the skill run cited 9. Only the skill run stated the exact decision class (`approve-with-edits`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/marketing-claims-review/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [Advertising and Marketing on the Internet: Rules of the Road](https://www.ftc.gov/system/files/ftc_gov/pdf/bus28-rulesroad-2023_508.pdf) — U.S. Federal Trade Commission |
| Official source (metadata only) | [.com Disclosures: How to Make Effective Disclosures in Digital Advertising](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf) — U.S. Federal Trade Commission |
| Official source (metadata only) | [Guides Concerning the Use of Endorsements and Testimonials in Advertising (16 CFR Part 255)](https://www.ecfr.gov/api/versioner/v1/full/2023-07-26/title-16.xml?part=255) — Electronic Code of Federal Regulations |
| Public method summary | `demos/marketing-claims-review/skill/public-method.md` |
| Synthetic company policy | `demos/marketing-claims-review/sources/company-policy.md` |
| Synthetic case | `demos/marketing-claims-review/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/marketing-claims-review/evaluation/` |
| Portable skill | `demos/marketing-claims-review/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Evidence status

| Asset | Status |
|---|---|
| Six-file Cowork skill package definition | Ready; deterministic packaging covered by test |
| Three-source synthetic case pack | Ready and tracked |
| Three-source FTC method manifest | Ready; public snapshots not tracked |
| Twelve locked scenarios and 14-point rubric | Ready |
| Answer-key-free deterministic scenario renderer | Ready; 12 input hashes locked |
| Presenter setup and expected checkpoints | Ready |
| Signed-in Cowork control | Captured; raw first response retained |
| Final package upload | Captured in Customize as `marketing-claims-review-copilot-3` |
| Signed-in final-package treatment | Captured with Auto and Claude Opus 4.8; first responses retained |
| Fixed-runtime formal benchmark and blinded human review | Pending |

The Cowork UX set now contains one clean brief-only control, one model-matched
Claude Opus 4.8 treatment, and one separate Auto treatment. Four operational
attempts are recorded as excluded. These remain UX observations, not causal or
formal benchmark evidence.

Cowork package SHA-256:
`35e0642d1fdf63f3698419d5b014acab4755d9c50c8dad812d459ac86f902e9b`.

## Clean Cowork control observation

The retained control used only the answer-key-free fictional campaign brief.
It selected the evidence-bounded campaign and found all primary claim problems.
It did not name the permitted `approve-with-edits` class or have access to the
MCS authority matrix. It correctly treated the named compatibility exclusions
as unavailable in its brief-only context. The raw response is retained without
repair.

[Open the full-size control capture](../assets/skills/marketing-claims-review/screenshots/01-control-1-1920x1080.png)

![Brief-only Cowork control response with no custom skill in Workspace](../assets/skills/marketing-claims-review/screenshots/01-control-1-1920x1080.png)

[Control 1 raw response](../assets/skills/marketing-claims-review/outputs/control-1.txt) ·
[Run manifest](../assets/skills/marketing-claims-review/metadata/cowork-runs.json)

Manifest paths are relative to the original manifest directory in the demo
source tree. Use the page links above and below for published raw assets.

## Skill-assisted Cowork observations

Both skill-assisted first responses selected `approve-with-edits`, recommended
the evidence-bounded campaign, inventoried all seven claim/disclosure rows,
applied the MCS authority and release controls, and kept FTC method separate from
synthetic policy. Both exceeded the requested 700-word limit.

[Open the full-size Claude treatment capture](../assets/skills/marketing-claims-review/screenshots/04-treatment-claude-1-1920x1080.png)

![Claude Opus 4.8 treatment with the Marketing Claims Review skill loaded](../assets/skills/marketing-claims-review/screenshots/04-treatment-claude-1-1920x1080.png)

[Claude treatment raw response](../assets/skills/marketing-claims-review/outputs/treatment-claude-1.txt) ·
[Auto treatment raw response](../assets/skills/marketing-claims-review/outputs/treatment-auto-1.txt) ·
[Preliminary review record](../assets/skills/marketing-claims-review/metadata/preliminary-review.json)

!!! warning "Preliminary rubric rehearsal — not a formal benchmark"

    A conservative blinded AI-assisted rehearsal scored the model-matched Claude
    treatment 12/14 with no penalties and the brief-only control 7 after one
    penalty. The separate Auto treatment also scored 12/14. Both treatments
    exceeded the requested 700-word limit.
    Human review is not complete. The prompts differ by explicit skill
    invocation, Cowork runtime controls were not fully pinned, and only one of
    12 scenarios was run. Do not interpret these figures as causal uplift,
    statistical estimates, or independently validated performance.

## Public method sources

- [Advertising and Marketing on the Internet: Rules of the Road](https://www.ftc.gov/system/files/ftc_gov/pdf/bus28-rulesroad-2023_508.pdf),
  16-page PDF served at the pinned FTC URL.
- [.com Disclosures: How to Make Effective Disclosures in Digital Advertising](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf),
  53 pages, March 2013.
- [Guides Concerning the Use of Endorsements and Testimonials in Advertising, 16 CFR Part 255](https://www.ecfr.gov/api/versioner/v1/full/2023-07-26/title-16.xml?part=255),
  date-pinned 2023-07-26 eCFR XML snapshot.

Exact snapshot SHA-256 values are recorded in the source manifest. The public
PDFs and XML are not committed, and the skill compiles concise method rules
rather than copying long passages. US federal government works are generally not
copyrightable under 17 U.S.C. 105, but third-party material and assets must be
checked separately.

All Lumena names, products, policies, people, sources, payments, results, and
campaign facts are fictional synthetic data.

## Baseline claims

| Claim | Supplied evidence fit | Required baseline disposition |
|---|---|---|
| Save 30% on home energy bills | Pilot measured median 12% HVAC electricity reduction, not bills | Replace with exact bounded pilot statement |
| Pays for itself in six months | Payback was not measured | Remove |
| Works in every home | Known equipment exclusions and installation requirements | Remove; show compatibility near CTA |
| Independent pilot proves the savings | Lumena sponsored and analyzed; no independent replication | State company sponsorship; remove independence claim |
| Ava Reed: 35% bill reduction | Dashboard showed 18% HVAC electricity reduction over 8 weeks; no typical-results analysis | Remove the performance endorsement |
| `#LumenaPartner` after collapsed boundary | Paid USD 5,000 and received free device | Put clear paid/device disclosure first and in content |
| Bottom-page `Results vary` footnote | Distant qualification cannot cure contradictory headlines under MCS-2.1 | Replace with close, unavoidable, non-contradictory disclosure |

The evidence-bounded option preserves the exact population, metric, duration,
baseline, result, sponsorship, compatibility conditions, and material-connection
facts without converting an exceptional personal result into a release claim.
Legal, Compliance, Marketing Director, and Product Evidence Owner participation
is required before release.

## Evaluation plan

The signed-in Cowork demonstration will retain first responses from a fresh
control conversation and a fresh explicit-skill-invocation conversation with the
same synthetic brief. This comparison is UX evidence only: explicit invocation
is a treatment choice because automatic discovery and host runtime may not be
pinned.

The formal benchmark is separate. It uses exactly 12 locked scenarios, one
permitted decision class, one campaign option, a maximum positive score of 14,
repeatable penalties, a declared model and parameters, randomized presentation,
and blinded human review. It reports total score, unsupported claim count,
correct abstention, response words, and evidence references only after execution
and review.

Release evidence includes raw first responses, run conditions, package hash,
scenario version, scoring records, exclusions, limitations, and failed cases.
Preliminary rehearsal metrics remain visibly separated from the pending formal
benchmark.

## Human boundary

The skill may inventory claims, map evidence, draft required edits, identify
missing facts, and route reviewers. It does not make a final legal determination
or authorize campaign release, publication, pause, correction, withdrawal, or
monitoring actions.

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/marketing-claims-review/marketing-claims-review-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/marketing-claims-review/marketing-claims-review-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.
