# Rekabet birleşme bildirimi

[English](../../skills/rekabet-birlesme-bildirimi.md)

## Kontrol ve skill: ölçülen

İki çalıştırma aynı kilitli vakayı aynı istemle yanıtladı. Tek fark, ikinci
çalıştırmada skill'in kurulu olmasıdır. Puanlama modele değil, kilitli senaryoya
bakan deterministik bir betiğe dayanır; sayıları herkes yeniden üretebilir.

| Yönetişim kapısı | Yalnız LLM | LLM + skill |
| --- | --- | --- |
| Atıf yapılan politika kuralı | 0 / 7 | 7 / 7 |
| Tam karar sınıfı yazıldı | hayır | evet |
| Adlandırılmış seçenek yazıldı | evet | evet |
| İnsan onay rotası adlandırıldı | evet | evet |
| Otonom yetki iddiası yok | evet | evet |
| **İz puanı** | **40 / 100** | **100 / 100** |

Host: GitHub Copilot coding agent (VS Code) · Model: Copilot agent default model · Tarih: 2026-08-04 · Senaryo: `RKB-01`

[Kontrol yanıtı](../../assets/skills/rekabet-birlesme-bildirimi/outputs/control-1.txt) · [Skill yanıtı](../../assets/skills/rekabet-birlesme-bildirimi/outputs/treatment-1.txt) · [Skor kartı](../../assets/skills/rekabet-birlesme-bildirimi/scorecard.json)

Yeniden üretmek için:

```bash
python tools/score_skill_answer.py scorecard --demo demos/rekabet-birlesme-bildirimi
```

Kontrol çalıştırması 7 politika kuralının 0 tanesine atıf yaptı skill çalıştırması 7 tanesine atıf yaptı. Tam karar sınıfını (`legal-notification-review`) yalnız skill çalıştırması yazdı.

Sınır: koşul başına tek çalıştırma, tek kilitli senaryo ve tek host. Bu tablo
makine ile denetlenebilir alt kümedir; 14 puanlık insan rubriği
`demos/rekabet-birlesme-bildirimi/evaluation/rubric.json` dosyasındadır.

## Kaynaktan skill'e

Bu skill'in hangi içerikten üretildiği aşağıdaki zincirle izlenir.

| Aşama | Üretilen içerik |
| --- | --- |
| Resmî kaynak (yalnız metadata) | [Birleşme ve Devralma Sayılan Haller ve Kontrol Kavramı Hakkında Kılavuz](https://www.rekabet.gov.tr/Dosya/kilavuzlar/birlesme-ve-devralma-sayilan-haller-ve-kontrol-kavrami-hakkinda-kilavuz.pdf) — Rekabet Kurumu |
| Resmî kaynak (yalnız metadata) | [Birleşme ve Devralma İşlemlerinde Ciro Hesaplanmasına İlişkin Kılavuz](https://www.rekabet.gov.tr/Dosya/bd-ciro-kilavuzu-20260504120128549.pdf) — Rekabet Kurumu |
| Kamuya açık yöntem özeti | `demos/rekabet-birlesme-bildirimi/skill/public-method.md` |
| Sentetik şirket politikası | `demos/rekabet-birlesme-bildirimi/sources/company-policy.md` |
| Sentetik vaka | `demos/rekabet-birlesme-bildirimi/sources/case-brief.md` |
| Kilitli değerlendirme | 12 senaryo ve 14 puanlık rubrik: `demos/rekabet-birlesme-bildirimi/evaluation/` |
| Taşınabilir skill | `demos/rekabet-birlesme-bildirimi/skill/SKILL.md` ve beş destek dosyası |
| Host paketleri | Cowork, Copilot/VS Code, Scout, Copilot Studio (harness ve classic) |

## Bir bakışta iş etkisi

| Soru | Etki |
|---|---|
| Hangi karar gerekir? | Temel vakada `legal-notification-review`; güvenli seçenek `hold-closing` |
| Hangi risk görünür olur? | `met` göstergesinin hukuki sonuç sanılması, `unknown` teknoloji statüsü, eksik danışman yönlendirmesi ve sürüm takibi |
| Kim karar verir? | Rekabet Hukuku Danışmanı; Finans yalnız precomputed ciro sonucunun sahibidir |
| Skill ne kazandırır? | Aynı beş sınıf, üç seçenek, kural izlenebilirliği ve 14 puanlık ölçülebilir çıktı |
| Skill ne yapmaz? | Ciro/eşik hesabı, filing kararı, bildirim, yeniden yapılandırma, imza veya kapanış |

## Nasıl çalışır?

Skill, iki Rekabet Kurumu kılavuzunu metadata-only manifestle sınırlar; PDF'leri
yeniden dağıtmaz veya resmi metni kopyalamaz. Kısa kamu yöntemi sorularını
sentetik BKP-1.0 şirket politikasından ve sentetik RKB-2608 işlem olgularından
ayırır.

Temel vakada `met` yalnız Finans'ın önceden hesaplanmış göstergesidir. Bildirim
gerekliliğine ilişkin hukuki sonuç değildir. Teknoloji teşebbüsü durumu
`unknown` kalır, Rekabet Hukuku Danışmanı incelemesi beklenir ve kayıtlı kapanış
yönlendirmesi olmadan kapı açılmaz.

## İndirmeler

Aşağıdaki paketler ortak release fabrikasıyla deterministik üretilmiş ve
SHA-256 manifestine bağlanmıştır:

- [Cowork skill paketi](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-cowork.skill)
- [Copilot VS Code ZIP](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-vscode.zip)
- [Scout ZIP](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/skills/rekabet-birlesme-bildirimi/rekabet-birlesme-bildirimi-copilot-studio-classic-setup.zip)

Classic setup ZIP, Copilot Studio için kurulum malzemesi ve yönerge paketidir;
doğrudan ajan içe aktarma paketi değildir.

## Değerlendirme

Demo, cevap anahtarı prompttan ayrı tam 12 kilitli senaryo ve her boyutu açık
ankrajlı 14 puanlık rubrik içerir. Puanlama doğru sınıf/seçenek kadar kontrol
olgusu envanterini, hesaplama yapmama disiplinini, teknoloji statüsü sınırını,
kaynak izlenebilirliğini, insan yetkisini ve kapanış kapısını ölçer.

Bu içerik eğitim ve yönetişim tasarımı içindir. Nihai hukuki karar ve bütün işlem
eylemleri yetkili insanlarda kalır.