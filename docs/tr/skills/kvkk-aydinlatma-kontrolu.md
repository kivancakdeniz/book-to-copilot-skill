# KVKK aydınlatma kontrolü

[English](../../skills/kvkk-aydinlatma-kontrolu.md)

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


## Bir bakışta iş sorusu

Sentetik B2B SaaS potansiyel müşteri formu, mevcut aydınlatma taslağı ve birleşik
pazarlama rızasıyla yayına çıkabilir mi?

## Başlangıç olguları

- Form ad, kurumsal e-posta, telefon, IP ve kampanya kaynağı topluyor.
- Bir yurt dışı işleyen kullanılıyor; aktarım yolu ve güvence ayrıntıları yok.
- Taslak veri sorumlusunu, amaçları ve yöntemi gösteriyor.
- Alıcı grupları, aktarım bağlamı, hukuki sebep eşlemesi ve ilgili kişi
  hakları/iletişim yolu eksik.
- Pazarlama rızası aydınlatma kabulüne bağlanmış.

## Beklenen karar

Başlangıç için karar `revise-before-launch`, seçenek
`separate-notice-and-consent` olur. İnsan rotası Privacy Counsel + Data
Protection/Compliance + Product Owner'dır.

## İş etkisi

Demo, ürün ekibinin “metin var mı?” kontrolünü veri envanteri, aydınlatma
tamamlığı, rıza ayrımı, aktarım kanıtı ve imzalı yayın kapısıyla izlenebilir bir
karara dönüştürür. Etki nitelikseldir: eksiklerin daha erken görünmesi, karar
sahipliğinin netleşmesi ve değerlendirmelerin aynı sözleşmeyle tekrarlanması
beklenir. Ölçülmüş ROI veya finansal kazanım iddiası yoktur.

## Kaynak ve lisans sınırı

6698 sayılı KVKK ile Aydınlatma Tebliği kamuya açık resmî yöntemdir. Manifest,
2026-08-04 tarihinde alınan resmî URL, yayıncı ve SHA-256 metadatasını taşır;
resmî dosyalar `metadata-only` yaklaşımıyla yeniden dağıtılmaz ve uzun pasajlar
kopyalanmaz. Sentetik politika ve vaka MIT lisanslıdır. Güncellik, yeniden
kullanım ve uygulama insan Legal tarafından doğrulanır.

## Güvenlik ve insan sınırı

Bu içerik hukuki tavsiye veya nihai hukuki sonuç değildir. İnsan Legal/Compliance
kararın sahibidir. Skill yalnız analiz, eksik belirleme ve yönlendirme yapar;
yayına alma, rıza toplama, veri aktarma, kayıt değiştirme veya başka otonom eylem
yapmaz. Gerçek kişisel veri demo girdisi olarak kullanılmamalıdır.

## 12 senaryo durumu

On iki benzersiz senaryo cevap anahtarlarıyla kilitlenmiş ve 14 puanlık rubriğe
bağlanmıştır. Senaryolar bu makalede çalıştırılmış veya sonuçlandırılmış olarak
sunulmaz; biçimsel yürütme ve insan incelemesi beklenmektedir.

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-vscode.zip)
- [Scout ZIP](../../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/turkiye-enterprise/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.