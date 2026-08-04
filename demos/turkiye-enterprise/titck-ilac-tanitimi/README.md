# TİTCK ilaç tanıtımı Copilot demosu

Bu Türkçe demo, reçeteli kurgusal bir ürün için tüketiciye açık Instagram
kreatifinin yayın talebini inceler. Kreatifte ürün adı, fayda ifadesi ve çağrı
vardır; sağlık meslek mensuplarına özel erişim kontrolü yoktur.

Kilitli başlangıç sonucu `do-not-publish`, önerilen seçenek
`professional-channel-review`dır. Bu seçenek ayrı profesyonel materyali veya
kanalı onaylamaz; ürün statüsü, iddia kapsamı, gerçek erişim kontrolü ve Medical,
Regulatory, Legal insan incelemesi gerektirir.

Bu materyal hukuki, mühendislik veya tıbbi tavsiye değildir. Copilot mevzuat ya
da tıbbi uygunluk sonucu vermez; içeriği onaylamaz, yayımlamaz, hedeflemez,
kaldırmaz veya kampanyayı durdurmaz. Bütün karar ve eylemler yetkili insanlarda
kalır.

## Yapı

```text
sources/       İki resmî kaynak metadatası ile sentetik politika ve vaka brifi
evaluation/    Donmuş prompt, 12 kilitli senaryo ve 14 puanlık rubrik
skill/         SKILL.md ve tam beş referans
presenter/     Kurulum, konuşma akışı ve beklenen kontrol noktaları
```

TİTCK ve Resmî Gazete dış kaynak metinleri bu ağaçta yeniden dağıtılmaz.
Manifest yalnızca URL, yayıncı, erişim tarihi, SHA-256 ve yeniden kullanım notu
taşır. Skill, uzun kopyalar yerine kısa ve atıflı bir inceleme yöntemi kullanır.

## Başlangıç dosyaları

- `sources/company-policy.md`: sentetik karar, seçenek, kural ve yetki sınırı
- `sources/case-brief.md`: cevap anahtarını taşıyan kilitli Instagram vakası
- `evaluation/frozen-prompt.md`: bütün değerlendirme kollarında aynı görev
- `evaluation/scenarios.json`: tam 12 senaryonun kilitli cevap anahtarı
- `evaluation/rubric.json`: azami 14 puan ve tam puan çapaları
