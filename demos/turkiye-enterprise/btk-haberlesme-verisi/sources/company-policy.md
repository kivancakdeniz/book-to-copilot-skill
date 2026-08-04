# Kurgusal Telco Haberleşme Verisi Kampanya Politikası BTK-1.0

> Bu dosya, `btk-haberlesme-verisi` demosu için kurgusal ve sentetik şirket
> politikasıdır. Hukuki tavsiye veya mevzuat metni değildir.

## Kapsam ve kurallar

- **BTK-V01 - Veri ve kategori envanteri.** Konum ve trafik verisi dahil her
  veri kategorisini, kaynağını, granülerliğini, ilgili kişiyi, CRM alanını,
  alıcıyı ve işleme adımını yalnız sağlanan olgularla kaydet.
- **BTK-A01 - Amaç ve hukuki rota olguları.** Her işleme amacı, amaç eşlemesi,
  gereklilik iddiası ve sağlanan hukuki rota olgusunu ayrı kaydet. Eksik rota
  `unknown` kalır. Resmi telekom kaynağının tek başına bütün mahremiyet hukukunu
  çözdüğünü varsayma; KVKK ortak incelemesini insanlara yönlendir.
- **BTK-R01 - Rıza ve kanıt.** Bu sentetik politika kapsamında bireysel konum
  veya trafik verisiyle kişiselleştirilmiş upsell, kampanya başlamadan önce
  kapsam, amaç, zaman, sürüm ve geri alma durumu gösterilen doğrulanabilir rıza
  kaydı gerektirir. Eksik ya da çelişkili rızayı varsayma.
- **BTK-S01 - Güvenlik ve saklama.** Erişim, aktarım, rol ayrımı, saklama süresi,
  silme ve anonimleştirme olgularını kaydet. Sağlanmayan kontrol veya süre
  `unknown` kalır; kesin değer üretme.
- **BTK-Y01 - İnsan yetkisi.** Privacy Counsel, Telecom Compliance ve DPO
  birlikte işleme, kampanya ve KVKK ortak inceleme kararını verir. Copilot
  hukuki karar, onay veya uygulama yetkisine sahip değildir.
- **BTK-G01 - Kampanya kapısı.** Veri envanteri, amaç/hukuki rota, gerektiğinde
  rıza kanıtı, güvenlik, saklama ve insan onayı tamamlanmadan işleme ya da
  kampanya başlayamaz. Copilot işlemeyi başlatamaz veya durduramaz.
- **BTK-M01 - Rıza ve saklama izleme.** İnsan sahibi, rıza metni/sürümü, geri
  alma senkronizasyonu, saklama inceleme tarihi, silme tetikleri ve amaç/veri
  değişiklikleri kaydedilir. Eksikler `unknown` kalır.

## Karar sınıfları

Tam olarak bir sınıf kullan:

- `approve-processing`: sağlanan işleme seçeneğinin tüm politika ve insan
  kapıları tamamlanmıştır.
- `approve-with-controls`: sağlanan daha dar seçenek desteklenir ve kalan tüm
  kontroller işleme öncesi nesnel olarak doğrulanabilir.
- `hold-for-consent-evidence`: gerekli rıza kaydı eksik, erişilemez veya
  çelişkilidir; insan incelemesi kanıt bekler.
- `escalate-privacy-counsel`: amaç, hukuki rota, kaynak kapsamı veya KVKK ortak
  değerlendirmesi Privacy Counsel kararı gerektirir.
- `stop-processing`: sağlanan işleme, sentetik politika kapısını karşılamaz ve
  mevcut haliyle başlamamalı ya da sürmemelidir. Bu danışman sınıf Copilot'a
  teknik durdurma yetkisi vermez.

## İşleme seçenekleri

Tam olarak bir seçenek kullan:

- `current-personalization`: mevcut bireysel kişiselleştirme akışı.
- `consent-first-redesign`: doğrulanabilir rıza, amaç, güvenlik, saklama ve geri
  alma kapıları tamamlanmadan bireysel işleme yapmayan yeniden tasarım.
- `aggregate-only`: bireysel konum veya trafik verisini hedefleme için
  kullanmayan, sağlanan toplulaştırılmış seçenek.

Bu politika KVKK dahil uygulanabilir bütün hukuk hakkında sonuç üretmez.
Telekom kaynağı ile KVKK boyutu birlikte insan incelemesine tabidir. Nihai
kararlar ve tüm eylemler adı geçen insan rollerine aittir.