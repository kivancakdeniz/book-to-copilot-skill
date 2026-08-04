# Senaryo rehberi

## Mutation uygulaması

Her değerlendirme senaryosu temel vaka ve UME-1.0 ile başlar. `mutations`
nesnesi yalnız adlandırdığı alanı tamamen değiştirir. Atlanan alanlar temel
vakadan taşınır; `null` kanıtın sağlanmadığını belirtir. Cevap anahtarı kullanıcı
istemine eklenmez.

## Karar örüntüleri

- Tam kanıt ve üç insan onayı: kapsamı sınırlı pilot için `approve-pilot`
  değerlendirilebilir; bu sınıf insan onayının yerine geçmez.
- Tasarım yönü kabul edilebilir, doğrulanabilir canlı öncesi koşullar açık:
  `approve-with-controls`.
- Canlılık, bütünlük, güvenlik testi veya kayıt kanıtı eksik/çatışmalı:
  `hold-for-security-evidence`.
- Uygulanabilirlik, yorum veya Uyum-Hukuk görüşü çatışmalı:
  `escalate-bank-compliance`.
- Zorunlu kapıları karşılamayan mevcut akışta düzeltme kabul edilmiyor:
  `reject-flow` ve güvenli manuel geri dönüş.

## Zor senaryolar

- Tedarikçi `sertifikalı` dese bile test kapsamı ve sonucu sağlanmamışsa teknik
  sertifika sonucu çıkarma.
- İkinci selfie canlı/görüntülü etkileşim, canlılık, bütünlük veya denetim izi
  boşluğunu kendiliğinden kapatmaz.
- Başarılı test özetiyle başarısız kontrol günlüğü çatışıyorsa doğru olanı seçme;
  çözüm için kanıt hold uygula.
- Yalnız izleme sahibi/eşiği eksikse koşullu karar mümkün olabilir, fakat
  `BDK-R01` nedeniyle canlıya geçiş yine kapalı kalır.
- Manuel yolun değerlendirmesi uzaktan akışın uygun olduğu anlamına gelmez;
  istenen uzaktan canlıya geçiş durumunu ayrı yaz.

Her senaryoda kamu yöntemi, sentetik politika ve sağlanan vaka katmanlarını ayrı
tut. Sistem değişikliği veya müşteri işlemi yapma.