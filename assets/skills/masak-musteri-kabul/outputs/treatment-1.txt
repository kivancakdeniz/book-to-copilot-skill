## Öneri

- İnceleme sınıfı: `enhanced-review`
- Onboarding seçeneği: `hold-onboarding`
- Kısa gerekçe: Vaka sisteminin sağladığı `high-risk-geography-supplied` işareti
  AML-E01 uyarınca gelişmiş inceleme gerektirir. Nihai faydalanıcı zincirinin ara
  halkası ve fon kaynağı kanıtı eksik olduğundan AML-C01 ve AML-F01 kapıları
  geçilmemiştir. Bu not danışman niteliktedir; kararı yetkili insanlar verir.

## Kural tablosu

| Kural | Sonuç | Sağlanan kanıt | Politika sonucu |
|---|---|---|---|
| `AML-C01` | fail | Kuruluş, vergi ve imza yetkilisi belgeleri tam işaretli; nihai faydalanıcı zincirinin ara ortaklık halkası eksik, nihai kontrol doğrulanamamış (Sağlanan olgu) | Zincir tamamlanmadan kapı geçilmez; eksik halka Eksik bilgi olarak kalır, üretilmez |
| `AML-R01` | pass | Yalnız sağlanan risk olgusu kullanıldı: `high-risk-geography-supplied` (Sağlanan olgu) | İşaretten ülke, suç veya bildirim sonucu çıkarımı yapılmadı |
| `AML-E01` | fail | Yüksek risk işareti sağlandı; gelişmiş incelemenin yapıldığına dair olgu sağlanmadı (Sağlanan olgu, Eksik bilgi) | Gelişmiş inceleme AML Officer gözetiminde tamamlanmalıdır |
| `AML-F01` | fail | Fon kaynağı alanı yalnız “ticari gelir”; açıklama ve destekleyici kanıt sağlanmadı (Sağlanan olgu) | Açıklama ve kanıt tamamlanmadan kapı geçilmez |
| `AML-S01` | not-applicable | SİB/STR kararı veya suç bulgusu sağlanmadı (Sağlanan olgu) | SİB/STR sonucu ve suç isnadı üretilmedi; değerlendirme AML Officer'a aittir |
| `AML-A01` | unknown | AML Officer, Compliance ve business owner kararı sağlanmadı (Eksik bilgi) | İnsan kararı alınmadan sınıf ve seçenek kesinleşmez |
| `AML-G01` | fail | Zorunlu kanıt, gelişmiş inceleme ve onaylar tamamlanmadı (Sağlanan olgu, Eksik bilgi) | Hesap açılmaz; onboarding beklemede kalır |
| `AML-M01` | unknown | Periyodik inceleme sahibi ve tetikleyicileri sağlanmadı (Eksik bilgi) | Kabul öncesinde sahip ve tetikleyiciler belgelenmelidir |

## Kanıt boşlukları ve gelişmiş inceleme

- Müşteri/temsilci kimliği: kuruluş, vergi ve imza yetkilisi belgeleri tam olarak
  işaretlenmiştir (Sağlanan olgu).
- Nihai faydalanıcı bütünlüğü: ara ortaklık halkası ve nihai kontrol eksiktir.
  Eksik ortaklık yapısı, pay oranları veya kişi bilgileri üretilmemiştir.
- Sağlanan risk olgusu: `high-risk-geography-supplied`. Bu yalnız bir işarettir;
  ülke, suç, bildirim yükümlülüğü veya sonuç çıkarımı yapılmamıştır.
- Gelişmiş tedbirler: kapsam, derinlik ve tamamlanma durumu sağlanmamıştır;
  kapsamı yalnız yetkili insan süreçleri belirler (Dış yöntem: müşteri tanıma ve
  risk temelli yaklaşım; Şirket politikası: AML-E01).
- Fon kaynağı kanıtı: “ticari gelir” beyanının açıklaması ve destekleyici belgesi
  eksiktir; varsayılan gelir kalemi veya tutar üretilmemiştir.

Bu boşlukların hiçbiri doldurulmamış, eksik olgu üretilmemiştir.

## İnsan kararı ve onboarding kapısı

AML-A01 uyarınca AML Officer, Compliance ve business owner nihai kararı verir.
AML Officer gelişmiş incelemenin kapsamını ve varsa bildirim değerlendirmesini
yönetir; kanıt kapısı istisnası yalnız AML Officer'a yönlendirilir, bu notta
istisna onaylanmamıştır.

AML-G01 koşulları: nihai faydalanıcı zinciri tamamlanmalı, fon kaynağı açıklaması
ve destekleyici kanıt sunulmalı, gelişmiş inceleme tamamlanmalı ve üç insan rolünün
onayı belgelenmelidir. Bunlar tamamlanmadan `open-account` kullanılmaz. Bu beceri
adına hesap açılmamış, ilişki reddedilmemiş, onay verilmemiş ve bildirim
yapılmamıştır; `reject-onboarding` ve `decline-relationship` için gereken
belgelenmiş insan ret kararı sağlanmamıştır.

## Periyodik inceleme

AML-M01 sahibi sağlanmamıştır (Eksik bilgi). Tetikleyiciler ve inceleme tarihleri
de sağlanmamıştır. Kabul kararı verilirse sahip, dönem ve tetikleyiciler yetkili
insanlarca belgelenmelidir; bu notta kişi, tarih veya eşik üretilmemiştir.

## Sınırlar

Bu not hukuki görüş veya nihai hukuki sonuç değildir. Kararın sahibi AML Officer,
Compliance ve business owner'dır. SİB/STR sonucu, bildirim değerlendirmesi veya
suç isnadı üretilmemiştir; sağlanan yüksek risk işareti suç göstergesi olarak
yorumlanmamıştır. Asistan hesap açma, ret, bildirim veya sistem değişikliği dâhil
hiçbir otonom işlem yapmamıştır.
