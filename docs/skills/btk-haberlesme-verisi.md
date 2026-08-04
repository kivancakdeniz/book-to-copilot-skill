# BTK communications data review

[Türkçe](../tr/skills/btk-haberlesme-verisi.md)

## Expected difference: LLM only vs LLM + skill

| Brief-only LLM | Compiled skill |
|---|---|
| May produce free-form guidance or an incomplete checklist | Structures the review around permitted decision classes, three action options, and rule identifiers |
| May fill evidence gaps with assumptions | Keeps missing facts `unknown` and routes them to the authorized human decision-makers |
| May offer a general compliance or operational recommendation | Applies an explicit gate for processing, campaign activation, redesign, or escalation |

This comparison is an expected design hypothesis, not an evaluation result. The
Cowork A/B comparison has not been run, and all 12 locked scenarios below are
pending execution and scoring. Metrics to measure are exact decision-class and
option matches, required-rule recall, unsupported-claim count, respect for human
authority boundaries, and response length.

## At a glance

| Field | Value |
|---|---|
| Review question | Assess the processing gate for an individualized telecom upsell campaign using location and traffic data |
| Baseline evidence | The campaign is requested without a supplied consent record, purpose match, or retention period |
| Expected class | `stop-processing` - do not continue the described processing |
| Expected option | `consent-first-redesign` - redesign the campaign so verified consent and related controls come first |
| Human decision | Privacy Counsel + Telecom Compliance + DPO; joint telecom and KVKK review |

## Code guide

Scenario IDs such as `BTK-01` are stable evaluation-case identifiers. A
decision class records the review outcome; an option records the permitted
campaign or data-use path that accompanies that outcome.

| Code | Plain-English meaning |
|---|---|
| `stop-processing` | Stop the proposed processing path pending an authorized human decision |
| `approve-processing` | Allow the documented processing path to continue through the human approval process |
| `hold-for-consent-evidence` | Pause until the required consent evidence can be verified |
| `escalate-privacy-counsel` | Send the unresolved privacy question to Privacy Counsel |
| `approve-with-controls` | Permit further review only with the stated controls in place |
| `consent-first-redesign` | Redesign the use case around verified consent before processing |
| `current-personalization` | Retain the currently documented personalization path |
| `aggregate-only` | Limit the use case to data that is aggregated and not linked back to an individual |

## Business targets and metrics to measure

The demo is designed to turn a CRM campaign request into a traceable record of
data category, purpose, consent evidence, security, retention, human decision,
and campaign gate. These are targets, not measured outcomes.

| Target | Metric to measure |
|---|---|
| Identify evidence gaps earlier | Review stage at which missing consent, purpose, security, or retention evidence is first recorded |
| Reduce campaign returns for incomplete evidence | Number and reason of campaign packages returned before activation |
| Make consent withdrawal handling visible | Time from recorded withdrawal to CRM suppression, plus unresolved synchronization exceptions |
| Give human reviewers a consistent case file | Required evidence fields completed, missing fields marked `unknown`, and source-to-rule traceability |
| Keep the system within its delegated role | Unsupported claims and actions attempted outside the human authority boundary |

## Sources and safety

The public method source is the BTK regulation published in the Official
Gazette of the Republic of Turkiye. The package does not redistribute the
official text. It carries only the official URL, publisher, access date of
2026-08-04, SHA-256 digest, and reuse notice. The skill uses a short, cited
method summary rather than copying the regulation. Decision classes and options
come from the synthetic, MIT-licensed Kurgusal Telco policy.

## Human, telecom, and KVKK boundary

This skill does not provide legal advice or make a legal determination. The
official telecom source is one input and does not by itself resolve the KVKK or
other privacy questions raised by a use case. Privacy Counsel, Telecom
Compliance, and the DPO must perform a joint telecom review and human KVKK
review. Copilot does not process data, activate or stop a campaign, delete data,
or change a system.

## 12 locked scenarios - evaluation pending

| ID | Focus | Expected class | Expected option |
|---|---|---|---|
| BTK-01 | Location and traffic-data upsell without consent evidence | `stop-processing` | `consent-first-redesign` |
| BTK-02 | Fully documented current personalization | `approve-processing` | `current-personalization` |
| BTK-03 | Inaccessible consent attachment | `hold-for-consent-evidence` | `consent-first-redesign` |
| BTK-04 | Unclear purpose or legal-review path | `escalate-privacy-counsel` | `consent-first-redesign` |
| BTK-05 | Verifiable controls before processing | `approve-with-controls` | `consent-first-redesign` |
| BTK-06 | Aggregation not linked to an individual | `approve-processing` | `aggregate-only` |
| BTK-07 | Conflicting consent systems | `hold-for-consent-evidence` | `consent-first-redesign` |
| BTK-08 | Missing retention and deletion triggers | `stop-processing` | `consent-first-redesign` |
| BTK-09 | Live campaign without consent evidence | `stop-processing` | `consent-first-redesign` |
| BTK-10 | Aggregation test pending | `approve-with-controls` | `aggregate-only` |
| BTK-11 | Treating the official telecom source as sufficient by itself | `escalate-privacy-counsel` | `consent-first-redesign` |
| BTK-12 | Consent withdrawal not reflected in CRM | `stop-processing` | `consent-first-redesign` |

These scenarios define the expected answer key. They have not yet produced
comparative performance results.

## Downloads

- [Cowork skill](../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-cowork.skill)
- [GitHub Copilot for VS Code ZIP](../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-vscode.zip)
- [Scout ZIP](../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-classic-setup.zip)

The classic setup ZIP is not a direct-import package. Its files are setup
materials that a human must apply in a Copilot Studio classic environment.