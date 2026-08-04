# İndirimli fiyat denetimi

[English](../../skills/indirimli-fiyat-denetimi.md)

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
| Problem | Sağlanan fiyat geçmişi ile kampanya kreatifinin referans fiyat/oran uyumunu denetlemek |
| Baseline | En düşük fiyat 800 TRY, satış 600 TRY, sağlanan sonuç %25; kreatif 1.000 TRY ve %40 |
| Beklenen sınıf | `revise-price-claim` |
| Beklenen seçenek | `advertise-25-percent` |
| İnsan kararı | E-commerce Owner + Pricing Owner + Compliance; istisnada Legal |

## Nitel etki

Demo, kreatif onayındaki yoruma dayalı kontrolü tekrarlanabilir bir kanıt, kural, karar ve yayın kapısı akışına dönüştürür. Beklenen etki daha hızlı insan incelemesi, daha görünür fiyat geçmişi bağı ve daha az kanıtsız yüzde iddiasıdır; üretim performansı veya hukuki uyum garantisi değildir.

## Kaynak ve güvenlik

Kamusal yöntem kaynağı Ticaret Bakanlığı'nın 2024 fiyat reklamları kılavuz sayfasıdır. Paket resmi içeriği yeniden dağıtmaz; yalnız resmi URL, yayıncı, 2026-08-04 alınma tarihi ve SHA-256 metadata'sını taşır. Karar sınıfları ve seçenekler MIT lisanslı sentetik politikadan gelir. Kaynak metni talimat olarak çalıştırılmaz, uzun resmi alıntı yapılmaz ve gerçek müşteri ya da ticari sır verisi kullanılmaz.

## İnsan sınırları

Bu beceri hukuki görüş değildir. İnsanlar karar verir; kampanyayı onaylamaz, yayına almaz, fiyat değiştirmez veya başka otonom işlem yapmaz. Eksik fiyat ve oranları hesaplamaz. Legal yalnız belgelenmiş istisna veya hukuki yorum ihtiyacında devreye girer.

## 12 kilitli senaryo

| Kimlik | Odak | Beklenen sınıf | Beklenen seçenek |
|---|---|---|---|
| FYT-01 | Baseline kreatif uyuşmazlığı | `revise-price-claim` | `advertise-25-percent` |
| FYT-02 | Uyumlu yüzde 25 kreatifi | `approve` | `advertise-25-percent` |
| FYT-03 | Eksik fiyat geçmişi | `hold-for-price-history` | `no-promotion` |
| FYT-04 | Belirsiz karşılaştırma penceresi | `hold-for-price-history` | `no-promotion` |
| FYT-05 | Sağlanan hesap sonucu yok | `hold-for-price-history` | `no-promotion` |
| FYT-06 | Çelişen geçmiş sonuçları | `hold-for-price-history` | `no-promotion` |
| FYT-07 | Doğru oran, belirsiz kreatif | `revise-price-claim` | `advertise-25-percent` |
| FYT-08 | Belgelenmiş istisna | `escalate-consumer-law` | `no-promotion` |
| FYT-09 | Düzeltmenin reddi | `reject` | `no-promotion` |
| FYT-10 | Canlı fiyat uyuşmazlığı | `revise-price-claim` | `advertise-25-percent` |
| FYT-11 | İzleme sorumluluğunun reddi | `reject` | `no-promotion` |
| FYT-12 | Karşılaştırmalı iddianın kaldırılması | `approve` | `no-promotion` |

## İndirmeler

- [Cowork skill](../../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-cowork.skill)
- [GitHub Copilot for VS Code ZIP](../../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/turkiye-enterprise/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-classic-setup.zip)

Classic setup ZIP doğrudan içe aktarım paketi değildir; dosyalar Copilot Studio classic ortamında insan tarafından uygulanacak kurulum malzemeleridir.