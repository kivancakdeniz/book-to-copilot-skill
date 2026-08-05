# İSG risk değerlendirmesi: değişiklikten devreye alma onayına

**Alan:** İş sağlığı ve güvenliği<br>
**Hedef ekip:** İSG, operasyon, bakım ve mühendislik ekipleri

Değişiklik risklerini katılım, kontrol ve devreye alma kanıtlarıyla görünür kılar.

## Dönüştürülen kaynak

Bu örnek, resmî yöntem kaynaklarını sentetik kurum politikası ve sentetik vakayla
birleştirir. Ham resmî belge pakete konmaz.

| Tür | Kaynak | Yayıncı / durum |
| --- | --- | --- |
| Resmî kaynak | [İş Sağlığı ve Güvenliği Risk Değerlendirmesi Yönetmeliği](https://www.resmigazete.gov.tr/eskiler/2012/12/20121229-13.htm) | T.C. Resmî Gazete |
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
`renew-assessment` (değerlendirmeyi yenile), önerilen seçenek olarak
`hold-commissioning` (devreye almayı beklet) ve 7
kural kimliğinin kullanılması beklenir. Nihai
incelemeden sorumlu roller:
`İşveren` · `İSG profesyonelleri` · `çalışan temsilcileri`.

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

[Kontrol yanıtı](../../assets/skills/isg-risk-degerlendirme/outputs/control-1.txt) ·
[Skill yanıtı](../../assets/skills/isg-risk-degerlendirme/outputs/treatment-1.txt) ·
[Puan kartı](../../assets/skills/isg-risk-degerlendirme/scorecard.json)

```bash
python tools/score_skill_answer.py scorecard --demo demos/isg-risk-degerlendirme
```

Bu karşılaştırmada her koşulda tek senaryo ve tek çalıştırma ortamı kullanılmıştır;
sonuçlar üretim doğruluğunun veya mevzuata uygunluğun kanıtı değildir.

## Copilot paketleri

- [Cowork `.skill`](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-cowork.skill)
- [VS Code için GitHub Copilot](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-vscode.zip)
- [Microsoft Scout](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-scout.zip)
- [Copilot Studio GitHub bağlantı paketi](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-github-harness.zip)
- [Copilot Studio klasik kurulum paketi](../../downloads/skills/isg-risk-degerlendirme/isg-risk-degerlendirme-copilot-studio-classic-setup.zip)

Klasik paket doğrudan içe aktarılabilen bir Copilot Studio çözümü değildir; hedef
ortamda elle uygulanacak kurulum dosyaları ve yönergeleri içerir.

## Yeniden kullanım

Kaynak bildirim dosyası, sentetik girdiler, senaryolar, ham yanıtlar ve puan kartı
`demos/isg-risk-degerlendirme/` altında herkese açıktır. Aynı yapıyı kendi kaynağınız için
kopyalayın; ancak yalnızca paylaşma hakkınız olan içeriği yayımlayın. [Güvenlik
ve yeniden kullanım](../safety.md) sınırlarını inceleyin.
