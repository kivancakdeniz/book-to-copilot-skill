# Yatırım Komitesi Copilot

[English](../../skills/investment-committee.md)

## Karar

Kurgusal Asteria Distribution Group, 4,8 milyon EUR tutarındaki tam otomasyon
önerisini onaylamalı mı; daha güvenli bir seçenek mi seçmeli, konuyu üst makama
mı taşımalı, reddetmeli mi, yoksa daha fazla kanıt mı istemeli?

Bu demo, aynı iş sorusu ve yatırım özeti için ilk yanıttan oluşan dört Cowork
UX koşusunu kaydeder:

| Koşul | Bağlam |
|---|---|
| Kontrol, iki koşu | Yalnız yatırım özeti; özel skill yok |
| Uygulama, iki koşu | Aynı özet; özel skill açıkça çağrıldı ve yüklenmiş olarak gösterildi |

Cowork Claude Opus 4.8'i gösterdi, ancak sabitlenmiş çalışma zamanı sürümünü
açıklamadı. Konuşma düzeyinde özel skill anahtarı görünmüyordu ve otomatik keşif
kurulu skill'i yüklemedi. Bu nedenle uygulama istemi skill'i açıkça çağırır.
Bu bir UX karşılaştırmasıdır, nedensel A/B değildir.

Uygulamanın Asteria'nın kurgusal politika kapılarını kullanması; asgari, aşamalı
ve talep edilen seçenekleri karşılaştırması; talep edilen seçeneğin ayrı hükmünü
koruması; eksik kanıtı belirlemesi; insan onay mercilerine yönlendirmesi ve her
kuralın kaynağını göstermesi beklenir.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 6 | 6 / 6 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

Host: Microsoft 365 Copilot Cowork · Model: Claude Opus 4.8 · Tarih: 2026-08-04 · Senaryo: `IC-01`

