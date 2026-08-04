# Şirket politikası

Kanonik kaynak: `../../sources/company-policy.md`.

UME-1.0 sentetik bir Kurgusal Ufuk Bankası politikasıdır. Gerçek banka kuralı veya resmi
yorum değildir.

## Kural özeti

| Kimlik | Uygulama |
|---|---|
| `BDK-I01` | Yöntem, kanal, rol, doğrulama, istisna ve geri dönüş envanteri tamamlanır. |
| `BDK-V01` | Onaylı canlı/görüntülü etkileşim ile kimlik doğrulama kanıtı gerekir; e-posta taraması ve selfie tek başına geçmez. |
| `BDK-L01` | Canlılık, oturum bütünlüğü ve kontrol sonuçları somut kanıtla gösterilir. |
| `BDK-K01` | Olay, sürüm, karar, kanıt, istisna ve sonuç geri çağrılabilir kayda bağlanır. |
| `BDK-A01` | Güvenlik, Uyum ve Hukuk birlikte insan yetkisidir. |
| `BDK-R01` | Zorunlu kapılar ve insan onayları tamamlanmadan canlıya geçilmez. |
| `BDK-M01` | Dolandırıcılık/kontrol sahibi, sıklığı, eşiği ve geri dönüş tetikleri sürümlenir. |

## İzin verilen karar sınıfları

- `approve-pilot`
- `approve-with-controls`
- `hold-for-security-evidence`
- `escalate-bank-compliance`
- `reject-flow`

## İzin verilen seçenekler

- `current-remote-flow`
- `compliant-redesign`
- `manual-onboarding-fallback`

Eksik teknik kanıt hold, çözümlenmemiş hukuki yorum escalation, zorunlu kapıları
karşılamayan ve düzeltmesi kabul edilmeyen akış rejection yönündedir. Koşullu
sonuç canlıya geçiş izni değildir. Asistan hiçbir sınıfı insan kararı yerine
uygulamaz.