# CUSTOMER-FACING TEMPLATES — SDRL, MRB INDEX, AND REQUIREMENT PROFILES

| Field | Value |
|-------|-------|
| **Document No.** | AM-CT-001 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Approved By** | Quality Manager / Commercial Manager |
| **Classification** | Internal — Engineering |
| **Work Package** | WP-2 |
| **Status** | Draft |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-21 | Quality Manager | Initial Release. Oil & Gas templates primary, Defence templates included. |

---

## 1. Purpose

This document defines all customer-facing templates used by the Digital MRB Builder to receive, parse, and structure customer documentation requirements. These templates are the **system's input layer** — everything downstream (validation, CoC generation, MRB assembly) depends on the structured data captured by these templates.

This document delivers Work Package 2 (WP-2) as defined in the MRB Builder Status Report.

## 2. Scope

This document covers:

- Oil & Gas SDRL Template (7-section, NORSOK/API) — **Phase 0 primary**
- Defence SDRL Template (8-section, AS9100/AQAP) — **Phase 0 secondary**
- MRB Index baseline templates for both industries
- Customer Requirement Profile (material-specific acceptance criteria)
- Data format specifications for SDRL parser (AM-TS-001 Section 6.4)

## 3. References

| Document | Title |
|----------|-------|
| PR-009 | SDRL Processing and MRB Management |
| PR-008 | Incoming Material Review and Release |
| PR-010 | Document Validation and Verification |
| AM-TS-001 | IT/System Technical Specification |
| AM-SDRL-2026-001 | Shipment Documentation Requirements (SDRL/MRB) |
| EN 10204:2004 | Metallic Products — Types of Inspection Documents |
| NORSOK M-650 | Qualification of Manufacturers |
| NORSOK M-630 | Material Data Sheets for Piping |
| NORSOK Z-CR-006 | Documentation Requirements |
| AS9102 | First Article Inspection Requirement |
| AQAP 2110 | NATO Quality Assurance Requirements |

---

## 4. Oil & Gas SDRL Template (7-Section)

### 4.1 Template Overview

This is the primary Phase 0 template. It defines the standard SDRL structure for Oil & Gas / Energy sector orders referencing NORSOK, API, ASME, ASTM, or DNV standards.

**Template ID:** `SDRL-OG-001`
**Industry classification:** OIL_GAS
**MRB sections:** 7
**Default line items:** 30
**Applicable standards:** NORSOK M-650, NORSOK Z-CR-006, EN 10204, API Q1

### 4.2 SDRL Line Items — Oil & Gas

Each line item in the SDRL represents one document the supplier must deliver. The customer may select, deselect, or modify line items based on order-specific requirements.

**Section 1 — General Information**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| OG-01-01 | MRB Cover Page | — | Yes | PDF/A | FOR_INFO | STANDARD | INTERNAL_QA |
| OG-01-02 | Master Document Index | — | Yes | PDF/A | FOR_INFO | STANDARD | INTERNAL_QA |
| OG-01-03 | Quality Plan / ITP | ISO 10005 / customer spec | Conditional | PDF/A | FOR_APPROVAL | CRITICAL | INTERNAL_QA |
| OG-01-04 | Project Specification Compliance Matrix | Customer spec | Conditional | PDF/A | FOR_REVIEW | MAJOR | INTERNAL_QA |
| OG-01-05 | Document Transmittal Record | — | Yes | PDF/A | FOR_INFO | STANDARD | INTERNAL_QA |

**Section 2 — Purchase and Technical Requirements**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| OG-02-01 | Purchase Order (relevant pages) | — | Yes | PDF | FOR_INFO | STANDARD | CUSTOMER |
| OG-02-02 | Technical Specification | Customer spec | Conditional | PDF | FOR_INFO | MAJOR | CUSTOMER |
| OG-02-03 | Approved SDRL | — | Yes | PDF | FOR_INFO | STANDARD | CUSTOMER |
| OG-02-04 | Equipment Data Sheet | Customer spec | Conditional | PDF | FOR_INFO | STANDARD | CUSTOMER |
| OG-02-05 | Approved Manufacturing Drawings | Customer spec | Conditional | PDF/native CAD | FOR_APPROVAL | CRITICAL | CUSTOMER |
| OG-02-06 | Deviation Request / Concession | — | Conditional | PDF/A | FOR_APPROVAL | CRITICAL | INTERNAL_QA |

