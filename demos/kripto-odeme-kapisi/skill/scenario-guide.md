# Senaryo rehberi

## Donmuş başlangıç

Her senaryo KRP-2401 ve KRP-1.0'dan başlar. Mutasyon yalnız adlandırdığı olguyu
değiştirir; diğer olgular taşınır. Mutasyonu politika değişikliği, insan onayı
veya hukuki sonuç sayma.

## Eksik akış kanıtı

Mutabakat birimi, dönüşüm, aracı rolü, sözleşme veya dağıtılan sürüm eksikse
ilgili öğeyi `unknown` işaretle. Belirleyici eksik karar vermeyi engelliyorsa
`hold-for-flow-evidence` kullan; varsayım veya sözleşme üretme.

## Ödeme dışı yeniden tasarım

Bir işlevin ödeme dışı olması için yalnız adı değil, uçtan uca olguları da
satıcı alımı, ödeme talimatı, cüzdan, dönüşüm, transfer ve mutabakattan ayrılmış
olmalıdır. İnsan onayı ve KRP-R01 kapısı ayrıca gereklidir.

## Aracısız akış

Ödeme hizmeti aracısının kaldırılması, kripto varlık satıcı siparişini doğrudan
kapatmaya devam ediyorsa KRP-O01 sorununu çözmez. İşleve ve sonuca bak.

## Kapsam dışı yatırım veya transfer sorusu

Vaka ödeme akışı dışındaki yatırım, saklama veya transfer hukukunu çözmez. Kesin
görüş verme; `escalate-payments-counsel` ile insan değerlendirmesine yönlendir.

## Çelişkili sürüm ve izleme

Akış diyagramı, ürün özeti ve dağıtılan sürüm uyuşmuyorsa değerleri uzlaştırma.
Çelişkiyi göster, dağıtılan sürümü `unknown` tut ve KRP-R01 kapısını geçirme.
Checkout, cüzdan, dönüşüm, aracı veya mutabakat adımı eklenmesi KRP-M01 uyarınca
yeni insan incelemesi tetikler; Copilot değişikliği durduramaz veya uygulayamaz.