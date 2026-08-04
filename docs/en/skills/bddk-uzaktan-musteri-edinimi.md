# Remote customer onboarding (BDDK)

**Domain:** Banking<br>
**For:** Digital banking, security, compliance, and legal teams

Tests a remote onboarding flow against evidence, control, and go-live gates.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [Bankalarca Kullanılacak Uzaktan Kimlik Tespiti Yöntemlerine ve Elektronik Ortamda Sözleşme İlişkisinin Kurulmasına İlişkin Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210401-7.htm) | Resmî Gazete |
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

The locked evaluation expects decision class `reject-flow`, option
`manual-onboarding-fallback`, and 7 rule identifiers.
Final human route: Güvenlik · Uyum · Hukuk.

## LLM only vs LLM + skill

The same case and prompt were run twice. The only difference was that the skill
was installed for the second run. A deterministic script using the locked answer
key, not another model, scored both answers.

| Check | LLM only | LLM + skill |
| --- | ---: | ---: |
| Policy rules cited | 0 / 7 | 7 / 7 |
| Exact decision class | no | no |
| Named option | yes | yes |
| Human route | yes | yes |
| **Trace score** | **40 / 100** | **80 / 100** |

[Control answer](../../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/bddk-uzaktan-musteri-edinimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/bddk-uzaktan-musteri-edinimi
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/bddk-uzaktan-musteri-edinimi/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