**Section 3 — Material Documentation**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| OG-03-01 | Material Test Certificate (raw material) | EN 10204 Type 3.1 or 3.2 | Yes | PDF | FOR_REVIEW | CRITICAL | SUPPLIER |
| OG-03-02 | Material Traceability Matrix | — | Yes | PDF/A | FOR_REVIEW | CRITICAL | INTERNAL_QA |
| OG-03-03 | PMI Report (Positive Material Identification) | ASTM E1476 / customer spec | Conditional | PDF | FOR_REVIEW | CRITICAL | INSPECTION |
| OG-03-04 | Material Certificates Summary / Cross-Reference | — | Yes | PDF/A | FOR_INFO | MAJOR | INTERNAL_QA |
| OG-03-05 | Raw Material Receiving Inspection Report | — | Yes | PDF/A | FOR_INFO | MAJOR | INTERNAL_QA |
| OG-03-06 | NORSOK Material Data Sheet (MDS) compliance | NORSOK M-630 | Conditional | PDF/A | FOR_REVIEW | CRITICAL | INTERNAL_QA |

**Section 4 — Manufacturing Records**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| OG-04-01 | Manufacturing Procedure (approved) | Customer spec | Conditional | PDF/A | FOR_APPROVAL | MAJOR | INTERNAL_QA |
| OG-04-02 | Welding Documentation (WPS, PQR, WPQ) | ASME IX / EN ISO 15614 | Conditional | PDF | FOR_REVIEW | CRITICAL | SPECIAL_PROCESS |
| OG-04-03 | Heat Treatment Records / Certificates | AMS 2750 / customer spec | Conditional | PDF | FOR_REVIEW | CRITICAL | SPECIAL_PROCESS |
| OG-04-04 | Machining Parameters / Process Sheet | — | Conditional | PDF/A | FOR_INFO | STANDARD | CNC_INLINE |
| OG-04-05 | Surface Finish Records | Customer spec | Conditional | PDF/A | FOR_REVIEW | MAJOR | INSPECTION |

**Section 5 — Testing and Inspection**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| OG-05-01 | Inspection Test Plan (ITP) — signed off | ISO 10005 / customer spec | Conditional | PDF/A | FOR_APPROVAL | CRITICAL | INTERNAL_QA |
| OG-05-02 | Dimensional Inspection Report (final) | Customer drawing | Yes | PDF/A | FOR_REVIEW | CRITICAL | INSPECTION |
| OG-05-03 | NDT Reports (UT, RT, MT, PT) | ASME V / EN ISO 17640 / customer spec | Conditional | PDF | FOR_REVIEW | CRITICAL | SPECIAL_PROCESS |
| OG-05-04 | Hydrostatic / Pressure Test Report | Customer spec / API | Conditional | PDF | FOR_REVIEW | CRITICAL | INSPECTION |
| OG-05-05 | Functional Test Report | Customer spec | Conditional | PDF | FOR_REVIEW | MAJOR | INSPECTION |
| OG-05-06 | Visual Inspection Report | — | Yes | PDF/A | FOR_INFO | STANDARD | INSPECTION |
| OG-05-07 | Hardness Test Report | ASTM E18 / E384 | Conditional | PDF | FOR_REVIEW | MAJOR | INSPECTION |
| OG-05-08 | ITP Hold/Witness/Review Point Sign-off Records | — | Conditional | PDF/A | FOR_REVIEW | CRITICAL | INTERNAL_QA |

**Section 6 — Compliance Documentation**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| OG-06-01 | Certificate of Conformance (CoC) | — | Yes | PDF/A | FOR_INFO | CRITICAL | INTERNAL_QA |
| OG-06-02 | NCR Log / Nonconformance Summary | — | Conditional | PDF/A | FOR_REVIEW | MAJOR | INTERNAL_QA |
| OG-06-03 | NORSOK Compliance Statement | NORSOK M-650 | Conditional | PDF/A | FOR_REVIEW | CRITICAL | INTERNAL_QA |
| OG-06-04 | API Monogram Sheet | API spec | Conditional | PDF/A | FOR_INFO | MAJOR | INTERNAL_QA |
| OG-06-05 | PED / ATEX Declaration (if applicable) | PED 2014/68/EU | Conditional | PDF/A | FOR_INFO | CRITICAL | INTERNAL_QA |

