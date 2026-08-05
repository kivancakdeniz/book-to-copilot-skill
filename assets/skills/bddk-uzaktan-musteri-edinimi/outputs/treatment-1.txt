## Karar

- Karar sınıfı: `hold-for-security-evidence`
- Önerilen seçenek: `manual-onboarding-fallback`
- İstenen canlıya geçiş: `beklemede`
- Kısa gerekçe: Etkileşim, canlılık, bütünlük, kayıt ve izleme kanıtlarının hiçbiri
  sağlanmadı [UME-2408; Sağlanan kanıt]. E-posta taraması ve selfie `BDK-V01`
  eşiğini tek başına karşılamaz; `BDK-L01`, `BDK-K01` ve `BDK-M01` kanıtsız
  olduğu için `BDK-R01` canlıya geçişi kapalı tutar [BDK-R01; UME-1.0, Kurallar].
  Zorunlu kanıt ve üç insan onayı tamamlanana kadar manuel edinim yolu önerilir.

## Yöntem envanteri

| Kanal/adım | İnsan veya sistem rolü | Doğrulama noktası | İstisna/geri dönüş | Kaynak | Durum |
|---|---|---|---|---|---|
| E-posta ile kimlik belgesi taraması | Aday müşteri gönderir; alıcı görevli bilinmiyor | Sağlanmadı | bilinmiyor | [UME-2408; İş talebi, adım 1] (`UME-E02`) | fail |
| Aynı e-postada tek selfie | Aday müşteri gönderir | Sağlanmadı | bilinmiyor | [UME-2408; İş talebi, adım 2] (`UME-E03`) | fail |
| Dosyaların görülüp müşteri sistemine aktarılması | Operasyon ekibi | Görevli doğrulaması sağlanmadı | bilinmiyor | [UME-2408; İş talebi, adım 3] (`UME-E04`) | unknown |
| Canlı veya görüntülü etkileşim adımı | bilinmiyor | Sağlanmadı | bilinmiyor | [UME-2408; Sağlanan kanıt, Canlı veya görüntülü etkileşim] (`UME-X01`) | fail |

`BDK-I01` envanteri eksiktir: kanal, rol, istisna ve geri dönüş alanları
`bilinmiyor` kalır [BDK-I01; UME-1.0, Kurallar].

## Kontrol ve kanıt kapıları

| Kural | Sağlanan kanıt | Eksik/çatışmalı bilgi | Bulgu | Kaynak |
|---|---|---|---|---|
| `BDK-I01` | Üç adımlık akış tanımı | Kanal, rol, istisna, geri dönüş haritası | unknown | [UME-2408; Sağlanan kanıt, Yöntem envanteri] |
| `BDK-V01` | E-posta kimlik taraması ve selfie | Canlı/görüntülü etkileşim ve doğrulama kanıtı | fail | [UME-2408; Sağlanan kanıt, Etkileşim ve kimlik doğrulama kanıtı] (`UME-X01`) |
| `BDK-L01` | Sağlanmadı | Canlılık, oturum bütünlüğü, tekrar/aktarım testi | unknown | [UME-2408; Sağlanan kanıt, Canlılık kanıtı] (`UME-X02`) |
| `BDK-K01` | Sağlanmadı | Kontrol ve denetim günlükleri | unknown | [UME-2408; Sağlanan kanıt, Kontrol ve denetim günlükleri] (`UME-X03`) |
| `BDK-A01` | Sağlanmadı | Güvenlik, Uyum, Hukuk onayı | fail | [UME-2408; Sağlanan kanıt, Güvenlik, Uyum ve Hukuk onayı] (`UME-X05`) |
| `BDK-R01` | Sağlanmadı | Tamamlanmış kapılar ve onaylar | fail | [UME-2408; İş talebi] (`UME-E01`) |
| `BDK-M01` | Sağlanmadı | Sahip, sıklık, eşik, geri dönüş tetiği | unknown | [UME-2408; Sağlanan kanıt, Dolandırıcılık ve kontrol izleme planı] (`UME-X04`) |

## Gerekli insan kararı

- **Güvenlik:** Canlılık, oturum bütünlüğü, tekrar ve aktarım savunmasının test
  kapsamı ile sonucunun gerçekten bulunup bulunmadığına karar verir (`BDK-L01`).
- **Uyum:** Kontrol ve denetim günlüklerinin kapsamını, dolandırıcılık izleme
  sahibini, sıklığını, eşiğini ve durdurma tetiklerini belirler
  (`BDK-K01`, `BDK-M01`).
- **Hukuk:** Uzaktan yöntemin uygulanabilirliğini ve yorumunu değerlendirir;
  bu paket hukuki sonuç içermez (`BDK-A01`).
- **Üçü birlikte:** `compliant-redesign` mi yoksa manuel yolun sürdürülmesi mi
  seçileceğine ve canlıya geçiş kapısının açılıp açılmayacağına karar verir
  (`BDK-A01`, `BDK-R01`).
- Asistanın karar, onay, canlıya geçiş veya sistem değiştirme yetkisi yoktur.

## Canlıya geçiş ve izleme

| Kapı | Sahip | Tamamlanma kanıtı | Engel veya tetik | Durum |
|---|---|---|---|---|
| `BDK-V01` etkileşim ve doğrulama | bilinmiyor | Sağlanmadı | Canlı/görüntülü etkileşim kanıtı yok | fail |
| `BDK-L01` canlılık ve bütünlük | bilinmiyor | Sağlanmadı | Test kapsamı ve sonucu yok | unknown |
| `BDK-K01` kayıt ve denetim izi | bilinmiyor | Sağlanmadı | Günlük yok | unknown |
| `BDK-A01` üçlü insan onayı | Güvenlik, Uyum, Hukuk | Sağlanmadı | Onay alınmadı | fail |
| `BDK-R01` canlıya geçiş | bilinmiyor | Sağlanmadı | Zorunlu kapılar açık | fail |
| `BDK-M01` dolandırıcılık/kontrol izleme | bilinmiyor | Sağlanmadı | Sahip, sıklık, eşik, geri dönüş tetiği bilinmiyor | unknown |

## Sınırlar

Bu yanıt danışman niteliklidir: hukuki tavsiye, resmi uygunluk sonucu veya teknik
sertifika değildir. Hiçbir sistem, müşteri süreci veya canlıya geçiş eylemi
yapılmadı; hiçbir onay verilmedi. Katmanlar ayrıdır: kamu yöntemi yalnız gözlem
çerçevesidir (Resmî Gazete, uzaktan kimlik tespiti düzenlemesinin metadata'sı,
manifest `resmi-gazete-uzaktan-kimlik-2021`); karar ölçütü sentetik UME-1.0
politikasıdır; bulgular yalnız UME-2408'de sağlanan vakadan gelir; kapı sınıfları
yargımdır; sağlanmayan alanlar eksik bilgi olarak `bilinmiyor` bırakılmıştır.
Nihai karar ve uygulama Güvenlik, Uyum ve Hukuk'tadır.
