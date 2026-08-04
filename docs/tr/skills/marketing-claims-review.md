# Pazarlama iddiaları incelemesi

<span class="bts-skill-kicker">Pazarlama ve reklam uyumu</span>

**Pazarlama, Legal ve Compliance ekipleri** için. Reklam iddialarını dayanak, ifşa ve yayın kontrolleriyle sınar.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>40</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>9/9</b><span>kural atfı</span></li>
  <li><b>12</b><span>kilitli senaryo</span></li>
</ul>

## Skill ne ekledi

Kontrol yanıtı 0/9 kural kimliğine, skill yanıtı 9/9 kural kimliğine atıf yaptı. Skill'in değeri daha uzun metin üretmesi değil; şirket politikasını, kanıt boşluklarını ve insan yetki sınırını aynı karar kaydında görünür kılmasıdır.

Copilot onay veremez, yayımlayamaz veya operasyonel eylem uygulayamaz.

## Karar sözleşmesi

| Kilitli beklenti | Değer |
| --- | --- |
| Karar sınıfı | `approve-with-edits` |
| Seçenek | `evidence-bounded-campaign` |
| Zorunlu kural | 9 kimlik |
| İnsan rotası | Legal · Compliance |

Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik skorlayıcı tarafından kullanılır.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 9 | 9 / 9 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

Host: Microsoft 365 Copilot Cowork · Model: Claude Opus 4.8 · Tarih: 2026-08-04 · Senaryo: `MC-01`

[Kontrol yanıtı](../../assets/skills/marketing-claims-review/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/marketing-claims-review/outputs/treatment-auto-1.txt) · [Skor kartı](../../assets/skills/marketing-claims-review/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/marketing-claims-review
```

Kontrol çalıştırması 9 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 9 tanesine atıf yaptı. Tam karar sınıfını (`approve-with-edits`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/marketing-claims-review/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Advertising and Marketing on the Internet: Rules of the Road](https://www.ftc.gov/system/files/ftc_gov/pdf/bus28-rulesroad-2023_508.pdf) — U.S. Federal Trade Commission |
| Resmî kaynak (yalnız metadata) | [.com Disclosures: How to Make Effective Disclosures in Digital Advertising](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf) — U.S. Federal Trade Commission |
| Resmî kaynak (yalnız metadata) | [Guides Concerning the Use of Endorsements and Testimonials in Advertising (16 CFR Part 255)](https://www.ecfr.gov/api/versioner/v1/full/2023-07-26/title-16.xml?part=255) — Electronic Code of Federal Regulations |
| Kamuya açık yöntem özeti | `demos/marketing-claims-review/skill/public-method.md` |
| Sentetik şirket politikası | `demos/marketing-claims-review/sources/company-policy.md` |
| Sentetik vaka | `demos/marketing-claims-review/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/marketing-claims-review/evaluation/` |
| Taşınabilir skill | `demos/marketing-claims-review/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/marketing-claims-review/marketing-claims-review-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
