---
hide:
  - toc
---

# 12 public examples

These examples show that the converter works with regulations and company
guidance as well as books. Every example includes a source manifest, synthetic
policy and case, generated skill, 12 locked scenarios, control answer, skill
answer, scorecard, and five Copilot packages.

Across the 12 examples, the mean trace score moved from **33/100**
without the skill to **95/100** with it. Results are limited to
one scenario and one host per condition.

## Examples

### [KVKK privacy notice review](kvkk-aydinlatma-kontrolu.md)

**Domain:** Data protection<br>
**Score:** LLM only **10/100** · LLM + skill **100/100**

Connects notice, consent, and transfer gaps to a human release gate.

### [Commercial message decision (ETK/IYS)](etk-iys-ileti-karari.md)

**Domain:** Commercial electronic messaging<br>
**Score:** LLM only **20/100** · LLM + skill **80/100**

Reviews a campaign audience against person-channel evidence and a suppression gate.

### [Discount price claim review](indirimli-fiyat-denetimi.md)

**Domain:** E-commerce and consumer law<br>
**Score:** LLM only **20/100** · LLM + skill **100/100**

Meets price history and campaign claims in a traceable release decision.

### [AML customer acceptance (MASAK)](masak-musteri-kabul.md)

**Domain:** Financial crime prevention<br>
**Score:** LLM only **20/100** · LLM + skill **100/100**

Routes identity, beneficial-owner, and source-of-funds gaps to human review.

### [Remote customer onboarding (BDDK)](bddk-uzaktan-musteri-edinimi.md)

**Domain:** Banking<br>
**Score:** LLM only **40/100** · LLM + skill **80/100**

Tests a remote onboarding flow against evidence, control, and go-live gates.

### [Merger notification review](rekabet-birlesme-bildirimi.md)

**Domain:** Mergers and acquisitions<br>
**Score:** LLM only **40/100** · LLM + skill **100/100**

Separates preliminary indicators from the legal notification and closing gate.

### [OHS risk assessment: from change to commissioning gate](isg-risk-degerlendirme.md)

**Domain:** Occupational health and safety<br>
**Score:** LLM only **40/100** · LLM + skill **100/100**

Makes change risk visible through participation, control, and commissioning evidence.

### [Pharmaceutical promotion review: audience and release gate](titck-ilac-tanitimi.md)

**Domain:** Pharmaceutical and health communication<br>
**Score:** LLM only **40/100** · LLM + skill **100/100**

Ties product status, audience, and channel reach to a human release review.

### [Crypto payment gateway review](kripto-odeme-kapisi.md)

**Domain:** Payment services and crypto assets<br>
**Score:** LLM only **40/100** · LLM + skill **100/100**

Reviews the role of crypto in a payment flow against product and launch gates.

### [Telecom communication data review](btk-haberlesme-verisi.md)

**Domain:** Telecom and privacy<br>
**Score:** LLM only **40/100** · LLM + skill **80/100**

Bounds location and traffic data use by purpose, consent, and retention gates.

### [Investment committee appraisal](investment-committee.md)

**Domain:** Capital allocation<br>
**Score:** LLM only **40/100** · LLM + skill **100/100**

Turns a capital brief into a gated, evidence-cited committee decision card.

### [Marketing claims review](marketing-claims-review.md)

**Domain:** Marketing and advertising compliance<br>
**Score:** LLM only **40/100** · LLM + skill **100/100**

Checks advertising claims against substantiation, disclosure, and release controls.


## What you can download

Each example page provides Cowork, GitHub Copilot for VS Code, Scout, and two
Copilot Studio formats. Every package is verified byte-identical after a clean
rebuild and recorded in `downloads/skills/SHA256SUMS`.

To run the same workflow on your material, [create a skill](../create-a-skill.md).
