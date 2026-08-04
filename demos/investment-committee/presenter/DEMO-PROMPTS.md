# Demo prompts

## Cowork UX prompts

Use `../evaluation/chat-only-prompt.md` for control and
`../evaluation/chat-only-treatment-prompt.md` for treatment. The treatment
prompt explicitly invokes the custom skill because no conversation-level toggle
was visible and automatic discovery did not load it. This is a Cowork UX
comparison, not a causal A/B.

Use `../evaluation/frozen-prompt.md` only for the formal fixed-model evaluation,
where context is injected outside an identical user prompt.

## What-if prompt

> The phased automation option now has final workforce-training sign-off from
> the COO. No other facts changed. Reassess the recommendation, preserve the
> requested full-automation option's separate disposition, and cite any decision
> class that changes.

## Missing-evidence prompt

> The phased option's downside NPV is unavailable. No other facts changed. Can
> the committee approve it? Do not calculate or infer the missing value.

Expected checkpoint: `insufficient-evidence`, not a guessed downside NPV and not
a conditional approval.

## Executive memo prompt

> Draft the recommendation as a one-page Investment Committee memo. Keep facts,
> policy application, judgement, missing information, and required human action
> visibly separate. Do not send, post, schedule, or approve anything.

## Prompts to avoid in the live demo

- Requests to recompute NPV or payback from missing cash flows
- Requests involving real companies or customer records
- Requests to send email or publish to Teams before the audience understands the
  decision analysis
- Prompts that reveal the treatment arm before the A/B comparison