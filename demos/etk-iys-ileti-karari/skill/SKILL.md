---
name: etk-iys-ileti-karari
description: Sentetik şirket politikasıyla ticari elektronik ileti amaçlarını, rıza ve IYS kanıtını, bastırma kapısını ve insan yetkisini inceleyen Türkçe karar skill'i.
license: MIT
---

# ETK/IYS ileti kararı

Bir kampanya özeti ve hedef kitle kanıtı verildiğinde yalnız sağlanan olgularla
izlenebilir bir gönderim kararı hazırla. Resmî hukuk ve rehberlik kamuya açık
yöntemdir; sentetik şirket politikası şirket kararlarını operasyonelleştirir.
Bunları birbirinin yerine kullanma.

Bu skill hukuki tavsiye veya nihai hukuki sonuç vermez. İnsan CRM Owner,
Compliance ve Legal kararın sahibidir. Mesaj gönderme, IYS kaydı değiştirme,
kitle bastırma, kampanya başlatma/durdurma veya başka bir otonom eylem yapma.

## Karar sınıfları

Tam olarak birini seç:

1. `approve-send`
2. `approve-with-controls`
3. `hold-for-iys-evidence`
4. `escalate-legal`
5. `do-not-send`

## Seçenekler

Tam olarak birini seç:

1. `full-audience`
2. `verified-consent-only`
3. `suppress-unverified-audience`

## Çalışma akışı

1. İleti amacını, kanalı ve hedef kitleyi sağlanan içerikle sınıflandır.
2. Kişi ve kanal düzeyinde güncel rıza/IYS kanıtını kontrol et.
3. İstisna iddiasını yalnız sağlanan ilişki ve işlem olgularıyla değerlendir.
4. Ret yolunu ayrı kontrol et; eksik ön dayanağı giderdiğini varsayma.
5. Bir karar sınıfı ve bir seçenek seç; bastırma kapısı ile insan rotasını göster.
6. Yanıtı zorunlu şemayla üret ve hiçbir eylemi kendin yürütme.

## Referanslar

- [Kamu yöntemi](public-method.md)
- [Şirket politikası](company-policy.md)
- [Kanıt haritası](evidence-map.md)
- [Çıktı şeması](output-schema.md)
- [Senaryo rehberi](scenario-guide.md)