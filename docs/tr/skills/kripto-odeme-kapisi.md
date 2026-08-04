# Kripto ödeme kapısı

[English](../../skills/kripto-odeme-kapisi.md)

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


## Bir bakışta

| Alan | Değer |
|---|---|
| Problem | USDT'nin satıcı alımını doğrudan kapattığı checkout akışının ürün sınırını incelemek |
| Baseline | Kripto doğrudan ödeme işlevinde; ödeme hizmeti aracısı akışta; lansman talep ediliyor |
| Beklenen sınıf | `reject-payment-flow` |
| Beklenen seçenek | `remove-crypto-checkout` |
| İnsan kararı | Payments Counsel + Compliance + Product |

## İş etkisi

Demo, hızlı lansman baskısı altındaki dağınık ürün tartışmasını izlenebilir bir
varlık, işlev, aracı, mutabakat, karar ve lansman kapısı kaydına dönüştürür.
Beklenen iş etkisi daha erken ürün sınırı tespiti, daha az geç aşama yeniden
çalışma ve insan karar sahiplerine daha tutarlı kanıt paketidir. Üretim sonucu,
mevzuata uyum veya hukuki yeterlilik garantisi değildir.

## Kaynak ve güvenlik

Kamusal yöntem kaynağı TCMB'nin T.C. Resmî Gazete'de yayımlanan düzenlemesidir.
Paket resmi içeriği yeniden dağıtmaz; yalnız resmi URL, yayıncı, 2026-08-04
erişim tarihi, SHA-256 ve yeniden kullanım uyarısı taşır. Skill kısa ve atıflı
yöntem özeti kullanır; mevzuat metnini kopyalamaz. Karar sınıfları ve seçenekler
MIT lisanslı sentetik Kurgusal Ödeme politikasından gelir.

## İnsan ve kapsam sınırı

Bu skill hukuki tavsiye değildir. Payments Counsel, Compliance ve Product karar
verir. Copilot onay, lansman, ödeme, transfer, ürün değişikliği veya durdurma
yapmaz. Sağlanan checkout akışının ötesinde yatırım ya da transfer hukukuna
ilişkin görüş vermez.

## 12 kilitli senaryo

| Kimlik | Odak | Beklenen sınıf | Beklenen seçenek |
|---|---|---|---|
| KRP-01 | Doğrudan USDT satıcı ödemesi | `reject-payment-flow` | `remove-crypto-checkout` |
| KRP-02 | Ödeme dışı piyasa bilgi ekranı | `approve-nonpayment-service` | `launch-current-flow` |
| KRP-03 | Checkout'tan kriptonun çıkarılması | `revise-product-boundary` | `remove-crypto-checkout` |
| KRP-04 | Eksik mutabakat/dönüşüm | `hold-for-flow-evidence` | `remove-crypto-checkout` |
| KRP-05 | Bilinmeyen aracı rolü | `hold-for-flow-evidence` | `redesign-nonpayment-service` |
| KRP-06 | Satıcı alımından ayrık transfer | `escalate-payments-counsel` | `redesign-nonpayment-service` |
| KRP-07 | Statik eğitim içeriği | `approve-nonpayment-service` | `redesign-nonpayment-service` |
| KRP-08 | Aracısız doğrudan satıcı transferi | `reject-payment-flow` | `remove-crypto-checkout` |
| KRP-09 | Yatırım uygunluğu görüşü | `escalate-payments-counsel` | `redesign-nonpayment-service` |
| KRP-10 | Çelişkili akış sürümleri | `hold-for-flow-evidence` | `remove-crypto-checkout` |
| KRP-11 | TRY checkout ve ayrık analiz | `revise-product-boundary` | `redesign-nonpayment-service` |
| KRP-12 | Ödeme işlevinin yeniden eklenmesi | `reject-payment-flow` | `remove-crypto-checkout` |

## İndirmeler

- [Cowork skill](../../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-cowork.skill)
- [GitHub Copilot for VS Code ZIP](../../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/turkiye-enterprise/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-classic-setup.zip)

Classic setup ZIP doğrudan içe aktarım paketi değildir; dosyalar Copilot Studio
classic ortamında insan tarafından uygulanacak kurulum malzemeleridir.