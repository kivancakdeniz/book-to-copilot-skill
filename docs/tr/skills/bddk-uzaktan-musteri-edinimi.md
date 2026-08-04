# BDDK uzaktan müşteri edinimi

**Alan:** Bankacılık<br>
**Hedef ekip:** Dijital bankacılık, güvenlik, Uyum ve Hukuk ekipleri

Uzaktan edinim akışını kanıt, kontrol ve canlıya geçiş kapılarıyla sınar.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Bankalarca Kullanılacak Uzaktan Kimlik Tespiti Yöntemlerine ve Elektronik Ortamda Sözleşme İlişkisinin Kurulmasına İlişkin Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210401-7.htm) | Resmî Gazete |
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

Kilitli değerlendirme `reject-flow` karar sınıfını,
`manual-onboarding-fallback` seçeneğini ve 7 kural
kimliğini bekler. Nihai insan rotası: Güvenlik · Uyum · Hukuk.

## LLM only ve LLM + skill

Aynı vaka ve istem iki kez çalıştırıldı. Tek fark, ikinci çalıştırmada skill'in
yüklü olmasıdır. Puanlama bir model tarafından değil, kilitli yanıt anahtarını
okuyan deterministik betik tarafından yapılır.

| Denetim | Yalnız LLM | LLM + skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı | hayır | hayır |
| Adlandırılmış seçenek | evet | evet |
| İnsan rotası | evet | evet |
| **İz puanı** | **40 / 100** | **80 / 100** |

[Kontrol yanıtı](../../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/bddk-uzaktan-musteri-edinimi/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/bddk-uzaktan-musteri-edinimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/bddk-uzaktan-musteri-edinimi
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/bddk-uzaktan-musteri-edinimi/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
