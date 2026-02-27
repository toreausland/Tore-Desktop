---
name: aurelian-doc-validator
description: Document validation engine for Aurelian Manufacturing's Digital MRB Builder system. Validates collected documents against SDRL requirements for Defence (AS9100/AQAP) and Oil & Gas (NORSOK/API) contracts. Checks completeness, standard compliance, traceability, signatures, format requirements, and cross-references between documents. Use this skill when validating incoming documents, checking MRB completeness, verifying material certificates, reviewing inspection reports, auditing document packages before shipment, or any question about document quality and compliance. Triggers on "validate document", "check certificate", "verify material cert", "document complete", "MRB ready", "shipment documentation check", "audit documents", "review inspection report", "FAIR validation", "ITP compliance", "EN 10204 check", "traceability verification", "NCR review", "document quality", "pre-shipment review", or any request to verify that collected documentation meets contractual and regulatory requirements.
---

# Aurelian Manufacturing — Document Validator Skill

Validation engine that verifies every collected document meets its SDRL-specified requirements before inclusion in the Manufacturing Record Book. Acts as the quality gate between document collection and MRB assembly.

**Source document:** AM-SDRL-2026-001 Rev 1.0 — Shipment Documentation Requirements (SDRL/MRB) located at `Quality System Input/Supplier Quality and Document requirements/Shipment_Documentation_Requirements_SDRL_MRB.pdf`

**Related MRB Builder skills:**
- `aurelian-sdrl-parser` — Provides the parsed requirement set that this validator checks against
- `aurelian-coc-generator` — Generates CoCs after validation confirms all prerequisites met
- `aurelian-mrb-builder` — Receives validated documents for final MRB assembly

---

## SECTION 1: VALIDATION PHILOSOPHY

### 1.1 Zero-Defect Document Delivery

Every document in an MRB will be scrutinized by the customer's quality engineers. A single missing signature, wrong material certificate type, or incomplete traceability chain can result in:

- **Shipment rejection** (immediate revenue impact)
- **Non-Conformance Report** against Aurelian (reputational damage)
- **Suspension from Approved Supplier List** (catastrophic for defence work)
- **Delayed payment** (cash flow impact)

The validator catches these issues BEFORE the MRB leaves Aurelian.

### 1.2 Validation Principle

```
RULE: Every document must be validated BEFORE it enters the MRB.
      No document enters the MRB without passing validation.
      Validation failures generate actionable correction requests.
      The validator does NOT modify documents — it only accepts or rejects.
```

---

## SECTION 2: VALIDATION FRAMEWORK

### 2.1 Five-Layer Validation

Each document passes through 5 validation layers:

| Layer | Check | Description | Failure Action |
|-------|-------|-------------|----------------|
| **L1: Existence** | Document received? | Has the document been collected from its source? | Flag as MISSING, notify responsible party |
| **L2: Format** | Correct format? | PDF/A, signed, correct template, legible | Flag as FORMAT_ERROR, request re-submission |
| **L3: Completeness** | All fields populated? | No blank mandatory fields, all pages present | Flag as INCOMPLETE, identify missing fields |
| **L4: Compliance** | Meets standard? | Content complies with referenced standard (EN 10204, AS9102, etc.) | Flag as NON_COMPLIANT, specify which requirement fails |
| **L5: Traceability** | Links verified? | Cross-references match (heat numbers, PO numbers, part numbers, dates) | Flag as TRACEABILITY_BREAK, identify broken link |

### 2.2 Validation Status Model

```
Document validation states:

  PENDING         → Document not yet received
  RECEIVED        → Document received, not yet validated
  VALIDATING      → Validation in progress
  VALIDATED       → Passed all 5 layers
  REJECTED        → Failed one or more layers (with specific failure codes)
  CORRECTED       → Previously rejected, re-submitted
  WAIVED          → Customer approved deviation/waiver
  NOT_APPLICABLE  → Requirement waived or not relevant for this order
```

---

## SECTION 3: MATERIAL CERTIFICATE VALIDATION (EN 10204)

### 3.1 Type 3.1 Certificate Validation Checklist

For EN 10204 Type 3.1 (minimum for defence, standard for oil & gas):

