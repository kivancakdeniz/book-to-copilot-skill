---
name: titck-ilac-tanitimi
description: "Türkiye'de beşerî tıbbi ürün tanıtım taslaklarını ürün statüsü, hedef kitle, kanal erişimi, iddia kapsamı, insan yetkisi ve yayın kapısı bakımından incelemek için kullan. Türkçe, kanıta dayalı ve Medical, Regulatory, Legal insan kararına bağlı yönetişim taslağı üretir."
license: MIT
---

# TİTCK ilaç tanıtımı

Sağlanan ürün ve materyal olgularını sentetik şirket politikasıyla incele. Bu
skill hukuki, mühendislik veya tıbbi tavsiye ve nihai mevzuat sonucu vermez.
İnsanlar bütün karar ve eylemlerin sahibidir; Copilot onaylayamaz, yayımlayamaz,
hedefleyemez, içeriği kaldıramaz veya kampanyayı durduramaz.

## Zorunlu aşamalı okuma

Yanıtı tamamlamadan önce beş referansın tümünü sırayla oku:

1. [Kamusal yöntem](./public-method.md): iki resmî kaynaktan kısa,
   atıflı inceleme yöntemi ve yeniden kullanım sınırı.
2. [Şirket politikası](./company-policy.md): sentetik karar
   sınıfları, seçenekler, kurallar ve insan yetkisi.
3. [Kanıt haritası](./evidence-map.md): vaka olguları ve `unknown`
   kalması gereken boşluklar.
4. [Çıktı şeması](./output-schema.md): zorunlu başlıklar, tablo ve
   durum değerleri.
5. [Senaryo rehberi](./scenario-guide.md): statü, kanal, iddia,
   erişim değişikliği ve zaten-yayında durumları.

Kamusal yöntemi, sentetik politikayı ve kurgusal vaka olgularını birbirine
karıştırma. Resmî kaynak Kurgusal Farma adına karar vermez; şirket politikası mevzuat
yerine geçmez; vaka olguları gerçek ürüne genellenmez.

## İnceleme akışı

1. TTK-P01 ile ürün adı, statü, statü kaynağı, pazar, hedef kitle ve talebi
   kaydet. Eksik veya çelişkili statüyü `unknown` bırak.
2. TTK-A01 ile briefteki niyet yerine kanalın fiilî erişimini değerlendir.
   Tüketiciye açık sosyal kanal ile profesyonel kanal incelemesini ayır.
3. Kreatifteki ürün adı, fayda, kullanım, çağrı, görsel ve hedefleme
   mesajlarını ayrı iddia satırlarına çıkar.
4. TTK-B01 ile her iddiayı sağlanan onaylı kapsam ve dayanakla eşle. Endikasyon,
   kanıt, güvenlilik, karşılaştırma veya sonuç uydurma.
5. TTK-U01 ile profesyonel erişimi doğrula. Profil etiketi, hashtag veya niyet
   gerçek rol doğrulamasının yerine geçmez.
6. Her satırı yalnızca `pass`, `fail`, `unknown` veya `not-applicable` olarak
   sınıflandır. Eksik Medical, Regulatory veya Legal görüşünü olmuş sayma.
7. Tam bir karar sınıfı seç: `approve-professional-material`,
   `revise-before-use`, `hold-for-product-status`, `escalate-medical-legal` veya
   `do-not-publish`.
8. Tam bir seçenek seç: `consumer-social`, `professional-channel-review` veya
   `no-campaign`. Talep edilen yayının durumunu ayrıca yaz. Profesyonel kanal
   seçeneği yeni materyali veya yayını onaylamaz.
9. TTK-Y01 ile Medical, Regulatory ve Legal yetkisini koru; TTK-R01 kapısını
   yalnız sağlanan ve insanlarca doğrulanan kayıtlarla değerlendir.
10. TTK-M01 kapsamında materyal sürümü, kanal, insan sahibi, gözden geçirme
    tarihi ve düzeltme/kaldırma tetiklerini göster. Sağlanmayan ayrıntıları
    `unknown` bırak ve hiçbir izleme ya da kaldırma eylemi iddia etme.

## Kaynak gösterme

- Sentetik politika uygulamasını tam kural kimliğiyle göster.
- Vaka olgusunu `case-brief.md` başlığı veya madde adıyla göster.
- Kamusal yöntemi yayıncı, başlık ve URL ile kısa biçimde atfet; uzun metin
  kopyalama.
- Çıkarımı `Judgement`, eksik bilgiyi `Missing information` olarak ayır.

Yanıt, sağlanan dosyalara dayalı insan inceleme taslağıdır. Medical, Regulatory
ve Legal onayı olmadan hiçbir yayın veya kanal eylemine dönüşmez.
