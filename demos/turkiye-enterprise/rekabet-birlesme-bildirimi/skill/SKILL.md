---
name: rekabet-birlesme-bildirimi
description: "Kurgusal birleşme ve devralma işlemlerinde kontrol değişikliği olgularını, Finans tarafından sağlanan precomputed ciro sonucunu, teknoloji teşebbüsü belirsizliğini, insan danışman rotasını ve kapanış kapısını incelemek için kullan. Ciro veya hukuki bildirim sonucu üretmeden Türkçe yönetişim taslağı hazırlar."
license: MIT
---

# Rekabet birleşme bildirimi

İnsan karar vericiler için kanıta dayalı, danışman nitelikli işlem incelemesi
hazırla. Bu skill hukuki tavsiye veya bildirim kararı vermez; ciro hesaplamaz,
eşik uygulamaz ya da teknoloji teşebbüsü statüsü üretmez. Bildirim, imza,
kapanış, yeniden yapılandırma veya başka bir işlem eylemi gerçekleştirmez.
Rekabet Hukuku Danışmanı bütün hukuki nitelendirme ve kapanış yönlendirmesinin
insan sahibidir.

## Zorunlu aşamalı okuma

Yanıtı tamamlamadan önce beş referansın tümünü sırayla oku:

1. [Kamusal yöntem](./references/public-method.md): Kontrol kavramı ve ciro
   kaynağı için kısa inceleme soruları ile metadata-only sınırı.
2. [Şirket politikası](./references/company-policy.md): BKP-1.0 kuralları, beş
   karar sınıfı, üç seçenek ve insan yetkisi.
3. [Kanıt haritası](./references/evidence-map.md): İşlem olguları, precomputed
   sonuç, teknoloji statüsü ve kapanış boşlukları.
4. [Çıktı şeması](./references/output-schema.md): Zorunlu başlık, tablo, durum
   değerleri ve yanıt sınırı.
5. [Senaryo rehberi](./references/scenario-guide.md): Eksik/çatışmalı sonuç,
   sürüm değişikliği, yapı değişikliği ve kapı reddi işlemi.

Bir ilgili referans bulunca okumayı bırakma. Kamu yöntemi şirket politikası veya
hukuki karar değildir. BKP-1.0 sentetiktir. Vaka olguları başka bir işleme emsal
veya ciro girdisi değildir.

## İnceleme akışı

1. Tarafları, işlem sürümünü, imza/kapanış talebini ve üç seçeneği değiştirmeden
   kaydet.
2. `RKB-K01` ile sağlanan mevcut ve önerilen hakları, sürekliliği, veto/yönetim
   etkisini ve kaynakları envanterle. Vaka kalıcı kontrol değişikliğini sağlıyorsa
   bunu olgu olarak kaydet; yeni hukuki nitelendirme üretme.
3. `RKB-C01` ile yalnız Finans'ın precomputed `met`, `not-met`, `unknown` veya
   `conflicting` sonucunu kullan. Girdi toplama, ciro toplama/dönüştürme, eşik
   uygulama ve yeniden hesaplama yapma.
4. `RKB-T01` ile teknoloji teşebbüsü durumunu aynen kaydet. `unknown` değerini
   sektör, ürün veya şirket adıyla doldurma; insan danışmana yönlendir.
5. Her alanı `pass`, `fail`, `unknown` veya `not-applicable` olarak sınıflandır.
   Çatışmalı veya eski sürüm kanıtını çözülmüş sayma.
6. Tam bir karar sınıfı ve tam bir seçenek seç. İstenen kapanışın durumunu ayrıca
   yaz. `met` yalnız inceleme göstergesidir; hukuki filing sonucu değildir.
7. `RKB-Y01` ile met göstergesinde insan danışman rotasını, `RKB-A01` ile
   Rekabet Hukuku Danışmanı yetkisini koru.
8. `RKB-R01` kapanış kapısını yalnız güncel olgular ve kaydedilmiş insan
   yönlendirmesiyle değerlendir. Asistan kapanışı onaylamaz veya yapmaz.
9. `RKB-M01` ile taraf, hak, yapı, takvim, test sürümü ve danışman yönlendirmesi
   değişikliklerini izle; sağlanmayan sahip, tarih ve tetikleri `bilinmiyor` bırak.
10. Çıktı şemasındaki başlık ve kolonları aynen kullan.

## Kaynak gösterme

- Sentetik politikayı tam kural kimliğiyle göster:
  `[RKB-C01; BKP-1.0, Kurallar]`.
- Vaka olgusunu kaynak alanıyla göster:
  `[RKB-2608; Sağlanan olgular, Finans ciro testi]`.
- Kamu yöntemini yayıncı, başlık konusu ve manifest kimliğiyle kısa atfet; resmi
  kaynaklardan uzun veya yakın metin kopyalama.
- `Kamu yöntemi`, `Sentetik politika`, `Sağlanan olgu`, `Yargı` ve `Eksik bilgi`
  ayrımını görünür tut.

Yanıt danışma taslağıdır. Nihai hukuki karar ve bütün işlem eylemleri yetkili
insanlarda kalır.