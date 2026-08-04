# Kurumsal karar skill kataloğu

[English](../../skills/index.md)

Bu katalog, tek bir yayın fabrikasıyla üretilen 12 kurumsal karar skill'ini
listeler. Her skill 12 kilitli senaryo, 14 puanlık rubrik, sentetik şirket
politikası ve resmî kaynak metadatası içerir.

Her skill için aynı vaka iki kez yanıtlandı: bir kez skill olmadan, bir kez
skill kurulu. Deterministik iz puanı ortalaması yalnız LLM'de 33/100,
LLM + skill'de 95/100 oldu. Politika kuralı atfı 12 kontrol
çalıştırmasının hepsinde sıfırdı. Bu bir üretim performansı, ROI veya uygunluk
iddiası değildir.

Yayın, beş host biçiminde 60 indirilebilir paket içerir. Paketler
deterministik üretilir ve temiz yeniden derlemede byte-identical doğrulanır.

[SHA256SUMS](../../downloads/skills/SHA256SUMS) ·
[Üçüncü taraf bildirimleri](../../downloads/skills/THIRD_PARTY_NOTICES.md)

## Katalog

| Skill | Alan | Hedef ekip | Tek cümlede değer | Yalnız LLM | LLM + skill |
|---|---|---|---|---|---|
| [KVKK aydınlatma kontrolü](kvkk-aydinlatma-kontrolu.md) | Veri koruma | Privacy, Compliance ve ürün ekipleri | Aydınlatma, rıza ve aktarım boşluklarını insan yayın kapısına bağlar. | 10/100 | 100/100 |
| [ETK/IYS ileti kararı](etk-iys-ileti-karari.md) | Ticari elektronik ileti | CRM, Compliance ve Legal ekipleri | Kampanya kitlesini kişi-kanal kanıtı ve bastırma kapısıyla inceler. | 20/100 | 80/100 |
| [İndirimli fiyat denetimi](indirimli-fiyat-denetimi.md) | E-ticaret ve tüketici hukuku | E-ticaret, fiyatlandırma ve Compliance ekipleri | Fiyat geçmişi ile kampanya iddiasını izlenebilir bir yayın kararında buluşturur. | 20/100 | 100/100 |
| [MASAK müşteri kabul](masak-musteri-kabul.md) | Finansal suçlarla mücadele | AML, Compliance ve müşteri kabul ekipleri | Kimlik, nihai faydalanıcı ve fon kaynağı boşluklarını insan incelemesine yönlendirir. | 20/100 | 100/100 |
| [BDDK uzaktan müşteri edinimi](bddk-uzaktan-musteri-edinimi.md) | Bankacılık | Dijital bankacılık, güvenlik, Uyum ve Hukuk ekipleri | Uzaktan edinim akışını kanıt, kontrol ve canlıya geçiş kapılarıyla sınar. | 40/100 | 80/100 |
| [Rekabet birleşme bildirimi](rekabet-birlesme-bildirimi.md) | Birleşme ve devralmalar | M&A, Finans ve Rekabet Hukuku ekipleri | Ön hesaplama göstergelerini hukuki bildirim kararı ve kapanış kapısından ayırır. | 40/100 | 100/100 |
| [İSG risk değerlendirmesi: değişiklikten devreye alma kapısına](isg-risk-degerlendirme.md) | İş sağlığı ve güvenliği | İSG, operasyon, bakım ve mühendislik ekipleri | Değişiklik risklerini katılım, kontrol ve devreye alma kanıtlarıyla görünür kılar. | 40/100 | 100/100 |
| [TİTCK ilaç tanıtımı: hedef kitle ve yayın kapısı](titck-ilac-tanitimi.md) | İlaç ve sağlık iletişimi | Medical, Regulatory, Legal ve pazarlama ekipleri | Ürün statüsü, hedef kitle ve kanal erişimini insan yayın incelemesine bağlar. | 40/100 | 100/100 |
| [Kripto ödeme kapısı](kripto-odeme-kapisi.md) | Ödeme hizmetleri ve kripto varlıklar | Payments, Compliance, Legal ve ürün ekipleri | Kripto işlevinin ödeme akışındaki rolünü ürün sınırı ve lansman kapısıyla inceler. | 40/100 | 100/100 |
| [BTK haberleşme verisi](btk-haberlesme-verisi.md) | Telekom ve mahremiyet | Telekom Compliance, Privacy, DPO ve CRM ekipleri | Konum ve trafik verisi kullanımını amaç, rıza ve saklama kapılarıyla sınırlar. | 40/100 | 80/100 |
| [Yatırım komitesi değerlendirmesi](investment-committee.md) | Sermaye tahsisi | CFO, COO, CIO ve yatırım komitesi üyeleri | Sermaye brifingini kapılı ve kanıt atıflı bir komite karar kartına dönüştürür. | 40/100 | 100/100 |
| [Pazarlama iddiaları incelemesi](marketing-claims-review.md) | Pazarlama ve reklam uyumu | Pazarlama, Legal ve Compliance ekipleri | Reklam iddialarını dayanak, ifşa ve yayın kontrolleriyle sınar. | 40/100 | 100/100 |

## Kaynak ve lisans sınırı

Resmî mevzuat, kılavuz ve yöntem kaynakları paketlere tam içerik olarak alınmaz.
Yayın yalnız başlık, resmî URL, yayıncı, erişim tarihi, SHA-256 ve yeniden
kullanım uyarısını üst veri olarak taşır. Güncellik, kapsam ve yeniden kullanım
koşulları resmî kaynaktan insan tarafından doğrulanır. Şirket politikaları,
vakalar ve operasyonel örnekler sentetiktir ve manifestte belirtilen MIT sınırı
içinde dağıtılır. Skill'ler hukuki, tıbbi veya mühendislik görüşü vermez; nihai
karar ve bütün sistem eylemleri yetkili insanlarda kalır.

## Çalışma ortamı paketleri

| Paket | Kök sözleşmesi | Kullanım |
|---|---|---|
| Cowork `.skill` | `SKILL.md` + beş eşlikçi dosya | Microsoft 365 Copilot Cowork özel skill yüklemesi |
| Copilot VS Code ZIP | `.github/skills/<slug>/` + `INSTALL.md` | Depo düzeyinde GitHub Copilot Agent Skill |
| Scout ZIP | `.copilot/skills/<slug>/` + `INSTALL.md` | Scout/Copilot skill dizini kurulumu |
| Copilot Studio GitHub harness ZIP | Kökte `SKILL.md`, eşlikçi dosyalar ve `INSTALL.md` | GitHub Copilot harness ön izlemesinde mevcut skill ZIP yüklemesi |
| Copilot Studio Classic kurulum ZIP'i | `README.md`, `instructions.md`, `knowledge/`, manifest | Classic ortamında yönlendirmeli manuel kurulum |

Copilot Studio GitHub harness paketi, resmî mevcut-skill ZIP sözleşmesine göre
doğrudan yüklenebilen skill paketidir. Classic kurulum paketi ise doğrudan ajan
veya çözüm içe aktarma paketi değildir: talimatlar ve bilgi dosyaları insan
tarafından hedef ortama uygulanır. Her iki durumda da MCP sunucuları, araçlar,
bağlantılar, kimlik, izin ve yayımlama ayarları ayrıca yapılandırılır.