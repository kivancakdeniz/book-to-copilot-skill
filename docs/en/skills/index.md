# Enterprise decision skill catalog

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

[SHA256SUMS](../../downloads/skills/SHA256SUMS) ·
[Third-party notices](../../downloads/skills/THIRD_PARTY_NOTICES.md)

## 12 skills

<div class="grid cards" markdown>

-   **[KVKK privacy notice review](kvkk-aydinlatma-kontrolu.md)**

    <span class="bts-skill-kicker">Data protection</span>

    Connects notice, consent, and transfer gaps to a human release gate.

    <span class="bts-score bts-score--control">LLM 10</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[Commercial message decision (ETK/IYS)](etk-iys-ileti-karari.md)**

    <span class="bts-skill-kicker">Commercial electronic messaging</span>

    Reviews a campaign audience against person-channel evidence and a suppression gate.

    <span class="bts-score bts-score--control">LLM 20</span> <span class="bts-score bts-score--skill">Skill 80</span>

-   **[Discount price claim review](indirimli-fiyat-denetimi.md)**

    <span class="bts-skill-kicker">E-commerce and consumer law</span>

    Meets price history and campaign claims in a traceable release decision.

    <span class="bts-score bts-score--control">LLM 20</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[AML customer acceptance (MASAK)](masak-musteri-kabul.md)**

    <span class="bts-skill-kicker">Financial crime prevention</span>

    Routes identity, beneficial-owner, and source-of-funds gaps to human review.

    <span class="bts-score bts-score--control">LLM 20</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[Remote customer onboarding (BDDK)](bddk-uzaktan-musteri-edinimi.md)**

    <span class="bts-skill-kicker">Banking</span>

    Tests a remote onboarding flow against evidence, control, and go-live gates.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 80</span>

-   **[Merger notification review](rekabet-birlesme-bildirimi.md)**

    <span class="bts-skill-kicker">Mergers and acquisitions</span>

    Separates preliminary indicators from the legal notification and closing gate.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[OHS risk assessment: from change to commissioning gate](isg-risk-degerlendirme.md)**

    <span class="bts-skill-kicker">Occupational health and safety</span>

    Makes change risk visible through participation, control, and commissioning evidence.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[Pharmaceutical promotion review: audience and release gate](titck-ilac-tanitimi.md)**

    <span class="bts-skill-kicker">Pharmaceutical and health communication</span>

    Ties product status, audience, and channel reach to a human release review.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[Crypto payment gateway review](kripto-odeme-kapisi.md)**

    <span class="bts-skill-kicker">Payment services and crypto assets</span>

    Reviews the role of crypto in a payment flow against product and launch gates.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[Telecom communication data review](btk-haberlesme-verisi.md)**

    <span class="bts-skill-kicker">Telecom and privacy</span>

    Bounds location and traffic data use by purpose, consent, and retention gates.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 80</span>

-   **[Investment committee appraisal](investment-committee.md)**

    <span class="bts-skill-kicker">Capital allocation</span>

    Turns a capital brief into a gated, evidence-cited committee decision card.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

-   **[Marketing claims review](marketing-claims-review.md)**

    <span class="bts-skill-kicker">Marketing and advertising compliance</span>

    Checks advertising claims against substantiation, disclosure, and release controls.

    <span class="bts-score bts-score--control">LLM 40</span> <span class="bts-score bts-score--skill">Skill 100</span>

</div>


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