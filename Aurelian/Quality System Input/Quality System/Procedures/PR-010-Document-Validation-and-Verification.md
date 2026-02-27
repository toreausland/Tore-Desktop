# DOCUMENT VALIDATION AND VERIFICATION

| Field | Value |
|-------|-------|
| **Document No.** | PR-010 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-19 |
| **Approved By** | Quality Manager |
| **Classification** | Internal |
| **ISO 9001 Clause** | 7.5, 8.6 |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-19 | Quality Manager | Initial Release |

---

## 1. Purpose

This procedure defines the systematic validation of every document collected for inclusion in a Manufacturing Record Book (MRB). Validation ensures that all documents meet their SDRL-specified requirements for existence, format, completeness, compliance, and traceability BEFORE they are accepted into the MRB and before the Certificate of Conformance (CoC) can be generated.

The Document Validator is the quality gate between document collection and MRB assembly. No document enters the MRB without passing validation. No CoC is generated until all documents are validated.

## 2. Scope

This procedure applies to:

- All documents collected for Defence MRBs (AS9100/AQAP 2110)
- All documents collected for Oil & Gas MRBs/MDRs (NORSOK/API)
- All documents collected for Maritime and general engineering MRBs
- Material certificates (EN 10204 Types 2.1, 2.2, 3.1, 3.2)
- AS9102 First Article Inspection Reports (FAIR)
- Dimensional inspection reports
- Non-destructive testing (NDT) reports
- Special process certificates
- ITP compliance records
- PMI reports
- All other documents required by the SDRL

This procedure does NOT apply to:

- Pre-production material release review (covered under PR-008)
- CoC generation (covered under PR-011)
- Final MRB assembly (covered under PR-012)

## 3. References

| Document | Title |
|----------|-------|
| QM-001 | Quality Manual |
| PR-004 | Nonconformance and CAPA |
| PR-006 | CNC Process Control |
| PR-008 | Incoming Material Review and Release |
| PR-009 | SDRL Processing and MRB Management |
| PR-011 | Certificate of Conformance |
| PR-012 | MRB Assembly and Release |
| EN 10204:2004 | Metallic Products — Types of Inspection Documents |
| AS9102 | First Article Inspection Requirement |
| ASME Section V | Nondestructive Examination |
| EN ISO 17640 | Non-destructive Testing of Welds — Ultrasonic Testing |
| ASTM E8/E8M | Standard Test Methods for Tension Testing |
| ASTM E18 | Standard Test Methods for Rockwell Hardness |
| ASTM E112 | Standard Test Methods for Determining Average Grain Size |
| NORSOK M-650 | Qualification of Manufacturers |

## 4. Definitions

| Term | Definition |
|------|-----------|
| **Validation** | The systematic verification that a document meets all specified requirements for existence, format, completeness, compliance, and traceability |
| **Validation Layer** | One of five sequential checks applied to every document (L1 through L5) |
| **Correction Request** | A formal notification issued when a document fails validation, specifying the exact failure and required corrective action |
| **Traceability Chain** | The linked sequence of document references that connects raw material to finished product (PO → material cert → goods receiving → traceability matrix → process sheet → inspection → FAIR → CoC) |
| **Borderline Result** | A test result within 5% of any specification limit, requiring additional review |
| **Waiver** | A customer-approved deviation from a SDRL requirement, allowing a document to be accepted despite non-compliance |

## 5. Responsibilities

| Role | Responsibility |
|------|---------------|
| **Quality Manager** | Owns this procedure. Approves waivers and deviations. Final authority on borderline decisions. Manages validation KPIs. |
| **QA Engineer** | Performs document validation against SDRL requirements. Issues Correction Requests. Maintains validation records. Monitors overall MRB completion status. |
| **Production Manager** | Ensures production-generated documents (CNC data, process sheets, in-process records) are submitted for validation in a timely manner. |
| **Purchasing** | Coordinates with suppliers to resolve document failures for externally sourced documents (material certs, special process certs). |
| **Commercial Manager** | Communicates with customer on waiver requests when documents cannot meet SDRL requirements. |

