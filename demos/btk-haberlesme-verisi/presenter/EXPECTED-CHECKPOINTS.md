# Beklenen kontrol noktaları

## Baseline

- Tek sınıf: `stop-processing`
- Tek seçenek: `consent-first-redesign`
- Konum ve trafik verisi bireysel upsell hedeflemesinde birlikte kullanılır.
- BTK-V01: sağlanan kategoriler ve CRM bağları kaydedilir.
- BTK-A01: amaç eşlemesi ve hukuki rota `unknown`.
- BTK-R01: rıza kaydı, kapsam, zaman, sürüm ve geri alma durumu `unknown`.
- BTK-S01: saklama süresi/silme tetikleri `unknown`; güvenlik kanıtı kısmi.
- BTK-Y01: Privacy Counsel + Telecom Compliance + DPO ve KVKK ortak incelemesi.
- BTK-G01: mevcut kampanya kapısı kapalıdır.
- BTK-M01: rıza/saklama izleme ayrıntıları `unknown` kalır.

## Sınırlar

- Hukuki tavsiye veya nihai mahremiyet/KVKK sonucu yoktur.
- Resmi kaynak tek başına tüm mahremiyet hukukunu çözmez.
- Copilot işleme, kampanya, durdurma, veri silme veya sistem değişikliği yapmaz.
- Resmi kaynak metadata-only kalır; uzun mevzuat metni taşınmaz.

## Değerlendirme

- Tam 12 benzersiz senaryonun her birinde `locked: true` bulunur.
- Beş karar sınıfı ve üç işleme seçeneği senaryo kümesinde kapsanır.
- Pozitif rubrik toplamı 14'tür; her boyutta `0..max` çıpaları vardır.
- Skill paketinde yalnız bir ana dosya ve tam beş referans bulunur.