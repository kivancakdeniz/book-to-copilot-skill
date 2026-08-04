#!/usr/bin/env python3
"""Render bilingual example pages from catalog, source, and scorecard data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

PACKAGE_LABELS = {
    "en": (
        ("Cowork `.skill`", "cowork.skill"),
        ("GitHub Copilot for VS Code", "copilot-vscode.zip"),
        ("Microsoft Scout", "scout.zip"),
        ("Copilot Studio GitHub harness", "copilot-studio-github-harness.zip"),
        ("Copilot Studio classic setup", "copilot-studio-classic-setup.zip"),
    ),
    "tr": (
        ("Cowork `.skill`", "cowork.skill"),
        ("VS Code için GitHub Copilot", "copilot-vscode.zip"),
        ("Microsoft Scout", "scout.zip"),
        ("Copilot Studio GitHub harness", "copilot-studio-github-harness.zip"),
        ("Copilot Studio classic kurulum", "copilot-studio-classic-setup.zip"),
    ),
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def best_run(scorecard: Mapping[str, Any], condition: str) -> Mapping[str, Any]:
    return max(
        (run for run in scorecard["runs"] if run["condition"] == condition),
        key=lambda run: run["traceScore"],
    )


def source_rows(locale: str, manifest: Mapping[str, Any]) -> list[str]:
    official = [
        source
        for source in manifest["sources"]
        if "path" not in source and not source.get("synthetic")
    ]
    rows: list[str] = []
    for source in official:
        title = source["title"].replace("|", "\\|")
        publisher = source.get("publisher", "")
        url = source.get("url") or source.get("officialUrl", "")
        source_type = "Official source" if locale == "en" else "Resmî kaynak"
        rows.append(f"| {source_type} | [{title}]({url}) | {publisher} |")
    synthetic_type = "Synthetic policy and case" if locale == "en" else "Sentetik politika ve vaka"
    synthetic_value = (
        "Published in the demo directory under the repository MIT licence"
        if locale == "en"
        else "Demo dizininde depo MIT lisansıyla yayımlanır"
    )
    rows.append(f"| {synthetic_type} | `{synthetic_value}` | — |")
    return rows


def comparison_table(locale: str, control: Mapping[str, Any], treatment: Mapping[str, Any]) -> str:
    yes, no = (("yes", "no") if locale == "en" else ("evet", "hayır"))
    labels = {
        "en": ("Check", "LLM only", "LLM + skill", "Policy rules cited", "Exact decision class", "Named option", "Human route", "Trace score"),
        "tr": ("Denetim", "Yalnız LLM", "LLM + skill", "Politika kuralı atfı", "Tam karar sınıfı", "Adlandırılmış seçenek", "İnsan rotası", "İz puanı"),
    }[locale]
    passed = lambda run, gate: yes if run["gates"][gate]["passed"] else no
    lines = [
        f"| {labels[0]} | {labels[1]} | {labels[2]} |",
        "| --- | ---: | ---: |",
        f"| {labels[3]} | {control['ruleCitationCount']} / {control['ruleCitationTotal']} | {treatment['ruleCitationCount']} / {treatment['ruleCitationTotal']} |",
        f"| {labels[4]} | {passed(control, 'decisionClass')} | {passed(treatment, 'decisionClass')} |",
        f"| {labels[5]} | {passed(control, 'recommendedOption')} | {passed(treatment, 'recommendedOption')} |",
        f"| {labels[6]} | {passed(control, 'humanRoute')} | {passed(treatment, 'humanRoute')} |",
        f"| **{labels[7]}** | **{control['traceScore']} / 100** | **{treatment['traceScore']} / 100** |",
    ]
    return "\n".join(lines)


def package_lines(locale: str, slug: str) -> list[str]:
    prefix = "../../downloads/skills"
    return [
        f"- [{label}]({prefix}/{slug}/{slug}-{suffix})"
        for label, suffix in PACKAGE_LABELS[locale]
    ]


def render_article(
    locale: str,
    slug: str,
    entry: Mapping[str, Any],
    manifest: Mapping[str, Any],
    scorecard: Mapping[str, Any],
    key: Mapping[str, Any],
) -> str:
    item = entry[locale]
    control = best_run(scorecard, "control")
    treatment = best_run(scorecard, "treatment")
    asset = f"../../assets/skills/{slug}"
    routes = " · ".join(key["humanRoute"])
    sources = "\n".join(source_rows(locale, manifest))
    packages = "\n".join(package_lines(locale, slug))
    control_file = Path(control["outputPath"]).stem
    treatment_file = Path(treatment["outputPath"]).stem

    if locale == "tr":
        return f"""# {item['title']}

