# BDDK uzaktan müşteri edinimi

<span class="bts-skill-kicker">Bankacılık</span>

**Dijital bankacılık, güvenlik, Uyum ve Hukuk ekipleri** için. Uzaktan edinim akışını kanıt, kontrol ve canlıya geçiş kapılarıyla sınar.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>40</b><span>LLM only</span></li>
  <li><b>80</b><span>LLM + skill</span></li>
  <li><b>7/7</b><span>kural atfı</span></li>
  <li><b>12</b><span>kilitli senaryo</span></li>
</ul>

## Skill ne ekledi

Kontrol yanıtı 0/7 kural kimliğine, skill yanıtı 7/7 kural kimliğine atıf yaptı. Skill'in değeri daha uzun metin üretmesi değil; şirket politikasını, kanıt boşluklarını ve insan yetki sınırını aynı karar kaydında görünür kılmasıdır.

Copilot onay veremez, yayımlayamaz veya operasyonel eylem uygulayamaz.

## Karar sözleşmesi

| Kilitli beklenti | Değer |
| --- | --- |
| Karar sınıfı | `reject-flow` |
| Seçenek | `manual-onboarding-fallback` |
| Zorunlu kural | 7 kimlik |
| İnsan rotası | Güvenlik · Uyum · Hukuk |

Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik skorlayıcı tarafından kullanılır.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı yazıldı | hayır | hayır |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **80 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `BDK-01`

[Kontrol yanıtı](../../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/bddk-uzaktan-musteri-edinimi/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/bddk-uzaktan-musteri-edinimi
```

Kontrol çalıştırması 7 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 7 tanesine atıf yaptı. Skill çalıştırması kilitli beklenen sınıf (`reject-flow`) yerine daha temkinli bir sınıf seçti; sınıf çağrısı insan incelemesinde kalır.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/bddk-uzaktan-musteri-edinimi/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Bankalarca Kullanılacak Uzaktan Kimlik Tespiti Yöntemlerine ve Elektronik Ortamda Sözleşme İlişkisinin Kurulmasına İlişkin Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210401-7.htm) — Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/bddk-uzaktan-musteri-edinimi/skill/public-method.md` |
| Sentetik şirket politikası | `demos/bddk-uzaktan-musteri-edinimi/sources/company-policy.md` |
| Sentetik vaka | `demos/bddk-uzaktan-musteri-edinimi/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/bddk-uzaktan-musteri-edinimi/evaluation/` |
| Taşınabilir skill | `demos/bddk-uzaktan-musteri-edinimi/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
