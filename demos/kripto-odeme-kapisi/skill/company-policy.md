# Şirket politikası

KRP-1.0 kurgusal ve sentetik Kurgusal Ödeme politikasıdır; hukuki tavsiye veya hukuk
metni değildir.

## Kurallar

| Kural | Uygulama |
|---|---|
| KRP-A01 | Varlık türü, işlev, hesap, dönüşüm, ödeyen, satıcı ve mutabakat birimini yalnız sağlanan olgularla kaydet. |
| KRP-O01 | Kripto varlık satıcı alımını doğrudan kapatıyorsa mevcut akış lansmanı geçemez. |
| KRP-I01 | Talimat, cüzdan, dönüşüm, transfer, aracı ve satıcı mutabakatının tümünü eşle. |
| KRP-X01 | Eksik veya çelişkili belirleyici olguları `unknown` tut ve kanıt için beklet. |
| KRP-Y01 | Payments Counsel, Compliance ve Product karar verir; Copilot danışmandır. |
| KRP-R01 | Akış kanıtı, ürün sınırı, sürüm ve insan onayı tamamlanmadan lansman yoktur. |
| KRP-M01 | Akış sahibi, sürüm, inceleme tarihi ve değişiklik tetikleri kaydedilir; eksikler `unknown` kalır. |

## Beş karar sınıfı

- `approve-nonpayment-service`: ödeme dışı işlev ve tüm kapılar sağlanan olgularla doğrulanmıştır.
- `revise-product-boundary`: mevcut istek geçmez; sağlanan daha dar sınır doğrulanabilir bir revizyondur.
- `hold-for-flow-evidence`: belirleyici akış kanıtı eksik veya çelişkilidir.
- `escalate-payments-counsel`: ürün sınırı, taraf rolü veya kapsam dışı hukuki soru insan hukuki kararı gerektirir.
- `reject-payment-flow`: sağlanan akış kripto varlığı satıcı alımını doğrudan kapatmak için kullanır.

## Üç ürün seçeneği

- `launch-current-flow`
- `remove-crypto-checkout`
- `redesign-nonpayment-service`

Tam olarak bir sınıf ve bir seçenek seç. Copilot hukuki karar veremez; lansman,
ödeme, transfer, durdurma veya ürün değişikliği yapamaz.