```
VALIDATE EN 10204 TYPE 3.1:

  L1 EXISTENCE:
    [ ] Certificate document exists for material lot/heat

  L2 FORMAT:
    [ ] PDF or original scan (legible)
    [ ] Manufacturer's letterhead or official format
    [ ] Date of issue present

  L3 COMPLETENESS — ALL of the following must be present:
    [ ] Material specification (e.g., ASTM A182 F316L, AMS 4078)
    [ ] Heat number / lot number
    [ ] Chemical composition (ACTUAL values, not just "conforms")
    [ ] Mechanical properties:
        [ ] Tensile strength (actual value + unit)
        [ ] Yield strength (actual value + unit)
        [ ] Elongation (actual value + %)
        [ ] Reduction of area (if applicable)
    [ ] Heat treatment condition (e.g., "Solution Annealed at 1040C, Water Quenched")
    [ ] Product form and dimensions
    [ ] Quantity / weight
    [ ] Manufacturer name and address

  L4 COMPLIANCE:
    [ ] Chemical composition within specification limits
    [ ] Mechanical properties within specification limits
    [ ] Heat treatment per specification requirements
    [ ] Test methods referenced (e.g., ASTM E8 for tensile, ASTM E18 for hardness)
    [ ] Standard edition/year referenced is current or customer-approved

  L5 TRACEABILITY:
    [ ] Heat number matches goods receiving record
    [ ] Heat number matches material traceability matrix
    [ ] Material specification matches PO/drawing requirement
    [ ] If material serves multiple orders: ERP linkage verified for each order

  AUTHORIZED REPRESENTATIVE:
    [ ] Name of authorized inspection representative
    [ ] Signature or electronic validation mark
    [ ] "This certificate is issued in accordance with EN 10204:2004, Type 3.1"
```

### 3.2 Type 3.2 Additional Checks

For EN 10204 Type 3.2 (third-party verified — required for safety-critical items):

```
ADDITIONAL CHECKS FOR TYPE 3.2 (on top of all 3.1 checks):

  [ ] Third-party inspector organization identified
  [ ] Third-party inspector name and credentials
  [ ] Third-party signature/stamp present
  [ ] Third-party accreditation reference (if applicable)
  [ ] Statement confirming independent verification of test results
  [ ] Third-party organization is independent of manufacturer
```

### 3.3 Common Material Certificate Failures

| Failure | Description | Severity | Resolution |
|---------|-------------|----------|------------|
| Missing heat number | No traceability possible | CRITICAL | Reject, request new cert |
| Typical vs actual values | "Typical" composition not acceptable | CRITICAL | Reject, require actual test results |
| Expired standard edition | References obsolete standard version | MAJOR | Verify with customer if acceptable |
| Missing mechanical tests | Only chemical composition shown | CRITICAL | Reject, require full cert |
| Unsigned | No authorized representative | CRITICAL | Reject, request signed copy |
| Wrong material grade | Cert shows different grade than specified | CRITICAL | Reject, investigate material mix-up |
| Illegible scan | Cannot read values | MAJOR | Request higher quality scan |

---

## SECTION 4: AS9102 FAIR VALIDATION (DEFENCE)

### 4.1 Form 1 — Part Number Accountability

```
VALIDATE FAIR FORM 1:

  [ ] Part number matches PO / drawing
  [ ] Part name / description correct
  [ ] Drawing number and revision correct
  [ ] Organization name (Aurelian Manufacturing AS)
  [ ] Part serial number(s) for inspected article(s)
  [ ] FAIR reason code:
      - First production
      - Design change
      - Process change
      - Tooling change
      - Production gap
      - Other (specify)
  [ ] Signature and date of preparer
  [ ] Signature and date of approver
```

### 4.2 Form 2 — Product Accountability

```
VALIDATE FAIR FORM 2:

  [ ] All raw materials listed with:
      [ ] Material specification (e.g., AMS 4078)
      [ ] Supplier name
      [ ] Certificate type (EN 10204 type)
      [ ] Heat/lot number
      [ ] Certificate reference (links to actual cert in MRB Section 3)
  [ ] All special processes listed with:
      [ ] Process type (anodize, heat treat, NDT, etc.)
      [ ] Specification reference
      [ ] Processor name
      [ ] Certificate/report reference
  [ ] All purchased components listed (if applicable)
  [ ] Traceability chain complete: raw material → finished part
```

### 4.3 Form 3 — Characteristic Accountability

