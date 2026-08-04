# Kurgusal Ufuk Bankası Uzaktan Müşteri Edinimi Politikası UME-1.0

Bu belge yalnızca demo için üretilmiş sentetik bir şirket politikasıdır. Gerçek
bir banka politikasını, hukuki görüşü veya teknik sertifikayı temsil etmez.
Çıktılar insan kararına hazırlık sağlar; Güvenlik, Uyum ve Hukuk yetkilileri
kararı ve her türlü uygulama eylemini kendileri yürütür.

## Kapsam

UME-1.0, bireysel müşteriler için uzaktan edinim akışlarının pilot ve canlıya
geçiş incelemesini düzenler. Kamu kaynağı yalnızca yöntem soruları sağlar. Bu
sentetik politika karar sınıflarını, kanıt kapılarını ve yetki matrisini belirler.

## Kurallar

| Kural | Sentetik şirket şartı |
|---|---|
| `BDK-I01` | Yöntem envanteri; kanal, adım, görevli rolü, kimlik doğrulama noktası, karar, istisna ve geri dönüş yolu eksiksiz kaydedilir. |
| `BDK-V01` | Etkileşim ve doğrulama kanıtı; şirketin onayladığı canlı veya görüntülü etkileşimin nasıl yürüdüğü, kimlik doğrulama adımları ve başarısızlık davranışı somut kanıtla gösterilir. E-posta ile kimlik taraması ve tek selfie bu kapıyı tek başına geçmez. |
| `BDK-L01` | Canlılık ve süreç bütünlüğü; canlılık kontrolleri, oturum bütünlüğü, tekrar/aktarım savunmaları ve kontrol sonuçları kanıtlanır. Tasarım iddiası kanıt yerine geçmez. |
| `BDK-K01` | Kayıt ve denetim izi; olay zamanı, yöntem sürümü, görevli veya sistem kararı, kanıt referansı, istisna ve sonuç geri çağrılabilir biçimde kaydedilir. |
| `BDK-A01` | Güvenlik, Uyum ve Hukuk birlikte yetkilidir. Bunlardan hiçbiri yerine asistan karar veremez; eksik veya çatışmalı hukuki yorum Uyum ve Hukuk rotasına gider. |
| `BDK-R01` | Canlıya geçiş; `BDK-V01`, `BDK-L01`, `BDK-K01` ve gerekli insan onayları tamamlanmadan uzaktan akış canlıya alınmaz. Uygun değilse manuel edinim yolu korunur. |
| `BDK-M01` | İzleme; dolandırıcılık göstergeleri, kontrol başarısızlıkları, sahip, inceleme sıklığı, eşik ve durdurma/geri dönüş tetikleri sürümlü planda yer alır. Sağlanmayan ayrıntı `bilinmiyor` kalır. |

## Karar sözleşmesi

Tam olarak bir karar sınıfı seçilir:

1. `approve-pilot`: Bütün zorunlu kanıtlar ve insan onayları tamamdır; kapsamı
   sınırlı pilot insan kararıyla ilerleyebilir.
2. `approve-with-controls`: Tasarım yönü kabul edilebilir, ancak listelenen ve
   doğrulanabilir kontroller tamamlanmadan canlıya geçiş yapılamaz.
3. `hold-for-security-evidence`: Güvenlik, canlılık, bütünlük veya kayıt kanıtı
   eksik ya da çatışmalıdır.
4. `escalate-bank-compliance`: Uygulanabilirlik, yorum veya yetki konusu Uyum ve
   Hukuk kararı gerektirir.
5. `reject-flow`: İstenen akış zorunlu kapıları karşılamaz ve mevcut haliyle
   pilot ya da canlı kullanım yolu yoktur.

Tam olarak bir seçenek önerilir:

1. `current-remote-flow`: Sunulan uzaktan akış değişmeden değerlendirilir.
2. `compliant-redesign`: Kanıtlanabilir etkileşim, canlılık, kayıt ve izleme
   kontrolleriyle yeniden tasarım yapılır.
3. `manual-onboarding-fallback`: İnsan kontrollü mevcut manuel müşteri edinimi
   korunur veya geçici ana yol olur.

## Öncelik ve insan sınırı

Canlıya geçiş talebi zorunlu kanıtlar yokken `approve-pilot` sonucu alamaz.
Hukuki yorum gerçekten bilinmiyorsa `escalate-bank-compliance`, teknik kanıt
eksikse `hold-for-security-evidence`, kanıtlanabilir bir düzeltme yolu kabul
edilmeyen mevcut akışta `reject-flow` önceliklidir. Asistan teknik sertifikasyon
iddiasında bulunmaz, müşteri kaydı açmaz, akışı etkinleştirmez ve kontrol
çalıştırmaz.