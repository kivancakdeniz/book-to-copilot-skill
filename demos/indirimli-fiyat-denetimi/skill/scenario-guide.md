# Senaryo rehberi

## Eksik ve çelişkili bilgi

- Fiyat geçmişi, pencere veya sağlanan hesap sonucu eksikse değeri üretme; `hold-for-price-history` ve `no-promotion` kullan.
- İki kaynak farklı en düşük fiyat veriyorsa birini seçme; çelişki çözülene kadar beklet.
- Doğru oran mevcut ancak kreatif belirsizse `revise-price-claim` kullan.

## İstisna ve ret

- Belgelenmiş politika istisnası veya tüketici hukuku yorumu gerekiyorsa Legal için `escalate-consumer-law`; kesin hukuki sonuç verme.
- Satıcı kanıtla uyuşmayan iddiayı düzeltmeyi veya zorunlu izlemeyi reddederse `reject` ve `no-promotion` kullan.

## Yayın ve izleme

- Kreatif doğru olsa bile planlı canlı fiyat eşleşmiyorsa yayın kapısını geçirme.
- Karşılaştırmalı iddia tamamen kaldırılmışsa `no-promotion` seçeneğini FYT-C01, FYT-A01, FYT-R01 ve FYT-M01 kapsamında değerlendir.
- What-if isteklerinde yalnız değiştirilen olguyu değiştir; diğer baseline olgularını koru.

Her durumda insanlar karar verir. Kampanyayı başlatma, sistemde değişiklik yapma veya hukuki görüş verme.