**Section 7 — Preservation and Shipping**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| OG-07-01 | Preservation Procedure / Records | Customer spec | Conditional | PDF/A | FOR_REVIEW | STANDARD | INTERNAL_QA |
| OG-07-02 | Packing List | — | Yes | PDF/A | FOR_INFO | STANDARD | INTERNAL_QA |
| OG-07-03 | Shipping / Transport Documentation | — | Conditional | PDF | FOR_INFO | STANDARD | INTERNAL_QA |
| OG-07-04 | Export Compliance Declaration | — | Conditional | PDF/A | FOR_INFO | MAJOR | INTERNAL_QA |

### 4.3 SDRL Parser Field Mapping

When the system parses a customer-supplied SDRL (or when QA Engineer manually enters requirements), each line item maps to the following database fields (per AM-TS-001 Section 7):

| SDRL Field | Database Field | Type | Required |
|------------|---------------|------|----------|
| Line ID | `line_item_id` | VARCHAR(20) | Yes |
| Document Title | `doc_title` | VARCHAR(255) | Yes |
| Standard/Specification | `standard_ref` | VARCHAR(255) | No |
| Required (Yes/No/Conditional) | `is_required` | BOOLEAN | Yes |
| Format | `required_format` | ENUM (PDF, PDF_A, NATIVE, SIGNED) | Yes |
| Review Code | `review_code` | ENUM (FOR_INFO, FOR_REVIEW, FOR_APPROVAL) | Yes |
| Criticality | `criticality` | ENUM (CRITICAL, MAJOR, STANDARD) | Yes |
| Data Source | `data_source` | ENUM (CNC_INLINE, METROLOGY, INSPECTION, SUPPLIER, SPECIAL_PROCESS, INTERNAL_QA, CUSTOMER) | Yes |
| MRB Section | `mrb_section` | INTEGER (1-7 for O&G, 1-8 for Defence) | Yes |
| Timing | `submission_timing` | ENUM (WITH_SHIPMENT, BEFORE_SHIPMENT, AT_MILESTONE, ON_REQUEST) | Yes |
| Notes | `notes` | TEXT | No |

---

## 5. Defence SDRL Template (8-Section)

### 5.1 Template Overview

**Template ID:** `SDRL-DEF-001`
**Industry classification:** DEFENCE
**MRB sections:** 8
**Default line items:** 25
**Applicable standards:** AS9100D, AQAP 2110, MIL-STDs, DEF-STANs

### 5.2 SDRL Line Items — Defence

**Section 1 — Identification and Index**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| DEF-01-01 | MRB Cover Sheet | — | Yes | PDF/A | FOR_INFO | STANDARD | INTERNAL_QA |
| DEF-01-02 | Table of Contents / Master Index | — | Yes | PDF/A | FOR_INFO | STANDARD | INTERNAL_QA |
| DEF-01-03 | Document Revision Log | — | Conditional | PDF/A | FOR_INFO | STANDARD | INTERNAL_QA |

**Section 2 — Contract Documentation**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| DEF-02-01 | Purchase Order (relevant pages) | — | Yes | PDF | FOR_INFO | STANDARD | CUSTOMER |
| DEF-02-02 | Engineering Drawing (as-built revision) | Customer spec | Yes | PDF/native CAD | FOR_INFO | CRITICAL | CUSTOMER |
| DEF-02-03 | Specification List with revision levels | — | Yes | PDF/A | FOR_INFO | MAJOR | INTERNAL_QA |

**Section 3 — Material Documentation**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| DEF-03-01 | Material Test Certificates | EN 10204 Type 3.1 / 3.2 | Yes | PDF | FOR_REVIEW | CRITICAL | SUPPLIER |
| DEF-03-02 | Material Traceability Matrix | — | Yes | PDF/A | FOR_REVIEW | CRITICAL | INTERNAL_QA |
| DEF-03-03 | Raw Material Receiving Inspection | — | Yes | PDF/A | FOR_REVIEW | MAJOR | INTERNAL_QA |
| DEF-03-04 | Conflict Minerals Declaration | Dodd-Frank / EU regulation | Conditional | PDF/A | FOR_INFO | STANDARD | SUPPLIER |
| DEF-03-05 | Counterfeit Prevention Records | DFARS 252.246-7007 | Conditional | PDF/A | FOR_REVIEW | CRITICAL | INTERNAL_QA |

