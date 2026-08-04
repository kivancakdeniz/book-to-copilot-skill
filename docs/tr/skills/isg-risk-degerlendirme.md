# İSG risk değerlendirmesi: değişiklikten devreye alma kapısına

**Alan:** İş sağlığı ve güvenliği<br>
**Hedef ekip:** İSG, operasyon, bakım ve mühendislik ekipleri

Değişiklik risklerini katılım, kontrol ve devreye alma kanıtlarıyla görünür kılar.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [İş Sağlığı ve Güvenliği Risk Değerlendirmesi Yönetmeliği](https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm) | T.C. Resmî Gazete |
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

Kilitli değerlendirme `renew-assessment` karar sınıfını,
`hold-commissioning` seçeneğini ve 7 kural
kimliğini bekler. Nihai insan rotası: İşveren · İSG profesyonelleri · çalışan temsilcileri.

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

[Kontrol yanıtı](../../assets/skills/isg-risk-degerlendirme/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/isg-risk-degerlendirme/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/isg-risk-degerlendirme/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/isg-risk-degerlendirme
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/isg-risk-degerlendirme/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
