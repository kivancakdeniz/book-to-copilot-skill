# Güvenlik ve yeniden kullanım

Bu projeyi yalnızca işleme hakkınız olan içerikle kullanın. Dönüştürücü ve herkese açık
örnekler; kaynak kitap, mevzuat, kurum içi belge, ekran görüntüsü veya model
çıktısının haklarını size devretmez.

## Kaynak hakları

- Depo hiçbir kaynak kitabı veya tam resmî belgeyi dağıtmaz.
- Telifli veya gizli kaynaklardan üretilen Agent Skill dosyalarını paylaşma izniniz yoksa özel
  tutun.
- 12 örnekteki resmî kaynaklar üstveri ve bağımsız yazılmış kısa yöntem
  özetleriyle temsil edilir.
- Sentetik politikalar, vakalar, değerlendirme test düzenekleri, türev proje kodu
  ve bu proje için yazılmış dokümantasyon MIT lisansı kapsamında yayımlanır.

## Veri işleme

Metin çıkarma yerelde çalışır. Herkese açık istemlere, ekran görüntülerine,
günlük kayıtlarına, sorun kayıtlarına veya kanıtlara kimlik bilgisi, kiracı
(tenant) kimliği, müşteri verisi, kişisel veri, gizli belge ya da düzenlemeye tabi kayıt
koymayın. Yapay zekâ modeli barındırılan bir serviste çalışıyorsa modele gönderilen
metin sağlayıcının veri koşullarına tabidir.

## Üretilen Agent Skill'i inceleyin

Her girdi belgesini güvenilmeyen kaynak olarak değerlendirin. Üretilen Agent
Skill'i kurmadan önce:

1. `SKILL.md` ve bütün destek dosyalarını inceleyin;
2. komutları, bağlantıları, yolları ve YAML üstbilgisini (frontmatter) kontrol edin;
3. hedef ortam uyumluluğu ve istem enjeksiyonu taramalarını çalıştırın;
4. tutulmaması veya paylaşılmaması gereken kaynak metni kaldırın;
5. güncel resmî kaynağı ve şirket politikasını doğrulayın.

Tarama araçları riski azaltır; ancak Agent Skill'in güvenli veya doğru olduğunu
onaylamaz.

## Değerlendirme iddiaları

Yayımlanan karşılaştırma, adı belirtilen ortamda her koşul için tek çalıştırma ve
önceden belirlenmiş tek senaryo kullanır. Davranışın makineyle doğrulanabilen
sınırlı bir bölümünü ölçer. Üretim doğruluğunu, hukuki uygunluğu, güvenliği,
adaleti, dayanıklılığı, yatırım getirisini veya gelecekteki performansı
kanıtlamaz.

Bir Agent Skill'in modeli iyileştirdiğini iddia ediyorsanız ham yanıtları ve
puanlama kurallarını yayımlayın. Beklenen sonuçla uyuşmayan çalıştırmaları
gizlemeyin.

## İnsan yetkisi

Agent Skill kanıtları yapılandırabilir ve inceleme yolu önerebilir. Onay veremez,
yayımlayamaz, başvuru yapamaz, müşteriyi kabul veya reddedemez, hesabı askıya
alamaz, aktarım veya gönderim yapamaz, işi durduramaz ve operasyonel karar
uygulayamaz. Yorumlama, onaylama ve eyleme geçme yetkisi insandadır.

## Proje ilişkisi

Bu proje, MIT lisanslı
[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)
projesinin bağımsız bir türevidir. Kaynak projenin yazarı, Microsoft, GitHub,
model sağlayıcıları veya herhangi bir kamu otoritesi tarafından onaylanmamıştır.

Güvenlik sorunlarını herkese açık bir sorun kaydı oluşturmak yerine deponun özel
güvenlik açığı bildirim akışıyla iletin.
