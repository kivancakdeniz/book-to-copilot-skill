# Türkiye enterprise decision skill catalog

[Türkçe](../tr/skills/index.md)

This catalog lists source skills built by one release factory for 10 enterprise
decision scenarios in Türkiye. All 10 demos are **ready for source validation
and evaluation**. Each includes 12 locked scenarios, a 14-point rubric, synthetic
company policy, and official-source metadata. No Microsoft 365 Copilot Cowork
A/B has been run for these demos, so the catalog makes no claim about model
effect, production performance, or ROI.

The release contains 50 downloadable packages across five host formats. They
were generated deterministically and verified byte-identical after a clean
rebuild.

[SHA256SUMS](../downloads/turkiye-enterprise/SHA256SUMS) ·
[Third-party notices](../downloads/turkiye-enterprise/THIRD_PARTY_NOTICES.md)

## Catalog

| Skill | Domain | Target team | Value in one sentence | Status |
|---|---|---|---|---|
| [KVKK privacy notice review](kvkk-aydinlatma-kontrolu.md) | Data protection | Privacy, Compliance, Product | Connects notice, consent, and transfer gaps to a human release gate. | Release |
| [ETK/IYS message decision](etk-iys-ileti-karari.md) | Commercial electronic messaging | CRM, Compliance, Legal | Reviews campaign audiences through person-channel evidence and suppression gates. | Release |
| [Discount price review](indirimli-fiyat-denetimi.md) | E-commerce and consumer law | E-commerce, Pricing, Compliance | Joins price history and campaign claims in a traceable release decision. | Release |
| [MASAK customer acceptance](masak-musteri-kabul.md) | Financial crime prevention | AML, Compliance, Customer Acceptance | Routes identity, beneficial-owner, and source-of-funds gaps to human review. | Release |
| [BDDK remote customer onboarding](bddk-uzaktan-musteri-edinimi.md) | Banking | Digital Banking, Security, Compliance, Legal | Tests remote onboarding against evidence, control, and go-live gates. | Release |
| [Competition merger notification](rekabet-birlesme-bildirimi.md) | Mergers and acquisitions | M&A, Finance, Competition Law | Separates preliminary calculation signals from the legal filing decision and closing gate. | Release |
| [Occupational safety risk assessment](isg-risk-degerlendirme.md) | Occupational health and safety | OHS, Operations, Maintenance, Engineering | Makes change risks visible through participation, control, and commissioning evidence. | Release |
| [TİTCK medicine promotion](titck-ilac-tanitimi.md) | Pharmaceutical and health communication | Medical, Regulatory, Legal, Marketing | Connects product status, audience, and channel access to human release review. | Release |
| [Crypto payment gate](kripto-odeme-kapisi.md) | Payment services and crypto-assets | Payments, Compliance, Legal, Product | Reviews a crypto function's role in the payment flow through product-boundary and launch gates. | Release |
| [BTK communications data](btk-haberlesme-verisi.md) | Telecom and privacy | Telecom Compliance, Privacy, DPO, CRM | Constrains location and traffic-data use through purpose, consent, and retention gates. | Release |

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