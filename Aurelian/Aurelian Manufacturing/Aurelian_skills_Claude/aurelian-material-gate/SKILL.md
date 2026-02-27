---
name: aurelian-material-gate
description: Pre-production AI-powered incoming material review and release gate for Aurelian Manufacturing. Validates supplier material certificates against customer-specific requirements BEFORE material is released to the shop floor — preventing wasted machine time on non-conforming material. Manages customer material requirement profiles, EN 10204 certificate parsing, chemical and mechanical property limit checking, traceability verification, and supplier approval status. Use this skill when receiving material from suppliers, reviewing material certificates, checking if material meets customer specifications, building customer requirement profiles, setting up incoming inspection criteria, or any question about material release, goods receiving quality, incoming inspection, material quarantine, or pre-production material validation. Triggers on "material gate", "incoming material", "material release", "goods receiving", "incoming inspection", "material certificate review", "supplier cert", "material approved", "can we use this material", "material quarantine", "material hold", "customer material requirements", "material specification check", "chemical composition check", "mechanical properties check", "cert review", "material profile", "approved supplier", "material acceptance", "pre-production check", "release to production", or any request related to validating incoming raw materials before manufacturing begins.
---

# Aurelian Manufacturing — Material Gate Skill

Pre-production AI-powered incoming material review and release gate. Validates that every piece of raw material entering the production floor meets the specific customer's requirements — BEFORE a single chip is cut. This is Aurelian's first quality gate and the most cost-effective quality intervention in the entire manufacturing process.

**Source document:** AM-SDRL-2026-001 Rev 1.0 — Shipment Documentation Requirements (SDRL/MRB) located at `Quality System Input/Supplier Quality and Document requirements/Shipment_Documentation_Requirements_SDRL_MRB.pdf`

**Position in the MRB Builder pipeline:**

```
  ★ aurelian-material-gate  ← THIS SKILL (pre-production gate)
  │
  ↓ Material released to production
  │
  aurelian-sdrl-parser      → SDRL intake and requirement parsing
  aurelian-doc-validator    → Post-production document validation
  aurelian-coc-generator    → Certificate of Conformance generation
  aurelian-mrb-builder      → MRB assembly and orchestration
```

The Material Gate sits UPSTREAM of the existing 4-skill MRB pipeline. It is the gatekeeper that prevents non-conforming material from entering production.

---

## SECTION 1: WHY THIS GATE EXISTS

### 1.1 The Cost of Catching Material Problems Late

```
COST ESCALATION OF MATERIAL NON-CONFORMANCE:

  At goods receiving (Material Gate):
    Cost to reject:  ~0 NOK machine time
    Action:           Return to supplier, request replacement
    Impact:           Minor schedule delay (days)

  During manufacturing (discovered at in-process inspection):
    Cost to reject:  Machine time + tooling + operator time
    Action:           Scrap part, quarantine remaining material
    Impact:           Schedule delay + wasted capacity + NCR

  At final inspection (discovered in inspection room):
    Cost to reject:  Full manufacturing cost of all parts in batch
    Action:           Scrap entire batch, quarantine, restart
    Impact:           Major schedule delay + full cost write-off + NCR + customer notification

  After shipment (discovered by customer):
    Cost:             Full manufacturing + shipping + customer NCR + reputation damage
    Action:           Product recall, root cause investigation, corrective action
    Impact:           Potential suspension from Approved Supplier List
                      = CATASTROPHIC for a startup building its reputation

  CONCLUSION: Every 1 NOK spent at the Material Gate saves 100-1000 NOK downstream.
```

### 1.2 The Customer-Specific Problem

The same material grade can have **completely different acceptance criteria** depending on the customer and application:

| Parameter | ASTM A182 F316L (Standard) | Equinor (NORSOK MDS) | Defence (AMS 5648) |
|-----------|---------------------------|----------------------|-------------------|
| Carbon | max 0.030% | max 0.030% | max 0.030% |
| Sulphur | max 0.030% | **max 0.015%** | max 0.030% |
| Phosphorus | max 0.045% | **max 0.025%** | max 0.040% |
| Nickel | 10.0-14.0% | 10.5-13.5% | 10.0-14.0% |
| Tensile | min 485 MPa | min 485 MPa | **min 515 MPa** |
| Impact (Charpy) | not required | **min 45J at -46C** | per contract |
| Cert type | 3.1 acceptable | **3.2 required** | 3.1 minimum |
| PMI | not required | **mandatory** | per contract |
| Supplier | any | **approved list only** | per contract |

If Aurelian receives F316L material that passes standard ASTM limits but has 0.020% sulphur, it's fine for standard orders but **fails** for Equinor. Without a Material Gate, this material could enter production for an Equinor order and every part machined from it would need to be scrapped.

---

## SECTION 2: MATERIAL GATE ARCHITECTURE

