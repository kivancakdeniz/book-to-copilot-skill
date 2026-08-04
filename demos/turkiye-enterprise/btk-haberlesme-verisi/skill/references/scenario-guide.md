# Senaryo rehberi

## Donmuş başlangıç

Her senaryo BTK-CRM-310 ve BTK-1.0'dan başlar. Mutasyon yalnız adlandırdığı
olguyu değiştirir; diğer olgular taşınır. Mutasyonu hukuki sonuç veya insan onayı
sayma.

## Eksik veya çelişkili rıza

Rıza kimliği, metni, kapsamı, amacı, zamanı, sürümü, eki veya geri alma durumu
eksikse ilgili alanı `unknown` tut. İki sistem çelişiyorsa birini seçme;
`hold-for-consent-evidence` ve `consent-first-redesign` ile insan kanıtını bekle.

## Amaç ve hukuki rota

Rıza kaydı bulunması amaç/veri eşlemesini veya uygulanabilir hukuki rota
incelemesini kendiliğinden tamamlamaz. Kapsam belirsizliğini
`escalate-privacy-counsel` ile Privacy Counsel'a yönlendir. Resmi kaynağı bütün
mahremiyet hukukunun cevabı sayma; KVKK ortak incelemesini koru.

## Kontrollerle onay

`approve-with-controls` yalnız sağlanan daha dar seçenekte kalan bütün güvenlik,
saklama, toplulaştırma veya senkronizasyon kontrolleri işleme öncesi nesnel olarak
doğrulanabiliyorsa kullanılır. Kontrol kanıtı gelmeden BTK-G01 kapısı açılmaz.

## Aggregate-only

Bireysel profil ve hedefleme kaldırılmalı; toplulaştırma ve yeniden tanımlama
olguları sağlanmalıdır. Yalnız seçeneğin adına bakarak anonimlik varsayma.

## Canlı kampanya veya geri alınan rıza

Canlı işleme ya da geri alınmış rızanın CRM'e yansımaması `stop-processing`
sınıfını gerektirebilir. Bu danışman sınıf teknik işlem yapmaz. Privacy Counsel,
Telecom Compliance, DPO ve insan operasyonu durdurma, düzeltme, silme veya yeniden
başlatma kararını verir.

## İzleme

Rıza sürümü, geri alma senkronizasyonu, saklama tarihi, silme tetikleri ve
amaç/veri değişiklikleri BTK-M01 kayıtlarıdır. Sağlanmayan sahip, tarih veya eşik
`unknown` kalır.