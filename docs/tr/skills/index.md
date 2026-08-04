# Türkiye kurumsal karar skill kataloğu

[English](../../skills/index.md)

Bu katalog, Türkiye'deki on kurumsal karar senaryosu için ortak yayın üretim
hattına bağlı kaynak skill'leri listeler. On demo **kaynak doğrulamasına ve
değerlendirmeye hazırdır**: her biri 12 kilitli senaryo, 14 puanlık rubrik,
sentetik şirket politikası ve resmî kaynak üst verisi taşır. Bu on demo için
henüz Microsoft 365 Copilot Cowork A/B çalışması yapılmamıştır; katalog model
etkisi, üretim performansı veya ROI sonucu iddia etmez.

Beş çalışma ortamı biçiminde toplam 50 paket deterministik üretilmiş, temiz
yeniden derleme ile bayt düzeyinde özdeş olduğu doğrulanmış ve indirilebilir hale
getirilmiştir.

[SHA256SUMS](../../downloads/turkiye-enterprise/SHA256SUMS) ·
[Üçüncü taraf bildirimleri](../../downloads/turkiye-enterprise/THIRD_PARTY_NOTICES.md)

## Katalog

| Skill | Sektör | Hedef ekip | Tek cümlede değer | Durum |
|---|---|---|---|---|
| [KVKK aydınlatma kontrolü](kvkk-aydinlatma-kontrolu.md) | Veri koruma | Mahremiyet, Uyum, Ürün | Aydınlatma, rıza ve aktarım boşluklarını insan yayın kapısına bağlar. | Yayıma hazır |
| [ETK/IYS ileti kararı](etk-iys-ileti-karari.md) | Ticari elektronik ileti | CRM, Uyum, Hukuk | Kampanya kitlesini kişi-kanal kanıtı ve bastırma kapısıyla inceler. | Yayıma hazır |
| [İndirimli fiyat denetimi](indirimli-fiyat-denetimi.md) | E-ticaret ve tüketici hukuku | E-ticaret, Fiyatlandırma, Uyum | Fiyat geçmişi ile kampanya iddiasını izlenebilir bir yayın kararında buluşturur. | Yayıma hazır |
| [MASAK müşteri kabul](masak-musteri-kabul.md) | Finansal suçlarla mücadele | AML, Uyum, Müşteri Kabul | Kimlik, nihai faydalanıcı ve fon kaynağı boşluklarını insan incelemesine yönlendirir. | Yayıma hazır |
| [BDDK uzaktan müşteri edinimi](bddk-uzaktan-musteri-edinimi.md) | Bankacılık | Dijital Bankacılık, Güvenlik, Uyum, Hukuk | Uzaktan edinim akışını kanıt, kontrol ve canlıya geçiş kapılarıyla sınar. | Yayıma hazır |
| [Rekabet birleşme bildirimi](rekabet-birlesme-bildirimi.md) | Birleşme ve devralmalar | M&A, Finans, Rekabet Hukuku | Ön hesaplama göstergelerini hukuki bildirim kararı ve kapanış kapısından ayırır. | Yayıma hazır |
| [İSG risk değerlendirmesi](isg-risk-degerlendirme.md) | İş sağlığı ve güvenliği | İSG, Operasyon, Bakım, Mühendislik | Değişiklik risklerini katılım, kontrol ve devreye alma kanıtlarıyla görünür kılar. | Yayıma hazır |
| [TİTCK ilaç tanıtımı](titck-ilac-tanitimi.md) | İlaç ve sağlık iletişimi | Tıbbi, Ruhsatlandırma, Hukuk, Pazarlama | Ürün statüsü, hedef kitle ve kanal erişimini insan yayın incelemesine bağlar. | Yayıma hazır |
| [Kripto ödeme kapısı](kripto-odeme-kapisi.md) | Ödeme hizmetleri ve kripto varlıklar | Ödemeler, Uyum, Hukuk, Ürün | Kripto işlevinin ödeme akışındaki rolünü ürün sınırı ve lansman kapısıyla inceler. | Yayıma hazır |
| [BTK haberleşme verisi](btk-haberlesme-verisi.md) | Telekom ve mahremiyet | Telekom Uyumu, Mahremiyet, DPO, CRM | Konum ve trafik verisi kullanımını amaç, rıza ve saklama kapılarıyla sınırlar. | Yayıma hazır |

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