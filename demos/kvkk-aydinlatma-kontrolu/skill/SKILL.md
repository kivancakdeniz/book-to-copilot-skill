---
name: kvkk-aydinlatma-kontrolu
description: Sentetik şirket politikasıyla KVKK aydınlatma taslaklarını kanıt, ayrım, aktarım ve insan yetkisi sınırlarında inceleyen Türkçe karar skill'i.
license: MIT
---

# KVKK aydınlatma kontrolü

Bir veri toplama yüzeyi ve taslak aydınlatma verildiğinde yalnız sağlanan
olgularla izlenebilir bir yayın kararı hazırla. Resmî hukuk ve rehberlik kamuya
açık yöntemdir; sentetik şirket politikası şirket kararlarını
operasyonelleştirir. Bunları birbirinin yerine kullanma.

Bu skill hukuki tavsiye veya nihai hukuki sonuç vermez. İnsan Privacy Counsel,
Data Protection/Compliance ve Product Owner kararın sahibidir. Yayına alma,
rıza toplama, veri aktarımı, kayıt değiştirme veya başka bir otonom eylem yapma.

## Karar sınıfları

Tam olarak birini seç:

1. `approve`
2. `revise-before-launch`
3. `hold-for-evidence`
4. `escalate-privacy`
5. `reject`

## Seçenekler

Tam olarak birini seç:

1. `current-notice`
2. `separate-notice-and-consent`
3. `no-launch`

## Çalışma akışı

1. Toplanan alanları, kaynakları, amaçları, yöntemi, alıcı/işleyenleri ve aktarım
   olgularını envanterle.
2. Aydınlatmanın zorunlu karar alanlarını kamu yöntemiyle kontrol et.
3. Aydınlatma ile pazarlama rızasını ayrı değerlendir.
4. Her sonucu sağlanan olguya ve sentetik politika kuralına bağla; bilinmeyeni
   uydurma.
5. Bir karar sınıfı ve bir seçenek seç; gerekli insan rotasını göster.
6. Yanıtı zorunlu şemayla üret ve hiçbir eylemi kendin yürütme.

## Referanslar

- [Kamu yöntemi](public-method.md)
- [Şirket politikası](company-policy.md)
- [Kanıt haritası](evidence-map.md)
- [Çıktı şeması](output-schema.md)
- [Senaryo rehberi](scenario-guide.md)