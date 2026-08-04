---
name: kripto-odeme-kapisi
description: "Kurgusal kripto ödeme ürünü akışlarını resmi kaynak yöntemi ve sentetik şirket politikasıyla incele; varlık işlevini, ödeme aracısını, satıcı mutabakatını, eksik akış kanıtını, insan yetkisini ve lansman kapısını ayır. Kripto checkout ürün sınırı, USDT satıcı ödemesi veya ödeme dışı yeniden tasarım incelemesinde kullan."
license: MIT
---

# Kripto ödeme kapısı

İnsan karar vericiler için kanıta dayalı, danışman bir ürün sınırı incelemesi
hazırla. Bu skill hukuki tavsiye veya nihai hukuki karar vermez. Lansman,
ödeme, transfer, ürün ayarı, durdurma ya da başka bir eylemi otonom yapamaz.

## Önce oku

1. Resmi kaynağın kısa yöntem soruları için [public-method.md](./public-method.md).
2. Sentetik KRP-1.0 kuralları için [company-policy.md](./company-policy.md).
3. Kanonik vaka olguları için [evidence-map.md](./evidence-map.md).
4. Zorunlu yanıt biçimi için [output-schema.md](./output-schema.md).
5. Eksik, çelişkili ve kapsam dışı varyantlar için [scenario-guide.md](./scenario-guide.md).

Katmanları ayrı tut. Resmi yayın inceleme yöntemine bilgi verir; Kurgusal Ödeme
politikası, ürün kararı veya hukuki tavsiye değildir. KRP-1.0 kurgusal ve
sentetik şirket politikasıdır. KRP-2401 kurgusal vaka olgularıdır.

## İş akışı

1. İstenen akışı, lansman durumunu ve izin verilen üç seçeneği değiştirmeden kaydet.
2. KRP-A01 ile varlık türünü, işlevi, ödeyeni, satıcıyı, hesabı, dönüşümü ve mutabakat birimini çıkar.
3. KRP-I01 ile talimattan satıcı mutabakatına kadar her aktörü ve adımı eşle; ödeme hizmeti aracısını açıkça göster.
4. Kripto varlık satıcı alımını doğrudan kapatıyorsa KRP-O01 ürün sınırını uygula. Aracının yokluğunu tek başına ödeme işlevinin yokluğu sayma.
5. Sağlanmayan veya çelişkili her belirleyici olguyu KRP-X01 uyarınca `unknown` tut. Kanıt, eşik, sözleşme veya akış adımı uydurma.
6. Tam olarak bir karar sınıfı seç: `approve-nonpayment-service`, `revise-product-boundary`, `hold-for-flow-evidence`, `escalate-payments-counsel` veya `reject-payment-flow`.
7. Tam olarak bir seçenek seç: `launch-current-flow`, `remove-crypto-checkout` veya `redesign-nonpayment-service`. İstenen mevcut akışın durumunu ayrıca belirt.
8. KRP-Y01 kapsamında Payments Counsel, Compliance ve Product rollerini yönlendir. Nihai karar, onay ve eylem yetkisini insanlarda bırak.
9. KRP-R01 lansman kapısını ve KRP-M01 akış/sürüm izlemesini uygula. Sağlanmayan sahip, sürüm, tarih ve değişiklik tetiklerini `unknown` yaz.
10. Çıktı şemasındaki başlıkları ve tablo sütunlarını aynen kullan.

Resmi yöntem için yayın başlığını ve konu adını kullan; mevzuat metni aktarma.
Sağlanan ödeme akışının ötesinde yatırım veya transfer hukukuna ilişkin görüş
verme. Copilot yalnız danışman analiz hazırlar; tüm kararlar ve eylemler insan
yetkililere aittir.