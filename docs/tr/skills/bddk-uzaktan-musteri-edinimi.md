# BDDK uzaktan müşteri edinimi

[English](../../skills/bddk-uzaktan-musteri-edinimi.md)

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


Kurgusal bir dijital banka ekibi, yalnız e-posta ile kimlik taraması ve selfie
isteyen uzaktan müşteri edinimi akışını canlıya almak istiyor. Bu portable Türkçe
skill, talebi resmi karar vermeden; yöntem, kanıt, kontrol, insan yetkisi ve
canlıya geçiş kapılarıyla inceler.

## Bir bakışta iş etkisi

| Soru | Etki |
|---|---|
| Hangi karar gerekir? | Temel vakada `reject-flow`; güvenli seçenek `manual-onboarding-fallback` |
| Hangi risk görünür olur? | Canlı/görüntülü etkileşim, canlılık/bütünlük, kayıt ve izleme kanıtı boşlukları |
| Kim karar verir? | Güvenlik, Uyum ve Hukuk insan yetkilileri |
| Skill ne kazandırır? | Aynı beş sınıf, üç seçenek, kural izlenebilirliği ve 14 puanlık ölçülebilir çıktı |
| Skill ne yapmaz? | Hukuki tavsiye, resmi uygunluk, teknik sertifika, canlıya geçiş veya müşteri işlemi |

## Nasıl çalışır?

Skill, Resmî Gazete kaynağını metadata-only manifestle sınırlar; resmi metni
yeniden dağıtmaz veya kopyalamaz. Kısa kamu yöntemi sorularını sentetik UME-1.0
şirket politikasından ve sentetik UME-2408 vaka kanıtından ayırır. Sonuç, tam bir
karar sınıfı, tam bir seçenek, kanıt kapıları ve gerekli insan rotasıdır.

Temel akışta canlı veya görüntülü etkileşim, canlılık ve süreç bütünlüğü kanıtı,
kontrol günlükleri, izleme planı ve insan onayları yoktur. Bu nedenle doğrudan
canlıya geçiş önerilmez. Her eksik alan açık kalır; selfie'den teknik
sertifikasyon sonucu çıkarılmaz.

## İndirmeler

- [Cowork skill](../../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-cowork.skill)
- [GitHub Copilot for VS Code paketi](../../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-vscode.zip)
- [Scout paketi](../../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-scout.zip)
- [Copilot Studio GitHub harness paketi](../../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-github-harness.zip)
- [Copilot Studio Classic kurulum paketi](../../downloads/turkiye-enterprise/bddk-uzaktan-musteri-edinimi/bddk-uzaktan-musteri-edinimi-copilot-studio-classic-setup.zip)

Copilot Studio Classic paketi doğrudan içe aktarılan bir çözüm değildir. Classic
ortamında insan tarafından uygulanacak kurulum dosyaları ve eşleme rehberi
sağlar; kurulum sonrası yetki, bağlantı ve yayın ayarları ayrıca doğrulanır.

## Değerlendirme

Demo, cevap anahtarı istemden ayrı tam 12 kilitli senaryo ve her boyutu açık
ankrajlı 14 puanlık rubrik içerir. Puanlama doğru sınıf/seçenek kadar yöntem
envanterini, kanıt disiplinini, kaynak izlenebilirliğini, insan yetkisini ve
canlıya geçiş/izleme kapılarını da ölçer.

Bu içerik eğitim ve yönetişim tasarımı içindir. Nihai karar ve bütün uygulama
eylemleri yetkili insanlarda kalır.