# Kanıt haritası

Kanonik vaka: `../../sources/case-brief.md`.

## Temel vaka kanıtı

| Kanıt kimliği | Vaka alanı | Sağlanan gerçek | Sınır |
|---|---|---|---|
| `UME-E01` | İş talebi | Dijital ekip doğrudan canlıya geçmek istiyor | İnsan onayı veya uygunluk sonucu değildir |
| `UME-E02` | Yöntem | E-posta ile kimlik belgesi taraması | Canlı/görüntülü etkileşim kanıtlamaz |
| `UME-E03` | Yöntem | Aynı e-postada tek selfie | Canlılık, bütünlük veya kimlik doğrulama sonucu kanıtlamaz |
| `UME-E04` | Operasyon | Dosyalar görülüp mevcut müşteri sistemine aktarılacak | Görevli doğrulaması, istisna veya geri dönüş haritası sağlanmadı |
| `UME-X01` | Etkileşim | Canlı veya görüntülü etkileşim kanıtı yok | Açıkça sağlanmadı |
| `UME-X02` | Güvenlik | Canlılık ve süreç/oturum bütünlüğü kanıtı yok | Tedarikçi veya sertifika varsayılmaz |
| `UME-X03` | Kayıt | Kontrol ve denetim günlükleri yok | Kayıt kapsamı üretilmez |
| `UME-X04` | İzleme | Dolandırıcılık ve kontrol izleme planı yok | Sahip, sıklık, eşik ve tetik bilinmiyor |
| `UME-X05` | Yetki | Güvenlik, Uyum ve Hukuk onayı yok | Asistan bu onayları veremez |

## Temel eşleme

- `BDK-I01`: `UME-E02`, `UME-E03`, `UME-E04`; kalan envanter eksik.
- `BDK-V01`: `UME-X01`; e-posta ve selfie ek doğrulama kanıtı oluşturmaz.
- `BDK-L01`: `UME-X02`.
- `BDK-K01`: `UME-X03`.
- `BDK-A01`: `UME-X05`.
- `BDK-R01`: Canlı talebi `UME-E01`, zorunlu kapılar tamamlanmadı.
- `BDK-M01`: `UME-X04`.

Senaryo mutation alanları bu temel gerçekleri adlandırdığı ölçüde değiştirir.
Değişmeyen alanlar taşınır; null değer kanıtın sağlanmadığı anlamına gelir.