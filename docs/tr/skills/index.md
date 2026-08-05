---
hide:
  - toc
---

# Herkese açık 12 örnek

Bu örnekler dönüştürücünün yalnız kitaplarda değil, mevzuat ve kurum
rehberlerinde de çalıştığını gösterir. Her örnekte kaynak bildirim dosyası, sentetik
politika ve vaka, üretilen Agent Skill, önceden belirlenmiş 12 senaryo,
yalnızca LLM ile alınan yanıt, Agent Skill destekli yanıt, puan kartı ve
beş Copilot paketi bulunur.

12 örneğin ortalama karar izlenebilirliği puanı yalnızca LLM ile **33/100**,
Agent Skill desteğiyle **95/100** oldu. Sonuçlar her koşul için
tek senaryo ve tek ortamla sınırlıdır.

## Örnekler

### [KVKK aydınlatma kontrolü](kvkk-aydinlatma-kontrolu.md)

**Alan:** Kişisel verilerin korunması<br>
**Puan:** Yalnızca LLM **10/100** · LLM + Agent Skill **100/100**

Aydınlatma, rıza ve aktarım eksiklerini yayımlamadan önce yetkili incelemesine sunar.

### [ETK/İYS ileti kararı](etk-iys-ileti-karari.md)

**Alan:** Ticari elektronik ileti<br>
**Puan:** Yalnızca LLM **20/100** · LLM + Agent Skill **80/100**

Kampanya kitlesini kişi ve kanal bazındaki kanıtlar ile gönderim engeli denetimine göre inceler.

### [İndirimli fiyat denetimi](indirimli-fiyat-denetimi.md)

**Alan:** E-ticaret ve tüketici hukuku<br>
**Puan:** Yalnızca LLM **20/100** · LLM + Agent Skill **100/100**

Fiyat geçmişi ile kampanya iddiasını birlikte inceleyerek izlenebilir bir yayımlama kararı oluşturur.

### [MASAK müşteri kabulü](masak-musteri-kabul.md)

**Alan:** Finansal suçlarla mücadele<br>
**Puan:** Yalnızca LLM **20/100** · LLM + Agent Skill **100/100**

Kimlik, nihai faydalanıcı ve fon kaynağı eksiklerini yetkili incelemesine yönlendirir.

### [BDDK uzaktan müşteri edinimi](bddk-uzaktan-musteri-edinimi.md)

**Alan:** Bankacılık<br>
**Puan:** Yalnızca LLM **40/100** · LLM + Agent Skill **80/100**

Uzaktan müşteri edinimi akışını kanıt, kontrol ve kullanıma alma koşullarına göre değerlendirir.

### [Birleşme bildirimi incelemesi](rekabet-birlesme-bildirimi.md)

**Alan:** Birleşme ve devralmalar<br>
**Puan:** Yalnızca LLM **40/100** · LLM + Agent Skill **100/100**

Ön değerlendirme bulgularını hukuki bildirim incelemesinden ve işlemin kapanış onayından ayrı ele alır.

### [İSG risk değerlendirmesi: değişiklikten devreye alma onayına](isg-risk-degerlendirme.md)

**Alan:** İş sağlığı ve güvenliği<br>
**Puan:** Yalnızca LLM **40/100** · LLM + Agent Skill **100/100**

Değişiklik risklerini katılım, kontrol ve devreye alma kanıtlarıyla görünür kılar.

### [TİTCK ilaç tanıtımı: hedef kitle ve yayımlama öncesi inceleme](titck-ilac-tanitimi.md)

**Alan:** İlaç ve sağlık iletişimi<br>
**Puan:** Yalnızca LLM **40/100** · LLM + Agent Skill **100/100**

Ürün statüsü, hedef kitle ve kanal erişimini yayımlamadan önce yetkili incelemesine sunar.

### [Kripto ödeme geçidi incelemesi](kripto-odeme-kapisi.md)

**Alan:** Ödeme hizmetleri ve kripto varlıklar<br>
**Puan:** Yalnızca LLM **40/100** · LLM + Agent Skill **100/100**

Kripto işlevinin ödeme akışındaki rolünü ürün kapsamı ve kullanıma alma koşulları açısından inceler.

### [BTK haberleşme verisi](btk-haberlesme-verisi.md)

**Alan:** Telekom ve kişisel verilerin korunması<br>
**Puan:** Yalnızca LLM **40/100** · LLM + Agent Skill **80/100**

Konum ve trafik verisi kullanımını amaç, rıza ve saklama koşullarına göre sınırlar.

### [Yatırım komitesi değerlendirmesi](investment-committee.md)

**Alan:** Sermaye tahsisi<br>
**Puan:** Yalnızca LLM **40/100** · LLM + Agent Skill **100/100**

Yatırım teklifini, onay adımlarını ve kanıt kaynaklarını gösteren bir komite değerlendirme özetine dönüştürür.

### [Pazarlama iddiaları incelemesi](marketing-claims-review.md)

**Alan:** Pazarlama ve reklam uyumu<br>
**Puan:** Yalnızca LLM **40/100** · LLM + Agent Skill **100/100**

Reklam iddialarını dayanakları, gerekli açıklamalar ve yayımlama öncesi denetimler açısından değerlendirir.


## Ne indirebilirsiniz

Her örnek sayfasında Cowork, VS Code için GitHub Copilot, Scout ve iki Copilot
Studio biçimi bulunur. Temiz bir yeniden derlemede bütün paketlerin bayt
düzeyinde birebir aynı olduğu doğrulanır ve sonuçlar
`downloads/skills/SHA256SUMS` sağlama toplamı listesine kaydedilir.

Kendi içeriğinizle aynı akışı kurmak için [Agent Skill oluşturun](../create-a-skill.md).
