---
name: isg-risk-degerlendirme
description: "Paletleme robotu gibi işyeri değişikliklerinde mevcut risk değerlendirmesinin kapsamını, ekip katılımını, tehlike ve kontrol kanıtını, aksiyon sahipliğini ve devreye alma kapısını incelemek için kullan. Türkçe, kanıta dayalı ve insan kararına bağlı İSG yönetişim taslağı üretir."
license: MIT
---

# İSG risk değerlendirmesi

İşyeri değişikliklerini sağlanan kanıt ve sentetik şirket politikasıyla incele.
Bu skill hukuki, mühendislik veya tıbbi tavsiye ya da mühendislik
sertifikasyonu vermez. İnsanlar bütün karar ve eylemlerin sahibidir; Copilot
değerlendirmeyi kabul edemez, kurul kararı veremez, devreye alamaz veya
çalışmayı durduramaz.

## Zorunlu aşamalı okuma

Yanıtı tamamlamadan önce beş referansın tümünü sırayla oku:

1. [Kamusal yöntem](./references/public-method.md): resmî kaynaktan kısa,
   atıflı inceleme yöntemi ve yeniden kullanım sınırı.
2. [Şirket politikası](./references/company-policy.md): sentetik karar
   sınıfları, seçenekler, kurallar ve insan yetkisi.
3. [Kanıt haritası](./references/evidence-map.md): vaka olguları ve `unknown`
   kalması gereken boşluklar.
4. [Çıktı şeması](./references/output-schema.md): zorunlu başlıklar, tablo ve
   durum değerleri.
5. [Senaryo rehberi](./references/scenario-guide.md): değişiklik, çelişki,
   olay, yeniden tasarım ve yetki uyuşmazlığı işlemi.

Kamusal yöntemi, sentetik politikayı ve kurgusal vaka olgularını birbirine
karıştırma. Resmî kaynak şirket adına karar vermez; şirket politikası mevzuat
yerine geçmez; vaka olguları başka tesise genellenmez.

## İnceleme akışı

1. Talep edilen devreye alma durumunu ve mevcut değerlendirme tarihini kaydet.
2. ISG-D01 ile ekipman, yerleşim, görev, yazılım, bakım ve insan-makine
   etkileşimi değişikliklerini mevcut belgenin kapsamıyla karşılaştır.
3. ISG-T01 ile sağlanan katılım kaydını işveren temsilcisi, İSG
   profesyonelleri, çalışan temsilcisi, operatör ve bakım rolleri bakımından
   incele. Eksik katılımı olmuş gibi gösterme.
4. ISG-H01 ile her tehlikeyi kontrol ve kanıta eşle. Koruma, erişim, sıkışma,
   beklenmeyen hareket, enerji izolasyonu ve bakım senaryolarını ayrı izle.
5. Her satırı yalnızca `pass`, `fail`, `unknown` veya `not-applicable` olarak
   sınıflandır. Sağlanmayan test sonucu, eşik veya tasarım ölçüsü uydurma.
6. ISG-O01 uyarınca her açık bulguya sağlandığı ölçüde insan sahibi,
   doğrulanabilir aksiyon ve hedef tarih bağla; eksik alanları `unknown` tut.
7. Tam bir karar sınıfı seç: `accept-assessment`, `renew-assessment`,
   `hold-for-evidence`, `escalate-isg-board` veya `reject-commissioning`.
8. Tam bir seçenek seç: `commission-now`, `hold-commissioning` veya
   `redesign-work-cell`. Talep edilen seçeneğin durumunu ayrıca yaz.
9. ISG-A01 ile işveren ve İSG profesyonellerinin yetkisini koru. ISG-R01
   kapısını yalnızca sağlanan ve insan tarafından doğrulanan kanıtla değerlendir.
10. ISG-M01 kapsamında olay, ramak kala, kontrol arızası ve yeni değişikliği
    yeniden inceleme tetikleri olarak göster; sağlanmayan izleme ayrıntılarını
    `unknown` bırak.

## Kaynak gösterme

- Sentetik politika uygulamasını tam kural kimliğiyle göster.
- Vaka olgusunu `case-brief.md` başlığı veya madde adıyla göster.
- Kamusal yöntemi yayıncı, başlık ve URL ile kısa biçimde atfet; uzun metin
  kopyalama.
- Çıkarımı `Judgement`, eksik bilgiyi `Missing information` olarak ayır.

Yanıt, sağlanan dosyalara dayalı danışma taslağıdır. Yetkili insanlar gözden
geçirmeden hiçbir saha veya devreye alma eylemine dönüşmez.
