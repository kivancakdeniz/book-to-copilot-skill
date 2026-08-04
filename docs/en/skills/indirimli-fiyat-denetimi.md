# Discount price claim review

**Domain:** E-commerce and consumer law<br>
**For:** E-commerce, pricing, and compliance teams

Meets price history and campaign claims in a traceable release decision.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [Fiyat bilgisi içeren reklamlar ile indirimli satış reklamları ve ticari uygulamaları hakkında kılavuz](https://tuketici.ticaret.gov.tr/haberler/fiyat-bilgisi-iceren-reklamlar-ile-indirimli-satis-reklamlari-ve-ticari-uygulamalari-hakkinda-kilavuz-guncellendi) | Ticaret Bakanlığı |
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

The locked evaluation expects decision class `revise-price-claim`, option
`advertise-25-percent`, and 7 rule identifiers.
Final human route: E-commerce Owner · Pricing Owner · Compliance · Legal.

## LLM only vs LLM + skill

The same case and prompt were run twice. The only difference was that the skill
was installed for the second run. A deterministic script using the locked answer
key, not another model, scored both answers.

| Check | LLM only | LLM + skill |
| --- | ---: | ---: |
| Policy rules cited | 0 / 7 | 7 / 7 |
| Exact decision class | no | yes |
| Named option | no | yes |
| Human route | yes | yes |
| **Trace score** | **20 / 100** | **100 / 100** |

[Control answer](../../assets/skills/indirimli-fiyat-denetimi/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/indirimli-fiyat-denetimi/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/indirimli-fiyat-denetimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/indirimli-fiyat-denetimi
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/indirimli-fiyat-denetimi/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
