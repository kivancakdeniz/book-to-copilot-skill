# İndirimli fiyat denetimi

<span class="bts-skill-kicker">E-ticaret ve tüketici hukuku</span>

**E-ticaret, fiyatlandırma ve Compliance ekipleri** için. Fiyat geçmişi ile kampanya iddiasını izlenebilir bir yayın kararında buluşturur.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>20</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>7/7</b><span>kural atfı</span></li>
  <li><b>12</b><span>kilitli senaryo</span></li>
</ul>

## Skill ne ekledi

Kontrol yanıtı 0/7 kural kimliğine, skill yanıtı 7/7 kural kimliğine atıf yaptı. Skill'in değeri daha uzun metin üretmesi değil; şirket politikasını, kanıt boşluklarını ve insan yetki sınırını aynı karar kaydında görünür kılmasıdır.

Copilot onay veremez, yayımlayamaz veya operasyonel eylem uygulayamaz.

## Karar sözleşmesi

| Kilitli beklenti | Değer |
| --- | --- |
| Karar sınıfı | `revise-price-claim` |
| Seçenek | `advertise-25-percent` |
| Zorunlu kural | 7 kimlik |
| İnsan rotası | E-commerce Owner · Pricing Owner · Compliance · Legal |

Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik skorlayıcı tarafından kullanılır.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | hayır | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **20 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `FYT-01`

[Kontrol yanıtı](../../assets/skills/indirimli-fiyat-denetimi/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/indirimli-fiyat-denetimi/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/indirimli-fiyat-denetimi/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/indirimli-fiyat-denetimi
```

Kontrol çalıştırması 7 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 7 tanesine atıf yaptı. Tam karar sınıfını (`revise-price-claim`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/indirimli-fiyat-denetimi/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Fiyat bilgisi içeren reklamlar ile indirimli satış reklamları ve ticari uygulamaları hakkında kılavuz](https://tuketici.ticaret.gov.tr/haberler/fiyat-bilgisi-iceren-reklamlar-ile-indirimli-satis-reklamlari-ve-ticari-uygulamalari-hakkinda-kilavuz-guncellendi) — Ticaret Bakanlığı |
| Kamuya açık yöntem özeti | `demos/indirimli-fiyat-denetimi/skill/public-method.md` |
| Sentetik şirket politikası | `demos/indirimli-fiyat-denetimi/sources/company-policy.md` |
| Sentetik vaka | `demos/indirimli-fiyat-denetimi/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/indirimli-fiyat-denetimi/evaluation/` |
| Taşınabilir skill | `demos/indirimli-fiyat-denetimi/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
