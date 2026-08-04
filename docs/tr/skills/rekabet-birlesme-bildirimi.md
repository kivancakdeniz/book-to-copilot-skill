# Rekabet birleşme bildirimi

<span class="bts-skill-kicker">Birleşme ve devralmalar</span>

**M&A, Finans ve Rekabet Hukuku ekipleri** için. Ön hesaplama göstergelerini hukuki bildirim kararı ve kapanış kapısından ayırır.

<ul class="bts-metrics bts-metrics--compact">
  <li><b>40</b><span>LLM only</span></li>
  <li><b>100</b><span>LLM + skill</span></li>
  <li><b>7/7</b><span>kural atfı</span></li>
  <li><b>12</b><span>kilitli senaryo</span></li>
</ul>

## Skill ne ekledi

Kontrol yanıtı 0/7 kural kimliğine, skill yanıtı 7/7 kural kimliğine atıf yaptı. Skill'in değeri daha uzun metin üretmesi değil; şirket politikasını, kanıt boşluklarını ve insan yetki sınırını aynı karar kaydında görünür kılmasıdır.

Copilot onay veremez, yayımlayamaz veya operasyonel eylem uygulayamaz.

## Karar sözleşmesi

| Kilitli beklenti | Değer |
| --- | --- |
| Karar sınıfı | `legal-notification-review` |
| Seçenek | `hold-closing` |
| Zorunlu kural | 7 kimlik |
| İnsan rotası | Rekabet Hukuku Danışmanı · Finans · Sponsor |

Bu değerler modele gösterilmez; yalnız kilitli senaryo ve deterministik skorlayıcı tarafından kullanılır.

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

## Kullanım sınırı

Bu sentetik demo profesyonel görüş veya üretim kontrolü değildir. Sonuçları resmî kaynaktan ve yetkili insanla doğrulayın. [Güvenlik ve kaynak](../safety.md) sayfası veri, kaynak, lisans ve insan yetkisi sınırlarını açıklar.
