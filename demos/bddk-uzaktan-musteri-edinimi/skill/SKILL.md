---
name: bddk-uzaktan-musteri-edinimi
description: "Kurgusal banka uzaktan müşteri edinimi akışlarını sağlanan kanıt ve sentetik şirket politikasıyla incele; yöntem envanteri, etkileşim/doğrulama, canlılık/bütünlük, kayıt, insan yetkisi, canlıya geçiş ve izleme kapılarını izlenebilir bir karara dönüştür."
license: MIT
---

# BDDK uzaktan müşteri edinimi

İnsan karar vericiler için kanıta dayalı, danışman nitelikli bir inceleme hazırla.
Bu skill hukuki tavsiye, resmi uygunluk sonucu veya teknik sertifika vermez.
Müşteri edinimi, sistem değişikliği, canlıya geçiş, onay veya kontrol eylemi
gerçekleştirmez. Güvenlik, Uyum ve Hukuk bütün karar ve eylem yetkisini korur.

## Zorunlu aşamalı okuma

İncelemeyi tamamlamadan önce aşağıdaki beş referansın tamamını sırayla oku:

1. [Kamusal yöntem](./public-method.md): Dış kaynaktan sentezlenen
   inceleme soruları ve kamu kaynağı sınırı.
2. [Şirket politikası](./company-policy.md): UME-1.0 kuralları, beş
   karar sınıfı, üç seçenek ve insan yetkisi.
3. [Kanıt haritası](./evidence-map.md): Temel vakanın sağlanan ve
   eksik kanıtları ile kesin kaynak yolları.
4. [Çıktı şeması](./output-schema.md): Zorunlu başlıklar, tablolar,
   durum değerleri ve yanıt sınırı.
5. [Senaryo rehberi](./scenario-guide.md): Eksik, çatışmalı, yeniden
   tasarlanmış ve manuel geri dönüş senaryoları.

Bir eşleşme bulunca okumayı bırakma. Kamu yöntemi şirket kuralı değildir;
UME-1.0 sentetik politikadır; vaka verileri resmi ölçüt veya emsal değildir.

## İnceleme akışı

1. Talebi, canlıya geçiş durumunu ve üç seçeneği değiştirmeden kaydet.
2. `BDK-I01` ile kanal, adım, rol, doğrulama, istisna ve geri dönüş envanterini
   çıkar. Verilmeyen alanı `bilinmiyor` bırak.
3. `BDK-V01` ile canlı veya görüntülü etkileşim ve doğrulama kanıtını ayrı ayrı
   eşle. E-posta kimlik taraması ve selfie'den ek kanıt çıkarma.
4. `BDK-L01` ile canlılık, oturum bütünlüğü, tekrar/aktarım savunması ve test
   sonucunu incele. Tedarikçi iddiasını test veya sertifikasyon sonucu sayma.
5. `BDK-K01` ile olay, yöntem sürümü, karar, kanıt, istisna ve sonuç kayıtlarını
   ara. Günlük sağlanmadıysa varmış gibi davranma.
6. Her kapıyı `pass`, `fail`, `unknown` veya `not-applicable` olarak sınıflandır.
7. Tam bir karar sınıfı ve tam bir seçenek seç. İstenen canlıya geçişin durumunu
   ayrıca yaz. Koşul yalnız sağlanan ve nesnel doğrulanabilir bir eksikliği
   kapatıyorsa kullanılabilir.
8. `BDK-A01` uyarınca Güvenlik, Uyum ve Hukuk rotasını koru. Hukuki yorumu bu
   insanlar yapar.
9. `BDK-R01` ile canlıya geçiş kapısını, `BDK-M01` ile dolandırıcılık ve kontrol
   izleme alanlarını uygula. Sağlanmayan sahip, sıklık, eşik ve geri dönüş
   tetiğini üretme.
10. Çıktı şeması başlıklarını ve tablo kolonlarını aynen kullan.

## Kaynak gösterme

- Sentetik şirket politikasını kural kimliğiyle göster:
  `[BDK-L01; UME-1.0, Kurallar]`.
- Vaka bulgusunu alan ve kaynakla göster:
  `[UME-2408; Sağlanan kanıt, Canlılık kanıtı]`.
- Kamu yöntemini yayıncı, başlık konusu ve manifest kimliğiyle kısa biçimde
  göster; resmi metinden uzun veya yakın alıntı yapma.
- `Kamu yöntemi`, `Sentetik politika`, `Sağlanan vaka`, `Yargı` ve `Eksik bilgi`
  ayrımını görünür tut.

Yanıt danışman niteliklidir. Nihai karar ve uygulama yetkili insanlardadır.