# Kripto ödeme kapısı demosu

Bu demo, kurgusal bir ödeme kuruluşunun satıcı checkout akışında USDT kullanma
talebini kanıta dayalı biçimde inceler. Resmi TCMB/Resmî Gazete kaynağı yönteme
bilgi verir; karar sınıfını, ürün seçeneğini ve insan yetkisini sentetik Kurgusal Ödeme
KRP-1.0 politikası belirler.

## Baseline

- USDT satıcı mal veya hizmet alımını doğrudan kapatır.
- Bir ödeme hizmeti aracısı talimat, dönüşüm ve mutabakat akışındadır.
- Talep mevcut akışı değiştirmeden lansmandır.
- Beklenen sınıf: `reject-payment-flow`
- Beklenen seçenek: `remove-crypto-checkout`

## Güvence sınırı

Bu demo hukuki tavsiye veya nihai hukuki karar vermez. Payments Counsel,
Compliance ve Product karar verir. Copilot lansman, ödeme, transfer, ürün
değişikliği veya durdurma yapmaz. Sağlanan ödeme akışının ötesinde yatırım veya
transfer hukukuna ilişkin görüş üretmez; resmi mevzuat metnini yeniden dağıtmaz.

## Yapı

- `sources/`: metadata-only resmi yöntem kaydı ile hashli sentetik politika/vaka
- `evaluation/`: donmuş prompt, tam 12 kilitli senaryo ve 14 puanlık rubrik
- `skill/`: taşınabilir `SKILL.md` ve tam beş yerel referans
- `presenter/`: kurulum, konuşma akışı ve beklenen kontrol noktaları

Her proje dosyası bu slug altında yereldir; başka demo dosyası paylaşılmaz.