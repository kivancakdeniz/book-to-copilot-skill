# Kurgusal AML Kuruluşu kurumsal müşteri kabul politikası

Bu belge sentetik demo politikasıdır. MASAK Tedbirler Yönetmeliği sayfası yöntemi açıklar; Kurgusal AML Kuruluşu adına inceleme sınıfını, onboarding seçeneğini, kanıt kapısını ve yetkiyi yalnız bu politika belirler.

## Kapsam ve sınırlar

- Yalnız vakada sağlanan kimlik, nihai faydalanıcı, risk ve fon kaynağı olgularını kullan.
- Eksik sahiplik halkasını, fon kaynağını, risk gerekçesini veya belgeyi varsayma.
- SİB/STR bildirimi gerekip gerekmediğine karar verme; suç isnadı veya şüpheli kişi/kurum nitelemesi yapma.
- Bu çalışma hukuki görüş değildir. İnsanlar karar verir; beceri hesap açamaz, ilişkiyi reddedemez, bildirim yapamaz veya sistemlerde değişiklik yapamaz.
- Resmi kaynaktan uzun alıntı üretme; yöntemi kısa biçimde özetle ve kaynağa bağla.

## İnceleme sınıfları

Tam olarak bir sınıf seç:

1. `standard-onboarding`: Kimlik ve nihai faydalanıcı bilgileri tamdır; sağlanan risk olguları standart akışı destekler.
2. `enhanced-review`: Sağlanan yüksek risk olgusu ek tedbir ve AML Officer gözetimi gerektirir. Eksik kanıt varsa onboarding seçeneği ayrıca bekletilir.
3. `hold-for-evidence`: Sağlanan yüksek risk tetikleyicisi olmadan zorunlu müşteri, nihai faydalanıcı, risk veya fon kaynağı kanıtı eksik/çelişkilidir.
4. `escalate-aml-officer`: Risk olguları çelişkilidir, istisna istenir veya sınıflandırma insan AML Officer kararı gerektirir.
5. `reject-onboarding`: İnsan AML Officer ve Compliance, giderilemeyen politika engeli nedeniyle ilişkiyi kabul etmemeye karar vermelidir; beceri bu kararı veremez.

## Onboarding seçenekleri

Tam olarak bir seçenek öner:

1. `open-account`: İnsan onayları ve tüm kapılar tamamlandıktan sonra hesap açma akışına geç.
2. `hold-onboarding`: Zorunlu kanıt, gelişmiş inceleme veya insan kararı tamamlanana kadar hesap açma.
3. `decline-relationship`: Yalnız yetkili insanların belgelenmiş ret kararı sonrasında ilişkiyi kurma.

## Zorunlu kurallar

- `AML-C01` Müşteri/nihai faydalanıcı bütünlüğü: Kurumsal kimlik ve nihai faydalanıcı zinciri doğrulanabilir biçimde tam olmalıdır. Eksikse hesap açma yoktur.
- `AML-R01` Risk olguları ve gerekçe: Yalnız sağlanan coğrafya, ürün, kanal ve müşteri olgularını kaydet; risk gerekçesini açıkla, eksik olguyu üretme.
- `AML-E01` Gelişmiş tedbirler: Sağlanan yüksek risk işareti varsa `enhanced-review` seç; gereken ek kanıt ve kontrolleri insan sahibine yönlendir.
- `AML-F01` Fon kaynağı kanıtı: Açıklama ve destekleyici kanıt sağlanmadan onboarding kapısı geçilemez.
- `AML-S01` Bildirim sınırı: SİB/STR sonucu üretme, bildirim kararı verme veya suç isnadı yapma. Gözlemleri yalnız AML Officer'a yönlendir.
- `AML-A01` Yetki: AML Officer, Compliance ve business owner insan kararı verir. Becerinin onay, ret veya bildirim yetkisi yoktur.
- `AML-G01` Onboarding kapısı: Zorunlu kanıtlar, uygulanabilir gelişmiş inceleme ve insan onayları tamamlanmadan hesap açılamaz.
- `AML-M01` Periyodik inceleme: Kabul edilen ilişkide risk, sahiplik ve fon kaynağına ilişkin periyodik insan incelemesinin sahibi ve tetikleyicileri belgelenir.

## Karar önceliği

Sağlanan yüksek risk işareti `enhanced-review` sınıfını belirler; eksik nihai faydalanıcı veya fon kaynağı aynı anda `hold-onboarding` seçeneğini gerektirir. Yüksek risk işareti yokken zorunlu kanıt eksikse `hold-for-evidence` kullan. Çelişki veya istisnayı `escalate-aml-officer` ile yönlendir. SİB/STR kararı verme ve otonom işlem yapma.