## 6. Procedure

### 6.1 Validation Principle

```
RULE: Every document must be validated BEFORE it enters the MRB.
      No document enters the MRB without passing validation.
      Validation failures generate actionable Correction Requests.
      The validator does NOT modify documents — it only accepts or rejects.
```

**Validation reference document:** The QA Engineer validates each incoming document against the **MRB Index** (Form FM-009-04) generated from the SDRL at order initialization (PR-009 Section 6.6). The MRB Index is the order-specific list of every document required for this particular order. It is variable from order to order because it is derived from the SDRL. The MRB Index tells the validator:

- What documents are expected (L1: Existence check)
- What format each document must be in (L2: Format check)
- What standard each document must comply with (L4: Compliance check)
- How each document links to the order's traceability chain (L5: Traceability check)

As documents are validated, their status in the MRB Index is updated from RECEIVED → VALIDATED (or REJECTED). The MRB Index is therefore both the input to and the live status tracker for the validation process.

### 6.2 Five-Layer Validation Framework

Each document collected for the MRB passes through 5 validation layers in sequence. A failure at any layer halts the document from proceeding to the MRB.

| Layer | Check | Description | Failure Action |
|-------|-------|-------------|----------------|
| **L1: Existence** | Document received? | Has the document been collected from its source? | Flag as MISSING, notify responsible party |
| **L2: Format** | Correct format? | PDF/A, signed, correct template, legible | Flag as FORMAT_ERROR, request re-submission |
| **L3: Completeness** | All fields populated? | No blank mandatory fields, all pages present | Flag as INCOMPLETE, identify missing fields |
| **L4: Compliance** | Meets standard? | Content complies with referenced standard (EN 10204, AS9102, etc.) | Flag as NON_COMPLIANT, specify which requirement fails |
| **L5: Traceability** | Links verified? | Cross-references match (heat numbers, PO numbers, part numbers, dates) | Flag as TRACEABILITY_BREAK, identify broken link |

### 6.3 Document Validation Status Model

| Status | Meaning |
|--------|---------|
| **PENDING** | Document not yet received |
| **RECEIVED** | Document received, not yet validated |
| **VALIDATING** | Validation in progress |
| **VALIDATED** | Passed all 5 layers |
| **REJECTED** | Failed one or more layers (with specific failure codes) |
| **CORRECTED** | Previously rejected, re-submitted for re-validation |
| **WAIVED** | Customer-approved deviation — document accepted as-is |
| **NOT_APPLICABLE** | Requirement waived or not relevant for this order |

### 6.4 Material Certificate Validation (EN 10204)

#### 6.4.1 Type 3.1 Certificate — Full Validation Checklist

For EN 10204 Type 3.1 (minimum for defence, standard for oil & gas):

**L1 — Existence:**

- [ ] Certificate document exists for each material lot/heat referenced in the order

**L2 — Format:**

- [ ] PDF or original scan (legible, all text readable)
- [ ] Manufacturer's letterhead or official format
- [ ] Date of issue present

**L3 — Completeness (ALL of the following must be present):**

- [ ] Material specification (e.g., ASTM A182 F316L, AMS 4078)
- [ ] Heat number / lot number
- [ ] Chemical composition — ACTUAL values (not "conforms" or "typical")
- [ ] Mechanical properties:
  - [ ] Tensile strength (actual value + unit)
  - [ ] Yield strength (actual value + unit)
  - [ ] Elongation (actual value + %)
  - [ ] Reduction of area (if applicable)
- [ ] Heat treatment condition (e.g., "Solution Annealed at 1040°C, Water Quenched")
- [ ] Product form and dimensions
- [ ] Quantity / weight
- [ ] Manufacturer name and address

**L4 — Compliance:**

- [ ] Chemical composition within specification limits
- [ ] Mechanical properties within specification limits
- [ ] Heat treatment per specification requirements
- [ ] Test methods referenced (e.g., ASTM E8 for tensile, ASTM E18 for hardness)
- [ ] Standard edition/year referenced is current or customer-approved

