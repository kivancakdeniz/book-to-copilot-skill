# Çıktı şeması

Aşağıdaki başlıkları aynen ve aynı sırada kullan. Hukuki sonuç ekleme.

## Karar

Tam olarak bir izin verilen karar sınıfı, kısa kanıt gerekçesi ve sonucun insan
incelemesine yönelik danışman analiz olduğunu yaz.

## Önerilen ürün seçeneği

Tam olarak bir seçenek yaz: `launch-current-flow`, `remove-crypto-checkout` veya
`redesign-nonpayment-service`.

## İstenen akışın durumu

Mevcut lansman talebini ve sunulduğu haliyle ilerleyip ilerleyemeyeceğini önerilen
seçenekten ayrı belirt.

## Akış ve kural kaydı

| Öğe | Sağlanan olgu | Aktör/adım | Kaynak | KRP kuralı | Durum | Gerekli insan işlemi |
|---|---|---|---|---|---|---|

Durum için yalnız `pass`, `fail`, `unknown` veya `not-applicable` kullan.
Varlık, işlev, talimat, cüzdan, dönüşüm, transfer, aracı ve mutabakatı kapsa.

## Eksik veya çelişkili bilgi

Her eksikliği, etkilenen akış öğesini ve kuralı, neden önemli olduğunu ve
sağlanmışsa insan sahibini listele. Eksikliği doldurma.

## İnsan yetki rotası

Payments Counsel, Compliance ve Product rollerini yaz. Copilot'un hukuki karar,
onay, lansman, ödeme, transfer, durdurma veya ürün değişikliği yetkisi olmadığını belirt.

## Lansman kapısı ve izleme

Akış kanıtı, ürün sınırı, sürüm ve insan onayı kapılarını kaydet. İzleme sahibi,
akış sürümü, inceleme tarihi ile değişiklik tetiklerini yaz; sağlanmayanları
`unknown` bırak.

## Sınırlar

Çalışmanın yalnız sağlanan ödeme akışını kullandığını, hukuki tavsiye olmadığını,
yatırım veya ödeme dışı transfer hukukuna ilişkin görüş vermediğini ve tüm karar
ile eylemleri insan yetkililere bıraktığını yaz.