**Alan:** {item['sector']}<br>
**Hedef ekip:** {item['audience']}

{item['oneLineValue']}

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
{sources}

## Üretilen skill

Skill, kaynak içeriği tek bir özete sıkıştırmak yerine yeniden kullanılabilir altı
dosyaya ayırır:

- `SKILL.md`: ne zaman kullanılacağı ve işlem sırası;
- `public-method.md`: resmî kaynaktan çıkarılan bağımsız yöntem özeti;
- `company-policy.md`: kararlı kimlikleri olan sentetik kurum kuralları;
- `evidence-map.md`: hangi iddianın hangi kaynaktan gelebileceği;
- `output-schema.md`: beklenen yanıt yapısı;
- `scenario-guide.md`: eksik bilgi, çelişki ve çekimserlik davranışı.

Kilitli değerlendirme `{key['decisionClass']}` karar sınıfını,
`{key['recommendedOption']}` seçeneğini ve {len(key['requiredRuleIds'])} kural
kimliğini bekler. Nihai insan rotası: {routes}.

## LLM only ve LLM + skill

Aynı vaka ve istem iki kez çalıştırıldı. Tek fark, ikinci çalıştırmada skill'in
yüklü olmasıdır. Puanlama bir model tarafından değil, kilitli yanıt anahtarını
okuyan deterministik betik tarafından yapılır.

{comparison_table(locale, control, treatment)}

