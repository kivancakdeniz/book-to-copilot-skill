# TİTCK medicinal product promotion: audience and publication gate

[Türkçe](../tr/skills/titck-ilac-tanitimi.md)

## LLM only vs LLM + skill: expected difference

| Brief-only LLM | Compiled skill |
|---|---|
| May produce an open-ended narrative or an incomplete checklist | Structures the review around the allowed decision classes, three options, and rule IDs |
| May fill evidence gaps with assumptions | Keeps unsupported facts `bilinmiyor` and routes them to the human decision owner |
| May offer a general compliance or campaign recommendation | Applies an explicit publication, targeting, or withdrawal gate |

This comparison is a design hypothesis only. Cowork A/B evaluation has not yet
been run for these 10 new skills. Metrics to measure are exact decision and
option match, required rule recall, unsupported-claim count, preservation of
human authority, and response length. No ROI, production-performance, or
model-impact claim is made.

## Scenario

A consumer-facing Instagram creative is proposed for a fictional prescription
product. It contains the product name, a benefit statement, and a "Ask your
doctor now" call to action. The account is public and has no access control
restricted to healthcare professionals.

The skill prepares a traceable draft for human Medical, Regulatory, and Legal
review instead of taking a publication action. The locked baseline result is
`do-not-publish`, and the recommended option is
`professional-channel-review`. That option does not approve separate
professional material or authorise its publication.

## What is reviewed

- The source supporting the product and prescription status.
- The material's actual audience and channel access, rather than its stated intent.
- Whether product-name, benefit, and call-to-action claims match the supplied approved scope.
- Whether any professional channel is restricted through genuine role verification.
- Whether Medical, Regulatory, and Legal review and the publication gate are recorded.
- Whether the version, channel, human owner, review cycle, and withdrawal triggers are explicit.

## Human authority and use boundary

The output is not legal or medical advice. Copilot does not approve, publish,
target, or remove content, and it does not stop a campaign. Authorised Medical,
Regulatory, Legal, and business owners make the final decision and carry out
every publication or operational action.

## Source approach

The public method is based on two official sources:

- [TİTCK - Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik](https://www.titck.gov.tr/mevzuat/beseri-tibbi-urunlerin-tanitim-faaliyetleri-hakkinda-yonetmelik-27122018172726),
  SHA-256 `552ce8f77c365599105d387e5d9d312998f26df634131faad66201a35ad027d1`.
- [T.C. Resmî Gazete yayımı](https://www.resmigazete.gov.tr/eskiler/2015/07/20150703-2.htm),
  SHA-256 `c23a03d934063bec7abd0a678cf947d2044af82f63d404a59028aaa5421191cf`.

Both sources were accessed on `2026-08-04`. External sources are distributed as
metadata only; the skill contains a short, cited method summary rather than
long copied passages. A human must verify the current text and reuse conditions
against the official sources. The company policy, product, creative, roles, and
all records are synthetic.

## Downloads

- [Microsoft 365 Copilot Cowork skill](../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-cowork.skill)
- [GitHub Copilot for VS Code package](../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-vscode.zip)
- [Scout package](../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-scout.zip)
- [Copilot Studio GitHub harness package](../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup package](../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-classic-setup.zip)

!!! warning "Copilot Studio classic setup"

    The classic setup ZIP is guided manual setup material, not a directly
    importable skill, agent, or solution, and it does not lock runtime behaviour.
    A human must review and configure its instructions, knowledge sources,
    connections, permissions, and publishing settings separately in the target
    environment.

## Evaluation status

The demo defines exactly 12 locked scenarios, five decision classes, three
options, and a maximum 14-point rubric with every score level anchored. Formal
scenario execution and human review are still pending; no evaluation result is
claimed. The frozen prompt prohibits inventing product status, medical evidence,
scope, targeting, access, dates, or authority, and prohibits producing
out-of-chat artefacts or performing publication or operational actions.
