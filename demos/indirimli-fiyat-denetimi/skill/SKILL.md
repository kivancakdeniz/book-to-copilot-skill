---
name: indirimli-fiyat-denetimi
description: "İndirimli satış kreatiflerinde sağlanan fiyat geçmişini, referans fiyatı ve indirim oranını sentetik şirket politikasına göre incele; karar sınıfı, kampanya seçeneği, insan onayı ve yayın kapısı üret. Şu durumlarda kullan: e-ticaret fiyat reklamı, üzeri çizili fiyat, indirim yüzdesi, kampanya go-live veya fiyat geçmişi incelemesi."
license: MIT
---

# İndirimli fiyat denetimi

Bu beceri, insan karar sahipleri için kanıta dayalı kampanya inceleme notu hazırlar. Hukuki görüş vermez; kampanyayı onaylamaz, yayına almaz veya sistemlerde değişiklik yapmaz.

## Önce oku

1. Yöntem ve kaynak sınırı için [public-method.md](./public-method.md).
2. Karar kuralları için [company-policy.md](./company-policy.md).
3. Kanıt konumları için [evidence-map.md](./evidence-map.md).
4. Yanıt biçimi için [output-schema.md](./output-schema.md).
5. Eksik, çelişkili ve değişken vakalar için [scenario-guide.md](./scenario-guide.md).

## İş akışı

1. Ürün, satıcı, kanal, fiyat geçmişi, karşılaştırma penceresi, sağlanan referans fiyat, sağlanan oran, kreatif ve canlı fiyat olgularını çıkar.
2. Eksik veya çelişkili fiyat/veri varsa hesaplama yapma; ilgili kuralı `unknown` işaretle.
3. FYT-H01, FYT-B01, FYT-O01, FYT-C01, FYT-A01, FYT-R01 ve FYT-M01 kurallarını uygula.
4. Yalnız şirket politikasındaki beş sınıftan birini ve üç seçenekten birini seç.
5. Bulguları kaynakla, insan rollerini ve yayın/izleme kapılarını belirt.
6. Resmi yöntemi sentetik şirket kararı gibi sunma; uzun resmi alıntı kullanma.

İnsan E-commerce Owner, Pricing Owner ve Compliance son kararı verir. Belgelenmiş istisna veya hukuki yorum için Legal gerekir.