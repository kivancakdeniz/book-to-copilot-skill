# ETK/IYS ileti kararı

<span class="bts-skill-kicker">Ticari elektronik ileti</span>

**CRM, Compliance ve Legal ekipleri** için. Kampanya kitlesini kişi-kanal kanıtı ve bastırma kapısıyla inceler.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>20</b><span>LLM only</span></li>
  <li><b>80</b><span>LLM + skill</span></li>
  <li><b>4/4</b><span>kural atfı</span></li>
  <li><b>12</b><span>kilitli senaryo</span></li>
</ul>

## Skill ne ekledi

Kontrol yanıtı 0/4 kural kimliğine, skill yanıtı 4/4 kural kimliğine atıf yaptı. Skill'in değeri daha uzun metin üretmesi değil; şirket politikasını, kanıt boşluklarını ve insan yetki sınırını aynı karar kaydında görünür kılmasıdır.

Copilot onay veremez, yayımlayamaz veya operasyonel eylem uygulayamaz.

## Karar sözleşmesi

| Kilitli beklenti | Değer |
| --- | --- |
| Karar sınıfı | `do-not-send` |
| Seçenek | `suppress-unverified-audience` |
| Zorunlu kural | 4 kimlik |
| İnsan rotası | CRM Owner · Compliance · Legal |

Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik skorlayıcı tarafından kullanılır.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 4 | 4 / 4 |
| Tam karar sınıfı yazıldı | hayır | hayır |
| Adlandırılmış seçenek yazıldı | hayır | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **20 / 100** | **80 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `ETK-E01`

[Kontrol yanıtı](../../assets/skills/etk-iys-ileti-karari/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/etk-iys-ileti-karari/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/etk-iys-ileti-karari/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/etk-iys-ileti-karari
```

Kontrol çalıştırması 4 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 4 tanesine atıf yaptı. Skill çalıştırması kilitli beklenen sınıf (`do-not-send`) yerine daha temkinli bir sınıf seçti; sınıf çağrısı insan incelemesinde kalır.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/etk-iys-ileti-karari/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6563.pdf) — Mevzuat Bilgi Sistemi |
| Resmî kaynak (yalnız metadata) | [Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2015/07/20150715-4.htm) — Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/etk-iys-ileti-karari/skill/public-method.md` |
| Sentetik şirket politikası | `demos/etk-iys-ileti-karari/sources/company-policy.md` |
| Sentetik vaka | `demos/etk-iys-ileti-karari/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/etk-iys-ileti-karari/evaluation/` |
| Taşınabilir skill | `demos/etk-iys-ileti-karari/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
