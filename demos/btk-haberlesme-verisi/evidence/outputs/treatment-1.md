## Karar

`hold-for-consent-evidence`. Bireysel konum ve trafik verisiyle kişiselleştirilmiş
upsell yapılacağı sağlanan olgudur (BTK-CRM-310, olgu 1-3), ancak BTK-R01'in
aradığı doğrulanabilir rıza kaydı, kapsamı, zamanı, sürümü ve geri alma durumu
sağlanmamıştır (olgu 4). BTK-A01 kapsamındaki amaç/veri eşlemesi ile hukuki rota
olgusu (olgu 5), BTK-S01 kapsamındaki saklama ve silme olguları (olgu 6) ve
BTK-Y01 kapsamındaki üç insan onayı ile KVKK ortak inceleme kaydı da yoktur
(olgu 8). Bu, insan incelemesine yönelik danışman bir analizdir; hukuki sonuç
değildir.

## Önerilen işleme seçeneği

`consent-first-redesign`.

## İstenen kampanyanın durumu

2026-09-01 için talep edilen `current-personalization` kampanyası sunulduğu
haliyle ilerleyemez; BTK-G01 kapısı açık değildir. Kampanya henüz başlamamıştır
(olgu 9), bu nedenle bulgu bir durdurma değil, kanıt beklemesidir. Kampanyanın
başlatılıp başlatılmayacağına insan yetkililer karar verir.

## Veri, amaç ve kontrol kaydı

| Öğe | Sağlanan olgu | Amaç/işleme | Kaynak | BTK kuralı | Durum | Gerekli insan işlemi |
|---|---|---|---|---|---|---|
| Konum verisi | Son görülen hücre bölgesinden türetilip abone profiline bağlanır | Bireysel upsell hedeflemesi | BTK-CRM-310, olgu 1 | BTK-V01 | pass | Granülerlik ve alıcıları envantere ekle |
| Trafik verisi | Kullanım zamanı ve hacmi profile bağlanır | Bireysel upsell hedeflemesi | olgu 2 | BTK-V01 | pass | Aynı envanter alanlarını tamamla |
| Birleşik kullanım | İki kategori teklif seçiminde birlikte kullanılır | Kişiselleştirilmiş upsell | olgu 3 | BTK-V01, BTK-A01 | pass | Gerekliliği ve daha dar seçeneği değerlendir |
| Rıza kaydı | Sağlanmadı: kayıt, metin/sürüm, kapsam, zaman, geri alma yok | Bireysel hedeflemenin ön koşulu | olgu 4 | BTK-R01 | unknown | Doğrulanabilir rıza kanıtını sun |
| Amaç/veri eşlemesi ve hukuki rota | Sağlanmadı | — | olgu 5 | BTK-A01 | unknown | Eşlemeyi ve sağlanan rota olgusunu belgele |
| Erişim ve rol ayrımı | Rol tabanlı CRM erişimi belirtilmiş; ayrıntılı matris yok | CRM işleme | olgu 7 | BTK-S01 | unknown | Erişim matrisini ve rol ayrımını kanıtla |
| Aktarım kontrolü | Sağlanmadı | — | olgu 7 | BTK-S01 | unknown | Alıcı ve aktarım kontrollerini kaydet |
| Saklama süresi ve silme tetikleri | Sağlanmadı | — | olgu 6 | BTK-S01 | unknown | Süre ve silme tetiklerini tanımla |
| Anonimleştirme/toplulaştırma | Kanıt sağlanmadı | `aggregate-only` ön koşulu | olgu 7 | BTK-S01 | unknown | Bireysel bağın kalktığını ve yeniden tanımlama kontrolünü kanıtla |
| İnsan onayı ve ortak inceleme | Privacy Counsel, Telecom Compliance, DPO onayı ve KVKK ortak inceleme kaydı yok | Kampanya kapısı | olgu 8 | BTK-Y01, BTK-G01 | fail | Onayı ve ortak incelemeyi yürüt |

## Eksik veya çelişkili bilgi

- **Rıza (BTK-R01):** Kayıt kimliği, metin/sürüm, kapsam, amaç, zaman ve geri
  alma durumu yok; bireysel hedeflemenin ön koşuludur. Sahip `unknown`.
- **Amaç ve hukuki rota (BTK-A01):** Belgelenmiş amaç/veri eşlemesi ve sağlanan
  rota olgusu yok; kapsam belirsizliği Privacy Counsel'a aittir.
- **Güvenlik ve saklama (BTK-S01):** Erişim matrisi, aktarım kontrolü, saklama
  süresi, silme tetikleri ve anonimleştirme kanıtı yok.
- **Yetki (BTK-Y01):** Üç rolün onayı ve KVKK ortak inceleme kaydı yok.
- Çelişkili olgu bildirilmemiştir; eksik alanlar `unknown` bırakılmış ve
  tarafımdan üretilmemiştir.

## İnsan ve ortak inceleme rotası

- **Privacy Counsel:** Amaç/veri eşlemesi, hukuki rota kapsamı ve rıza içeriğinin
  yeterliliği (BTK-A01, BTK-R01).
- **Telecom Compliance:** Haberleşme verisi kategorileri, erişim, aktarım ve
  saklama olguları (BTK-V01, BTK-S01).
- **DPO:** İlgili kişi hakları, geri alma senkronizasyonu, silme ve izleme
  (BTK-S01, BTK-M01).
- Telekom boyutu ile KVKK boyutu birlikte, ortak insan incelemesiyle
  değerlendirilir; resmi kaynak tek başına sonucu belirlemez.
- Copilot'un hukuki karar, onay, işleme, kampanya başlatma, durdurma, silme veya
  sistem değişikliği yetkisi yoktur; bu yanıt yalnız danışman analizdir.

## Kampanya kapısı ve izleme

BTK-G01 kapısı kapalıdır: envanter kısmen tamam, amaç/rota `unknown`, rıza
`unknown`, güvenlik ve saklama `unknown`, insan onayı yok. Kapı yalnız bu
kalemler nesnel kanıtla kapandığında ve üç rol onay verdiğinde açılabilir; kapıyı
açma yetkisi insanlardadır.

BTK-M01 izleme alanları: rıza metni/sürümü `unknown`; geri alma senkronizasyonu
`unknown`; saklama inceleme tarihi `unknown`; silme tetikleri `unknown`; amaç/veri
değişiklik tetikleri `unknown`; izleme sahipleri `unknown`.

## Sınırlar

Bu çalışma yalnız BTK-CRM-310'da sağlanan sentetik olgularla ve BTK-1.0 sentetik
politikasıyla sınırlıdır; hukuki tavsiye, hukuki sonuç veya uygunluk beyanı
değildir. Resmi telekom kaynağı (BTK-RG-2020 metadata'sı) yalnız kısa inceleme
yöntemidir ve tek başına tüm mahremiyet hukukunu ya da KVKK sonucunu çözmez.
Hiçbir işleme, kampanya, durdurma, silme veya sistem değişikliği yapılmadı ve
hiçbir onay verilmedi; tüm karar ve eylemler Privacy Counsel, Telecom Compliance,
DPO ve ilgili insan operasyonundadır.
