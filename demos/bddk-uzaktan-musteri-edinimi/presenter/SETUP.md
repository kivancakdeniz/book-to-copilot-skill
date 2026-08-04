# Sunucu kurulumu

## Hazırlık

- Yalnız bu demo ağacındaki sentetik politika ve vaka dosyalarını kullanın.
- Resmî Gazete kaynağını manifest URL ve SHA-256 bilgisiyle doğrulayın; resmi
  metni demo paketine eklemeyin veya uzun alıntı olarak göstermeyin.
- `skill/` paketinde kök `SKILL.md` ve `references/` altında tam beş dosya
  bulunduğunu doğrulayın.
- Kontrol konuşmasına yalnız `sources/case-brief.md`, treatment konuşmasına aynı
  vaka ile portable skill'i verin.
- Her iki konuşmada `evaluation/frozen-prompt.md` metnini değiştirmeden kullanın.

Gerçek müşteri kaydı, kimlik belgesi, banka politikası, güvenlik bulgusu veya
hukuki görüş kullanmayın. Bu demo hukuki tavsiye ya da teknik sertifikasyon
değildir.

## Gösterim sırası

1. Temiz bir kontrol konuşması açın; skill yüklü olmasın.
2. Sentetik temel vakayı ve donmuş promptu verin; ilk tam yanıtı koruyun.
3. Ayrı temiz bir konuşma açın ve skill'in beş referansla görünür olduğunu
   doğrulayın.
4. Aynı vaka ve donmuş promptla ilk tam treatment yanıtını koruyun.
5. Yalnız davranış farklarını `evaluation/rubric.json` ile puanlayın; beğenilen
   yanıt çıkana kadar tekrar çalıştırmayın.

Asistanın sistemi değiştirdiğini, müşteri süreci başlattığını, canlıya geçişi
onayladığını, resmi uygunluk belirlediğini veya teknik sertifika verdiğini
söylemeyin. Karar ve eylemler Güvenlik, Uyum ve Hukuk insan yetkililerindedir.