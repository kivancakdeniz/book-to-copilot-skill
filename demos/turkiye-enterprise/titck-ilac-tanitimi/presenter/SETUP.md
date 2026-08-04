# Sunucu kurulumu

## Gereksinimler

- Temiz bir demo oturumu
- İncelenmiş `titck-ilac-tanitimi` skill paketi
- Sentetik `case-brief.md` eki
- Donmuş prompt
- Tıbbi, hukuki ve Regulatory sınırları açıklayacak insan sunucu

Gerçek ürün, hasta, sağlık meslek mensubu, kampanya, kreatif, ruhsat kaydı veya
gizli şirket politikası kullanma. Demo hukuki, mühendislik veya tıbbi tavsiye
değildir.

## Paket kontrolü

`book-to-copilot-skill` proje kökünden:

```bash
.venv/bin/python tools/package_cowork_skill.py \
  demos/turkiye-enterprise/titck-ilac-tanitimi/skill \
  dist/turkiye-enterprise/titck-ilac-tanitimi-cowork.skill
```

Arşiv kökünde `SKILL.md` ve `references/` altında tam beş dosya bulunmalıdır.
Sunumdan önce kilitli senaryo, rubrik, link ve hash kapılarını çalıştır.

## Oturum

1. Yeni bir konuşma aç ve yalnız sentetik vaka brifini ekle.
2. Skill'in oturumda görünür olduğunu doğrula.
3. Donmuş promptu değiştirmeden gönder.
4. İlk tam yanıtı koru; daha iyi cevap almak için yeniden çalıştırma.
5. Çıktının hiçbir yayın, hedefleme, kaldırma veya durdurma eylemi yapmadığını
   ve insan yetkisini koruduğunu göster.

## Kapanış

Yüklenen sentetik dosyaları kaldır. Paylaşımı özel tut. Ürün statüsü, tıbbi
kapsam, mevzuat yorumu ve yayın kararlarının Medical, Regulatory, Legal ve diğer
yetkili insanlarda kaldığını yeniden belirt.