**Section 4 — Manufacturing Process Documentation**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| DEF-04-01 | Process Routing / Traveler (signed off) | — | Yes | PDF/A | FOR_INFO | MAJOR | INTERNAL_QA |
| DEF-04-02 | CNC Program Verification Record | — | Conditional | PDF/A | FOR_INFO | STANDARD | CNC_INLINE |
| DEF-04-03 | In-Process Inspection Records | — | Yes | PDF/A | FOR_REVIEW | MAJOR | INSPECTION |
| DEF-04-04 | Deviation / Waiver Records | — | Conditional | PDF/A | FOR_APPROVAL | CRITICAL | INTERNAL_QA |

**Section 5 — Special Process Documentation**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| DEF-05-01 | Heat Treatment Certification | AMS 2750 / customer spec | Conditional | PDF | FOR_REVIEW | CRITICAL | SPECIAL_PROCESS |
| DEF-05-02 | Surface Treatment Certification | Customer spec | Conditional | PDF | FOR_REVIEW | CRITICAL | SPECIAL_PROCESS |
| DEF-05-03 | NDT Reports (MT, PT, RT, UT) | ASME V / NAS 410 | Conditional | PDF | FOR_REVIEW | CRITICAL | SPECIAL_PROCESS |
| DEF-05-04 | Special Process Supplier Approvals (NADCAP) | NADCAP / customer approval | Conditional | PDF | FOR_INFO | CRITICAL | SPECIAL_PROCESS |

**Section 6 — Inspection Documentation**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| DEF-06-01 | First Article Inspection Report (FAIR) — Form 1, 2, 3 | AS9102 | Conditional | PDF/A | FOR_REVIEW | CRITICAL | INSPECTION + INTERNAL_QA |
| DEF-06-02 | Final Dimensional Inspection Report | Customer drawing | Yes | PDF/A | FOR_REVIEW | CRITICAL | INSPECTION |
| DEF-06-03 | CMM Reports | — | Conditional | PDF/native | FOR_REVIEW | MAJOR | INSPECTION |
| DEF-06-04 | Gage Calibration Records (referenced instruments) | ISO 10012 | Conditional | PDF | FOR_INFO | STANDARD | INTERNAL_QA |
| DEF-06-05 | Visual / Workmanship Inspection Record | — | Yes | PDF/A | FOR_INFO | STANDARD | INSPECTION |

**Section 7 — Test Documentation**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| DEF-07-01 | Mechanical Test Reports (tensile, hardness) | ASTM E8, E18, E384 | Conditional | PDF | FOR_REVIEW | CRITICAL | SUPPLIER / INSPECTION |
| DEF-07-02 | Pressure / Leak Test Report | Customer spec | Conditional | PDF | FOR_REVIEW | CRITICAL | INSPECTION |
| DEF-07-03 | Functional Test Report | Customer spec | Conditional | PDF | FOR_REVIEW | MAJOR | INSPECTION |

**Section 8 — Compliance Declarations**

| Line ID | Document Title | Standard/Spec | Default Required | Format | Review Code | Criticality | Data Source |
|---------|---------------|---------------|-----------------|--------|-------------|-------------|-------------|
| DEF-08-01 | Certificate of Conformance (CoC) | — | Yes | PDF/A | FOR_INFO | CRITICAL | INTERNAL_QA |
| DEF-08-02 | RoHS / REACH Declaration | EU directives | Conditional | PDF/A | FOR_INFO | STANDARD | INTERNAL_QA |
| DEF-08-03 | DFARS Specialty Metals Compliance | DFARS 252.225-7014 | Conditional | PDF/A | FOR_INFO | CRITICAL | INTERNAL_QA |
| DEF-08-04 | Packing List | — | Yes | PDF/A | FOR_INFO | STANDARD | INTERNAL_QA |

---

## 6. MRB Index Baseline Templates

### 6.1 Purpose of the MRB Index

The MRB Index is generated from the parsed SDRL (per PR-009 Section 6.6). It is NOT a fixed document — it is order-specific, derived from the customer's SDRL requirements. The baseline templates below define the **default structure** that the system populates; the QA Engineer then adjusts based on the specific SDRL.

### 6.2 Oil & Gas MRB Index Template

**Template ID:** `MRB-IDX-OG-001`

