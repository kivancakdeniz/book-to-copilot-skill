## Karar

- Karar sınıfı: `legal-notification-review`
- Önerilen seçenek: `hold-closing`
- İstenen kapanış: `insan danışman yönlendirmesi gerekli`
- Kısa gerekçe: Finans'ın precomputed ciro sonucu `met` olarak sağlanmıştır
  [RKB-2608; Sağlanan olgular, Finans ciro testi] ve bu gösterge `RKB-Y01`
  uyarınca insan danışman rotasını zorunlu kılar [BKP-1.0, Kurallar]. Rekabet
  Hukuku Danışmanı görüşü, kapanış yönlendirmesi ve teknoloji teşebbüsü durumu
  sağlanmadığından kapanış kapısı açılamaz. Bu taslak danışma niteliğindedir;
  bildirim gerekip gerekmediğine dair hukuki sonuç üretilmemiştir.

## İşlem ve kontrol olguları

| Olgu | Sağlanan değer | Kaynak/sürüm | Eksik veya çatışma | Durum |
|---|---|---|---|---|
| İşlem yapısı | Oy haklarının %75'i süresiz devralınıyor | `RKB-E01`; `RKB-2608-v3` | yok | pass |
| Kontrol değişikliği | Brif kalıcı tek kontrol değişikliğini açıkça sağlıyor | `RKB-E02`; `RKB-2608-v3` | Ek hukuki nitelendirme üretilmedi | pass |
| İşlem sürümü | `RKB-2608-v3` | `RKB-E03` | yok | pass |
| Ciro testi sonucu | Finans precomputed `met` | `RKB-E04`; `RKB-2608-v3` | Kapsam beyanı sınırlı | pass |
| Ciro girdileri | Sağlanmadı | `RKB-X01` | Girdi yok | not-applicable |
| Teknoloji teşebbüsü | `unknown` | `RKB-X02` | Çözülmedi | unknown |
| Danışman görüşü | Sağlanmadı | `RKB-X03` | Eksik bilgi | unknown |
| Takvim | İmza yakında, gecikmesiz kapanış isteniyor | `RKB-E05` | Kapanış yetkisi değil | fail |
| Kapanış kapısı | Yönlendirme ve kapı kaydı yok | `RKB-X04` | Eksik bilgi | fail |
| İzleme | Sahip ve tetikler yok | `RKB-X05` | Eksik bilgi | unknown |

## Gösterge ve kanıt kapıları

| Kural | Sağlanan sonuç/olgu | Yapılmayan hesaplama veya çıkarım | Bulgu | Kaynak |
|---|---|---|---|---|
| `RKB-C01` | Precomputed `met` | Ciro toplanmadı, dönüştürülmedi, eşik uygulanmadı, yeniden hesaplanmadı | Sonuç yalnız inceleme göstergesi; bildirim kararı değil | [RKB-C01; BKP-1.0, Kurallar] · `RKB-E04`, `RKB-X01` |
| `RKB-T01` | Teknoloji statüsü `unknown` | Sektör, ürün veya şirket adından statü türetilmedi | Bilinmiyor kalır; insan danışman çözer | [RKB-T01; BKP-1.0, Kurallar] · `RKB-X02` |
| `RKB-Y01` | `met` + danışman görüşü yok + yönlendirme yok | `met` bildirim yükümlülüğüne çevrilmedi | Danışman rotası ve yönlendirme olmadan kapanış ilerlemez | [RKB-Y01; BKP-1.0, Kurallar] · `RKB-E04`, `RKB-X03`, `RKB-X04` |
| `RKB-R01` | Gecikmesiz kapanış talebi; kapı kaydı yok | Kapanış onaylanmadı, kapı açılmadı | Kapanış kapısı kapalı | [RKB-R01; BKP-1.0, Kurallar] · `RKB-E05`, `RKB-X04` |
| `RKB-M01` | Sürüm `RKB-2608-v3`; izleme sahibi/tetik yok | Sahip, tarih ve tetik üretilmedi | İzleme kaydı eksik | [RKB-M01; BKP-1.0, Kurallar] · `RKB-E03`, `RKB-X05` |

## Gerekli insan kararı

- Kontrol: Brifte sağlanan kalıcı tek kontrol değişikliği olgusunun hukuki
  nitelendirmesini Rekabet Hukuku Danışmanı yapar [`RKB-K01`, `RKB-A01`].
- Teknoloji teşebbüsü durumu: `unknown` değerini yalnız insan danışman çözer
  [`RKB-T01`].
- Bildirim incelemesi: `met` göstergesinin hukuki sonuca dönüşüp dönüşmeyeceğine
  Rekabet Hukuku Danışmanı karar verir [`RKB-A01`].
- Kapanış yönlendirmesi: Yazılı yönlendirme ve kapı kaydı Rekabet Hukuku
  Danışmanı yetkisindedir [`RKB-R01`, `RKB-A01`].
- Finans yalnız precomputed ciro sonucunun sahibidir; hukuki nitelendirme yetkisi
  yoktur.

## Kapanış ve değişiklik izleme

| Kapı/değişiklik | İnsan sahibi | Kayıt veya kanıt | Yeniden inceleme tetiği | Durum |
|---|---|---|---|---|
| Kapanış kapısı | Rekabet Hukuku Danışmanı | Yönlendirme ve kapı kaydı yok | Yönlendirmenin kaydedilmesi | fail |
| Teknoloji statüsü | Rekabet Hukuku Danışmanı | Sağlanmadı | Statünün çözülmesi | unknown |
| Ciro sonucu sürümü | Finans | `met`, `RKB-2608-v3` | Yeni işlem sürümü veya kapsam değişikliği | pass |
| Taraf, hak veya yapı | bilinmiyor | Sağlanmadı | Veto/yönetim hakkı ya da oran değişikliği | unknown |
| İmza/kapanış takvimi | bilinmiyor | Sağlanmadı | Takvim değişikliği | unknown |
| Olgu/sürüm izleme sahipliği | bilinmiyor | Sağlanmadı | bilinmiyor | unknown |

## Sınırlar

Ciro hesaplanmamış, eşik uygulanmamış ve hukuki filing kararı verilmemiştir.
Teknoloji teşebbüsü statüsü üretilmemiştir. Hiçbir bildirim, imza, kapanış,
yeniden yapılandırma veya işlem eylemi yapılmamış; kapanış durdurulduğu iddia
edilmemiştir. Nihai hukuki karar ve tüm işlem eylemleri yetkili insanlardadır.
