# TİTCK ilaç tanıtımı: hedef kitle ve yayımlama öncesi inceleme

**Alan:** İlaç ve sağlık iletişimi<br>
**Hedef ekip:** Medikal, ruhsatlandırma, hukuk ve pazarlama ekipleri

Ürün statüsü, hedef kitle ve kanal erişimini yayımlamadan önce yetkili incelemesine sunar.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik](https://www.titck.gov.tr/mevzuat/beseri-tibbi-urunlerin-tanitim-faaliyetleri-hakkinda-yonetmelik-27122018172726) | Türkiye İlaç ve Tıbbî Cihaz Kurumu (TİTCK) |
| Resmî kaynak | [Beşerî Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik - Resmî Gazete yayımı](https://www.resmigazete.gov.tr/eskiler/2015/07/20150703-2.htm) | T.C. Resmî Gazete |
| Sentetik politika ve vaka | Sentetik politika ve vaka, demo dizininde MIT lisansıyla yayımlanır | — |

## Üretilen Agent Skill

Agent Skill, kaynak içeriği tek bir özete sıkıştırmak yerine yeniden kullanılabilir altı
dosyaya ayırır:

- `SKILL.md`: ne zaman kullanılacağı ve çalışma sırası;
- `public-method.md`: resmî kaynaktan çıkarılan bağımsız yöntem özeti;
- `company-policy.md`: değişmeyen kimliklere sahip sentetik kurum kuralları;
- `evidence-map.md`: hangi iddianın hangi kaynaktan gelebileceği;
- `output-schema.md`: beklenen yanıt yapısı;
- `scenario-guide.md`: eksik bilgi, çelişki ve yanıt vermekten kaçınma davranışı.

Önceden belirlenen değerlendirmede karar sınıfı olarak
`do-not-publish` (yayımlanmamalı), önerilen seçenek olarak
`professional-channel-review` (mesleki kanallara uygunluk incelemesi) ve 7
kural kimliğinin kullanılması beklenir. Nihai
incelemeden sorumlu roller:
`Medical` (Medikal) · `Regulatory` (Ruhsatlandırma ve mevzuat) · `Legal` (Hukuk).

## Yalnızca LLM ve LLM + Agent Skill

Aynı vaka ve istem iki kez çalıştırıldı. İkinci çalıştırmada ayrıca Agent Skill
yüklüdür. Her iki yanıtı da başka bir model değil, önceden belirlenmiş yanıt
anahtarını kullanan deterministik bir betik puanlar.

| Denetim | Yalnızca LLM | LLM + Agent Skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 7 | 7 / 7 |
| Beklenen karar sınıfıyla tam eşleşme | hayır | evet |
| Önerilen seçenek | evet | evet |
| Yetkili incelemeye yönlendirme | evet | evet |
| **Karar izlenebilirliği puanı** | **40 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/titck-ilac-tanitimi/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/titck-ilac-tanitimi/outputs/treatment-1.txt) ·
[Puan kartı](../../assets/skills/titck-ilac-tanitimi/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/titck-ilac-tanitimi
```

Bu karşılaştırmada her koşulda tek senaryo ve tek çalıştırma ortamı kullanılmıştır;
sonuçlar üretim doğruluğunun veya mevzuata uygunluğun kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-scout.zip)
- [Copilot Studio GitHub bağlantı paketi](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-github-harness.zip)
- [Copilot Studio klasik kurulum paketi](../../downloads/skills/titck-ilac-tanitimi/titck-ilac-tanitimi-copilot-studio-classic-setup.zip)

Klasik paket doğrudan içe aktarılabilen bir Copilot Studio çözümü değildir; hedef
ortamda elle uygulanacak kurulum dosyaları ve yönergeleri içerir.

## Yeniden kullanım

Kaynak bildirim dosyası, sentetik girdiler, senaryolar, ham yanıtlar ve puan kartı
`demos/titck-ilac-tanitimi/` altında herkese açıktır. Aynı yapıyı kendi kaynağınız için
kopyalayın; ancak yalnızca paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik
ve yeniden kullanım](../safety.md) sınırlarını inceleyin.
