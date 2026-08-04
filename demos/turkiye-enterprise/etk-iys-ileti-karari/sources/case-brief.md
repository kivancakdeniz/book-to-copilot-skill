# Sentetik vaka özeti: eski müşterilere indirim SMS'i

Bu vaka MIT lisanslı, tamamen sentetik demo verisidir.

## İş isteği

CRM ekibi 48.000 eski perakende müşterisine indirim SMS'i göndermek istiyor.

## Sağlanan olgular

- Mesaj indirim ve satın alma çağrısı içeriyor; hizmet bildirimi değil,
  promosyon amaçlı.
- Güncel rıza veya IYS durum anlık görüntüsü sağlanmadı.
- Kişi ve kanal düzeyinde kanıt listesi sağlanmadı.
- Mesajda ret/çıkış ifadesi bulunuyor.
- Bir istisna uygulanmasını destekleyen müşteri rolü, işlem veya başka olgu
  sağlanmadı.
- Kampanya bastırma kapısının çalıştığına dair kayıt ve insan onayı sağlanmadı.

## Kilitli başlangıç sonucu

- Karar sınıfı: `do-not-send`
- Seçenek: `suppress-unverified-audience`
- İnsan rotası: CRM Owner + Compliance + Legal

Ret/çıkış ifadesi, eksik ön dayanağı gidermez. Bu sonuç hukuki görüş veya nihai
hukuki sonuç değildir. Resmî hukuk ve rehberlik kamuya açık yöntemdir; sentetik
politika şirket kararını operasyonelleştirir. İnsan Legal/Compliance kararın
sahibidir. Asistan mesaj göndermez, IYS kaydı değiştirmez veya başka bir otonom
eylem yapmaz.