# Nasıl çalışır

Bu katalogdaki bir skill, bir istem ya da doküman yığını değildir. Karar
yöntemini, uygulanan şirket kurallarını, her iddianın kaynağını ve kararın
insana geçtiği sınırı taşıyan küçük ve denetlenebilir bir pakettir.

<figure class="bts-diagram">
<picture>
	<source media="(max-width: 720px)" srcset="../../assets/diagrams/pipeline-mobile.svg">
	<img src="../../assets/diagrams/pipeline.svg" alt="Onaylı rehberden beş host paketine">
</picture>
<figcaption>Onaylı rehber bir kez derlenir ve desteklenen her ortama aktarılır. Resmî belgelerin ham hâli hiçbir pakete konmaz.</figcaption>
</figure>

## 1. Kaynak

Her skill, birbirinden kesin biçimde ayrılan iki girdiyle başlar.

**Resmî yöntem.** Mevzuat ve düzenleyici rehberliği yalnız metadata ile
anılır: başlık, yayıncı, resmî URL, erişim tarihi ve SHA-256. Depo, kaynak
metnin kendisi yerine bağımsız yazılmış kısa bir yöntem özeti taşır; böylece
yeniden dağıtılmaması gereken hiçbir içerik dağıtılmaz.

**Şirket katmanı.** Operasyonel kurallar, eşikler ve onay rotaları sentetiktir
ve tamamı yayımlanır. Böylece örnek, gerçek bir kurumu ifşa etmeden baştan sona
incelenebilir ve yeniden kullanılabilir.

## 2. Derleme

Derlenmiş skill her zaman altı Markdown dosyasıdır:

| Dosya | Taşıdığı |
| --- | --- |
| `SKILL.md` | Ne zaman tetikleneceği, akış ve kesin sınırlar |
| `company-policy.md` | Sabit kimlikli karar kuralları |
| `public-method.md` | Resmî yöntemin bağımsız özeti |
| `evidence-map.md` | Hangi iddianın hangi kaynaktan gelebileceği |
| `output-schema.md` | Yanıtın tam biçimi |
| `scenario-guide.md` | Eksik olgu, çelişki, çekimserlik, olasılık soruları |

Bu ayrım, her zaman yüklenen bölümü küçük tutar; gerisi yalnız vaka gerektirince
okunur.

## 3. Yanıt neye benzer

Asıl mesele şemadır. Yönetişimli bir yanıt izin verilen tek karar sınıfını
yazar, uyguladığı her kuralı izlenebilir kılar, bilinmeyeni bilinmiyor bırakır
ve kararı adı konmuş bir insana devreder.

<figure class="bts-diagram">
<picture>
	<source media="(max-width: 720px)" srcset="../../assets/diagrams/decision-card-mobile.svg">
	<img src="../../assets/diagrams/decision-card.svg" alt="Yönetişimli karar kartının anatomisi">
</picture>
<figcaption>KVKK aydınlatma kontrolü skill'inden bir karar kartı. Kural kimlikleri, eksik kanıt ve insan sahibi biçimsel bir tercih değil, zorunlu çıktının parçasıdır.</figcaption>
</figure>

## 4. Kanıt

Skill hakkında iddia üretmek ucuzdur; bu yüzden katalogdaki her skill aynı
yöntemle ölçülür ve sonuç, lehimize olmadığında da yayımlanır.

<figure class="bts-diagram">
<picture>
	<source media="(max-width: 720px)" srcset="../../assets/diagrams/evaluation-mobile.svg">
	<img src="../../assets/diagrams/evaluation.svg" alt="Aynı kilitli vaka iki kez yanıtlanır ve deterministik puanlanır">
</picture>
<figcaption>Kontrol ve skill çalıştırması aynı kilitli vakayı aynı istemle yanıtlar. İkisini de bir model değil, bir betik puanlar.</figcaption>
</figure>

Skorlayıcı, makine ile doğrulanabilen beş şeye bakar: tam karar sınıfı, önerilen
seçenek, gerekli her kural kimliğine atıf, adı konmuş insan rotası ve otonom
yetki iddiasının bulunmaması. Kriterleri kilitli senaryodan kopyalanır; bu
kriterler senaryodan saparsa yayın derlemesi durur.

```bash
python tools/score_skill_answer.py scorecard --demo demos/kvkk-aydinlatma-kontrolu
```

## 5. Aktarım

Tek bir fabrika kataloğu doğrular ve skill başına beş deterministik paket üretir:
Microsoft 365 Copilot Cowork, VS Code'da GitHub Copilot, Microsoft Scout ve iki
biçimde Copilot Studio. Temiz yeniden derleme byte-identical sonuç verir ve her
arşiv kendi lisansı ile üçüncü taraf bildirimlerini taşır.

## Bu iş nereden geliyor

Alttaki çıkarım motoru, MIT lisanslı
[`book-to-skill`](https://github.com/virgiliojr94/book-to-skill) projesidir. Bu
downstream; Copilot ekosistemi paketlemesini, yönetişimli kurumsal örnekleri,
deterministik değerlendirmeyi ve yayın fabrikasını ekler. Kaynak projenin
yazarının bir onayı yoktur. İlişki, yeniden kullanım, veri ve insan yetkisi
sınırları için [Güvenlik ve kaynak](safety.md) sayfasına bakın.
