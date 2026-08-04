# MASAK müşteri kabul

**Alan:** Finansal suçlarla mücadele<br>
**Hedef ekip:** AML, Compliance ve müşteri kabul ekipleri

Kimlik, nihai faydalanıcı ve fon kaynağı boşluklarını insan incelemesine yönlendirir.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Suç gelirlerinin aklanmasının ve terörün finansmanının önlenmesine dair tedbirler hakkında yönetmelik](https://masak.hmb.gov.tr/suc-gelirlerinin-aklanmasinin-ve-terorun-finansmaninin-onlenmesine-dair-tedbirler-hakkinda-yonetmelik-3/) | MASAK |
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

Kilitli değerlendirme `enhanced-review` karar sınıfını,
`hold-onboarding` seçeneğini ve 8 kural
kimliğini bekler. Nihai insan rotası: AML Officer · Compliance.

## LLM only ve LLM + skill

Aynı vaka ve istem iki kez çalıştırıldı. Tek fark, ikinci çalıştırmada skill'in
yüklü olmasıdır. Puanlama bir model tarafından değil, kilitli yanıt anahtarını
okuyan deterministik betik tarafından yapılır.

| Denetim | Yalnız LLM | LLM + skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 8 | 8 / 8 |
| Tam karar sınıfı | hayır | evet |
| Adlandırılmış seçenek | hayır | evet |
| İnsan rotası | evet | evet |
| **İz puanı** | **20 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/masak-musteri-kabul/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/masak-musteri-kabul/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/masak-musteri-kabul/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/masak-musteri-kabul
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/masak-musteri-kabul/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
