# Kripto ödeme geçidi incelemesi

**Alan:** Ödeme hizmetleri ve kripto varlıklar<br>
**Hedef ekip:** Ödeme, uyum, hukuk ve ürün ekipleri

Kripto işlevinin ödeme akışındaki rolünü ürün kapsamı ve kullanıma alma koşulları açısından inceler.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Ödemelerde Kripto Varlıkların Kullanılmamasına Dair Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210416-4.htm) | Türkiye Cumhuriyet Merkez Bankası / T.C. Resmî Gazete |
| Sentetik politika ve vaka | Sentetik politika ve vaka, demo dizininde MIT lisansıyla yayımlanır | — |

## Üretilen Agent Skill

Agent Skill, kaynak içeriği tek bir özete sıkıştırmak yerine yeniden kullanılabilir altı
dosyaya ayırır:

- `SKILL.md`: ne zaman kullanılacağı ve çalışma sırası;
- `public-method.md`: resmî kaynaktan çıkarılan bağımsız yöntem özeti;
- `company-policy.md`: değişmeyen kimliklere sahip sentetik kurum kuralları;
- `evidence-map.md`: hangi iddianın hangi kaynaktan gelebileceği;
- `output-schema.md`: beklenen yanıt yapısı;
- `scenario-guide.md`: eksik bilgi, çelişki ve yanıt vermekten kaçınma davranışı.

Önceden belirlenen değerlendirmede karar sınıfı olarak
`reject-payment-flow` (ödeme akışını reddet), önerilen seçenek olarak
`remove-crypto-checkout` (kripto ödeme seçeneğini kaldır) ve 6
kural kimliğinin kullanılması beklenir. Nihai
incelemeden sorumlu roller:
`Payments Counsel` (Ödeme hizmetleri hukuk danışmanı) · `Compliance` (Uyum) · `Product` (Ürün).

## Yalnızca LLM ve LLM + Agent Skill

Aynı vaka ve istem iki kez çalıştırıldı. İkinci çalıştırmada ayrıca Agent Skill
yüklüdür. Her iki yanıtı da başka bir model değil, önceden belirlenmiş yanıt
anahtarını kullanan deterministik bir betik puanlar.

| Denetim | Yalnızca LLM | LLM + Agent Skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 6 | 6 / 6 |
| Beklenen karar sınıfıyla tam eşleşme | hayır | evet |
| Önerilen seçenek | evet | evet |
| Yetkili incelemeye yönlendirme | evet | evet |
| **Karar izlenebilirliği puanı** | **40 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/kripto-odeme-kapisi/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/kripto-odeme-kapisi/outputs/treatment-1.txt) ·
[Puan kartı](../../assets/skills/kripto-odeme-kapisi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/kripto-odeme-kapisi
```

Bu karşılaştırmada her koşulda tek senaryo ve tek çalıştırma ortamı kullanılmıştır;
sonuçlar üretim doğruluğunun veya mevzuata uygunluğun kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-scout.zip)
- [Copilot Studio GitHub bağlantı paketi](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-github-harness.zip)
- [Copilot Studio klasik kurulum paketi](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-classic-setup.zip)

Klasik paket doğrudan içe aktarılabilen bir Copilot Studio çözümü değildir; hedef
ortamda elle uygulanacak kurulum dosyaları ve yönergeleri içerir.

## Yeniden kullanım

Kaynak bildirim dosyası, sentetik girdiler, senaryolar, ham yanıtlar ve puan kartı
`demos/kripto-odeme-kapisi/` altında herkese açıktır. Aynı yapıyı kendi kaynağınız için
kopyalayın; ancak yalnızca paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik
ve yeniden kullanım](../safety.md) sınırlarını inceleyin.
