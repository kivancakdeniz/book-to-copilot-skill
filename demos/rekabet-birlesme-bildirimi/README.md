# Rekabet birleşme bildirimi Copilot demosu

Bu Türkçe demo, kalıcı kontrol değişikliği içeren kurgusal bir devralmada
bildirim göstergesi ve kapanış kapısının nasıl insan incelemesine yönlendirileceğini
gösterir. Finans yalnız önceden hesaplanmış ciro testi sonucunu `met` olarak
sağlamıştır; hedefin teknoloji teşebbüsü durumu `unknown`dır. İmza yakındır ve
kapanış istenmektedir.

Kilitli başlangıç sonucu `legal-notification-review`, önerilen seçenek
`hold-closing`dir. Asistan ciro hesaplamaz, eşik uygulamaz veya hukuki bildirim
kararı vermez. Rekabet Hukuku Danışmanı bütün hukuki nitelendirme ve kapanış
yönlendirmesinin insan sahibidir.

Bu paket hukuki tavsiye değildir. Asistan işlem yapısını değiştiremez, imza veya
kapanış yapamaz, bildirim gönderemez ya da kapanış izni veremez.

## Yapı

```text
sources/       İki kamu kaynağı metadatası ile MIT lisanslı sentetik politika/vaka
evaluation/    Donmuş prompt, tam 12 kilitli senaryo ve ankrajlı 14 puanlık rubrik
skill/         SKILL.md ve tam beş referans
presenter/     SETUP, TALK_TRACK ve EXPECTED sunum belgeleri
```

Rekabet Kurumu kaynaklarının içeriği bu ağaçta yeniden dağıtılmaz. Manifest
yalnız URL, yayıncı, alınma tarihi, SHA-256 ve yeniden kullanım uyarısı taşır.
Skill resmi metin kopyalamak yerine kısa ve atıflı yöntem soruları kullanır.

## Başlangıç dosyaları

- `sources/company-policy.md`: sentetik sınıf, seçenek, kural ve yetki sınırı
- `sources/case-brief.md`: kilitli kurgusal devralma vakası
- `evaluation/frozen-prompt.md`: bütün değerlendirme kollarında aynı görev
- `evaluation/scenarios.json`: tam 12 senaryonun kilitli cevap anahtarı
- `evaluation/rubric.json`: azami 14 puan ve açık puan ankrajları