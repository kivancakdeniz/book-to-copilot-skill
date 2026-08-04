# BTK haberleşme verisi

[English](../../skills/btk-haberlesme-verisi.md)

## LLM only vs LLM + skill - beklenen fark

| Brief-only LLM | Derlenmiş skill |
|---|---|
| Serbest anlatım ve eksik kontrol listesi üretebilir | İzinli karar sınıfları, üç seçenek ve kural kimlikleriyle yapılandırır |
| Eksik kanıtı varsayım ile doldurma riski taşır | Eksik olguyu `bilinmiyor` tutar ve insan karar sahibine yönlendirir |
| Genel bir uyum veya operasyon önerisi verir | Yayın, canlıya geçiş, işlem veya kapanış kapısını açıkça uygular |

Bu tablo tasarım hipotezidir; bu 10 yeni skill için Cowork A/B henüz
çalıştırılmadı. Ölçülecek metrikler: exact karar/seçenek, gerekli kural geri
çağırma, desteksiz iddia sayısı, insan yetki sınırı ve yanıt uzunluğu. ROI veya
üretim performansı iddia edilmez.


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

- [Cowork skill](../../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-cowork.skill)
- [GitHub Copilot for VS Code ZIP](../../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/turkiye-enterprise/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-classic-setup.zip)

Classic setup ZIP doğrudan içe aktarım paketi değildir; dosyalar Copilot Studio
classic ortamında insan tarafından uygulanacak kurulum malzemeleridir.