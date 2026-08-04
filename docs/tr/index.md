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
[12 skill'lik katalog](skills/index.md){ .md-button }
[Skill'ler nasıl kanıtlandı](#kontrol-ve-skill-12-skillde-olculdu){ .md-button }

## Bu proje ne için var

Bu downstream tek bir soruyu kanıtla yanıtlamak için var: **onaylı kurum
rehberini bir Agent Skill'e derlemek, gerçek bir kurumsal kararda asistanın
ürettiği çıktıyı gerçekten değiştiriyor mu?**

Yanıt için proje, Türkiye mevzuatı ile kurumsal operasyonun kesişiminde on iki
işlenmiş karar sunar, her birini iki kez çalıştırır, iki çalıştırmayı da
deterministik bir betikle puanlar ve sonucu Microsoft 365 Copilot Cowork, GitHub
Copilot, Microsoft Scout ve Copilot Studio'ya aktarılabilir paketler hâline
getirir.

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

## Kontrol ve skill: 12 skill'de ölçüldü

Katalogdaki her skill aynı yöntemle sınandı. Aynı kilitli vaka, aynı istem ve tek
fark: ikinci çalıştırmada skill kuruluydu. İki yanıt da `tools/score_skill_answer.py`
ile puanlanır; betik yanıtı kilitli senaryoya göre denetler. Sonucu bir model
değerlendirmez, bu yüzden puanlamayı herkes yeniden çalıştırıp aynı sayıları alır.

| 12 skill genelinde ölçüm | Yalnız LLM | LLM + skill |
|---|---|---|
| Ortalama iz puanı | 33 / 100 | 95 / 100 |
| Hiç politika kuralına atıf yapmayan skill | 12 / 12 | 0 / 12 |
| Tam karar sınıfını yazan skill | 0 / 12 | 9 / 12 |
| Yayımlanan ham yanıt | 12 | 12 |

Kontrol çalıştırmaları yetersiz değildir; çoğunlukla makul bir iş yönü bulur.
Yapamadıkları şey, şirket kural kimliklerine atıf yapmak, izin verilen tam karar
sınıfını yazmak ve kararı adı konmuş insan sahibine yönlendirmektir; çünkü skill
olmadan bu bilgi modele hiç ulaşmaz.

!!! warning "Bu neyi kanıtlar, neyi kanıtlamaz"

    Bu, kilitli senaryolara karşı skill başına tek çalıştırmalı bir karşılaştırmadır;
    nedensel bir benchmark değildir. Her skill için tek host üzerinde bir kontrol ve
    bir skill çalıştırması vardır ve skill çalıştırması, kontrolün hiç görmediği
    şirket politikasını meşru biçimde alır. On iki skill çalıştırmasının üçü kilitli
    beklentiden daha temkinli bir karar sınıfı seçti; bu gizlenmedi, yayımlandı. İlk
    iki demo ayrıca host düzeyinde Microsoft 365 Copilot Cowork ekran görüntüleri ve
    manifestleri taşır.

## Katalog durumu

[Katalog](skills/index.md); mahremiyet, ticari ileti, e-ticaret, finansal suç,
bankacılık, rekabet, iş güvenliği, sağlık, ödeme, telekom, sermaye tahsisi ve
reklam incelemesi alanlarında **12 skill** içerir. Her biri 12 kilitli senaryo,
14 puanlık rubrik, sentetik şirket politikası, resmî kaynak metadatası, ham
kontrol yanıtı, ham skill yanıtı ve deterministik skor kartı ile gelir.

**60 host paketi yayımlandı**: Cowork, VS Code'da GitHub Copilot, Microsoft Scout
ve Copilot Studio (GitHub harness ve classic setup) için skill başına beş
deterministik, byte-identical biçim.

## Başvuru

[Mimari](../ARCHITECTURE.md) · [Performans](../PERFORMANCE.md) ·
[Skill referansı](../skill-reference.md) ·
[Kurumsal demo planı](../ENTERPRISE-DEMO-PLAN.md)