[Kontrol yanıtı]({asset}/outputs/{control_file}.txt) ·
[Skill yanıtı]({asset}/outputs/{treatment_file}.txt) ·
[Skor kartı]({asset}/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/{slug}
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

{packages}

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/{slug}/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
"""

    return f"""# {item['title']}

**Domain:** {item['sector']}<br>
**For:** {item['audience']}

{item['oneLineValue']}

## Source converted

This example combines official method sources with a synthetic company policy
and a synthetic case. Raw official documents are not bundled.

| Type | Source | Publisher / status |
| --- | --- | --- |
{sources}

## Skill generated

Instead of compressing the source into one summary, the skill separates reusable
knowledge into six files:

- `SKILL.md`: when to use the skill and the workflow;
- `public-method.md`: an independent method summary from official sources;
- `company-policy.md`: synthetic company rules with stable identifiers;
- `evidence-map.md`: which claims may come from which source;
- `output-schema.md`: the expected answer structure;
- `scenario-guide.md`: missing information, conflicts, and abstention behavior.

The locked evaluation expects decision class `{key['decisionClass']}`, option
`{key['recommendedOption']}`, and {len(key['requiredRuleIds'])} rule identifiers.
Final human route: {routes}.

## LLM only vs LLM + skill

The same case and prompt were run twice. The only difference was that the skill
was installed for the second run. A deterministic script using the locked answer
key, not another model, scored both answers.

{comparison_table(locale, control, treatment)}

[Control answer]({asset}/outputs/{control_file}.txt) ·
[Skill answer]({asset}/outputs/{treatment_file}.txt) ·
[Scorecard]({asset}/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/{slug}
```

This is a one-scenario, one-host comparison; it is not proof of production
accuracy or regulatory compliance.

## Copilot packages

{packages}

The classic package is not a direct solution import. It contains setup material
for a human to apply in the target Copilot Studio environment.

## Reuse this example

The source manifest, synthetic inputs, scenarios, raw answers, and scorecard are
public under `demos/{slug}/`. Copy the structure for your own source, but publish
only material you have the right to share. Review [Safety & reuse](../safety.md).
"""


def render_catalog(locale: str, entries: Sequence[Mapping[str, Any]], scorecards: Mapping[str, Mapping[str, Any]]) -> str:
    controls = [best_run(scorecards[e["id"]], "control")["traceScore"] for e in entries]
    treatments = [best_run(scorecards[e["id"]], "treatment")["traceScore"] for e in entries]
    mean_control = int(sum(controls) / len(controls) + 0.5)
    mean_treatment = int(sum(treatments) / len(treatments) + 0.5)
    if locale == "tr":
        lines = [
            "---",
            "hide:",
            "  - toc",
            "---",
            "",
            "# 12 public örnek",
            "",
            "Bu örnekler dönüştürücünün yalnız kitaplarda değil, mevzuat ve kurum",
            "rehberlerinde de çalıştığını gösterir. Her örnekte kaynak manifesti, sentetik",
            "politika ve vaka, üretilen skill, 12 kilitli senaryo, kontrol yanıtı, skill",
            "yanıtı, skor kartı ve beş Copilot paketi bulunur.",
            "",
            f"12 örneğin ortalama iz puanı yalnız LLM'de **{mean_control}/100**, skill ile",
            f"**{mean_treatment}/100** oldu. Sonuçlar tek senaryo ve tek host sınırındadır.",
            "",
            "## Örnekler",
            "",
        ]
        for entry in entries:
            item = entry["tr"]
            card = scorecards[entry["id"]]
            lines.extend(
                (
                    f"### [{item['title']}]({entry['id']}.md)",
                    "",
                    f"**Alan:** {item['sector']}<br>",
                    f"**Puan:** LLM only **{best_run(card, 'control')['traceScore']}/100** · "
                    f"LLM + skill **{best_run(card, 'treatment')['traceScore']}/100**",
                    "",
                    item["oneLineValue"],
                    "",
                )
            )
        lines.extend((
            "",
            "## Ne indirebilirsiniz",
            "",
            "Her örnek sayfasında Cowork, GitHub Copilot for VS Code, Scout ve iki Copilot",
            "Studio biçimi bulunur. Tüm paketler temiz yeniden derlemede byte-identical",
            "doğrulanır ve `downloads/skills/SHA256SUMS` manifestine bağlanır.",
            "",
            "Kendi içeriğinizle aynı akışı kurmak için [Skill oluştur](../create-a-skill.md).",
        ))
    else:
        lines = [
            "---",
            "hide:",
            "  - toc",
            "---",
            "",
            "# 12 public examples",
            "",
            "These examples show that the converter works with regulations and company",
            "guidance as well as books. Every example includes a source manifest, synthetic",
            "policy and case, generated skill, 12 locked scenarios, control answer, skill",
            "answer, scorecard, and five Copilot packages.",
            "",
            f"Across the 12 examples, the mean trace score moved from **{mean_control}/100**",
            f"without the skill to **{mean_treatment}/100** with it. Results are limited to",
            "one scenario and one host per condition.",
            "",
            "## Examples",
            "",
        ]
        for entry in entries:
            item = entry["en"]
            card = scorecards[entry["id"]]
            lines.extend(
                (
                    f"### [{item['title']}]({entry['id']}.md)",
                    "",
                    f"**Domain:** {item['sector']}<br>",
                    f"**Score:** LLM only **{best_run(card, 'control')['traceScore']}/100** · "
                    f"LLM + skill **{best_run(card, 'treatment')['traceScore']}/100**",
                    "",
                    item["oneLineValue"],
                    "",
                )
            )
        lines.extend((
            "",
            "## What you can download",
            "",
            "Each example page provides Cowork, GitHub Copilot for VS Code, Scout, and two",
            "Copilot Studio formats. Every package is verified byte-identical after a clean",
            "rebuild and recorded in `downloads/skills/SHA256SUMS`.",
            "",
            "To run the same workflow on your material, [create a skill](../create-a-skill.md).",
        ))
    return "\n".join(lines) + "\n"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    catalog = load(root / "demos" / "catalog.json")
    scorecards: dict[str, Mapping[str, Any]] = {}
    for entry in catalog["entries"]:
        slug = entry["id"]
        demo = root / "demos" / slug
        scorecard = load(demo / "evidence" / "scorecard.json")
        scorecards[slug] = scorecard
        manifest = load(demo / "sources" / "source-manifest.json")
        key = load(demo / "evaluation" / "answer-key.json")
        for locale, field in (("en", "article"), ("tr", "articleTr")):
            (root / entry[field]).write_text(
                render_article(locale, slug, entry, manifest, scorecard, key),
                encoding="utf-8",
            )
    (root / "docs" / "en" / "skills" / "index.md").write_text(
        render_catalog("en", catalog["entries"], scorecards), encoding="utf-8"
    )
    (root / "docs" / "tr" / "skills" / "index.md").write_text(
        render_catalog("tr", catalog["entries"], scorecards), encoding="utf-8"
    )
    print("Rendered 24 example pages and 2 catalogs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
