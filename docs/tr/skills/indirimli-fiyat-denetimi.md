# İndirimli fiyat denetimi

**Alan:** E-ticaret ve tüketici hukuku<br>
**Hedef ekip:** E-ticaret, fiyatlandırma ve uyum ekipleri

Fiyat geçmişi ile kampanya iddiasını birlikte inceleyerek izlenebilir bir yayımlama kararı oluşturur.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Fiyat bilgisi içeren reklamlar ile indirimli satış reklamları ve ticari uygulamaları hakkında kılavuz](https://tuketici.ticaret.gov.tr/haberler/fiyat-bilgisi-iceren-reklamlar-ile-indirimli-satis-reklamlari-ve-ticari-uygulamalari-hakkinda-kilavuz-guncellendi) | Ticaret Bakanlığı |
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
`revise-price-claim` (fiyat iddiasını düzelt), önerilen seçenek olarak
`advertise-25-percent` (yüzde 25 indirim iddiasını kullan) ve 7
kural kimliğinin kullanılması beklenir. Nihai
incelemeden sorumlu roller:
`E-commerce Owner` (E-ticaret sorumlusu) · `Pricing Owner` (Fiyatlandırma sorumlusu) · `Compliance` (Uyum) · `Legal` (Hukuk).

## Yalnızca LLM ve LLM + Agent Skill

Aynı vaka ve istem iki kez çalıştırıldı. İkinci çalıştırmada ayrıca Agent Skill
yüklüdür. Her iki yanıtı da başka bir model değil, önceden belirlenmiş yanıt
anahtarını kullanan deterministik bir betik puanlar.

| Denetim | Yalnızca LLM | LLM + Agent Skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 7 | 7 / 7 |
| Beklenen karar sınıfıyla tam eşleşme | hayır | evet |
| Önerilen seçenek | hayır | evet |
| Yetkili incelemeye yönlendirme | evet | evet |
| **Karar izlenebilirliği puanı** | **20 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/indirimli-fiyat-denetimi/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/indirimli-fiyat-denetimi/outputs/treatment-1.txt) ·
[Puan kartı](../../assets/skills/indirimli-fiyat-denetimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/indirimli-fiyat-denetimi
```

Bu karşılaştırmada her koşulda tek senaryo ve tek çalıştırma ortamı kullanılmıştır;
sonuçlar üretim doğruluğunun veya mevzuata uygunluğun kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-scout.zip)
- [Copilot Studio GitHub bağlantı paketi](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-github-harness.zip)
- [Copilot Studio klasik kurulum paketi](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-classic-setup.zip)

Klasik paket doğrudan içe aktarılabilen bir Copilot Studio çözümü değildir; hedef
ortamda elle uygulanacak kurulum dosyaları ve yönergeleri içerir.

## Yeniden kullanım

Kaynak bildirim dosyası, sentetik girdiler, senaryolar, ham yanıtlar ve puan kartı
`demos/indirimli-fiyat-denetimi/` altında herkese açıktır. Aynı yapıyı kendi kaynağınız için
kopyalayın; ancak yalnızca paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik
ve yeniden kullanım](../safety.md) sınırlarını inceleyin.
