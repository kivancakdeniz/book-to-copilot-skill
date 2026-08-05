# KVKK aydınlatma kontrolü

**Alan:** Kişisel verilerin korunması<br>
**Hedef ekip:** Kişisel verilerin korunması, uyum ve ürün ekipleri

Aydınlatma, rıza ve aktarım eksiklerini yayımlamadan önce yetkili incelemesine sunar.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [6698 sayılı Kişisel Verilerin Korunması Kanunu](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf) | Mevzuat Bilgi Sistemi |
| Resmî kaynak | [Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ](https://www.resmigazete.gov.tr/eskiler/2018/03/20180310-5.htm) | Resmî Gazete |
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
`revise-before-launch` (kullanıma sunmadan önce düzelt), önerilen seçenek olarak
`separate-notice-and-consent` (aydınlatma ile rızayı ayır) ve 5
kural kimliğinin kullanılması beklenir. Nihai
incelemeden sorumlu roller:
`Privacy Counsel` (Kişisel verilerin korunması hukuk danışmanı) · `Data Protection/Compliance` (Kişisel verilerin korunması ve uyum) · `Product Owner` (Ürün sorumlusu).

## Yalnızca LLM ve LLM + Agent Skill

Aynı vaka ve istem iki kez çalıştırıldı. İkinci çalıştırmada ayrıca Agent Skill
yüklüdür. Her iki yanıtı da başka bir model değil, önceden belirlenmiş yanıt
anahtarını kullanan deterministik bir betik puanlar.

| Denetim | Yalnızca LLM | LLM + Agent Skill |
| --- | ---: | ---: |
| Politika kuralı atfı | 0 / 5 | 5 / 5 |
| Beklenen karar sınıfıyla tam eşleşme | hayır | evet |
| Önerilen seçenek | hayır | evet |
| Yetkili incelemeye yönlendirme | hayır | evet |
| **Karar izlenebilirliği puanı** | **10 / 100** | **100 / 100** |

[Kontrol yanıtı](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/treatment-1.txt) ·
[Puan kartı](../../assets/skills/kvkk-aydinlatma-kontrolu/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/kvkk-aydinlatma-kontrolu
```

Bu karşılaştırmada her koşulda tek senaryo ve tek çalıştırma ortamı kullanılmıştır;
sonuçlar üretim doğruluğunun veya mevzuata uygunluğun kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-scout.zip)
- [Copilot Studio GitHub bağlantı paketi](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-github-harness.zip)
- [Copilot Studio klasik kurulum paketi](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-classic-setup.zip)

Klasik paket doğrudan içe aktarılabilen bir Copilot Studio çözümü değildir; hedef
ortamda elle uygulanacak kurulum dosyaları ve yönergeleri içerir.

## Yeniden kullanım

Kaynak bildirim dosyası, sentetik girdiler, senaryolar, ham yanıtlar ve puan kartı
`demos/kvkk-aydinlatma-kontrolu/` altında herkese açıktır. Aynı yapıyı kendi kaynağınız için
kopyalayın; ancak yalnızca paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik
ve yeniden kullanım](../safety.md) sınırlarını inceleyin.
