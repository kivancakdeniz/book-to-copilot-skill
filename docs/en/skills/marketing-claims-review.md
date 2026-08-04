# Marketing claims review

**Domain:** Marketing and advertising compliance<br>
**For:** Marketing, legal, and compliance teams

Checks advertising claims against substantiation, disclosure, and release controls.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [Advertising and Marketing on the Internet: Rules of the Road](https://www.ftc.gov/system/files/ftc_gov/pdf/bus28-rulesroad-2023_508.pdf) | U.S. Federal Trade Commission |
| Official source | [.com Disclosures: How to Make Effective Disclosures in Digital Advertising](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf) | U.S. Federal Trade Commission |
| Official source | [Guides Concerning the Use of Endorsements and Testimonials in Advertising (16 CFR Part 255)](https://www.ecfr.gov/api/versioner/v1/full/2023-07-26/title-16.xml?part=255) | Electronic Code of Federal Regulations |
| Synthetic policy and case | `Published in the demo directory under the repository MIT licence` | — |

## Skill generated

Instead of compressing the source into one summary, the skill separates reusable
knowledge into six files:

- `SKILL.md`: when to use the skill and the workflow;
- `public-method.md`: an independent method summary from official sources;
- `company-policy.md`: synthetic company rules with stable identifiers;
- `evidence-map.md`: which claims may come from which source;
- `output-schema.md`: the expected answer structure;
- `scenario-guide.md`: missing information, conflicts, and abstention behavior.

The locked evaluation expects decision class `approve-with-edits`, option
`evidence-bounded-campaign`, and 9 rule identifiers.
Final human route: Legal · Compliance.

## LLM only vs LLM + skill

The same case and prompt were run twice. The only difference was that the skill
was installed for the second run. A deterministic script using the locked answer
key, not another model, scored both answers.

| Check | LLM only | LLM + skill |
| --- | ---: | ---: |
| Policy rules cited | 0 / 9 | 9 / 9 |
| Exact decision class | no | yes |
| Named option | yes | yes |
| Human route | yes | yes |
| **Trace score** | **40 / 100** | **100 / 100** |

[Control answer](../../assets/skills/marketing-claims-review/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/marketing-claims-review/outputs/treatment-auto-1.txt) ·
[Scorecard](../../assets/skills/marketing-claims-review/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/marketing-claims-review
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/marketing-claims-review/marketing-claims-review-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/marketing-claims-review/marketing-claims-review-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/marketing-claims-review/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
