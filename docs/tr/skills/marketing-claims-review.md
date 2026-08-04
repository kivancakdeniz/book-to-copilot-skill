# Pazarlama iddiaları incelemesi

**Alan:** Pazarlama ve reklam uyumu<br>
**Hedef ekip:** Pazarlama, Legal ve Compliance ekipleri

Reklam iddialarını dayanak, ifşa ve yayın kontrolleriyle sınar.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Advertising and Marketing on the Internet: Rules of the Road](https://www.ftc.gov/system/files/ftc_gov/pdf/bus28-rulesroad-2023_508.pdf) | U.S. Federal Trade Commission |
| Resmî kaynak | [.com Disclosures: How to Make Effective Disclosures in Digital Advertising](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf) | U.S. Federal Trade Commission |
| Resmî kaynak | [Guides Concerning the Use of Endorsements and Testimonials in Advertising (16 CFR Part 255)](https://www.ecfr.gov/api/versioner/v1/full/2023-07-26/title-16.xml?part=255) | Electronic Code of Federal Regulations |
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

Kilitli değerlendirme `approve-with-edits` karar sınıfını,
`evidence-bounded-campaign` seçeneğini ve 9 kural
kimliğini bekler. Nihai insan rotası: Legal · Compliance.

## LLM only ve LLM + skill

Aynı vaka ve istem iki kez çalıştırıldı. Tek fark, ikinci çalıştırmada skill'in
yüklü olmasıdır. Puanlama bir model tarafından değil, kilitli yanıt anahtarını
okuyan deterministik betik tarafından yapılır.

| Denetim | Yalnız LLM | LLM + skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 9 | 9 / 9 |
| Tam karar sınıfı | hayır | evet |
| Adlandırılmış seçenek | evet | evet |
| İnsan rotası | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/marketing-claims-review/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/marketing-claims-review/outputs/treatment-auto-1.txt) ·
[Skor kartı](../../assets/skills/marketing-claims-review/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/marketing-claims-review
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/marketing-claims-review/marketing-claims-review-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/marketing-claims-review/marketing-claims-review-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/marketing-claims-review/marketing-claims-review-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/marketing-claims-review/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
