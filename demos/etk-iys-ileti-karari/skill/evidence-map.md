# Kanıt haritası

## Başlangıç vakası

| Kanıt | Sağlanan olgu | İlgili kurallar | Başlangıç etkisi |
|---|---|---|---|
| `ETK-F01` | 48.000 eski perakende müşterisi hedefleniyor. | `ETK-I01` | Kişi ve kanal kanıtı gerekir. |
| `ETK-F02` | SMS indirim ve satın alma çağrısı içeriyor. | `ETK-C01` | İleti promosyon olarak incelenir. |
| `ETK-F03` | Güncel rıza/IYS anlık görüntüsü sağlanmadı. | `ETK-I01` | Kitle doğrulanmış sayılamaz. |
| `ETK-F04` | Mesajda ret/çıkış ifadesi var. | `ETK-O01` | Sonraki ret olanağı eksik ön kanıtı gidermez. |
| `ETK-F05` | İstisnayı destekleyen olgu yok. | `ETK-X01` | İstisna varsayılmaz. |
| `ETK-F06` | Bastırma kaydı ve insan onayı yok. | `ETK-A01`, `ETK-R01` | Gönderim kapısı kapalı kalır. |

Yalnız bu olgular kullanılabilir. Sağlanmayan rıza, IYS durumu, ilişki, istisna,
onay veya hukuki sonuç bilinmiyor olarak işaretlenir.