# Çıktı şeması

Yanıt 650 kelimeyi aşmaz ve aşağıdaki başlıkları aynen kullanır.

## Karar

- Karar sınıfı: izin verilen beş değerden tam biri
- Önerilen seçenek: izin verilen üç değerden tam biri
- İstenen canlıya geçiş: `uygun`, `koşullu`, `beklemede`, `escalation gerekli`
  veya `reddedildi`
- Kısa gerekçe: en fazla üç cümle

## Yöntem envanteri

| Kanal/adım | İnsan veya sistem rolü | Doğrulama noktası | İstisna/geri dönüş | Kaynak | Durum |
|---|---|---|---|---|---|

Durum yalnız `pass`, `fail`, `unknown` veya `not-applicable` olur.

## Kontrol ve kanıt kapıları

| Kural | Sağlanan kanıt | Eksik/çatışmalı bilgi | Bulgu | Kaynak |
|---|---|---|---|---|

`BDK-V01`, `BDK-L01`, `BDK-K01`, `BDK-R01` ve `BDK-M01` ayrı satırlarda yer
alır. Kanıt yoksa hücrede açıkça `Sağlanmadı` yazılır.

## Gerekli insan kararı

Güvenlik, Uyum ve Hukuk için gereken kararı ve hangi eksik/çatışmalı bilgiyi
çözeceklerini ayrı maddelerde yaz. Asistanın karar veya eylem yetkisi olmadığını
tek cümlede belirt.

## Canlıya geçiş ve izleme

| Kapı | Sahip | Tamamlanma kanıtı | Engel veya tetik | Durum |
|---|---|---|---|---|

Sağlanmayan sahip, sıklık, eşik, durdurma veya manuel geri dönüş tetiği
`bilinmiyor` kalır.

## Sınırlar

Hukuki tavsiye, resmi uygunluk sonucu ve teknik sertifika verilmediğini; hiçbir
sistem veya müşteri eylemi yapılmadığını; nihai kararın insanlarda olduğunu yaz.