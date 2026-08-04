---
hide:
  - toc
---

# 12 public örnek

Bu örnekler dönüştürücünün yalnız kitaplarda değil, mevzuat ve kurum
rehberlerinde de çalıştığını gösterir. Her örnekte kaynak manifesti, sentetik
politika ve vaka, üretilen skill, 12 kilitli senaryo, kontrol yanıtı, skill
yanıtı, skor kartı ve beş Copilot paketi bulunur.

12 örneğin ortalama iz puanı yalnız LLM'de **33/100**, skill ile
**95/100** oldu. Sonuçlar tek senaryo ve tek host sınırındadır.

## Örnekler

### [KVKK aydınlatma kontrolü](kvkk-aydinlatma-kontrolu.md)

**Alan:** Veri koruma<br>
**Puan:** LLM only **10/100** · LLM + skill **100/100**

Aydınlatma, rıza ve aktarım boşluklarını insan yayın kapısına bağlar.

### [ETK/IYS ileti kararı](etk-iys-ileti-karari.md)

**Alan:** Ticari elektronik ileti<br>
**Puan:** LLM only **20/100** · LLM + skill **80/100**

Kampanya kitlesini kişi-kanal kanıtı ve bastırma kapısıyla inceler.

### [İndirimli fiyat denetimi](indirimli-fiyat-denetimi.md)

**Alan:** E-ticaret ve tüketici hukuku<br>
**Puan:** LLM only **20/100** · LLM + skill **100/100**

Fiyat geçmişi ile kampanya iddiasını izlenebilir bir yayın kararında buluşturur.

### [MASAK müşteri kabul](masak-musteri-kabul.md)

**Alan:** Finansal suçlarla mücadele<br>
**Puan:** LLM only **20/100** · LLM + skill **100/100**

Kimlik, nihai faydalanıcı ve fon kaynağı boşluklarını insan incelemesine yönlendirir.

### [BDDK uzaktan müşteri edinimi](bddk-uzaktan-musteri-edinimi.md)

**Alan:** Bankacılık<br>
**Puan:** LLM only **40/100** · LLM + skill **80/100**

Uzaktan edinim akışını kanıt, kontrol ve canlıya geçiş kapılarıyla sınar.

### [Rekabet birleşme bildirimi](rekabet-birlesme-bildirimi.md)

**Alan:** Birleşme ve devralmalar<br>
**Puan:** LLM only **40/100** · LLM + skill **100/100**

Ön hesaplama göstergelerini hukuki bildirim kararı ve kapanış kapısından ayırır.

### [İSG risk değerlendirmesi: değişiklikten devreye alma kapısına](isg-risk-degerlendirme.md)

**Alan:** İş sağlığı ve güvenliği<br>
**Puan:** LLM only **40/100** · LLM + skill **100/100**

Değişiklik risklerini katılım, kontrol ve devreye alma kanıtlarıyla görünür kılar.

### [TİTCK ilaç tanıtımı: hedef kitle ve yayın kapısı](titck-ilac-tanitimi.md)

**Alan:** İlaç ve sağlık iletişimi<br>
**Puan:** LLM only **40/100** · LLM + skill **100/100**

Ürün statüsü, hedef kitle ve kanal erişimini insan yayın incelemesine bağlar.

### [Kripto ödeme kapısı](kripto-odeme-kapisi.md)

**Alan:** Ödeme hizmetleri ve kripto varlıklar<br>
**Puan:** LLM only **40/100** · LLM + skill **100/100**

Kripto işlevinin ödeme akışındaki rolünü ürün sınırı ve lansman kapısıyla inceler.

### [BTK haberleşme verisi](btk-haberlesme-verisi.md)

**Alan:** Telekom ve mahremiyet<br>
**Puan:** LLM only **40/100** · LLM + skill **80/100**

Konum ve trafik verisi kullanımını amaç, rıza ve saklama kapılarıyla sınırlar.

### [Yatırım komitesi değerlendirmesi](investment-committee.md)

**Alan:** Sermaye tahsisi<br>
**Puan:** LLM only **40/100** · LLM + skill **100/100**

Sermaye brifingini kapılı ve kanıt atıflı bir komite karar kartına dönüştürür.

### [Pazarlama iddiaları incelemesi](marketing-claims-review.md)

**Alan:** Pazarlama ve reklam uyumu<br>
**Puan:** LLM only **40/100** · LLM + skill **100/100**

Reklam iddialarını dayanak, ifşa ve yayın kontrolleriyle sınar.


## Ne indirebilirsiniz

Her örnek sayfasında Cowork, GitHub Copilot for VS Code, Scout ve iki Copilot
Studio biçimi bulunur. Tüm paketler temiz yeniden derlemede byte-identical
doğrulanır ve `downloads/skills/SHA256SUMS` manifestine bağlanır.

Kendi içeriğinizle aynı akışı kurmak için [Skill oluştur](../create-a-skill.md).
