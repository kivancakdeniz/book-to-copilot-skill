# Kurumsal karar skill kataloğu

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

## 12 skill

<div class="grid cards" markdown>

-   **[KVKK aydınlatma kontrolü](kvkk-aydinlatma-kontrolu.md)**

    <span class="bts-skill-kicker">Veri koruma</span>

    Aydınlatma, rıza ve aktarım boşluklarını insan yayın kapısına bağlar.

    <span class="bts-score bts-score--control">LLM 10</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[ETK/IYS ileti kararı](etk-iys-ileti-karari.md)**

    <span class="bts-skill-kicker">Ticari elektronik ileti</span>

    Kampanya kitlesini kişi-kanal kanıtı ve bastırma kapısıyla inceler.

    <span class="bts-score bts-score--control">LLM 20</span> <span class="bts-score bts-score--skill">Skill 80</span>

-   **[İndirimli fiyat denetimi](indirimli-fiyat-denetimi.md)**

    <span class="bts-skill-kicker">E-ticaret ve tüketici hukuku</span>

    Fiyat geçmişi ile kampanya iddiasını izlenebilir bir yayın kararında buluşturur.

    <span class="bts-score bts-score--control">LLM 20</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[MASAK müşteri kabul](masak-musteri-kabul.md)**

    <span class="bts-skill-kicker">Finansal suçlarla mücadele</span>

    Kimlik, nihai faydalanıcı ve fon kaynağı boşluklarını insan incelemesine yönlendirir.

    <span class="bts-score bts-score--control">LLM 20</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[BDDK uzaktan müşteri edinimi](bddk-uzaktan-musteri-edinimi.md)**

    <span class="bts-skill-kicker">Bankacılık</span>

    Uzaktan edinim akışını kanıt, kontrol ve canlıya geçiş kapılarıyla sınar.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 80</span>

-   **[Rekabet birleşme bildirimi](rekabet-birlesme-bildirimi.md)**

    <span class="bts-skill-kicker">Birleşme ve devralmalar</span>

    Ön hesaplama göstergelerini hukuki bildirim kararı ve kapanış kapısından ayırır.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[İSG risk değerlendirmesi: değişiklikten devreye alma kapısına](isg-risk-degerlendirme.md)**

    <span class="bts-skill-kicker">İş sağlığı ve güvenliği</span>

    Değişiklik risklerini katılım, kontrol ve devreye alma kanıtlarıyla görünür kılar.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[TİTCK ilaç tanıtımı: hedef kitle ve yayın kapısı](titck-ilac-tanitimi.md)**

    <span class="bts-skill-kicker">İlaç ve sağlık iletişimi</span>

    Ürün statüsü, hedef kitle ve kanal erişimini insan yayın incelemesine bağlar.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[Kripto ödeme kapısı](kripto-odeme-kapisi.md)**

    <span class="bts-skill-kicker">Ödeme hizmetleri ve kripto varlıklar</span>

    Kripto işlevinin ödeme akışındaki rolünü ürün sınırı ve lansman kapısıyla inceler.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[BTK haberleşme verisi](btk-haberlesme-verisi.md)**

    <span class="bts-skill-kicker">Telekom ve mahremiyet</span>

    Konum ve trafik verisi kullanımını amaç, rıza ve saklama kapılarıyla sınırlar.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 80</span>

-   **[Yatırım komitesi değerlendirmesi](investment-committee.md)**

    <span class="bts-skill-kicker">Sermaye tahsisi</span>

    Sermaye brifingini kapılı ve kanıt atıflı bir komite karar kartına dönüştürür.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[Pazarlama iddiaları incelemesi](marketing-claims-review.md)**

    <span class="bts-skill-kicker">Pazarlama ve reklam uyumu</span>

    Reklam iddialarını dayanak, ifşa ve yayın kontrolleriyle sınar.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

</div>


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