# BTK haberleşme verisi

[English](../../skills/btk-haberlesme-verisi.md)

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

## Bir bakışta

| Alan | Değer |
|---|---|
| Problem | Konum ve trafik verisiyle bireysel telekom upsell kampanyasının işleme kapısını incelemek |
| Baseline | Rıza kaydı, amaç eşlemesi ve saklama süresi sağlanmadan kampanya isteniyor |
| Beklenen sınıf | `stop-processing` |
| Beklenen seçenek | `consent-first-redesign` |
| İnsan kararı | Privacy Counsel + Telecom Compliance + DPO; telekom + KVKK ortak incelemesi |

## İş etkisi

Demo, CRM kampanya talebini izlenebilir bir veri kategorisi, amaç, rıza kanıtı,
güvenlik, saklama, insan kararı ve kampanya kapısı kaydına dönüştürür. Beklenen iş
etkisi daha erken kanıt boşluğu tespiti, daha az kampanya geri dönüşü, geri alınan
rızanın daha görünür yönetimi ve insan incelemesi için tutarlı bir dosyadır.
Üretim sonucu, mevzuata uyum veya hukuki yeterlilik garantisi değildir.

## Kaynak ve güvenlik

Kamusal yöntem kaynağı BTK düzenlemesinin T.C. Resmî Gazete yayınıdır. Paket
resmi içeriği yeniden dağıtmaz; yalnız resmi URL, yayıncı, 2026-08-04 erişim
tarihi, SHA-256 ve yeniden kullanım uyarısı taşır. Skill kısa ve atıflı yöntem
özeti kullanır; mevzuat metnini kopyalamaz. Karar sınıfları ve seçenekler MIT
lisanslı sentetik Kurgusal Telco politikasından gelir.

## İnsan ve hukuk sınırı

Bu skill hukuki tavsiye değildir. Resmi telekom kaynağı tek başına bütün
mahremiyet hukukunu veya KVKK sonucunu çözmez. Privacy Counsel, Telecom
Compliance ve DPO telekom + KVKK ortak incelemesini yapar. Copilot işleme,
kampanya, durdurma, veri silme veya sistem değişikliği yapmaz.

## 12 kilitli senaryo

| Kimlik | Odak | Beklenen sınıf | Beklenen seçenek |
|---|---|---|---|
| BTK-01 | Rızasız konum + trafik upsell | `stop-processing` | `consent-first-redesign` |
| BTK-02 | Tam belgeli mevcut kişiselleştirme | `approve-processing` | `current-personalization` |
| BTK-03 | Erişilemeyen rıza eki | `hold-for-consent-evidence` | `consent-first-redesign` |
| BTK-04 | Amaç/hukuki rota belirsizliği | `escalate-privacy-counsel` | `consent-first-redesign` |
| BTK-05 | İşleme öncesi doğrulanabilir kontroller | `approve-with-controls` | `consent-first-redesign` |
| BTK-06 | Bireye bağlanmayan toplulaştırma | `approve-processing` | `aggregate-only` |
| BTK-07 | Çelişkili rıza sistemleri | `hold-for-consent-evidence` | `consent-first-redesign` |
| BTK-08 | Eksik saklama ve silme tetikleri | `stop-processing` | `consent-first-redesign` |
| BTK-09 | Rıza kanıtsız canlı kampanya | `stop-processing` | `consent-first-redesign` |
| BTK-10 | Toplulaştırma testi bekleniyor | `approve-with-controls` | `aggregate-only` |
| BTK-11 | Resmi kaynağın tek başına yeterli sayılması | `escalate-privacy-counsel` | `consent-first-redesign` |
| BTK-12 | Geri alınan rızanın CRM'e yansımaması | `stop-processing` | `consent-first-redesign` |

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
