# BTK haberleşme verisi demosu

Bu demo, kurgusal bir telekom CRM'inin konum ve trafik verisiyle bireysel upsell
kampanyası başlatma talebini kanıta dayalı biçimde inceler. Resmi BTK/Resmî
Gazete kaynağı yönteme bilgi verir; karar sınıfını, işleme seçeneğini ve insan
yetkisini sentetik Kurgusal Telco BTK-1.0 politikası belirler.

## Baseline

- Konum ve trafik verisi bireysel upsell hedeflemesinde birlikte kullanılır.
- Rıza kaydı ve amaç/veri eşlemesi sağlanmamıştır.
- Saklama süresi sağlanmamıştır.
- Kampanyanın başlatılması talep edilmektedir.
- Beklenen sınıf: `stop-processing`
- Beklenen seçenek: `consent-first-redesign`

## Güvence sınırı

Bu demo hukuki tavsiye veya nihai hukuki karar vermez. Privacy Counsel, Telecom
Compliance ve DPO, telekom ile KVKK boyutlarını birlikte inceler. Resmi kaynak
tek başına tüm mahremiyet hukukunu çözmez. Copilot işleme, kampanya, durdurma,
veri silme veya sistem değişikliği yapmaz; uzun mevzuat metni yeniden dağıtmaz.

## Yapı

- `sources/`: metadata-only resmi yöntem kaydı ile hashli sentetik politika/vaka
- `evaluation/`: donmuş prompt, tam 12 kilitli senaryo ve 14 puanlık rubrik
- `skill/`: taşınabilir `SKILL.md` ve tam beş yerel referans
- `presenter/`: kurulum, konuşma akışı ve beklenen kontrol noktaları

Her proje dosyası bu slug altında yereldir; başka demo dosyası paylaşılmaz.