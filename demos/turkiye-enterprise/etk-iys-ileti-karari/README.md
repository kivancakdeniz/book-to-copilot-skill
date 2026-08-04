# ETK/IYS ileti kararı demosu

Bu kurumsal demo, CRM ekibinin 48.000 eski perakende müşterisine göndermek
istediği indirim SMS'inin mevcut kanıtlarla başlatılıp başlatılamayacağını inceler.

## Kilitli başlangıç

Beklenen karar `do-not-send`, seçenek `suppress-unverified-audience` olur. Mesaj
promosyon amaçlıdır, hizmet bildirimi değildir. Ret/çıkış ifadesi vardır; güncel
rıza/IYS durum anlık görüntüsü ve kişi-kanal kanıtı yoktur. Ret olanağı eksik ön
dayanağı gidermez.

İnsan rotası CRM Owner + Compliance + Legal'dır. İnsan Legal/Compliance nihai
kararın sahibidir. Skill hukuki görüş veya nihai hukuki sonuç üretmez; SMS
göndermez, IYS kaydı değiştirmez, kampanya başlatmaz veya başka bir otonom eylem
yapmaz.

## Kaynak modeli

6563 sayılı ETK ile Ticari İletişim Yönetmeliği kamuya açık resmî yöntemi sağlar.
Uzun resmî pasajlar kopyalanmaz. Sentetik şirket politikası yöntemi karar
sınıfları, kanıt kapıları ve yetki sınırlarıyla operasyonelleştirir; resmî
kaynağın yerine geçmez.

## Ağaç

```text
sources/       Kaynak manifesti, sentetik politika ve vaka
evaluation/    Kilitli istem, 12 senaryo ve 14 puanlık rubrik
skill/         SKILL.md ve tam beş taşınabilir referans
presenter/     Kurulum, konuşma akışı ve beklenen kontrol noktaları
```

Tüm adlar ve şirket olguları sentetiktir. Bu paket eğitim ve yönetişim demosudur;
hukuki tavsiye değildir.