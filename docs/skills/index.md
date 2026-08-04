# Enterprise decision skill catalog

[Türkçe](../tr/skills/index.md)

This catalog lists 12 enterprise decision skills built by one release
factory. Each skill ships 12 locked scenarios, a 14-point rubric, a synthetic
company policy, and official-source metadata.

For every skill the same case was answered twice: once without the skill and
once with it installed. The deterministic trace score averaged 33/100
for the model alone and 95/100 with the skill. Policy-rule citations
were zero in all 12 control runs. This is not a claim about production
performance, ROI, or regulatory compliance.

The release contains 60 downloadable packages across five host formats.
They are generated deterministically and verified byte-identical after a clean
rebuild.

[SHA256SUMS](../downloads/skills/SHA256SUMS) ·
[Third-party notices](../downloads/skills/THIRD_PARTY_NOTICES.md)

## Catalog

| Skill | Domain | Target team | Value in one sentence | LLM only | LLM + skill |
|---|---|---|---|---|---|
| [KVKK privacy notice review](kvkk-aydinlatma-kontrolu.md) | Data protection | Privacy, compliance, and product teams | Connects notice, consent, and transfer gaps to a human release gate. | 10/100 | 100/100 |
| [Commercial message decision (ETK/IYS)](etk-iys-ileti-karari.md) | Commercial electronic messaging | CRM, compliance, and legal teams | Reviews a campaign audience against person-channel evidence and a suppression gate. | 20/100 | 80/100 |
| [Discount price claim review](indirimli-fiyat-denetimi.md) | E-commerce and consumer law | E-commerce, pricing, and compliance teams | Meets price history and campaign claims in a traceable release decision. | 20/100 | 100/100 |
| [AML customer acceptance (MASAK)](masak-musteri-kabul.md) | Financial crime prevention | AML, compliance, and onboarding teams | Routes identity, beneficial-owner, and source-of-funds gaps to human review. | 20/100 | 100/100 |
| [Remote customer onboarding (BDDK)](bddk-uzaktan-musteri-edinimi.md) | Banking | Digital banking, security, compliance, and legal teams | Tests a remote onboarding flow against evidence, control, and go-live gates. | 40/100 | 80/100 |
| [Merger notification review](rekabet-birlesme-bildirimi.md) | Mergers and acquisitions | M&A, finance, and competition law teams | Separates preliminary indicators from the legal notification and closing gate. | 40/100 | 100/100 |
| [OHS risk assessment: from change to commissioning gate](isg-risk-degerlendirme.md) | Occupational health and safety | OHS, operations, maintenance, and engineering teams | Makes change risk visible through participation, control, and commissioning evidence. | 40/100 | 100/100 |
| [Pharmaceutical promotion review: audience and release gate](titck-ilac-tanitimi.md) | Pharmaceutical and health communication | Medical, regulatory, legal, and marketing teams | Ties product status, audience, and channel reach to a human release review. | 40/100 | 100/100 |
| [Crypto payment gateway review](kripto-odeme-kapisi.md) | Payment services and crypto assets | Payments, compliance, legal, and product teams | Reviews the role of crypto in a payment flow against product and launch gates. | 40/100 | 100/100 |
| [Telecom communication data review](btk-haberlesme-verisi.md) | Telecom and privacy | Telecom compliance, privacy, DPO, and CRM teams | Bounds location and traffic data use by purpose, consent, and retention gates. | 40/100 | 80/100 |
| [Investment committee appraisal](investment-committee.md) | Capital allocation | CFO, COO, CIO, and investment committee members | Turns a capital brief into a gated, evidence-cited committee decision card. | 40/100 | 100/100 |
| [Marketing claims review](marketing-claims-review.md) | Marketing and advertising compliance | Marketing, legal, and compliance teams | Checks advertising claims against substantiation, disclosure, and release controls. | 40/100 | 100/100 |

## Source and license boundary

Official legislation, guidance, and method sources are not copied in full into
the packages. The release carries only title, official URL, publisher, access
date, SHA-256, and reuse warnings as metadata. A human must verify currency,
scope, and reuse conditions at the official source. Company policies, cases, and
operational examples are synthetic and distributed within the MIT boundary
declared in each manifest. The skills do not provide legal, medical, or
engineering advice; authorized humans retain final decisions and all system
actions.

## Host packages

| Package | Root contract | Use |
|---|---|---|
| Cowork `.skill` | `SKILL.md` + five companion files | Microsoft 365 Copilot Cowork custom-skill upload |
| Copilot VS Code ZIP | `.github/skills/<slug>/` + `INSTALL.md` | Repository-level GitHub Copilot Agent Skill |
| Scout ZIP | `.copilot/skills/<slug>/` + `INSTALL.md` | Scout/Copilot skill-directory installation |
| Copilot Studio GitHub harness ZIP | Root `SKILL.md`, companion files, and `INSTALL.md` | Existing-skill ZIP upload in the GitHub Copilot harness preview |
| Copilot Studio classic setup ZIP | `README.md`, `instructions.md`, `knowledge/`, manifest | Guided manual setup in a classic environment |

The Copilot Studio GitHub harness package is directly uploadable under the
official existing-skill ZIP contract. The classic setup package is not a direct
agent or solution import: a human applies its instructions and knowledge files
to the target environment. In both cases, MCP servers, tools, connections,
identity, permissions, and publishing settings require separate configuration.