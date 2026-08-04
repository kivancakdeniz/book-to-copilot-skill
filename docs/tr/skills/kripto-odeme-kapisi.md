# Kripto ödeme kapısı

[English](../../skills/kripto-odeme-kapisi.md)

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 6 | 6 / 6 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `KRP-01`

[Kontrol yanıtı](../../assets/skills/kripto-odeme-kapisi/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/kripto-odeme-kapisi/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/kripto-odeme-kapisi/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/kripto-odeme-kapisi
```

Kontrol çalıştırması 6 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 6 tanesine atıf yaptı. Tam karar sınıfını (`reject-payment-flow`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/kripto-odeme-kapisi/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Ödemelerde Kripto Varlıkların Kullanılmamasına Dair Yönetmelik](https://www.resmigazete.gov.tr/eskiler/2021/04/20210416-4.htm) — Türkiye Cumhuriyet Merkez Bankası / T.C. Resmî Gazete |
| Kamuya açık yöntem özeti | `demos/kripto-odeme-kapisi/skill/public-method.md` |
| Sentetik şirket politikası | `demos/kripto-odeme-kapisi/sources/company-policy.md` |
| Sentetik vaka | `demos/kripto-odeme-kapisi/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/kripto-odeme-kapisi/evaluation/` |
| Taşınabilir skill | `demos/kripto-odeme-kapisi/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Bir bakışta

| Alan | Değer |
|---|---|
| Problem | USDT'nin satıcı alımını doğrudan kapattığı checkout akışının ürün sınırını incelemek |
| Baseline | Kripto doğrudan ödeme işlevinde; ödeme hizmeti aracısı akışta; lansman talep ediliyor |
| Beklenen sınıf | `reject-payment-flow` |
| Beklenen seçenek | `remove-crypto-checkout` |
| İnsan kararı | Payments Counsel + Compliance + Product |

## İş etkisi

Demo, hızlı lansman baskısı altındaki dağınık ürün tartışmasını izlenebilir bir
varlık, işlev, aracı, mutabakat, karar ve lansman kapısı kaydına dönüştürür.
Beklenen iş etkisi daha erken ürün sınırı tespiti, daha az geç aşama yeniden
çalışma ve insan karar sahiplerine daha tutarlı kanıt paketidir. Üretim sonucu,
mevzuata uyum veya hukuki yeterlilik garantisi değildir.

## Kaynak ve güvenlik

Kamusal yöntem kaynağı TCMB'nin T.C. Resmî Gazete'de yayımlanan düzenlemesidir.
Paket resmi içeriği yeniden dağıtmaz; yalnız resmi URL, yayıncı, 2026-08-04
erişim tarihi, SHA-256 ve yeniden kullanım uyarısı taşır. Skill kısa ve atıflı
yöntem özeti kullanır; mevzuat metnini kopyalamaz. Karar sınıfları ve seçenekler
MIT lisanslı sentetik Kurgusal Ödeme politikasından gelir.

## İnsan ve kapsam sınırı

Bu skill hukuki tavsiye değildir. Payments Counsel, Compliance ve Product karar
verir. Copilot onay, lansman, ödeme, transfer, ürün değişikliği veya durdurma
yapmaz. Sağlanan checkout akışının ötesinde yatırım ya da transfer hukukuna
ilişkin görüş vermez.

## 12 kilitli senaryo

| Kimlik | Odak | Beklenen sınıf | Beklenen seçenek |
|---|---|---|---|
| KRP-01 | Doğrudan USDT satıcı ödemesi | `reject-payment-flow` | `remove-crypto-checkout` |
| KRP-02 | Ödeme dışı piyasa bilgi ekranı | `approve-nonpayment-service` | `launch-current-flow` |
| KRP-03 | Checkout'tan kriptonun çıkarılması | `revise-product-boundary` | `remove-crypto-checkout` |
| KRP-04 | Eksik mutabakat/dönüşüm | `hold-for-flow-evidence` | `remove-crypto-checkout` |
| KRP-05 | Bilinmeyen aracı rolü | `hold-for-flow-evidence` | `redesign-nonpayment-service` |
| KRP-06 | Satıcı alımından ayrık transfer | `escalate-payments-counsel` | `redesign-nonpayment-service` |
| KRP-07 | Statik eğitim içeriği | `approve-nonpayment-service` | `redesign-nonpayment-service` |
| KRP-08 | Aracısız doğrudan satıcı transferi | `reject-payment-flow` | `remove-crypto-checkout` |
| KRP-09 | Yatırım uygunluğu görüşü | `escalate-payments-counsel` | `redesign-nonpayment-service` |
| KRP-10 | Çelişkili akış sürümleri | `hold-for-flow-evidence` | `remove-crypto-checkout` |
| KRP-11 | TRY checkout ve ayrık analiz | `revise-product-boundary` | `redesign-nonpayment-service` |
| KRP-12 | Ödeme işlevinin yeniden eklenmesi | `reject-payment-flow` | `remove-crypto-checkout` |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/kripto-odeme-kapisi/kripto-odeme-kapisi-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.
