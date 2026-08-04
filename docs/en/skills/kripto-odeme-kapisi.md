# Crypto payment gateway review

**Domain:** Payment services and crypto assets<br>
**For:** Payments, compliance, legal, and product teams

Reviews the role of crypto in a payment flow against product and launch gates.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [Ödemelerde Kripto Varlıkların Kullanılmamasına Dair Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210416-4.htm) | Türkiye Cumhuriyet Merkez Bankası / T.C. Resmî Gazete |
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

The locked evaluation expects decision class `reject-payment-flow`, option
`remove-crypto-checkout`, and 6 rule identifiers.
Final human route: Payments Counsel · Compliance · Product.

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

[Control answer](../../assets/skills/kripto-odeme-kapisi/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/kripto-odeme-kapisi/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/kripto-odeme-kapisi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/kripto-odeme-kapisi
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/kripto-odeme-kapisi/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
