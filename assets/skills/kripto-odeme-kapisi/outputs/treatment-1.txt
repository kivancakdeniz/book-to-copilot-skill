## Karar

`reject-payment-flow`. Sağlanan olgu 2, USDT'nin satıcı alımını doğrudan kapatan
değer olarak kullanıldığını gösterir; KRP-O01 uyarınca mevcut akış lansmanı
geçemez. Olgu 3 ve 4 aracıyı ve TRY mutabakatını doğrular, ancak TRY mutabakatı
USDT'nin akıştaki doğrudan işlevini kendiliğinden ortadan kaldırmaz. Bu sonuç,
insan incelemesine yönelik danışman analizdir.

## Önerilen ürün seçeneği

`remove-crypto-checkout`.

## İstenen akışın durumu

İstenen `launch-current-flow` (2026-09-15, akış değişmeden) sunulduğu haliyle
ilerleyemez. `redesign-nonpayment-service` sağlanan olgularla doğrulanmamıştır;
ayrı insan incelemesi gerektirir.

## Akış ve kural kaydı

| Öğe | Sağlanan olgu | Aktör/adım | Kaynak | KRP kuralı | Durum | Gerekli insan işlemi |
|---|---|---|---|---|---|---|
| Varlık ve işlev | USDT satıcı alımını doğrudan kapatan değerdir | Müşteri → checkout | KRP-2401, olgu 1-2 | KRP-A01, KRP-O01 | fail | Payments Counsel ürün sınırını değerlendirir |
| Ödeme talimatı | Aracı talimat akışında yer alır | Ödeme hizmeti aracısı | KRP-2401, olgu 3 | KRP-I01 | pass | Compliance adım eşlemesini doğrular |
| Aracı rolü | Aracı dönüşüm ve mutabakat akışındadır | Ödeme hizmeti aracısı | KRP-2401, olgu 3 | KRP-I01 | pass | Compliance rol tanımını kayda alır |
| Cüzdan ve hesap | Sağlanmamıştır | unknown | KRP-2401 | KRP-A01, KRP-X01 | unknown | Product cüzdan/hesap kaydını sunar |
| Dönüşüm | USDT dönüşümü aracı akışının içindedir | Ödeme hizmeti aracısı | KRP-2401, olgu 4 | KRP-I01 | pass | Compliance dönüşüm adımını teyit eder |
| Checkout dışı transfer | Vaka sınırı dışıdır | yok | KRP-2401, vaka sınırı | KRP-X01 | not-applicable | Payments Counsel ayrı ele alır |
| Satıcı mutabakatı | Satıcıya TRY mutabakatı yapılır | Aracı → satıcı | KRP-2401, olgu 4 | KRP-A01, KRP-I01 | pass | Product mutabakat birimini kayda alır |
| Akış sürümü | Diyagram ve özet `checkout-v3`; dağıtılan sürüm yok | Product | KRP-2401, olgu 5 | KRP-R01, KRP-M01 | unknown | Product dağıtılan sürümü doğrular |
| İnsan onayı | Üç rolün lansman onayı yoktur | Payments Counsel, Compliance, Product | KRP-2401, olgu 6 | KRP-Y01, KRP-R01 | fail | Üç rol yazılı karar üretir |
| İzleme kaydı | Sahip, tarih ve tetikler sağlanmamıştır | unknown | KRP-2401, olgu 7 | KRP-M01 | unknown | Product izleme sahibini atar |

## Eksik veya çelişkili bilgi

- Cüzdan ve hesap yapısı sağlanmamıştır (KRP-A01, KRP-X01): varlık kaydı
  tamamlanamaz. Sahip sağlanmamıştır.
- Dağıtılan checkout sürümü sağlanmamıştır (KRP-R01, KRP-M01): `checkout-v3`
  yalnız diyagram ve ürün özeti için bildirilmiştir; değerler uzlaştırılmamıştır.
- Payments Counsel, Compliance ve Product lansman onayı yoktur (KRP-Y01).
- İzleme sahibi, inceleme tarihi ve değişiklik tetikleri `unknown` (KRP-M01).

Bu eksiklikler doldurulmamıştır; kanıt, eşik veya sözleşme üretilmemiştir.

## İnsan yetki rotası

- Payments Counsel: ürün sınırı, taraf rolleri ve resmi kaynağın yorum gerektiren
  noktası (KRP-Y01).
- Compliance: talimat, aracı, dönüşüm ve mutabakat kanıtının doğrulanması.
- Product: cüzdan/hesap kaydı, dağıtılan sürüm, izleme sahipliği ve seçilen ürün
  seçeneğinin uygulanması.

Copilot'un hukuki karar, onay, lansman, ödeme, transfer, durdurma veya ürün
değişikliği yetkisi yoktur. Bu incelemede hiçbir eylem yapılmamış, onay
verilmemiştir.

## Lansman kapısı ve izleme

KRP-R01 kapısı açık değildir: akış kanıtı `unknown` (cüzdan, dağıtılan sürüm),
ürün sınırı `fail` (KRP-O01), sürüm `unknown`, insan onayı `fail`.

KRP-M01 izleme kaydı: akış sahibi `unknown`, akış sürümü `checkout-v3` (yalnız
diyagram ve özet; dağıtılan sürüm `unknown`), inceleme tarihi `unknown`,
değişiklik tetikleri `unknown`. Checkout, cüzdan, dönüşüm, aracı veya mutabakat
adımı eklenmesi yeni insan incelemesini tetikler.

## Sınırlar

Bu çalışma yalnız KRP-2401'de sağlanan ödeme akışı olgularını ve KRP-1.0
kurallarını kullanır. Hukuki tavsiye değildir ve nihai hukuki sonuç içermez.
Kripto varlığın yatırım amacıyla edinilmesi, saklanması veya checkout dışı
transferi hakkında görüş verilmemiştir. TCMB-RG-2021 yalnız yöntem sorusu için
kullanılmış, mevzuat metni aktarılmamıştır. Tüm kararlar ve eylemler insan
yetkililere aittir.
