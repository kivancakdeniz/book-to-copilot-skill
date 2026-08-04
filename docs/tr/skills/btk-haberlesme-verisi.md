# BTK haberleşme verisi

<span class="bts-skill-kicker">Telekom ve mahremiyet</span>

**Telekom Compliance, Privacy, DPO ve CRM ekipleri** için. Konum ve trafik verisi kullanımını amaç, rıza ve saklama kapılarıyla sınırlar.

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
| Karar sınıfı | `stop-processing` |
| Seçenek | `consent-first-redesign` |
| Zorunlu kural | 7 kimlik |
| İnsan rotası | Privacy Counsel · Telecom Compliance · DPO |

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

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `BTK-01`

[Kontrol yanıtı](../../assets/skills/btk-haberlesme-verisi/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/btk-haberlesme-verisi/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/btk-haberlesme-verisi/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/btk-haberlesme-verisi
```

Kontrol çalıştırması 7 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 7 tanesine atıf yaptı. Skill çalıştırması kilitli beklenen sınıf (`stop-processing`) yerine daha temkinli bir sınıf seçti; sınıf çağrısı insan incelemesinde kalır.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/btk-haberlesme-verisi/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Elektronik Haberleşme Sektöründe Kişisel Verilerin İşlenmesi ve Gizliliğin Korunmasına İlişkin Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2020/12/20201204-13.htm) — Bilgi Teknolojileri ve İletişim Kurumu / T.C. Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/btk-haberlesme-verisi/skill/public-method.md` |
| Sentetik şirket politikası | `demos/btk-haberlesme-verisi/sources/company-policy.md` |
| Sentetik vaka | `demos/btk-haberlesme-verisi/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/btk-haberlesme-verisi/evaluation/` |
| Taşınabilir skill | `demos/btk-haberlesme-verisi/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
