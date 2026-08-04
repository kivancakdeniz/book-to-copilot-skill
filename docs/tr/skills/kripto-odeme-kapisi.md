# Kripto ödeme kapısı

<span class="bts-skill-kicker">Ödeme hizmetleri ve kripto varlıklar</span>

**Payments, Compliance, Legal ve ürün ekipleri** için. Kripto işlevinin ödeme akışındaki rolünü ürün sınırı ve lansman kapısıyla inceler.

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
| Karar sınıfı | `reject-payment-flow` |
| Seçenek | `remove-crypto-checkout` |
| Zorunlu kural | 6 kimlik |
| İnsan rotası | Payments Counsel · Compliance · Product |

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

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `KRP-01`

[Kontrol yanıtı](../../assets/skills/kripto-odeme-kapisi/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/kripto-odeme-kapisi/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/kripto-odeme-kapisi/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/kripto-odeme-kapisi
```

Kontrol çalıştırması 6 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 6 tanesine atıf yaptı. Tam karar sınıfını (`reject-payment-flow`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/kripto-odeme-kapisi/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Ödemelerde Kripto Varlıkların Kullanılmamasına Dair Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210416-4.htm) — Türkiye Cumhuriyet Merkez Bankası / T.C. Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/kripto-odeme-kapisi/skill/public-method.md` |
| Sentetik şirket politikası | `demos/kripto-odeme-kapisi/sources/company-policy.md` |
| Sentetik vaka | `demos/kripto-odeme-kapisi/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/kripto-odeme-kapisi/evaluation/` |
| Taşınabilir skill | `demos/kripto-odeme-kapisi/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
