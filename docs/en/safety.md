# Safety & reuse

Use this project with material you are allowed to process. The converter and the
public examples do not grant rights in source books, regulations, internal
documents, screenshots, or model output.

## Source rights

- The repository ships no source book or complete official document.
- Keep generated skills from copyrighted or confidential sources private unless
  you have permission to share them.
- Official sources in the 12 examples are represented by metadata and short,
  independently written method summaries.
- Synthetic policies, cases, evaluation fixtures, downstream code, and authored
  documentation are released under the repository MIT license.

## Data handling

Extraction runs locally. Do not put credentials, tenant identifiers, customer
data, personal data, confidential documents, or regulated records into public
prompts, screenshots, traces, issues, or evidence. If the agent model runs in a
hosted service, text sent to that model follows the provider's data terms.

## Generated skill review

Treat every input document as untrusted. Before installing a generated skill:

1. inspect `SKILL.md` and every supporting file;
2. review commands, links, paths, and frontmatter;
3. run host compatibility and prompt-injection scans;
4. remove source text that should not be retained or shared;
5. verify the current official source and company policy.

The scanners reduce risk; they do not certify a skill as safe or correct.

## Evaluation claims

The published comparison uses one frozen scenario and one run per condition on
the named host. It checks a machine-verifiable subset of behavior. It does not
prove production accuracy, legal compliance, safety, fairness, robustness, ROI,
or future performance.

Publish raw answers and scoring rules when claiming that a skill improved a
model. Do not hide runs that disagree with the expected result.

## Human authority

A skill can structure evidence and recommend a review path. It cannot approve,
publish, submit, onboard, reject, suspend, transfer, send, stop, or execute an
operational decision. An authorized human owns interpretation, approval, and
action.

## Project relationship

This is an independent downstream of the MIT-licensed
[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)
project. It is not endorsed by the upstream author, Microsoft, GitHub, model
providers, or any public authority.

Report security issues through the repository's private vulnerability-reporting
flow, not a public issue.
