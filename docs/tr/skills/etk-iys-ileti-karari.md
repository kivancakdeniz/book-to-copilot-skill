# ETK/IYS ileti kararı

[English](../../skills/etk-iys-ileti-karari.md)

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

CRM ekibi, güncel rıza/IYS kanıtı sunmadan 48.000 eski perakende müşterisine
indirim SMS'i gönderebilir mi?

## Başlangıç olguları

- Mesaj indirim ve satın alma çağrısı içeriyor; hizmet bildirimi değil.
- Güncel rıza veya IYS durum anlık görüntüsü sağlanmadı.
- Kişi ve SMS kanalı düzeyinde kanıt listesi yok.
- Ret/çıkış ifadesi var.
- İstisna, bastırma kapısı ve insan onayını destekleyen kayıt sağlanmadı.

## Beklenen karar

Başlangıç için karar `do-not-send`, seçenek `suppress-unverified-audience` olur.
İnsan rotası CRM Owner + Compliance + Legal'dır.

## İş etkisi

Demo, kampanya ekibinin kitle büyüklüğünden önce ileti amacı, kişi-kanal kanıtı,
ret kontrolü, istisna olgusu ve bastırma kapısını incelemesini sağlar. Etki
nitelikseldir: doğrulanmamış kitlenin görünür olması, insan karar rotasının
netleşmesi ve kampanya incelemelerinin aynı sözleşmeyle tekrarlanması beklenir.
Ölçülmüş ROI veya finansal kazanım iddiası yoktur.

## Kaynak ve lisans sınırı

6563 sayılı ETK ile Ticari İletişim Yönetmeliği kamuya açık resmî yöntemdir.
Manifest, 2026-08-04 tarihinde alınan resmî URL, yayıncı ve SHA-256 metadatasını
taşır; resmî dosyalar `metadata-only` yaklaşımıyla yeniden dağıtılmaz ve uzun
pasajlar kopyalanmaz. Sentetik politika ve vaka MIT lisanslıdır. Güncellik,
yeniden kullanım ve uygulama insan Legal tarafından doğrulanır.

## Güvenlik ve insan sınırı

Bu içerik hukuki tavsiye veya nihai hukuki sonuç değildir. İnsan Legal/Compliance
kararın sahibidir. Skill yalnız analiz, eksik belirleme ve yönlendirme yapar;
mesaj gönderme, IYS kaydı değiştirme, kitle bastırma, kampanya başlatma/durdurma
veya başka otonom eylem yapmaz. Gerçek müşteri listesi demo girdisi olarak
kullanılmamalıdır.

## 12 senaryo durumu

On iki benzersiz senaryo cevap anahtarlarıyla kilitlenmiş ve 14 puanlık rubriğe
bağlanmıştır. Senaryolar bu makalede çalıştırılmış veya sonuçlandırılmış olarak
sunulmaz; biçimsel yürütme ve insan incelemesi beklenmektedir.

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-vscode.zip)
- [Scout ZIP](../../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/turkiye-enterprise/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.