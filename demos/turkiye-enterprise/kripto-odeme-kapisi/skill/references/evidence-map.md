# Kanıt haritası

## Kaynak katmanları

| Kimlik | Tür | Kullanım | Kullanılmayacağı yer |
|---|---|---|---|
| TCMB-RG-2021 | Resmi kaynak metadata ve yöntem | Varlık işlevi, ödeme kullanımı ve aracı akışını inceleme soruları | Kurgusal Ödeme kararı, şirket onayı veya uzun mevzuat alıntısı |
| KRP-1.0 | Sentetik şirket politikası | Kurallar, sınıflar, seçenekler, kapı ve insan yetkisi | Hukuk beyanı |
| KRP-2401 | Sentetik vaka | Donmuş ürün ve akış olguları | Başka ürünlere genelleme |

## KRP-2401 kanonik olguları

| Olgu | Kaynak | Durum |
|---|---|---|
| Müşteri USDT seçeneğini satıcı alımı için checkout'ta seçer. | KRP-2401, olgu 1 | supplied |
| USDT satıcı alımını doğrudan kapatan değer olarak kullanılır. | KRP-2401, olgu 2 | supplied |
| Ödeme hizmeti aracısı talimat, dönüşüm ve mutabakat akışındadır. | KRP-2401, olgu 3 | supplied |
| Satıcı TRY alır; USDT dönüşümü aracı akışının içindedir. | KRP-2401, olgu 4 | supplied |
| Akış diyagramı ve ürün özeti `checkout-v3` sürümündedir. | KRP-2401, olgu 5 | supplied |
| Üç gerekli insan rolünün lansman onayı yoktur. | KRP-2401, olgu 6 | supplied |
| İzleme sahibi, tarihi ve değişiklik tetikleri sağlanmamıştır. | KRP-2401, olgu 7 | unknown |

Satıcı TRY mutabakatı, USDT'nin akıştaki doğrudan işlevini kendiliğinden ortadan
kaldırmaz. Bir aracının varlığı ya da yokluğu tek başına bütün ürün
sınıflandırmasını çözmez. KRP-2401 yatırım amacı, saklama veya checkout dışı
transfer hukuku hakkında kanıt sağlamaz.