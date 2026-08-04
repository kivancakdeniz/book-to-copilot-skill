# Anadolu Sistemleri Birleşme Kontrol Politikası BKP-1.0

Bu belge yalnız demo için hazırlanmış sentetik şirket politikasıdır. Gerçek bir
şirket politikasını, hukuki görüşü veya Rekabet Kurumu kararını temsil etmez.
Asistan yalnız sağlanan işlem olgularını düzenler ve insan incelemesine taslak
hazırlar. Bildirim gerekip gerekmediğine karar vermez, ciro hesaplamaz, işlem
yapısını değiştirmez, imza veya kapanış eylemi yürütmez.

## Kapsam

BKP-1.0, birleşme ve devralma işlemlerinde kontrol değişikliği, Finans tarafından
önceden hesaplanmış ciro testi, teknoloji teşebbüsü durumu, insan yetkisi ve
kapanış kapısının iç incelemesini düzenler. Kamu kaynakları kısa yöntem soruları
sağlar; sentetik politika karar sınıflarını ve şirket kapılarını belirler.

## Kurallar

| Kural | Sentetik şirket şartı |
|---|---|
| `RKB-K01` | Kontrol değişikliği olguları; taraflar, mevcut ve önerilen haklar, süreklilik, veto/yönetim etkisi, işlem sürümü ve kaynakları kaydedilir. Sağlanan hukuki nitelendirme yoksa asistan üretmez. |
| `RKB-C01` | Yalnız Finans tarafından sağlanan önceden hesaplanmış ciro testi sonucu kullanılır: `met`, `not-met`, `unknown` veya `conflicting`. Asistan ciro toplamaz, dönüştürmez, eşik uygulamaz ya da yeniden hesaplamaz. |
| `RKB-T01` | Hedefin teknoloji teşebbüsü durumu `unknown` ise açık bırakılır ve Rekabet Hukuku Danışmanı incelemesine gider. Varsayım, sektör etiketi veya ürün tanımıyla doldurulmaz. |
| `RKB-Y01` | Ciro göstergesi `met` olduğunda Rekabet Hukuku Danışmanı rotası ve kaydedilmiş kapanış yönlendirmesi olmadan kapanış ilerlemez. Bu kural hukuki bildirim sonucu değildir. |
| `RKB-A01` | Bildirim analizi, hukuki nitelendirme ve kapanış yönlendirmesi yalnız Rekabet Hukuku Danışmanı insan yetkisindedir. Finans yalnız önceden hesaplanmış ciro sonucunun sahibidir. |
| `RKB-R01` | Kapanış kapısı; güncel işlem olguları, precomputed sonuç, teknoloji durumu işlemi, danışman yönlendirmesi ve gerekli insan onayları kayda girmeden açılmaz. |
| `RKB-M01` | Taraf, hak, yapı, takvim, ciro testi sürümü, teknoloji durumu ve danışman yönlendirmesi değişiklikleri izlenir; sahip, tarih ve yeniden inceleme tetikleri sürümlenir. Sağlanmayan alan `bilinmiyor` kalır. |

## Karar sözleşmesi

Tam olarak bir karar sınıfı seçilir:

1. `no-filing-indicator`: Sağlanan güncel olgular ve kayıtlı insan danışman
   yönlendirmesi bildirim göstergesi olmadığını belirtir; asistan hukuki karar
   vermez.
2. `legal-notification-review`: Sağlanan göstergeler Rekabet Hukuku Danışmanı
   tarafından bildirim incelemesi gerektirir.
3. `hold-for-turnover-evidence`: Finans’ın precomputed sonucu eksik, eski,
   kapsamı belirsiz veya çatışmalıdır.
4. `escalate-competition-counsel`: Kontrol, teknoloji statüsü, kapsam, yapı veya
   yetki konusu doğrudan insan danışman kararı gerektirir.
5. `reject-transaction-path`: Sponsor zorunlu insan rotasını veya kapanış
   kapısını kabul etmeden işlemi ilerletmek istiyordur.

Tam olarak bir seçenek önerilir:

1. `proceed-closing`: Yalnız sağlanan ve kaydedilmiş insan danışman yönlendirmesi
   ile bütün sentetik kapanış kapıları tamamlandığında değerlendirilir.
2. `hold-closing`: Belirleyici inceleme, kanıt veya yönlendirme tamamlanana kadar
   kapanış ilerlemez.
3. `restructure-review`: Önerilen yapı değişikliği yeni kontrol ve danışman
   incelemesine gider; asistan yeniden yapılandırma tasarlamaz.

## İnsan sınırı

Asistan ciro hesaplamaz, `met` sonucunu hukuki bildirim kararı saymaz ve kapanış
izni vermez. Rekabet Hukuku Danışmanı bildirim ve kapanış yönlendirmesinin tek
insan sahibidir. İmza ve kapanış dahil bütün işlem eylemleri yetkili insanlarda
kalır.