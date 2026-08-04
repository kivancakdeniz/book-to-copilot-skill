---
hide:
  - navigation
  - toc
---

# book-to-copilot-skill

[English](../index.md)

<p style="font-size: 1.25rem; max-width: 42rem;">
Onaylı iş rehberlerini yönetişimli ve değerlendirilebilir Copilot skill'lerine
dönüştürün: karar yöntemleri, kurumsal kurallar, kaynak izi ve insan onay
sınırları. <strong>Bir başka bağlam yığını değil, belgelerden kararlara giden
bir yapı.</strong>
</p>

[Başlangıç rehberi](../guide.md){ .md-button .md-button--primary }
[Yatırım Komitesi demosu](demos/investment-committee.md){ .md-button }
[Pazarlama İddiaları İncelemesi](demos/marketing-claims-review.md){ .md-button }
[10 skill'lik katalog](skills/index.md){ .md-button }

## Kaynak proje ve bağımsızlık

Bu proje, [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)
projesinin [MIT Lisansı](https://github.com/virgiliojr94/book-to-skill/blob/main/LICENSE.md)
altında yeniden kullanılan bağımsız bir alt sürümüdür. Kaynak proje ve
bakımcıları bu alt sürümü desteklediğini veya onayladığını beyan
etmemiştir. Bu sürüm GitHub Copilot uyumluluğu, yönetişimli kurumsal örnekler,
deterministik paketler ve değerlendirme malzemeleri ekler.

## Rehber neden skill'e derlenir

- Kaynaklar hash'lerle ve biçime özel geri dönüşlerle yerel olarak çıkarılır.
- Kamusal yöntemler, şirket politikası, vaka olguları ve insan yetkisi ayrı ve
  izlenebilir kalır.
- Agent Skills çalışma ortamları önce çekirdek iş akışını, yalnız gerektiğinde destek
  kaynaklarını yükler.
- Çıktı daha büyük bir istem değil; açık kapıları, kaynak izi ve insan onay
  sınırları olan bir karar kaydıdır.

## Yalnız LLM ve derlenmiş skill

| Tek bakışta | Yalnız LLM | LLM + derlenmiş skill |
|---|---|---|
| İş yönü | Çoğu zaman makul | Genellikle aynı makul yön |
| Karar biçimi | Serbest metin | Kontrollü karar sınıfı ve yapılandırılmış satırlar |
| Kural ve kanıt | Özet düzeyinde kaynaklar | Kural ID'leri, kanıt ID'leri ve yöntem kaynakları |
| İnsan yetkisi | Genel veya çıkarımsal | Adlandırılmış roller ve açık onay kapıları |

## Mevcut kanıt

[Yatırım Komitesi demosu](demos/investment-committee.md), yalnız özet kullanan
iki kontrolü ve skill'in açıkça çağrıldığı iki uygulama koşusunu korur. Dört koşunun
tamamı aşamalı otomasyonu seçti; uygulama koşuları kesin karar sınıfını, politika
kapılarını, yetki rotasını ve izlenebilir kaynakları ekledi.

[Pazarlama İddiaları İncelemesi](demos/marketing-claims-review.md), model eşleşmiş
bir Claude Opus 4.8 kontrol/uygulama çiftini ve ayrı bir Auto uygulamasını
korur. İki taraf da kanıtla sınırlandırılmış kampanyayı seçti; skill destekli
koşular kesin sınıfı, denetlenebilir yedi satırı, kural/kanıt eşlemesini ve yayın
kontrollerini ekledi.

!!! warning "Bu kanıt neyi gösterir"

    Bunlar nedensel A/B kanıtı değil, oturum açılmış Cowork UX gözlemleridir.
    Uygulama istemleri skill'leri açıkça çağırdı ve kontrollere verilmeyen
    kaynakları içerdi. Ham ilk yanıtlar, ekran görüntüleri, manifestler ve ön
    rubrik provaları yayımlandı; sabit modelli değerlendirme ile kör insan
    incelemesi beklemededir.

## Katalog durumu

[Türkiye kurumsal kataloğu](skills/index.md); mahremiyet, pazarlama, finans,
güvenlik, sağlık, ödeme ve telekom alanlarında **değerlendirmeye hazır 10 yeni
demo** içerir. Her skill için beş deterministik, bayt düzeyinde özdeş biçim olmak
üzere **50 çalışma ortamı paketi hazırdır**. Bu 10 demo için Cowork A/B
çalıştırılmadığından
katalog model etkisi, üretim performansı veya ROI iddiasında bulunmaz.

## Başvuru

[Mimari](../ARCHITECTURE.md) · [Performans](../PERFORMANCE.md) ·
[Skill referansı](../skill-reference.md) ·
[Kurumsal demo planı](../ENTERPRISE-DEMO-PLAN.md)
