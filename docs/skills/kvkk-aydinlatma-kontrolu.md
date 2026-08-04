# KVKK Notice Review

[Türkçe](../tr/skills/kvkk-aydinlatma-kontrolu.md)

## LLM-only vs LLM + skill — expected difference

| Brief-only LLM | Compiled skill |
|---|---|
| May produce free-form guidance and an incomplete checklist | Structures the review around allowed decision classes, three options, and rule IDs |
| Risks filling gaps in evidence with assumptions | Keeps a missing fact as `bilinmiyor` and routes it to the human decision owner |
| Provides a general compliance or operational recommendation | Explicitly applies the publication, go-live, transaction, or closure gate |

**Design hypothesis:** This table states the expected difference; no Cowork A/B
has yet been run for these 10 new skills. Metrics to be measured are exact
decision/option matching, required-rule recall, unsupported-claim count, respect
for human authority boundaries, and response length. No ROI or production
performance is claimed.

## Business question at a glance

Can a synthetic B2B SaaS lead form go live with its current notice draft and
bundled marketing consent?

## Starting facts

- The form collects a name, business email address, phone number, IP address,
  and campaign source.
- An overseas processor is used; the transfer route and safeguard details are
  missing.
- The draft identifies the data controller, purposes, and collection method.
- Recipient groups, transfer context, legal-basis mapping, and the data
  subject's rights/contact route are missing.
- Marketing consent is tied to acceptance of the notice.

## Expected decision

For the starting case, the decision is `revise-before-launch` and the option is
`separate-notice-and-consent`. The human route is Privacy Counsel + Data
Protection/Compliance + Product Owner.

## Business impact

The demo turns the product team's “do we have text?” check into a traceable
decision based on the data inventory, completeness of the notice, separation of
consent, transfer evidence, and a signed publication gate. The expected impact
is qualitative: earlier visibility of gaps, clearer decision ownership, and
repeatable assessments under the same contract. No measured ROI or financial
gain is claimed.

## Source and licensing boundary

6698 sayılı KVKK and Aydınlatma Tebliği are publicly available official source
materials. The manifest records the official URL, publisher, and SHA-256
metadata retrieved on 2026-08-04; official files are not redistributed under
the `metadata-only` approach, and long passages are not copied. The synthetic
policy and case are MIT-licensed. Human Legal must verify currency, reuse, and
application.

## Safety and human boundary

This content is not legal advice or a final legal conclusion. Human
Legal/Compliance owns the decision. The skill only analyzes, identifies gaps,
and routes the matter; it does not publish, collect consent, transfer data,
change records, or take any other autonomous action. Real personal data must
not be used as demo input.

## 12-scenario readiness

Twelve unique scenarios are ready: they are locked with answer keys and tied to
a 14-point rubric. The scenarios are not presented as run or concluded in this
article; formal execution and human review are still pending.

## Downloads

The following packages were generated deterministically by the shared release
factory and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-cowork.skill)
- [Copilot VS Code ZIP](../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-vscode.zip)
- [Scout ZIP](../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.