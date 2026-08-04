# KVKK privacy notice review

**Domain:** Data protection<br>
**For:** Privacy, compliance, and product teams

Connects notice, consent, and transfer gaps to a human release gate.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [6698 sayılı Kişisel Verilerin Korunması Kanunu](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf) | Mevzuat Bilgi Sistemi |
| Official source | [Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ](https://www.resmigazete.gov.tr/eskiler/2018/03/20180310-5.htm) | Resmî Gazete |
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

The locked evaluation expects decision class `revise-before-launch`, option
`separate-notice-and-consent`, and 5 rule identifiers.
Final human route: Privacy Counsel · Data Protection/Compliance · Product Owner.

## LLM only vs LLM + skill

The same case and prompt were run twice. The only difference was that the skill
was installed for the second run. A deterministic script using the locked answer
key, not another model, scored both answers.

| Check | LLM only | LLM + skill |
| --- | ---: | ---: |
| Policy rules cited | 0 / 5 | 5 / 5 |
| Exact decision class | no | yes |
| Named option | no | yes |
| Human route | no | yes |
| **Trace score** | **10 / 100** | **100 / 100** |

[Control answer](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/kvkk-aydinlatma-kontrolu/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/kvkk-aydinlatma-kontrolu
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/kvkk-aydinlatma-kontrolu/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
