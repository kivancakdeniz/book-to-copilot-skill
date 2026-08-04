# BDDK uzaktan müşteri edinimi

[English](../../skills/bddk-uzaktan-musteri-edinimi.md)

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı yazıldı | hayır | hayır |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **80 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `BDK-01`

[Kontrol yanıtı](../../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/bddk-uzaktan-musteri-edinimi/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/bddk-uzaktan-musteri-edinimi
```

Kontrol çalıştırması 7 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 7 tanesine atıf yaptı. Skill çalıştırması kilitli beklenen sınıf (`reject-flow`) yerine daha temkinli bir sınıf seçti; sınıf çağrısı insan incelemesinde kalır.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/bddk-uzaktan-musteri-edinimi/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Bankalarca Kullanılacak Uzaktan Kimlik Tespiti Yöntemlerine ve Elektronik Ortamda Sözleşme İlişkisinin Kurulmasına İlişkin Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210401-7.htm) — Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/bddk-uzaktan-musteri-edinimi/skill/public-method.md` |
| Sentetik şirket politikası | `demos/bddk-uzaktan-musteri-edinimi/sources/company-policy.md` |
| Sentetik vaka | `demos/bddk-uzaktan-musteri-edinimi/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/bddk-uzaktan-musteri-edinimi/evaluation/` |
| Taşınabilir skill | `demos/bddk-uzaktan-musteri-edinimi/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Bir bakışta iş etkisi

| Soru | Etki |
|---|---|
| Hangi karar gerekir? | Temel vakada `reject-flow`; güvenli seçenek `manual-onboarding-fallback` |
| Hangi risk görünür olur? | Canlı/görüntülü etkileşim, canlılık/bütünlük, kayıt ve izleme kanıtı boşlukları |
| Kim karar verir? | Güvenlik, Uyum ve Hukuk insan yetkilileri |
| Skill ne kazandırır? | Aynı beş sınıf, üç seçenek, kural izlenebilirliği ve 14 puanlık ölçülebilir çıktı |
| Skill ne yapmaz? | Hukuki tavsiye, resmi uygunluk, teknik sertifika, canlıya geçiş veya müşteri işlemi |

## Nasıl çalışır?

Skill, Resmî Gazete kaynağını metadata-only manifestle sınırlar; resmi metni
yeniden dağıtmaz veya kopyalamaz. Kısa kamu yöntemi sorularını sentetik UME-1.0
şirket politikasından ve sentetik UME-2408 vaka kanıtından ayırır. Sonuç, tam bir
karar sınıfı, tam bir seçenek, kanıt kapıları ve gerekli insan rotasıdır.

Temel akışta canlı veya görüntülü etkileşim, canlılık ve süreç bütünlüğü kanıtı,
kontrol günlükleri, izleme planı ve insan onayları yoktur. Bu nedenle doğrudan
canlıya geçiş önerilmez. Her eksik alan açık kalır; selfie'den teknik
sertifikasyon sonucu çıkarılmaz.

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Değerlendirme

Demo, cevap anahtarı istemden ayrı tam 12 kilitli senaryo ve her boyutu açık
ankrajlı 14 puanlık rubrik içerir. Puanlama doğru sınıf/seçenek kadar yöntem
envanterini, kanıt disiplinini, kaynak izlenebilirliğini, insan yetkisini ve
canlıya geçiş/izleme kapılarını da ölçer.

Bu içerik eğitim ve yönetişim tasarımı içindir. Nihai karar ve bütün uygulama
eylemleri yetkili insanlarda kalır.