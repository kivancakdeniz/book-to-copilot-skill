# Kendi kaynağınızdan Agent Skill oluşturun

Bir yapay zekâ aracısının içeriği çıkarmasını, analiz etmesini ve Agent Skill'i yazmasını
istiyorsanız deponun tamamını Agent Skill olarak kullanın. Yalnızca yerel metin
çıkarma aracına ihtiyacınız varsa bağımsız CLI'yi kullanın.

## Depoyu Agent Skill olarak kurun

Herkese açık bu türev depoyu desteklenen bir Agent Skill dizinine klonlayın.
GitHub Copilot CLI için:

```bash
git clone https://github.com/kivancakdeniz/book-to-copilot-skill.git \
  ~/.copilot/skills/book-to-skill
```

Diğer kullanıcı düzeyi konumlar arasında Copilot CLI veya Amp için
`~/.agents/skills/book-to-skill`, Claude Code için
`~/.claude/skills/book-to-skill` bulunur. Shell ve dosya erişimi vermeden önce
depoyu inceleyin.

## Bir kaynağı dönüştürün

Kurulu Agent Skill'i bir veya birden çok yol ve isteğe bağlı kısa bir çıktı
adıyla (slug) çağırın:

```text
/book-to-skill <yol-veya-dosya-kalıbı>... [skill-adı]
```

Örnekler:

```bash
# Tek PDF
/book-to-skill ~/kitaplar/operasyon-modeli.pdf operasyon-modeli

# Birden çok kaynağı tek Agent Skill içinde birleştir
/book-to-skill ~/politika/mevzuat.pdf ~/politika/kurum-politikasi.docx uyum-rehberi

# Klasördeki desteklenen bütün belgeler
/book-to-skill ~/workspace/runbooks/ operasyon-kilavuzu

# İlişkili araştırma dosyaları
/book-to-skill "~/makaleler/*.pdf" arastirma-yontemleri
```

Tam Agent Skill, içeriğin teknik mi yoksa metin ağırlıklı mı olduğunu sorar,
uygun metin çıkarma yöntemini seçer, yapıyı analiz eder ve üretilen Agent Skill'i
hedef ortamla uyumlu dizine yazar.

## Desteklenen girdiler

| Girdi | Metin çıkarma yöntemi |
| --- | --- |
| PDF, metin ağırlıklı | `pdftotext`, sonra `pypdf` veya `pdfminer.six` |
| PDF, teknik | Tablo ve kod blokları için Docling |
| EPUB | `ebooklib`, çalışmazsa standart kütüphane |
| DOCX | `python-docx`, çalışmazsa ZIP/XML yöntemi |
| HTML | Beautiful Soup, çalışmazsa standart kütüphane |
| RTF | `striprtf`, çalışmazsa düzenli ifade yöntemi |
| MOBI / AZW / AZW3 | Calibre `ebook-convert` |
| Markdown, TXT, reStructuredText, AsciiDoc | Dahili |

Klonlanan depoda bağımlılık denetimini çalıştırın:

```bash
python3 scripts/extract.py --check
```

## Ne üretilir

Tam kitap dönüşümü normalde şunu üretir:

```text
<skill-adı>/
├── SKILL.md
├── chapters/
├── glossary.md
├── patterns.md
└── cheatsheet.md
```

Kök `SKILL.md` zihinsel modelleri ve konu dizinini taşır. Destek dosyaları yalnız
istek gerektirdiğinde yüklenir. Bu depodaki düzenlemeye tabi karar örneklerinde
kullanılan altı dosyalı şablon ise herkese açık yöntemi, kurum politikasını,
kanıt haritasını, çıktı şemasını ve senaryo rehberini ayrı tutar.

## Sonucu doğrulayın

Üretilen Agent Skill'i kurmadan veya paylaşmadan önce hedef ortam uyumluluğu ve
istem enjeksiyonu denetimlerini çalıştırın:

```bash
python tools/validate_skill.py --lens copilot path/to/skill/SKILL.md
python tools/validate_skill.py --lens claude path/to/skill/SKILL.md
python tools/scan_generated_skill.py path/to/skill
```

Kaynağı güvenilmeyen girdi olarak değerlendirin. Agent Skill'i bir yapay zekâ aracısına
yüklemeden önce üretilen komutları, bağlantıları, YAML üstbilgisini (frontmatter) ve iddiaları
inceleyin.

## Fayda sağlayıp sağlamadığını test edin

Aynı vaka ve istemi iki kez kullanın:

1. Modeli üretilen Agent Skill olmadan çalıştırın.
2. Agent Skill'i kurup aynı isteği tekrarlayın.
3. İki yanıtı okumadan önce beklenen davranışı tanımlayın.
4. Doğruluk, kural kullanımı, kanıt, eksikler ve uygunsuz yetkiyi karşılaştırın.
5. Performans iddiası yapıyorsanız ham yanıtları ve puanlama yöntemini yayımlayın.

Bu depodaki 12 örnek, `demos/<slug>/evaluation/` altında yeniden kullanılabilir
test düzenekleri ve `demos/<slug>/evidence/` altında yeniden hesaplanabilir puan
kartları içerir.

## Cowork için paketleyin

`SKILL.md` içeren herhangi bir Agent Skill dizininden deterministik Microsoft
365 Copilot Cowork arşivi üretin:

```bash
python tools/package_cowork_skill.py path/to/skill dist/my-skill.skill
```

GitHub Copilot veya Scout için incelenmiş Agent Skill'i hedef ortamın beklediği
dizine yerleştirin. 12 örnek, Copilot Studio için GitHub bağlantı paketi ve klasik
kurulum biçimlerini de gösterir.

## Bağımsız metin çıkarma aracı

Agent destekli Agent Skill üretimi olmadan yalnızca metin çıkarma gerekiyorsa
klonladığınız depodan yerel CLI'yi kurun:

```bash
python3 -m venv .venv
.venv/bin/pip install -e '.[pdf,epub,docx,rtf]'
.venv/bin/book-to-skill ~/kitaplar/kaynak.pdf --mode text
```

CLI metni ve üstveriyi çıkarır. `/book-to-skill` Agent Skill'ini kaydetmez ve son
Agent Skill'i tek başına yazmaz.

## Sonraki adım

Kaynak bildirim dosyalarını, yalnızca LLM ile alınan yanıtları, Agent Skill destekli
yanıtları, puan kartlarını ve hazır Copilot paketlerini görmek için [herkese açık
örnekleri inceleyin](skills/index.md).
