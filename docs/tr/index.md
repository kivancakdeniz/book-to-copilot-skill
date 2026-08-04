# Kaynak içeriği test edilmiş, yeniden kullanılabilir Agent Skill'lere dönüştürün

`book-to-copilot-skill`; kitapları, PDF'leri, mevzuatı, kurum rehberlerini ve
doküman koleksiyonlarını yapılandırılmış Agent Skill'lere dönüştürür. Ardından
skill'in LLM yanıtında anlamlı fark yaratıp yaratmadığını test etmeyi ve sonucu
Microsoft Copilot ekosistemi için paketlemeyi sağlar.

[Kendi skill'inizi oluşturun](create-a-skill.md){ .md-button .md-button--primary }
[12 örneği inceleyin](skills/index.md){ .md-button }

## Bu proje ne yapar

### 1. Dönüştürür

Agent Skill'e tek dosya, birden çok dosya, klasör veya glob verin. Yerel çıkarıcı
PDF, EPUB, DOCX, Markdown, düz metin, HTML, RTF ve MOBI/AZW destekler. Agent;
kaynağın yapısını, çerçevelerini, kurallarını, tekniklerini ve kaçınılması gereken
yaklaşımları bulur; tek kullanımlık özet yerine yeniden kullanılabilir bir skill
yazar.

```text
kitap / PDF / mevzuat / kurum dokümanı
                    ↓
          yapılandırılmış Agent Skill
```

### 2. Kanıtlar

Üretilen skill ancak yanıtı anlamlı ve yeniden üretilebilir biçimde değiştiriyorsa
değerlidir. Depo kontrol-versus-skill değerlendirme kalıbı sunar: aynı vaka ve
istem önce skill olmadan, sonra skill ile çalıştırılır. Deterministik skorlayıcı
karar sınıfını, seçeneği, kural atıflarını, insan rotasını ve uygunsuz yetki
iddialarını denetler.

Yayımlanan 12 örnekte:

| Sonuç | Yalnız LLM | LLM + skill |
| --- | ---: | ---: |
| Ortalama iz puanı | 33 / 100 | 95 / 100 |
| Hiç politika kuralına atıf yapmayan örnek | 12 / 12 | 0 / 12 |
| Tam beklenen karar sınıfı | 0 / 12 | 9 / 12 |

Ham yanıtlar ve skor kartları herkese açıktır. Üç skill çalıştırması kilitli
beklentiden daha temkinli bir sınıf seçti; bu başarısızlıklar da yayımlandı.

### 3. Paketler

Skill düz Markdown olarak kalır ve Agent Skills destekleyen ortamlarda taşınabilir.
Yayın fabrikası her örnek için beş deterministik paket üretir:

- Microsoft 365 Copilot Cowork `.skill`
- VS Code için GitHub Copilot
- Microsoft Scout
- Copilot Studio GitHub harness
- Copilot Studio classic kurulum malzemeleri

12 örnek toplam 60 byte-identical paket üretir.

## Kendi içeriğinizi kullanın

Proje, içindeki mevzuat örnekleriyle sınırlı değildir. Şunlardan skill
oluşturabilirsiniz:

- kitap veya teknik kılavuz;
- mevzuat ve kendi operasyon politikanız;
- kurum içi dokümantasyon, runbook veya mimari kararlar;
- araştırma koleksiyonu veya ilişkili makaleler;
- kurumunuzun sahip olduğu ürün, marka veya süreç rehberi.

Çıkarım sırasında girdi makinenizde kalır. Agent modeli bulutta çalışıyorsa modele
gönderilen metin sağlayıcının normal veri koşullarına tabidir.

## 12 örnek neden var

Örnekler tüm yaşam döngüsünü incelenebilir malzemeyle gösterir: kaynak metadatası,
sentetik politika ve vaka, üretilen skill, kilitli senaryolar, kontrol yanıtı,
skill yanıtı, skor kartı ve host paketleri. Akışın mahremiyet, bankacılık,
finansal suç, rekabet, iş güvenliği, sağlık, ödeme, telekom, sermaye tahsisi ve
pazarlama incelemesinde tekrarlanabildiğini kanıtlar.

Bunlar şablondur; dönüştürücünün sınırı değildir.

## Açık kaynak ve yeniden kullanılabilir

Depo; kodu, sentetik örnekleri ve yazılmış dokümantasyonu için MIT lisansıyla
public'tir. Klonlayın, kendi skill'inizi üretin, değerlendirme fixture'ını
uyarlayın ve yalnız paylaşma hakkınız olan içeriği yayımlayın.

Bu proje, MIT lisanslı
[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)
dönüştürücüsünün bağımsız downstream'idir. Çıkarım temelini korur; Copilot
paketleme, tekrarlanabilir değerlendirme, 12 kurumsal örnek ve yayın
sertleştirmesi ekler. Kaynak projenin yazarı, Microsoft veya herhangi bir kamu
otoritesi tarafından onaylanmamıştır.

[Kendi kaynağınızla başlayın](create-a-skill.md) ·
[Güvenlik ve yeniden kullanım sınırlarını inceleyin](safety.md)
