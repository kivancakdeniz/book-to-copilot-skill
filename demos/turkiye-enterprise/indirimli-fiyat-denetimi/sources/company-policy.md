# Kurgusal Sepet indirimli fiyat iletişimi politikası

Bu belge sentetik demo politikasıdır. Ticaret Bakanlığı kılavuzu yöntemi açıklar; Kurgusal Sepet adına karar sınıfını, seçeneği, yetkiyi ve yayın kapısını yalnız bu politika belirler.

## Kapsam ve sınırlar

- Yalnız vakada sağlanan fiyat geçmişini, karşılaştırma penceresini ve hesap sonuçlarını kullan.
- Eksik fiyatı, pencereyi, oranı veya yetkiyi hesaplama, tamamlama ya da varsayma.
- Bu çalışma hukuki görüş değildir. İnsanlar karar verir; beceri kampanyayı onaylayamaz, yayına alamaz veya sistemlerde değişiklik yapamaz.
- Resmi kaynaktan uzun alıntı üretme; yöntemi kısa biçimde özetle ve kaynağa bağla.

## Karar sınıfları

Tam olarak bir sınıf seç:

1. `approve`: Zorunlu kanıtlar tamdır, gösterilen oran sağlanan sonuçla eşleşir, kreatif açıktır ve yetkili insanlar yayın kararını verebilir.
2. `revise-price-claim`: Temel kampanya yürütülebilir; ancak referans fiyat, oran veya kreatif iddia yayın öncesi düzeltilmelidir.
3. `hold-for-price-history`: Fiyat geçmişi, karşılaştırma penceresi veya sağlanan hesap sonucu eksik ya da çelişkilidir.
4. `escalate-consumer-law`: Belgelenmiş istisna, yorum ihtilafı veya tüketici hukuku değerlendirmesi Legal incelemesi gerektirir.
5. `reject`: İddia kanıtla desteklenemez, düzeltme kabul edilmez veya yanıltıcılık giderilemez.

## Kampanya seçenekleri

Tam olarak bir seçenek öner:

1. `advertise-40-percent`: Üzeri çizili 1.000 TRY ve “%40” iddiasını kullan.
2. `advertise-25-percent`: 800 TRY karşılaştırma fiyatını, 600 TRY satış fiyatını ve sağlanan “%25” sonucunu kullan.
3. `no-promotion`: İndirim oranı veya karşılaştırmalı fiyat iddiası yayımlama.

## Zorunlu kurallar

- `FYT-H01` Fiyat geçmişi ve pencere: Ürün, satıcı, kanal, tarih aralığı ve pencerenin eksiksiz olduğuna ilişkin sağlanan kayıt bulunmalıdır. Eksik veya çelişkiliyse `hold-for-price-history`.
- `FYT-B01` Referans fiyat: Vakada resmi yöntemle uyumlu olduğu belirtilen, önceden hesaplanmış referans fiyatı kullan. Sonuç sağlanmamışsa hesaplama yapma; `hold-for-price-history`.
- `FYT-O01` Gösterilen oran: Kreatifteki oran sağlanan aritmetik sonuçla aynı olmalıdır. Fark varsa yayın öncesi `revise-price-claim`.
- `FYT-C01` Kreatif açıklığı: Satış fiyatı, karşılaştırma fiyatı ve iddia tüketicinin kolayca ayırt edebileceği biçimde açık olmalıdır. Belirsizlik varsa düzeltme iste.
- `FYT-A01` Yetki: E-commerce Owner, Pricing Owner ve Compliance birlikte insan kararı verir. Belgelenmiş istisna veya hukuki yorum için Legal gerekir.
- `FYT-R01` Yayın kapısı: İnsan onayı, onaylı kreatif ve ticaret sistemindeki fiyat birebir eşleşmeden kampanya yayına alınamaz.
- `FYT-M01` İzleme: Fiyat/geçmiş kaydı, canlı kreatif ve satış fiyatı yayın boyunca izlenir; sapmada insan sahibi kampanyayı durdurup yeniden inceler.

## Karar önceliği

Eksik zorunlu kanıt varsa düzeltilebilir bir oran uyuşmazlığından önce `hold-for-price-history` seç. Hukuki istisna varsa `escalate-consumer-law` seç. Kanıtlar tam ve yalnız iddia/oran hatalıysa `revise-price-claim` seç. Hiçbir otomatik işlem yapma.