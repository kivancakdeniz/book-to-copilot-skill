**Önerim: `consent-first-redesign`.** Kampanya 2026-09-01'de mevcut haliyle
başlatılmamalı. Bu tarihte bir şey yayınlanması şartsa, yalnızca bireye
bağlanmayan `aggregate-only` planlama seçeneği ayrıca doğrulanarak
değerlendirilebilir.

## 1. Uygun, uygun olmayan ve bilinmeyen konular

**Sağlanan olgulara göre olumlu:** Kampanya henüz başlamamış, yani karar geri
dönülemez hale gelmeden inceleniyor. CRM'de rol tabanlı erişim olduğu
belirtilmiş. Hangi veri kategorilerinin (konum, trafik) hangi amaçla kullanılmak
istendiği net biçimde tarif edilmiş.

**Sağlanan olgulara göre yetersiz:** Rıza kaydı, rıza metni ve sürümü, kapsamı,
zamanı ve geri alma durumu sağlanmamış. Kampanya amacı ile veri kategorileri
arasında belgelenmiş bir amaç eşlemesi yok ve dayanılan hukuki rota olgusu
sunulmamış. Saklama süresi ve silme tetikleri yok. Privacy Counsel, Telecom
Compliance ve DPO onayı yok; ortak inceleme kaydı yok.

**Bilinmiyor:** Rol tabanlı erişimin ayrıntısı (kim hangi alanı görüyor),
aktarım kontrolleri, anonimleştirme veya toplulaştırma yöntemi, verinin
üçüncü taraflarla paylaşılıp paylaşılmadığı, abonelere yapılan bilgilendirmenin
içeriği, teklif gösteriminin hangi kanaldan yapılacağı. Bunlar "sağlanmadı"
olarak işaretli; yani kanıtın kendisi eksik, kontrolün var olmadığı iddia
edilmiyor.

**Kendi yorumum (sağlanan olgu değil):** Hücre bölgesinden türetilen konum ve
zaman/hacim içeren trafik verisi, tipik olarak abone başına davranış profili
üretebilen ve hassasiyeti yüksek kabul edilen veri türleridir. Bu tür verinin
pazarlama amacıyla bireysel hedeflemede kullanılması, çoğu hukuk düzeninde
haberleşmeye özgü ek koruma ve genel veri koruma kuralları olmak üzere iki ayrı
katmanla değerlendirilir. Hangi kuralın burada nasıl uygulanacağını söyleyemem;
vaka sınırında da belirtildiği gibi bu, Privacy Counsel, Telecom Compliance ve
DPO'nun birlikte vereceği bir karardır.

## 2. Kararı destekleyen sağlanan olgular

- Kampanya bireysel hedefleme yapıyor: konum ve trafik verisi, "hangi aboneye
  hangi teklif" sorusunu cevaplamak için birlikte kullanılıyor. Yani veri, abone
  düzeyinde ve profil üretecek şekilde işleniyor.
- Bu işlemeyi taşıyacak doğrulanabilir bir rıza kaydı sunulmamış; rızanın var
  olup olmadığı, kapsamının bu amacı içerip içermediği ve geri alınıp
  alınmadığı bilinmiyor.
- Amaç–veri eşlemesi belgelenmemiş; yani hangi verinin neden gerekli olduğu
  gösterilmemiş.
- Saklama ve silme kuralı yok; veri süresiz kalabilir.
- Üç yetkili fonksiyonun hiçbirinin onayı alınmamış.

Bu beş nokta birlikte, kampanyayı başlatmayı destekleyecek bir kanıt tabanı
oluşturmuyor.

## 3. Hâlâ gereken bilgi, kanıt ve insan onayı

- Abone bazında doğrulanabilir rıza kaydı: metin ve sürüm, kapsam, alınma zamanı
  ve kanalı, geri alma durumu ve geri almanın CRM'e ne kadar sürede yansıdığı.
- Kampanya amacının hangi veri alanlarını gerektirdiğini gösteren amaç eşlemesi
  ve veri minimizasyonu gerekçesi.
- Saklama süreleri, silme tetikleri ve bunların teknik olarak uygulandığının
  kanıtı.
- Ayrıntılı erişim matrisi, aktarım kontrolleri, günlükleme ve varsa
  anonimleştirme/toplulaştırma yönteminin doğrulanması.
- Abonelere yapılan bilgilendirmenin metni ve zamanı.
- Privacy Counsel, Telecom Compliance ve DPO'nun yazılı ve ortak incelemesi;
  hukuki rotanın hangi dayanağa oturduğuna dair kararlarını ben veremem.

## 4. Uygulanması gereken koşullar, kayıt ve izleme adımları

- Başlatma, rıza kaydı ve üç onayın tamamlanmasına bağlı tek bir kapı olarak
  tanımlansın; tarih baskısı bu kapıyı esnetmesin.
- Rızası doğrulanamayan aboneler hedeflemeden otomatik olarak dışlansın ve bu
  dışlamanın çalıştığı test edilerek kayıt altına alınsın.
- Geri alma (opt-out) talepleri tanımlı ve kısa bir süre içinde tüm hedefleme
  katmanlarına yansısın; senkronizasyon gecikmesi ölçülsün.
- Her teklif gösterimi için hangi veriye ve hangi rıza kaydına dayanıldığı
  izlenebilir biçimde loglansın.
- Şikâyet, opt-out oranı ve erişim günlükleri düzenli izlensin; anormal artışta
  kampanya durdurulsun.
- `aggregate-only` seçilirse, çıktının gerçekten bireye bağlanamaz olduğu bağımsız
  şekilde doğrulansın; küçük bölgelerde yeniden kimliklendirme riski ayrıca
  değerlendirilsin.

Bu bir hukuki görüş veya nihai KVKK sonucu değildir; karar yetkili insanlarındır.
