# TİTCK ilaç tanıtımı: hedef kitle ve yayın kapısı

[English](../../skills/titck-ilac-tanitimi.md)

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


Kurgusal reçeteli bir ürün için tüketiciye açık Instagram kreatifi hazırlanıyor.
Kreatifte ürün adı, fayda ifadesi ve "Şimdi doktoruna sor" çağrısı var; hesap
herkese açık ve sağlık meslek mensuplarına özel erişim kontrolü bulunmuyor.

Bu Türkçe skill, bir yayın eylemi yapmak yerine Medical, Regulatory ve Legal
insan incelemesine izlenebilir bir taslak hazırlar. Kilitli başlangıç sonucu
`do-not-publish`, önerilen seçenek `professional-channel-review`dır. Bu seçenek
ayrı profesyonel materyali veya yayını onaylamaz. Çıktı hukuki, mühendislik veya
tıbbi tavsiye değildir; Copilot onaylamaz, yayımlamaz, hedeflemez, içeriği
kaldırmaz veya kampanyayı durdurmaz. Yetkili insanlar karar verir ve eylemleri
yürütür.

## Ne denetlenir?

- Ürün ve reçete statüsü hangi kaynağa dayanıyor?
- Materyalin niyeti değil, fiilî hedef kitlesi ve kanal erişimi nedir?
- Ürün adı, fayda ve çağrı iddiaları sağlanan onaylı kapsamla eşleşiyor mu?
- Profesyonel kanal gerçek rol doğrulamasıyla sınırlı mı?
- Medical, Regulatory, Legal incelemesi ve yayın kapısı kayıtlı mı?
- Sürüm, kanal, insan sahibi, gözden geçirme ve kaldırma tetikleri belli mi?

## Kaynak yaklaşımı

Kamusal yöntem iki resmî kaynağa dayanır:

- [TİTCK - Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik](https://www.titck.gov.tr/mevzuat/beseri-tibbi-urunlerin-tanitim-faaliyetleri-hakkinda-yonetmelik-27122018172726),
  SHA-256 `552ce8f77c365599105d387e5d9d312998f26df634131faad66201a35ad027d1`.
- [T.C. Resmî Gazete yayımı](https://www.resmigazete.gov.tr/eskiler/2015/07/20150703-2.htm),
  SHA-256 `c23a03d934063bec7abd0a678cf947d2044af82f63d404a59028aaa5421191cf`.

Her iki kaynağın erişim tarihi `2026-08-04`tür. Dış kaynaklar yalnızca metadata
olarak dağıtılır; skill uzun kopyalar yerine kısa ve atıflı yöntem özeti taşır.
Güncel metin ve yeniden kullanım koşulları insan tarafından resmî kaynaklardan
doğrulanır. Şirket politikası, ürün, kreatif, roller ve bütün kayıtlar
sentetiktir.

## İndir

- [Microsoft 365 Copilot Cowork skill](../../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-cowork.skill)
- [GitHub Copilot for VS Code paketi](../../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-vscode.zip)
- [Scout paketi](../../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-scout.zip)
- [Copilot Studio GitHub harness paketi](../../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum paketi](../../downloads/turkiye-enterprise/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-classic-setup.zip)

!!! warning "Copilot Studio classic kurulumu"

    Classic paket doğrudan yüklenen, çalışma zamanını veya davranışı sabitleyen
    bir skill değildir. Yönlendirmeli manuel kurulum malzemesidir; talimatlar,
    bilgi kaynakları, bağlantılar, izinler ve yayımlama ayarları bir insan
    tarafından hedef ortamda ayrı ayrı incelenip yapılandırılmalıdır.

## Değerlendirme sözleşmesi

Demo tam 12 kilitli senaryo, beş karar sınıfı, üç seçenek ve her puan düzeyi
çapalanmış azami 14 puanlık rubrik kullanır. Donmuş prompt; ürün statüsü, tıbbi
kanıt, kapsam, hedefleme, erişim, tarih veya yetki uydurmayı ve sohbet dışı eser,
yayın ya da operasyonel eylem üretmeyi yasaklar.
