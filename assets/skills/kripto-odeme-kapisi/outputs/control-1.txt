## Öneri

Planlanan 2026-09-15 tarihinde `launch-current-flow` uygulanmamalıdır. Sağlanan
olgularla desteklenebilecek karar, USDT seçeneğinin satıcı ödeme sayfasından
şimdilik çıkarılması (`remove-crypto-checkout`) ya da en azından yetkili insan
onayları tamamlanana kadar lansmanın durdurulmasıdır.

## Kararı destekleyen sağlanan olgular

- USDT, satıcı alımını doğrudan kapatan değer olarak kullanılıyor. Yani akış bir
  bilgi veya analiz hizmeti değil, gerçek bir ödeme akışıdır.
- Ödeme talimatı, dönüşüm ve mutabakat adımları bir ödeme hizmeti aracısının
  akışı içinde yer alıyor; tasarım ve sorumluluk tek başına ürün ekibinin
  kontrolünde değil.
- Payments Counsel, Compliance ve Product tarafından verilmiş bir lansman onayı
  yok. Bu tek başına, sabit bir tarihe kilitlenmiş canlıya alma kararını
  engellemek için yeterlidir.
- Akış ve sürüm izleme sahibi, inceleme tarihi ve değişiklik tetikleri
  belirlenmemiş. Yayına alınsa bile akışın yayın sonrası sahibi yok.

## Uygun, uygun olmayan ve bilinmeyen konular

Uygun görünen: satıcıya mutabakatın TRY olarak yapılması ve akışın sürümlenmiş
olması (`checkout-v3`), incelenebilir bir temel sağlıyor.

Uygun görünmeyen: onayı ve sahibi olmayan bir ödeme akışının sabit bir lansman
tarihine bağlanması; kripto varlığın alım bedelini kapatan ödeme aracı olarak
konumlandırılması.

Bilinmeyen: aracının hukuki niteliği, lisans durumu ve sözleşmesel
yükümlülükleri; dönüşümün kim nezdinde, hangi kurla ve hangi anda yapıldığı; kur
ve zamanlama riskini kimin taşıdığı; iade, itiraz ve ters ibraz akışının nasıl
işlediği; müşteriye gösterilecek bilgilendirme ve ücret metinleri; mevcut satıcı
sözleşmelerinin bu ürünü kapsayıp kapsamadığı; müşteri tanıma ve fon kaynağı
kontrollerinin bu akışta nasıl uygulandığı; vergi ve muhasebe ele alınışı.

Yorum (sağlanan olgu değildir): genel bilgime göre Türkiye'de kripto varlıkların
ödemelerde kullanılmasına ilişkin kısıtlayıcı bir düzenleme bulunduğu
bilinmektedir. Bu düzenlemenin güncel metni bana sağlanmadı ve burada
doğrulayamıyorum; bu nedenle hukuki bir sonuç yazmıyorum. Ancak bu, kararın
mutlaka hukuk danışmanına götürülmesi için ek bir nedendir.

## Hâlâ gereken bilgi, kanıt ve insan onayı

- Payments Counsel'ın yazılı değerlendirmesi ve Compliance'ın yazılı onayı.
- Aracıyla yapılan sözleşmenin ilgili maddeleri, aracının bu akıştaki rolünü ve
  yetkisini gösteren belgeler.
- Uçtan uca akışın adım adım tanımı: müşterinin USDT gönderdiği an, dönüşümün
  yapıldığı an, satıcı alacağının doğduğu an.
- Risk, hazine ve operasyon ekiplerinin kur riski ve mutabakat kesintileri
  hakkındaki değerlendirmesi.
- Müşteri deneyimi metinleri ve satıcı bilgilendirme materyalinin onaylı hâli.
- Ürünün hangi satıcı segmentine ve hangi hacimle açılacağına dair karar.

## Koşullar, kayıt ve izleme adımları

- Onaylar tamamlanana kadar özellik bayrağı kapalı kalmalı; bu kararı ve
  gerekçesini tarih ve karar sahibiyle birlikte kayda geçirin.
- Akış için tek bir sahip atayın; `checkout-v3` sürümünü, akış diyagramını ve
  ürün özetini aynı sürüm numarasıyla eşleyin.
- Hangi olgunun değişmesi hâlinde kararın yeniden inceleneceğini önceden yazın
  (aracı değişimi, dönüşüm adımının yeri, satıcı mutabakat para birimi,
  düzenleyici gelişme).
- Bir inceleme tarihi belirleyin ve bu tarihte kararın hâlâ geçerli olup
  olmadığını yetkili insanlara sorun.
- Lansman gerçekleşirse: işlem, dönüşüm ve iade kayıtlarının izlenebilir
  tutulması, hata ve şikâyet eşiğinde durdurma yetkisinin kimde olduğunun
  önceden belirlenmesi.

`redesign-nonpayment-service` seçeneği ancak yeni işlevin satıcı alımını
kapatmadığı somut olarak gösterilirse anlamlıdır; bu, mevcut brifle
değerlendirilemez ve ayrı bir insan incelemesi gerektirir.

Bu değerlendirme hukuki görüş değildir ve nihai hukuki sonuç içermez; karar
Payments Counsel, Compliance ve Product'ın yetkisindedir.