```
VALIDATE FAIR FORM 3:

  [ ] Every characteristic from drawing identified:
      [ ] Characteristic number (sequential)
      [ ] Drawing requirement (nominal + tolerance)
      [ ] Measurement result (ACTUAL value)
      [ ] Upper/lower specification limits
      [ ] PASS/FAIL determination correct
  [ ] All critical dimensions marked as "Key Characteristic" if flagged on drawing
  [ ] GD&T callouts properly interpreted and measured
  [ ] Measurement method identified (CMM, micrometer, gauge, etc.)
  [ ] No FAIL results without accompanying NCR or deviation approval
  [ ] Statistical data (Cp, Cpk) if required by customer

  DATA SOURCE VERIFICATION:
    [ ] Characteristic data matches CMM/inspection report data
    [ ] CNC in-machine measurement data cross-referenced where applicable
    [ ] All measurement instruments calibrated (calibration cert reference)
```

---

## SECTION 5: INSPECTION REPORT VALIDATION

### 5.1 Dimensional Inspection Reports

```
VALIDATE DIMENSIONAL INSPECTION:

  L3 COMPLETENESS:
    [ ] Part number and serial number
    [ ] Drawing number and revision
    [ ] Inspection date
    [ ] Inspector name/ID
    [ ] All drawing dimensions measured
    [ ] Actual values recorded (not just PASS/FAIL)
    [ ] Measurement uncertainty stated (if required by customer)
    [ ] Equipment identification (CMM serial number, instrument IDs)

  L4 COMPLIANCE:
    [ ] All dimensions within tolerance
    [ ] IF any out-of-tolerance:
        [ ] NCR raised
        [ ] Disposition recorded (use-as-is, rework, scrap, return to vendor)
        [ ] Customer approval obtained (if use-as-is or repair)
    [ ] Surface finish measurements included (Ra, Rz) where specified
    [ ] Thread gauge results (GO/NO-GO) where applicable

  L5 TRACEABILITY:
    [ ] Inspection report linked to correct order/serial number
    [ ] Instruments have valid calibration (date within calibration interval)
    [ ] Inspector qualified for this inspection type
```

### 5.2 NDT Report Validation

```
VALIDATE NDT REPORT:

  [ ] NDT method identified (RT, UT, MT, PT, ET, VT)
  [ ] Applicable standard referenced (e.g., ASME V, EN ISO 17640)
  [ ] NDT procedure reference number
  [ ] Acceptance criteria specified and referenced
  [ ] Technician qualification:
      [ ] Name and certification level (e.g., ASNT Level II, PCN Level 2)
      [ ] Certification number and expiry date
  [ ] Equipment:
      [ ] Equipment identification
      [ ] Calibration status current
  [ ] Results:
      [ ] Area/volume inspected clearly defined
      [ ] All indications recorded with location and size
      [ ] Accept/reject determination for each indication
      [ ] Overall PASS/FAIL
  [ ] Signed by qualified technician AND reviewed by Level III (if required)
```

---

## SECTION 6: ITP VALIDATION (OIL & GAS)

### 6.1 ITP Compliance Check

```
VALIDATE ITP COMPLIANCE:

  FOR EACH Hold Point (H):
    [ ] Customer/third-party inspector was present
    [ ] Sign-off obtained BEFORE production continued
    [ ] Date and time of inspection recorded
    [ ] Inspector name and organization recorded
    [ ] Results/findings documented
    [ ] IF failed: NCR raised, corrective action before proceeding

  FOR EACH Witness Point (W):
    [ ] Customer notified minimum 48-72h in advance
    [ ] IF customer attended: sign-off obtained
    [ ] IF customer waived attendance: waiver documented (email/letter)
    [ ] Activity proceeded with or without customer presence
    [ ] Results documented regardless of attendance

  FOR EACH Review Point (R):
    [ ] Documentation submitted to customer
    [ ] Submission date and method recorded
    [ ] Customer acknowledgement received (or timeout per contract)
    [ ] Comments addressed if any

  OVERALL ITP:
    [ ] All H/W/R points have been addressed
    [ ] No open Hold Points
    [ ] ITP summary sheet signed off by Aurelian QA
    [ ] Customer final ITP acceptance (if required)
```

---

## SECTION 7: PMI VALIDATION

