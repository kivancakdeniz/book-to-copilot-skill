# BRSA remote customer onboarding

[Türkçe](../tr/skills/bddk-uzaktan-musteri-edinimi.md)

## Control vs skill-assisted LLM: expected difference only

| Control: brief-only LLM | Skill-assisted LLM |
|---|---|
| May produce an open-ended narrative or an incomplete checklist | Structures the response around allowed decision classes, three options, and rule IDs |
| May fill evidence gaps with assumptions | Keeps missing facts `unknown` and routes them to a human decision-maker |
| May offer general compliance or operational guidance | Explicitly applies the publication, go-live, transaction, or closing gate |

This comparison is a design hypothesis about the expected difference only.
Cowork A/B execution for these 10 new skills, including the 12 locked scenarios
and the 14-point rubric, is still pending. Planned metrics are exact decision
and option match, required-rule recall, unsupported-claim count, observance of
human authority, and response length. No ROI or production-performance claim is made.

A fictional digital-bank team wants to launch a remote onboarding flow that
requests an identity-document scan and selfie by email only. This portable skill
reviews the request through method, evidence, control, human-authority, and
go-live gates without making an official determination.

## Business impact at a glance

| Question | Impact |
|---|---|
| What decision is required? | `reject-flow` in the base case; `manual-onboarding-fallback` is the recommended fallback option |
| What risk becomes visible? | Evidence gaps concerning live or video interaction, liveness and process integrity, records, and monitoring |
| Who decides? | Human Security, Compliance, and Legal authorities |
| What does the skill add? | Consistent use of five classes, three options, rule traceability, and an output designed for a 14-point rubric whose execution is pending |
| What does the skill not do? | Provide legal advice, official compliance certification, technical certification, go-live approval, or customer transactions |

## How it works

The skill limits the Official Gazette source through a metadata-only manifest;
it neither redistributes nor reproduces the official text. It separates concise
questions about the public method from the synthetic UME-1.0 company policy and
the synthetic UME-2408 case evidence. The output provides one exact decision
class, one exact option, evidence gates, and the required route to human review.

In the base flow, there is no evidence of live or video interaction, liveness
and process integrity, control logs, a monitoring plan, or human approvals.
Direct go-live is therefore not recommended. Every missing field remains
explicitly `unknown`, and the skill does not infer technical certification from
a selfie. Humans make the final decision and authorize every implementation
action.

## Downloads

- [Cowork skill](../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-cowork.skill)
- [GitHub Copilot for VS Code package](../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-vscode.zip)
- [Scout package](../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-scout.zip)
- [Copilot Studio GitHub harness package](../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-github-harness.zip)
- [Copilot Studio Classic setup package](../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-classic-setup.zip)

The Copilot Studio Classic package is not a directly importable solution. It
provides setup files and a mapping guide for human implementation in a Classic
environment; permissions, connections, and publication settings must be
verified separately after setup.

## Evaluation

The demo contains exactly 12 locked scenarios, with the answer key kept
separate from the prompt, and a 14-point rubric with explicit anchors for every
dimension. Execution is pending. The rubric is designed to measure the method
inventory, evidence discipline, source traceability, human authority, and
go-live and monitoring gates, as well as the correct class and option.

This material is for education and governance design. It is not legal advice,
official certification, or authorization to proceed. Authorized humans retain
the final decision and all implementation authority.