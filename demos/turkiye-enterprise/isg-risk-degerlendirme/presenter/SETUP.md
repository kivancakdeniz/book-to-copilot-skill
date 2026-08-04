# Sunucu kurulumu

## Gereksinimler

- Temiz bir demo oturumu
- İncelenmiş `isg-risk-degerlendirme` skill paketi
- Sentetik `case-brief.md` eki
- Donmuş prompt
- İnsan sunucu ve İSG sınırlarını açıklayacak yetkili konu sahibi

Gerçek tesis, çalışan, olay, risk değerlendirmesi, fotoğraf veya gizli şirket
politikası kullanma. Demo hukuki, mühendislik veya tıbbi tavsiye ve mühendislik
sertifikasyonu değildir.

## Paket kontrolü

`book-to-copilot-skill` proje kökünden:

```bash
.venv/bin/python tools/package_cowork_skill.py \
  demos/turkiye-enterprise/isg-risk-degerlendirme/skill \
  dist/turkiye-enterprise/isg-risk-degerlendirme-cowork.skill
```

Arşiv kökünde `SKILL.md` ve `references/` altında tam beş dosya bulunmalıdır.
Sunumdan önce kilitli senaryo, rubrik, link ve hash kapılarını çalıştır.

## Oturum

1. Yeni bir konuşma aç ve yalnız sentetik vaka brifini ekle.
2. Skill'in oturumda görünür olduğunu doğrula.
3. Donmuş promptu değiştirmeden gönder.
4. İlk tam yanıtı koru; daha iyi cevap almak için yeniden çalıştırma.
5. Çıktının hiçbir saha eylemi yapmadığını ve insan yetkisini koruduğunu göster.

## Kapanış

Yüklenen sentetik dosyaları kaldır. Paylaşımı özel tut. Gerçek devreye alma,
değerlendirme kabulü ve çalışma durdurma kararlarının işveren ile
görevlendirilmiş İSG profesyonellerinde kaldığını yeniden belirt.