### 2.1 Gate Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      MATERIAL GATE                               │
│              Pre-Production Release System                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INPUTS:                                                         │
│  ┌─────────────────┐  ┌──────────────────┐  ┌────────────────┐  │
│  │ Supplier         │  │ Customer Material│  │ Aurelian       │  │
│  │ Certificate      │  │ Requirement      │  │ Incoming       │  │
│  │ (EN 10204)       │  │ Profile          │  │ PMI Results    │  │
│  │                  │  │ (from PO/SDRL)   │  │ (if required)  │  │
│  └────────┬─────────┘  └────────┬─────────┘  └───────┬────────┘  │
│           │                      │                     │          │
│           ▼                      ▼                     ▼          │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              AI-POWERED REVIEW ENGINE                        │  │
│  │                                                              │  │
│  │  STEP 1: Certificate Parsing (OCR / structured data)        │  │
│  │     Extract: grade, heat number, chemical composition,       │  │
│  │     mechanical properties, heat treatment, cert type,        │  │
│  │     supplier, test methods, authorized signature              │  │
│  │                                                              │  │
│  │  STEP 2: Requirement Matching                                │  │
│  │     Load customer-specific requirement profile               │  │
│  │     Match each extracted value against customer limits        │  │
│  │                                                              │  │
│  │  STEP 3: Limit Checking                                     │  │
│  │     Chemical composition: each element within customer spec  │  │
│  │     Mechanical properties: each value within customer spec   │  │
│  │     Supplementary tests: present and passing (if required)   │  │
│  │                                                              │  │
│  │  STEP 4: Traceability Verification                          │  │
│  │     Heat number present and traceable                        │  │
│  │     Cert type matches requirement (3.1 vs 3.2)              │  │
│  │     Supplier on approved list (if required)                  │  │
│  │                                                              │  │
│  │  STEP 5: Integrity Check                                    │  │
│  │     Certificate completeness (no missing fields)             │  │
│  │     Authorized signature present                             │  │
│  │     Values internally consistent                             │  │
│  │     No red flags (unusual values, round numbers, etc.)       │  │
│  │                                                              │  │
│  └─────────────────────────────────────────────────────────────┘  │
│           │                                                      │
│           ▼                                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                    GATE DECISION                              │  │
│  │                                                              │  │
│  │  ✅ RELEASED    → Material approved for production           │  │
│  │                   Cert pre-staged for MRB Section 3          │  │
│  │                   ERP material status: RELEASED              │  │
│  │                                                              │  │
│  │  ❌ REJECTED    → Material quarantined                       │  │
│  │                   Supplier notified (replacement/credit)     │  │
│  │                   NCR generated automatically                │  │
│  │                   ERP material status: QUARANTINED           │  │
│  │                                                              │  │
│  │  ⚠️  REVIEW     → Needs human QA engineer decision          │  │
│  │                   Borderline values or ambiguous cert        │  │
│  │                   Customer contact may be required           │  │
│  │                   ERP material status: ON HOLD               │  │
│  │                                                              │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Gate Decision Logic

```
DECISION RULES:

  RELEASED (automatic — no human intervention needed):
    ALL of the following must be TRUE:
    - Certificate type matches or exceeds requirement (3.2 satisfies 3.1 requirement)
    - Material grade matches specification
    - ALL chemical composition values within customer limits
    - ALL mechanical property values within customer limits
    - ALL supplementary tests present and passing (if required)
    - Heat number present and traceable
    - Supplier on approved list (if approval required)
    - Certificate is complete (no missing mandatory fields)
    - Authorized signature present
    - No integrity red flags

  REJECTED (automatic — clear non-conformance):
    ANY of the following is TRUE:
    - Wrong material grade (cert says 304L, order requires 316L)
    - Certificate type insufficient (3.1 provided, 3.2 required)
    - Chemical composition element outside customer limits by > margin
    - Mechanical property below customer minimum by > margin
    - Required supplementary test missing entirely
    - Supplier NOT on approved list (when approval mandatory)
    - Certificate unsigned or clearly invalid
    - Heat number missing

  REVIEW (human decision needed — borderline or ambiguous):
    ANY of the following is TRUE:
    - Value within 5% of customer limit (borderline)
    - Supplementary test present but format/method non-standard
    - Supplier not on approved list but approval not explicitly mandatory
    - Certificate partially illegible
    - Unusual values that could indicate transcription error
    - Customer requirement ambiguous or could be interpreted multiple ways
    - Material grade acceptable as alternate but not exact match specified
```

---

## SECTION 3: CUSTOMER MATERIAL REQUIREMENT PROFILES

### 3.1 Profile Concept

Each customer + material specification + application combination gets a **Material Requirement Profile** — a structured data set that defines exactly what the Material Gate checks against.

```
PROFILE STRUCTURE:

  profile_id:           "PROF-EQN-F316L-NORSOK-001"
  customer:             "Equinor"
  material_spec:        "ASTM A182 F316L"
  application:          "Subsea valve body"
  industry:             "OIL_GAS"
  governing_standards:  ["NORSOK M-630", "NORSOK M-650", "ASTM A182"]
  cert_type_required:   "3.2"
  pmi_required:         true
  approved_suppliers:   ["Sandvik", "Outokumpu", "Tubacex"]

  chemical_limits:
    C:    { max: 0.030 }
    Mn:   { max: 2.00 }
    Si:   { max: 0.75 }
    P:    { max: 0.025 }          # tighter than ASTM (0.045)
    S:    { max: 0.015 }          # tighter than ASTM (0.030)
    Cr:   { min: 16.0, max: 18.0 }
    Ni:   { min: 10.5, max: 13.5 } # tighter than ASTM (10.0-14.0)
    Mo:   { min: 2.0, max: 3.0 }
    N:    { min: 0.04, max: 0.10 }  # NORSOK addition

  mechanical_limits:
    tensile:     { min: 485, unit: "MPa" }
    yield:       { min: 170, unit: "MPa" }
    elongation:  { min: 25, unit: "%" }
    hardness:    { max: 200, unit: "HB" }

  supplementary_tests:
    impact_test:
      required: true
      method: "ASTM A370 / ISO 148-1"
      temperature: -46    # Celsius
      min_value: 45       # Joules (average of 3)
      min_single: 35      # Joules (single minimum)
    intergranular_corrosion:
      required: true
      method: "ASTM A262 Practice E"
      acceptance: "No cracks at 15x magnification"
    ferrite_content:
      required: false     # not required for austenitic

  special_requirements:
    - "Solution annealed at minimum 1040C, water quenched"
    - "No welding repair permitted"
    - "NORSOK MDS to be submitted with cert"

  notes:
    - "Equinor typically audits new suppliers before approval"
    - "Sulphur and phosphorus limits are NORSOK-specific — tighter than standard ASTM"
```

