# Competition-law merger notification

[Türkçe](../tr/skills/rekabet-birlesme-bildirimi.md)

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

In a fictional acquisition, the transaction produces a lasting change of
control. Finance supplied a precomputed turnover test, meaning a turnover
calculation completed before the skill review, and labeled it `met`, meaning
Finance's stated test condition was satisfied. The target's technology-
undertaking status remains `unknown`, meaning the available evidence does not
establish that status. Signing is imminent and the parties want to close. This
portable skill structures the route to human counsel and the closing gate
without calculating turnover or making the legal filing decision. Here,
"filing" means submitting a formal merger notification to the competent
authority.

## Business impact at a glance

| Question | Impact |
|---|---|
| What decision is required? | `legal-notification-review` in the base case; `hold-closing` is the recommended hold option |
| What risk becomes visible? | Treating the `met` indicator as a legal conclusion, the `unknown` technology-undertaking status, incomplete counsel routing, and missing version tracking |
| Who decides? | Human Competition Counsel; Finance owns only the precomputed turnover result |
| What does the skill add? | Consistent use of five classes, three options, rule traceability, and an output designed for a 14-point rubric whose execution is pending |
| What does the skill not do? | Provide legal advice or official certification; calculate turnover or thresholds; make a filing decision; file a notification; restructure, sign, or close the transaction |

## How it works

The skill limits two Turkish Competition Authority guidelines through a
metadata-only manifest; it neither redistributes the PDFs nor reproduces the
official text. It separates concise questions about the public method from the
synthetic BKP-1.0 company policy and the synthetic RKB-2608 transaction facts.

In the base case, `met` remains only Finance's precomputed indicator. It is not
a legal conclusion about whether notification is required. The technology-
undertaking status remains `unknown` pending review by human Competition
Counsel, and the closing gate does not open without recorded human direction.
Humans make the final legal and transaction decisions.

## Downloads

- [Cowork skill](../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-cowork.skill)
- [GitHub Copilot for VS Code package](../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-vscode.zip)
- [Scout package](../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-scout.zip)
- [Copilot Studio GitHub harness package](../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-github-harness.zip)
- [Copilot Studio Classic setup package](../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-classic-setup.zip)

The Copilot Studio Classic package is not a directly importable solution. It
provides setup files and a mapping guide for human implementation in a Classic
environment; permissions, connections, and publication settings must be
verified separately after setup.

## Evaluation

The demo contains exactly 12 locked scenarios, with the answer key kept
separate from the prompt, and a 14-point rubric with explicit anchors for every
dimension. Execution is pending. The rubric is designed to measure the control-
fact inventory, discipline against recalculation, the technology-status
boundary, source traceability, human authority, and the closing gate, as well
as the correct class and option.

This material is for education and governance design. It is not legal advice,
official certification, or authorization to proceed. Authorized humans retain
the final legal decision and all transaction authority.