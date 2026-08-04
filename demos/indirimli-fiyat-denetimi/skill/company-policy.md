# Şirket politikası

Bu referans, sentetik Kurgusal Sepet politikasının çalıştırılabilir özetidir. Resmi kaynak yöntemdir; kararları bu politika belirler.

## Beş karar sınıfı

- `approve`: Zorunlu kanıtlar tam, iddia sağlanan sonuçla uyumlu, kreatif açık ve insan yayın kapısı hazır.
- `revise-price-claim`: Referans fiyat, oran, kreatif veya yayın paketi yayın öncesi düzeltilebilir.
- `hold-for-price-history`: Fiyat geçmişi, pencere ya da sağlanan hesap sonucu eksik/çelişkili.
- `escalate-consumer-law`: Belgelenmiş istisna veya hukuki yorum Legal incelemesi gerektirir.
- `reject`: İddia desteklenemez ya da gerekli düzeltme/kontrol reddedilir.

## Üç seçenek

- `advertise-40-percent`: 1.000 TRY ve %40 iddiası.
- `advertise-25-percent`: 800 TRY, 600 TRY ve sağlanan %25 sonucu.
- `no-promotion`: Karşılaştırmalı fiyat veya oran iddiası yok.

## Kurallar

- `FYT-H01`: Ürün/satıcı/kanal için fiyat geçmişi ve karşılaştırma penceresi tam olmalı.
- `FYT-B01`: Yalnız sağlanan resmi-yöntem uyumlu referans fiyat sonucunu kullan; eksik sonucu hesaplama.
- `FYT-O01`: Gösterilen oran sağlanan sonuçla aynı olmalı.
- `FYT-C01`: Satış fiyatı, karşılaştırma fiyatı ve iddia açık olmalı.
- `FYT-A01`: E-commerce Owner + Pricing Owner + Compliance karar verir; istisnada Legal gerekir.
- `FYT-R01`: İnsan onayı, onaylı kreatif ve canlı fiyat eşleşmeden yayın yoktur.
- `FYT-M01`: Fiyat/geçmiş ve kreatif izlenir; sapmayı insan sahibi inceler.

Eksik veri `hold-for-price-history`, belgelenmiş hukuki istisna `escalate-consumer-law` önceliğindedir. Hiçbir otonom işlem yapma.