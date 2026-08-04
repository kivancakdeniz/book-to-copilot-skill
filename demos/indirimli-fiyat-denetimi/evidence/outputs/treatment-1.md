## Öneri

- Karar sınıfı: `revise-price-claim`
- Kampanya seçeneği: `advertise-25-percent`
- Kısa gerekçe: Sağlanan olgular karşılaştırma penceresinin tam, en düşük fiyatın
  `800 TRY`, satış fiyatının `600 TRY` ve sağlanan indirim sonucunun `%25`
  olduğunu gösteriyor. Sunulan kreatifteki üzeri çizili `1.000 TRY` ve
  "`%40 indirim`" ifadesi bu sağlanan sonuçla uyuşmuyor; bu yüzden `FYT-O01` ve
  `FYT-C01` yayın öncesi düzeltmeyi gerektiriyor. Düzeltme yayın öncesi mümkün
  olduğu için sınıf `reject` değil `revise-price-claim`.

## Kural tablosu

| Kural | Sonuç | Sağlanan kanıt | Politika sonucu |
|---|---|---|---|
| `FYT-H01` | pass | Karşılaştırma penceresi ürün, satıcı ve kanal için tam olarak işaretlenmiş (Sağlanan olgu; `sources/case-brief.md`, Sağlanan olgular) | Fiyat geçmişi kapısı karşılanıyor |
| `FYT-B01` | pass | Penceredeki en düşük fiyat `800 TRY` olarak sağlandı (Sağlanan olgu) | Yalnız bu sağlanan referans kullanılabilir; kreatifteki `1.000 TRY` sağlanan referans değildir |
| `FYT-O01` | fail | Sağlanan oran `%25`; kreatifte gösterilen oran `%40` (Sağlanan olgu) | Gösterilen oran sağlanan sonuçla eşitlenmeli |
| `FYT-C01` | fail | Kreatif üzeri çizili `1.000 TRY`, satış `600 TRY` ve "%40 indirim" içeriyor (Sağlanan olgu) | Karşılaştırma fiyatı ve iddia açık ve tutarlı hâle getirilmeli |
| `FYT-A01` | unknown | E-commerce Owner, Pricing Owner ve Compliance kararı sağlanmadı (Eksik bilgi) | Üçlü insan kararı alınmalı |
| `FYT-R01` | unknown | Planlı canlı fiyat `600 TRY` satış fiyatıyla eşleşiyor; onaylı kreatif ve insan onayı sağlanmadı (Sağlanan olgu + Eksik bilgi) | Onay ve onaylı kreatif tamamlanmadan yayın yok |
| `FYT-M01` | unknown | İzleme sahibi, kayıt ve sıklık sağlanmadı (Eksik bilgi) | İzleme sahibi ve kaydı tanımlanmalı |

## Kreatif ve fiyat bulguları

- **Sağlanan referans fiyat:** `800 TRY` (pencere içindeki en düşük fiyat olarak
  sağlanmıştır). Kreatifteki üzeri çizili `1.000 TRY` için sağlanan bir fiyat
  geçmişi dayanağı yoktur; kaynağı `bilinmiyor` (Eksik bilgi).
- **Sağlanan oran:** `%25` (800 TRY referansına göre sağlanan aritmetik sonucu).
- **Gösterilen iddia:** "`%40 indirim`" — sağlanan sonuçla uyuşmuyor.
- **Canlı fiyat eşleşmesi:** Ticaret sistemindeki planlı canlı fiyat `600 TRY`,
  kreatifteki satış fiyatıyla aynıdır (Sağlanan olgu).
- Hiçbir hesap yapılmadı: referans fiyat, indirim oranı ve fark yalnız vakada
  sağlanan sonuçlardan alındı; yeni oran, fiyat veya pencere türetilmedi.
- Dış yöntem (Ticaret Bakanlığı kılavuzu, yalnız metadata) referans fiyatın,
  karşılaştırma döneminin ve gösterilen indirimin birlikte incelenmesi için
  çerçevedir; karar sınıfını ve seçeneği sentetik şirket politikası belirler.

## İnsan kararı ve yayın kapısı

- **Pricing Owner:** Sağlanan pencerenin ve `800 TRY` referansının kreatife
  yansıtılmasını doğrular (`FYT-B01`, `FYT-H01`).
- **E-commerce Owner:** Düzeltilmiş kreatifin satış fiyatı, karşılaştırma fiyatı
  ve oran açısından tutarlı olduğunu teyit eder (`FYT-C01`).
- **Compliance:** `%25` iddiasının sağlanan kanıtla uyumunu ve yayın paketini
  inceler (`FYT-O01`, `FYT-A01`).
- **Legal:** Yalnız belgelenmiş bir istisna veya tüketici hukuku yorumu gerekirse
  devreye girer; bu vakada böyle bir olgu sağlanmadı, durum `bilinmiyor`.
- **`FYT-R01` yayın koşulları:** Üç insan sahibinin onayı, onaylı kreatif ve
  canlı fiyatın eşleşmesi birlikte tamamlanmadan yayın yapılmaz. Canlı fiyat
  eşleşmesi sağlanmıştır; onay ve onaylı kreatif eksiktir, bu nedenle kapı
  kapalıdır. Bu beceri adına onay verilmemiştir.

## İzleme

`FYT-M01` kapsamında fiyat geçmişi, referans fiyat ve yayındaki kreatif izlenir;
sapma tespit edildiğinde insan sahibi inceler ve gerekirse kampanyayı gözden
geçirir. İzleme sahibi, izleme sıklığı, kayıt yeri ve inceleme tarihi
sağlanmadığı için `bilinmiyor` kalır; kişi veya tarih üretilmemiştir.

## Sınırlar

Bu not yalnız sağlanan sentetik olgulara dayanan bir inceleme notudur; hukuki
görüş veya nihai hukuki sonuç değildir. Kararın sahibi E-commerce Owner, Pricing
Owner ve Compliance'tır; gerektiğinde Legal incelemesi eklenir. Kampanya
onaylanmadı, yayına alınmadı, hiçbir fiyat, kreatif veya sistem değiştirilmedi
ve hiçbir otonom işlem yapılmadı.