### 3.2 Profile Library Architecture

```
PROFILE LIBRARY:

  LEVEL 1: Industry Base Profiles (built-in defaults)
    ├── DEF-BASE-ALU-7075     Defence baseline for 7075-T6 aluminium
    ├── DEF-BASE-SS-316       Defence baseline for 316/316L stainless
    ├── DEF-BASE-TI-6AL4V     Defence baseline for Ti-6Al-4V
    ├── DEF-BASE-STEEL-4340   Defence baseline for 4340 alloy steel
    ├── OG-BASE-SS-316L       Oil & Gas baseline for F316L (NORSOK)
    ├── OG-BASE-SS-DUPLEX     Oil & Gas baseline for duplex stainless
    ├── OG-BASE-INCONEL-625   Oil & Gas baseline for Inconel 625
    ├── OG-BASE-INCONEL-718   Oil & Gas baseline for Inconel 718
    └── GEN-BASE-CARBON       General engineering carbon steel

  LEVEL 2: Customer-Specific Profiles (built from actual POs)
    ├── PROF-KDA-7075-AMS4078       Kongsberg, 7075-T6, AMS 4078
    ├── PROF-KDA-316L-AMS5648       Kongsberg, 316L, AMS 5648
    ├── PROF-EQN-F316L-NORSOK       Equinor, F316L, NORSOK MDS
    ├── PROF-EQN-DUPLEX-NORSOK      Equinor, Duplex 2205, NORSOK MDS
    ├── PROF-NAMMO-4340-DEF         Nammo, 4340, defence spec
    ├── PROF-AKER-INCONEL625-OG     Aker Solutions, Inconel 625, O&G
    └── ...

  LEVEL 3: Order-Specific Overrides (when PO has unique requirements)
    ├── PO-2027-001-OVERRIDE        Extra impact test at -60C
    ├── PO-2027-015-OVERRIDE        Customer-approved alternate supplier
    └── ...

  RESOLUTION ORDER:
    Order-specific override (if exists)
      → Customer-specific profile (if exists)
        → Industry base profile (always exists as fallback)
```

### 3.3 Profile Creation Workflow

```
NEW CUSTOMER ORDER ARRIVES:

  CASE A: Existing profile matches
    → SDRL parser identifies material requirement
    → Material Gate loads matching customer profile
    → Ready to validate incoming material immediately

  CASE B: New customer or new material — no profile exists
    1. SDRL parser extracts material requirements from PO
    2. AI-assisted profile builder:
       a. Identifies base material specification (e.g., ASTM A182 F316L)
       b. Loads industry base profile as starting point
       c. Parses customer PO/SDRL for additional/tighter requirements
       d. Identifies NORSOK/AMS/MIL-STD overlays
       e. Generates DRAFT profile
    3. QA Engineer reviews and approves profile
    4. Profile saved to library for reuse on future orders
    5. Material Gate ready to validate

  CASE C: Repeat order, customer changed requirements
    → Flag profile difference
    → QA Engineer reviews changes
    → Profile updated or new version created
    → Change logged with effective date
```

---

## SECTION 4: CERTIFICATE PARSING ENGINE

### 4.1 What the AI Extracts from a Certificate

```
CERTIFICATE DATA EXTRACTION:

  HEADER INFORMATION:
    - Certificate type (2.1 / 2.2 / 3.1 / 3.2)
    - Certificate number
    - Issue date
    - Manufacturer / mill name
    - Manufacturer address
    - Reference standard (e.g., EN 10204:2004)

  MATERIAL IDENTIFICATION:
    - Material grade / designation (e.g., "316L", "F316L", "1.4404")
    - Material specification (e.g., "ASTM A182", "EN 10088-3")
    - Product form (bar, plate, forging, pipe)
    - Dimensions (diameter, thickness, length)
    - Heat number / lot number
    - Melt source / country of origin (if stated)

  CHEMICAL COMPOSITION (extract each element):
    - C, Si, Mn, P, S, Cr, Ni, Mo, N, Cu, Ti, Nb, V, W, Co, Al, B
    - Extract as numerical values with units (% or ppm)
    - Flag "< 0.005" type values (below detection limit)
    - Note which elements are reported vs. which are absent

  MECHANICAL PROPERTIES:
    - Tensile strength (MPa or ksi — normalize to MPa)
    - Yield strength / 0.2% proof stress (MPa)
    - Elongation (% — note gauge length: 4D, 5D, 50mm, 200mm)
    - Reduction of area (%)
    - Hardness (HB, HRC, HV — note scale)
    - Impact/Charpy values (J — note temperature and specimen size)

  HEAT TREATMENT:
    - Condition (solution annealed, quenched & tempered, normalized, etc.)
    - Temperature(s)
    - Holding time (if stated)
    - Cooling method (water quench, air cool, furnace cool)

  SUPPLEMENTARY TESTS (if present):
    - Intergranular corrosion test (method + result)
    - Ultrasonic test (method + result)
    - Grain size (ASTM number)
    - Ferrite content (%)
    - Flattening/bending test results
    - Macro/micro examination results

  AUTHORIZATION:
    - Authorized representative name
    - Signature (present / absent)
    - Stamp (if third-party for 3.2)
    - Third-party organization (for 3.2)

  METADATA:
    - Number of pages
    - Language(s)
    - Quality of scan (if scanned)
    - Confidence scores for extracted values (AI parsing)
```

