# Enterprise Demo Plan

## Product story

`book-to-copilot-skill` turns approved business guidance into a reusable Copilot
decision capability. The customer-facing object is not a book summary or a
chatbot. It is a governed decision package with rules, evidence, limits,
evaluation cases, and a documented Cowork UX workflow.

The first demo is **Investment Committee Copilot**:

> Should Asteria Distribution Group approve a EUR 4.8 million warehouse
> automation investment, reject it, or approve a safer alternative?

## Why this demo

- The decision is recognizable to CFO, COO, strategy, finance, and operations leaders.
- The source method is public, current, and reusable.
- Company-specific thresholds can be synthetic and unambiguously fictional.
- The task requires policy application, option comparison, missing-information
  detection, risk treatment, approval routing, and an auditable recommendation.
- It can be demonstrated without CRM, ERP, write-back, or a remote MCP server.

## Source pack

### Open method source

- **The Green Book (2026)**, HM Treasury and Government Finance Function
- Purpose: appraisal of costs, benefits, risks, and options for achieving objectives
- Formats: official HTML and 88-page PDF
- Licence: Open Government Licence v3.0
- Required attribution:
  `Contains public sector information licensed under the Open Government Licence v3.0.`
- No government logo, endorsement, or official-status implication is permitted.

### Fictional enterprise sources

All company names, people, numbers, proposals, policies, and expected decisions
are synthetic.

1. `company-policy.md`
   - investment thresholds;
   - approval authority;
   - payback and NPV gates;
   - supplier concentration;
   - cyber and operational readiness;
   - exception and review rules.
2. `warehouse-automation-options.md`
   - do-minimum, phased, and full-automation options;
   - precomputed financial measures;
   - operational benefits and implementation risks;
   - known unknowns and evidence status.
3. `case-brief.md`
   - the facts supplied to every experimental arm;
   - no hidden calculation or policy text.

## Generated capability

The compiler produces a Cowork-compatible skill containing:

- `SKILL.md`: invocation, decision workflow, output contract, and limits;
- `./public-method.md`: distilled options-appraisal method;
- `./company-policy.md`: approved enterprise thresholds;
- `./evidence-map.md`: rule-to-source provenance;
- `./output-schema.md`: decision-card structure;
- `./scenario-guide.md`: missing-information and abstention rules.

The demo skill must stay within Cowork custom-skill limits:

- up to 20 companion files;
- 5 MB per companion file;
- 10 MB total per skill;
- at most 50 user-created skills in Cowork.

The first package is a `.skill` or `.zip` archive with `SKILL.md` at its root.
It is uploaded through **Customize → Skills → Add → Upload skill**. Cowork saves
it to OneDrive and can share it with **Only you** or specific users.

## Decision contract

Every skill-assisted answer uses this structure:

1. **Decision**: approve, conditional approval, escalate, reject, or insufficient evidence.
2. **Recommended option**: do minimum, phased automation, or full automation.
3. **Gate results**: pass, fail, unknown, and not applicable.
4. **Evidence**: rule ID, source, section, and short rationale.
5. **Missing information**: facts required before approval.
6. **Approvers**: roles required by the synthetic authority matrix.
7. **Conditions and mitigations**: actions that make approval defensible.
8. **Monitoring plan**: leading indicators, decision review date, and stop conditions.
9. **Limits**: no autonomous approval and no invented financial calculations.

## Experimental design

### Executive demo: two UX conditions

Use the same investment brief and business question in fresh Cowork
conversations. The control uses the chat-only prompt with the custom skill
absent. Because automatic discovery did not load the installed skill, the
treatment prompt explicitly invokes it and the presenter confirms that Cowork
shows it as loaded.

| Arm | Context | Purpose |
|---|---|---|
| Control | Cowork with the custom skill absent | Show the brief-only response |
| Treatment | Cowork with the custom skill explicitly invoked and loaded | Show policy-grounded decision behavior |

These conditions document the customer experience. They are not called a causal
A/B because the prompts differ and Cowork does not expose every runtime control.

### Formal evaluation design: three arms

The public evidence page adds a third arm:

| Arm | Context |
|---|---|
| A | Scenario only |
| B | Scenario plus raw source documents |
| C | Scenario plus compiled skill |

This distinguishes the compiled decision layer from merely adding more context.

### Cowork versus formal evaluation

Cowork documents the customer experience. It may not expose or pin every model
runtime parameter, so the four UX runs are not a causal benchmark.

Formal evaluation runs separately with:

- one fixed model and version;
- one fixed system configuration;
- identical prompt and scenario facts;
- independent conversations;
- at least three runs per arm;
- first-run outputs retained without cherry-picking;
- raw outputs and timestamps published;
- deterministic rubric scoring plus blinded human review.

## Evaluation set

The first release contains 12 locked scenarios:

1. clear approval;
2. negative NPV;
3. payback above policy limit;
4. supplier concentration above limit;
5. missing cyber review;
6. implementation-readiness failure;
7. financially marginal but strategically important;
8. conflicting facts;
9. missing downside case;
10. phased option dominates full automation;
11. authority threshold requires escalation;
12. insufficient evidence requiring abstention.

Each case has an answer key containing only observable gates and the expected
decision class. The key does not prescribe prose.

## Rubric

