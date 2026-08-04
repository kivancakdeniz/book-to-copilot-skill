**Önerim: `compliant-redesign`.** Sunulan kanıtla mevcut akış canlıya alınmamalı; eksikler kapanana kadar `manual-onboarding-fallback` ile devam edilmeli.

## 1. Uygun, uygun olmayan ve bilinmeyen konular

**Sağlanan olgulara göre olumlu:** Akış henüz canlıya alınmamış ve karar önceden
incelemeye sunulmuş. Talep edilen üç adım açıkça tanımlanmış, yani üzerinde
konuşulabilir bir tasarım var.

**Sağlanan olgulara göre yetersiz:** Kanıt tablosundaki sekiz alanın yedisi
"sağlanmadı" durumunda. Canlı veya görüntülü etkileşim yok; canlılık kanıtı yok;
süreç ve oturum bütünlüğü kanıtı yok; kontrol ve denetim günlüğü yok;
dolandırıcılık ve kontrol izleme planı yok; Güvenlik, Uyum ve Hukuk onayı yok.
Yöntem envanteri yalnızca üç adımdan ibaret; kanal, görevli, istisna ve geri
dönüş haritası içermiyor.

**Bilinmiyor:** E-posta kanalının nasıl korunduğu, belgelerin nerede ve ne kadar
saklandığı, kimlik belgesinin sahtecilik açısından incelenip incelenmediği,
selfie ile belge fotoğrafının karşılaştırılıp karşılaştırılmadığı, kararı kimin
verdiği, ret ve itiraz akışının ne olduğu. Bunların hiçbiri "yok" diye
belirtilmiş değil, "sağlanmadı" diye işaretli; yani kanıt yokluğu söz konusu.
Kanıt yokluğu kontrolün olmadığını kesin olarak göstermez, ama canlıya geçiş
kararı için kanıtın yerine de geçmez.

**Kendi yorumum (sağlanan olgu değil):** Uzaktan müşteri edinimi yüksek riskli
bir süreçtir; e-posta ile gönderilen tek bir tarama ve tek bir selfie, kimlik
hırsızlığı, sahte hesap açma ve deepfake/fotoğraf tekrar kullanımı senaryolarına
karşı bilinen zayıflıklar taşır. Bankacılıkta uzaktan kimlik tespitine dair
düzenleyici beklentiler ülkeye ve kuruma göre değişir; hangi somut kuralın hangi
şekilde uygulandığını buradaki bilgilerle söyleyemem. Bu değerlendirme Hukuk ve
Uyum'a aittir.

## 2. Kararı destekleyen sağlanan olgular

Karar tek bir eksikliğe değil, sistematik kanıt boşluğuna dayanıyor:

- Akışta kimlik sahibinin o anda ve gerçekten orada olduğunu gösteren hiçbir
  unsur sunulmamış (canlı etkileşim ve canlılık kanıtı yok).
- Sürecin sonradan denetlenebilirliğini sağlayacak günlük ve bütünlük kanıtı
  sunulmamış; yani bir uyuşmazlıkta "ne oldu" sorusu cevaplanamaz.
- Operasyon ekibinin rolü "dosyaların ulaştığını görmek" olarak tarif edilmiş;
  belgeyi doğrulayan bir kontrol adımı tanımlanmamış.
- Güvenlik, Uyum ve Hukuk onayı alınmamış; dolayısıyla yetkili bir insan kararı
  henüz oluşmamış.

## 3. Hâlâ gereken bilgi, kanıt ve insan onayı

- Uçtan uca yöntem tanımı: kanallar, görevliler, istisnalar, başarısızlık ve geri
  dönüş senaryoları.
- Kimlik doğrulama kanıtı: belge doğrulama yöntemi, yüz eşleştirme, canlılık
  testi, tekrar saldırılarına karşı kontroller ve bunların test sonuçları.
- Oturum ve süreç bütünlüğü kanıtı: kaydın kim tarafından, ne zaman, hangi
  sistemde üretildiğini gösteren izler.
- Denetim günlükleri ve saklama/silme kuralları; kişisel veri işlemenin hukuki
  dayanağı ve bilgilendirme metinleri.
- Dolandırıcılık izleme planı: hangi metrik, hangi eşik, kim izliyor, alarm
  durumunda ne oluyor.
- İnsan onayları: Güvenlik, Uyum ve Hukuk'un yazılı onayı. Bu vakada asıl karar
  merci onlardır; ben yalnız kanıt boşluklarını gösterebilirim.

## 4. Uygulanması gereken koşullar, kayıt ve izleme adımları

- Canlıya geçiş, yukarıdaki kanıtların tamamlanmasına ve üç fonksiyonun yazılı
  onayına bağlı bir kapı olarak tanımlansın; kısmi onayla açılmasın.
- Yeni tasarım önce sınırlı bir pilot ile, düşük hacimde ve manuel ikinci göz
  kontrolüyle çalıştırılsın.
- Her başvuru için karar gerekçesi, kullanılan kanıtlar ve karar veren kişi/kural
  kaydedilsin; kayıtlar değiştirilemez biçimde tutulsun.
- Reddedilen ve manuel incelemeye düşen başvuru oranları, sahtecilik şüphesi
  vakaları ve sonradan tespit edilen sahte hesaplar düzenli izlensin; belirgin
  sapmada akış durdurulsun.
- Geçiş döneminde manuel edinim kullanılırken, mevcut e-posta akışıyla toplanan
  belgelerin saklama ve erişim koşulları da gözden geçirilsin.

Bu bir hukuki görüş veya nihai uygunluk değerlendirmesi değildir. Herhangi bir
sistemi veya müşteri sürecini değiştirmedim; karar yetkili insanlarındır.
