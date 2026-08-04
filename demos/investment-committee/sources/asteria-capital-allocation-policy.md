# Asteria Capital Allocation Policy

**Document ID:** ACP-4.2  
**Effective:** 2026-01-01  
**Status:** Fictional demo policy; not financial advice or a real company policy

## Purpose

Asteria evaluates material investments through objectives, options, financial
and non-financial effects, delivery risk, evidence quality, approval authority,
and a measurable post-decision plan. A recommendation must compare at least
business-as-usual or do-minimum, a proportionate intermediate option, and the
requested option.

## Decision classes

- **Approve:** mandatory evidence is complete, all mandatory gates pass, and the
  decision sits within the named authority.
- **Conditional approval:** the preferred option passes strategic, financial,
  downside, concentration, and cyber gates; only remediable implementation
  conditions remain, each with an owner and due date before commitment or go-live.
- **Escalate:** an authority threshold, explicit strategic exception, severe
  supplier concentration, or unresolved conflict requires a higher body.
- **Reject:** the option fails a mandatory objective or financial/downside gate
  without an approved strategic exception, or presents an unmitigable critical risk.
- **Insufficient evidence:** a required fact is absent or contradictory, so no
  defensible decision class can be assigned.

## Gates

| Rule | Requirement | Effect when unmet |
|---|---|---|
| ACP-F01 | Risk-adjusted NPV must be greater than EUR 0. | Reject unless a documented strategic exception is escalated. |
| ACP-F02 | Base-case payback must be 5.0 years or less. | Escalate a documented exception; otherwise reject the option. |
| ACP-F03 | Downside-case NPV must be zero or positive. | Reject unless a documented strategic exception is escalated. |
| ACP-E01 | Base, downside, and sensitivity evidence must be present and internally consistent. | Insufficient evidence. |
| ACP-O01 | At least do-minimum, phased, and requested options must be compared against the same objectives. | Insufficient evidence. |
| ACP-S01 | No single implementation supplier may receive more than 50% of implementation spend without a mitigation plan. | Conditional approval at 51-65%; escalate above 65%. |
| ACP-C01 | A documented operational-technology cyber assessment is mandatory. | Missing assessment: insufficient evidence. Known pending remediations: conditional approval only, with CISO owner and due date before contract award. |
| ACP-R01 | Workforce, training, cutover, continuity, and benefit-owner plans must be identified. | Remediable gaps may be conditions; missing ownership is insufficient evidence. |
| ACP-M01 | Benefits must have named owners, measures, baselines, targets, review dates, and stop/review conditions. | Conditional approval until completed. |

## Authority matrix

| Total commitment | Minimum authority |
|---|---|
| Up to EUR 1.0 million | Business-unit EVP and Finance Director |
| Above EUR 1.0 million through EUR 5.0 million | Investment Committee: CFO, COO, and CIO |
| Above EUR 5.0 million | Board approval after Investment Committee recommendation |

The CISO joins when ACP-C01 is pending or failed. Procurement joins when ACP-S01
is above 50%. Legal joins when non-standard liability, data, or service terms are
requested.

## Balanced judgement

NPV alone does not determine the decision. The committee considers strategic
objectives, monetised and non-monetised effects, distribution of operational
impact, delivery feasibility, risk and uncertainty, and the credibility of the
monitoring plan. Quantitative outputs must not hide missing evidence.

## Human boundary

The Copilot skill may prepare a recommendation, identify rules, and draft a
decision memo. It cannot approve investment, release budget, select a supplier,
sign a contract, or invent missing financial calculations.