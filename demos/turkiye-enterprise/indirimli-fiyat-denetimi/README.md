# İndirimli fiyat denetimi demosu

Bu demo, bir e-ticaret kampanyasındaki referans fiyat ve indirim oranını kanıta dayalı biçimde inceler. Resmi Ticaret Bakanlığı kaynağı yöntemi açıklar; hangi karar sınıfının ve kampanya seçeneğinin uygulanacağını sentetik Kurgusal Sepet politikası belirler.

## Baseline

- Sağlanan pencerenin en düşük fiyatı: 800 TRY
- Kampanya fiyatı: 600 TRY
- Sağlanan sonuç: %25
- Kreatif: üzeri çizili 1.000 TRY ve “%40”
- Beklenen sınıf: `revise-price-claim`
- Beklenen seçenek: `advertise-25-percent`

## Güvence sınırı

Bu demo hukuki görüş vermez. İnsanlar karar verir; hiçbir kampanyayı onaylamaz, yayına almaz veya sistemde değiştirmez. Eksik hesap üretmez ve resmi kaynaktan uzun alıntı taşımaz.

## Yapı

- `sources/`: dış yöntem metadatası ve MIT lisanslı sentetik karar girdileri
- `evaluation/`: dondurulmuş istem, 12 kilitli senaryo ve 14 puanlık rubrik
- `skill/`: `SKILL.md` ve tam beş referans
- `presenter/`: kurulum, konuşma akışı ve beklenen kontrol noktaları

JSON dosyaları ayrıştırılmalı; `skill/` altında yalnız `SKILL.md` ile beş referans bulunmalıdır.