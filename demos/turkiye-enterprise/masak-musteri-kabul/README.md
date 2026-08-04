# MASAK müşteri kabul demosu

Bu demo, kurgusal bir kurumsal müşteri onboarding vakasını kimlik, nihai faydalanıcı, risk ve fon kaynağı kanıtlarıyla inceler. MASAK Tedbirler Yönetmeliği sayfası yöntemi açıklar; hangi inceleme sınıfının ve onboarding seçeneğinin uygulanacağını sentetik Kurgusal AML Kuruluşu politikası belirler.

## Baseline

- Kurumsal kimlik belgeleri: tam
- Nihai faydalanıcı zinciri: eksik
- Fon kaynağı: açıklamasız ve kanıtsız
- Sağlanan risk olgusu: yüksek riskli coğrafya işareti
- Beklenen sınıf: `enhanced-review`
- Beklenen seçenek: `hold-onboarding`

## Güvence sınırı

Bu demo hukuki görüş vermez. İnsanlar karar verir; hesap açmaz, ilişkiyi reddetmez, bildirim yapmaz veya sistemde değişiklik yapmaz. SİB/STR kararı vermez, suç isnadı yapmaz, eksik olgu üretmez ve resmi kaynaktan uzun alıntı taşımaz.

## Yapı

- `sources/`: dış yöntem metadatası ve MIT lisanslı sentetik karar girdileri
- `evaluation/`: dondurulmuş istem, 12 kilitli senaryo ve 14 puanlık rubrik
- `skill/`: `SKILL.md` ve tam beş referans
- `presenter/`: kurulum, konuşma akışı ve beklenen kontrol noktaları

JSON dosyaları ayrıştırılmalı; `skill/` altında yalnız `SKILL.md` ile beş referans bulunmalıdır.