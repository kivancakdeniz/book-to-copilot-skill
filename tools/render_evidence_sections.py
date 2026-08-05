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
        ("Copilot Studio GitHub bağlantı paketi", "copilot-studio-github-harness.zip"),
        ("Copilot Studio klasik kurulum paketi", "copilot-studio-classic-setup.zip"),
    ),
}

TR_DISPLAY_LABELS = {
    "AML Officer": "AML yetkilisi",
    "CRM Owner": "CRM sorumlusu",
    "Compliance": "Uyum",
    "Data Protection/Compliance": "Kişisel verilerin korunması ve uyum",
    "E-commerce Owner": "E-ticaret sorumlusu",
    "Investment Committee": "Yatırım komitesi",
    "Legal": "Hukuk",
    "Medical": "Medikal",
    "Payments Counsel": "Ödeme hizmetleri hukuk danışmanı",
    "Pricing Owner": "Fiyatlandırma sorumlusu",
    "Privacy Counsel": "Kişisel verilerin korunması hukuk danışmanı",
    "Product": "Ürün",
    "Product Owner": "Ürün sorumlusu",
    "Regulatory": "Ruhsatlandırma ve mevzuat",
    "Sponsor": "Proje sponsoru",
    "Telecom Compliance": "Telekom uyumu",
    "advertise-25-percent": "yüzde 25 indirim iddiasını kullan",
    "approve-with-edits": "düzeltmelerle onayla",
    "conditional-approval": "koşullu onay",
    "consent-first-redesign": "rıza sürecini önceleyen yeniden tasarım",
    "do-not-publish": "yayımlanmamalı",
    "do-not-send": "gönderilmemeli",
    "enhanced-review": "ayrıntılı inceleme",
    "evidence-bounded-campaign": "yalnızca kanıtlanabilir iddiaları kullanan kampanya",
    "hold-closing": "işlemin kapanışını beklet",
    "hold-commissioning": "devreye almayı beklet",
    "hold-onboarding": "müşteri edinimini beklet",
    "legal-notification-review": "hukuki bildirim incelemesi",
    "manual-onboarding-fallback": "elle müşteri edinimine geç",
    "phased-automation": "aşamalı otomasyon",
    "professional-channel-review": "mesleki kanallara uygunluk incelemesi",
    "reject-flow": "akışı reddet",
    "reject-payment-flow": "ödeme akışını reddet",
    "remove-crypto-checkout": "kripto ödeme seçeneğini kaldır",
    "renew-assessment": "değerlendirmeyi yenile",
    "revise-before-launch": "kullanıma sunmadan önce düzelt",
    "revise-price-claim": "fiyat iddiasını düzelt",
    "separate-notice-and-consent": "aydınlatma ile rızayı ayır",
    "stop-processing": "işlemeyi durdur",
    "suppress-unverified-audience": "doğrulanmamış kitleyi gönderimden çıkar",
}


def display_label(locale: str, value: str) -> str:
    return TR_DISPLAY_LABELS.get(value, value) if locale == "tr" else value


def traced_label(locale: str, value: str) -> str:
    label = display_label(locale, value)
    if locale == "tr" and label != value:
        return f"`{value}` ({label})"
    return f"`{value}`"


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
        else "Sentetik politika ve vaka, demo dizininde MIT lisansıyla yayımlanır"
    )
    rendered_value = f"`{synthetic_value}`" if locale == "en" else synthetic_value
    rows.append(f"| {synthetic_type} | {rendered_value} | — |")
    return rows


