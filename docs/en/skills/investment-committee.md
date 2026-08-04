# Investment committee appraisal

**Domain:** Capital allocation<br>
**For:** CFO, COO, CIO, and investment committee members

Turns a capital brief into a gated, evidence-cited committee decision card.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [The Green Book - UK government guidance on appraisal](https://assets.publishing.service.gov.uk/media/698dbcd17da91680ad7f4308/The_Green_Book_2026.pdf) | HM Treasury and Government Finance Function |
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

The locked evaluation expects decision class `conditional-approval`, option
`phased-automation`, and 6 rule identifiers.
Final human route: Investment Committee.

## LLM only vs LLM + skill

The same case and prompt were run twice. The only difference was that the skill
was installed for the second run. A deterministic script using the locked answer
key, not another model, scored both answers.

| Check | LLM only | LLM + skill |
| --- | ---: | ---: |
| Policy rules cited | 0 / 6 | 6 / 6 |
| Exact decision class | no | yes |
| Named option | yes | yes |
| Human route | yes | yes |
| **Trace score** | **40 / 100** | **100 / 100** |

[Control answer](../../assets/skills/investment-committee/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/investment-committee/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/investment-committee/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/investment-committee
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/investment-committee/investment-committee-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/investment-committee/investment-committee-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/investment-committee/investment-committee-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/investment-committee/investment-committee-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/investment-committee/investment-committee-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/investment-committee/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
