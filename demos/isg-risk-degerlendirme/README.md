# İSG risk değerlendirmesi Copilot demosu

Bu Türkçe demo, kurgusal bir depoya paletleme robotu eklenirken değişiklik
öncesi hazırlanmış risk değerlendirmesinin devreye alma için yeterli olup
olmadığını inceler.

Kilitli başlangıç sonucu `renew-assessment`, önerilen seçenek
`hold-commissioning`dır. Operatör ve bakım katılımı ile koruma ve enerji
izolasyonu kanıtları eksiktir. Copilot yalnızca kanıtı düzenler ve insan
incelemesine taslak hazırlar; değerlendirmeyi kabul etmez, mühendislik
sertifikasyonu vermez, devreye alma veya durdurma işlemi yapmaz.

Bu materyal hukuki, mühendislik veya tıbbi tavsiye değildir. İşveren,
görevlendirilmiş İSG profesyonelleri ve diğer yetkili insanlar bütün karar ve
eylemlerin sahibidir.

## Yapı

```text
sources/       Resmî kaynak metadatası ile sentetik politika ve vaka brifi
evaluation/    Donmuş prompt, 12 kilitli senaryo ve 14 puanlık rubrik
skill/         SKILL.md ve tam beş referans
presenter/     Kurulum, konuşma akışı ve beklenen kontrol noktaları
```

Resmî Gazete kaynağının içeriği bu ağaçta yeniden dağıtılmaz. Manifest yalnızca
URL, yayıncı, erişim tarihi, SHA-256 ve yeniden kullanım notunu taşır. Skill,
kaynağın uzun bölümleri yerine kısa ve atıflı bir inceleme yöntemi kullanır.

## Başlangıç dosyaları

- `sources/company-policy.md`: sentetik karar, seçenek, kural ve yetki sınırı
- `sources/case-brief.md`: cevap anahtarını taşıyan kilitli paletleme robotu vakası
- `evaluation/frozen-prompt.md`: bütün değerlendirme kollarında aynı görev
- `evaluation/scenarios.json`: tam 12 senaryonun kilitli cevap anahtarı
- `evaluation/rubric.json`: azami 14 puan ve tam puan çapaları
