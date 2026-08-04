# Sunum kurulumu

## Amaç

Eski müşterilere promosyon SMS'inde amaç sınıflandırmasını, güncel rıza/IYS
kanıtını, bastırma kapısını ve insan karar sınırını göstermek.

## Hazırlık

1. `sources/source-manifest.json` içindeki iki resmî URL ve SHA-256 kaydını
   ekranda hazır tut; resmî dosyaları pakete kopyalama.
2. `sources/company-policy.md` ile `sources/case-brief.md` dosyalarını aç.
3. Altı dosyalık `skill/` klasörünü desteklenen hosta yükle.
4. Yeni bir konuşmada yalnız `evaluation/frozen-prompt.md` ve başlangıç vaka
   olgularını kullan.
5. İlk yanıtı değiştirmeden sakla; rubriği yanıt üretildikten sonra uygula.

## Güvenlik

Gerçek telefon numarası, müşteri listesi, rıza kaydı veya IYS dışa aktarımı
kullanma. Demo hukuki tavsiye veya nihai hukuki sonuç değildir. İnsan CRM Owner,
Compliance ve Legal kararın sahibidir. Asistan mesaj göndermez, kayıt değiştirmez,
kitle bastırmaz veya başka otonom eylem yapmaz.