```
VALIDATE PMI REPORT:

  [ ] PMI method identified (XRF, OES, Laboratory)
  [ ] Equipment identification and calibration status
  [ ] Operator qualification
  [ ] Material/component tested:
      [ ] Part identification (serial/lot)
      [ ] Test location on component
  [ ] Results:
      [ ] Elemental analysis results
      [ ] Material grade identification confirmed
      [ ] Statement: "Material composition consistent with [specification]"
  [ ] Cross-reference:
      [ ] Heat number matches material certificate
      [ ] Grade matches PO/drawing specification
      [ ] Results consistent with EN 10204 cert values (within instrument accuracy)

  COMMON PMI FAILURES:
    - Material swap (wrong grade identified) → CRITICAL, quarantine part
    - Missing elements in analysis (carbon not detectable by XRF) → Use OES
    - Calibration expired → Reject report, re-test with calibrated instrument
```

---

## SECTION 8: CERTIFICATE OF CONFORMANCE VALIDATION

### 8.1 CoC Pre-Generation Check

Before `aurelian-coc-generator` can produce a CoC, the validator must confirm:

```
COC READINESS CHECK:

  DEFENCE CoC prerequisites:
    [ ] All MRB sections 1-7 have status VALIDATED or NOT_APPLICABLE
    [ ] No open NCRs without approved disposition
    [ ] All FAIR forms complete and validated (if FAIR required)
    [ ] Material certificates validated for all materials used
    [ ] Special process certificates validated
    [ ] All inspection reports validated
    [ ] All test reports validated
    [ ] Export compliance verified (if applicable)

  OIL & GAS CoC prerequisites:
    [ ] All MRB sections 1-6 have status VALIDATED or NOT_APPLICABLE
    [ ] All ITP Hold Points signed off
    [ ] All ITP Witness Points addressed
    [ ] No open NCRs without approved disposition
    [ ] PMI completed and validated (if required)
    [ ] Hydrostatic/pressure test completed and validated (if required)
    [ ] NORSOK MDS completed (if required)
    [ ] Preservation procedure defined (Section 7 preparation)

  IF ANY prerequisite FAILS:
    → BLOCK CoC generation
    → Report specific missing/failed items
    → CoC will not be generated until all prerequisites met
```

---

## SECTION 9: CROSS-DOCUMENT TRACEABILITY VALIDATION

### 9.1 Traceability Chain Verification

The validator must confirm that cross-references between documents form a complete, unbroken chain:

```
TRACEABILITY CHAIN:

  Purchase Order (PO number)
    └─→ Material Certificate (references PO, heat number)
        └─→ Goods Receiving Record (heat number, PO number)
            └─→ Material Traceability Matrix (heat number → part serial numbers)
                └─→ Manufacturing Process Sheet (part serial, material lot)
                    └─→ Inspection Reports (part serial, drawing rev)
                        └─→ FAIR Form 2 (material trace) + Form 3 (measurements)
                            └─→ Certificate of Conformance (part serial, PO, all refs)

VALIDATION RULE:
  At each link in the chain, verify:
    - PO number is consistent
    - Part number/serial is consistent
    - Material heat/lot number is consistent
    - Drawing revision is consistent
    - Dates are chronologically logical (material cert before machining, machining before inspection)
    - Quantity is consistent (parts produced <= material available)
```

### 9.2 Cross-Document Number Matching

```
AUTOMATED CROSS-REFERENCE CHECKS:

  CHECK 1: PO Number Consistency
    → Same PO number appears in: PO copy, material order, process sheet, CoC

  CHECK 2: Heat Number Chain
    → Material cert heat number = Goods receiving heat number
    → Goods receiving heat number = Traceability matrix heat number
    → Traceability matrix heat number → Part serial numbers

  CHECK 3: Drawing Revision Lock
    → Drawing revision on inspection report = Drawing revision on FAIR
    → Drawing revision on process sheet = Drawing revision on PO
    → IF drawing was revised during production: change control documented

  CHECK 4: Part Serial Continuity
    → Serial numbers on inspection reports = Serial numbers on CoC
    → No serial number gaps without explanation (scrapped parts documented)

  CHECK 5: Date Logic
    → Material cert date ≤ Goods receiving date
    → Goods receiving date ≤ Manufacturing start date
    → Manufacturing start date ≤ Inspection date
    → Inspection date ≤ CoC date
    → CoC date ≤ Shipment date
```

---

## SECTION 10: VALIDATION REPORTING

### 10.1 Validation Summary Report

