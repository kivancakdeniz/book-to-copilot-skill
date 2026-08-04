# Merger notification review

**Domain:** Mergers and acquisitions<br>
**For:** M&A, finance, and competition law teams

Separates preliminary indicators from the legal notification and closing gate.

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
| Official source | [Birleşme ve Devralma Sayılan Haller ve Kontrol Kavramı Hakkında Kılavuz](https://www.rekabet.gov.tr/Dosya/kilavuzlar/birlesme-ve-devralma-sayilan-haller-ve-kontrol-kavrami-hakkinda-kilavuz.pdf) | Rekabet Kurumu |
| Official source | [Birleşme ve Devralma İşlemlerinde Ciro Hesaplanmasına İlişkin Kılavuz](https://www.rekabet.gov.tr/Dosya/bd-ciro-kilavuzu-20260504120128549.pdf) | Rekabet Kurumu |
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

The locked evaluation expects decision class `legal-notification-review`, option
`hold-closing`, and 7 rule identifiers.
Final human route: Rekabet Hukuku Danışmanı · Finans · Sponsor.

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

[Control answer](../../assets/skills/rekabet-birlesme-bildirimi/outputs/control-1.txt) ·
[Skill answer](../../assets/skills/rekabet-birlesme-bildirimi/outputs/treatment-1.txt) ·
[Scorecard](../../assets/skills/rekabet-birlesme-bildirimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/rekabet-birlesme-bildirimi
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

- [Cowork `.skill`](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-cowork.skill)
- [GitHub Copilot for VS Code](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-classic-setup.zip)

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/rekabet-birlesme-bildirimi/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
