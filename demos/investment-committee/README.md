# Investment Committee Copilot demo

This demo shows the same business question answered under two conditions:

1. the model receives only the investment brief;
2. the same model receives the same brief plus a compiled decision skill.

The public method source is HM Treasury's *The Green Book (2026)*. Asteria
Distribution Group, its policies, investment options, suppliers, people, and
financial values are entirely fictional.

## Demo question

> Should Asteria approve the EUR 4.8 million full-automation proposal, choose a
> different option, escalate, reject, or request more evidence?

## Expected treatment behavior

The skill should recommend **conditional approval of phased automation**, not
full automation as presented. It should identify the full option's payback,
downside, supplier-concentration, and cyber-readiness issues; route the decision
to the Investment Committee; and make workforce-training sign-off a condition
of the phased option.

## Structure

```text
sources/
  source-manifest.json
  company-policy.md
  warehouse-automation-options.md
  case-brief.md
evaluation/
  chat-only-prompt.md
  chat-only-treatment-prompt.md
  frozen-prompt.md
  ic-01-scorecard.json
  rubric.json
  scenarios.json
evidence/
  metadata/
  outputs/
  screenshots/
```

The official PDF is not committed. Fetch it from the URL and verify the SHA-256
recorded in `source-manifest.json` before extraction.

## Experimental rule

For the captured Cowork UX, use `chat-only-prompt.md` for control and
`chat-only-treatment-prompt.md` for treatment. The treatment prompt explicitly
invokes the skill because automatic discovery did not load it. Use fresh
conversations and identical attachments. Cowork runs are the UX demo;
`frozen-prompt.md` remains the identical prompt for the future fixed-model
causal evaluation.

The retained UX set contains two control and two explicit-skill treatment runs;
two operational attempts are recorded as excluded. Raw first responses, 16:9
screenshots, and a public-safe run manifest are included. The formal three-arm,
12-scenario fixed-model evaluation and blinded human review remain pending.

Package SHA-256:
`40c4f763cd0ffc30a939cd7a7cda2e58780ea9731eb4a3dc3376c4864168a659`.