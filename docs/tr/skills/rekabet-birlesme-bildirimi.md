# Rekabet birleşme bildirimi

**Alan:** Birleşme ve devralmalar<br>
**Hedef ekip:** M&A, Finans ve Rekabet Hukuku ekipleri

Ön hesaplama göstergelerini hukuki bildirim kararı ve kapanış kapısından ayırır.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Birleşme ve Devralma Sayılan Haller ve Kontrol Kavramı Hakkında Kılavuz](https://www.rekabet.gov.tr/Dosya/kilavuzlar/birlesme-ve-devralma-sayilan-haller-ve-kontrol-kavrami-hakkinda-kilavuz.pdf) | Rekabet Kurumu |
| Resmî kaynak | [Birleşme ve Devralma İşlemlerinde Ciro Hesaplanmasına İlişkin Kılavuz](https://www.rekabet.gov.tr/Dosya/bd-ciro-kilavuzu-20260504120128549.pdf) | Rekabet Kurumu |
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

Kilitli değerlendirme `legal-notification-review` karar sınıfını,
`hold-closing` seçeneğini ve 7 kural
kimliğini bekler. Nihai insan rotası: Rekabet Hukuku Danışmanı · Finans · Sponsor.

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

[Kontrol yanıtı](../../assets/skills/rekabet-birlesme-bildirimi/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/rekabet-birlesme-bildirimi/outputs/treatment-1.txt) ·
[Skor kartı](../../assets/skills/rekabet-birlesme-bildirimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/rekabet-birlesme-bildirimi
```

Bu tek senaryo ve tek host karşılaştırmasıdır; üretim doğruluğu veya mevzuata
uygunluk kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-scout.zip)
- [Copilot Studio GitHub harness](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic kurulum](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-classic-setup.zip)

Classic paket doğrudan solution import değildir; hedef Copilot Studio ortamında
insan tarafından uygulanacak kurulum malzemesidir.

## Yeniden kullanım

Kaynak manifesti, sentetik girdiler, senaryolar, ham yanıtlar ve skor kartı
`demos/rekabet-birlesme-bildirimi/` altında public'tir. Aynı yapıyı kendi kaynağınız için kopyalayın,
ancak yalnız paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik ve yeniden
kullanım](../safety.md) sınırlarını inceleyin.
