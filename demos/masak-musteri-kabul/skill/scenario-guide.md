# Senaryo rehberi

## Eksik ve çelişkili bilgi

- Sağlanan yüksek risk işareti varsa sınıf `enhanced-review`; eksik nihai faydalanıcı veya fon kanıtı varsa seçenek aynı anda `hold-onboarding` olur.
- Yüksek risk tetikleyicisi yokken zorunlu kanıt eksikse `hold-for-evidence` ve `hold-onboarding` kullan.
- Risk kaynakları çelişiyorsa birini seçme; `escalate-aml-officer` ile beklet.

## Yetki, ret ve bildirim

- Kanıt kapısı istisnasını AML Officer'a yönlendir; beceri istisna onaylamaz.
- `reject-onboarding` ve `decline-relationship` yalnız AML Officer ve Compliance'ın belgelenmiş insan ret kararı sağlandığında kullanılabilir.
- SİB/STR dosyala veya dosyalama sonucu verme. Yüksek risk olgusunu suç isnadına dönüştürme.

## Kapı ve periyodik inceleme

- Gelişmiş inceleme tamamlanmış olsa bile insan onayları ve AML-M01 planı tamamlanmadan `open-account` kullanma.
- Standart inceleme sınıfı, insan onayı beklenirken `hold-onboarding` seçeneğiyle birlikte kullanılabilir.
- What-if isteklerinde yalnız değiştirilen olguyu değiştir; diğer baseline olgularını koru.

Her durumda insanlar karar verir. Hesap açma, ilişkiyi reddetme, bildirim yapma veya sistemde değişiklik yapma.