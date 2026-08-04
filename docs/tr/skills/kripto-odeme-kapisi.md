# Kripto ödeme kapısı

**Alan:** Ödeme hizmetleri ve kripto varlıklar<br>
**Hedef ekip:** Payments, Compliance, Legal ve ürün ekipleri

Kripto işlevinin ödeme akışındaki rolünü ürün sınırı ve lansman kapısıyla inceler.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Ödemelerde Kripto Varlıkların Kullanılmamasına Dair Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210416-4.htm) | Türkiye Cumhuriyet Merkez Bankası / T.C. Resmî Gazete |
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

Kilitli değerlendirme `reject-payment-flow` karar sınıfını,
`remove-crypto-checkout` seçeneğini ve 6 kural
kimliğini bekler. Nihai insan rotası: Payments Counsel · Compliance · Product.

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

[Kontrol yanıtı](../../assets/skills/kripto-odeme-kapisi/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/kripto-odeme-kapisi/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/kripto-odeme-kapisi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/kripto-odeme-kapisi
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/kripto-odeme-kapisi/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
