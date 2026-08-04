# MaviHat İSG değişiklik ve devreye alma politikası

Sürüm: `MH-ISG-1.0`

Bu belge yalnızca kurgusal MaviHat Lojistik demosu için üretilmiş sentetik
şirket politikasıdır. Mevzuat metni, hukuki veya mühendislik tavsiyesi ya da
mühendislik sertifikasyonu değildir. Nihai değerlendirme ve devreye alma
kararlarını yetkili insanlar verir.

## İzin verilen karar sınıfları

1. `accept-assessment`
2. `renew-assessment`
3. `hold-for-evidence`
4. `escalate-isg-board`
5. `reject-commissioning`

## İzin verilen seçenekler

1. `commission-now`
2. `hold-commissioning`
3. `redesign-work-cell`

## Kurallar

### ISG-D01 - Değişiklik incelemesi

Yeni ekipman, teknoloji, yerleşim, iş akışı veya çalışma yöntemi mevcut risk
değerlendirmesini etkileyebilecek bir değişikliktir. Etki kayda alınmadan eski
değerlendirme olduğu gibi kabul edilemez.

### ISG-T01 - Ekip katılımı

İnceleme; işveren temsilcisi, İSG profesyonelleri, ilgili çalışan temsilcileri,
operatörler ve bakım işini bilen kişilerin katılımını kayda alır. Eksik temsil
bir bulgudur; varsayımla tamamlanmaz.

### ISG-H01 - Tehlike ve kontrol kanıtı

Robot hareket alanı, insan-makine etkileşimi, erişim, sıkışma, beklenmeyen
enerjilenme, bakım ve arıza giderme senaryoları ayrı izlenir. Koruyucu donanım,
kilitleme/etiketleme ve doğrulama kanıtı yoksa durum `unknown` kalır.

### ISG-O01 - Aksiyon kaydı

Her açık bulgu için insan sahibi, doğrulanabilir aksiyon ve hedef tarih gerekir.
Bilgi sağlanmadıysa alan `unknown` yazılır; kişi veya tarih uydurulmaz.

### ISG-A01 - İnsan yetkisi

İşveren ve görevlendirilmiş İSG profesyonelleri değerlendirme ve yetki sınırını
korur. Copilot değerlendirmeyi kabul edemez, kurul kararı veremez, ekipmanı
devreye alamaz veya çalışmayı durduramaz.

### ISG-R01 - Devreye alma kapısı

Etkilenen risk değerlendirmesi yenilenmeden, gerekli katılım belgelenmeden ve
kritik kontrollerin kanıtı yetkili insanlarca doğrulanmadan devreye alma kapısı
geçilmiş sayılmaz.

### ISG-M01 - Olay ve değişiklik izleme

Devreye alma sonrası olay, ramak kala, kontrol arızası, görev değişikliği ve yeni
değişiklikler yeniden inceleme sinyalidir. İzleme sahibi, sıklığı ve tetikleri
verilmemişse `unknown` kalır.

## Seçim ilkeleri

- Belgelendirilmiş değişiklik etkisi yoksa `accept-assessment` kullanılmaz.
- Kritik kanıt eksikliği giderilebilirken `hold-for-evidence` kullanılabilir.
- Değişiklik eski değerlendirmeyi maddi olarak etkiliyorsa
  `renew-assessment` seçilir; kapı açık değilse seçenek `hold-commissioning`dır.
- Yetki, ciddi uyuşmazlık veya kabul edilemez artık risk insan kuruluna taşınır.
- Kanıtla kapatılamayan kritik tehlike veya reddedilen zorunlu kontrol,
  `reject-commissioning` ya da hücrenin yeniden tasarımını gerektirebilir.
