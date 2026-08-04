# AML customer acceptance (MASAK)

**Domain:** Financial crime prevention<br>
**For:** AML, compliance, and onboarding teams

Routes identity, beneficial-owner, and source-of-funds gaps to human review.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [Suç gelirlerinin aklanmasının ve terörün finansmanının önlenmesine dair tedbirler hakkında yönetmelik](https://masak.hmb.gov.tr/suc-gelirlerinin-aklanmasinin-ve-terorun-finansmaninin-onlenmesine-dair-tedbirler-hakkinda-yonetmelik-3/) | MASAK |
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

The locked evaluation expects decision class `enhanced-review`, option
`hold-onboarding`, and 8 rule identifiers.
Final human route: AML Officer · Compliance.

## LLM only vs LLM + skill

The same case and prompt were run twice. The only difference was that the skill
was installed for the second run. A deterministic script using the locked answer
key, not another model, scored both answers.

| Check | LLM only | LLM + skill |
| --- | ---: | ---: |
| Policy rules cited | 0 / 8 | 8 / 8 |
| Exact decision class | no | yes |
| Named option | no | yes |
| Human route | yes | yes |
| **Trace score** | **20 / 100** | **100 / 100** |

[Control answer](../../assets/skills/masak-musteri-kabul/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/masak-musteri-kabul/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/masak-musteri-kabul/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/masak-musteri-kabul
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/masak-musteri-kabul/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
