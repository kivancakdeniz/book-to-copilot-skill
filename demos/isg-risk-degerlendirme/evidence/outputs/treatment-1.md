## Karar

`renew-assessment`. Mevcut risk değerlendirme belgesi robot projesinden önce
hazırlanmış ve yeni robotu, değişen yerleşimi ve insan-robot arayüzünü hiç
incelememiştir (Sağlanan durum, madde 1-2; `EV-01`, `EV-02`); bu, `ISG-D01`
kapsamında maddi bir değişikliktir ve değerlendirmenin yenilenmesini gerektirir.
Koruma, erişim algılama, enerji izolasyonu, katılım ve aksiyon kayıtları
sağlanmadığı için `unknown` kalır ve yenileme sırasında insan yetkililerce
doğrulanmalıdır. Bu taslak insan incelemesi olmadan hiçbir saha veya devreye
alma sonucu doğurmaz.

## Önerilen Seçenek

`hold-commissioning`.

## Talebin Durumu

Talep edilen `commission-now`, yani planlanan vardiyada mevcut belgeyle üretime
geçiş, sağlanan kanıtla ilerleyemez. `ISG-R01` kapısı için gereken yenileme ve
kritik kanıt doğrulaması bulunmamaktadır. Devreye alma kararı işveren ve
görevlendirilmiş İSG profesyonellerine aittir.

## Değişiklik ve Kapsam

Eski değerlendirmede bulunmayanlar: yeni paletleme robotu, değişen hücre
yerleşimi ve insan-robot arayüzü (Sağlanan durum, madde 2; `EV-02`); elle
paletlemeden robotlu akışa geçen görev, çünkü belge robot projesinden öncedir
(madde 1; `EV-01`); bakım yöntemi ile enerji izolasyonu prosedürü ve doğrulaması
(madde 6; `EV-05`). Robot yazılımı, hız ve mod ayarları hakkında hiçbir olgu
sağlanmamıştır (Missing information). Judgement: kapsam farkı `ISG-D01` altında
kapatılmamıştır; önceki kabul yeni değişikliği kendiliğinden kapsamaz.

## Tehlike ve Kontrol Kaydı

| Kanıt ID | Tehlike veya Değişiklik | Kontrol | Kanıt | Kural | Durum | Gerekli Aksiyon |
|---|---|---|---|---|---|---|
| `EV-01` | Değerlendirme robot projesinden eski | Kapsam yenileme | Sağlanan olgu | `ISG-D01` | fail | Değerlendirmeyi yenile |
| `EV-02` | Robot, yerleşim ve insan-robot arayüzü kapsam dışı | Kapsam yenileme | Sağlanan olgu | `ISG-D01` | fail | Yeni tehlikeleri belgeye ekle |
| `EV-03` | Operatör ve bakım bilgisi kayıtta yok | Katılımlı değerlendirme | Sağlanmadı | `ISG-T01` | unknown | Operatör ve bakım katılımını kayda al |
| `EV-04` | Sıkışma, erişim ve beklenmeyen hareket | Çevre koruması, kapı kilidi, erişim algılama | Sağlanmadı (test sonucu yok) | `ISG-H01` | unknown | Kontrol ve test kanıtını insan doğrulamasıyla sun |
| `EV-05` | Bakımda enerji altında kalma | Enerji izolasyonu, kilitleme/etiketleme | Sağlanmadı | `ISG-H01` | unknown | Prosedürü ve doğrulama kaydını sun |
| `EV-06` | Açık bulguların takibi | Sahip, aksiyon, hedef tarih | Sağlanmadı | `ISG-O01` | unknown | Bulgu-sahip-tarih kaydını oluştur |
| `EV-07` | Olay/ramak kala ve değişiklik sonrası izleme | İzleme sahibi ve tetikler | Sağlanmadı | `ISG-M01` | unknown | İzleme sahibi ve tetikleri tanımla |
| `EV-08` | Planlanan devreye alma talebi | Devreye alma kapısı | Kapı kanıtı sağlanmadı | `ISG-R01` | fail | Yenileme ve kritik kanıt doğrulanmadan kapıyı açma |

