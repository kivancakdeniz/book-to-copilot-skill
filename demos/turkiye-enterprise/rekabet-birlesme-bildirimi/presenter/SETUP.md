# Sunucu kurulumu

## Hazırlık

- Yalnız bu demo ağacındaki sentetik politika ve vaka brifini kullanın.
- İki Rekabet Kurumu kaynağını manifest URL ve SHA-256 bilgileriyle doğrulayın;
  PDF'leri pakete eklemeyin veya resmi metinden uzun alıntı göstermeyin.
- `skill/` altında kök `SKILL.md` ve `references/` altında tam beş dosya
  bulunduğunu doğrulayın.
- Kontrol konuşmasına yalnız `sources/case-brief.md`, treatment konuşmasına aynı
  vaka ile portable skill'i verin.
- Her iki konuşmada `evaluation/frozen-prompt.md` metnini değiştirmeden kullanın.

Gerçek birleşme/devralma, taraf, ciro, teknoloji teşebbüsü değerlendirmesi,
hukuki görüş veya kapanış kaydı kullanmayın. Bu demo hukuki tavsiye değildir.

## Gösterim sırası

1. Skill bulunmayan temiz bir kontrol konuşması açın.
2. Sentetik vaka ve donmuş promptla ilk tam yanıtı koruyun.
3. Ayrı temiz konuşmada skill'in beş referansla görünür olduğunu doğrulayın.
4. Aynı vaka ve donmuş promptla ilk tam treatment yanıtını koruyun.
5. Yanıtları kilitli 14 puanlık rubrikle değerlendirin; tercih edilen cevap
   çıkana kadar yeniden çalıştırmayın.

Asistanın ciro hesapladığını, bildirim kararı verdiğini, dosya gönderdiğini,
işlemi yeniden yapılandırdığını, imza veya kapanış yaptığını söylemeyin. Rekabet
Hukuku Danışmanı hukuki inceleme ve kapanış yönlendirmesinin insan sahibidir.