```
ORDER VALIDATION REPORT
========================
Order:      [PO Number]
Customer:   [Customer Name]
Date:       [Validation Date]
Validator:  [QA Engineer / System]

SUMMARY:
  Total documents required:  [N]
  Validated (PASS):          [N] (green)
  Rejected (FAIL):           [N] (red — action required)
  Pending:                   [N] (yellow — awaiting documents)
  Not applicable:            [N] (grey)
  Waived:                    [N] (blue — customer-approved deviation)

VALIDATION SCORE: [X]% complete

CRITICAL FINDINGS:
  [List of any CRITICAL severity failures]

BLOCKING ITEMS (must resolve before shipment):
  [List of items preventing CoC generation and MRB release]

RECOMMENDATIONS:
  [Corrective actions for each rejected document]
```

### 10.2 Failure Severity Classification

| Severity | Definition | Action | Timeline |
|----------|-----------|--------|----------|
| **CRITICAL** | Missing or wrong document that prevents MRB release | Immediate correction required | Must resolve before CoC |
| **MAJOR** | Incomplete or non-compliant document | Correction or customer waiver required | Must resolve before shipment |
| **MINOR** | Formatting issue, legibility concern | Correct if possible, document if not | Best effort before shipment |
| **OBSERVATION** | Improvement opportunity, not a failure | Log for process improvement | No immediate action |

---

## SECTION 11: DIGITAL VALIDATION RULES

### 11.1 Format Validation

```
FORMAT CHECKS:

  PDF/A Compliance (for archival documents):
    [ ] File is valid PDF/A (PDF/A-1b minimum, PDF/A-3 preferred)
    [ ] No embedded JavaScript or dynamic content
    [ ] All fonts embedded
    [ ] Color space compliant
    [ ] File not password-protected (or password provided)

  Electronic Signatures:
    [ ] Digital signature valid and not expired
    [ ] Signer identity verifiable
    [ ] Document not modified after signing
    [ ] Timestamp present

  Scan Quality (for scanned documents):
    [ ] Resolution minimum 300 DPI
    [ ] All pages legible
    [ ] No truncated or cut-off content
    [ ] Color where needed (e.g., stamps, colored markings)
```

### 11.2 Metadata Validation

```
DOCUMENT METADATA:
  [ ] Document title matches SDRL requirement
  [ ] Document date present and logical
  [ ] Document revision/version tracked
  [ ] File naming convention followed (if Aurelian standard applies)
  [ ] File size reasonable (not empty, not corrupted)
```

---

## SECTION 12: EPICOR ERP INTEGRATION NOTES

For documents routed through Epicor ERP (supplier documents serving multiple orders):

```
ERP VALIDATION INTERFACE:

  INCOMING (Supplier → ERP):
    - Material certificates attached to Purchase Order receipt
    - Linked to heat/lot number in ERP material master
    - Available for routing to ANY order using that material

  OUTGOING (ERP → Order MRB):
    - Validator confirms ERP document is linked to correct order
    - Validator confirms material lot matches order's traceability matrix
    - Validator confirms document version is current (not superseded)

  CRITICAL RULE:
    One material certificate can serve MULTIPLE orders
    → Validator must confirm the specific heat/lot number on the cert
       matches the material ACTUALLY USED in the specific order being validated
    → This prevents cert-shopping (using a cert from a different material batch)
```

---

## SECTION 13: VALIDATION AUTOMATION LEVELS

### 13.1 Automation Maturity Model

| Level | Description | Checks | Human Role |
|-------|-------------|--------|------------|
| **Level 1** (Launch) | Checklist-driven | L1 Existence, L2 Format basics | QA engineer validates L3-L5 manually with checklist guidance |
| **Level 2** (6 months) | Semi-automated | L1-L2 automated, L3 partially | QA engineer validates compliance and traceability |
| **Level 3** (12 months) | Mostly automated | L1-L4 automated via OCR/parsing | QA engineer reviews exceptions and signs off |
| **Level 4** (24 months) | Fully automated | L1-L5 automated with AI parsing | QA engineer handles only exceptions and customer disputes |

### 13.2 Phase 1 (Launch) — Minimum Viable Validation

At production start (August 2027), the validator operates as an intelligent checklist system:

```
PHASE 1 CAPABILITIES:
  ✅ Parse SDRL requirements (via aurelian-sdrl-parser output)
  ✅ Track document collection status per requirement
  ✅ Provide validation checklists per document type
  ✅ Flag missing documents
  ✅ Generate validation summary reports
  ✅ Check date logic and PO number consistency
  ✅ Block CoC generation when prerequisites not met

  ❌ NOT YET: OCR-based content extraction from certificates
  ❌ NOT YET: Automated compliance checking of values vs. specification limits
  ❌ NOT YET: AI-powered cross-reference verification
```