| Col | Field | Width | Description |
|-----|-------|-------|-------------|
| A | **Line Item** | 10 | MRB section + sequential (e.g., 3.1, 3.2, 5.1) |
| B | **MRB Section** | 5 | Section number (1-7) |
| C | **Document Title** | 40 | From SDRL parsing |
| D | **Standard / Spec** | 25 | Applicable standard |
| E | **Data Source** | 15 | CNC_INLINE, SUPPLIER, INSPECTION, etc. |
| F | **Responsible** | 15 | Role responsible for providing this document |
| G | **Format** | 10 | PDF, PDF/A, native |
| H | **Review Code** | 15 | FOR_INFO, FOR_REVIEW, FOR_APPROVAL |
| I | **Criticality** | 10 | CRITICAL, MAJOR, STANDARD |
| J | **Status** | 15 | PENDING → RECEIVED → VALIDATED → INCLUDED |
| K | **Received Date** | 12 | Date document was received |
| L | **Validated Date** | 12 | Date document passed validation |
| M | **Page Range** | 10 | Page numbers in final MRB PDF (added at assembly) |
| N | **Notes** | 30 | Free text |

**System behavior:**

- Columns A–I are populated automatically from SDRL parsing
- Column J is initialized as `PENDING` for all line items
- Columns K–M are populated as the order progresses
- The MRB Index is the **live tracking document** throughout the order lifecycle
- At MRB assembly (PR-012), the index is finalized and becomes the Master Document Index

### 6.3 Defence MRB Index Template

**Template ID:** `MRB-IDX-DEF-001`

Identical column structure to Oil & Gas (Section 6.2), with the following differences:

- MRB Section range: 1-8 (instead of 1-7)
- Additional column: **FAIR Ref** — links inspection line items to AS9102 Form 3 characteristic numbers (only populated when FAIR is required)
- Default line items are populated from SDRL-DEF-001 template

### 6.4 Index Lifecycle States

| State | Triggered By | Description |
|-------|-------------|-------------|
| **DRAFT** | MRB initialization (PR-009 §6.6) | Index generated from SDRL. All statuses PENDING. Subject to change until confirmed. |
| **LIVE** | First document received | Index is the active tracking document. Updated in real-time. |
| **FINAL** | MRB assembly start (PR-012) | Index locked. Page numbers assigned. Becomes the Master Document Index in the MRB. |

---

## 7. Customer Requirement Profile

### 7.1 Purpose

The Customer Requirement Profile (CRP) captures customer-specific acceptance criteria for materials, certificates, and documentation. It is used by the Material Gate (PR-008) to validate incoming material against the correct requirements, and by the validation engine (PR-010) to check document compliance.

One profile is created per customer. It may contain multiple material entries (one per material grade the customer orders).

### 7.2 Profile Structure

**Template ID:** `CRP-001`

#### 7.2.1 Customer Header

| Field | Type | Description |
|-------|------|-------------|
| `customer_id` | FK | Reference to customer record in ERP module |
| `customer_name` | VARCHAR | Company name |
| `industry` | ENUM | OIL_GAS, DEFENCE, MARITIME, STANDARD |
| `default_cert_type` | ENUM | EN_10204_2_1, EN_10204_2_2, EN_10204_3_1, EN_10204_3_2 |
| `requires_pmi` | BOOLEAN | Whether PMI is required by default |
| `requires_fair` | BOOLEAN | Whether FAIR is required (typically Defence) |
| `requires_itp` | BOOLEAN | Whether ITP is required (typically O&G) |
| `default_review_code` | ENUM | FOR_INFO, FOR_REVIEW, FOR_APPROVAL |
| `retention_years` | INTEGER | Customer-specific retention period (if longer than standard) |
| `special_instructions` | TEXT | Free text — customer-specific notes |
| `export_classification` | VARCHAR | ITAR/EAR/ECC classification if applicable |

#### 7.2.2 Material Requirement Entries