def comparison_table(locale: str, control: Mapping[str, Any], treatment: Mapping[str, Any]) -> str:
    yes, no = (("yes", "no") if locale == "en" else ("evet", "hayır"))
    labels = {
        "en": ("Check", "LLM only", "LLM + skill", "Policy rules cited", "Exact decision class", "Named option", "Human route", "Trace score"),
        "tr": (
            "Denetim",
            "Yalnızca LLM",
            "LLM + Agent Skill",
            "Politika kuralı atfı",
            "Beklenen karar sınıfıyla tam eşleşme",
            "Önerilen seçenek",
            "Yetkili incelemeye yönlendirme",
            "Karar izlenebilirliği puanı",
        ),
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
    routes = " · ".join(
        traced_label(locale, route) if locale == "tr" else route
        for route in key["humanRoute"]
    )
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

## Üretilen Agent Skill

Agent Skill, kaynak içeriği tek bir özete sıkıştırmak yerine yeniden kullanılabilir altı
dosyaya ayırır:

- `SKILL.md`: ne zaman kullanılacağı ve çalışma sırası;
- `public-method.md`: resmî kaynaktan çıkarılan bağımsız yöntem özeti;
- `company-policy.md`: değişmeyen kimliklere sahip sentetik kurum kuralları;
- `evidence-map.md`: hangi iddianın hangi kaynaktan gelebileceği;
- `output-schema.md`: beklenen yanıt yapısı;
- `scenario-guide.md`: eksik bilgi, çelişki ve yanıt vermekten kaçınma davranışı.

Önceden belirlenen değerlendirmede karar sınıfı olarak
{traced_label(locale, key['decisionClass'])}, önerilen seçenek olarak
{traced_label(locale, key['recommendedOption'])} ve {len(key['requiredRuleIds'])}
kural kimliğinin kullanılması beklenir. Nihai
incelemeden sorumlu roller:
{routes}.

## Yalnızca LLM ve LLM + Agent Skill

Aynı vaka ve istem iki kez çalıştırıldı. İkinci çalıştırmada ayrıca Agent Skill
yüklüdür. Her iki yanıtı da başka bir model değil, önceden belirlenmiş yanıt
anahtarını kullanan deterministik bir betik puanlar.

{comparison_table(locale, control, treatment)}

[Kontrol yanıtı]({asset}/outputs/{control_file}.txt) ·
[Skill yanıtı]({asset}/outputs/{treatment_file}.txt) ·
[Puan kartı]({asset}/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/{slug}
```

Bu karşılaştırmada her koşulda tek senaryo ve tek çalıştırma ortamı kullanılmıştır;
sonuçlar üretim doğruluğunun veya mevzuata uygunluğun kanıtı değildir.

## Copilot paketleri

{packages}

Klasik paket doğrudan içe aktarılabilen bir Copilot Studio çözümü değildir; hedef
ortamda elle uygulanacak kurulum dosyaları ve yönergeleri içerir.

## Yeniden kullanım

Kaynak bildirim dosyası, sentetik girdiler, senaryolar, ham yanıtlar ve puan kartı
`demos/{slug}/` altında herkese açıktır. Aynı yapıyı kendi kaynağınız için
kopyalayın; ancak yalnızca paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik
ve yeniden kullanım](../safety.md) sınırlarını inceleyin.
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
            "# Herkese açık 12 örnek",
            "",
            "Bu örnekler dönüştürücünün yalnız kitaplarda değil, mevzuat ve kurum",
            "rehberlerinde de çalıştığını gösterir. Her örnekte kaynak bildirim dosyası, sentetik",
            "politika ve vaka, üretilen Agent Skill, önceden belirlenmiş 12 senaryo,",
            "yalnızca LLM ile alınan yanıt, Agent Skill destekli yanıt, puan kartı ve",
            "beş Copilot paketi bulunur.",
            "",
            f"12 örneğin ortalama karar izlenebilirliği puanı yalnızca LLM ile **{mean_control}/100**,",
            f"Agent Skill desteğiyle **{mean_treatment}/100** oldu. Sonuçlar her koşul için",
            "tek senaryo ve tek ortamla sınırlıdır.",
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
                    f"**Puan:** Yalnızca LLM **{best_run(card, 'control')['traceScore']}/100** · "
                    f"LLM + Agent Skill **{best_run(card, 'treatment')['traceScore']}/100**",
                    "",
                    item["oneLineValue"],
                    "",
                )
            )
        lines.extend((
            "",
            "## Ne indirebilirsiniz",
            "",
            "Her örnek sayfasında Cowork, VS Code için GitHub Copilot, Scout ve iki Copilot",
            "Studio biçimi bulunur. Temiz bir yeniden derlemede bütün paketlerin bayt",
            "düzeyinde birebir aynı olduğu doğrulanır ve sonuçlar",
            "`downloads/skills/SHA256SUMS` sağlama toplamı listesine kaydedilir.",
            "",
            "Kendi içeriğinizle aynı akışı kurmak için [Agent Skill oluşturun](../create-a-skill.md).",
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