| Dimension | Score |
|---|---:|
| Correct decision class | 0-2 |
| Correct recommended option | 0-2 |
| Policy-gate coverage | 0-2 |
| Missing-information detection | 0-2 |
| Evidence and provenance | 0-2 |
| Approval routing | 0-1 |
| Actionable conditions and monitoring | 0-2 |
| Unsupported rule or invented fact | -2 each |
| False precision or autonomous approval | -2 each |

Report total score, unsupported-claim count, abstention correctness, median
response length, and estimated context use. Do not claim ROI until a customer
pilot establishes a baseline.

## Cowork live-demo script

Target duration: 10 minutes.

1. **Problem, 45 seconds**: show the scattered-source problem and decision question.
2. **Source pack, 60 seconds**: show official method, fictional policy, and proposal.
3. **Compilation, 60 seconds**: show rule cards and provenance, not raw prompt text.
4. **Control, 90 seconds**: skill absent; run the chat-only control prompt.
5. **Treatment, 120 seconds**: explicitly invoke the skill; confirm it is loaded.
6. **Decision evidence, 90 seconds**: open failed gates and source references.
7. **What-if, 90 seconds**: replace full automation with the phased option.
8. **Approval boundary, 45 seconds**: show that Cowork drafts but a human approves.
9. **Reveal and metrics, 60 seconds**: reveal A/B and show the locked evaluation set.

## Presenter kit

Microsoft managers receive one versioned release containing:

- Cowork skill archive;
- synthetic investment brief;
- versioned Cowork control and treatment prompts;
- separate identical prompt for formal evaluation;
- 10-minute talk track;
- expected checkpoints, not memorized model wording;
- setup and teardown instructions;
- common objections and truthful answers;
- a backup recording and screenshots;
- a QR/link to the public evidence page.

The presenter must be able to complete setup without cloning the repository.

## Screenshot and recording plan

Capture only synthetic content. Crop or redact tenant identity, personal data,
notifications, browser profile details, and unrelated Microsoft 365 content.

Required captures:

1. Cowork Customize page with the uploaded skill;
2. skill detail and description;
3. control Workspace with the brief only and custom skill absent;
4. control response;
5. treatment Workspace with the custom skill under Skills & Plugins;
6. loaded-skill panel;
7. treatment decision card;
8. provenance/evidence detail;
9. changed scenario and updated recommendation;
10. Word decision memo preview and action-approval boundary.

Screenshots and raw Cowork outputs document the UX; neither proves output
quality or causal uplift. Fixed-model raw outputs, rubric scores, and blinded
human review records will be the primary formal evidence.

## Public repository gates

Do not change repository visibility until all gates pass:

1. licence and attribution inventory;
2. secret and history scan;
3. remove private tenant IDs, user names, paths, screenshots, and logs;
4. replace private operational links with public documentation;
5. dependency and workflow review;
6. generated demo package reproducible from tracked sources;
7. all tests and package validation green;
8. screenshots reviewed for privacy;
9. README clearly separates code licence from demo-content licences;
10. security policy and responsible-use limits published.

## Public web experience

The repository website becomes an evidence-led product page, not a marketing-only landing page.

### Pages

- `/`: problem, transformation, and reproducible proof;
- `/demo/investment-committee`: interactive A/B reveal and decision evidence;
- `/method`: source → extraction → compilation → validation → evaluation;
- `/cowork`: upload, run, share, and teardown instructions;
- `/reproduce`: pinned sources, package command, prompts, and test commands;
- `/security`: data boundaries, prompt-injection controls, and human approval;
- `/demo/<second-demo>`: second business-domain proof after the first is stable.

### Interactive A/B

Visitors read the scenario, compare randomized outputs, choose the stronger
answer, and then reveal the condition. The page explains why an answer scored
well by showing rubric dimensions and evidence—not by claiming that skill use is
always superior.

## Second demo gate

Do not build the second demo until the first meets all of these conditions:

- repeatable Cowork upload and discovery;
- 12-case evaluation complete;
- no unsupported policy claims in the treatment arm;
- presenter kit tested by someone other than the author;
- public page understandable without narration.

Preferred second scenario: **Marketing Claims Review**. It converts public
advertising guidance plus a fictional brand and evidence policy into a skill
that classifies campaign claims as approve, revise, escalate, or unsupported.
This demonstrates a different business function and produces highly visible
control-versus-skill differences without requiring a live CRM or ERP.

## Delivery phases

### Phase 1: tracked demo corpus

- source manifest and licences;
- fictional company policy;
- investment proposal and 12 scenarios;
- answer keys and rubric.

### Phase 2: compilation and Cowork package

- generated decision skill;
- deterministic package builder;
- package contract tests;
- personal Cowork upload.

### Phase 3: evidence capture

- four Cowork UX runs captured: two controls and two explicitly invoked treatments;
- two excluded operational attempts documented;
- raw first responses, 16:9 screenshots, and public-safe manifest captured;
- complete screenshot set and backup recording pending;
- fixed-model three-arm evaluation and blinded human review pending.

### Phase 4: public launch preparation

- public-readiness audit;
- repository visibility review and explicit approval;
- evidence website;
- downloadable release and presenter kit.

### Phase 5: second domain

- marketing-claims source pack;
- same evaluation contract;
- second Cowork package and web proof.