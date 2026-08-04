---
hide:
  - navigation
  - toc
---

<div class="bts-hero" markdown>

<span class="bts-hero__eyebrow">Yönetişimli agent skill'leri</span>

# İnceleyenin denetleyebileceği kararlar { .bts-hero__title }

<p class="bts-hero__lede">
Onaylı rehberi; izin verilen tek karar sınıfını yazan, her satırın arkasındaki
kuralı gösteren, bilinmeyeni bilinmiyor bırakan ve kararı adı konmuş bir insana
devreden küçük ve taşınabilir bir Agent Skill'e derleyin. On iki işlenmiş
kurumsal karar; her biri, skill olmadan çalışan aynı modelle karşılaştırıldı.
</p>

[12 skill'i incele](skills/index.md){ .md-button .md-button--primary }
[Nasıl çalıştığını gör](how-it-works.md){ .md-button }

</div>

<ul class="bts-metrics">
  <li><b>12</b><span>skill, her biri 12 kilitli senaryo ile</span></li>
  <li><b>60</b><span>byte-identical host paketi</span></li>
  <li><b>33 &rarr; 95</b><span>ortalama iz puanı: yalnız model, sonra skill ile</span></li>
  <li><b>24</b><span>incelemeye açık ham yanıt</span></li>
</ul>

## Skill yüklendiğinde ne değişir

Katalogdaki her skill aynı yöntemle sınandı: aynı kilitli vaka, aynı istem ve
tek fark — ikinci çalıştırmada skill kuruluydu. İki yanıtı da bir model değil,
bir betik puanlar; bu yüzden puanlamayı herkes yeniden çalıştırıp aynı sayıları
elde eder.

| 12 skill genelinde ölçüm | Yalnız LLM | LLM + skill |
|---|---|---|
| Ortalama iz puanı | 33 / 100 | 95 / 100 |
| Hiç politika kuralına atıf yapmayan skill | 12 / 12 | 0 / 12 |
| Tam karar sınıfını yazan skill | 0 / 12 | 9 / 12 |
| Yayımlanan ham yanıt | 12 | 12 |

Kontrol çalıştırmaları yetersiz değildir; çoğunlukla makul bir iş yönü bulur.
Yapamadıkları şey, şirket kural kimliklerine atıf yapmak, izin verilen tam karar
sınıfını yazmak ve kararı adı konmuş sahibine yönlendirmektir; çünkü skill
olmadan bu bilgi modele hiç ulaşmaz.

<figure class="bts-diagram">
<picture>
    <source media="(max-width: 720px)" srcset="../assets/diagrams/evaluation-mobile.svg">
    <img src="../assets/diagrams/evaluation.svg" alt="Aynı kilitli vaka iki kez yanıtlanır ve deterministik puanlanır">
</picture>
<figcaption>Bu sitedeki her sayının arkasındaki değerlendirme yöntemi. Ham yanıtlar, skor kartları ve skorlayıcının kendisi yayımlanır.</figcaption>
</figure>

!!! warning "Bu neyi kanıtlar, neyi kanıtlamaz"

    Bu, kilitli senaryolara karşı skill başına tek çalıştırmalı bir
    karşılaştırmadır; nedensel bir benchmark değildir. Her skill için tek host
    üzerinde bir kontrol ve bir skill çalıştırması vardır ve skill çalıştırması,
    kontrolün hiç görmediği şirket politikasını meşru biçimde alır. On iki skill
    çalıştırmasının üçü kilitli beklentiden daha temkinli bir karar sınıfı seçti;
    bu gizlenmedi, yayımlandı. İki skill ayrıca host düzeyinde Microsoft 365
    Copilot Cowork ekran görüntüleri ve manifestleri taşır.

## Skill'ler nerede işe yarar

<div class="grid cards" markdown>

-   :material-shield-account: **Mahremiyet ve ticari ileti**

    ---

    KVKK aydınlatma kontrolü, ETK/IYS ileti kararı ve BTK haberleşme verisi;
    amaç, rıza ve saklama kapılarıyla sınırlanır.

-   :material-bank: **Düzenlenmiş finans**

    ---

    MASAK müşteri kabul, BDDK uzaktan edinim, kripto ödeme kapısı ve rekabet
    birleşme bildirimi; kararı verecek incelemeciye yönlendirilir.

-   :material-hard-hat: **İş güvenliği, sağlık ve piyasa davranışı**

    ---

    İSG risk değerlendirmesi, TİTCK ilaç tanıtımı, indirimli fiyat denetimi ve
    reklam iddiası dayanağı; açık yayın kontrolleriyle.

-   :material-cube-outline: **Her Agent Skills ortamı**

    ---

    Cowork, VS Code'da GitHub Copilot, Microsoft Scout ve iki biçimde Copilot
    Studio — skill başına beş deterministik paket.

</div>

## Bir skill nasıl kurulur

<figure class="bts-diagram">
<picture>
    <source media="(max-width: 720px)" srcset="../assets/diagrams/pipeline-mobile.svg">
    <img src="../assets/diagrams/pipeline.svg" alt="Onaylı rehberden beş host paketine">
</picture>
<figcaption>Yalnız metadata ile resmî yöntem, yayımlanmış sentetik şirket katmanı, tek derlenmiş skill ve beş host aktarımı.</figcaption>
</figure>

[Yöntemi oku](how-it-works.md){ .md-button }

## Kaynak ve bağımsızlık

Alttaki çıkarım motoru, MIT lisanslı
[`book-to-skill`](https://github.com/virgiliojr94/book-to-skill) projesidir. Bu
downstream; Copilot ekosistemi paketlemesini, yönetişimli kurumsal örnekleri,
deterministik değerlendirmeyi ve yayın fabrikasını ekler. Bağımsız olarak
sürdürülür; kaynak projenin yazarı, Microsoft ya da herhangi bir kamu otoritesi
tarafından onaylanmamıştır.

[Güvenlik, kaynak ve yeniden kullanım sınırları](safety.md)
