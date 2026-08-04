# MASAK müşteri kabul

[English](../../skills/masak-musteri-kabul.md)

## LLM only vs LLM + skill - beklenen fark

| Brief-only LLM | Derlenmiş skill |
|---|---|
| Serbest anlatım ve eksik kontrol listesi üretebilir | İzinli karar sınıfları, üç seçenek ve kural kimlikleriyle yapılandırır |
| Eksik kanıtı varsayım ile doldurma riski taşır | Eksik olguyu `bilinmiyor` tutar ve insan karar sahibine yönlendirir |
| Genel bir uyum veya operasyon önerisi verir | Yayın, canlıya geçiş, işlem veya kapanış kapısını açıkça uygular |

Bu tablo tasarım hipotezidir; bu 10 yeni skill için Cowork A/B henüz
çalıştırılmadı. Ölçülecek metrikler: exact karar/seçenek, gerekli kural geri
çağırma, desteksiz iddia sayısı, insan yetki sınırı ve yanıt uzunluğu. ROI veya
üretim performansı iddia edilmez.


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

- [Cowork skill](../../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-cowork.skill)
- [GitHub Copilot for VS Code ZIP](../../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-copilot-vscode.zip)
- [Scout ZIP](../../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-scout.zip)
- [Copilot Studio GitHub harness ZIP](../../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-github-harness.zip)
- [Copilot Studio classic setup ZIP](../../downloads/turkiye-enterprise/masak-musteri-kabul/masak-musteri-kabul-copilot-studio-classic-setup.zip)

Classic setup ZIP doğrudan içe aktarım paketi değildir; dosyalar Copilot Studio classic ortamında insan tarafından uygulanacak kurulum malzemeleridir.