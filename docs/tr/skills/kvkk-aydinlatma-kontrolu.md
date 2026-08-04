# KVKK aydınlatma kontrolü

**Alan:** Veri koruma<br>
**Hedef ekip:** Privacy, Compliance ve ürün ekipleri

Aydınlatma, rıza ve aktarım boşluklarını insan yayın kapısına bağlar.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [6698 sayılı Kişisel Verilerin Korunması Kanunu](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf) | Mevzuat Bilgi Sistemi |
| Resmî kaynak | [Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ](https://www.resmigazete.gov.tr/eskiler/2018/03/20180310-5.htm) | Resmî Gazete |
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

Kilitli değerlendirme `revise-before-launch` karar sınıfını,
`separate-notice-and-consent` seçeneğini ve 5 kural
kimliğini bekler. Nihai insan rotası: Privacy Counsel · Data Protection/Compliance · Product Owner.

## LLM only ve LLM + skill

Aynı vaka ve istem iki kez çalıştırıldı. Tek fark, ikinci çalıştırmada skill'in
yüklü olmasıdır. Puanlama bir model tarafından değil, kilitli yanıt anahtarını
okuyan deterministik betik tarafından yapılır.

| Denetim | Yalnız LLM | LLM + skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 5 | 5 / 5 |
| Tam karar sınıfı | hayır | evet |
| Adlandırılmış seçenek | hayır | evet |
| İnsan rotası | hayır | evet |
| **İz puanı** | **10 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/kvkk-aydinlatma-kontrolu/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/kvkk-aydinlatma-kontrolu
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/kvkk-aydinlatma-kontrolu/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