One entry per material grade per customer. These define the acceptance criteria the Material Gate (PR-008) checks against.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `material_grade` | VARCHAR | Material specification | ASTM A182 F316 |
| `cert_type_required` | ENUM | Minimum EN 10204 type | EN_10204_3_1 |
| `chemical_limits` | JSONB | Chemical composition acceptance ranges | See Section 7.3 |
| `mechanical_limits` | JSONB | Mechanical property acceptance ranges | See Section 7.4 |
| `hardness_limits` | JSONB | Hardness acceptance range | See Section 7.5 |
| `impact_test_required` | BOOLEAN | Whether Charpy impact test is required | true |
| `impact_test_temp_c` | NUMERIC | Impact test temperature | -46 |
| `impact_test_min_j` | NUMERIC | Minimum impact energy in Joules | 27 |
| `grain_size_required` | BOOLEAN | Whether grain size must be reported | true |
| `grain_size_min_astm` | NUMERIC | Minimum ASTM grain size number | 5 |
| `supplementary_tests` | JSONB | Additional tests beyond standard | See Section 7.6 |
| `norsok_mds_ref` | VARCHAR | NORSOK Material Data Sheet reference (if applicable) | MDS D45 |
| `pmi_required` | BOOLEAN | PMI required for this material | true |
| `pmi_method` | ENUM | XRF, OES, LABORATORY | XRF |
| `notes` | TEXT | Material-specific notes | "Customer requires 3.2 cert for pressure-containing applications" |

### 7.3 Chemical Composition Limits (JSONB structure)

```json
{
  "C":  { "min": null, "max": 0.030 },
  "Mn": { "min": null, "max": 2.00 },
  "P":  { "min": null, "max": 0.045 },
  "S":  { "min": null, "max": 0.030 },
  "Si": { "min": null, "max": 0.75 },
  "Cr": { "min": 16.00, "max": 18.00 },
  "Ni": { "min": 10.00, "max": 14.00 },
  "Mo": { "min": 2.00, "max": 3.00 },
  "N":  { "min": null, "max": 0.10 }
}
```

The Material Gate (PR-008) compares the chemical analysis on the EN 10204 certificate against these limits. Values outside the range trigger a REJECTED or REVIEW decision.

**Borderline rule (PR-010 §L4):** Any value within 5% of a limit boundary is flagged as "borderline" for additional review by the Quality Manager.

### 7.4 Mechanical Property Limits (JSONB structure)

```json
{
  "tensile_strength_mpa": { "min": 515, "max": null },
  "yield_strength_mpa":   { "min": 205, "max": null },
  "elongation_pct":       { "min": 30, "max": null },
  "reduction_of_area_pct": { "min": 50, "max": null }
}
```

### 7.5 Hardness Limits (JSONB structure)

```json
{
  "scale": "HBW",
  "min": null,
  "max": 217,
  "nace_mr0175_limit": true
}
```

When `nace_mr0175_limit` is true, NACE MR0175 / ISO 15156 hardness limits apply (critical for sour service applications in O&G).

### 7.6 Supplementary Tests (JSONB structure)

```json
[
  {
    "test": "intergranular_corrosion",
    "standard": "ASTM A262 Practice E",
    "required": true,
    "acceptance": "No intergranular attack"
  },
  {
    "test": "ferrite_content",
    "standard": "ASTM E562",
    "required": true,
    "acceptance": { "min_pct": 30, "max_pct": 70 }
  },
  {
    "test": "ultrasonic_testing",
    "standard": "ASTM A388",
    "required": true,
    "acceptance": "No indications exceeding reference standard"
  }
]
```

### 7.7 Profile Usage in System

| System Component | How Profile is Used |
|-----------------|---------------------|
| **Material Gate (PR-008)** | QA Engineer selects customer + material grade → system loads the Material Requirement Profile → 5-point certificate check runs against these limits |
| **SDRL Parser (PR-009)** | Customer profile determines default SDRL template (O&G or Defence) and pre-sets conditional line items (e.g., if `requires_itp = true`, ITP-related line items are automatically enabled) |
| **Validation Engine (PR-010)** | L4 compliance checks use chemical_limits, mechanical_limits, hardness_limits to validate document values against acceptance criteria |
| **CoC Generator (PR-011)** | Customer profile determines CoC template (Defence or O&G) and which conformance statements are included |

---

## 8. SDRL Parser Input Formats

### 8.1 Supported Input Methods

The SDRL parser must accept SDRL data in multiple formats, since customers do not use a standard format:

| Input Method | Description | Phase |
|-------------|-------------|-------|
| **Manual entry** | QA Engineer enters SDRL requirements line-by-line in the QA Workbench UI | Phase 0 |
| **Excel upload** | Customer provides SDRL as Excel/CSV → system parses columns into SDRL fields | Phase 0 |
| **PDF extraction** | Customer provides SDRL as PDF → system extracts table data (with QA review) | Phase 1 |
| **Customer portal submission** | Customer enters requirements directly in the portal using the SDRL template | Phase 2 |

