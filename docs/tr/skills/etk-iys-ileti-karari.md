# ETK/IYS ileti kararı

**Alan:** Ticari elektronik ileti<br>
**Hedef ekip:** CRM, Compliance ve Legal ekipleri

Kampanya kitlesini kişi-kanal kanıtı ve bastırma kapısıyla inceler.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6563.pdf) | Mevzuat Bilgi Sistemi |
| Resmî kaynak | [Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2015/07/20150715-4.htm) | Resmî Gazete |
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

Kilitli değerlendirme `do-not-send` karar sınıfını,
`suppress-unverified-audience` seçeneğini ve 4 kural
kimliğini bekler. Nihai insan rotası: CRM Owner · Compliance · Legal.

## LLM only ve LLM + skill

Aynı vaka ve istem iki kez çalıştırıldı. Tek fark, ikinci çalıştırmada skill'in
yüklü olmasıdır. Puanlama bir model tarafından değil, kilitli yanıt anahtarını
okuyan deterministik betik tarafından yapılır.

| Denetim | Yalnız LLM | LLM + skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 4 | 4 / 4 |
| Tam karar sınıfı | hayır | hayır |
| Adlandırılmış seçenek | hayır | evet |
| İnsan rotası | evet | evet |
| **İz puanı** | **20 / 100** | **80 / 100** |

[Kontrol yanıtı](../../assets/skills/etk-iys-ileti-karari/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/etk-iys-ileti-karari/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/etk-iys-ileti-karari/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/etk-iys-ileti-karari
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/etk-iys-ileti-karari/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
