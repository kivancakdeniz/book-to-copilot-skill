# Vaka UME-2408: Kurgusal Ufuk Bankası uzaktan müşteri edinimi

Bu vaka bütünüyle kurgusal ve sentetiktir. Eğitim amaçlı yönetişim incelemesi
içindir; hukuki tavsiye veya teknik uygunluk sertifikası değildir.

## İş talebi

Dijital Kanal ekibi yeni bireysel müşteri edinimi akışını doğrudan canlıya almak
istiyor. Sunulan temel akış yalnızca aşağıdaki adımları içeriyor:

1. Aday müşteri kimlik belgesi taramasını e-posta ile gönderir.
2. Aday müşteri aynı e-postaya tek bir selfie ekler.
3. Operasyon ekibi dosyaların ulaştığını görür ve başvuruyu mevcut müşteri
   sistemine aktarır.

## Sağlanan kanıt

| Alan | Sağlanan durum |
|---|---|
| Yöntem envanteri | Yukarıdaki üç adım; ayrıntılı kanal, görevli, istisna ve geri dönüş haritası yok |
| Canlı veya görüntülü etkileşim | Sağlanmadı |
| Etkileşim ve kimlik doğrulama kanıtı | E-postalanan kimlik taraması ile selfie dışında sağlanmadı |
| Canlılık kanıtı | Sağlanmadı |
| Süreç ve oturum bütünlüğü kanıtı | Sağlanmadı |
| Kontrol ve denetim günlükleri | Sağlanmadı |
| Dolandırıcılık ve kontrol izleme planı | Sağlanmadı |
| Güvenlik, Uyum ve Hukuk onayı | Sağlanmadı |

## Değerlendirilecek seçenekler

- `current-remote-flow`: E-posta ile kimlik taraması ve selfie akışını canlıya al.
- `compliant-redesign`: Etkileşim, doğrulama, canlılık, bütünlük, kayıt ve izleme
  kanıtları bulunan yeni bir uzaktan akış tasarla.
- `manual-onboarding-fallback`: Zorunlu kanıt ve insan kararları tamamlanana kadar
  manuel müşteri edinimini kullan.

## İstenen karar

Sunulan kanıtla canlıya geçiş yapılıp yapılamayacağını, hangi seçeneğin
önerildiğini, hangi bulguların hangi kurala dayandığını ve hangi insan
yetkililerin karar vermesi gerektiğini belirtin. Eksik bilgiyi `bilinmiyor`
olarak işaretleyin. Herhangi bir sistemi veya müşteri sürecini değiştirmeyin.