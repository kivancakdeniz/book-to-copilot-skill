# İSG risk değerlendirmesi: değişiklikten devreye alma kapısına

[English](../../skills/isg-risk-degerlendirme.md)

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `ISG-01`

[Kontrol yanıtı](../../assets/skills/isg-risk-degerlendirme/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/isg-risk-degerlendirme/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/isg-risk-degerlendirme/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/isg-risk-degerlendirme
```

Kontrol çalıştırması 7 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 7 tanesine atıf yaptı. Tam karar sınıfını (`renew-assessment`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/isg-risk-degerlendirme/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [İş Sağlığı ve Güvenliği Risk Değerlendirmesi Yönetmeliği](https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm) — T.C. Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/isg-risk-degerlendirme/skill/public-method.md` |
| Sentetik şirket politikası | `demos/isg-risk-degerlendirme/sources/company-policy.md` |
| Sentetik vaka | `demos/isg-risk-degerlendirme/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/isg-risk-degerlendirme/evaluation/` |
| Taşınabilir skill | `demos/isg-risk-degerlendirme/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Ne derler?

- Değişiklik mevcut risk değerlendirmesinin kapsamında mı?
- Operatör, bakım ve çalışan temsilinin katılımı kanıtlı mı?
- Koruma, erişim ve kilitleme/etiketleme kontrolleri doğrulanmış mı?
- Açık bulguların insan sahibi, aksiyonu ve tarihi var mı?
- Devreye alma kapısı ile olay ve değişiklik izleme tetikleri açık mı?

## Kaynak yaklaşımı

Kamusal yöntem kaynağı, T.C. Resmî Gazete'de yayımlanan
[İş Sağlığı ve Güvenliği Risk Değerlendirmesi Yönetmeliği](https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm)
sayfasıdır. Snapshot SHA-256 değeri
`a1ab5bfc1ea7c305393d7fa75f33d7a7debaf97fe3a6e46cc5d4dfb9276a31dc`,
erişim tarihi `2026-08-04`tür. Dış kaynak yalnızca metadata olarak dağıtılır;
skill uzun kopyalar yerine kısa ve atıflı yöntem özeti taşır. Güncel metin ve
yeniden kullanım koşulları insan tarafından resmî kaynaktan doğrulanır.

Şirket politikası, vaka, roller ve bütün operasyonel kayıtlar sentetiktir.

## İndir

- [Microsoft 365 Copilot Cowork skill](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [GitHub Copilot for VS Code paketi](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Scout paketi](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub harness paketi](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum paketi](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

!!! warning "Copilot Studio classic kurulumu"

    Classic paket doğrudan yüklenen, çalışma zamanını veya davranışı sabitleyen
    bir skill değildir. Yönlendirmeli manuel kurulum malzemesidir; talimatlar,
    bilgi kaynakları, bağlantılar, izinler ve yayımlama ayarları bir insan
    tarafından hedef ortamda ayrı ayrı incelenip yapılandırılmalıdır.

## Değerlendirme sözleşmesi

Demo tam 12 kilitli senaryo, beş karar sınıfı, üç seçenek ve her puan düzeyi
çapalanmış azami 14 puanlık rubrik kullanır. Donmuş prompt; kanıt, kişi, tarih,
eşik veya yetki uydurmayı ve sohbet dışı eser ya da operasyonel eylem üretmeyi
yasaklar.

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.
