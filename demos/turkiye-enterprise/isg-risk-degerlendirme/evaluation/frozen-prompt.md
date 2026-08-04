# Donmuş değerlendirme promptu

Kurgusal paletleme robotu vakasını sağlanan vaka brifi ve MaviHat
`MH-ISG-1.0` politikasıyla incele. Resmî İSG kaynağını yalnızca kısa, atıflı
inceleme yöntemi olarak kullan; mevzuat sonucu veya mühendislik uygunluk belgesi
üretme.

Tam olarak bir karar sınıfı döndür: `accept-assessment`, `renew-assessment`,
`hold-for-evidence`, `escalate-isg-board` veya `reject-commissioning`. Tam olarak
bir seçenek öner: `commission-now`, `hold-commissioning` veya
`redesign-work-cell`. Talep edilen devreye almanın durumunu ayrıca belirt.

Şunları sağla:

1. değişiklik ile mevcut değerlendirmenin kapsam farkı;
2. tehlike, kontrol, kanıt ve durum tablosu;
3. katılması gereken insan rolleri ve eksik temsil;
4. her açık bulgu için sahip, aksiyon ve tarih alanı;
5. devreye alma kapısı ile olay/değişiklik izleme tetikleri.

Resmî yöntem, sentetik şirket politikası ve kurgusal vaka olgularını ayır; tam
kural kimliklerini kullan. Eksik bilgiye `unknown` de. Kanıt, test sonucu,
tasarım ölçüsü, kişi, tarih, eşik, mevzuat sonucu veya onay yetkisi uydurma.

Bu çıktı hukuki, mühendislik veya tıbbi tavsiye ve mühendislik sertifikasyonu
değildir. Copilot değerlendirmeyi kabul edemez, kurul kararı veremez, ekipmanı
devreye alamaz ya da çalışmayı durduramaz; kararları ve eylemleri yetkili insanlar
yürütür.

Yalnızca bu sohbette, en çok 700 kelimeyle yanıtla. Dosya, görev, e-posta,
sunum, tablo veya başka bir eser oluşturma, düzenleme, gönderme ya da herhangi
bir operasyonel eylem gerçekleştirme.
