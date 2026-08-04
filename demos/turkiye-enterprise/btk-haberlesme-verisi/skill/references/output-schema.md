# Çıktı şeması

Aşağıdaki başlıkları aynen ve aynı sırada kullan. Hukuki sonuç ekleme.

## Karar

Tam olarak bir izin verilen karar sınıfı, kısa kanıt gerekçesi ve sonucun insan
incelemesine yönelik danışman analiz olduğunu yaz.

## Önerilen işleme seçeneği

Tam olarak bir seçenek yaz: `current-personalization`, `consent-first-redesign`
veya `aggregate-only`.

## İstenen kampanyanın durumu

Mevcut kampanya talebini ve sunulduğu haliyle ilerleyip ilerleyemeyeceğini
önerilen seçenekten ayrı belirt.

## Veri, amaç ve kontrol kaydı

| Öğe | Sağlanan olgu | Amaç/işleme | Kaynak | BTK kuralı | Durum | Gerekli insan işlemi |
|---|---|---|---|---|---|---|

Durum için yalnız `pass`, `fail`, `unknown` veya `not-applicable` kullan. Konum,
trafik, rıza, amaç/rota, erişim, aktarım, saklama, silme ve anonimleştirmeyi kapsa.

## Eksik veya çelişkili bilgi

Her eksikliği, etkilenen veri/amaç/kontrolü, kuralı, neden önemli olduğunu ve
sağlanmışsa insan sahibini listele. Eksik rıza veya kontrol üretme.

## İnsan ve ortak inceleme rotası

Privacy Counsel, Telecom Compliance ve DPO rollerini; telekom + KVKK ortak
incelemesini yaz. Copilot'un hukuki karar, onay, işleme, kampanya, durdurma,
silme veya sistem değişikliği yetkisi olmadığını belirt.

## Kampanya kapısı ve izleme

BTK-G01 kapısını kaydet. BTK-M01 için rıza metni/sürümü, geri alma
senkronizasyonu, saklama inceleme tarihi, silme tetikleri ve amaç/veri değişiklik
tetiklerini yaz; sağlanmayanları `unknown` bırak.

## Sınırlar

Çalışmanın sağlanan olgularla sınırlı ve hukuki tavsiye olmadığını; resmi
telekom kaynağının tek başına tüm mahremiyet hukukunu veya KVKK sonucunu
çözmediğini; tüm karar ve eylemleri insan yetkililere bıraktığını yaz.