# Güvenlik ve yeniden kullanım

Bu projeyi yalnız işleme hakkınız olan içerikle kullanın. Dönüştürücü ve public
örnekler; kaynak kitap, mevzuat, kurum içi belge, ekran görüntüsü veya model
çıktısının haklarını size devretmez.

## Kaynak hakları

- Depo hiçbir kaynak kitabı veya tam resmî belgeyi dağıtmaz.
- Telifli veya gizli kaynaklardan üretilen skill'leri paylaşma izniniz yoksa özel
  tutun.
- 12 örnekteki resmî kaynaklar metadata ve bağımsız yazılmış kısa yöntem
  özetleriyle temsil edilir.
- Sentetik politikalar, vakalar, değerlendirme fixture'ları, downstream kod ve
  yazılmış dokümantasyon depo MIT lisansı altındadır.

## Veri işleme

Çıkarım yerelde çalışır. Public istemlere, ekran görüntülerine, izlere, issue'lara
veya kanıta kimlik bilgisi, tenant kimliği, müşteri verisi, kişisel veri, gizli
belge ya da düzenlenmiş kayıt koymayın. Agent modeli barındırılan bir serviste
çalışıyorsa modele gönderilen metin sağlayıcının veri koşullarına tabidir.

## Üretilen skill'i inceleyin

Her girdi belgesini güvenilmeyen kaynak olarak değerlendirin. Üretilen skill'i
kurmadan önce:

1. `SKILL.md` ve bütün destek dosyalarını inceleyin;
2. komutları, bağlantıları, yolları ve frontmatter'ı kontrol edin;
3. host uyumluluğu ve prompt injection taramalarını çalıştırın;
4. tutulmaması veya paylaşılmaması gereken kaynak metni kaldırın;
5. güncel resmî kaynağı ve şirket politikasını doğrulayın.

Tarayıcılar riski azaltır; skill'in güvenli veya doğru olduğunu belgelemez.

## Değerlendirme iddiaları

Yayımlanan karşılaştırma, adı verilen host üzerinde koşul başına tek çalıştırma
ve tek kilitli senaryo kullanır. Davranışın makineyle doğrulanabilir bir alt
kümesini ölçer. Üretim doğruluğu, hukuki uygunluk, güvenlik, adalet, dayanıklılık,
ROI veya gelecek performansı kanıtlamaz.

Bir skill'in modeli iyileştirdiğini iddia ediyorsanız ham yanıtları ve puanlama
kurallarını yayımlayın. Beklenen sonuçla uyuşmayan çalıştırmaları gizlemeyin.

## İnsan yetkisi

Skill kanıtı yapılandırabilir ve inceleme rotası önerebilir. Onay veremez,
yayımlayamaz, başvuru yapamaz, müşteri kabul veya reddedemez, hesabı askıya
alamaz, aktarım veya gönderim yapamaz, işi durduramaz ve operasyonel karar
uygulayamaz. Yorum, onay ve eylemin sahibi yetkili insandır.

## Proje ilişkisi

Bu proje, MIT lisanslı
[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)
projesinin bağımsız downstream'idir. Kaynak projenin yazarı, Microsoft, GitHub,
model sağlayıcıları veya herhangi bir kamu otoritesi tarafından onaylanmamıştır.

Güvenlik sorunlarını public issue yerine deponun özel güvenlik açığı bildirim
akışıyla iletin.