**L5 — Traceability:**

- [ ] Heat number matches goods receiving record (PR-008)
- [ ] Heat number matches material traceability matrix
- [ ] Material specification matches PO/drawing requirement
- [ ] If material serves multiple orders: ERP linkage verified for each order

**Authorized Representative:**

- [ ] Name of authorized inspection representative
- [ ] Signature or electronic validation mark
- [ ] Statement: "This certificate is issued in accordance with EN 10204:2004, Type 3.1"

#### 6.4.2 Type 3.2 Additional Checks

For EN 10204 Type 3.2, all Type 3.1 checks apply PLUS:

- [ ] Third-party inspector organization identified
- [ ] Third-party inspector name and credentials
- [ ] Third-party signature/stamp present
- [ ] Third-party accreditation reference (if applicable)
- [ ] Statement confirming independent verification of test results
- [ ] Third-party organization is independent of the manufacturer

#### 6.4.3 Common Material Certificate Failures

| Failure | Severity | Resolution |
|---------|----------|------------|
| Missing heat number | CRITICAL | Reject, request new certificate |
| "Typical" vs actual values reported | CRITICAL | Reject, require actual test results |
| Expired standard edition referenced | MAJOR | Verify with customer if acceptable |
| Missing mechanical test results | CRITICAL | Reject, require complete certificate |
| Unsigned (no authorized representative) | CRITICAL | Reject, request signed copy |
| Wrong material grade | CRITICAL | Reject, investigate potential material mix-up |
| Illegible scan | MAJOR | Request higher quality scan |
| Values borderline (within 5% of limits) | REVIEW | Escalate to Quality Manager |

### 6.5 AS9102 FAIR Validation (Defence Orders)

When FAIR is required (per PR-009 Section 6.4), all three forms must be validated:

#### 6.5.1 Form 1 — Part Number Accountability

- [ ] Part number matches PO / drawing
- [ ] Part name / description correct
- [ ] Drawing number and revision correct
- [ ] Organization name: Aurelian Manufacturing AS
- [ ] Part serial number(s) for inspected article(s)
- [ ] FAIR reason code documented (first production, design change, process change, tooling change, production gap, other)
- [ ] Signature and date of preparer
- [ ] Signature and date of approver

#### 6.5.2 Form 2 — Product Accountability

- [ ] All raw materials listed with:
  - [ ] Material specification (e.g., AMS 4078)
  - [ ] Supplier name
  - [ ] Certificate type (EN 10204 type)
  - [ ] Heat/lot number
  - [ ] Certificate reference (must link to actual certificate in MRB Section 3)
- [ ] All special processes listed with:
  - [ ] Process type (anodize, heat treat, NDT, etc.)
  - [ ] Specification reference
  - [ ] Processor name
  - [ ] Certificate/report reference
- [ ] All purchased components listed (if applicable)
- [ ] Traceability chain complete: raw material → finished part

#### 6.5.3 Form 3 — Characteristic Accountability

- [ ] Every characteristic from the drawing identified:
  - [ ] Characteristic number (sequential)
  - [ ] Drawing requirement (nominal + tolerance)
  - [ ] Measurement result (ACTUAL value, not just PASS/FAIL)
  - [ ] Upper/lower specification limits
  - [ ] PASS/FAIL determination correct
- [ ] All critical dimensions marked as "Key Characteristic" if flagged on drawing
- [ ] GD&T callouts properly interpreted and measured
- [ ] Measurement method identified (CMM, micrometer, gauge, etc.)
- [ ] No FAIL results without accompanying NCR or deviation approval
- [ ] Statistical data (Cp, Cpk) if required by customer

**Data Source Verification:**

- [ ] Characteristic data matches CMM/inspection report data
- [ ] CNC in-machine measurement data cross-referenced where applicable
- [ ] All measurement instruments have current calibration (calibration certificate reference)

### 6.6 Dimensional Inspection Report Validation