### 4.2 Parsing Challenges and Solutions

```
COMMON PARSING CHALLENGES:

  CHALLENGE 1: Multiple formats and languages
    - Certificates come from global suppliers in various formats
    - Languages: English, German, Swedish, Italian, Japanese, Chinese
    SOLUTION: Multi-language OCR + AI model trained on certificate formats
    PHASE 1 FALLBACK: QA engineer manually enters key values into structured form

  CHALLENGE 2: Equivalent designations
    - Same material has different names in different standards:
      316L = 1.4404 = SUS316L = X2CrNiMo17-12-2 = S31603
    SOLUTION: Material equivalence table (see Section 4.3)

  CHALLENGE 3: Unit variations
    - Tensile in MPa vs ksi vs N/mm2
    - Elongation with different gauge lengths
    - Hardness in different scales (HB vs HRC vs HV)
    SOLUTION: Unit conversion library with standard factors

  CHALLENGE 4: Ambiguous or missing data
    - Element not reported (does it mean zero or not tested?)
    - "Typical" values instead of actual test results
    - Ranges instead of specific values
    SOLUTION: Flag as REVIEW — never assume missing data is compliant

  CHALLENGE 5: Fraudulent or suspect certificates
    - Known industry problem, especially with imported materials
    - Photocopied signatures, impossible values, round numbers
    SOLUTION: Integrity checks (Section 6) + PMI verification
```

### 4.3 Material Equivalence Table

```
COMMON MATERIAL EQUIVALENCES:

  AUSTENITIC STAINLESS:
  | ASTM/AISI | UNS    | EN/DIN    | W.Nr   | JIS      |
  |-----------|--------|-----------|--------|----------|
  | 304       | S30400 | X5CrNi18-10 | 1.4301 | SUS304  |
  | 304L      | S30403 | X2CrNi18-9  | 1.4307 | SUS304L |
  | 316       | S31600 | X5CrNiMo17-12-2 | 1.4401 | SUS316 |
  | 316L      | S31603 | X2CrNiMo17-12-2 | 1.4404 | SUS316L |

  DUPLEX STAINLESS:
  | Grade     | UNS    | EN           | W.Nr   |
  |-----------|--------|--------------|--------|
  | 2205      | S31803 | X2CrNiMoN22-5-3 | 1.4462 |
  | 2507      | S32750 | X2CrNiMoCuN25-6-3 | 1.4410 |

  NICKEL ALLOYS:
  | Common    | UNS    | EN            | W.Nr   |
  |-----------|--------|---------------|--------|
  | Inconel 625 | N06625 | NiCr22Mo9Nb | 2.4856 |
  | Inconel 718 | N07718 | NiCr19NbMo  | 2.4668 |

  ALUMINIUM (AEROSPACE):
  | Grade     | UNS    | AMS   | EN         |
  |-----------|--------|-------|------------|
  | 7075-T6   | A97075 | 4078  | EN AW-7075 |
  | 6061-T6   | A96061 | 4027  | EN AW-6061 |
  | 2024-T3   | A92024 | 4037  | EN AW-2024 |

  ALLOY STEEL:
  | Grade     | UNS    | AMS   | EN          |
  |-----------|--------|-------|-------------|
  | 4340      | G43400 | 6414  | 34CrNiMo6  |
  | 4130      | G41300 | 6370  | 25CrMo4    |

  TITANIUM:
  | Grade     | UNS    | AMS   |
  |-----------|--------|-------|
  | Ti-6Al-4V | R56400 | 4911  |
  | CP Grade 2| R50400 | 4902  |

  EQUIVALENCE RULE:
    When a cert uses a different designation than the PO:
    → Look up equivalence
    → IF equivalent: ACCEPT but LOG the designation mapping
    → IF not clearly equivalent: FLAG for REVIEW
    → NEVER assume equivalence without verification
```

---

## SECTION 5: LIMIT CHECKING ENGINE

### 5.1 Chemical Composition Limit Check

```
FOR EACH element in customer profile:

  EXTRACT actual value from certificate
  LOAD limit from customer requirement profile

  CHECK:
    IF limit has max only:
      actual <= max → PASS
      actual > max  → FAIL (over maximum)

    IF limit has min only:
      actual >= min → PASS
      actual < min  → FAIL (under minimum)

    IF limit has min AND max (range):
      min <= actual <= max → PASS
      actual < min → FAIL (under minimum)
      actual > max → FAIL (over maximum)

    IF element not reported on certificate:
      IF element is in customer profile → FAIL (missing data)
      IF element is NOT in customer profile → N/A

  BORDERLINE CHECK (generates REVIEW flag):
    IF actual is within 5% of any limit:
      → PASS but flag as "BORDERLINE — [element] at [X]% vs limit [Y]%"
      → QA engineer should review

  OUTPUT per element:
    { element: "S", actual: 0.012, limit_max: 0.015,
      result: "PASS", borderline: true, margin: "20% from limit" }
```

### 5.2 Mechanical Property Limit Check

