**Önerim: `hold-commissioning`.** Robot, planlanan vardiyada mevcut belgeyle
üretime alınmamalı. Risk değerlendirmesi yeni duruma göre yenilenmeli; yenileme
sonucunda gerekirse `redesign-work-cell` seçeneğine geçilmeli. `commission-now`
sağlanan kanıtla desteklenmiyor.

## 1. Uygun, uygun olmayan ve bilinmeyen konular

**Sağlanan olgulara göre olumlu:** Bir risk değerlendirme belgesi mevcut ve
proje toplantılarına operasyon yöneticisi ile entegratör katılmış. Yani ne
başlangıç noktası ne de teknik muhatap eksik; devreye alma henüz yapılmamış
durumda ve karar önceden inceleniyor.

**Sağlanan olgulara göre yetersiz:** Mevcut değerlendirme robot projesinden önce
hazırlanmış ve yeni robotu, değişen yerleşimi ve insan–robot arayüzünü
incelememiş. Yani hücrenin bugünkü hali için yapılmış bir değerlendirme yok.
Ayrıca çevre koruması, kapı kilidi, erişim algılama ve test sonuçları hakkında
kanıt sağlanmamış; bakım için enerji izolasyonu ve kilitleme/etiketleme
prosedürü ile doğrulama kaydı sağlanmamış; açık bulgular için sahip, aksiyon ve
hedef tarih kaydı yok; olay, ramak kala ve değişiklik sonrası izleme sahibi ile
tetikleri yok. Robot operatörleri ve bakım teknisyenlerinin değerlendirmeye
katıldığına dair kayıt da sağlanmamış.

**Bilinmiyor:** Robotun hızı, erişim alanı ve yükü; insanların hücreye hangi
sıklıkla ve hangi amaçla girdiği; sıkışma ve ezilme noktalarının nerede olduğu;
acil durdurma ve yeniden başlatma mantığı; operatör ve bakım eğitimi; entegratör
teslim dokümanları ve kabul testleri. Bunlar "sağlanmadı" olarak işaretli;
kontrollerin var olmadığı iddia edilmiyor, kanıtları sunulmamış.

**Kendi yorumum (sağlanan olgu değil):** Elle paletlemenin yapıldığı bir hücreye
robot eklenmesi, işin niteliğini değiştiren bir değişikliktir; insanla robotun
aynı alanı paylaştığı durumlarda ezilme ve sıkışma riskleri tipik olarak en
ciddi sonuçlu risklerdir. Bu nedenle, koruma ve enerji izolasyonu kanıtı
görülmeden üretime geçmek, önlenebilir ve ağır sonuçlu bir riski kabul etmek
anlamına gelir. Bu bir mühendislik sertifikasyonu veya uygunluk beyanı değildir.

## 2. Kararı destekleyen sağlanan olgular

- Değerlendirme, değerlendirdiği tesisin bugünkü halini kapsamıyor: robot,
  yerleşim ve insan–robot arayüzü belgede yok.
- Koruma sisteminin (çevre koruması, kapı kilidi, erişim algılama) kurulduğuna ve
  test edildiğine dair kanıt yok.
- Bakım sırasında enerjinin güvenle kesildiğini gösteren prosedür ve doğrulama
  kaydı yok.
- Riske en çok maruz kalacak kişilerin (operatörler ve bakımcılar) görüşü
  alınmamış; bu, sahadaki gerçek çalışma alışkanlıklarının gözden kaçmasına yol
  açar.
- Açık bulguların sahibi ve tarihi yok; yani kapanıp kapanmadığı takip
  edilemiyor.

Talebin gerekçesi vardiya zamanlaması; bu, kanıt eksikliğini karşılayan bir olgu
değil.

## 3. Hâlâ gereken bilgi, kanıt ve insan onayı

- Robotu, yeni yerleşimi ve insan–robot etkileşimini kapsayan güncellenmiş risk
  değerlendirmesi; operatör ve bakım teknisyenlerinin katılım kaydıyla.
- Koruyucu önlemlerin kurulum ve fonksiyon test sonuçları: çevre koruması, kapı
  kilidi, erişim algılama, acil durdurma, güvenli durdurma ve yeniden başlatma
  davranışı.
- Enerji izolasyonu ve kilitleme/etiketleme prosedürü, uygulama noktaları ve
  doğrulama kaydı.
- Entegratör teslim dokümanları, kabul testleri ve kalan riskler listesi.
- Operatör ve bakım eğitimi ile yetkilendirme kaydı.
- İSG uzmanı, işveren vekili/tesis yönetimi ve iş güvenliğinden sorumlu yetkili
  insanların yazılı onayı. Devreye alma kararı proje sponsorunun tek başına
  vereceği bir karar olmamalı.

## 4. Uygulanması gereken koşullar, kayıt ve izleme adımları

- Devreye alma, güncellenmiş değerlendirme ve koruma testleri tamamlanmadan
  açılmayacak tek bir kapıya bağlansın; vardiya baskısı bu kapıyı esnetmesin.
- Bu süre içinde hücrede robot çalıştırılmasın veya yalnızca insan erişimi fiziken
  engellenmiş, üretim dışı test modunda çalıştırılsın.
- Her açık bulgu için sahip, aksiyon ve hedef tarih kaydedilsin; kapanışlar
  doğrulanarak arşivlensin.
- Devreye alma sonrası izleme sahibi ve tetikleri tanımlansın: olay ve ramak kala
  bildirimleri, koruma devreye girme sayısı, manuel müdahale ve durdurma
  sıklığı; belirgin sapmada üretim durdurulsun.
- İlk dönemde artırılmış gözetim ve kısa aralıklı gözden geçirme uygulansın;
  yerleşim, ürün veya çevrim değiştiğinde değerlendirme yeniden açılsın.

Bu bir hukuki veya mühendislik tavsiyesi değildir; karar yetkili insanlarındır.