**L3 — Completeness:**

- [ ] Part number and serial number
- [ ] Drawing number and revision
- [ ] Inspection date
- [ ] Inspector name/ID
- [ ] All drawing dimensions measured
- [ ] Actual values recorded (not just PASS/FAIL)
- [ ] Measurement uncertainty stated (if required by customer)
- [ ] Equipment identification (CMM serial number, instrument IDs)

**L4 — Compliance:**

- [ ] All dimensions within tolerance
- [ ] If any out-of-tolerance:
  - [ ] NCR raised (per PR-004)
  - [ ] Disposition recorded (use-as-is, rework, scrap, return to vendor)
  - [ ] Customer approval obtained (if use-as-is or repair)
- [ ] Surface finish measurements included (Ra, Rz) where specified
- [ ] Thread gauge results (GO/NO-GO) where applicable

**L5 — Traceability:**

- [ ] Inspection report linked to correct order/serial number
- [ ] Instruments have valid calibration (date within calibration interval)
- [ ] Inspector qualified for this inspection type

### 6.7 NDT Report Validation

- [ ] NDT method identified (RT, UT, MT, PT, ET, VT)
- [ ] Applicable standard referenced (e.g., ASME V, EN ISO 17640)
- [ ] NDT procedure reference number
- [ ] Acceptance criteria specified and referenced
- [ ] Technician qualification:
  - [ ] Name and certification level (e.g., ASNT Level II, PCN Level 2)
  - [ ] Certification number and expiry date
- [ ] Equipment:
  - [ ] Equipment identification
  - [ ] Calibration status current
- [ ] Results:
  - [ ] Area/volume inspected clearly defined
  - [ ] All indications recorded with location and size
  - [ ] Accept/reject determination for each indication
  - [ ] Overall PASS/FAIL
- [ ] Signed by qualified technician AND reviewed by Level III (if required)

### 6.8 ITP Compliance Validation (Oil & Gas Orders)

For each Hold Point (H):

- [ ] Customer/third-party inspector was present
- [ ] Sign-off obtained BEFORE production continued
- [ ] Date and time of inspection recorded
- [ ] Inspector name and organization recorded
- [ ] Results/findings documented
- [ ] If failed: NCR raised, corrective action completed before proceeding

For each Witness Point (W):

- [ ] Customer notified minimum 48–72 hours in advance
- [ ] If customer attended: sign-off obtained
- [ ] If customer waived attendance: waiver documented (email/letter reference)
- [ ] Activity proceeded with or without customer presence
- [ ] Results documented regardless of attendance

For each Review Point (R):

- [ ] Documentation submitted to customer
- [ ] Submission date and method recorded
- [ ] Customer acknowledgement received (or timeout per contract terms)
- [ ] Comments addressed if any

Overall ITP:

- [ ] All H/W/R points have been addressed
- [ ] No open Hold Points remaining
- [ ] ITP summary sheet signed off by Aurelian QA
- [ ] Customer final ITP acceptance (if required by contract)

### 6.9 PMI Report Validation

- [ ] PMI method identified (XRF, OES, Laboratory)
- [ ] Equipment identification and calibration status current
- [ ] Operator qualification documented
- [ ] Material/component tested:
  - [ ] Part identification (serial/lot)
  - [ ] Test location on component
- [ ] Results:
  - [ ] Elemental analysis results
  - [ ] Material grade identification confirmed
  - [ ] Statement: "Material composition consistent with [specification]"
- [ ] Cross-reference:
  - [ ] Heat number matches material certificate
  - [ ] Grade matches PO/drawing specification
  - [ ] Results consistent with EN 10204 certificate values (within instrument accuracy)

**Common PMI Failures:**

| Failure | Action |
|---------|--------|
| Material swap (wrong grade identified) | CRITICAL — quarantine part immediately |
| Missing elements in analysis (e.g., carbon not detectable by XRF) | Use OES method instead |
| Calibration expired | Reject report, re-test with calibrated instrument |

### 6.10 Special Process Certificate Validation

