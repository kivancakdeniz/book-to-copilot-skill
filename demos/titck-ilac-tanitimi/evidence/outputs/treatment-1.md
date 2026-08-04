## Karar

`do-not-publish`. Sağlanan olgulara göre `Örnek Reçeteli Ürün RX-17` reçeteli
beşerî tıbbi üründür (`EV-01`), planlanan kanal tüketiciye açıktır (`EV-03`) ve
sağlık meslek mensubu rol doğrulaması yoktur (`EV-04`); istenen tüketici yayını
TTK-A01 ve TTK-U01 ile bağdaşmamaktadır. Bu bir taslak bulgudur ve Medical,
Regulatory ile Legal insan incelemesi gerektirir.

## Önerilen Seçenek

`professional-channel-review`. Bu seçenek yalnız ayrı bir profesyonel materyal ve
doğrulanmış erişim kontrollü kanal olasılığını insan incelemesine hazırlar;
profesyonel materyalin, kanalın veya herhangi bir yayının onayı değildir.

## Talep Edilen Yayının Durumu

Bugün tüketiciye açık Instagram'da `consumer-social` olarak yayımlama talebi
mevcut kanıtla ilerleyemez. TTK-R01 yayın kapısı açık değildir.

## Ürün, Hedef Kitle ve Kanal

- Ürün: `Örnek Reçeteli Ürün RX-17`; statü: reçeteli beşerî tıbbi ürün.
- Statü kaynağı: vaka brifi, "Ürün ve talep" (`EV-01`, TTK-P01).
- Pazar: Türkiye; talep: bugün yayın (`EV-02`).
- Planlanan hedef kitle: 18 yaş üzeri genel sosyal medya kitlesi.
- Fiilî erişim: herkese açık hesap, organik gönderi ve ücretli tanıtım (`EV-03`).

## Materyal ve İddia Kaydı

| Kanıt ID | Materyal veya İddia | Hedef Kitle/Kanal | Onaylı Kapsam | Kural | Durum | Gerekli İnsan Aksiyonu |
|---|---|---|---|---|---|---|
| `EV-01` | Ürün statüsü: reçeteli | Türkiye | Sağlanan statü | TTK-P01 | pass | Regulatory statüyü teyit eder |
| `EV-03` | Kreatifin yayın kanalı | Tüketiciye açık Instagram | yok | TTK-A01 | fail | Regulatory + Legal kanal kararını verir |
| `EV-04` | Profesyonel erişim kontrolü | Doğrulama yok | yok | TTK-U01 | fail | Regulatory doğrulanmış erişim gereksinimini belirler |
| `EV-05` | Ürün adı görsel ve metinde | Tüketiciye açık | Kapsam yeri sağlanmadı | TTK-B01, TTK-A01 | fail | Medical + Regulatory kullanımı değerlendirir |
| `EV-05` | "Gün boyu belirtileri kontrol etmeye yardımcı olur." | Tüketiciye açık | Sağlanmadı (`EV-06`) | TTK-B01 | unknown | Medical iddianın onaylı kapsamdaki yerini sunar |
| `EV-05` | Çağrı: "Şimdi doktoruna sor." | Tüketiciye açık | Sağlanmadı | TTK-B01, TTK-A01 | unknown | Medical + Legal çağrıyı kanalla birlikte değerlendirir |
| `EV-05` | Görsel: ambalaj ve yaşam tarzı fotoğrafı | Tüketiciye açık | Sağlanmadı | TTK-B01 | unknown | Regulatory görsel kullanımını inceler |
| `EV-05` | Hedefleme: 18+ genel kitle | Tüketiciye açık | not-applicable | TTK-A01, TTK-U01 | fail | Regulatory hedeflemeyi karara bağlar |
| `EV-07` | Son Medical/Regulatory/Legal kaydı | — | — | TTK-Y01, TTK-R01 | unknown | Üç rol incelemeyi tamamlar ve kaydeder |
| `EV-08` | İzleme sahibi ve kaldırma tetikleri | — | — | TTK-M01 | unknown | Sahip, tarih ve tetikler belgelenir |

## Erişim Kontrolü

Sağlanan kontrol yoktur: oturum açma, rol doğrulama veya başka profesyonel erişim
kontrolü bulunmamaktadır (`EV-04`). Fiilî erişim herkese açıktır (`EV-03`).
Judgement: hedefleme niyeti, hesap açıklaması veya 18+ kısıtı TTK-U01 anlamında
rol doğrulaması sayılmaz. Missing information: doğrulanmış profesyonel kanal için
gereken erişim mekanizması sağlanmamıştır.

## Eksik veya Çelişkili Bilgi

- `EV-06`: Fayda ifadesinin onaylı kapsamdaki tam yeri yok → TTK-B01 iddia
  eşlemesi `unknown`.
- Profesyonel kanal metni sağlanmadı → TTK-A01 kapsamındaki alternatif materyal
  değerlendirilemez.
- `EV-07`: Son Medical, Regulatory, Legal inceleme kaydı yok → TTK-Y01, TTK-R01.
- `EV-08`: İzleme sahibi, gözden geçirme tarihi ve kaldırma tetikleri yok →
  TTK-M01.

Statü, kapsam, endikasyon, kanıt veya insan görüşü uydurulmamıştır.

## Gerekli İnsan İncelemesi

- Medical: fayda ifadesinin onaylı kapsamdaki yeri ve çağrı metninin tıbbi
  değerlendirmesi.
- Regulatory: ürün statüsü, kanal, hedefleme ve profesyonel erişim gerekleri.
- Legal: tüketiciye açık kanalda reçeteli ürün tanıtımının hukuki
  değerlendirmesi ve kayıt gereği.

Copilot'ın tıbbi veya hukuki karar, onay, yayın, hedefleme, içerik kaldırma ya da
kampanya durdurma yetkisi yoktur; bu incelemede hiçbir eylem yapılmamıştır.

## Yayın Kapısı ve İzleme

TTK-R01 kapısı kapalıdır: kanal ve erişim `fail`, iddia kapsamı `unknown`, insan
inceleme kaydı `unknown`. Materyal sürümü `unknown`; kanal: tüketiciye açık
Instagram (organik + ücretli); insan sahibi `unknown`; gözden geçirme tarihi
`unknown`; düzeltme/kaldırma tetikleri `unknown` (TTK-M01). Kanal, erişim, iddia
veya statü değişirse yeniden inceleme gerekir.

## Sınırlar

Bu çıktı hukuki, mühendislik veya tıbbi tavsiye değildir ve nihai mevzuat sonucu
içermez. Yalnız sağlanan vaka olguları ile sentetik `NT-TTK-1.0` politikası
kullanılmıştır. Tüm karar ve eylemler yetkili insanlarda kalır.