### 8.2 Excel Upload Format

For Phase 0, the primary import path is Excel upload. The system expects:

| Column | Header | Maps To | Required |
|--------|--------|---------|----------|
| A | Line Item | `line_item_id` | Yes |
| B | Document Title | `doc_title` | Yes |
| C | Standard / Specification | `standard_ref` | No |
| D | Required (Y/N) | `is_required` | Yes |
| E | Format | `required_format` | Yes |
| F | Review Code | `review_code` | No (default: FOR_INFO) |
| G | Timing | `submission_timing` | No (default: WITH_SHIPMENT) |
| H | Notes | `notes` | No |

Columns not present in the upload are populated from the default SDRL template (Section 4 or 5) based on the industry classification. The QA Engineer reviews and confirms all populated fields before the SDRL is marked as parsed.

### 8.3 Validation on Import

The parser validates:

1. All required columns present
2. No duplicate line item IDs
3. Document titles match known document types in the Document Type Registry (AM-TS-001 Section 11.1) — unknown types are flagged for QA review
4. Standards references are valid (checked against a maintained standards list)
5. At least one CRITICAL line item exists (every SDRL must require at least one critical document)

---

## 9. Template Customization Rules

### 9.1 What Can Be Customized Per Order

| Aspect | Customizable? | By Whom | How |
|--------|--------------|---------|-----|
| Line items — add new | Yes | QA Engineer | Manual entry during SDRL parsing |
| Line items — remove | Yes | QA Engineer | Mark as NOT_APPLICABLE with justification |
| Line items — modify criticality | Yes | QA Engineer (Quality Manager approval for downgrade) | Edit during SDRL parsing |
| Review code — change | Yes | QA Engineer | Based on customer SDRL |
| Required format — change | Yes | QA Engineer | Based on customer SDRL |
| MRB section assignment — change | Yes (within industry template) | QA Engineer | Must stay within valid section range |
| Chemical / mechanical limits — change | Yes | Quality Manager only | Creates order-specific override of Customer Requirement Profile |
| New MRB section — add | No | — | MRB section structure is fixed per industry template |

### 9.2 What Cannot Be Customized

- MRB section structure (7 for O&G, 8 for Defence) — fixed per industry
- CoC as a required document — always required, cannot be removed
- Master Document Index — always required, cannot be removed
- Traceability Matrix — always required when material certificates are present
- Data source routing logic — system-enforced per AM-TS-001

---

## 10. Template Versioning

### 10.1 Version Control

- Templates are version-controlled in the database
- Each template has an effective date range (`valid_from`, `valid_until`)
- When a template is updated, the old version is retained — existing orders continue using the template version active when the order was created
- Template changes require Quality Manager approval
- Template version history is maintained for audit purposes

### 10.2 Customer Override History

- Customer Requirement Profiles are versioned
- When material limits change (e.g., customer tightens Cr range), a new version is created
- Orders reference the profile version active at order creation
- Profile changes do NOT retroactively affect in-progress orders

---

## 11. Records

| Form / Template | Template ID | Retention |
|-----------------|------------|-----------|
| Oil & Gas SDRL Template | SDRL-OG-001 | System configuration — permanent |
| Defence SDRL Template | SDRL-DEF-001 | System configuration — permanent |
| Oil & Gas MRB Index Template | MRB-IDX-OG-001 | System configuration — permanent |
| Defence MRB Index Template | MRB-IDX-DEF-001 | System configuration — permanent |
| Customer Requirement Profile | CRP-001 | Per customer — permanent (versioned) |
| Order-specific MRB Index (generated) | FM-009-04 | Per order archival requirement |
| Order Requirement Matrix (generated) | FM-009-01 | Per order archival requirement |

---

*This document defines the system's input layer. Changes to these templates affect all downstream processes (validation, CoC, MRB assembly). All template changes require Quality Manager approval and follow the document control process defined in PR-001.*

*Companion documents: PR-009 (SDRL Processing) · PR-008 (Material Gate) · PR-010 (Document Validation) · AM-TS-001 (IT/System Technical Specification) · AM-SDRL-2026-001 (Industry Requirements)*
