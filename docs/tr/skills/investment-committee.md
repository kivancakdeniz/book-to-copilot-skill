# Yatırım komitesi değerlendirmesi

**Alan:** Sermaye tahsisi<br>
**Hedef ekip:** CFO, COO, CIO ve yatırım komitesi üyeleri

Sermaye brifingini kapılı ve kanıt atıflı bir komite karar kartına dönüştürür.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [The Green Book - UK government guidance on appraisal](https://assets.publishing.service.gov.uk/media/698dbcd17da91680ad7f4308/The_Green_Book_2026.pdf) | HM Treasury and Government Finance Function |
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

Kilitli değerlendirme `conditional-approval` karar sınıfını,
`phased-automation` seçeneğini ve 6 kural
kimliğini bekler. Nihai insan rotası: Investment Committee.

## LLM only ve LLM + skill

Aynı vaka ve istem iki kez çalıştırıldı. Tek fark, ikinci çalıştırmada skill'in
yüklü olmasıdır. Puanlama bir model tarafından değil, kilitli yanıt anahtarını
okuyan deterministik betik tarafından yapılır.

| Denetim | Yalnız LLM | LLM + skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 6 | 6 / 6 |
| Tam karar sınıfı | hayır | evet |
| Adlandırılmış seçenek | evet | evet |
| İnsan rotası | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/investment-committee/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/investment-committee/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/investment-committee/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/investment-committee
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/investment-committee/investment-committee-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/investment-committee/investment-committee-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/investment-committee/investment-committee-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/investment-committee/investment-committee-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/investment-committee/investment-committee-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/investment-committee/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
