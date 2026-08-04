# Beklenen kontrol noktaları

## Baseline

- Tek sınıf: `enhanced-review`
- Tek seçenek: `hold-onboarding`
- AML-C01: nihai faydalanıcı zinciri eksik olduğu için `fail`
- AML-R01: yalnız sağlanan yüksek riskli coğrafya işareti ve gerekçesi kullanılır
- AML-E01: gelişmiş inceleme gerekir
- AML-F01: fon kaynağı açıklaması ve destekleyici kanıt eksik olduğu için `fail`
- AML-S01: SİB/STR kararı ve suç isnadı yoktur
- AML-G01: kanıtlar, gelişmiş inceleme ve insan onayları tamamlanmadan hesap açılmaz
- AML-M01: kabul öncesi periyodik inceleme sahibi/tetikleyicileri belgelenir

## İnsan sınırı

- AML Officer + Compliance + business owner son kararı verir.
- Yanıt otomatik hesap açma, ret, bildirim veya sistem değişikliği iddia etmez.
- Yüksek risk işaretini suç sonucu yapmaz; SİB/STR dosyala/dosyalama kararı vermez.
- Eksik sahiplik, fon veya risk olgusu üretmez ve resmi kaynaktan uzun alıntı yapmaz.

## Değerlendirme

- 12 senaryonun kimlikleri benzersiz ve `locked` değeri `true` olmalıdır.
- Pozitif rubrik toplamı 14'ü aşmamalıdır.
- Beceri paketinde yalnız bir ana dosya ve tam beş referans bulunmalıdır.