# Çıktı şeması

Yanıt 650 kelimeyi aşmaz ve aşağıdaki başlıkları aynen kullanır.

## Karar

- Karar sınıfı: izin verilen beş değerden tam biri
- Önerilen seçenek: izin verilen üç değerden tam biri
- İstenen kapanış: `ilerleyebilir`, `beklemede`, `insan danışman yönlendirmesi
  gerekli` veya `reddedildi`
- Kısa gerekçe: en fazla üç cümle

## İşlem ve kontrol olguları

| Olgu | Sağlanan değer | Kaynak/sürüm | Eksik veya çatışma | Durum |
|---|---|---|---|---|

Durum yalnız `pass`, `fail`, `unknown` veya `not-applicable` olur. Hukuki kontrol
nitelendirmesi sağlanmamışsa insan danışmana bırakılır.

## Gösterge ve kanıt kapıları

| Kural | Sağlanan sonuç/olgu | Yapılmayan hesaplama veya çıkarım | Bulgu | Kaynak |
|---|---|---|---|---|

`RKB-C01`, `RKB-T01`, `RKB-Y01`, `RKB-R01` ve `RKB-M01` ayrı satırlarda yer
alır. Precomputed sonuç ile hukuki bildirim kararı açıkça ayrılır.

## Gerekli insan kararı

Rekabet Hukuku Danışmanının çözmesi gereken kontrol, teknoloji statüsü,
bildirim incelemesi ve kapanış yönlendirmesi konularını ayrı maddelerde yaz.
Finans'ın yalnız precomputed sonuç sahibi olduğunu belirt.

## Kapanış ve değişiklik izleme

| Kapı/değişiklik | İnsan sahibi | Kayıt veya kanıt | Yeniden inceleme tetiği | Durum |
|---|---|---|---|---|

Sağlanmayan sahip, tarih, yönlendirme ve tetik `bilinmiyor` kalır.

## Sınırlar

Ciro hesaplanmadığını, hukuki filing kararı verilmediğini, hiçbir bildirim,
imza, kapanış veya yapı değişikliği yapılmadığını ve nihai kararın insanlarda
olduğunu yaz.