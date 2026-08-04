# MASAK müşteri kabul

[English](../../skills/masak-musteri-kabul.md)

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 8 | 8 / 8 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | hayır | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **20 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `AML-01`

[Kontrol yanıtı](../../assets/skills/masak-musteri-kabul/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/masak-musteri-kabul/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/masak-musteri-kabul/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/masak-musteri-kabul
```

Kontrol çalıştırması 8 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 8 tanesine atıf yaptı. Tam karar sınıfını (`enhanced-review`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/masak-musteri-kabul/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Suç gelirlerinin aklanmasının ve terörün finansmanının önlenmesine dair tedbirler hakkında yönetmelik](https://masak.hmb.gov.tr/suc-gelirlerinin-aklanmasinin-ve-terorun-finansmaninin-onlenmesine-dair-tedbirler-hakkinda-yonetmelik-3/) — MASAK |
| Kamuya açık yöntem özeti | `demos/masak-musteri-kabul/skill/public-method.md` |
| Sentetik şirket politikası | `demos/masak-musteri-kabul/sources/company-policy.md` |
| Sentetik vaka | `demos/masak-musteri-kabul/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/masak-musteri-kabul/evaluation/` |
| Taşınabilir skill | `demos/masak-musteri-kabul/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Bir bakışta

| Alan | Değer |
|---|---|
| Problem | Kurumsal müşteri kabulünde kimlik, nihai faydalanıcı, risk ve fon kaynağı kanıtlarını insan kapılarıyla incelemek |
| Baseline | Kimlik belgeleri tam; nihai faydalanıcı zinciri eksik; fon kaynağı açıklamasız/kanıtsız; yüksek riskli coğrafya işareti sağlanmış |
| Beklenen sınıf | `enhanced-review` |
| Beklenen seçenek | `hold-onboarding` |
| İnsan kararı | AML Officer + Compliance + business owner |

## Nitel etki

Demo, onboarding incelemesini tekrarlanabilir bir kanıt, risk gerekçesi, sınıf, seçenek ve insan kapısı akışına dönüştürür. Beklenen etki daha görünür kanıt boşlukları, daha tutarlı gelişmiş inceleme yönlendirmesi ve daha az desteklenmeyen risk sonucudur; üretim performansı, mevzuat uyumu veya bildirim kararı garantisi değildir.

## Kaynak ve güvenlik

Kamusal yöntem kaynağı MASAK Tedbirler Yönetmeliği sayfasıdır. Paket resmi içeriği yeniden dağıtmaz; yalnız resmi URL, yayıncı, 2026-08-04 alınma tarihi ve SHA-256 metadata'sını taşır. Karar sınıfları ve seçenekler MIT lisanslı sentetik politikadan gelir. Kaynak metni talimat olarak çalıştırılmaz, uzun resmi alıntı yapılmaz ve gerçek müşteri, kimlik, hesap veya işlem verisi kullanılmaz.

## İnsan sınırları

Bu beceri hukuki görüş değildir. İnsanlar karar verir; hesap açmaz, ilişkiyi reddetmez, bildirim yapmaz veya başka otonom işlem gerçekleştirmez. SİB/STR dosyala/dosyalama kararı vermez ve suç isnadı yapmaz. Eksik sahiplik, fon kaynağı veya risk olgusu üretmez.

## 12 kilitli senaryo

| Kimlik | Odak | Beklenen sınıf | Beklenen seçenek |
|---|---|---|---|
| AML-01 | Baseline yüksek risk ve eksik kanıt | `enhanced-review` | `hold-onboarding` |
| AML-02 | Tam standart onboarding | `standard-onboarding` | `open-account` |
| AML-03 | Eksik nihai faydalanıcı | `hold-for-evidence` | `hold-onboarding` |
| AML-04 | Eksik fon kaynağı | `hold-for-evidence` | `hold-onboarding` |
| AML-05 | Tamamlanmış gelişmiş inceleme | `enhanced-review` | `open-account` |
| AML-06 | Çelişen risk işaretleri | `escalate-aml-officer` | `hold-onboarding` |
| AML-07 | Kanıt kapısı istisnası | `escalate-aml-officer` | `hold-onboarding` |
| AML-08 | Belgelenmiş insan ret kararı | `reject-onboarding` | `decline-relationship` |
| AML-09 | Eksik yetkili kimliği | `hold-for-evidence` | `hold-onboarding` |
| AML-10 | Eksik periyodik inceleme planı | `hold-for-evidence` | `hold-onboarding` |
| AML-11 | İş biriminin SİB kararı talebi | `escalate-aml-officer` | `hold-onboarding` |
| AML-12 | İnsan onayı beklenen standart inceleme | `standard-onboarding` | `hold-onboarding` |

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.