[Kontrol yanıtı](../../assets/skills/investment-committee/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/investment-committee/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/investment-committee/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/investment-committee
```

Kontrol çalıştırması 6 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 6 tanesine atıf yaptı. Tam karar sınıfını (`conditional-approval`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/investment-committee/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [The Green Book - UK government guidance on appraisal](https://assets.publishing.service.gov.uk/media/698dbcd17da91680ad7f4308/The_Green_Book_2026.pdf) — HM Treasury and Government Finance Function |
| Kamuya açık yöntem özeti | `demos/investment-committee/skill/public-method.md` |
| Sentetik şirket politikası | `demos/investment-committee/sources/company-policy.md` |
| Sentetik vaka | `demos/investment-committee/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/investment-committee/evaluation/` |
| Taşınabilir skill | `demos/investment-committee/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Temel vaka

| Seçenek | Taahhüt | NPV | Geri ödeme | Aşağı yönlü NPV | En büyük tedarikçi | Sonuç |
|---|---:|---:|---:|---:|---:|---|
| Asgari | EUR 0.8m | EUR 0.3m | 3.5y | EUR 0.0m | 30% | Operasyonel hedefleri karşılamıyor |
| Aşamalı otomasyon | EUR 3.2m | EUR 1.1m | 4.2y | EUR 0.2m | 45% | Hedefleri karşılıyor; eğitim onayı beklemede |
| Tam otomasyon | EUR 4.8m | EUR 1.6m | 5.4y | EUR -0.7m | 72% | Siber değerlendirme ve geri dönüş planı yok |

Kilitli uygulama cevap anahtarı, aşamalı otomasyonun koşullu onayını bekler.
Model bu sonucu ikna edici bir öneri üretmesi söylenerek değil, kanıt ve politika
uygulamasıyla kazanmalıdır.

## Değerlendirme

On iki senaryo; açık onayı, negatif NPV'yi, geri ödeme istisnasını, tedarikçi
yoğunlaşmasını, siber kanıtı, çelişkili olguları, eksik aşağı yönlü kanıtı, yetki
eskalasyonunu ve uygulanabilir seçenek bulunmamasını test eder.

Resmî kanıt yayını şunları gösterecektir:

- ham ilk koşu çıktıları;
- rastgeleleştirilmiş A/B karşılaştırması;
- karar ve seçenek doğruluğu;
- kapı kapsamı ve eksik bilgi tespiti;
- kaynak izi kalitesi;
- desteksiz kural ve uydurulmuş olgu cezaları;
- sınırlamalar ve başarısız vakalar.

## Cowork UX gözlemleri

Dört ayrı Cowork görevi korundu: iki kontrol ve skill'in açıkça çağrıldığı iki
uygulama. İki operasyonel deneme dışlandı: Word üretimini tetikleyen uzun biçimli
bir istem ve otomatik keşfin özel skill'i yüklemediği bir uygulama denemesi.

| Gözlem | Kontroller | Skill'in açıkça çağrıldığı uygulamalar |
|---|---|---|
| Aşamalı otomasyon önerildi | 2/2 | 2/2 |
| ACP eşikleri mevcut ve kural ID'siyle uygulandı | Mevcut değil | Evet |
| İnsan onay sınırı korundu | Evet | Evet |
| Desteksiz ayrıntılar içerdi | Evet | Evet |

İkinci uygulama kilitli altı IC-01 politika bulgusunun tamamını kullandı. İlk
uygulama açık bir ACP-F01 geçişini atladı. İki uygulama yanıtı da eksik izleme
ölçümleri veya sağlanmamış başka ayrıntılar hakkında desteksiz iddialarda bulundu.
Ham ilk yanıtlar düzeltilmeden veya yeniden koşturulmadan korundu.

Paket SHA-256:
`40c4f763cd0ffc30a939cd7a7cda2e58780ea9731eb4a3dc3376c4864168a659`.

### Kontrol kaydı

[Tam boyutlu kontrol kaydını aç](../../assets/skills/investment-committee/screenshots/06-control-2-1920x1080.png)

![Çalışma alanında yalnız yatırım özeti ve karar kartı bulunan Cowork kontrol yanıtı](../../assets/skills/investment-committee/screenshots/06-control-2-1920x1080.png)

[Kontrol 1 ham yanıtı](../../assets/skills/investment-committee/outputs/control-1.txt) ·
[Kontrol 2 ham yanıtı](../../assets/skills/investment-committee/outputs/control-2.txt)

### Skill'in açıkça çağrıldığı uygulama kaydı

[Tam boyutlu uygulama kaydını aç](../../assets/skills/investment-committee/screenshots/05-treatment-2-1920x1080.png)

![Yatırım Komitesi skill'i yüklenmiş Cowork uygulama yanıtı](../../assets/skills/investment-committee/screenshots/05-treatment-2-1920x1080.png)

[Uygulama 1 ham yanıtı](../../assets/skills/investment-committee/outputs/treatment-1.txt) ·
[Uygulama 2 ham yanıtı](../../assets/skills/investment-committee/outputs/treatment-2.txt) ·
[Koşu manifesti](../../assets/skills/investment-committee/metadata/cowork-runs.json)

Manifest yolları, demo kaynak ağacındaki özgün manifest klasörüne göredir.
Yayımlanmış ham varlıklar için yukarıdaki sayfa bağlantılarını kullanın.

!!! warning "Resmî kıyaslama beklemede"

    Bu dört kayıt Cowork UX gözlemidir; nedensel kanıt veya bağımsız doğrulanmış
    kıyaslama değildir. Sabit modelli, 12 senaryolu, üç kollu değerlendirme ve
    kör insan incelemesi beklemededir. Ön iç rubrik prova skorları performans
    iddiası olarak sunulmaz.

## Yeniden üretme

Kamusal yayın; bir `.skill` dosyasını, kurgusal yatırım özetini, ayrı Cowork
kontrol ve uygulama istemlerini, özdeş resmî değerlendirme istemini, paket
SHA-256 değerini, kurulum ve kaldırma talimatlarını, sunum metnini, beklenen
davranış kontrol noktalarını ve yedek kaydı içerecektir.

Yayın kapıları ve ikinci demo ölçütleri için [kurumsal teslimat planına](../../ENTERPRISE-DEMO-PLAN.md)
bakın.

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/investment-committee/investment-committee-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/investment-committee/investment-committee-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/investment-committee/investment-committee-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/investment-committee/investment-committee-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/investment-committee/investment-committee-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.
