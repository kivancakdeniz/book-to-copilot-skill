# MASAK müşteri kabul

<span class="bts-skill-kicker">Finansal suçlarla mücadele</span>

**AML, Compliance ve müşteri kabul ekipleri** için. Kimlik, nihai faydalanıcı ve fon kaynağı boşluklarını insan incelemesine yönlendirir.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>20</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>8/8</b><span>kural atfı</span></li>
  <li><b>12</b><span>kilitli senaryo</span></li>
</ul>

## Skill ne ekledi

Kontrol yanıtı 0/8 kural kimliğine, skill yanıtı 8/8 kural kimliğine atıf yaptı. Skill'in değeri daha uzun metin üretmesi değil; şirket politikasını, kanıt boşluklarını ve insan yetki sınırını aynı karar kaydında görünür kılmasıdır.

Copilot onay veremez, yayımlayamaz veya operasyonel eylem uygulayamaz.

## Karar sözleşmesi

| Kilitli beklenti | Değer |
| --- | --- |
| Karar sınıfı | `enhanced-review` |
| Seçenek | `hold-onboarding` |
| Zorunlu kural | 8 kimlik |
| İnsan rotası | AML Officer · Compliance |

Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik skorlayıcı tarafından kullanılır.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 8 | 8 / 8 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | hayır | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **20 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `AML-01`

[Kontrol yanıtı](../../assets/skills/masak-musteri-kabul/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/masak-musteri-kabul/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/masak-musteri-kabul/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/masak-musteri-kabul
```

Kontrol çalıştırması 8 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 8 tanesine atıf yaptı. Tam karar sınıfını (`enhanced-review`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/masak-musteri-kabul/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Suç gelirlerinin aklanmasının ve terörün finansmanının önlenmesine dair tedbirler hakkında yönetmelik](https://masak.hmb.gov.tr/suc-gelirlerinin-aklanmasinin-ve-terorun-finansmaninin-onlenmesine-dair-tedbirler-hakkinda-yonetmelik-3/) — MASAK |
| Kamuya açık yöntem özeti | `demos/masak-musteri-kabul/skill/public-method.md` |
| Sentetik şirket politikası | `demos/masak-musteri-kabul/sources/company-policy.md` |
| Sentetik vaka | `demos/masak-musteri-kabul/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/masak-musteri-kabul/evaluation/` |
| Taşınabilir skill | `demos/masak-musteri-kabul/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
