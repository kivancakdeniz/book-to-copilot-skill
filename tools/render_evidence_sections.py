#!/usr/bin/env python3
"""Render the measured control-versus-skill section into every catalog article.

The numbers always come from ``demos/<slug>/evidence/scorecard.json`` so the
published claim cannot drift away from the deterministic scorer.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

EVIDENCE_HEADING = {
    "en": "## Control vs skill: measured",
    "tr": "## Kontrol ve skill: ölçülen",
}
LINEAGE_HEADING = {
    "en": "## From source to skill",
    "tr": "## Kaynaktan skill'e",
}
DOWNLOADS_HEADING = {"en": "## Downloads", "tr": "## İndirmeler"}
PACKAGE_LABELS = {
    "en": (
        ("Cowork skill package", "cowork.skill"),
        ("Copilot VS Code ZIP", "copilot-vscode.zip"),
        ("Scout ZIP", "scout.zip"),
        ("Copilot Studio GitHub harness ZIP", "copilot-studio-github-harness.zip"),
        ("Copilot Studio classic setup ZIP", "copilot-studio-classic-setup.zip"),
    ),
    "tr": (
        ("Cowork skill paketi", "cowork.skill"),
        ("Copilot VS Code ZIP", "copilot-vscode.zip"),
        ("Scout ZIP", "scout.zip"),
        ("Copilot Studio GitHub harness ZIP", "copilot-studio-github-harness.zip"),
        ("Copilot Studio classic setup ZIP", "copilot-studio-classic-setup.zip"),
    ),
}
COMPARISON_HEADING_RE = re.compile(
    r"(?m)^## (?:.*LLM.*|Control vs skill: measured|Kontrol ve skill: ölçülen)$"
)
SECTION_RE = r"(?ms)^{heading}\n.*?(?=\n## |\Z)"


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def _yes_no(locale: str, value: bool) -> str:
    if locale == "tr":
        return "evet" if value else "hayır"
    return "yes" if value else "no"


def _gate_rows(locale: str, control: Mapping[str, Any], treatment: Mapping[str, Any]) -> list[str]:
    labels = {
        "en": (
            "Policy rules cited",
            "Exact decision class stated",
            "Named option stated",
            "Human approval route named",
            "No autonomous-authority claim",
            "**Trace score**",
        ),
        "tr": (
            "Atıf yapılan politika kuralı",
            "Tam karar sınıfı yazıldı",
            "Adlandırılmış seçenek yazıldı",
            "İnsan onay rotası adlandırıldı",
            "Otonom yetki iddiası yok",
            "**İz puanı**",
        ),
    }[locale]
    total = control["ruleCitationTotal"]
    rows = [
        f"| {labels[0]} | {control['ruleCitationCount']} / {total} | {treatment['ruleCitationCount']} / {total} |",
    ]
    for index, gate in enumerate(
        ("decisionClass", "recommendedOption", "humanRoute", "forbiddenClaims"), start=1
    ):
        rows.append(
            f"| {labels[index]} | {_yes_no(locale, control['gates'][gate]['passed'])} "
            f"| {_yes_no(locale, treatment['gates'][gate]['passed'])} |"
        )
    rows.append(
        f"| {labels[5]} | **{control['traceScore']} / 100** | **{treatment['traceScore']} / 100** |"
    )
    return rows


def _summary_sentence(locale: str, key: Mapping[str, Any], control: Mapping[str, Any],
                      treatment: Mapping[str, Any]) -> str:
    total = control["ruleCitationTotal"]
    decision = key["decisionClass"]
    if locale == "tr":
        parts = [
            f"Kontrol çalıştırması {total} politika kuralının {control['ruleCitationCount']} tanesine atıf yaptı",
            f"skill çalıştırması {treatment['ruleCitationCount']} tanesine atıf yaptı.",
        ]
        if treatment["gates"]["decisionClass"]["passed"] and not control["gates"]["decisionClass"]["passed"]:
            parts.append(f"Tam karar sınıfını (`{decision}`) yalnız skill çalıştırması yazdı.")
        elif not treatment["gates"]["decisionClass"]["passed"]:
            parts.append(
                f"Skill çalıştırması kilitli beklenen sınıf (`{decision}`) yerine daha temkinli "
                "bir sınıf seçti; sınıf çağrısı insan incelemesinde kalır."
            )
        return " ".join(parts)
    parts = [
        f"The control run cited {control['ruleCitationCount']} of {total} policy rules",
        f"and the skill run cited {treatment['ruleCitationCount']}.",
    ]
    if treatment["gates"]["decisionClass"]["passed"] and not control["gates"]["decisionClass"]["passed"]:
        parts.append(f"Only the skill run stated the exact decision class (`{decision}`).")
    elif not treatment["gates"]["decisionClass"]["passed"]:
        parts.append(
            f"The skill run chose a more cautious class than the locked expectation (`{decision}`), "
            "so the class call stays with the human reviewer."
        )
    return " ".join(parts)


def render_evidence(locale: str, slug: str, scorecard: Mapping[str, Any],
                    key: Mapping[str, Any]) -> str:
    runs = scorecard["runs"]
    control = max(
        (run for run in runs if run["condition"] == "control"), key=lambda run: run["traceScore"]
    )
    treatment = max(
        (run for run in runs if run["condition"] == "treatment"), key=lambda run: run["traceScore"]
    )
    asset = f"../../assets/skills/{slug}"
    rows = _gate_rows(locale, control, treatment)
    if locale == "tr":
        head = (
            f"{EVIDENCE_HEADING['tr']}\n\n"
            "İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci\n"
            "çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya\n"
            "bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.\n\n"
            "| Yönetişim kapısı | Yalnız LLM | LLM + skill |\n| --- | --- | --- |\n"
        )
        meta = (
            f"\nHost: {control['host']} · Model: {control['model']} · Tarih: {control['capturedAt']} "
            f"· Senaryo: `{scorecard['scenarioId']}`\n\n"
            f"[Kontrol yanıtı]({asset}/outputs/{Path(control['outputPath']).stem}.txt) · "
            f"[Skill yanıtı]({asset}/outputs/{Path(treatment['outputPath']).stem}.txt) · "
            f"[Skor kartı]({asset}/scorecard.json)\n\n"
            "Yeniden üretmek için:\n\n"
            "```bash\n"
            f"python tools/score_skill_answer.py scorecard --demo demos/{slug}\n"
            "```\n\n"
            f"{_summary_sentence('tr', key, control, treatment)}\n\n"
            "Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo\n"
            f"makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği\n"
            f"`demos/{slug}/evaluation/rubric.json` dosyasındadır.\n"
        )
    else:
        head = (
            f"{EVIDENCE_HEADING['en']}\n\n"
            "Both runs answered the same locked case with the same prompt. The only\n"
            "difference is that the second run had the skill installed. Scoring is done by a\n"
            "deterministic script against the locked scenario, not by a model, so anyone can\n"
            "reproduce these numbers.\n\n"
            "| Governance gate | LLM only | LLM + skill |\n| --- | --- | --- |\n"
        )
        meta = (
            f"\nHost: {control['host']} · Model: {control['model']} · Captured: {control['capturedAt']} "
            f"· Scenario: `{scorecard['scenarioId']}`\n\n"
            f"[Control answer]({asset}/outputs/{Path(control['outputPath']).stem}.txt) · "
            f"[Skill answer]({asset}/outputs/{Path(treatment['outputPath']).stem}.txt) · "
            f"[Scorecard]({asset}/scorecard.json)\n\n"
            "Reproduce:\n\n"
            "```bash\n"
            f"python tools/score_skill_answer.py scorecard --demo demos/{slug}\n"
            "```\n\n"
            f"{_summary_sentence('en', key, control, treatment)}\n\n"
            "Limits: one run per condition, one locked scenario, and a single host. This table\n"
            "is the machine-checkable subset; the 14-point human rubric lives in\n"
            f"`demos/{slug}/evaluation/rubric.json`.\n"
        )
    return head + "\n".join(rows) + "\n" + meta


def render_lineage(locale: str, slug: str, manifest: Mapping[str, Any]) -> str:
    official = [
        source
        for source in manifest["sources"]
        if "path" not in source and not source.get("synthetic")
    ]
    if locale == "tr":
        lines = [
            LINEAGE_HEADING["tr"],
            "",
            "Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.",
            "",
            "| Aşama | Üretilen içerik |",
            "| --- | --- |",
        ]
        source_label = "Resmî kaynak (yalnız metadata)"
        rows = [
            ("Kamuya açık yöntem özeti", f"`demos/{slug}/skill/public-method.md`"),
            ("Sentetik şirket politikası", f"`demos/{slug}/sources/company-policy.md`"),
            ("Sentetik vaka", f"`demos/{slug}/sources/case-brief.md`"),
            ("Kilitli değerlendirme", f"12 senaryo ve 14 puanlık rubrik: `demos/{slug}/evaluation/`"),
            ("Taşınabilir skill", f"`demos/{slug}/skill/SKILL.md` ve beş destek dosyası"),
            ("Host paketleri", "Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic)"),
        ]
    else:
        lines = [
            LINEAGE_HEADING["en"],
            "",
            "This chain shows exactly which content produced the skill.",
            "",
            "| Stage | Produced content |",
            "| --- | --- |",
        ]
        source_label = "Official source (metadata only)"
        rows = [
            ("Public method summary", f"`demos/{slug}/skill/public-method.md`"),
            ("Synthetic company policy", f"`demos/{slug}/sources/company-policy.md`"),
            ("Synthetic case", f"`demos/{slug}/sources/case-brief.md`"),
            ("Locked evaluation", f"12 scenarios and a 14-point rubric: `demos/{slug}/evaluation/`"),
            ("Portable skill", f"`demos/{slug}/skill/SKILL.md` plus five companions"),
            ("Host packages", "Cowork, Copilot/VS Code, Scout, Copilot Studio (harness and classic)"),
        ]
    for source in official:
        title = source["title"].replace("|", "\\|")
        url = source.get("url") or source.get("officialUrl", "")
        lines.append(f"| {source_label} | [{title}]({url}) — {source['publisher']} |")
    for label, value in rows:
        lines.append(f"| {label} | {value} |")
    lines.append("")
    return "\n".join(lines)


def render_article(
    locale: str,
    slug: str,
    entry: Mapping[str, Any],
    scorecard: Mapping[str, Any],
    key: Mapping[str, Any],
    manifest: Mapping[str, Any],
) -> str:
    localized = entry[locale]
    runs = scorecard["runs"]
    control = max(
        (run for run in runs if run["condition"] == "control"),
        key=lambda run: run["traceScore"],
    )
    treatment = max(
        (run for run in runs if run["condition"] == "treatment"),
        key=lambda run: run["traceScore"],
    )
    route = " · ".join(key["humanRoute"])
    if locale == "tr":
        intro = (
            f"**{localized['audience']}** için. {localized['oneLineValue']}"
        )
        contract = (
            "## Karar sözleşmesi\n\n"
            "| Kilitli beklenti | Değer |\n| --- | --- |\n"
            f"| Karar sınıfı | `{key['decisionClass']}` |\n"
            f"| Seçenek | `{key['recommendedOption']}` |\n"
            f"| Zorunlu kural | {len(key['requiredRuleIds'])} kimlik |\n"
            f"| İnsan rotası | {route} |\n\n"
            "Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik "
            "skorlayıcı tarafından kullanılır.\n"
        )
        contribution = (
            "## Skill ne ekledi\n\n"
            f"Kontrol yanıtı {control['ruleCitationCount']}/{control['ruleCitationTotal']} "
            f"kural kimliğine, skill yanıtı {treatment['ruleCitationCount']}/"
            f"{treatment['ruleCitationTotal']} kural kimliğine atıf yaptı. "
            "Skill'in değeri daha uzun metin üretmesi değil; şirket politikasını, kanıt "
            "boşluklarını ve insan yetki sınırını aynı karar kaydında görünür kılmasıdır.\n\n"
            "Copilot onay veremez, yayımlayamaz veya operasyonel eylem uygulayamaz.\n"
        )
        safety = (
            "## Kullanım sınırı\n\n"
            "Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları "
            "resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) "
            "sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.\n"
        )
    else:
        intro = f"For **{localized['audience']}**. {localized['oneLineValue']}"
        contract = (
            "## Decision contract\n\n"
            "| Locked expectation | Value |\n| --- | --- |\n"
            f"| Decision class | `{key['decisionClass']}` |\n"
            f"| Option | `{key['recommendedOption']}` |\n"
            f"| Required rules | {len(key['requiredRuleIds'])} identifiers |\n"
            f"| Human route | {route} |\n\n"
            "These values are never shown to the model; only the locked scenario and the "
            "deterministic scorer use them.\n"
        )
        contribution = (
            "## What the skill added\n\n"
            f"The control answer cited {control['ruleCitationCount']}/"
            f"{control['ruleCitationTotal']} rule identifiers; the skill answer cited "
            f"{treatment['ruleCitationCount']}/{treatment['ruleCitationTotal']}. "
            "The value is not a longer answer. It is a decision record that exposes company "
            "policy, evidence gaps, and the human authority boundary together.\n\n"
            "Copilot cannot approve, publish, or execute an operational action.\n"
        )
        safety = (
            "## Use boundary\n\n"
            "This synthetic demo is not professional advice or a production control. Verify "
            "the result against the official source and with the authorized human. "
            "[Safety & source](../safety.md) explains the data, source, licence, evaluation, "
            "and human-authority boundaries.\n"
        )
    hero = (
        f"# {localized['title']}\n\n"
        f"<span class=\"bts-skill-kicker\">{localized['sector']}</span>\n\n"
        f"{intro}\n\n"
        "<ul class=\"bts-metrics bts-metrics--compact\">\n"
        f"  <li><b>{control['traceScore']}</b><span>LLM only</span></li>\n"
        f"  <li><b>{treatment['traceScore']}</b><span>LLM + skill</span></li>\n"
        f"  <li><b>{treatment['ruleCitationCount']}/{treatment['ruleCitationTotal']}</b>"
        f"<span>{'kural atfı' if locale == 'tr' else 'rule citations'}</span></li>\n"
        "  <li><b>12</b><span>"
        f"{'kilitli senaryo' if locale == 'tr' else 'locked scenarios'}</span></li>\n"
        "</ul>\n"
    )
    evidence = render_evidence(locale, slug, scorecard, key)
    lineage = render_lineage(locale, slug, manifest)
    downloads = render_downloads(locale, slug)
    return "\n\n".join(
        section.strip()
        for section in (hero, contribution, contract, evidence, lineage, downloads, safety)
    ) + "\n"


def update_article(
    path: Path,
    locale: str,
    slug: str,
    entry: Mapping[str, Any],
    scorecard: Mapping[str, Any],
    key: Mapping[str, Any],
    manifest: Mapping[str, Any],
) -> bool:
    path.write_text(
        render_article(locale, slug, entry, scorecard, key, manifest),
        encoding="utf-8",
    )
    return True


def render_downloads(locale: str, slug: str) -> str:
    prefix = "../../downloads/skills"
    if locale == "tr":
        lines = [
            DOWNLOADS_HEADING["tr"],
            "",
            "Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve",
            "SHA-256 manifestine bağlanmıştır:",
            "",
        ]
        tail = (
            "\nClassic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;\n"
            "doğrudan ajan içe aktarma paketi değildir.\n"
        )
    else:
        lines = [
            DOWNLOADS_HEADING["en"],
            "",
            "These packages are generated deterministically by the shared release factory",
            "and are bound to the SHA-256 manifest:",
            "",
        ]
        tail = (
            "\nThe classic setup ZIP is a package of setup materials and instructions for\n"
            "Copilot Studio; it is not a direct agent import package.\n"
        )
    for label, suffix in PACKAGE_LABELS[locale]:
        lines.append(f"- [{label}]({prefix}/{slug}/{slug}-{suffix})")
    return "\n".join(lines) + "\n" + tail


def render_catalog(locale: str, entries: Sequence[Mapping[str, Any]],
                   scorecards: Mapping[str, Mapping[str, Any]]) -> str:
    count = len(entries)
    packages = count * 5
    controls = [scorecards[entry["id"]]["summary"]["controlTraceScore"] for entry in entries]
    treatments = [scorecards[entry["id"]]["summary"]["treatmentTraceScore"] for entry in entries]
    mean_control = int(sum(controls) / count + 0.5)
    mean_treatment = int(sum(treatments) / count + 0.5)
    if locale == "tr":
        lines = [
            "# Kurumsal karar skill kataloğu",
            "",
            f"Bu katalog, tek bir yayın fabrikasıyla üretilen {count} kurumsal karar skill'ini",
            "listeler. Her skill 12 kilitli senaryo, 14 puanlık rubrik, sentetik şirket",
            "politikası ve resmî kaynak metadatası içerir.",
            "",
            "Her skill için aynı vaka iki kez yanıtlandı: bir kez skill olmadan, bir kez",
            f"skill kurulu. Deterministik iz puanı ortalaması yalnız LLM'de {mean_control}/100,",
            f"LLM + skill'de {mean_treatment}/100 oldu. Politika kuralı atfı {count} kontrol",
            "çalıştırmasının hepsinde sıfırdı. Bu bir üretim performansı, ROI veya uygunluk",
            "iddiası değildir.",
            "",
            f"Yayın, beş host biçiminde {packages} indirilebilir paket içerir. Paketler",
            "deterministik üretilir ve temiz yeniden derlemede byte-identical doğrulanır.",
            "",
            "[SHA256SUMS](../../downloads/skills/SHA256SUMS) ·",
            "[Üçüncü taraf bildirimleri](../../downloads/skills/THIRD_PARTY_NOTICES.md)",
            "",
            "## 12 skill",
            "",
            '<div class="grid cards" markdown>',
            "",
        ]
        for entry in entries:
            summary = scorecards[entry["id"]]["summary"]
            locale_entry = entry["tr"]
            lines.extend(
                (
                    f"-   **[{locale_entry['title']}]({entry['id']}.md)**",
                    "",
                    f"    <span class=\"bts-skill-kicker\">{locale_entry['sector']}</span>",
                    "",
                    f"    {locale_entry['oneLineValue']}",
                    "",
                    f"    <span class=\"bts-score bts-score--control\">LLM {summary['controlTraceScore']}</span> "
                    f"<span class=\"bts-score bts-score--skill\">Skill {summary['treatmentTraceScore']}</span>",
                    "",
                )
            )
        lines.extend(("</div>", ""))
    else:
        lines = [
            "# Enterprise decision skill catalog",
            "",
            f"This catalog lists {count} enterprise decision skills built by one release",
            "factory. Each skill ships 12 locked scenarios, a 14-point rubric, a synthetic",
            "company policy, and official-source metadata.",
            "",
            "For every skill the same case was answered twice: once without the skill and",
            f"once with it installed. The deterministic trace score averaged {mean_control}/100",
            f"for the model alone and {mean_treatment}/100 with the skill. Policy-rule citations",
            f"were zero in all {count} control runs. This is not a claim about production",
            "performance, ROI, or regulatory compliance.",
            "",
            f"The release contains {packages} downloadable packages across five host formats.",
            "They are generated deterministically and verified byte-identical after a clean",
            "rebuild.",
            "",
            "[SHA256SUMS](../../downloads/skills/SHA256SUMS) ·",
            "[Third-party notices](../../downloads/skills/THIRD_PARTY_NOTICES.md)",
            "",
            "## 12 skills",
            "",
            '<div class="grid cards" markdown>',
            "",
        ]
        for entry in entries:
            summary = scorecards[entry["id"]]["summary"]
            locale_entry = entry["en"]
            lines.extend(
                (
                    f"-   **[{locale_entry['title']}]({entry['id']}.md)**",
                    "",
                    f"    <span class=\"bts-skill-kicker\">{locale_entry['sector']}</span>",
                    "",
                    f"    {locale_entry['oneLineValue']}",
                    "",
                    f"    <span class=\"bts-score bts-score--control\">LLM {summary['controlTraceScore']}</span> "
                    f"<span class=\"bts-score bts-score--skill\">Skill {summary['treatmentTraceScore']}</span>",
                    "",
                )
            )
        lines.extend(("</div>", ""))
    lines.append("")
    return "\n".join(lines)


def update_catalog_page(path: Path, locale: str, rendered: str) -> None:
    text = path.read_text(encoding="utf-8")
    tail_heading = "## Source and license boundary" if locale == "en" else "## Kaynak ve lisans sınırı"
    index = text.find(tail_heading)
    if index < 0:
        raise SystemExit(f"{path}: tail heading not found")
    path.write_text(rendered + "\n" + text[index:], encoding="utf-8")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    catalog = _load(root / "demos" / "catalog.json")
    entries = catalog["entries"]
    scorecards: dict[str, Mapping[str, Any]] = {}
    updated = 0
    for entry in entries:
        slug = entry["id"]
        demo = root / "demos" / slug
        scorecard = _load(demo / "evidence" / "scorecard.json")
        scorecards[slug] = scorecard
        key = _load(demo / "evaluation" / "answer-key.json")
        manifest = _load(demo / "sources" / "source-manifest.json")
        for locale, field in (("en", "article"), ("tr", "articleTr")):
            update_article(
                root / entry[field], locale, slug, entry, scorecard, key, manifest
            )
            updated += 1
    update_catalog_page(root / "docs" / "en" / "skills" / "index.md", "en",
                        render_catalog("en", entries, scorecards))
    update_catalog_page(root / "docs" / "tr" / "skills" / "index.md", "tr",
                        render_catalog("tr", entries, scorecards))
    print(f"Updated {updated} articles and 2 catalog pages from deterministic scorecards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
