# Yatırım komitesi değerlendirmesi

<span class="bts-skill-kicker">Sermaye tahsisi</span>

**CFO, COO, CIO ve yatırım komitesi üyeleri** için. Sermaye brifingini kapılı ve kanıt atıflı bir komite karar kartına dönüştürür.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>40</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>6/6</b><span>kural atfı</span></li>
  <li><b>12</b><span>kilitli senaryo</span></li>
</ul>

## Skill ne ekledi

Kontrol yanıtı 0/6 kural kimliğine, skill yanıtı 6/6 kural kimliğine atıf yaptı. Skill'in değeri daha uzun metin üretmesi değil; şirket politikasını, kanıt boşluklarını ve insan yetki sınırını aynı karar kaydında görünür kılmasıdır.

Copilot onay veremez, yayımlayamaz veya operasyonel eylem uygulayamaz.

## Karar sözleşmesi

| Kilitli beklenti | Değer |
| --- | --- |
| Karar sınıfı | `conditional-approval` |
| Seçenek | `phased-automation` |
| Zorunlu kural | 6 kimlik |
| İnsan rotası | Investment Committee |

Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik skorlayıcı tarafından kullanılır.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 6 | 6 / 6 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

Host: Microsoft 365 Copilot Cowork · Model: Claude Opus 4.8 · Tarih: 2026-08-04 · Senaryo: `IC-01`

[Kontrol yanıtı](../../assets/skills/investment-committee/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/investment-committee/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/investment-committee/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/investment-committee
```

Kontrol çalıştırması 6 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 6 tanesine atıf yaptı. Tam karar sınıfını (`conditional-approval`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/investment-committee/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [The Green Book - UK government guidance on appraisal](https://assets.publishing.service.gov.uk/media/698dbcd17da91680ad7f4308/The_Green_Book_2026.pdf) — HM Treasury and Government Finance Function |
| Kamuya açık yöntem özeti | `demos/investment-committee/skill/public-method.md` |
| Sentetik şirket politikası | `demos/investment-committee/sources/company-policy.md` |
| Sentetik vaka | `demos/investment-committee/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/investment-committee/evaluation/` |
| Taşınabilir skill | `demos/investment-committee/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/investment-committee/investment-committee-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/investment-committee/investment-committee-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/investment-committee/investment-committee-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/investment-committee/investment-committee-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/investment-committee/investment-committee-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
