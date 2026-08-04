# Kurgusal Farma ilaç tanıtım yönetişimi politikası

Sürüm: `NT-TTK-1.0`

Bu belge yalnızca kurgusal Kurgusal Farma İlaç demosu için üretilmiş sentetik şirket
politikasıdır. Mevzuat, hukuki görüş veya tıbbi tavsiye değildir. Copilot ürün,
hedef kitle, iddia, erişim ya da yayın uygunluğuna nihai karar vermez; bütün
karar ve eylemler yetkili insanlardadır.

## İzin verilen karar sınıfları

1. `approve-professional-material`
2. `revise-before-use`
3. `hold-for-product-status`
4. `escalate-medical-legal`
5. `do-not-publish`

## İzin verilen seçenekler

1. `consumer-social`
2. `professional-channel-review`
3. `no-campaign`

## Kurallar

### TTK-P01 - Ürün, statü ve hedef kitle olguları

Ürün adı, ruhsat/statü bilgisi, reçete durumu, hedef kitle ve planlanan ülke ile
kanal sağlanan kaynaktan ayrı ayrı kaydedilir. Eksik veya çelişkili statü
uydurulmaz; gerektiğinde inceleme bekletilir.

### TTK-A01 - Hedef kitle ve kanal sınırı

Materyalin fiilî erişim kitlesi, yalnız briefte yazan niyete göre değil kanalın
erişim biçimine göre değerlendirilir. Tüketiciye açık sosyal yayın ile sağlık
meslek mensuplarına yönelik inceleme aynı seçenek değildir.

### TTK-B01 - İddia kanıtı ve onaylı kapsam

Her ürün, fayda, kullanım ve çağrı iddiası sağlanan onaylı kapsam ve dayanakla
eşleştirilir. Kanıt, endikasyon, karşılaştırma, güvenlilik, kesinlik veya sonuç
uydurulmaz. Kapsam dışı iddia revizyon ya da insan eskalasyonu gerektirir.

### TTK-U01 - Erişim kontrolü

Profesyonel materyal için hedef kitleyi gerçekten sınırlayan ve insan tarafından
doğrulanan erişim kontrolü gerekir. Profil açıklaması, hashtag veya yalnızca
"sağlık profesyonelleri içindir" ibaresi tek başına erişim kontrolü sayılmaz.

### TTK-Y01 - İnsan yetkisi

Medical, Regulatory ve Legal rolleri ürün statüsü, tıbbi kapsam, mevzuat yorumu
ve yayın kapısındaki yetkilerini korur. Copilot onaylayamaz, yayımlayamaz,
hedefleme yapamaz, içeriği kaldıramaz veya kampanyayı durduramaz.

### TTK-R01 - Yayın kapısı

Ürün statüsü, hedef kitle, kanal, iddia kapsamı, erişim kontrolü ve gerekli insan
incelemeleri doğrulanmadan yayın kapısı açık sayılmaz. Kapı sonucu operasyonel
yayın talimatı değildir.

### TTK-M01 - Kanal ve materyal izleme

Onaylanan sürüm, kanal, erişim kuralı, versiyon, insan sahibi, gözden geçirme
tarihi ve düzeltme/kaldırma tetikleri izlenir. Sağlanmayan alanlar `unknown`
kalır; Copilot kanalı izlediğini veya materyali kaldırdığını iddia etmez.

## Seçim ilkeleri

- Reçeteli ürün için tüketiciye açık ürün tanıtımı `consumer-social` seçeneğiyle
  yayın kapısını geçmez.
- Ürün statüsü belirsizse `hold-for-product-status` kullanılır.
- Profesyonel kanal olasılığı ancak hedef kitle, erişim kontrolü, onaylı kapsam
  ve Medical, Regulatory, Legal incelemesiyle değerlendirilir.
- Doğrulanabilir metin düzeltmesi yeterliyse `revise-before-use`; tıbbi veya
  hukuki yorum gerekiyorsa `escalate-medical-legal` kullanılır.
- İstenen kanal ile ürün/erişim sınırı bağdaşmıyorsa `do-not-publish` kullanılır;
  bu sınıf insan yayın kararının yerini almaz.
