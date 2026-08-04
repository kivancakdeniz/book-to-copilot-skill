# BDDK uzaktan müşteri edinimi Copilot demosu

Bu Türkçe demo, yalnızca e-posta ile kimlik taraması ve selfie isteyen kurgusal
bir dijital banka akışının canlıya geçiş talebini inceler. Canlı veya görüntülü
etkileşim, canlılık ve süreç bütünlüğü ile kontrol günlüğü kanıtları yoktur.

Kilitli başlangıç sonucu `reject-flow`, önerilen seçenek
`manual-onboarding-fallback`tır. `current-remote-flow` canlıya alınmaz. Güvenlik,
Uyum ve Hukuk bütün karar ve eylemlerin sahibidir.

Bu paket hukuki tavsiye, resmi uygunluk kararı veya teknik sertifika vermez.
Asistan müşteri edinimini başlatamaz, sistemi değiştiremez ya da canlıya geçişi
onaylayamaz.

## Yapı

```text
sources/       Metadata-only dış kaynak ile MIT lisanslı sentetik politika/vaka
evaluation/    Donmuş prompt, tam 12 kilitli senaryo ve ankrajlı 14 puanlık rubrik
skill/         SKILL.md ve tam beş referans
presenter/     SETUP, TALK_TRACK ve EXPECTED sunum belgeleri
```

Resmî Gazete metni bu ağaçta tutulmaz veya kopyalanmaz. Manifest yalnızca URL,
yayıncı, alınma tarihi, hash ve yeniden kullanım uyarısı taşır. Demo kural ve
örnekleri sentetiktir.

## Başlangıç dosyaları

- `sources/company-policy.md`: sentetik karar, seçenek, kural ve yetki sınırı
- `sources/case-brief.md`: kilitli uzaktan müşteri edinimi vakası
- `evaluation/frozen-prompt.md`: bütün değerlendirme kollarında aynı görev
- `evaluation/scenarios.json`: tam 12 senaryonun kilitli cevap anahtarı
- `evaluation/rubric.json`: azami 14 puan ve açık puan ankrajları