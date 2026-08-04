# TİTCK ilaç tanıtımı: hedef kitle ve yayın kapısı

<span class="bts-skill-kicker">İlaç ve sağlık iletişimi</span>

**Medical, Regulatory, Legal ve pazarlama ekipleri** için. Ürün statüsü, hedef kitle ve kanal erişimini insan yayın incelemesine bağlar.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>40</b><span>LLM only</span></li>
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
| Karar sınıfı | `do-not-publish` |
| Seçenek | `professional-channel-review` |
| Zorunlu kural | 7 kimlik |
| İnsan rotası | Medical · Regulatory · Legal |

Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik skorlayıcı tarafından kullanılır.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `TTK-01`

[Kontrol yanıtı](../../assets/skills/titck-ilac-tanitimi/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/titck-ilac-tanitimi/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/titck-ilac-tanitimi/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/titck-ilac-tanitimi
```

Kontrol çalıştırması 7 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 7 tanesine atıf yaptı. Tam karar sınıfını (`do-not-publish`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/titck-ilac-tanitimi/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik](https://www.titck.gov.tr/mevzuat/beseri-tibbi-urunlerin-tanitim-faaliyetleri-hakkinda-yonetmelik-27122018172726) — Türkiye İlaç ve Tıbbî Cihaz Kurumu (TİTCK) |
| Resmî kaynak (yalnız metadata) | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik - Resmî Gazete yayımı](https://www.resmigazete.gov.tr/eskiler/2015/07/20150703-2.htm) — T.C. Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/titck-ilac-tanitimi/skill/public-method.md` |
| Sentetik şirket politikası | `demos/titck-ilac-tanitimi/sources/company-policy.md` |
| Sentetik vaka | `demos/titck-ilac-tanitimi/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/titck-ilac-tanitimi/evaluation/` |
| Taşınabilir skill | `demos/titck-ilac-tanitimi/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
