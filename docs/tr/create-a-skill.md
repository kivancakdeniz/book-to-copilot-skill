# Kendi kaynağınızdan skill oluşturun

Bir agent'ın içeriği çıkarmasını, analiz etmesini ve skill'i yazmasını
istiyorsanız deponun tamamını Agent Skill olarak kullanın. Yalnız yerel metin
çıkarma motoruna ihtiyacınız varsa standalone CLI'yi kullanın.

## Agent Skill'i kurun

Bu public downstream'i desteklenen bir skill dizinine klonlayın. GitHub Copilot
CLI için:

```bash
git clone https://github.com/kivancakdeniz/book-to-copilot-skill.git \
  ~/.copilot/skills/book-to-skill
```

Diğer kullanıcı düzeyi konumlar arasında Copilot CLI veya Amp için
`~/.agents/skills/book-to-skill`, Claude Code için
`~/.claude/skills/book-to-skill` bulunur. Shell ve dosya erişimi vermeden önce
depoyu inceleyin.

## Bir kaynağı dönüştürün

Kurulu skill'i bir veya birden çok yol ve isteğe bağlı çıktı slug'ıyla çağırın:

```text
/book-to-skill <yol-veya-glob>... [skill-adı]
```

Örnekler:

```bash
# Tek PDF
/book-to-skill ~/kitaplar/operasyon-modeli.pdf operasyon-modeli

# Birden çok kaynağı tek skill'de birleştir
/book-to-skill ~/politika/mevzuat.pdf ~/politika/kurum-politikasi.docx uyum-rehberi

# Klasördeki desteklenen bütün belgeler
/book-to-skill ~/workspace/runbooks/ operasyon-runbook

# İlişkili araştırma dosyaları
/book-to-skill "~/makaleler/*.pdf" arastirma-yontemleri
```

Tam Agent Skill, içeriğin teknik mi metin ağırlıklı mı olduğunu sorar, uygun
çıkarıcıyı seçer, yapıyı analiz eder ve üretilen skill'i host ile uyumlu skill
dizinine yazar.

## Desteklenen girdiler

| Girdi | Çıkarım yolu |
| --- | --- |
| PDF, metin ağırlıklı | `pdftotext`, sonra `pypdf` veya `pdfminer.six` |
| PDF, teknik | Tablo ve kod blokları için Docling |
| EPUB | `ebooklib`, standart kütüphane fallback'i ile |
| DOCX | `python-docx`, ZIP/XML fallback'i ile |
| HTML | Beautiful Soup, standart kütüphane fallback'i ile |
| RTF | `striprtf`, regex fallback'i ile |
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

Kök `SKILL.md` mental modelleri ve konu indeksini taşır. Destek dosyaları yalnız
istek gerektirdiğinde yüklenir. Bu depodaki regüle karar örneklerinde kullanılan
altı dosyalı şablon ise kamu yöntemini, şirket politikasını, kanıt haritasını,
çıktı şemasını ve senaryo rehberini ayrı tutar.

## Sonucu doğrulayın

Üretilen skill'i kurmadan veya paylaşmadan önce host uyumluluğu ve prompt
injection denetimlerini çalıştırın:

```bash
python tools/validate_skill.py --lens copilot path/to/skill/SKILL.md
python tools/validate_skill.py --lens claude path/to/skill/SKILL.md
python tools/scan_generated_skill.py path/to/skill
```

Kaynağı güvenilmeyen girdi olarak değerlendirin. Skill'i bir agent'a yüklemeden
önce üretilen komutları, bağlantıları, frontmatter'ı ve iddiaları inceleyin.

## Fayda sağlayıp sağlamadığını test edin

Aynı vaka ve istemi iki kez kullanın:

1. Modeli üretilen skill olmadan çalıştırın.
2. Skill'i kurup aynı isteği tekrarlayın.
3. İki yanıtı okumadan önce beklenen davranışı tanımlayın.
4. Doğruluk, kural kullanımı, kanıt, eksikler ve uygunsuz yetkiyi karşılaştırın.
5. Performans iddiası yapıyorsanız ham yanıtları ve puanlama yöntemini yayımlayın.

Bu depodaki 12 örnek, `demos/<slug>/evaluation/` altında yeniden kullanılabilir
fixture'lar ve `demos/<slug>/evidence/` altında yeniden hesaplanabilir skor
kartları içerir.

## Cowork için paketleyin

`SKILL.md` içeren herhangi bir skill dizininden deterministik Microsoft 365
Copilot Cowork arşivi üretin:

```bash
python tools/package_cowork_skill.py path/to/skill dist/my-skill.skill
```

GitHub Copilot veya Scout için incelenmiş skill'i host'un beklediği skill dizinine
yerleştirin. 12 örnek, Copilot Studio için GitHub harness ve classic kurulum
biçimlerini de gösterir.

## Standalone çıkarıcı

Agent destekli skill üretimi olmadan yalnız çıkarım gerekiyorsa klondan yerel
CLI'yi kurun:

```bash
python3 -m venv .venv
.venv/bin/pip install -e '.[pdf,epub,docx,rtf]'
.venv/bin/book-to-skill ~/kitaplar/kaynak.pdf --mode text
```

CLI metin ve metadata çıkarır. `/book-to-skill` Agent Skill'ini kaydetmez ve son
skill'i tek başına yazmaz.

## Sonraki adım

Kaynak manifestlerini, kontrol ve skill yanıtlarını, skor kartlarını ve hazır
Copilot paketlerini görmek için [public örnekleri inceleyin](skills/index.md).
