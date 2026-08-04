# Rekabet birleşme bildirimi

[English](../../skills/rekabet-birlesme-bildirimi.md)

## LLM only vs LLM + skill - beklenen fark

| Brief-only LLM | Derlenmiş skill |
|---|---|
| Serbest anlatım ve eksik kontrol listesi üretebilir | İzinli karar sınıfları, üç seçenek ve kural kimlikleriyle yapılandırır |
| Eksik kanıtı varsayım ile doldurma riski taşır | Eksik olguyu `bilinmiyor` tutar ve insan karar sahibine yönlendirir |
| Genel bir uyum veya operasyon önerisi verir | Yayın, canlıya geçiş, işlem veya kapanış kapısını açıkça uygular |

Bu tablo tasarım hipotezidir; bu 10 yeni skill için Cowork A/B henüz
çalıştırılmadı. Ölçülecek metrikler: exact karar/seçenek, gerekli kural geri
çağırma, desteksiz iddia sayısı, insan yetki sınırı ve yanıt uzunluğu. ROI veya
üretim performansı iddia edilmez.


Kurgusal bir devralmada kalıcı kontrol değişikliği sağlanmış, Finans precomputed
ciro testini `met` olarak vermiş, hedefin teknoloji teşebbüsü durumu ise
`unknown` kalmıştır. İmza yakındır ve kapanış istenmektedir. Bu portable Türkçe
skill, ciro hesaplamadan veya hukuki bildirim kararı vermeden insan danışman
rotasını ve kapanış kapısını yapılandırır.

## Bir bakışta iş etkisi

| Soru | Etki |
|---|---|
| Hangi karar gerekir? | Temel vakada `legal-notification-review`; güvenli seçenek `hold-closing` |
| Hangi risk görünür olur? | `met` göstergesinin hukuki sonuç sanılması, `unknown` teknoloji statüsü, eksik danışman yönlendirmesi ve sürüm takibi |
| Kim karar verir? | Rekabet Hukuku Danışmanı; Finans yalnız precomputed ciro sonucunun sahibidir |
| Skill ne kazandırır? | Aynı beş sınıf, üç seçenek, kural izlenebilirliği ve 14 puanlık ölçülebilir çıktı |
| Skill ne yapmaz? | Ciro/eşik hesabı, filing kararı, bildirim, yeniden yapılandırma, imza veya kapanış |

## Nasıl çalışır?

Skill, iki Rekabet Kurumu kılavuzunu metadata-only manifestle sınırlar; PDF'leri
yeniden dağıtmaz veya resmi metni kopyalamaz. Kısa kamu yöntemi sorularını
sentetik BKP-1.0 şirket politikasından ve sentetik RKB-2608 işlem olgularından
ayırır.

Temel vakada `met` yalnız Finans'ın önceden hesaplanmış göstergesidir. Bildirim
gerekliliğine ilişkin hukuki sonuç değildir. Teknoloji teşebbüsü durumu
`unknown` kalır, Rekabet Hukuku Danışmanı incelemesi beklenir ve kayıtlı kapanış
yönlendirmesi olmadan kapı açılmaz.

## İndirmeler

- [Cowork skill](../../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-cowork.skill)
- [GitHub Copilot for VS Code paketi](../../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-vscode.zip)
- [Scout paketi](../../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-scout.zip)
- [Copilot Studio GitHub harness paketi](../../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-github-harness.zip)
- [Copilot Studio Classic kurulum paketi](../../downloads/turkiye-enterprise/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-classic-setup.zip)

Copilot Studio Classic paketi doğrudan içe aktarılan bir çözüm değildir. Classic
ortamında insan tarafından uygulanacak kurulum dosyaları ve eşleme rehberi
sağlar; kurulum sonrası yetki, bağlantı ve yayın ayarları ayrıca doğrulanır.

## Değerlendirme

Demo, cevap anahtarı prompttan ayrı tam 12 kilitli senaryo ve her boyutu açık
ankrajlı 14 puanlık rubrik içerir. Puanlama doğru sınıf/seçenek kadar kontrol
olgusu envanterini, hesaplama yapmama disiplinini, teknoloji statüsü sınırını,
kaynak izlenebilirliğini, insan yetkisini ve kapanış kapısını ölçer.

Bu içerik eğitim ve yönetişim tasarımı içindir. Nihai hukuki karar ve bütün işlem
eylemleri yetkili insanlarda kalır.