# ETK/IYS ileti kararı

[English](../../skills/etk-iys-ileti-karari.md)

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 4 | 4 / 4 |
| Tam karar sınıfı yazıldı | hayır | hayır |
| Adlandırılmış seçenek yazıldı | hayır | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **20 / 100** | **80 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `ETK-E01`

[Kontrol yanıtı](../../assets/skills/etk-iys-ileti-karari/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/etk-iys-ileti-karari/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/etk-iys-ileti-karari/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/etk-iys-ileti-karari
```

Kontrol çalıştırması 4 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 4 tanesine atıf yaptı. Skill çalıştırması kilitli beklenen sınıf (`do-not-send`) yerine daha temkinli bir sınıf seçti; sınıf çağrısı insan incelemesinde kalır.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/etk-iys-ileti-karari/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6563.pdf) — Mevzuat Bilgi Sistemi |
| Resmî kaynak (yalnız metadata) | [Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2015/07/20150715-4.htm) — Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/etk-iys-ileti-karari/skill/public-method.md` |
| Sentetik şirket politikası | `demos/etk-iys-ileti-karari/sources/company-policy.md` |
| Sentetik vaka | `demos/etk-iys-ileti-karari/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/etk-iys-ileti-karari/evaluation/` |
| Taşınabilir skill | `demos/etk-iys-ileti-karari/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Bir bakışta iş sorusu

CRM ekibi, güncel rıza/IYS kanıtı sunmadan 48.000 eski perakende müşterisine
indirim SMS'i gönderebilir mi?

## Başlangıç olguları

- Mesaj indirim ve satın alma çağrısı içeriyor; hizmet bildirimi değil.
- Güncel rıza veya IYS durum anlık görüntüsü sağlanmadı.
- Kişi ve SMS kanalı düzeyinde kanıt listesi yok.
- Ret/çıkış ifadesi var.
- İstisna, bastırma kapısı ve insan onayını destekleyen kayıt sağlanmadı.

## Beklenen karar

Başlangıç için karar `do-not-send`, seçenek `suppress-unverified-audience` olur.
İnsan rotası CRM Owner + Compliance + Legal'dır.

## İş etkisi

Demo, kampanya ekibinin kitle büyüklüğünden önce ileti amacı, kişi-kanal kanıtı,
ret kontrolü, istisna olgusu ve bastırma kapısını incelemesini sağlar. Etki
nitelikseldir: doğrulanmamış kitlenin görünür olması, insan karar rotasının
netleşmesi ve kampanya incelemelerinin aynı sözleşmeyle tekrarlanması beklenir.
Ölçülmüş ROI veya finansal kazanım iddiası yoktur.

## Kaynak ve lisans sınırı

6563 sayılı ETK ile Ticari İletişim Yönetmeliği kamuya açık resmî yöntemdir.
Manifest, 2026-08-04 tarihinde alınan resmî URL, yayıncı ve SHA-256 metadatasını
taşır; resmî dosyalar `metadata-only` yaklaşımıyla yeniden dağıtılmaz ve uzun
pasajlar kopyalanmaz. Sentetik politika ve vaka MIT lisanslıdır. Güncellik,
yeniden kullanım ve uygulama insan Legal tarafından doğrulanır.

## Güvenlik ve insan sınırı

Bu içerik hukuki tavsiye veya nihai hukuki sonuç değildir. İnsan Legal/Compliance
kararın sahibidir. Skill yalnız analiz, eksik belirleme ve yönlendirme yapar;
mesaj gönderme, IYS kaydı değiştirme, kitle bastırma, kampanya başlatma/durdurma
veya başka otonom eylem yapmaz. Gerçek müşteri listesi demo girdisi olarak
kullanılmamalıdır.

## 12 senaryo durumu

On iki benzersiz senaryo cevap anahtarlarıyla kilitlenmiş ve 14 puanlık rubriğe
bağlanmıştır. Senaryolar bu makalede çalıştırılmış veya sonuçlandırılmış olarak
sunulmaz; biçimsel yürütme ve insan incelemesi beklenmektedir.

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/etk-iys-ileti-karari/etk-iys-ileti-karari-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.
