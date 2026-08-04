# Ten-minute talk track

## 0:00-0:45 — The business problem

“Investment decisions rarely fail because leaders cannot write a summary. They
fail because objectives, options, policy thresholds, evidence quality, risks,
and approval authority are scattered across documents.”

State the question: should Asteria approve EUR 4.8 million for full warehouse
automation?

## 0:45-1:45 — The source boundary

Show three source classes:

- public appraisal method: HM Treasury Green Book 2026;
- fictional company policy: ACP-4.2;
- fictional options and frozen committee brief.

Say explicitly: “The public method does not set Asteria thresholds. The company
policy does. The skill keeps those provenance layers separate.”

## 1:45-2:45 — Compile, do not dump

Show the small Cowork skill structure. Explain that the source pack is compiled
into a bounded workflow, policy references, evidence map, output schema, and
missing-information discipline. Cowork loads only the relevant companion files.

Do not claim that the process proves factual correctness automatically. Human
review, security scanning, evaluation, and source attribution are separate gates.

## 2:45-4:15 — Control

Show a fresh conversation with only the brief attached and the custom skill
absent. Run the chat-only control prompt. Ask the audience to look for:

- one clear decision class;
- comparison of all three options;
- policy thresholds and authority routing;
- missing evidence;
- source-backed conditions.

Do not criticize the model. The control shows what the model can infer from the
brief alone.

## 4:15-6:15 — Treatment

Open a fresh treatment conversation, attach the same brief, and run the
explicit-invocation treatment prompt. Confirm the skill is shown as loaded under
**Workspace → Skills & Plugins**. Highlight:

- the recommended phased option;
- the requested full option's separate disposition;
- ACP-F02, ACP-F03, ACP-S01, and ACP-C01;
- CFO, COO, CIO, CISO, and Procurement routing;
- training sign-off as a condition;
- Green Book method citations separated from Asteria policy citations.

## 6:15-7:30 — Evidence, not confidence theatre

Open the evidence map. Show that a rule has an owner, source, and exact section.
Explain that the system must say `insufficient-evidence` instead of inventing NPV,
payback, downside, cyber, or approval facts.

## 7:30-8:30 — What-if

Ask:

> If phased automation's training sign-off is complete, what changes? Preserve
> the original requested option's disposition.

Expected checkpoint: phased automation can move from conditional approval to
approval if all other gates remain complete; full automation remains separately
dispositioned.

## 8:30-9:15 — Human boundary

Explain that Cowork can draft a decision memo or stakeholder communication, but
the Investment Committee retains approval. Any send, post, schedule, or file
action remains visible and subject to Cowork approval controls.

## 9:15-10:00 — Proof and next step

Show the 12 locked scenarios and rubric. Say:

“This live run documents the customer experience. The fixed-model three-arm
test—scenario only, raw documents, and compiled skill—will provide the formal
causal evidence.”

Invite a pilot using approved customer policy and anonymised historical cases,
not live production data.