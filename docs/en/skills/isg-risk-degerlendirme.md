# OHS risk assessment: from change to commissioning gate

**Domain:** Occupational health and safety<br>
**For:** OHS, operations, maintenance, and engineering teams

Makes change risk visible through participation, control, and commissioning evidence.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [İş Sağlığı ve Güvenliği Risk Değerlendirmesi Yönetmeliği](https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm) | T.C. Resmî Gazete |
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

The locked evaluation expects decision class `renew-assessment`, option
`hold-commissioning`, and 7 rule identifiers.
Final human route: İşveren · İSG profesyonelleri · çalışan temsilcileri.

## LLM only vs LLM + skill

The same case and prompt were run twice. The only difference was that the skill
was installed for the second run. A deterministic script using the locked answer
key, not another model, scored both answers.

| Check | LLM only | LLM + skill |
| --- | ---: | ---: |
| Policy rules cited | 0 / 7 | 7 / 7 |
| Exact decision class | no | yes |
| Named option | yes | yes |
| Human route | yes | yes |
| **Trace score** | **40 / 100** | **100 / 100** |

[Control answer](../../assets/skills/isg-risk-degerlendirme/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/isg-risk-degerlendirme/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/isg-risk-degerlendirme/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/isg-risk-degerlendirme
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/isg-risk-degerlendirme/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
