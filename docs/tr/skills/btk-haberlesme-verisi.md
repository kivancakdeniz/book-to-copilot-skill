# BTK haberleşme verisi

**Alan:** Telekom ve mahremiyet<br>
**Hedef ekip:** Telekom Compliance, Privacy, DPO ve CRM ekipleri

Konum ve trafik verisi kullanımını amaç, rıza ve saklama kapılarıyla sınırlar.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Elektronik Haberleşme Sektöründe Kişisel Verilerin İşlenmesi ve Gizliliğin Korunmasına İlişkin Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2020/12/20201204-13.htm) | Bilgi Teknolojileri ve İletişim Kurumu / T.C. Resmî Gazete |
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

Kilitli değerlendirme `stop-processing` karar sınıfını,
`consent-first-redesign` seçeneğini ve 7 kural
kimliğini bekler. Nihai insan rotası: Privacy Counsel · Telecom Compliance · DPO.

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

[Kontrol yanıtı](../../assets/skills/btk-haberlesme-verisi/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/btk-haberlesme-verisi/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/btk-haberlesme-verisi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/btk-haberlesme-verisi
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/btk-haberlesme-verisi/btk-haberlesme-verisi-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/btk-haberlesme-verisi/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
