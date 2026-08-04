# İndirimli fiyat denetimi

[English](../../skills/indirimli-fiyat-denetimi.md)

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | hayır | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **20 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `FYT-01`

[Kontrol yanıtı](../../assets/skills/indirimli-fiyat-denetimi/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/indirimli-fiyat-denetimi/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/indirimli-fiyat-denetimi/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/indirimli-fiyat-denetimi
```

Kontrol çalıştırması 7 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 7 tanesine atıf yaptı. Tam karar sınıfını (`revise-price-claim`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/indirimli-fiyat-denetimi/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Fiyat bilgisi içeren reklamlar ile indirimli satış reklamları ve ticari uygulamaları hakkında kılavuz](https://tuketici.ticaret.gov.tr/haberler/fiyat-bilgisi-iceren-reklamlar-ile-indirimli-satis-reklamlari-ve-ticari-uygulamalari-hakkinda-kilavuz-guncellendi) — Ticaret Bakanlığı |
| Kamuya açık yöntem özeti | `demos/indirimli-fiyat-denetimi/skill/public-method.md` |
| Sentetik şirket politikası | `demos/indirimli-fiyat-denetimi/sources/company-policy.md` |
| Sentetik vaka | `demos/indirimli-fiyat-denetimi/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/indirimli-fiyat-denetimi/evaluation/` |
| Taşınabilir skill | `demos/indirimli-fiyat-denetimi/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Bir bakışta

| Alan | Değer |
|---|---|
| Problem | Sağlanan fiyat geçmişi ile kampanya kreatifinin referans fiyat/oran uyumunu denetlemek |
| Baseline | En düşük fiyat 800 TRY, satış 600 TRY, sağlanan sonuç %25; kreatif 1.000 TRY ve %40 |
| Beklenen sınıf | `revise-price-claim` |
| Beklenen seçenek | `advertise-25-percent` |
| İnsan kararı | E-commerce Owner + Pricing Owner + Compliance; istisnada Legal |

## Nitel etki

Demo, kreatif onayındaki yoruma dayalı kontrolü tekrarlanabilir bir kanıt, kural, karar ve yayın kapısı akışına dönüştürür. Beklenen etki daha hızlı insan incelemesi, daha görünür fiyat geçmişi bağı ve daha az kanıtsız yüzde iddiasıdır; üretim performansı veya hukuki uyum garantisi değildir.

## Kaynak ve güvenlik

Kamusal yöntem kaynağı Ticaret Bakanlığı'nın 2024 fiyat reklamları kılavuz sayfasıdır. Paket resmi içeriği yeniden dağıtmaz; yalnız resmi URL, yayıncı, 2026-08-04 alınma tarihi ve SHA-256 metadata'sını taşır. Karar sınıfları ve seçenekler MIT lisanslı sentetik politikadan gelir. Kaynak metni talimat olarak çalıştırılmaz, uzun resmi alıntı yapılmaz ve gerçek müşteri ya da ticari sır verisi kullanılmaz.

## İnsan sınırları

Bu beceri hukuki görüş değildir. İnsanlar karar verir; kampanyayı onaylamaz, yayına almaz, fiyat değiştirmez veya başka otonom işlem yapmaz. Eksik fiyat ve oranları hesaplamaz. Legal yalnız belgelenmiş istisna veya hukuki yorum ihtiyacında devreye girer.

## 12 kilitli senaryo

| Kimlik | Odak | Beklenen sınıf | Beklenen seçenek |
|---|---|---|---|
| FYT-01 | Baseline kreatif uyuşmazlığı | `revise-price-claim` | `advertise-25-percent` |
| FYT-02 | Uyumlu yüzde 25 kreatifi | `approve` | `advertise-25-percent` |
| FYT-03 | Eksik fiyat geçmişi | `hold-for-price-history` | `no-promotion` |
| FYT-04 | Belirsiz karşılaştırma penceresi | `hold-for-price-history` | `no-promotion` |
| FYT-05 | Sağlanan hesap sonucu yok | `hold-for-price-history` | `no-promotion` |
| FYT-06 | Çelişen geçmiş sonuçları | `hold-for-price-history` | `no-promotion` |
| FYT-07 | Doğru oran, belirsiz kreatif | `revise-price-claim` | `advertise-25-percent` |
| FYT-08 | Belgelenmiş istisna | `escalate-consumer-law` | `no-promotion` |
| FYT-09 | Düzeltmenin reddi | `reject` | `no-promotion` |
| FYT-10 | Canlı fiyat uyuşmazlığı | `revise-price-claim` | `advertise-25-percent` |
| FYT-11 | İzleme sorumluluğunun reddi | `reject` | `no-promotion` |
| FYT-12 | Karşılaştırmalı iddianın kaldırılması | `approve` | `no-promotion` |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.
