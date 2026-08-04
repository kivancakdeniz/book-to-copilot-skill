# KVKK aydınlatma kontrolü

[English](../../skills/kvkk-aydinlatma-kontrolu.md)

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 5 | 5 / 5 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | hayır | evet |
| İnsan onay rotası adlandırıldı | hayır | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **10 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `KVK-E01`

[Kontrol yanıtı](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/kvkk-aydinlatma-kontrolu/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/kvkk-aydinlatma-kontrolu/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/kvkk-aydinlatma-kontrolu
```

Kontrol çalıştırması 5 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 5 tanesine atıf yaptı. Tam karar sınıfını (`revise-before-launch`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/kvkk-aydinlatma-kontrolu/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [6698 sayılı Kişisel Verilerin Korunması Kanunu](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf) — Mevzuat Bilgi Sistemi |
| Resmî kaynak (yalnız metadata) | [Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ](https://www.resmigazete.gov.tr/eskiler/2018/03/20180310-5.htm) — Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/kvkk-aydinlatma-kontrolu/skill/public-method.md` |
| Sentetik şirket politikası | `demos/kvkk-aydinlatma-kontrolu/sources/company-policy.md` |
| Sentetik vaka | `demos/kvkk-aydinlatma-kontrolu/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/kvkk-aydinlatma-kontrolu/evaluation/` |
| Taşınabilir skill | `demos/kvkk-aydinlatma-kontrolu/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Bir bakışta iş sorusu

Sentetik B2B SaaS potansiyel müşteri formu, mevcut aydınlatma taslağı ve birleşik
pazarlama rızasıyla yayına çıkabilir mi?

## Başlangıç olguları

- Form ad, kurumsal e-posta, telefon, IP ve kampanya kaynağı topluyor.
- Bir yurt dışı işleyen kullanılıyor; aktarım yolu ve güvence ayrıntıları yok.
- Taslak veri sorumlusunu, amaçları ve yöntemi gösteriyor.
- Alıcı grupları, aktarım bağlamı, hukuki sebep eşlemesi ve ilgili kişi
  hakları/iletişim yolu eksik.
- Pazarlama rızası aydınlatma kabulüne bağlanmış.

## Beklenen karar

Başlangıç için karar `revise-before-launch`, seçenek
`separate-notice-and-consent` olur. İnsan rotası Privacy Counsel + Data
Protection/Compliance + Product Owner'dır.

## İş etkisi

Demo, ürün ekibinin “metin var mı?” kontrolünü veri envanteri, aydınlatma
tamamlığı, rıza ayrımı, aktarım kanıtı ve imzalı yayın kapısıyla izlenebilir bir
karara dönüştürür. Etki nitelikseldir: eksiklerin daha erken görünmesi, karar
sahipliğinin netleşmesi ve değerlendirmelerin aynı sözleşmeyle tekrarlanması
beklenir. Ölçülmüş ROI veya finansal kazanım iddiası yoktur.

## Kaynak ve lisans sınırı

6698 sayılı KVKK ile Aydınlatma Tebliği kamuya açık resmî yöntemdir. Manifest,
2026-08-04 tarihinde alınan resmî URL, yayıncı ve SHA-256 metadatasını taşır;
resmî dosyalar `metadata-only` yaklaşımıyla yeniden dağıtılmaz ve uzun pasajlar
kopyalanmaz. Sentetik politika ve vaka MIT lisanslıdır. Güncellik, yeniden
kullanım ve uygulama insan Legal tarafından doğrulanır.

## Güvenlik ve insan sınırı

Bu içerik hukuki tavsiye veya nihai hukuki sonuç değildir. İnsan Legal/Compliance
kararın sahibidir. Skill yalnız analiz, eksik belirleme ve yönlendirme yapar;
yayına alma, rıza toplama, veri aktarma, kayıt değiştirme veya başka otonom eylem
yapmaz. Gerçek kişisel veri demo girdisi olarak kullanılmamalıdır.

## 12 senaryo durumu

On iki benzersiz senaryo cevap anahtarlarıyla kilitlenmiş ve 14 puanlık rubriğe
bağlanmıştır. Senaryolar bu makalede çalıştırılmış veya sonuçlandırılmış olarak
sunulmaz; biçimsel yürütme ve insan incelemesi beklenmektedir.

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/kvkk-aydinlatma-kontrolu/kvkk-aydinlatma-kontrolu-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.
