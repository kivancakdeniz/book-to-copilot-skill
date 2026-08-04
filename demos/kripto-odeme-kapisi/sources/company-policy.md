# Kurgusal Ödeme Kripto Ürün Sınırı Politikası KRP-1.0

> Bu dosya, `kripto-odeme-kapisi` demosu için kurgusal ve sentetik şirket
> politikasıdır. Hukuki tavsiye veya mevzuat metni değildir.

## Kapsam ve kurallar

- **KRP-A01 - Varlık ve işlev olguları.** İncelenen akışta kripto varlığın
  türünü, kimin hesabında tutulduğunu, hangi işlevi gördüğünü, dönüşüm adımını,
  ödeyeni, satıcıyı ve mutabakat birimini yalnız sağlanan olgularla kaydet.
- **KRP-O01 - Ödemede kullanım sınırı.** Sentetik politika kapsamında kripto
  varlık bir satıcı alımını doğrudan kapatmak için kullanılıyorsa mevcut akışın
  lansmanı geçemez. Daha dar bir seçenek yalnız sağlanan seçeneklerden seçilir.
- **KRP-I01 - Aracı ve hizmet akışı.** Talimat, cüzdan, dönüşüm, transfer,
  satıcı mutabakatı ve ödeme hizmeti aracısı dahil her aktörü ve adımı eşle.
  Aracının akışta bulunmasını önemsiz veya varsayımsal sayma.
- **KRP-X01 - Eksik olgu disiplini.** Sağlanmayan cüzdan, saklama, dönüşüm,
  mutabakat, sözleşme veya taraf rolü `unknown` kalır. Eksik belirleyici olgu
  varsa akışı kanıt için beklet; varsayım üretme.
- **KRP-Y01 - İnsan yetkisi.** Payments Counsel, Compliance ve Product birlikte
  ürün sınırını ve lansman kararını verir. Copilot yalnız danışman analiz
  hazırlar; hukuki karar, onay veya uygulama yetkisi yoktur.
- **KRP-R01 - Lansman kapısı.** Akış kanıtı, seçilen ürün sınırı, sürüm ve gerekli
  insan onayları kayda geçmeden lansman yapılamaz. Copilot lansman başlatamaz,
  durduramaz, ödeme işleyemez veya ürün ayarı değiştiremez.
- **KRP-M01 - Akış ve sürüm izleme.** İnsan sahibi, akış sürümü, inceleme tarihi
  ve cüzdan, aracı, dönüşüm ya da mutabakat değişikliği tetikleri kaydedilir.
  Sağlanmayan izleme ayrıntıları `unknown` kalır.

## Karar sınıfları

Tam olarak bir sınıf kullan:

- `approve-nonpayment-service`: sağlanan olgular işlevin satıcı alımını kapatan
  bir ödeme akışı olmadığını ve gerekli insan kapısının tamamlandığını gösterir.
- `revise-product-boundary`: mevcut istek geçemez, ancak sağlanan daha dar ürün
  sınırı doğrulanabilir bir revizyon sunar.
- `hold-for-flow-evidence`: belirleyici akış olguları eksik veya çelişkilidir.
- `escalate-payments-counsel`: ürün sınırı, taraf rolü veya kapsam dışı hukuki
  soru Payments Counsel kararı gerektirir.
- `reject-payment-flow`: sağlanan akış kripto varlığı satıcı alımını doğrudan
  kapatmak için kullanır ve mevcut ödeme akışı reddedilmelidir.

## Ürün seçenekleri

Tam olarak bir seçenek kullan:

- `launch-current-flow`: yalnız mevcut akış sentetik politika kapılarını
  sağlıyorsa değerlendirilebilir.
- `remove-crypto-checkout`: satıcı ödeme adımından kripto seçeneğini çıkarır.
- `redesign-nonpayment-service`: ürünü satıcı alımını kapatmayan, ayrı ve
  kanıtlanabilir bir ödeme dışı işleve dönüştürür.

Bu politika yatırım veya transfer faaliyetlerinin hukuka uygunluğu hakkında,
sağlanan ödeme akışının ötesinde görüş üretmez. Nihai kararlar ve tüm eylemler
adı geçen insan rollerine aittir.