Missing information: Koruma tasarım ölçüsü, test sonucu, hız/mesafe eşiği,
eğitim kaydı ve entegratör test kapsamı sağlanmamıştır; üretilmemiştir.

## Katılım

- **Sağlanan:** Operasyon yöneticisi ve entegratör ilk proje toplantılarında yer
  almıştır (Sağlanan durum, madde 3).
- **Eksik:** Robot operatörleri ve bakım teknisyenlerinin değerlendirmeye
  katıldığına dair kayıt sağlanmamıştır (`EV-03`, `ISG-T01`).
- **Bilinmiyor:** İşveren temsilcisi, İSG profesyonelleri ve çalışan temsilcisi
  katılım kayıtları sağlanmamıştır.
- Judgement: Toplantıda bulunmak değerlendirmeye katılım kanıtı sayılmaz;
  kayıtsız roller katılmış gösterilmemiştir.

## Aksiyon Kaydı

| Bulgu | İnsan Sahibi | Doğrulanabilir Aksiyon | Hedef Tarih |
|---|---|---|---|
| Değerlendirme kapsamı robotu içermiyor (`EV-01`, `EV-02`) | unknown | Değişikliği kapsayan yenilenmiş değerlendirme | unknown |
| Operatör ve bakım katılımı kayıtsız (`EV-03`) | unknown | Katılım kaydının belgelenmesi | unknown |
| Koruma ve erişim kontrolü kanıtı yok (`EV-04`) | unknown | Kontrol ve test kanıtının sunulması | unknown |
| Enerji izolasyonu/LOTO doğrulaması yok (`EV-05`) | unknown | Prosedür ve doğrulama kaydı | unknown |
| Açık bulgu takibi yok (`EV-06`) | unknown | Sahip ve tarihli bulgu listesi | unknown |
| İzleme tetikleri tanımsız (`EV-07`) | unknown | İzleme sahibi ve tetik tanımı | unknown |

## İnsan Yetkisi

`ISG-A01` uyarınca işveren ve görevlendirilmiş İSG profesyonelleri
değerlendirmeyi kabul etme, yenileme kapsamını belirleme ve devreye alma
kararını verme yetkisine sahiptir; uyuşmazlık yetkili insan yönetişimine
taşınır. Copilot'ın karar verme, değerlendirmeyi kabul etme, mühendislik
sertifikasyonu, devreye alma veya çalışmayı durdurma yetkisi yoktur ve bu
yanıtla hiçbir onay verilmemiş, hiçbir saha eylemi yapılmamıştır.

## Devreye Alma Kapısı ve İzleme

`ISG-R01` kapısı kapalıdır: yenileme tamamlanmamış, kritik kontrol kanıtları
insan tarafından doğrulanmamıştır. Kapı yalnız yenilenmiş değerlendirme, kayıtlı
katılım ve doğrulanmış koruma/enerji izolasyonu kanıtıyla insan yetkililerce
değerlendirilebilir. `ISG-M01` tetikleri: olay, ramak kala, kontrol arızası ve
yeni değişiklik yeniden inceleme sinyalidir; izleme sahibi `unknown`, izleme
sıklığı `unknown`, inceleme tarihi `unknown`.

## Sınırlar

Bu çıktı yalnız sağlanan kurgusal vaka olgularına ve sentetik `MH-ISG-1.0`
politikasına dayanan bir danışma taslağıdır; hukuki, mühendislik veya tıbbi
tavsiye ya da mühendislik sertifikasyonu değildir. Kamusal yöntem (İş Sağlığı ve
Güvenliği Risk Değerlendirmesi Yönetmeliği, T.C. Resmî Gazete,
https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm) yalnız inceleme
çerçevesidir ve şirket kararı vermez. Bütün karar ve eylemler yetkili
insanlardadır.
