# Kanıt haritası

Kanonik vaka: `../../sources/case-brief.md`.

## Temel vaka olguları

| Kanıt kimliği | Alan | Sağlanan olgu | Sınır |
|---|---|---|---|
| `RKB-E01` | İşlem | Anadolu Sistemleri, Nova Veri oy haklarının yüzde 75'ini süresiz devralacak | Taraflar ve oran sentetiktir |
| `RKB-E02` | Kontrol | Brif, kalıcı tek kontrol değişikliğini açıkça sağlıyor | Asistan ek hukuki nitelendirme üretmez |
| `RKB-E03` | Sürüm | `RKB-2608-v3` | Başka sürüm sonucu otomatik taşınmaz |
| `RKB-E04` | Ciro testi | Finans precomputed sonucu `met` | Ciro girdisi veya hukuki filing sonucu değildir |
| `RKB-X01` | Ciro girdileri | Sağlanmadı | Asistan hesaplama yapmaz |
| `RKB-X02` | Teknoloji statüsü | `unknown` | Ürün/şirket adına bakılarak doldurulmaz |
| `RKB-X03` | İnsan görüşü | Rekabet Hukuku Danışmanı görüşü yok | Asistan görüş üretmez |
| `RKB-E05` | Takvim | İmza yakında, gecikmeden kapanış isteniyor | Kapanış yetkisi değildir |
| `RKB-X04` | Kapanış kapısı | Yönlendirme ve kapı kaydı yok | `hold-closing` yönünü destekler |
| `RKB-X05` | İzleme | Sahip ve yeniden inceleme tetikleri yok | Bilinmiyor kalır |

## Temel eşleme

- `RKB-K01`: `RKB-E01`, `RKB-E02`, `RKB-E03`.
- `RKB-C01`: `RKB-E04`, `RKB-X01`.
- `RKB-T01`: `RKB-X02`.
- `RKB-Y01`: `RKB-E04`, `RKB-X03`, `RKB-X04`.
- `RKB-A01`: `RKB-X03`.
- `RKB-R01`: `RKB-E05`, `RKB-X04`.
- `RKB-M01`: `RKB-E03`, `RKB-X05`.

Senaryo mutation alanları bu temel olguları adlandırdığı ölçüde değiştirir.
Değişmeyen alanlar taşınır; null değer bilginin sağlanmadığını gösterir.