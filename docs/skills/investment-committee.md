# Investment Committee Copilot

[Türkçe](../tr/skills/investment-committee.md)

## Decision

Should fictional Asteria Distribution Group approve a EUR 4.8 million full-
automation proposal, choose a safer option, escalate, reject, or request more evidence?

This demo captures four first-response Cowork UX runs against the same business
question and investment brief:

| Condition | Context |
|---|---|
| Control, two runs | Investment brief only; custom skill absent |
| Treatment, two runs | Same brief; custom skill explicitly invoked and shown as loaded |

Cowork showed Claude Opus 4.8, but did not expose a pinned runtime version. No
conversation-level custom-skill toggle was visible, and automatic discovery did
not load the installed skill. The treatment prompt therefore invokes the skill
explicitly. This is a UX comparison, not a causal A/B.

The treatment is expected to apply Asteria's fictional policy gates, compare the
do-minimum, phased, and requested options, preserve the requested option's
separate disposition, identify missing evidence, route human approvers, and cite
the source of each rule.

## Control vs skill: measured

Both runs answered the same locked case with the same prompt. The only
difference is that the second run had the skill installed. Scoring is done by a
deterministic script against the locked scenario, not by a model, so anyone can
reproduce these numbers.

| Governance gate | LLM only | LLM + skill |
| --- | --- | --- |
| Policy rules cited | 0 / 6 | 6 / 6 |
| Exact decision class stated | no | yes |
| Named option stated | yes | yes |
| Human approval route named | yes | yes |
| No autonomous-authority claim | yes | yes |
| **Trace score** | **40 / 100** | **100 / 100** |

Host: Microsoft 365 Copilot Cowork · Model: Claude Opus 4.8 · Captured: 2026-08-04 · Scenario: `IC-01`

[Control answer](../assets/skills/investment-committee/outputs/control-1.txt) · [Skill answer](../assets/skills/investment-committee/outputs/treatment-1.txt) · [Scorecard](../assets/skills/investment-committee/scorecard.json)

Reproduce:

```bash
python tools/score_skill_answer.py scorecard --demo demos/investment-committee
```

The control run cited 0 of 6 policy rules and the skill run cited 6. Only the skill run stated the exact decision class (`conditional-approval`).

Limits: one run per condition, one locked scenario, and a single host. This table
is the machine-checkable subset; the 14-point human rubric lives in
`demos/investment-committee/evaluation/rubric.json`.

## From source to skill

This chain shows exactly which content produced the skill.

| Stage | Produced content |
| --- | --- |
| Official source (metadata only) | [The Green Book - UK government guidance on appraisal](https://assets.publishing.service.gov.uk/media/698dbcd17da91680ad7f4308/The_Green_Book_2026.pdf) — HM Treasury and Government Finance Function |
| Public method summary | `demos/investment-committee/skill/public-method.md` |
| Synthetic company policy | `demos/investment-committee/sources/company-policy.md` |
| Synthetic case | `demos/investment-committee/sources/case-brief.md` |
| Locked evaluation | 12 scenarios and a 14-point rubric: `demos/investment-committee/evaluation/` |
| Portable skill | `demos/investment-committee/skill/SKILL.md` plus five companions |
| Host packages | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic) |

## Baseline case

| Option | Commitment | NPV | Payback | Downside NPV | Largest supplier | Result |
|---|---:|---:|---:|---:|---:|---|
| Do minimum | EUR 0.8m | EUR 0.3m | 3.5y | EUR 0.0m | 30% | Fails operational objectives |
| Phased automation | EUR 3.2m | EUR 1.1m | 4.2y | EUR 0.2m | 45% | Meets objectives; training sign-off pending |
| Full automation | EUR 4.8m | EUR 1.6m | 5.4y | EUR -0.7m | 72% | Cyber assessment and fallback absent |

The locked treatment answer key expects conditional approval of phased automation.
The model must earn that result through evidence and policy application rather
than being told to produce a persuasive recommendation.

## Evaluation

Twelve scenarios test clear approval, negative NPV, payback exception, supplier
concentration, cyber evidence, conflicting facts, missing downside evidence,
authority escalation, and no viable option.

The formal evidence release will show:

- raw first-run outputs;
- randomized A/B comparison;
- decision and option accuracy;
- gate coverage and missing-information detection;
- provenance quality;
- unsupported-rule and invented-fact penalties;
- limitations and failed cases.

## Cowork UX observations

Four separate Cowork tasks were retained: two controls and two
explicit-skill treatments. Two operational attempts were excluded: a long-form
prompt that triggered Word generation and a treatment attempt where automatic
discovery did not load the custom skill.

| Observation | Controls | Explicit-skill treatments |
|---|---|---|
| Recommended phased automation | 2/2 | 2/2 |
| ACP thresholds available and applied by rule ID | Not available | Yes |
| Preserved human approval boundary | Yes | Yes |
| Included unsupported details | Yes | Yes |

The second treatment applied all six locked IC-01 policy findings. The first
treatment omitted an explicit ACP-F01 pass. Both treatment responses still made
unsupported claims about missing monitoring measures or other unsupplied
details. The raw first responses are retained rather than repaired or rerun.

Package SHA-256:
`40c4f763cd0ffc30a939cd7a7cda2e58780ea9731eb4a3dc3376c4864168a659`.

### Control capture

[Open the full-size control capture](../assets/skills/investment-committee/screenshots/06-control-2-1920x1080.png)

![Control Cowork response with decision card and only the investment brief in Workspace](../assets/skills/investment-committee/screenshots/06-control-2-1920x1080.png)

[Control 1 raw response](../assets/skills/investment-committee/outputs/control-1.txt) ·
[Control 2 raw response](../assets/skills/investment-committee/outputs/control-2.txt)

### Explicit-skill treatment capture

[Open the full-size treatment capture](../assets/skills/investment-committee/screenshots/05-treatment-2-1920x1080.png)

![Treatment Cowork response with the Investment Committee skill loaded](../assets/skills/investment-committee/screenshots/05-treatment-2-1920x1080.png)

[Treatment 1 raw response](../assets/skills/investment-committee/outputs/treatment-1.txt) ·
[Treatment 2 raw response](../assets/skills/investment-committee/outputs/treatment-2.txt) ·
[Run manifest](../assets/skills/investment-committee/metadata/cowork-runs.json)

Manifest paths are relative to the original manifest directory in the demo
source tree. Use the page links above for published raw assets.

!!! warning "Formal benchmark pending"

    These four captures are Cowork UX observations, not causal evidence or an
    independently validated benchmark. The fixed-model, 12-scenario, three-arm
    evaluation and blinded human review remain pending. Preliminary internal
    rubric rehearsal scores are not presented as performance claims.

## Reproduce

The public release will include one `.skill` file, the fictional investment
brief, separate Cowork control and treatment prompts, the identical formal
evaluation prompt, package SHA-256, setup and teardown instructions, talk track,
expected behavioral checkpoints, and a backup recording.

See the [enterprise delivery plan](../ENTERPRISE-DEMO-PLAN.md) for release gates and
the second-demo criteria.

## Downloads

These packages are generated deterministically by the shared release factory
and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/skills/investment-committee/investment-committee-cowork.skill)
- [Copilot VS Code ZIP](../downloads/skills/investment-committee/investment-committee-copilot-vscode.zip)
- [Scout ZIP](../downloads/skills/investment-committee/investment-committee-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/skills/investment-committee/investment-committee-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/skills/investment-committee/investment-committee-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.
