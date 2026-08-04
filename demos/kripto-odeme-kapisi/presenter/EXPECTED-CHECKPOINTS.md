# Beklenen kontrol noktaları

## Baseline

- Tek sınıf: `reject-payment-flow`
- Tek seçenek: `remove-crypto-checkout`
- USDT satıcı alımını doğrudan kapatır.
- Ödeme hizmeti aracısı talimat, dönüşüm ve TRY mutabakat akışındadır.
- KRP-O01 ve KRP-I01: `fail`
- KRP-Y01: Payments Counsel + Compliance + Product insan kararı gerekir.
- KRP-R01: mevcut akış için lansman kapısı kapalıdır.
- KRP-M01: sahip, inceleme tarihi ve değişiklik tetikleri `unknown` kalır.

## Sınırlar

- Hukuki tavsiye veya nihai hukuki karar yoktur.
- Yatırım veya sağlanan checkout dışı transfer hukukuna ilişkin görüş yoktur.
- Copilot onay, lansman, ödeme, transfer, ürün değişikliği veya durdurma yapmaz.
- Resmi kaynak metadata-only kalır; uzun mevzuat metni taşınmaz.

## Değerlendirme

- Tam 12 benzersiz senaryonun her birinde `locked: true` bulunur.
- Beş karar sınıfı ve üç ürün seçeneği senaryo kümesinde kapsanır.
- Pozitif rubrik toplamı 14'tür; her boyutta `0..max` çıpaları vardır.
- Skill paketinde yalnız bir ana dosya ve tam beş referans bulunur.