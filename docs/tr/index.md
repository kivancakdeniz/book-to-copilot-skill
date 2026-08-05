# Kitap ya da farklı dokümanları yeniden kullanılabilir Agent Skill'lere dönüştürün

`book-to-copilot-skill`, kitap, PDF, mevzuat, kurum rehberi ve doküman
koleksiyonlarını yapılandırılmış Agent Skill'lere dönüştürür. Ardından aynı
istemi Agent Skill olmadan ve Agent Skill'le çalıştırarak yanıttaki farkı
ölçmenizi, incelediğiniz sonucu Microsoft Copilot ekosistemi için paketlemenizi
sağlar.

![Kitaplar, dokümanlar, mevzuat ve kurum rehberleri tek bir yapılandırılmış Agent Skill'e dönüşür; yalnızca LLM ile Agent Skill destekli yanıtların karşılaştırıldığı bir değerlendirmeden geçer ve beş Copilot paketine ayrılır.](../assets/book-to-copilot-skill-cover.webp){ loading=eager fetchpriority=high }

[Kendi Agent Skill'inizi oluşturun](create-a-skill.md){ .md-button .md-button--primary }
[12 örneği inceleyin](skills/index.md){ .md-button }

## Proje nasıl çalışır

### 1. Dönüştürün

Bir dosya, birden çok dosya, klasör veya dosya kalıbı (glob) belirtin. Yerel metin çıkarma aracı
PDF, EPUB, DOCX, Markdown, düz metin, HTML, RTF ve MOBI/AZW biçimlerini destekler.
Agent; kaynağın yapısını, çerçevelerini, kurallarını, tekniklerini ve kaçınılması
gereken yaklaşımları bulur; tek kullanımlık özet yerine yeniden kullanılabilir bir
Agent Skill yazar.

```text
kitap / PDF / mevzuat / kurum dokümanı
                    ↓
          yapılandırılmış Agent Skill
```

### 2. Farkı ölçün

Üretilen Agent Skill ancak yanıtı anlamlı ve yeniden üretilebilir biçimde
değiştiriyorsa değerlidir. Bu nedenle aynı vaka ve istem önce yalnızca LLM ile,
sonra Agent Skill desteğiyle çalıştırılır. Deterministik puanlayıcı; karar
sınıfını, önerilen seçeneği, kural atıflarını, yetkili incelemeye yönlendirmeyi
ve modelin üstlenmemesi gereken yetki iddialarını denetler.

Yayımlanan 12 örnekte:

| Sonuç | Yalnızca LLM | LLM + Agent Skill |
| --- | ---: | ---: |
| Ortalama karar izlenebilirliği puanı | 33 / 100 | 95 / 100 |
| Politika kuralı atfı bulunmayan örnek | 12 / 12 | 0 / 12 |
| Beklenen karar sınıfıyla tam eşleşme | 0 / 12 | 9 / 12 |

Ham yanıtlar ve puan kartları herkese açıktır. Üç Agent Skill çalıştırması,
önceden belirlenen beklentiden daha temkinli bir sınıf seçti; bu sonuçlar da
yayımlandı.

### 3. Paketleyin

Agent Skill düz Markdown olarak kalır ve Agent Skills destekleyen ortamlar
arasında taşınabilir. Paketleme aracı her örnek için beş deterministik paket
üretir:

- Microsoft 365 Copilot Cowork `.skill`
- VS Code için GitHub Copilot
- Microsoft Scout
- Copilot Studio GitHub bağlantı paketi
- Copilot Studio klasik kurulum paketi

12 örnek toplam 60 paket üretir. Temiz bir yeniden derlemede bu paketlerin bayt
düzeyinde birebir aynı olduğu doğrulanır.

## Kendi içeriğinizi kullanın

Proje, içindeki mevzuat örnekleriyle sınırlı değildir. Şunlardan Agent Skill
oluşturabilirsiniz:

- kitap veya teknik kılavuz;
- mevzuat ve kendi operasyon politikanız;
- kurum içi dokümantasyon, işletim kılavuzu (runbook) veya mimari kararlar;
- araştırma koleksiyonu veya ilişkili makaleler;
- kurumunuzun sahip olduğu ürün, marka veya süreç rehberi.

Metin çıkarma sırasında girdi makinenizde kalır. Yapay zekâ modeli bulutta çalışıyorsa
modele gönderilen metin sağlayıcının normal veri koşullarına tabidir.

## 12 örnek neden var

Örnekler bütün süreci incelenebilir malzemeyle gösterir: kaynak üstverisi,
sentetik politika ve vaka, üretilen Agent Skill, önceden belirlenmiş senaryolar,
yalnızca LLM ile alınan yanıt, Agent Skill destekli yanıt, puan kartı ve farklı
Copilot ortamlarına yönelik paketler. Akışın kişisel verilerin korunması,
bankacılık, finansal suçlarla mücadele, rekabet, iş güvenliği, sağlık, ödeme,
telekom, sermaye tahsisi ve pazarlama incelemesinde tekrarlanabildiğini gösterir.

Bunlar şablondur; dönüştürücünün sınırı değildir.

## Açık kaynak ve yeniden kullanılabilir

Deponun kodu, sentetik örnekleri ve bu proje için yazılmış dokümantasyonu MIT
lisansıyla herkese açıktır. Depoyu klonlayın, kendi Agent Skill'inizi üretin,
değerlendirme test düzeneğini uyarlayın ve yalnızca paylaşma hakkınız olan
içeriği yayımlayın.

Bu proje, MIT lisanslı
[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)
dönüştürücüsünün bağımsız bir türevidir. Metin çıkarma temelini korur; Copilot
paketleme, tekrarlanabilir değerlendirme, 12 kurumsal örnek ve yayın
güvenilirliği iyileştirmeleri ekler. Kaynak projenin yazarı, Microsoft veya
herhangi bir kamu otoritesi tarafından onaylanmamıştır.

[Kendi kaynağınızla başlayın](create-a-skill.md) ·
[Güvenlik ve yeniden kullanım sınırlarını inceleyin](safety.md)