For surface treatment, external heat treatment, and other special processes:

- [ ] Process performed by qualified/approved supplier
- [ ] Specification referenced matches PO/drawing requirement
- [ ] Process parameters documented (temperature, duration, medium)
- [ ] Test results (coating thickness, hardness, adhesion) where required
- [ ] Signed by responsible representative
- [ ] Batch/lot traceability to correct parts
- [ ] Supplier NADCAP accreditation valid (if required for defence)

### 6.11 Cross-Document Traceability Verification

After individual document validation, the QA Engineer verifies the complete traceability chain across all documents:

```
TRACEABILITY CHAIN VERIFICATION:

  PO/Contract
      ↓ PO number matches on all documents
  Material Certificate (EN 10204)
      ↓ Heat number links to:
  Goods Receiving Record (PR-008)
      ↓ Heat number + PO links to:
  Material Traceability Matrix
      ↓ Heat number + serial numbers link to:
  Process Sheet / CNC Records
      ↓ Serial number + operation links to:
  Inspection Reports (dimensional, NDT, hardness)
      ↓ Serial number + results link to:
  FAIR Form 3 (if defence)
      ↓ All data cross-referenced links to:
  Certificate of Conformance
      ↓ References MRB number
  Manufacturing Record Book
```

**Verify at minimum:**

1. PO number is consistent across all documents
2. Part number and drawing revision are consistent across all documents
3. Material heat number(s) chain from certificate → goods receiving → traceability matrix → process records → inspection records
4. Serial numbers chain from manufacturing → inspection → FAIR → CoC
5. Dates are chronologically consistent (material cert date ≤ goods receiving date ≤ manufacturing date ≤ inspection date ≤ CoC date)
6. No orphan documents (documents present that do not link to any requirement)
7. No missing links (requirements present that have no corresponding document)

### 6.12 Correction Request Process

When a document fails validation at any layer:

**Step 1:** QA Engineer records the failure on Form FM-010-01 (Correction Request):

| Field | Content |
|-------|---------|
| CR Number | AM-CR-[YYYY]-[NNNNN] |
| Order reference | PO number, MRB number |
| Document type | Type of document that failed |
| Validation layer | L1, L2, L3, L4, or L5 |
| Failure code | MISSING, FORMAT_ERROR, INCOMPLETE, NON_COMPLIANT, TRACEABILITY_BREAK |
| Specific finding | Exact description of what failed |
| Required action | What needs to be done to correct the document |
| Responsible party | Who must take corrective action |
| Due date | When corrected document is needed |

**Step 2:** Correction Request is issued to the responsible party:

| Source of Document | Responsible Party |
|-------------------|-------------------|
| Supplier material certificate | Purchasing → Supplier |
| Special process certificate | Purchasing → Sub-supplier |
| CNC/manufacturing records | Production Manager |
| Inspection reports | QA Engineer / Inspector |
| FAIR forms | QA Engineer |
| ITP records | QA Engineer + Customer |

**Step 3:** Corrected document is re-submitted and goes through the full 5-layer validation again.

**Step 4:** If a document cannot be corrected (e.g., supplier cannot provide required test data):

1. QA Engineer escalates to Quality Manager
2. Quality Manager determines if a customer waiver can be requested
3. Commercial Manager communicates waiver request to customer
4. If waiver approved: document status set to WAIVED with customer approval reference
5. If waiver denied: NCR raised per PR-004, with production impact assessment

### 6.13 CoC Prerequisite Gate

Before PR-011 (CoC generation) can proceed, ALL of the following must be confirmed:

**Defence Orders:**

- [ ] MRB Section 1 (Identification) — all documents VALIDATED
- [ ] MRB Section 2 (Contract Documentation) — all documents VALIDATED
- [ ] MRB Section 3 (Material Documentation) — all documents VALIDATED or N/A
- [ ] MRB Section 4 (Manufacturing Process) — all documents VALIDATED
- [ ] MRB Section 5 (Special Processes) — all documents VALIDATED or N/A
- [ ] MRB Section 6 (Inspection) — all documents VALIDATED
- [ ] MRB Section 7 (Testing) — all documents VALIDATED or N/A
- [ ] FAIR complete (if required) — VALIDATED
- [ ] No open CRITICAL NCRs
- [ ] All material certificates validated
- [ ] Export compliance cleared (if applicable)

