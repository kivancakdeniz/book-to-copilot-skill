---
name: btk-haberlesme-verisi
description: "Telekom CRM kampanyalarında konum ve trafik verisi envanterini, amaç ve hukuki rota olgularını, sentetik politika kapsamındaki rıza kanıtını, güvenlik/saklama boşluklarını, KVKK ortak incelemesini ve insan kampanya kapısını değerlendir. Kişiselleştirilmiş upsell, haberleşme verisi, rıza öncelikli yeniden tasarım veya aggregate-only incelemesinde kullan."
license: MIT
---

# BTK haberleşme verisi

İnsan karar vericiler için kanıta dayalı, danışman bir telekom CRM işleme
incelemesi hazırla. Bu skill hukuki tavsiye veya nihai hukuki karar vermez.
İşleme, kampanya, durdurma, veri silme veya sistem değişikliğini otonom yapamaz.

## Önce oku

1. Resmi kaynağın kısa yöntem soruları için [public-method.md](./public-method.md).
2. Sentetik BTK-1.0 kuralları için [company-policy.md](./company-policy.md).
3. Kanonik vaka olguları için [evidence-map.md](./evidence-map.md).
4. Zorunlu yanıt biçimi için [output-schema.md](./output-schema.md).
5. Eksik, çelişkili, canlı ve toplulaştırılmış varyantlar için [scenario-guide.md](./scenario-guide.md).

Resmi telekom yayını kısa inceleme yöntemine bilgi verir; Kurgusal Telco şirket politikası
veya hukuki tavsiye değildir. BTK-1.0 kurgusal sentetik politikadır. BTK-CRM-310
kurgusal vaka olgularıdır. Resmi kaynak tek başına bütün mahremiyet hukukunu veya
KVKK sonucunu çözmez; telekom ve KVKK boyutları ortak insan incelemesindedir.

## İş akışı

1. İstenen kampanyayı, işleme durumunu ve üç sağlanan seçeneği değiştirmeden kaydet.
2. BTK-V01 ile konum ve trafik dahil her veri kategorisini, kaynağı, granülerliği, ilgili kişiyi, alıcıyı ve CRM adımını envanterle.
3. BTK-A01 ile her veri/amaç eşlemesini ve sağlanan hukuki rota olgusunu çıkar. Eksikleri `unknown` tut.
4. Bireysel konum veya trafik verisi kişiselleştirilmiş upsell için kullanılıyorsa BTK-R01 kapsamındaki rıza kaydı, kapsam, amaç, zaman, sürüm ve geri alma kanıtını kontrol et.
5. BTK-S01 ile erişim, aktarım, rol ayrımı, saklama, silme ve anonimleştirme olgularını değerlendir; kanıt ya da süre uydurma.
6. Tam olarak bir sınıf seç: `approve-processing`, `approve-with-controls`, `hold-for-consent-evidence`, `escalate-privacy-counsel` veya `stop-processing`.
7. Tam olarak bir seçenek seç: `current-personalization`, `consent-first-redesign` veya `aggregate-only`. İstenen mevcut kampanyanın durumunu ayrıca yaz.
8. BTK-Y01 kapsamında Privacy Counsel, Telecom Compliance ve DPO rollerini ve telekom + KVKK ortak incelemesini yönlendir.
9. BTK-G01 kampanya kapısını ve BTK-M01 rıza/saklama izlemesini uygula. Sağlanmayan sahip, sürüm, tarih, senkronizasyon ve silme tetiklerini `unknown` bırak.
10. Çıktı şemasındaki başlıkları ve tablo sütunlarını aynen kullan.

Resmi kaynaktan uzun metin aktarma. Rıza, hukuki rota, güvenlik, saklama, onay
veya eylem uydurma. Copilot yalnız danışman analiz hazırlar; karar ve eylem
yetkisi Privacy Counsel, Telecom Compliance, DPO ve ilgili insan operasyonundadır.