```
FOR EACH mechanical property in customer profile:

  EXTRACT actual value from certificate
  NORMALIZE units (ksi → MPa, etc.)
  LOAD limit from customer requirement profile

  CHECK:
    tensile_strength:
      actual >= min → PASS
      actual < min  → FAIL

    yield_strength:
      actual >= min → PASS
      actual < min  → FAIL

    elongation:
      actual >= min → PASS
      actual < min  → FAIL
      NOTE: Check gauge length compatibility
            5D gauge: direct comparison if spec uses 5D
            4D gauge: apply conversion factor if spec uses 5D
            50mm gauge: apply conversion if spec uses proportional

    hardness:
      IF max specified: actual <= max → PASS
      IF range specified: min <= actual <= max → PASS
      NOTE: Convert between scales if needed (HRC ↔ HB ↔ HV)
            Use standard conversion tables (ASTM E140)

    impact_charpy:
      IF required:
        - Check test temperature matches requirement
        - Check specimen size (10x10, 7.5x10, 5x10 — apply correction factors for sub-size)
        - Average of 3 >= min_average → PASS (first check)
        - Each individual >= min_single → PASS (second check)
        - Both must pass

  UNIT CONVERSION TABLE:
    | From | To | Factor |
    |------|----|--------|
    | ksi  | MPa | x 6.895 |
    | MPa  | ksi | x 0.1450 |
    | HRC  | HB  | ASTM E140 table |
    | HV   | HB  | ASTM E140 table |
    | ft·lbf | J | x 1.356 |
```

### 5.3 Supplementary Test Check

```
FOR EACH supplementary test in customer profile:

  IF required == true:
    CHECK test report present on certificate:
      IF present:
        - Method matches requirement (or acceptable equivalent)
        - Result meets acceptance criteria
        - Test conditions match (temperature, duration, etc.)
        → PASS / FAIL
      IF absent:
        → FAIL (required test missing)

  COMMON SUPPLEMENTARY TESTS:

    Intergranular Corrosion (IGC):
      Methods: ASTM A262 Practice A/B/C/E/F, ASTM G28
      Acceptance: Typically "no cracks" or "acceptable microstructure"
      Common for: Austenitic stainless in corrosive service

    Ultrasonic Testing (UT):
      Standards: ASTM A388, EN 10228, ASME SA-388
      Acceptance: Per applicable standard (defect size limits)
      Common for: Forgings, thick sections

    Grain Size:
      Method: ASTM E112
      Acceptance: Typically ASTM No. 5 or finer
      Common for: Aerospace materials

    Ferrite Content:
      Method: ASTM E562, magnetic measurement (Feritscope)
      Acceptance: Varies (typically 30-70% for duplex)
      Common for: Duplex stainless steel

    Hydrogen Content:
      Method: Various (vacuum extraction, melt extraction)
      Acceptance: Typically max 2-4 ppm
      Common for: High-strength steel, titanium
```

---

## SECTION 6: INTEGRITY AND FRAUD DETECTION

### 6.1 Certificate Integrity Checks

```
RED FLAG INDICATORS (trigger REVIEW, not auto-reject):

  STATISTICAL FLAGS:
    - All mechanical values exactly at minimum specification values
      (real tests have natural variation — exact minimums are suspicious)
    - Chemical composition values all at round numbers
      (e.g., C: 0.020, Cr: 17.00, Ni: 12.00 — real analysis has more decimal variation)
    - Multiple heat numbers with identical test results
      (different heats should have different chemistry/properties)
    - Tensile and yield values identical between heats
      (statistically improbable for independent tests)

  DOCUMENT FLAGS:
    - Certificate appears to be a photocopy of a photocopy (degraded quality)
    - Signature appears identical across multiple certificates (rubber stamp)
    - Certificate format does not match known formats from that manufacturer
    - Date inconsistencies (cert date before melt date, etc.)
    - Corrections or alterations without proper annotation
    - Missing manufacturer letterhead or certificate number

  LOGICAL FLAGS:
    - Chemical composition doesn't balance (doesn't add up near 100%)
    - Mechanical properties inconsistent with chemistry
      (e.g., very high tensile for a low-alloy composition)
    - Heat treatment condition inconsistent with properties
      (e.g., "annealed" but hardness is very high)
    - Specimen orientation not stated for directional properties

  ACTION ON RED FLAGS:
    → Material placed ON HOLD (not rejected, not released)
    → QA Engineer reviews flagged items
    → Options:
       a. Contact supplier for clarification
       b. Perform incoming PMI to verify material identity
       c. Request replacement certificate from mill
       d. Accept with documented justification
       e. Reject and return material
```

### 6.2 PMI Cross-Verification

```
PMI AS SECOND LINE OF DEFENCE:

  WHEN PMI IS MANDATORY (per customer profile):
    → Perform PMI at goods receiving regardless of cert quality
    → PMI results must correlate with certificate values

  WHEN PMI IS TRIGGERED BY RED FLAGS:
    → Integrity checks flagged suspicious certificate
    → PMI performed to verify material identity
    → PMI results compared against cert values

  PMI CORRELATION CHECK:
    FOR EACH major element (Cr, Ni, Mo, Mn, Si):
      cert_value vs pmi_value
      IF difference > expected instrument variation (~0.5-1.0% for XRF):
        → FAIL — possible material mix-up or fraudulent cert
        → Quarantine material immediately
        → Escalate to QA Manager

  NOTE: XRF cannot detect carbon or nitrogen — use OES if these are critical.
```

---

## SECTION 7: GATE OUTPUT AND ERP INTEGRATION

### 7.1 Gate Decision Report

