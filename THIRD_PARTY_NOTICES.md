# Third-party notices

This document is a technical inventory of external sources, product names,
screenshots, model outputs, and site dependencies used or referenced by this
repository. It is not legal advice and does not determine whether a particular
reuse is permitted.

## Upstream software

This repository is a downstream of `virgiliojr94/book-to-skill`:

- Repository: https://github.com/virgiliojr94/book-to-skill
- License: MIT
- Preserved notice: Copyright (c) 2025 virgiliojr94

Downstream modifications and authored demo materials are identified in
[NOTICE.md](NOTICE.md) and licensed under [LICENSE.md](LICENSE.md) where stated.

## HM Treasury Green Book

The Investment Committee demo references *The Green Book: UK government
guidance on appraisal (2026)*, published by HM Treasury and the Government
Finance Function:

- Landing page: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government
- Source PDF: https://assets.publishing.service.gov.uk/media/698dbcd17da91680ad7f4308/The_Green_Book_2026.pdf
- Licence: Open Government Licence v3.0
- Licence URL: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

Required attribution:

> Contains public sector information licensed under the Open Government Licence v3.0.

The raw PDF is not bundled. OGL reuse does not cover third-party material that
the source identifies separately, and no endorsement by HM Treasury or the UK
Government is implied.

## U.S. Federal Trade Commission materials

The Marketing Claims Review demo references FTC publications and a date-pinned
eCFR source, including:

- *Advertising and Marketing on the Internet: Rules of the Road*:
  https://www.ftc.gov/system/files/ftc_gov/pdf/bus28-rulesroad-2023_508.pdf
- *.com Disclosures: How to Make Effective Disclosures in Digital Advertising*:
  https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf
- *Guides Concerning the Use of Endorsements and Testimonials in Advertising*,
  16 CFR Part 255, snapshot dated 2023-07-26:
  https://www.ecfr.gov/api/versioner/v1/full/2023-07-26/title-16.xml?part=255

Works of the U.S. federal government are generally not copyrightable in the
United States under 17 U.S.C. 105. That rule does not necessarily cover
third-party text, photographs, illustrations, logos, data, or other material
appearing in or linked from a federal publication, and treatment outside the
United States may differ. The raw FTC and eCFR snapshots are not bundled.

## Türkiye official legislation

The Türkiye enterprise demos link to legislation and other official sources.
Article 31 of Law No. 5846 on Intellectual and Artistic Works (FSEK) addresses
reuse of the limited categories it lists, such as officially published or
announced laws, regulations, notifications, circulars, and court decisions:

- FSEK: https://www.mevzuat.gov.tr/mevzuatmetin/1.3.5846.pdf

This inventory does not assume that Article 31 covers official guidance pages,
page design, databases, photographs, logos, attachments, or third-party
material. Article 30 contains a separate, purpose-limited rule concerning public
security and judicial reasons; it is not treated here as a general reuse
licence. Moral rights, database rights, trademark rights, contractual terms,
privacy rights, and other applicable rights may remain relevant.

Raw legislation snapshots are omitted. The package records official titles,
publishers, dates or versions where available, and source URLs so a qualified
human can verify the current official text.

## Official guidance pages

Guidance pages from Turkish authorities and other public bodies are handled as
metadata-only sources unless an explicit licence says otherwise. `Metadata-only`
means the raw official snapshot is omitted while its title, publisher, source
URL, date or version, and a short independently written method summary may be
included. The summary is not an official interpretation, does not replace the
live source, and does not imply endorsement.

## Product names and screenshots

Microsoft, Microsoft 365, Cowork, GitHub, GitHub Copilot, Copilot Studio,
Microsoft Scout, Anthropic, Claude, and related names, logos, trade dress, and UI
elements belong to their respective owners. Screenshots in the evidence folders
show compatibility and evaluation context only. Repository MIT terms apply to
authored annotations and metadata, not to third-party marks, UI, fonts, icons,
or other protected elements visible in a screenshot.

## AI model outputs

Some evidence records contain outputs produced by AI models. Model outputs can
be incomplete, incorrect, non-unique, or affected by provider terms and source
rights. They are evaluation evidence, not authoritative advice or approval, and
require human review before reuse or publication.

## Documentation site dependencies

The generated documentation site uses these build dependencies:

- MkDocs, BSD-2-Clause: https://github.com/mkdocs/mkdocs
- Material for MkDocs, MIT: https://github.com/squidfunk/mkdocs-material

Their own distributions and dependency trees carry their applicable licence and
notice files. Generated site assets may include third-party fonts, icons,
JavaScript, or styles governed by those notices. The public site ZIP must include
the repository root `LICENSE.md` and `THIRD_PARTY_NOTICES.md`; the release factory
task handles those files.