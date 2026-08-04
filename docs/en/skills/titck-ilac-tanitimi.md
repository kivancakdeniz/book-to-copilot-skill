# Pharmaceutical promotion review: audience and release gate

**Domain:** Pharmaceutical and health communication<br>
**For:** Medical, regulatory, legal, and marketing teams

Ties product status, audience, and channel reach to a human release review.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik](https://www.titck.gov.tr/mevzuat/beseri-tibbi-urunlerin-tanitim-faaliyetleri-hakkinda-yonetmelik-27122018172726) | Türkiye İlaç ve Tıbbî Cihaz Kurumu (TİTCK) |
| Official source | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik - Resmî Gazete yayımı](https://www.resmigazete.gov.tr/eskiler/2015/07/20150703-2.htm) | T.C. Resmî Gazete |
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

The locked evaluation expects decision class `do-not-publish`, option
`professional-channel-review`, and 7 rule identifiers.
Final human route: Medical · Regulatory · Legal.

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

[Control answer](../../assets/skills/titck-ilac-tanitimi/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/titck-ilac-tanitimi/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/titck-ilac-tanitimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/titck-ilac-tanitimi
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/titck-ilac-tanitimi/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