```
MATERIAL GATE REPORT
═══════════════════════════════════════════════
Gate Reference:   MG-2027-00042
Date:             15 August 2027
Reviewer:         AI Engine (v1.0) / [QA Engineer name if REVIEW]

MATERIAL:
  Supplier:       Sandvik Materials Technology
  Grade:          ASTM A182 F316L (W.Nr 1.4404)
  Form:           Round bar, dia. 150mm x 3000mm
  Heat Number:    H-42891
  Quantity:       12 bars (total 2,400 kg)
  Certificate:    EN 10204 Type 3.1, Cert No. SMT-2027-84521

TARGET ORDER(S):
  PO-2027-003 (Equinor, valve bodies) — 6 bars
  PO-2027-007 (TechnipFMC, pump housing) — 4 bars
  STOCK (unallocated) — 2 bars

REQUIREMENT PROFILE USED:
  PO-2027-003: PROF-EQN-F316L-NORSOK (Equinor NORSOK requirements)
  PO-2027-007: PROF-TFMC-F316L-STD (TechnipFMC standard requirements)

═══════════════════════════════════════════════
CHEMICAL COMPOSITION CHECK:
═══════════════════════════════════════════════

| Element | Cert Value | Equinor Limit | Status | TechnipFMC Limit | Status |
|---------|-----------|---------------|--------|------------------|--------|
| C       | 0.018%    | max 0.030     | ✅ PASS | max 0.030       | ✅ PASS |
| Si      | 0.42%     | max 0.75      | ✅ PASS | max 1.00        | ✅ PASS |
| Mn      | 1.55%     | max 2.00      | ✅ PASS | max 2.00        | ✅ PASS |
| P       | 0.023%    | max 0.025     | ⚠️ BORDER| max 0.045      | ✅ PASS |
| S       | 0.008%    | max 0.015     | ✅ PASS | max 0.030       | ✅ PASS |
| Cr      | 17.2%     | 16.0-18.0     | ✅ PASS | 16.0-18.0       | ✅ PASS |
| Ni      | 11.8%     | 10.5-13.5     | ✅ PASS | 10.0-14.0       | ✅ PASS |
| Mo      | 2.15%     | 2.0-3.0       | ✅ PASS | 2.0-3.0         | ✅ PASS |
| N       | 0.058%    | 0.04-0.10     | ✅ PASS | not specified    | N/A    |

═══════════════════════════════════════════════
MECHANICAL PROPERTY CHECK:
═══════════════════════════════════════════════

| Property    | Cert Value | Equinor Min | Status | TechnipFMC Min | Status |
|-------------|-----------|-------------|--------|----------------|--------|
| Tensile     | 572 MPa   | 485 MPa     | ✅ PASS | 485 MPa       | ✅ PASS |
| Yield 0.2%  | 285 MPa   | 170 MPa     | ✅ PASS | 170 MPa       | ✅ PASS |
| Elongation  | 52%       | 25%         | ✅ PASS | 25%            | ✅ PASS |
| Hardness    | 168 HB    | max 200 HB  | ✅ PASS | max 200 HB     | ✅ PASS |

═══════════════════════════════════════════════
SUPPLEMENTARY TEST CHECK:
═══════════════════════════════════════════════

| Test                  | Required (EQN) | Present | Result     | Status |
|-----------------------|----------------|---------|------------|--------|
| Impact -46C           | YES            | YES     | 185/192/178J| ✅ PASS|
| IGC (A262 Pr.E)       | YES            | YES     | Acceptable | ✅ PASS |
| Required (TFMC)       | Required       | Present | Result     | Status |
| Impact -46C           | NO             | YES     | —          | N/A    |
| IGC                   | NO             | YES     | —          | N/A    |

═══════════════════════════════════════════════
TRACEABILITY & COMPLIANCE CHECK:
═══════════════════════════════════════════════

| Check                          | Equinor  | TechnipFMC |
|--------------------------------|----------|------------|
| Cert type matches requirement  | 3.1 ≠ 3.2 ❌ | 3.1 = 3.1 ✅ |
| Heat number present            | ✅        | ✅          |
| Supplier on approved list      | ✅ Sandvik| N/A        |
| Heat treatment stated          | ✅ SA 1060C WQ | ✅      |
| Signature present              | ✅        | ✅          |
| Certificate complete           | ✅        | ✅          |

═══════════════════════════════════════════════
INTEGRITY CHECK:
═══════════════════════════════════════════════
  No red flags detected.

═══════════════════════════════════════════════
GATE DECISIONS:
═══════════════════════════════════════════════

  PO-2027-003 (Equinor):
    ❌ REJECTED — Certificate type 3.1 does not meet requirement for 3.2
    ⚠️ BORDERLINE — Phosphorus at 0.023% vs limit 0.025% (8% margin)
    ACTION: Request EN 10204 Type 3.2 certificate from Sandvik.
            Material QUARANTINED pending 3.2 cert.
            Note: All values including P are within limits — once 3.2
            cert is obtained, material can be released.

  PO-2027-007 (TechnipFMC):
    ✅ RELEASED — All checks passed.
    Material released for production on PO-2027-007.
    Certificate pre-staged for MRB Section 3.

  STOCK (unallocated):
    ✅ RELEASED TO STOCK — Meets base specification.
    Note: When allocated to a specific order, must re-validate
    against that order's customer profile.

═══════════════════════════════════════════════
```

### 7.2 ERP Integration Interface

