# İSG risk değerlendirmesi: değişiklikten devreye alma kapısına

[English](../../skills/isg-risk-degerlendirme.md)

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


Kurgusal bir depo, mevcut paletleme hücresine robot ekliyor. Risk değerlendirme
belgesi bu değişiklikten önce hazırlanmış; operatör ve bakım katılımı ile koruma
ve enerji izolasyonu kanıtları sağlanmamış. Buna rağmen üretim devreye alımı
isteniyor.

Bu Türkçe skill, cevabı otomatikleştirmek yerine insan kararını hazırlayan
izlenebilir bir inceleme üretir. Kilitli başlangıç sonucu `renew-assessment`,
önerilen seçenek `hold-commissioning`dır. Çıktı hukuki, mühendislik veya tıbbi
tavsiye ve mühendislik sertifikasyonu değildir. Copilot değerlendirmeyi kabul
etmez, kurul kararı vermez, ekipmanı devreye almaz veya çalışmayı durdurmaz;
yetkili insanlar karar verir ve eylemleri yürütür.

## Ne derler?

- Değişiklik mevcut risk değerlendirmesinin kapsamında mı?
- Operatör, bakım ve çalışan temsilinin katılımı kanıtlı mı?
- Koruma, erişim ve kilitleme/etiketleme kontrolleri doğrulanmış mı?
- Açık bulguların insan sahibi, aksiyonu ve tarihi var mı?
- Devreye alma kapısı ile olay ve değişiklik izleme tetikleri açık mı?

## Kaynak yaklaşımı

Kamusal yöntem kaynağı, T.C. Resmî Gazete'de yayımlanan
[İş Sağlığı ve Güvenliği Risk Değerlendirmesi Yönetmeliği](https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm)
sayfasıdır. Snapshot SHA-256 değeri
`a1ab5bfc1ea7c305393d7fa75f33d7a7debaf97fe3a6e46cc5d4dfb9276a31dc`,
erişim tarihi `2026-08-04`tür. Dış kaynak yalnızca metadata olarak dağıtılır;
skill uzun kopyalar yerine kısa ve atıflı yöntem özeti taşır. Güncel metin ve
yeniden kullanım koşulları insan tarafından resmî kaynaktan doğrulanır.

Şirket politikası, vaka, roller ve bütün operasyonel kayıtlar sentetiktir.

## İndir

- [Microsoft 365 Copilot Cowork skill](../../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [GitHub Copilot for VS Code paketi](../../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Scout paketi](../../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub harness paketi](../../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum paketi](../../downloads/turkiye-enterprise/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

!!! warning "Copilot Studio classic kurulumu"

    Classic paket doğrudan yüklenen, çalışma zamanını veya davranışı sabitleyen
    bir skill değildir. Yönlendirmeli manuel kurulum malzemesidir; talimatlar,
    bilgi kaynakları, bağlantılar, izinler ve yayımlama ayarları bir insan
    tarafından hedef ortamda ayrı ayrı incelenip yapılandırılmalıdır.

## Değerlendirme sözleşmesi

Demo tam 12 kilitli senaryo, beş karar sınıfı, üç seçenek ve her puan düzeyi
çapalanmış azami 14 puanlık rubrik kullanır. Donmuş prompt; kanıt, kişi, tarih,
eşik veya yetki uydurmayı ve sohbet dışı eser ya da operasyonel eylem üretmeyi
yasaklar.
