# Kanıt haritası

## Kilitli başlangıç olguları

| Kanıt | Sağlanan olgu | İlgili kural | Başlangıç durumu |
|---|---|---|---|
| `EV-01` | Risk değerlendirmesi robot değişikliğinden önce | ISG-D01 | `fail` |
| `EV-02` | Robot ve değişen yerleşim eski belgede yok | ISG-D01 | `fail` |
| `EV-03` | Operatör ve bakım katılım kaydı sağlanmadı | ISG-T01 | `unknown` |
| `EV-04` | Çevre koruması ve erişim kontrolü kanıtı sağlanmadı | ISG-H01 | `unknown` |
| `EV-05` | Enerji izolasyonu ve kilitleme/etiketleme doğrulaması sağlanmadı | ISG-H01 | `unknown` |
| `EV-06` | Açık bulgular için sahip, aksiyon ve tarih yok | ISG-O01 | `unknown` |
| `EV-07` | İzleme sahibi ve tetikleri sağlanmadı | ISG-M01 | `unknown` |
| `EV-08` | Planlanan devreye alma talep edildi | ISG-R01 | Kapı incelemesi gerekli |

## Kanıt kullanımı

- `unknown`, kontrolün kesinlikle bulunmadığı anlamına gelmez; sağlanan pakette
  doğrulanamadığı anlamına gelir.
- Entegratör beyanını bağımsız test veya insan kabul kaydı sayma.
- Bir kontrolün adı, tasarım uygunluğu veya etkinlik kanıtı değildir.
- Vaka dışında standart, ölçü, performans, eğitim, kişi veya tarih ekleme.
- Senaryo mutasyonu açıkça bir olguyu değiştiriyorsa yalnız o alanı değiştir;
  diğer başlangıç olgularını koru.

Kilitli başlangıçta değişiklik kapsanmamış, gerekli katılım ve kritik kanıtlar
doğrulanmamıştır. Bu harita mühendislik doğrulaması veya saha kontrol listesi
değildir.
