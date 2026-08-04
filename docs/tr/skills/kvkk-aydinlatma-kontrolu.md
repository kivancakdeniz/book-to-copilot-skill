# KVKK aydınlatma kontrolü

<span class="bts-skill-kicker">Veri koruma</span>

**Privacy, Compliance ve ürün ekipleri** için. Aydınlatma, rıza ve aktarım boşluklarını insan yayın kapısına bağlar.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>10</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>5/5</b><span>kural atfı</span></li>
  <li><b>12</b><span>kilitli senaryo</span></li>
</ul>

## Skill ne ekledi

Kontrol yanıtı 0/5 kural kimliğine, skill yanıtı 5/5 kural kimliğine atıf yaptı. Skill'in değeri daha uzun metin üretmesi değil; şirket politikasını, kanıt boşluklarını ve insan yetki sınırını aynı karar kaydında görünür kılmasıdır.

Copilot onay veremez, yayımlayamaz veya operasyonel eylem uygulayamaz.

## Karar sözleşmesi

| Kilitli beklenti | Değer |
| --- | --- |
| Karar sınıfı | `revise-before-launch` |
| Seçenek | `separate-notice-and-consent` |
| Zorunlu kural | 5 kimlik |
| İnsan rotası | Privacy Counsel · Data Protection/Compliance · Product Owner |

Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik skorlayıcı tarafından kullanılır.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 5 | 5 / 5 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | hayır | evet |
| İnsan onay rotası adlandırıldı | hayır | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **10 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `KVK-E01`

[Kontrol yanıtı](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/kvkk-aydinlatma-kontrolu/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/kvkk-aydinlatma-kontrolu
```

Kontrol çalıştırması 5 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 5 tanesine atıf yaptı. Tam karar sınıfını (`revise-before-launch`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/kvkk-aydinlatma-kontrolu/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [6698 sayılı Kişisel Verilerin Korunması Kanunu](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf) — Mevzuat Bilgi Sistemi |
| Resmî kaynak (yalnız metadata) | [Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ](https://www.resmigazete.gov.tr/eskiler/2018/03/20180310-5.htm) — Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/kvkk-aydinlatma-kontrolu/skill/public-method.md` |
| Sentetik şirket politikası | `demos/kvkk-aydinlatma-kontrolu/sources/company-policy.md` |
| Sentetik vaka | `demos/kvkk-aydinlatma-kontrolu/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/kvkk-aydinlatma-kontrolu/evaluation/` |
| Taşınabilir skill | `demos/kvkk-aydinlatma-kontrolu/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
