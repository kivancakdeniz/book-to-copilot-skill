# Commercial message decision (ETK/IYS)

**Domain:** Commercial electronic messaging<br>
**For:** CRM, compliance, and legal teams

Reviews a campaign audience against person-channel evidence and a suppression gate.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6563.pdf) | Mevzuat Bilgi Sistemi |
| Official source | [Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2015/07/20150715-4.htm) | Resmî Gazete |
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

The locked evaluation expects decision class `do-not-send`, option
`suppress-unverified-audience`, and 4 rule identifiers.
Final human route: CRM Owner · Compliance · Legal.

## LLM only vs LLM + skill

The same case and prompt were run twice. The only difference was that the skill
was installed for the second run. A deterministic script using the locked answer
key, not another model, scored both answers.

| Check | LLM only | LLM + skill |
| --- | ---: | ---: |
| Policy rules cited | 0 / 4 | 4 / 4 |
| Exact decision class | no | no |
| Named option | no | yes |
| Human route | yes | yes |
| **Trace score** | **20 / 100** | **80 / 100** |

[Control answer](../../assets/skills/etk-iys-ileti-karari/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/etk-iys-ileti-karari/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/etk-iys-ileti-karari/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/etk-iys-ileti-karari
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/etk-iys-ileti-karari/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
