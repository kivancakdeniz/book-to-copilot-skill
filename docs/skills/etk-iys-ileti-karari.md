# ETK/IYS Commercial Message Decision

[Türkçe](../tr/skills/etk-iys-ileti-karari.md)

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

Can the CRM team send a discount SMS message to 48,000 former retail customers
without providing current consent/IYS evidence?

## Starting facts

- The message includes a discount and a call to purchase; it is not a service
	notification.
- No current consent or IYS status snapshot has been provided.
- There is no evidence list at the individual-and-SMS-channel level.
- The message includes refusal/opt-out wording.
- No record supporting an exception, suppression gate, or human approval has
	been provided.

## Expected decision

For the starting case, the decision is `do-not-send` and the option is
`suppress-unverified-audience`. The human route is CRM Owner + Compliance +
Legal.

## Business impact

The demo leads the campaign team to review the communication purpose,
individual-channel evidence, refusal checks, exception facts, and the
suppression gate before considering audience size. The expected impact is
qualitative: visibility of the unverified audience, a clearer human decision
route, and repeatable campaign reviews under the same contract. No measured ROI
or financial gain is claimed.

## Source and licensing boundary

6563 sayılı ETK and Ticari İletişim Yönetmeliği are publicly available official
source materials. The manifest records the official URL, publisher, and SHA-256
metadata retrieved on 2026-08-04; official files are not redistributed under
the `metadata-only` approach, and long passages are not copied. The synthetic
policy and case are MIT-licensed. Human Legal must verify currency, reuse, and
application.

## Safety and human boundary

This content is not legal advice or a final legal conclusion. Human
Legal/Compliance owns the decision. The skill only analyzes, identifies gaps,
and routes the matter; it does not send messages, change IYS records, suppress
an audience, start or stop a campaign, or take any other autonomous action.
Real customer lists must not be used as demo input.

## 12-scenario readiness

Twelve unique scenarios are ready: they are locked with answer keys and tied to
a 14-point rubric. The scenarios are not presented as run or concluded in this
article; formal execution and human review are still pending.

## Downloads

The following packages were generated deterministically by the shared release
factory and are bound to the SHA-256 manifest:

- [Cowork skill package](../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-cowork.skill)
- [Copilot VS Code ZIP](../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-vscode.zip)
- [Scout ZIP](../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-scout.zip)
- [Copilot Studio GitHub harness ZIP](../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-classic-setup.zip)

The classic setup ZIP is a package of setup materials and instructions for
Copilot Studio; it is not a direct agent import package.