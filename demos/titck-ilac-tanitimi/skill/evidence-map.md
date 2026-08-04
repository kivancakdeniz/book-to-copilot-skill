# Kanıt haritası

## Kilitli başlangıç olguları

| Kanıt | Sağlanan olgu | İlgili kural | Başlangıç durumu |
|---|---|---|---|
| `EV-01` | Örnek Reçeteli Ürün RX-17 reçeteli beşerî tıbbi ürün olarak sağlandı | TTK-P01 | Sağlanan vaka olgusu |
| `EV-02` | Pazar Türkiye; yayın bugün isteniyor | TTK-P01, TTK-R01 | Kapı incelemesi gerekli |
| `EV-03` | Instagram hesabı ve ücretli hedefleme tüketiciye açık | TTK-A01 | `fail` |
| `EV-04` | Sağlık meslek mensubu rol doğrulaması yok | TTK-U01 | `fail` |
| `EV-05` | Kreatifte ürün adı, fayda ifadesi ve çağrı var | TTK-B01 | Kapsam eşlemesi gerekli |
| `EV-06` | İddianın onaylı kapsamdaki tam yeri sağlanmadı | TTK-B01 | `unknown` |
| `EV-07` | Son Medical, Regulatory, Legal inceleme kaydı sağlanmadı | TTK-Y01, TTK-R01 | `unknown` |
| `EV-08` | İzleme sahibi ve kaldırma tetikleri sağlanmadı | TTK-M01 | `unknown` |

## Kanıt kullanımı

- `unknown`, ürün veya iddianın kesin olarak uygunsuz olduğunu değil, sağlanan
  pakette doğrulanamadığını anlatır.
- Kreatifteki bir cümleyi tıbbi kanıt, endikasyon veya onaylı kapsam sayma.
- Profil etiketi veya hedefleme niyetini rol doğrulamalı erişim kontrolü sayma.
- Vaka dışında ürün özelliği, hasta sonucu, güvenlilik, karşılaştırma, kişi,
  tarih veya mevzuat yorumu ekleme.
- Senaryo mutasyonu bir olguyu değiştiriyorsa yalnız o alanı değiştir; diğer
  başlangıç olgularını koru.

Kilitli başlangıçta reçeteli ürün tüketiciye açık kanalda ürün adı ve fayda
ifadesiyle yayımlanmak istenmektedir. Bu harita tıbbi veya hukuki uygunluk görüşü
değildir.
