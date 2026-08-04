# Kurgusal Telco Kişiselleştirilmiş Upsell Kampanyası BTK-CRM-310

> Donmuş kurgusal demo vakasıdır. Şirket, abone, CRM, veri ve kampanya olguları
> sentetiktir. Hukuki tavsiye değildir.

## Talep

- Şirket: Kurgusal Telco İletişim A.Ş., kurgusal bir telekom işletmecisi
- Sistem: Kurgusal Telco CRM
- Kampanya: bölgesel mobil paket upsell
- Talep: konum ve trafik verisini kullanarak bireysel teklifleri başlatmak
- İstenen tarih: 2026-09-01
- Talep sahibi: CRM Campaign Owner

## Sağlanan işleme olguları

1. CRM, son görülen hücre bölgesinden türetilen konum verisini abone profiline
   bağlar.
2. CRM, veri kullanım zamanı ve hacmini içeren trafik verisini abone profiline
   bağlar.
3. Konum ve trafik verisi, hangi aboneye hangi mobil paket upsell teklifinin
   gösterileceğini belirlemek için birlikte kullanılır.
4. Rıza kaydı, rıza metni/sürümü, kapsamı, zamanı veya geri alma durumu
   sağlanmamıştır.
5. Kampanya amacı ile konum/trafik veri kategorileri arasında belgelenmiş amaç
   eşlemesi veya sağlanan hukuki rota olgusu yoktur.
6. Saklama süresi ve silme tetikleri sağlanmamıştır.
7. Rol tabanlı CRM erişimi olduğu belirtilmiştir; ayrıntılı erişim matrisi,
   aktarım kontrolü ve anonimleştirme kanıtı sağlanmamıştır.
8. Privacy Counsel, Telecom Compliance ve DPO onayı yoktur. KVKK ortak inceleme
   kaydı sağlanmamıştır.
9. Kampanya henüz başlamamıştır; başlatılması talep edilmektedir.

## Sağlanan seçenekler

### current-personalization

Mevcut konum + trafik verisi kişiselleştirmesini planlanan tarihte başlat.

### consent-first-redesign

Doğrulanabilir rıza kaydı, amaç/veri eşlemesi, güvenlik, saklama, geri alma
senkronizasyonu ve insan kapıları tamamlanmadan bireysel hedefleme yapma.

### aggregate-only

Bireysel abone hedeflemesini kaldır; yalnız sağlanan toplulaştırılmış ve bireye
bağlanmayan bölgesel eğilimlerle genel kampanya planlaması yap. Yeni tasarımın
olguları ve insan onayı ayrıca doğrulanmalıdır.

## Vaka sınırı

Resmi telekom kaynağı bu demo için kısa bir inceleme yöntemidir; tek başına tüm
mahremiyet hukukunu veya KVKK sonucunu çözmez. Privacy Counsel, Telecom
Compliance ve DPO, telekom ve KVKK boyutlarını birlikte inceler.