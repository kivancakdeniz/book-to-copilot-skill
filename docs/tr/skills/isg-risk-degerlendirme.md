# İSG risk değerlendirmesi: değişiklikten devreye alma kapısına

<span class="bts-skill-kicker">İş sağlığı ve güvenliği</span>

**İSG, operasyon, bakım ve mühendislik ekipleri** için. Değişiklik risklerini katılım, kontrol ve devreye alma kanıtlarıyla görünür kılar.

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
| Karar sınıfı | `renew-assessment` |
| Seçenek | `hold-commissioning` |
| Zorunlu kural | 7 kimlik |
| İnsan rotası | İşveren · İSG profesyonelleri · çalışan temsilcileri |

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

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `ISG-01`

[Kontrol yanıtı](../../assets/skills/isg-risk-degerlendirme/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/isg-risk-degerlendirme/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/isg-risk-degerlendirme/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/isg-risk-degerlendirme
```

Kontrol çalıştırması 7 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 7 tanesine atıf yaptı. Tam karar sınıfını (`renew-assessment`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/isg-risk-degerlendirme/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [İş Sağlığı ve Güvenliği Risk Değerlendirmesi Yönetmeliği](https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm) — T.C. Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/isg-risk-degerlendirme/skill/public-method.md` |
| Sentetik şirket politikası | `demos/isg-risk-degerlendirme/sources/company-policy.md` |
| Sentetik vaka | `demos/isg-risk-degerlendirme/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/isg-risk-degerlendirme/evaluation/` |
| Taşınabilir skill | `demos/isg-risk-degerlendirme/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
