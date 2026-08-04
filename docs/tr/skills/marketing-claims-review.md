# Pazarlama İddiaları İncelemesi Copilot

[English](../../skills/marketing-claims-review.md)

## Karar

Kurgusal Lumena Home Energy, Lumena Sense akıllı HVAC enerji kontrol cihazı için
ABD dijital lansman kampanyasını sunulduğu haliyle yayımlayabilir mi, yoksa
kanıtla sınırlandırılmış bir revizyonu mu onaylamalı?

Kilitli temel cevap, `evidence-bounded-campaign` ile `approve-with-edits`'tir.
Özgün kampanya sunulduğu haliyle onaylanmaz. Bu bir hukuki tavsiye veya nihai
hukuki sonuç değil, yönetişim danışmanlığı demosudur. Legal, Compliance,
Marketing ve Product Evidence insan inceleyicileri tüm yetkiyi korur; Copilot
onay veremez veya yayın yapamaz.

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 9 | 9 / 9 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

Host: Microsoft 365 Copilot Cowork · Model: Claude Opus 4.8 · Tarih: 2026-08-04 · Senaryo: `MC-01`

[Kontrol yanıtı](../../assets/skills/marketing-claims-review/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/marketing-claims-review/outputs/treatment-auto-1.txt) · [Skor kartı](../../assets/skills/marketing-claims-review/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/marketing-claims-review
```

Kontrol çalıştırması 9 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 9 tanesine atıf yaptı. Tam karar sınıfını (`approve-with-edits`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/marketing-claims-review/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Advertising and Marketing on the Internet: Rules of the Road](https://www.ftc.gov/system/files/ftc_gov/pdf/bus28-rulesroad-2023_508.pdf) — U.S. Federal Trade Commission |
| Resmî kaynak (yalnız metadata) | [.com Disclosures: How to Make Effective Disclosures in Digital Advertising](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf) — U.S. Federal Trade Commission |
| Resmî kaynak (yalnız metadata) | [Guides Concerning the Use of Endorsements and Testimonials in Advertising (16 CFR Part 255)](https://www.ecfr.gov/api/versioner/v1/full/2023-07-26/title-16.xml?part=255) — Electronic Code of Federal Regulations |
| Kamuya açık yöntem özeti | `demos/marketing-claims-review/skill/public-method.md` |
| Sentetik şirket politikası | `demos/marketing-claims-review/sources/company-policy.md` |
| Sentetik vaka | `demos/marketing-claims-review/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/marketing-claims-review/evaluation/` |
| Taşınabilir skill | `demos/marketing-claims-review/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Kanıt durumu

| Varlık | Durum |
|---|---|
| Altı dosyalı Cowork skill paket tanımı | Hazır; deterministik paketleme test kapsamında |
| Üç kaynaklı sentetik vaka paketi | Hazır ve izleniyor |
| Üç kaynaklı FTC yöntem manifesti | Hazır; kamusal anlık görüntüler izlenmiyor |
| On iki kilitli senaryo ve 14 puanlık rubrik | Hazır |
| Cevap anahtarsız deterministik senaryo oluşturucusu | Hazır; 12 girdi hash'i kilitli |
| Sunucu kurulumu ve beklenen kontrol noktaları | Hazır |
| Oturum açılmış Cowork kontrolü | Kaydedildi; ham ilk yanıt korundu |
| Nihai paket yüklemesi | Customize içinde `marketing-claims-review-copilot-3` olarak kaydedildi |
| Oturum açılmış nihai paket uygulaması | Auto ve Claude Opus 4.8 ile kaydedildi; ilk yanıtlar korundu |
| Sabit çalışma zamanlı resmî kıyaslama ve kör insan incelemesi | Beklemede |

Cowork UX seti artık yalnız özet kullanan temiz bir kontrol, model eşleşmiş bir
Claude Opus 4.8 uygulaması ve ayrı bir Auto uygulaması içerir. Dört operasyonel
deneme dışlanmış olarak kaydedildi. Bunlar nedensel veya resmî kıyaslama kanıtı
değil, UX gözlemleridir.

Cowork paket SHA-256:
`35e0642d1fdf63f3698419d5b014acab4755d9c50c8dad812d459ac86f902e9b`.

## Temiz Cowork kontrol gözlemi

Korunan kontrol yalnızca cevap anahtarı içermeyen kurgusal kampanya özetini
kullandı. Kanıtla sınırlandırılmış kampanyayı seçti ve birincil iddia sorunlarının
tamamını buldu. İzin verilen `approve-with-edits` sınıfını adlandırmadı ve MCS
yetki matrisine erişimi yoktu. Adlandırılmış uyumluluk istisnalarını, yalnız özet
bulunan bağlamında mevcut değil olarak doğru ele aldı. Ham yanıt düzeltilmeden
korundu.

[Tam boyutlu kontrol kaydını aç](../../assets/skills/marketing-claims-review/screenshots/01-control-1-1920x1080.png)

![Çalışma alanında özel skill bulunmayan, yalnız özet kullanan Cowork kontrol yanıtı](../../assets/skills/marketing-claims-review/screenshots/01-control-1-1920x1080.png)

[Kontrol 1 ham yanıtı](../../assets/skills/marketing-claims-review/outputs/control-1.txt) ·
[Koşu manifesti](../../assets/skills/marketing-claims-review/metadata/cowork-runs.json)

Manifest yolları, demo kaynak ağacındaki özgün manifest klasörüne göredir.
Yayımlanmış ham varlıklar için yukarıdaki ve aşağıdaki sayfa bağlantılarını
kullanın.

## Skill destekli Cowork gözlemleri

Skill destekli iki ilk yanıt da `approve-with-edits` seçti, kanıtla
sınırlandırılmış kampanyayı önerdi, yedi iddia/açıklama satırının tamamını
envantere aldı, MCS yetki ve yayın kontrollerini uyguladı ve FTC yöntemini
sentetik politikadan ayrı tuttu. İkisi de istenen 700 sözcük sınırını aştı.

[Tam boyutlu Claude uygulama kaydını aç](../../assets/skills/marketing-claims-review/screenshots/04-treatment-claude-1-1920x1080.png)

![Pazarlama İddiaları İncelemesi skill'i yüklenmiş Claude Opus 4.8 uygulaması](../../assets/skills/marketing-claims-review/screenshots/04-treatment-claude-1-1920x1080.png)

[Claude uygulama ham yanıtı](../../assets/skills/marketing-claims-review/outputs/treatment-claude-1.txt) ·
[Auto uygulama ham yanıtı](../../assets/skills/marketing-claims-review/outputs/treatment-auto-1.txt) ·
[Ön inceleme kaydı](../../assets/skills/marketing-claims-review/metadata/preliminary-review.json)

!!! warning "Ön rubrik provası, resmî kıyaslama değildir"

    Muhafazakâr, kör ve yapay zekâ destekli bir prova; model eşleşmiş Claude
    uygulamasına cezasız 12/14, yalnız özet kullanan kontrole bir ceza sonrası
    7 puan verdi. Ayrı Auto uygulaması da 12/14 aldı. İki uygulama da istenen
    700 sözcük sınırını aştı.
    İnsan incelemesi tamamlanmadı. İstemler açık skill çağrısı nedeniyle
    farklıdır, Cowork çalışma zamanı kontrolleri tam sabitlenmemiştir ve 12
    senaryodan yalnız biri çalıştırılmıştır. Bu sayıları nedensel artış,
    istatistiksel tahmin veya bağımsız doğrulanmış performans olarak yorumlamayın.

## Kamusal yöntem kaynakları

- [Advertising and Marketing on the Internet: Rules of the Road](https://www.ftc.gov/system/files/ftc_gov/pdf/bus28-rulesroad-2023_508.pdf),
  sabitlenmiş FTC URL'sinde sunulan 16 sayfalık PDF.
- [.com Disclosures: How to Make Effective Disclosures in Digital Advertising](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf),
  53 sayfa, Mart 2013.
- [Guides Concerning the Use of Endorsements and Testimonials in Advertising, 16 CFR Part 255](https://www.ecfr.gov/api/versioner/v1/full/2023-07-26/title-16.xml?part=255),
    tarih olarak 2023-07-26'ya sabitlenmiş eCFR XML anlık görüntüsü.

Kesin anlık görüntü SHA-256 değerleri kaynak manifestine kaydedilmiştir. Kamusal PDF
ve XML dosyaları commit edilmez; skill uzun bölümleri kopyalamak yerine kısa yöntem
kuralları derler. ABD federal hükûmet eserleri 17 U.S.C. 105 kapsamında genel
olarak telif hakkına tabi değildir, ancak üçüncü taraf malzeme ve varlıklar ayrıca
kontrol edilmelidir.

Tüm Lumena adları, ürünleri, politikaları, kişileri, kaynakları, ödemeleri,
sonuçları ve kampanya olguları kurgusal sentetik veridir.

## Temel iddialar

| İddia | Sağlanan kanıtın uyumu | Gerekli temel hüküm |
|---|---|---|
| Ev enerji faturalarında %30 tasarruf | Pilot faturaları değil, medyan %12 HVAC elektrik azalmasını ölçtü | Kesin ve sınırlandırılmış pilot ifadesiyle değiştir |
| Altı ayda maliyetini çıkarır | Geri ödeme ölçülmedi | Kaldır |
| Her evde çalışır | Bilinen ekipman istisnaları ve kurulum gereksinimleri var | Kaldır; uyumluluğu CTA yakınında göster |
| Bağımsız pilot tasarrufu kanıtlıyor | Lumena sponsor oldu ve analiz etti; bağımsız tekrar yok | Şirket sponsorluğunu belirt; bağımsızlık iddiasını kaldır |
| Ava Reed: faturada %35 azalma | Gösterge paneli 8 haftada %18 HVAC elektrik azalması gösterdi; tipik sonuç analizi yok | Performans tanıklığını kaldır |
| Daraltılmış sınırdan sonra `#LumenaPartner` | 5.000 USD ödendi ve ücretsiz cihaz verildi | Açık ödeme/cihaz açıklamasını ilk sıraya ve içeriğe koy |
| Sayfa altı `Results vary` dipnotu | Uzak niteleme, MCS-2.1 altında çelişkili başlıkları düzeltemez | Yakın, kaçınılmaz ve çelişkisiz açıklamayla değiştir |

Kanıtla sınırlandırılmış seçenek; istisnai bir kişisel sonucu yayın iddiasına
dönüştürmeden kesin popülasyonu, metriği, süreyi, başlangıç değerini, sonucu, sponsorluğu,
uyumluluk koşullarını ve maddi bağlantı olgularını korur. Yayından önce Legal,
Compliance, Marketing Director ve Product Evidence Owner katılımı gerekir.

## Değerlendirme planı

Oturum açılmış Cowork gösterimi, aynı sentetik özet ile yeni bir kontrol
konuşmasından ve skill'in açıkça çağrıldığı yeni bir konuşmadan ilk yanıtları
koruyacaktır. Bu karşılaştırma yalnız UX kanıtıdır: otomatik keşif ve çalışma
ortamı çalışma zamanı sabitlenemeyebileceği için açık çağrı bir uygulama tercihidir.

Resmî kıyaslama ayrıdır. Tam olarak 12 kilitli senaryo, bir izin verilen karar
sınıfı, bir kampanya seçeneği, azami 14 pozitif puan, tekrarlanabilir cezalar,
beyan edilmiş model ve parametreler, rastgeleleştirilmiş sunum ve kör insan
incelemesi kullanır. Toplam skoru, desteksiz iddia sayısını, doğru çekimserliği,
yanıt sözcüklerini ve kanıt kaynaklarını yalnız yürütme ve inceleme sonrasında
raporlar.

Yayın kanıtı; ham ilk yanıtları, koşu koşullarını, paket hash'ini, senaryo
sürümünü, puanlama kayıtlarını, dışlamaları, sınırlamaları ve başarısız vakaları
içerir. Ön prova metrikleri bekleyen resmî kıyaslamadan görünür biçimde ayrı
tutulur.

## İnsan sınırı

Skill iddiaları envantere alabilir, kanıtı eşleyebilir, gerekli düzeltmeleri
taslaklaştırabilir, eksik olguları belirleyebilir ve inceleyicilere yönlendirebilir.
Nihai hukuki karar vermez; kampanyanın yayınına, yayımlanmasına, durdurulmasına,
düzeltilmesine, geri çekilmesine veya izleme eylemlerine yetki vermez.

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/marketing-claims-review/marketing-claims-review-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.
