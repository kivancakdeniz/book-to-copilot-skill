# Frozen Cowork treatment prompt

Use the `investment-committee-copilot` custom skill.

Evaluate Investment Committee Brief IC-0247 for Asteria Distribution Group.

Recommend one decision class and one option. Explain:

1. which objectives and decision gates pass, fail, or remain unknown;
2. what evidence supports the recommendation;
3. what information or approvals are still required;
4. what conditions, mitigations, monitoring measures, and stop/review points should apply.

Do not invent calculations, thresholds, policy, evidence, or authority. Clearly
separate supplied facts from judgement.

Respond only in this chat. Do not create, edit, render, or attach Word documents,
files, tasks, emails, presentations, spreadsheets, or other artifacts. Use at
most 700 words. Produce a compact executive decision card that a CFO, COO, and
CIO can review.

This explicit invocation is required for the current Cowork UX proof because an
automatic-discovery attempt did not load the custom skill. It is not used as the
formal causal A/B prompt; the fixed-model evaluation injects skill context outside
the user prompt.