```
ERP (EPICOR) INTEGRATION POINTS:

  INCOMING TRIGGER:
    Event: Purchase Order receipt completed in Epicor
    Data:  PO number, supplier, material grade, heat number, qty
    Action: Material Gate initiates review

  CERTIFICATE ATTACHMENT:
    Event: Supplier cert attached to PO receipt in DocStar
    Data:  Document ID, file, metadata
    Action: Material Gate begins parsing

  GATE DECISION OUTPUT → ERP:
    RELEASED:
      → Epicor material status = "QC APPROVED"
      → Inventory available for production allocation
      → Certificate linked to material lot in document management
      → MRB pre-staging: cert flagged for future MRB inclusion

    REJECTED:
      → Epicor material status = "QUARANTINED"
      → Inventory blocked from production allocation
      → Supplier non-conformance record created
      → Purchasing notified for replacement/credit action

    REVIEW:
      → Epicor material status = "QC HOLD"
      → Inventory blocked from production allocation
      → QA work queue item created
      → Notification to QA Engineer

  MULTI-ORDER ALLOCATION:
    When same material lot serves multiple orders:
    → Gate validates against EACH order's customer profile
    → Material can be RELEASED for one order and REJECTED for another
    → ERP tracks which orders are approved for which material lots
```

---

## SECTION 8: API INTERFACE FOR CUSTOMER REQUIREMENTS

### 8.1 Customer Requirements API Concept

For Tier 1 customers with digital procurement systems, an API interface allows requirements to flow in automatically:

```
API ENDPOINT CONCEPT:

  POST /api/v1/material-requirements

  PURPOSE: Customer pushes material requirements when issuing a PO

  REQUEST BODY:
  {
    "customer_id": "EQUINOR",
    "po_number": "EQN-PO-2027-0042",
    "line_items": [
      {
        "line": 1,
        "part_number": "VB-316L-150",
        "material_spec": "ASTM A182 F316L",
        "governing_standards": ["NORSOK M-630", "NORSOK M-650"],
        "cert_type": "3.2",
        "pmi_required": true,
        "chemical_limits": {
          "P": { "max": 0.025 },
          "S": { "max": 0.015 },
          "N": { "min": 0.04, "max": 0.10 }
        },
        "mechanical_limits": {
          "impact_test": {
            "temperature_c": -46,
            "min_average_j": 45,
            "min_single_j": 35
          }
        },
        "supplementary_tests": ["IGC_A262_E"],
        "approved_suppliers": ["Sandvik", "Outokumpu"],
        "special_requirements": [
          "Solution annealed min 1040C water quenched",
          "No welding repair"
        ]
      }
    ]
  }

  RESPONSE:
  {
    "status": "accepted",
    "profile_id": "PROF-EQN-F316L-NORSOK-001",
    "message": "Material requirement profile created/updated for PO EQN-PO-2027-0042"
  }
```

### 8.2 Requirement Input Methods (by customer tier)

```
TIERED INPUT METHODS:

  TIER 1 — API Integration (Kongsberg, Equinor, Aker):
    → Customer pushes requirements via API
    → Automatic profile creation/update
    → Real-time requirement changes during order lifecycle
    → Bi-directional: Aurelian can push gate decisions back
    → TARGET: Phase 3 (Q3 2028)

  TIER 2 — Structured Template (Nammo, Saab, BAE):
    → Customer fills in standardized Excel/web form
    → Parsed automatically into profile
    → Email notification for requirement changes
    → TARGET: Phase 2 (Q1 2028)

  TIER 3 — PO Parsing (smaller customers):
    → Requirements extracted from PO text/PDF by AI parser
    → QA Engineer reviews and approves extracted profile
    → Manual process supported by AI assistance
    → TARGET: Phase 1 (August 2027 — launch)

  FUTURE — Customer Portal (all tiers):
    → Web portal where customers can:
      - View their material requirement profiles
      - Modify requirements for upcoming orders
      - See gate decisions in real-time
      - Download validated certificates
    → TARGET: Phase 3-4 (2028-2029)
```

### 8.3 API Security and Access Control

```
API SECURITY:

  AUTHENTICATION:
    → API key per customer (Phase 2)
    → OAuth 2.0 with customer SSO (Phase 3)
    → Mutual TLS for defence customers (Phase 3)

  AUTHORIZATION:
    → Customer can only view/modify their own requirements
    → Customer cannot see other customers' profiles or orders
    → Read-only access to gate decisions for their orders
    → Write access limited to material requirements

  DATA PROTECTION:
    → All data encrypted in transit (TLS 1.3)
    → All data encrypted at rest
    → GDPR compliant (personal data minimal in this context)
    → Audit trail for all API calls
    → Rate limiting to prevent abuse

  DEFENCE CONSIDERATIONS:
    → Classified material specifications NOT transmitted via public API
    → Defence customers may require on-premise integration
    → ITAR/EAR controlled data handled per export regulations
    → Separate network segment for defence data (if required)
```

---

## SECTION 9: IMPLEMENTATION PHASES

### 9.1 Phase 1 — Manual Gate with AI Assistance (August 2027)

```
PHASE 1 CAPABILITY:

  ✅ Customer requirement profiles: Built manually by QA engineer
     (AI assists by extracting requirements from PO text)
  ✅ Certificate parsing: QA engineer enters key values into structured form
     (AI assists by suggesting values from OCR scan)
  ✅ Limit checking: Automated comparison of entered values vs profile
  ✅ Gate decision: System recommends RELEASE/REJECT/REVIEW
     QA engineer confirms decision
  ✅ Gate report: Automated report generation
  ✅ ERP update: Manual status update in Epicor

  TOOLS:
    → Structured Excel/web form for profile management
    → Structured Excel/web form for cert data entry
    → Automated limit checking formulas
    → Report template
    → Claude Code skill (this skill) for guidance

  EXPECTED: 5-15 material lots per month (5 CNC, initial orders)
  TIME PER LOT: ~30-60 minutes (with AI assistance)
```

### 9.2 Phase 2 — Semi-Automated Gate (Q1 2028)

