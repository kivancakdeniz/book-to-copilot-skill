# TİTCK ilaç tanıtımı: hedef kitle ve yayın kapısı

**Alan:** İlaç ve sağlık iletişimi<br>
**Hedef ekip:** Medical, Regulatory, Legal ve pazarlama ekipleri

Ürün statüsü, hedef kitle ve kanal erişimini insan yayın incelemesine bağlar.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik](https://www.titck.gov.tr/mevzuat/beseri-tibbi-urunlerin-tanitim-faaliyetleri-hakkinda-yonetmelik-27122018172726) | Türkiye İlaç ve Tıbbî Cihaz Kurumu (TİTCK) |
| Resmî kaynak | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik - Resmî Gazete yayımı](https://www.resmigazete.gov.tr/eskiler/2015/07/20150703-2.htm) | T.C. Resmî Gazete |
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

Kilitli değerlendirme `do-not-publish` karar sınıfını,
`professional-channel-review` seçeneğini ve 7 kural
kimliğini bekler. Nihai insan rotası: Medical · Regulatory · Legal.

## LLM only ve LLM + skill

Aynı vaka ve istem iki kez çalıştırıldı. Tek fark, ikinci çalıştırmada skill'in
yüklü olmasıdır. Puanlama bir model tarafından değil, kilitli yanıt anahtarını
okuyan deterministik betik tarafından yapılır.

| Denetim | Yalnız LLM | LLM + skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı | hayır | evet |
| Adlandırılmış seçenek | evet | evet |
| İnsan rotası | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/titck-ilac-tanitimi/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/titck-ilac-tanitimi/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/titck-ilac-tanitimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/titck-ilac-tanitimi
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/titck-ilac-tanitimi/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
