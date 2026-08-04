# Sunum kurulumu

1. `sources/source-manifest.json` içindeki resmi URL, SHA-256, yayıncı, erişim tarihi ve metadata-only yeniden kullanım kaydını göster.
2. `sources/company-policy.md` ve `sources/case-brief.md` dosyalarını aç; tüm şirket ve vaka verisinin sentetik olduğunu belirt.
3. `skill/` altında yalnız `SKILL.md` ile `references/` içindeki tam beş dosyanın bulunduğunu doğrula.
4. `evaluation/frozen-prompt.md` metnini değiştirmeden çalıştır.
5. Yanıtı `evaluation/rubric.json` ile puanla; what-if için yalnız seçilen kilitli senaryonun mutasyonunu uygula.

Gerçek müşteri, cüzdan, ödeme, satıcı veya sözleşme verisi kullanma. Demo hukuki
tavsiye vermez; lansman, ödeme, transfer, ürün değişikliği veya durdurma yapmaz.
Yatırım ve checkout dışı transfer hukukunu kapsam dışı tut.