```
PHASE 2 UPGRADES:

  ✅ Certificate parsing: OCR + AI extracts values automatically
     QA engineer reviews and confirms extracted values
  ✅ Profile library: Growing database of customer profiles
     New profiles built faster from existing templates
  ✅ ERP integration: Gate decisions write directly to Epicor
  ✅ Structured input: Customer Excel template for requirements
  ✅ PMI correlation: Automated comparison of PMI vs cert values

  EXPECTED: 15-30 material lots per month
  TIME PER LOT: ~10-20 minutes
```

### 9.3 Phase 3 — Intelligent Gate (Q3 2028)

```
PHASE 3 UPGRADES:

  ✅ Full AI parsing: Certificates processed without human data entry
  ✅ Customer API: Tier 1 customers push requirements automatically
  ✅ Fraud detection: Statistical analysis for suspicious certificates
  ✅ Automated gate: RELEASE decisions for clear-pass material
     without human confirmation (REJECT and REVIEW still need human)
  ✅ Historical learning: System learns supplier patterns
     and flags anomalies based on historical data
  ✅ Supplier scorecards: Track supplier cert quality over time

  EXPECTED: 30-60 material lots per month
  TIME PER LOT: ~2-5 minutes (human review only for exceptions)
```

### 9.4 Phase 4 — Autonomous Gate (2029+)

```
PHASE 4 VISION:

  ✅ Zero-touch for known supplier + known customer + repeat material
  ✅ Customer portal: Real-time gate status visibility
  ✅ Predictive: Pre-order material validation based on production schedule
  ✅ Blockchain/DLT: Certificate provenance tracking (if industry adopts)
  ✅ Multi-site: Centralized profile library across facilities
  ✅ Industry data sharing: Participate in material cert verification networks

  EXPECTED: 60-100+ material lots per month
  TIME PER LOT: ~0 minutes (autonomous) to ~5 minutes (exceptions)
```

---

## SECTION 10: RELATIONSHIP TO OTHER MRB SKILLS

### 10.1 Updated Pipeline

```
COMPLETE MRB BUILDER PIPELINE (6 skills):

  ★ aurelian-material-gate        PRE-PRODUCTION
  │   ↓ Material released
  │   ↓ Validated cert pre-staged for MRB
  │
  ① aurelian-sdrl-parser          ORDER SETUP
  │   ↓ Requirements parsed
  │   ↓ MRB structure initialized
  │
  ② [PRODUCTION HAPPENS]          MANUFACTURING
  │   ↓ Documents collected in real-time
  │   ↓ CNC/metrology/inspection data → direct to MRB
  │   ↓ Pre-staged supplier certs → linked to MRB sections
  │
  ③ aurelian-doc-validator         POST-PRODUCTION
  │   ↓ All documents validated
  │   ↓ Cross-references verified
  │
  ④ aurelian-coc-generator         COMPLIANCE
  │   ↓ CoC generated and signed
  │
  ⑤ aurelian-mrb-builder           ASSEMBLY & DELIVERY
      ↓ MRB compiled, released, shipped, archived
```

### 10.2 Data Flow Between Skills

```
aurelian-material-gate OUTPUTS:
  → TO aurelian-sdrl-parser:
      Gate decision per material lot
      Validated cert references
      Customer profile ID used

  → TO aurelian-doc-validator:
      Pre-validated material certificates (skip re-validation for certs already gate-approved)
      Gate report reference (proof of incoming inspection)

  → TO aurelian-mrb-builder:
      Material cert pre-staged for MRB Section 3
      Gate report available for MRB (incoming inspection evidence)
      Material traceability data (heat number → order linkage)
```

---

## SECTION 11: REFERENCE STANDARDS FOR MATERIAL ACCEPTANCE

| Standard | Title | Relevance |
|----------|-------|-----------|
| EN 10204:2004 | Metallic products — Types of inspection documents | Certificate types 2.1/2.2/3.1/3.2 |
| ASTM A182 | Forged or Rolled Alloy and Stainless Steel Pipe Flanges/Fittings | Common O&G material spec |
| ASTM A240 | Chromium and Chromium-Nickel Stainless Steel Plate/Sheet/Strip | Flat products |
| ASTM A276/A479 | Stainless Steel Bars and Shapes | Bar products |
| ASTM E8/E8M | Standard Test Methods for Tension Testing | Mechanical testing |
| ASTM E18 | Standard Test Methods for Rockwell Hardness | Hardness testing |
| ASTM E23 | Standard Test Methods for Notched Bar Impact Testing | Charpy impact |
| ASTM E112 | Standard Test Methods for Determining Average Grain Size | Grain size |
| ASTM E140 | Standard Hardness Conversion Tables | HRC/HB/HV conversion |
| ASTM A262 | Standard Practices for Detecting Susceptibility to IGC | Corrosion testing |
| ASTM E1019 | Standard Test Methods for Carbon/Sulphur/Nitrogen/Oxygen | Elemental analysis |
| AMS 4078 | Aluminium Alloy 7075 Bar, Rod, and Wire | Aerospace aluminium |
| AMS 5648 | Corrosion-Resistant Steel Bars (316L) | Aerospace stainless |
| NORSOK M-630 | Material Data Sheets for Piping | O&G material documentation |
| NORSOK M-650 | Qualification of Manufacturers | O&G supplier qualification |
| NORSOK M-CR-006 | Documentation Requirements | O&G documentation standards |
| API 6A | Wellhead and Christmas Tree Equipment | Valve material requirements |
| ASME SA-182 | ASME adoption of ASTM A182 | Pressure equipment |
| EN 10088-3 | Stainless Steel Technical Delivery Conditions for Bars/Rods | European stainless spec |