**Oil & Gas Orders:**

- [ ] MRB Section 1 (General Information) — all documents VALIDATED
- [ ] MRB Section 2 (Purchase/Technical) — all documents VALIDATED
- [ ] MRB Section 3 (Material Documentation) — all documents VALIDATED
- [ ] MRB Section 4 (Manufacturing Records) — all documents VALIDATED
- [ ] MRB Section 5 (Testing/Inspection) — all documents VALIDATED
- [ ] All ITP Hold Points signed off
- [ ] All ITP Witness Points addressed
- [ ] PMI completed (if required) — VALIDATED
- [ ] Hydrostatic/pressure test (if required) — VALIDATED
- [ ] No open CRITICAL NCRs
- [ ] NORSOK MDS completed (if required)

**If ANY prerequisite is not met:**

- CoC generation is BLOCKED
- QA Engineer receives a list of all blocking items
- No partial or conditional CoCs are generated

## 7. Records

| Form | Title | Retention |
|------|-------|-----------|
| FM-010-01 | Correction Request | Per order archival requirement (minimum 15 years) |
| FM-010-02 | Document Validation Log | Per order archival requirement (minimum 15 years) |
| FM-010-03 | Cross-Document Traceability Verification Record | Per order archival requirement (minimum 15 years) |
| FM-010-04 | CoC Prerequisite Gate Checklist | Per order archival requirement (minimum 15 years) |

## 8. Key Performance Indicators

| KPI | Target | Measured |
|-----|--------|----------|
| Document first-pass validation rate | > 85% of documents pass validation on first submission | Monthly |
| Correction Request closure time | < 3 business days average | Monthly |
| Traceability chain integrity | 100% of MRBs have complete, unbroken traceability chain | Per order |
| CoC gate blocking rate | < 10% of orders blocked at CoC prerequisite gate | Quarterly |
| Post-shipment document defects | 0 document defects found by customer after delivery | Per incident |

## 9. Flowchart

```
Document Received from Source
            │
            ▼
┌─────────────────────────┐
│ L1: EXISTENCE            │──FAIL──→ MISSING → Notify responsible party
│ Document exists?         │
└───────────┬─────────────┘
            │ PASS
            ▼
┌─────────────────────────┐
│ L2: FORMAT               │──FAIL──→ FORMAT_ERROR → Request re-submission
│ Correct format/legible?  │
└───────────┬─────────────┘
            │ PASS
            ▼
┌─────────────────────────┐
│ L3: COMPLETENESS         │──FAIL──→ INCOMPLETE → Issue Correction Request
│ All fields populated?    │
└───────────┬─────────────┘
            │ PASS
            ▼
┌─────────────────────────┐
│ L4: COMPLIANCE           │──FAIL──→ NON_COMPLIANT → Issue Correction Request
│ Meets standard/spec?    │
└───────────┬─────────────┘
            │ PASS
            ▼
┌─────────────────────────┐
│ L5: TRACEABILITY         │──FAIL──→ TRACEABILITY_BREAK → Investigate
│ Cross-refs match?        │
└───────────┬─────────────┘
            │ PASS
            ▼
   Document status → VALIDATED
   Enter into MRB slot
            │
            ▼
   All MRB documents VALIDATED?
      │               │
     YES              NO
      │               │
      ▼               ▼
  CoC Prerequisite   Continue
  Gate → PR-011      collecting/
                     validating
```

## 10. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Prepared By | Quality Manager | _______ | _______ |
| Reviewed By | Production Manager | _______ | _______ |
| Approved By | Managing Director | _______ | _______ |

This document is controlled. Printed copies are uncontrolled unless stamped "CONTROLLED COPY" in red.
