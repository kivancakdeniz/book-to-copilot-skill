# Şirket politikası

BTK-1.0 kurgusal ve sentetik Kurgusal Telco politikasıdır; hukuki tavsiye veya hukuk
metni değildir.

| Kural | Uygulama |
|---|---|
| BTK-V01 | Veri kategorisi, kaynak, granülerlik, ilgili kişi, CRM alanı, alıcı ve işleme adımını envanterle. |
| BTK-A01 | Amaç, amaç/veri eşlemesi, gereklilik ve sağlanan hukuki rota olgularını ayır; KVKK ortak incelemesini koru. |
| BTK-R01 | Bireysel konum/trafik upsell'i için kapsam, amaç, zaman, sürüm ve geri alma durumu bulunan doğrulanabilir rıza kaydı gerekir. |
| BTK-S01 | Erişim, aktarım, rol ayrımı, saklama süresi, silme ve anonimleştirme olgularını kaydet. |
| BTK-Y01 | Privacy Counsel, Telecom Compliance ve DPO karar verir; Copilot danışmandır. |
| BTK-G01 | Envanter, amaç/rota, gerektiğinde rıza, güvenlik, saklama ve insan onayı tamamlanmadan işleme/kampanya yoktur. |
| BTK-M01 | Rıza sürümü, geri alma senkronizasyonu, saklama incelemesi, silme ve amaç/veri değişiklik tetikleri izlenir. |

## Beş karar sınıfı

- `approve-processing`
- `approve-with-controls`
- `hold-for-consent-evidence`
- `escalate-privacy-counsel`
- `stop-processing`

## Üç işleme seçeneği

- `current-personalization`
- `consent-first-redesign`
- `aggregate-only`

Tam olarak bir sınıf ve bir seçenek seç. `stop-processing` danışman sınıftır;
Copilot'a teknik durdurma yetkisi vermez. Resmi telekom kaynağı ile KVKK boyutu
birlikte insan incelemesine tabidir.