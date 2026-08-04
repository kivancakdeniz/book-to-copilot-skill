# İndirimli fiyat denetimi

**Alan:** E-ticaret ve tüketici hukuku<br>
**Hedef ekip:** E-ticaret, fiyatlandırma ve Compliance ekipleri

Fiyat geçmişi ile kampanya iddiasını izlenebilir bir yayın kararında buluşturur.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Fiyat bilgisi içeren reklamlar ile indirimli satış reklamları ve ticari uygulamaları hakkında kılavuz](https://tuketici.ticaret.gov.tr/haberler/fiyat-bilgisi-iceren-reklamlar-ile-indirimli-satis-reklamlari-ve-ticari-uygulamalari-hakkinda-kilavuz-guncellendi) | Ticaret Bakanlığı |
| Sentetik politika ve vaka | `Demo dizininde depo MIT lisansıyla yayımlanır` | — |

## Üretilen skill

Skill, kaynak içeriği tek bir özete sıkıştırmak yerine yeniden kullanılabilir altı
dosyaya ayırır:

- `SKILL.md`: ne zaman kullanılacağı ve işlem sırası;
- `public-method.md`: resmî kaynaktan çıkarılan bağımsız yöntem özeti;
- `company-policy.md`: kararlı kimlikleri olan sentetik kurum kuralları;
- `evidence-map.md`: hangi iddianın hangi kaynaktan gelebileceği;
- `output-schema.md`: beklenen yanıt yapısı;
- `scenario-guide.md`: eksik bilgi, çelişki ve çekimserlik davranışı.

Kilitli değerlendirme `revise-price-claim` karar sınıfını,
`advertise-25-percent` seçeneğini ve 7 kural
kimliğini bekler. Nihai insan rotası: E-commerce Owner · Pricing Owner · Compliance · Legal.

## LLM only ve LLM + skill

Aynı vaka ve istem iki kez çalıştırıldı. Tek fark, ikinci çalıştırmada skill'in
yüklü olmasıdır. Puanlama bir model tarafından değil, kilitli yanıt anahtarını
okuyan deterministik betik tarafından yapılır.

| Denetim | Yalnız LLM | LLM + skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı | hayır | evet |
| Adlandırılmış seçenek | hayır | evet |
| İnsan rotası | evet | evet |
| **İz puanı** | **20 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/indirimli-fiyat-denetimi/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/indirimli-fiyat-denetimi/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/indirimli-fiyat-denetimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/indirimli-fiyat-denetimi
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/indirimli-fiyat-denetimi/indirimli-fiyat-denetimi-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/indirimli-fiyat-denetimi/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
