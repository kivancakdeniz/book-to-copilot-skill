---
name: masak-musteri-kabul
description: "Kurumsal müşteri kabulünde sağlanan kimlik, nihai faydalanıcı, risk ve fon kaynağı kanıtlarını sentetik şirket politikasına göre incele; sınıf, onboarding seçeneği, insan yetkisi ve kapı üret. Şu durumlarda kullan: KYB/KYC, kurumsal onboarding, yüksek risk işareti, fon kaynağı, nihai faydalanıcı veya müşteri kabul incelemesi."
license: MIT
---

# MASAK müşteri kabul

Bu beceri, insan karar sahipleri için kanıta dayalı kurumsal onboarding notu hazırlar. Hukuki görüş vermez; hesap açmaz, ilişkiyi reddetmez, bildirim yapmaz veya sistemlerde değişiklik yapmaz. SİB/STR kararı vermez ve suç isnadı yapmaz.

## Önce oku

1. Yöntem ve kaynak sınırı için [public-method.md](./references/public-method.md).
2. Karar kuralları için [company-policy.md](./references/company-policy.md).
3. Kanıt konumları için [evidence-map.md](./references/evidence-map.md).
4. Yanıt biçimi için [output-schema.md](./references/output-schema.md).
5. Eksik, çelişkili ve değişken vakalar için [scenario-guide.md](./references/scenario-guide.md).

## İş akışı

1. Müşteri/temsilci kimliği, nihai faydalanıcı zinciri, sağlanan risk olguları, fon kaynağı, ürün talebi ve insan onaylarını çıkar.
2. Eksik veya çelişkili olguyu üretme; ilgili kuralı `unknown` işaretle.
3. AML-C01, AML-R01, AML-E01, AML-F01, AML-S01, AML-A01, AML-G01 ve AML-M01 kurallarını uygula.
4. Yalnız şirket politikasındaki beş sınıftan birini ve üç seçenekten birini seç.
5. Bulguları kaynakla, insan rollerini, onboarding kapısını ve periyodik incelemeyi belirt.
6. Resmi yöntemi sentetik şirket kararı gibi sunma; uzun resmi alıntı kullanma.

AML Officer, Compliance ve business owner son kararı verir. Bildirim değerlendirmesi yalnız yetkili insan sürecindedir.