# FORM TEMPLATE SPECIFICATIONS — DIGITAL MRB BUILDER

| Field | Value |
|-------|-------|
| **Document No.** | AM-FM-001 |
| **Revision** | 1.1 |
| **Effective Date** | 2026-02-22 |
| **Approved By** | Technical Lead / Quality Manager |
| **Classification** | Internal — Engineering |
| **Status** | Draft — Post Founding Team Review |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-21 | Industry & Requirements Lead | Initial release. 24 form templates covering PR-008 through PR-013. Phase 0 critical forms (FM-008-01, FM-009-01, FM-009-04, FM-010-01) prioritized. |
| **1.1** | **2026-02-22** | **Industry & Requirements Lead** | **Post founding team review (Tore). 9 findings implemented: gate_decision ENUM renamed (APPROVED/REJECTED/CONDITIONAL_APPROVAL), CONDITIONAL added to gate_check_result, document_review_response ENUM added, MONITOR added to itp_point_type, default_notification_lead_hours added to FM-009-01, HOLD/MONITOR notifications extended, retention updated to 25yr O&G / 30yr Defence (min ≥20), custom MRB sections enabled, chemical JSONB updated with min+max ranges per EN 10204.** |

---

## 1. Purpose

This document defines the complete field-level specifications for all 24 quality forms (FM-xxx series) used by the Digital MRB Builder system. Each form template specifies:

- Every field the software must capture, display, and store
- Data types, validation rules, and character limits
- Auto-population logic (which fields populate from which database entities)
- Cross-form dependencies (how forms feed into each other)
- Workflow integration (which pipeline stage uses each form, and which state machine transitions it triggers)
- Explicit mapping to the database entities defined in AM-TS-001

**This document is the binding specification for the development team.** Together with AM-TS-001 (system architecture) and AM-CT-001 (customer-facing templates), it provides everything needed to build the MRB Builder application.

## 2. Scope

This specification covers 24 form templates across 6 quality procedures:

| Procedure | Forms | Pipeline Stage |
|-----------|-------|---------------|
| PR-008 — Incoming Material Review and Release | FM-008-01 to FM-008-04 (4) | Material Gate |
| PR-009 — SDRL Processing and MRB Management | FM-009-01 to FM-009-04 (4) | SDRL Intake → MRB Initialization |
| PR-010 — Document Validation and Verification | FM-010-01 to FM-010-04 (4) | Document Collection → Validation |
| PR-011 — Certificate of Conformance | FM-011-01 to FM-011-03 (3) | CoC Generation |
| PR-012 — MRB Assembly and Release | FM-012-01 to FM-012-04 (4) | MRB Assembly → Release |
| PR-013 — Document Archival and Retention | FM-013-01 to FM-013-05 (5) | Archive → Retention |
| **Total** | **24 forms** | **Full MRB lifecycle** |

### Phase 0 Critical Forms

The following 4 forms are required before Phase 0 software development can begin. They are marked with ★ throughout this document:

1. **FM-008-01** — Material Gate Review Checklist ★
2. **FM-009-01** — Order Requirement Matrix ★
3. **FM-009-04** — MRB Index (SDRL-derived) ★
4. **FM-010-01** — Correction Request ★

## 3. References

| Document | Relevance |
|----------|-----------|
| AM-TS-001 — IT/System Technical Specification | Database entities (§7), storage architecture (§14), security model (§8), state machine (§7.3) |
| AM-CT-001 — Customer-Facing Templates | SDRL templates (O&G + Defence), MRB Index baseline (14 columns), Customer Requirement Profile (JSONB structures) |
| PR-008 — Incoming Material Review and Release | Material Gate business rules, 5-point certificate check |
| PR-009 — SDRL Processing and MRB Management | SDRL parsing rules, MRB lifecycle, document routing |
| PR-010 — Document Validation and Verification | 5-layer validation, correction request process |
| PR-011 — Certificate of Conformance | CoC generation rules, signature authority |
| PR-012 — MRB Assembly and Release | Assembly prerequisites, 10-point quality check |
| PR-013 — Document Archival and Retention | Archive, retention periods, disposition |
| AM-IF-001 — ERP ↔ MRB Interface Specification | 20 interface data contracts (internal module boundaries) |

## 4. Definitions

| Term | Definition |
|------|-----------|
| **Form** | A structured data capture screen in the MRB Builder application. Each form maps to one or more database entities. |
| **Field** | A single data element within a form. Maps to a database column or computed value. |
| **Auto-population** | A field value that is automatically populated from a database entity when the form is opened or a trigger condition is met. Users may override auto-populated values unless marked read-only. |
| **Cross-form reference** | A dependency between two forms where one form's output serves as another form's input. |
| **Validation rule** | A constraint applied to a field value before the form can be saved. Validation failures block save and display an error message. |
| **ENUM** | A fixed set of allowed values for a field. All ENUMs are defined in Section 6 (Master ENUM Registry). |
| **Pipeline stage** | A named phase in the 7-stage MRB lifecycle: Material Gate → SDRL Intake → MRB Index → Document Collection → Validation → CoC → MRB Assembly → Archive. |
| **Read-only** | A field that is displayed but cannot be edited by the user. Populated by the system. |
| **Conditional** | A field that is required only when a specific condition is met (e.g., another field has a certain value). |

## 5. Form Design Conventions

### 5.1 Standard Field Types

All form fields use these data types, which map directly to PostgreSQL column types:

| Type | PostgreSQL | UI Widget | Example |
|------|-----------|-----------|---------|
| `UUID` | `UUID` | Hidden / read-only label | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| `VARCHAR(n)` | `VARCHAR(n)` | Text input with character counter | `AM-CR-2026-00001` (max 20 chars) |
| `TEXT` | `TEXT` | Multi-line textarea | Free-text description |
| `INTEGER` | `INTEGER` | Number input (no decimals) | Section number: `3` |
| `NUMERIC(p,s)` | `NUMERIC(p,s)` | Number input with decimal places | Chemical composition: `0.045` |
| `BOOLEAN` | `BOOLEAN` | Checkbox or toggle | PMI required: `true` |
| `DATE` | `DATE` | Date picker (ISO 8601) | `2026-03-15` |
| `TIMESTAMP` | `TIMESTAMP WITH TIME ZONE` | Read-only datetime (UTC) | `2026-03-15T14:32:00Z` |
| `ENUM(values)` | Custom PostgreSQL ENUM | Dropdown / radio buttons | `APPROVED / REJECTED / CONDITIONAL_APPROVAL` |
| `JSONB` | `JSONB` | Structured sub-form or table | Chemical limits object |
| `FK → entity` | `UUID REFERENCES entity(pk)` | Lookup / search-select | Customer selector |

### 5.2 Field Requirement Levels

| Level | Symbol | Meaning |
|-------|--------|---------|
| **Required** | `R` | Must be filled before form can be saved. |
| **Conditional** | `C` | Required when a stated condition is true. Condition noted in field description. |
| **Optional** | `O` | May be left blank. |
| **Auto** | `A` | System-generated. Read-only for the user. |
| **Auto-editable** | `AE` | System-populated but user may override. |

### 5.3 Naming Conventions

- **Form IDs:** `FM-[procedure]-[sequence]` — e.g., FM-008-01
- **Field IDs:** `[entity].[column_name]` — e.g., `gate_review.decision`
- **Validation Rule IDs:** `VR-[form]-[sequence]` — e.g., VR-008-01-001
- **CR Numbers:** `AM-CR-[YYYY]-[NNNNN]` — auto-generated, sequential, never reused
- **CoC Numbers:** `AM-COC-[YYYY]-[NNNNN]` — auto-generated, sequential, never reused

### 5.4 Timestamps and Checksums

- All timestamps are `TIMESTAMP WITH TIME ZONE`, stored in UTC, displayed in user's local timezone.
- All checksums are SHA-256, stored as `VARCHAR(64)`.
- All storage URIs follow the Supabase Storage bucket structure: `aurelian-mrb/{customer_id}/{order_id}/source|validated|mrb|coc/`

---

## 6. Master ENUM Registry

All ENUM types used across the 24 forms. Each ENUM is a PostgreSQL custom type. New values require a database migration.

### 6.1 Order and Classification ENUMs

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `industry_class` | `OIL_GAS`, `DEFENCE`, `MARITIME`, `STANDARD` | All forms via Order |
| `order_state` | `NEW`, `SDRL_RECEIVED`, `SDRL_PARSED`, `MRB_INITIALIZED`, `COLLECTING`, `VALIDATING`, `COC_PENDING`, `COC_SIGNED`, `MRB_ASSEMBLY`, `MRB_RELEASED`, `SHIPPED`, `ARCHIVED` | FM-009-03, state machine |
| `mrb_index_state` | `DRAFT`, `LIVE`, `FINAL` | FM-009-04 |

### 6.2 Material and Certificate ENUMs

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `cert_type` | `EN_10204_2_1`, `EN_10204_2_2`, `EN_10204_3_1`, `EN_10204_3_2` | FM-008-01, FM-008-04 |
| `gate_decision` | `APPROVED`, `REJECTED`, `CONDITIONAL_APPROVAL` | FM-008-01, FM-012-02, FM-012-03 |
| `gate_check_result` | `PASS`, `FAIL`, `CONDITIONAL`, `BORDERLINE`, `N_A` | FM-008-01 |
| `pmi_method` | `XRF`, `OES`, `LABORATORY` | FM-008-02, FM-008-04 |

### 6.3 SDRL and Document ENUMs

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `required_format` | `PDF`, `PDF_A`, `NATIVE`, `SIGNED` | FM-009-01, FM-009-04 |
| `review_code` | `FOR_INFO`, `FOR_REVIEW`, `FOR_APPROVAL` | FM-009-01, FM-009-04 |
| `criticality` | `CRITICAL`, `MAJOR`, `STANDARD` | FM-009-01, FM-009-04, FM-010-01 |
| `data_source` | `CNC_INLINE`, `METROLOGY`, `INSPECTION`, `SUPPLIER`, `SPECIAL_PROCESS`, `INTERNAL_QA`, `CUSTOMER` | FM-009-01, FM-009-04 |
| `submission_timing` | `WITH_SHIPMENT`, `BEFORE_SHIPMENT`, `AT_MILESTONE`, `ON_REQUEST` | FM-009-01, FM-009-04 |
| `sdrl_parse_method` | `MANUAL`, `EXCEL_UPLOAD`, `PDF_EXTRACT`, `PORTAL` | FM-009-01 |
| `itp_point_type` | `HOLD`, `WITNESS`, `REVIEW`, `MONITOR`, `SURVEILLANCE` | FM-009-02 |
| `document_review_response` | `APPROVED`, `APPROVED_WITH_COMMENTS`, `CONDITIONAL_APPROVAL`, `REJECTED`, `REVISE_AND_RESUBMIT` | FM-012-03 |

### 6.4 Validation and Correction ENUMs

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `validation_status` | `PENDING`, `RECEIVED`, `VALIDATING`, `VALIDATED`, `REJECTED`, `CORRECTED`, `WAIVED`, `NOT_APPLICABLE` | FM-009-04, FM-010-02 |
| `validation_layer` | `L1_EXISTENCE`, `L2_FORMAT`, `L3_COMPLETENESS`, `L4_COMPLIANCE`, `L5_TRACEABILITY` | FM-010-01, FM-010-02 |
| `validation_result` | `PASS`, `FAIL`, `WAIVED` | FM-010-02 |
| `failure_code` | `MISSING`, `FORMAT_ERROR`, `INCOMPLETE`, `NON_COMPLIANT`, `TRACEABILITY_BREAK` | FM-010-01 |
| `cr_status` | `OPEN`, `IN_PROGRESS`, `RESOLVED`, `ESCALATED`, `WAIVED` | FM-010-01 |
| `responsible_role` | `QA_ENGINEER`, `PURCHASING`, `PRODUCTION`, `CUSTOMER`, `SUPPLIER` | FM-010-01 |

### 6.5 CoC and Signature ENUMs

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `signature_method` | `INTERNAL_PKI`, `BANKID`, `MANUAL` | FM-011-01, FM-011-03 |
| `coc_status` | `ACTIVE`, `SUPERSEDED`, `VOID` | FM-011-01, FM-011-02 |
| `authority_level` | `LEVEL_1`, `LEVEL_2`, `LEVEL_3` | FM-011-03 |
| `coc_template_type` | `OIL_GAS_STANDARD`, `DEFENCE_STANDARD`, `DEFENCE_AQAP`, `CUSTOM` | FM-011-01 |

### 6.6 Archive ENUMs

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `archive_tier` | `ACTIVE`, `DEEP` | FM-013-01 |
| `disposition_method` | `SECURE_DELETE`, `CRYPTO_SHRED` | FM-013-04 |
| `integrity_check_result` | `MATCH`, `MISMATCH`, `UNREADABLE` | FM-013-05 |

### 6.7 Delivery ENUMs

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `delivery_method` | `PHYSICAL`, `ELECTRONIC`, `BOTH` | FM-012-04 |
| `release_type` | `STANDARD`, `ELEVATED` | FM-012-02 |

---

## 7. Cross-Form Dependency Map

The 24 forms follow the MRB pipeline. Arrows show data flow direction (output → input):

```
FM-008-04 (Material Req Profile) ─────┐
                                      ▼
FM-009-01 (Order Req Matrix) ───► FM-008-01 (Material Gate) ───► FM-008-02 (Physical Insp)
    │                                 │                              │
    │                                 └──► FM-008-03 (Traceability)  │
    ▼                                                                │
FM-009-03 (MRB Init) ──► FM-009-04 (MRB Index) ◄────────────────────┘
    │                        │
    ▼                        ▼
FM-009-02 (ITP) [O&G]   FM-010-02 (Validation Log)
                             │
                             ├──► FM-010-01 (Correction Req) [on failure]
                             │
                             ▼
                         FM-010-03 (Traceability Verif)
                             │
                             ▼
                         FM-010-04 (CoC Prereq Gate)
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
              FM-011-01 (CoC Reg)  FM-011-03 (Signatory Reg)
                    │
                    ├──► FM-011-02 (CoC Rev/Void)
                    ▼
              FM-012-01 (Assembly Checklist)
                    │
                    ▼
              FM-012-02 (Quality Check)
                    │
                    ├──► FM-012-03 (Customer Approval)
                    ▼
              FM-012-04 (Delivery Confirm)
                    │
                    ▼
              FM-013-01 (Archive Register)
                    │
                    ├──► FM-013-02 (Access Log)
                    ├──► FM-013-03 (Disposition Req) ──► FM-013-04 (Disposition Rec)
                    └──► FM-013-05 (Annual Integrity)
```

### Dependency Rules

1. A form cannot be opened until its upstream dependencies have valid data.
2. Bidirectional references: if Form A depends on Form B, Form B's cross-references list Form A as a downstream consumer.
3. FM-009-04 (MRB Index) is the central hub — it receives from FM-009-01 and feeds all validation, CoC, and assembly forms.

---

## 8. PR-008 Forms — Incoming Material Review and Release

### 8.1 FM-008-01: Material Gate Review Checklist ★ Phase 0

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-008-01 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-008 — Incoming Material Review and Release |
| **Industry** | BOTH (Oil & Gas and Defence) |
| **Pipeline Stage** | Material Gate |
| **DB Entity** | `mrb.gate_review` (primary), `mrb.material_receipt` (linked) |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Records the results of the 5-point certificate verification check (PR-008, Section 6.3) for each material lot received against a specific order. One gate review record is created per material-receipt/order combination, because the same material lot may be evaluated against different customer requirement profiles for different orders (PR-008, Section 6.6).

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Gate Review ID | `gate_review.review_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Receipt Reference | `gate_review.receipt_id` | FK → `material_receipt` | R | — | Links to the goods receiving record. Lookup selector filtered by pending receipts. |
| 3 | Order Reference | `gate_review.order_id` | FK → `order` | R | — | Which order this material is being reviewed for. Required because same material may serve multiple orders. |
| 4 | Material Grade | `material_receipt.material_grade` | VARCHAR(100) | A | 100 | Auto-populated from receipt. Read-only. E.g., "ASTM A182 F316". |
| 5 | Heat Number | `material_receipt.heat_number` | VARCHAR(50) | A | 50 | Auto-populated from receipt. Read-only. |
| 6 | Supplier | `supplier.name` | VARCHAR(200) | A | 200 | Auto-populated via receipt → supplier. Read-only. |
| 7 | Customer | `customer.name` | VARCHAR(200) | A | 200 | Auto-populated via order → customer. Read-only. |
| 8 | Industry | `order.industry_class` | ENUM(`industry_class`) | A | — | Auto-populated from order. Read-only. |
| 9 | Profile Used | `gate_review.profile_id` | FK → `material_requirement_profile` | R | — | Which customer-specific material requirement profile is applied. Dropdown filtered by customer + material grade. |
| 10 | Certificate URI | `material_receipt.cert_uri` | VARCHAR(500) | R | 500 | Storage path to the uploaded material certificate (Supabase Storage). Viewer opens inline. |
| 11 | **Check 1: Certificate Type** | `gate_review.check_cert_type` | ENUM(`gate_check_result`) | R | — | PASS if certificate type meets or exceeds required type. FAIL if wrong type. |
| 12 | Required Cert Type | (from profile) | ENUM(`cert_type`) | A | — | Auto-populated from requirement profile. Read-only. |
| 13 | Actual Cert Type | `gate_review.cert_type_actual` | ENUM(`cert_type`) | R | — | QA Engineer selects the certificate type found on the actual document. |
| 14 | **Check 2: Chemical Composition** | `gate_review.check_chemical` | ENUM(`gate_check_result`) | R | — | PASS / FAIL / BORDERLINE. Borderline = within 5% of specification limit. |
| 15 | Chemical Results | `gate_review.chemical_results` | JSONB | R | — | Per-element comparison with min and max ranges: `{ "C": {"actual": 0.042, "min": null, "max": 0.045, "result": "PASS"}, "Cr": {"actual": 17.2, "min": 16.0, "max": 18.0, "result": "PASS"}, "Ni": {"actual": 10.5, "min": 10.0, "max": 14.0, "result": "PASS"}, ... }`. Must contain entries for every element in the profile's `chemical_limits`. Min and max values sourced from the material requirement profile — EN 10204 certificates typically specify ranges (e.g., Cr: 16.0–18.0%). |
| 16 | **Check 3: Mechanical Properties** | `gate_review.check_mechanical` | ENUM(`gate_check_result`) | R | — | PASS / FAIL / BORDERLINE per property. |
| 17 | Mechanical Results | `gate_review.mechanical_results` | JSONB | R | — | Per-property comparison: `{ "tensile_strength": {"actual": 520, "min": 485, "max": 620, "unit": "MPa", "result": "PASS"}, ... }`. Must match profile's `mechanical_limits`. |
| 18 | **Check 4: Supplementary Tests** | `gate_review.check_supplementary` | ENUM(`gate_check_result`) | R | — | PASS / FAIL / N_A. N_A if no supplementary tests required by profile. |
| 19 | Supplementary Results | `gate_review.supplementary_results` | JSONB | C | — | Required if Check 4 is not N_A. Array: `[{"test": "Impact -46C", "standard": "ASTM A370", "actual": "45J avg", "required": "27J min", "result": "PASS"}]`. |
| 20 | **Check 5: Traceability & Integrity** | `gate_review.check_traceability` | ENUM(`gate_check_result`) | R | — | PASS / FAIL / FLAG. FLAG = suspicious pattern (e.g., identical values across heats, improbable results). |
| 21 | Traceability Notes | `gate_review.traceability_notes` | TEXT | C | 2000 | Required if Check 5 is FAIL or FLAG. Description of traceability gaps or integrity concerns. |
| 22 | Borderline Flags | `gate_review.borderline_flags` | JSONB | A | — | Auto-calculated. Array of elements/properties within 5% of limit. `[{"field": "C", "actual": 0.043, "limit": 0.045, "margin_pct": 4.4}]`. |
| 23 | Integrity Red Flags | `gate_review.integrity_flags` | JSONB | O | — | QA Engineer records suspected anomalies. `[{"flag": "Identical Mn values across 3 heats", "severity": "HIGH"}]`. |
| 24 | Physical Inspection Required | `gate_review.physical_inspection_required` | BOOLEAN | R | — | True = triggers FM-008-02 (Physical Inspection). Mandatory for CRITICAL materials and when Check 5 = FLAG. |
| 25 | **Gate Decision** | `gate_review.decision` | ENUM(`gate_decision`) | R | — | APPROVED / REJECTED / CONDITIONAL_APPROVAL. Final decision for this material-order combination. CONDITIONAL_APPROVAL = material may proceed with documented conditions (auto-creates Correction Request with conditions). |
| 26 | Decision Reason | `gate_review.decision_reason` | TEXT | R | 2000 | Free text justification. Required for all decisions. |
| 27 | Reviewer | `gate_review.reviewer_id` | FK → `auth.users` | A | — | Authenticated user. Read-only. |
| 28 | Review Date | `gate_review.reviewed_at` | TIMESTAMP | A | — | System timestamp at form submission. Read-only. |
| 29 | QM Override Required | `gate_review.qm_override` | BOOLEAN | R | — | QA Engineer can escalate to Quality Manager by setting this to true. When true, gate review appears in QM queue. Default: false. |
| 30 | QM Decision | `gate_review.qm_decision` | ENUM(`gate_decision`) | C | — | Required when `qm_override` = true. Quality Manager selects APPROVED, REJECTED, or CONDITIONAL_APPROVAL. |
| 31 | QM Decision Reason | `gate_review.qm_decision_reason` | TEXT | C | 2000 | Required when `qm_override` = true. |
| 32 | QM Reviewer | `gate_review.qm_reviewer_id` | FK → `auth.users` | C | — | Auto-populated when QM submits decision. Must have Quality Manager role. |
| 33 | QM Review Date | `gate_review.qm_reviewed_at` | TIMESTAMP | C | — | System timestamp when QM submits. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-008-01-001 | Check 1–5 | Completeness | All five checks must have a value before `decision` can be set. | "All five gate checks must be completed before making a gate decision." |
| VR-008-01-002 | decision | Business logic | If any Check = FAIL, `decision` cannot be APPROVED. | "Material with a FAIL check cannot be approved. Decision must be REJECTED or CONDITIONAL_APPROVAL (with documented conditions)." |
| VR-008-01-003 | chemical_results | Structural | Must contain an entry for every element in the profile's `chemical_limits` JSONB. | "Chemical results missing for element: {element}." |
| VR-008-01-004 | mechanical_results | Structural | Must contain an entry for every property in the profile's `mechanical_limits` JSONB. | "Mechanical results missing for property: {property}." |
| VR-008-01-005 | supplementary_results | Conditional | Required when `check_supplementary` is not N_A. | "Supplementary test results required when supplementary check is not N/A." |
| VR-008-01-006 | traceability_notes | Conditional | Required when `check_traceability` is FAIL or FLAG. | "Traceability notes required when check is FAIL or FLAG." |
| VR-008-01-007 | qm_decision | Conditional | Required when `qm_override` = true. | "Quality Manager decision required for escalated materials." |
| VR-008-01-008 | qm_decision | Constraint | Must be APPROVED, REJECTED, or CONDITIONAL_APPROVAL. | "Quality Manager must make a final decision (APPROVED, REJECTED, or CONDITIONAL_APPROVAL)." |
| VR-008-01-009 | physical_inspection_required | Business logic | Auto-set to true when `criticality` = CRITICAL (from order's SDRL line items for material docs) or when `check_traceability` = FLAG. | "Physical inspection is mandatory for critical materials and flagged integrity concerns." |
| VR-008-01-010 | borderline_flags | Auto-calculation | System auto-calculates after chemical and mechanical results are entered. Any value within 5% of its specification limit is flagged. | (System-generated, no user error.) |
| VR-008-01-011 | cert_type_actual vs required | Cross-check | `cert_type_actual` must meet or exceed `cert_type_required` (3.2 > 3.1 > 2.2 > 2.1) for Check 1 to be PASS. | "Certificate type {actual} does not meet the required type {required}." |

#### Auto-Population Specifications

| Field | Source Entity | Source Column | Trigger | Condition |
|-------|-------------|---------------|---------|-----------|
| Material Grade | `mrb.material_receipt` | `material_grade` | On `receipt_id` selection | Always |
| Heat Number | `mrb.material_receipt` | `heat_number` | On `receipt_id` selection | Always |
| Supplier | `erp.supplier` | `name` | Via `material_receipt.supplier_id` | Always |
| Customer | `erp.customer` | `name` | Via `order.customer_id` | Always |
| Industry | `mrb.order` | `industry_class` | Via `order_id` | Always |
| Required Cert Type | `mrb.material_requirement_profile` | `cert_type_required` | On `profile_id` selection | Always |
| Borderline Flags | (calculated) | — | After chemical/mechanical results saved | When any value within 5% of limit |
| Reviewer | `auth.users` | Current session user | On form open | Always |
| Review Date | System | `NOW()` | On form submit | Always |
| QM Override | (user-set) | — | On decision save | When QA Engineer escalates to Quality Manager |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-008-04 (Material Requirement Profile) | Provides the requirement profile (`chemical_limits`, `mechanical_limits`, `supplementary_tests`) against which the certificate is checked. |
| **IN** ← | FM-009-01 (Order Requirement Matrix) | Provides the order context and industry classification. Material gate only opens for orders that have been through SDRL parsing. |
| **OUT** → | FM-008-02 (Physical Inspection Report) | When `physical_inspection_required` = true, triggers creation of FM-008-02 for this receipt. |
| **OUT** → | FM-008-03 (Material Traceability Matrix) | Gate decision (APPROVED or CONDITIONAL_APPROVAL) feeds the traceability matrix for this material-order combination. |
| **OUT** → | FM-009-04 (MRB Index) | Gate decision updates MRB Index document status for material certificate line items (e.g., Section 3.1 "Material Test Certificate" → VALIDATED when APPROVED). |
| **OUT** → | FM-010-01 (Correction Request) | Gate decision REJECTED may trigger a correction request to the supplier for a replacement certificate. |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | Material Gate (PR-008) |
| **Triggered by** | Goods receipt notification (IF-003). QA Engineer opens the form from the pending material queue. |
| **Order state requirement** | Order must be in state `MRB_INITIALIZED` or later. |
| **On APPROVED** | Updates `material_receipt.gate_decision` to APPROVED. Triggers IF-005 (Material Gate Decision → ERP). Pre-stages certificate as validated document in MRB Section 3. |
| **On REJECTED** | Updates `material_receipt.gate_decision` to REJECTED. Triggers IF-005. May trigger FM-010-01 (Correction Request to supplier). Material blocked from production use. |
| **On CONDITIONAL_APPROVAL** | Updates `material_receipt.gate_decision` to CONDITIONAL_APPROVAL. Material may proceed to production. Auto-creates Correction Request (FM-010-01) documenting the conditions that must be resolved. Conditions tracked until closure. |
| **On QM escalation** | When `qm_override` = true: gate review appears in Quality Manager queue. Form remains open pending QM decision. No state change until QM decides. |

#### Industry Applicability

| Field / Feature | Oil & Gas | Defence |
|----------------|-----------|---------|
| All 33 fields | ✓ | ✓ |
| Supplementary tests (Check 4) | Typically includes impact testing, hardness per NORSOK M-650 | May include additional tests per customer spec (NADCAP, AMS) |
| PMI triggering (Check 5 FLAG → FM-008-02) | Mandatory for pressure-containing per NORSOK Z-CR-006 | Per customer contract |
| Certificate hierarchy (3.2 > 3.1) | Standard EN 10204 | Standard EN 10204 |

---

### 8.2 FM-008-02: Incoming Physical Inspection Report

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-008-02 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-008 — Incoming Material Review and Release |
| **Industry** | BOTH |
| **Pipeline Stage** | Material Gate |
| **DB Entity** | `mrb.physical_inspection` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Documents PMI (Positive Material Identification), visual, and dimensional inspection results when triggered by the Material Gate Review (FM-008-01). PMI is mandatory for pressure-containing materials in Oil & Gas (NORSOK Z-CR-006) and when integrity red flags are raised (Check 5 = FLAG). Physical inspection confirms that the actual material matches the certificate claims.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Inspection ID | `physical_inspection.inspection_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Gate Review Reference | `physical_inspection.gate_review_id` | FK → `gate_review` | R | — | Links to FM-008-01 that triggered this inspection. |
| 3 | Material Receipt Reference | `physical_inspection.receipt_id` | FK → `material_receipt` | A | — | Auto-populated via gate review. Read-only. |
| 4 | Order Reference | `physical_inspection.order_id` | FK → `order` | A | — | Auto-populated. Read-only. |
| 5 | Material Grade | (from receipt) | VARCHAR(100) | A | 100 | Auto-populated. Read-only. |
| 6 | Heat Number | (from receipt) | VARCHAR(50) | A | 50 | Auto-populated. Read-only. |
| 7 | Inspection Date | `physical_inspection.inspected_at` | DATE | R | — | Date physical inspection was performed. |
| 8 | **PMI Performed** | `physical_inspection.pmi_performed` | BOOLEAN | R | — | Enables PMI section. Mandatory if `gate_review.check_traceability` = FLAG or `profile.pmi_required` = true. |
| 9 | PMI Method | `physical_inspection.pmi_method` | ENUM(`pmi_method`) | C | — | XRF / OES / LABORATORY. Required when `pmi_performed` = true. |
| 10 | PMI Instrument Serial | `physical_inspection.pmi_instrument_serial` | VARCHAR(100) | C | 100 | Instrument identification. Required when `pmi_performed` = true. |
| 11 | PMI Calibration Expiry | `physical_inspection.pmi_calibration_expiry` | DATE | C | — | Required when `pmi_performed` = true. Must be >= inspection date. |
| 12 | PMI Test Location | `physical_inspection.pmi_location_desc` | TEXT | C | 1000 | Required when `pmi_performed` = true. E.g., "Top surface, 50mm from corner". |
| 13 | PMI Element Results | `physical_inspection.pmi_results` | JSONB | C | — | Required when `pmi_performed` = true. Per-element: `{"Cr": {"actual": 17.2, "cert_value": 17.0, "variance": 0.2, "within_tolerance": true}}`. Tolerance: ±1.0% absolute for major elements (Cr, Ni, Mo). |
| 14 | PMI Correlation Status | (calculated) | ENUM (PASS / FAIL) | A | — | Auto-calculated. FAIL if variance exceeds tolerance for any major element. |
| 15 | **Visual Inspection Performed** | `physical_inspection.visual_performed` | BOOLEAN | R | — | Always required. |
| 16 | Visual Defects Observed | `physical_inspection.visual_defects` | BOOLEAN | R | — | True if any defects found. |
| 17 | Visual Defect Description | `physical_inspection.visual_defects_desc` | TEXT | C | 1000 | Required when `visual_defects` = true. |
| 18 | Corrosion Status | `physical_inspection.corrosion_status` | ENUM (NONE / LIGHT / MODERATE / HEAVY) | R | — | Surface corrosion assessment. |
| 19 | Contamination Observed | `physical_inspection.contamination` | BOOLEAN | R | — | Foreign material, oils, or debris present. |
| 20 | Material Marking Present | `physical_inspection.marking_present` | BOOLEAN | R | — | Is heat number/grade stamped or painted on material? Must match certificate. |
| 21 | Marking Details | `physical_inspection.marking_details` | TEXT | O | 500 | What marking is visible and where. |
| 22 | **Dimensional Inspection Performed** | `physical_inspection.dimensional_performed` | BOOLEAN | R | — | Whether dimensional sampling was conducted. |
| 23 | Dimension Spec Reference | `physical_inspection.dimension_spec_ref` | VARCHAR(100) | C | 100 | PO or drawing reference. Required when `dimensional_performed` = true. |
| 24 | Dimension Results | `physical_inspection.dimension_results` | JSONB | C | — | Required when `dimensional_performed` = true. `{"diameter": {"measured": 25.05, "min": 24.95, "max": 25.05, "unit": "mm", "result": "PASS"}}`. |
| 25 | Dimensional Pass/Fail | (calculated) | ENUM (PASS / FAIL) | A | — | Auto-calculated. PASS only if all dimensions within tolerance. |
| 26 | **Overall Inspection Result** | `physical_inspection.overall_result` | ENUM (PASS / FAIL) | R | — | PASS = visual clean, dimensions OK, PMI correlates (if done). FAIL = any aspect fails. |
| 27 | Inspected By | `physical_inspection.inspected_by` | FK → `auth.users` | R | — | QA Engineer or technician who performed inspection. |
| 28 | Notes | `physical_inspection.notes` | TEXT | O | 2000 | Free text observations. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-008-02-001 | PMI fields (9–14) | Conditional | All PMI fields required when `pmi_performed` = true. | "PMI fields are required when PMI is performed." |
| VR-008-02-002 | pmi_calibration_expiry | Range | Must be >= `inspected_at`. | "PMI instrument calibration has expired. Inspection invalid." |
| VR-008-02-003 | PMI correlation | Business logic | If PMI variance exceeds tolerance for any major element → material quarantined, gate decision changes to REJECTED. | "PMI correlation failed for {element}. Material quarantined." |
| VR-008-02-004 | visual_defects_desc | Conditional | Required when `visual_defects` = true. | "Defect description required when defects are observed." |
| VR-008-02-005 | dimension_results | Conditional | Required when `dimensional_performed` = true. | "Dimension measurements required when dimensional inspection is performed." |
| VR-008-02-006 | overall_result | Consistency | Cannot be PASS if PMI failed, visual defects critical, or dimensional FAIL. | "Overall result cannot be PASS with failing sub-inspections." |

#### Auto-Population Specifications

| Field | Source Entity | Source Column | Trigger | Condition |
|-------|-------------|---------------|---------|-----------|
| Material Receipt | `mrb.gate_review` | `receipt_id` | On `gate_review_id` selection | Always |
| Order | `mrb.gate_review` | `order_id` | On `gate_review_id` selection | Always |
| Material Grade | `mrb.material_receipt` | `material_grade` | Via receipt | Always |
| Heat Number | `mrb.material_receipt` | `heat_number` | Via receipt | Always |
| PMI Correlation Status | (calculated) | — | After PMI results entered | When `pmi_performed` = true |
| Dimensional Pass/Fail | (calculated) | — | After dimension results entered | When `dimensional_performed` = true |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-008-01 (Material Gate Checklist) | Triggered when `physical_inspection_required` = true. Gate review context provides order and material info. |
| **OUT** → | FM-008-01 (Material Gate Checklist) | PMI mismatch auto-fails Check 5, triggering gate decision change to REJECTED. |
| **OUT** → | FM-008-03 (Material Traceability Matrix) | Inspection results (especially PMI) feed into the traceability record. |
| **OUT** → | FM-009-04 (MRB Index) | Physical inspection report is itself a deliverable document in MRB Section 3 (PMI Report line item). |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | Material Gate (PR-008, Section 6.4) |
| **Triggered by** | FM-008-01 gate review setting `physical_inspection_required` = true. |
| **On PASS** | Inspection report stored as validated document. Gate review proceeds (or remains as-is if already decided). |
| **On FAIL** | Gate review decision overridden to REJECTED if PMI correlation fails. Material quarantined. |

#### Industry Applicability

| Feature | Oil & Gas | Defence |
|---------|-----------|---------|
| PMI mandatory | Pressure-containing per NORSOK Z-CR-006 | Per customer contract |
| PMI method | Typically XRF (field portable) | Per specification (may require OES for carbon-critical alloys) |
| Visual standards | API, NORSOK | AS9100, customer IPC/workmanship |
| Dimensional sampling | Per PO/drawing requirements | Per engineering drawing + AS9102 FAIR requirements |

---

### 8.3 FM-008-03: Material Traceability Matrix

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-008-03 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-008 — Incoming Material Review and Release |
| **Industry** | BOTH |
| **Pipeline Stage** | Material Gate → Production |
| **DB Entity** | `mrb.material_traceability` (header) + `mrb.material_traceability_detail` (allocations) |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Records the linkage between material heat numbers, supplier certificates, production orders, and part serial numbers. Enables forward traceability (heat number → which parts?) and reverse traceability (part serial → which heat?). Critical for rapid containment if a material non-conformance is discovered post-release. One traceability header per material lot, with multiple allocation lines (one per order using that material).

#### Field Definitions — Header

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Traceability ID | `material_traceability.trace_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Material Receipt | `material_traceability.receipt_id` | FK → `material_receipt` | R | — | Links to the goods receiving record. Only receipts with `gate_decision` = APPROVED or CONDITIONAL_APPROVAL are available. |
| 3 | Heat Number | (from receipt) | VARCHAR(50) | A | 50 | Auto-populated. Read-only. |
| 4 | Material Grade | (from receipt) | VARCHAR(100) | A | 100 | Auto-populated. Read-only. |
| 5 | Supplier | (from receipt → supplier) | VARCHAR(200) | A | 200 | Auto-populated. Read-only. |
| 6 | Certificate Type | (from gate review) | ENUM(`cert_type`) | A | — | EN 10204 type. Auto-populated. Read-only. |
| 7 | Gate Decision | (from FM-008-01) | ENUM(`gate_decision`) | A | — | Should be APPROVED or CONDITIONAL_APPROVAL. Read-only. |
| 8 | Gate Reviewed By | (from FM-008-01) | FK → `auth.users` | A | — | Auto-populated. Read-only. |
| 9 | Gate Review Date | (from FM-008-01) | DATE | A | — | Auto-populated. Read-only. |
| 10 | Physical Inspection Done | `material_traceability.physical_inspection_done` | BOOLEAN | A | — | Whether FM-008-02 was completed for this receipt. Auto-populated. |
| 11 | PMI Summary | (from FM-008-02) | VARCHAR(100) | A | 100 | "PASS" or "FAIL — {reason}". Auto-populated. Read-only. |
| 12 | Total Quantity Received | `material_traceability.qty_received` | NUMERIC(12,2) | A | — | Auto-populated from receipt. Read-only. |
| 13 | Unit of Measure | `material_traceability.uom` | VARCHAR(20) | A | 20 | kg, m, pcs, etc. Auto-populated. Read-only. |
| 14 | Storage Location | `material_traceability.storage_location` | VARCHAR(100) | O | 100 | Warehouse bin, shelf, area. Optional. |
| 15 | Created By | `material_traceability.created_by` | FK → `auth.users` | A | — | Auto-populated. Read-only. |
| 16 | Created At | `material_traceability.created_at` | TIMESTAMP | A | — | Auto-populated. Read-only. |
| 17 | Notes | `material_traceability.notes` | TEXT | O | 2000 | Free text. |

#### Field Definitions — Allocation Line Items (repeating)

Each row represents one order's allocation of this material lot:

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 18 | Detail ID | `material_traceability_detail.detail_id` | UUID | A | — | Primary key. Auto-generated. |
| 19 | Order Reference | `material_traceability_detail.order_id` | FK → `order` | R | — | Which order uses this material. |
| 20 | PO Number | (from order) | VARCHAR(50) | A | 50 | Auto-populated. Read-only. |
| 21 | Customer | (from order → customer) | VARCHAR(200) | A | 200 | Auto-populated. Read-only. |
| 22 | Quantity Allocated | `material_traceability_detail.qty_allocated` | NUMERIC(12,2) | R | — | How much of the heat used for this order. |
| 23 | First Serial Number | `material_traceability_detail.serial_first` | VARCHAR(50) | R | 50 | Lowest serial number of parts made from this lot. |
| 24 | Last Serial Number | `material_traceability_detail.serial_last` | VARCHAR(50) | R | 50 | Highest serial number. Enables range traceability. |
| 25 | Part Count | (calculated) | INTEGER | A | — | Auto-calculated from serial range. Read-only. |
| 26 | Production Status | `material_traceability_detail.prod_status` | ENUM (IN_PROCESS / COMPLETED / SHIPPED / RETAINED) | AE | — | Auto-updated from order lifecycle. Editable for corrections. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-008-03-001 | (line items) | Completeness | At least one allocation line item must exist. | "Traceability matrix must have at least one order allocation." |
| VR-008-03-002 | qty_allocated (sum) | Range | Sum of `qty_allocated` across all line items must not exceed `qty_received`. | "Total allocated quantity ({sum}) exceeds received quantity ({received})." |
| VR-008-03-003 | serial_last vs serial_first | Order | `serial_last` must be >= `serial_first` (when numerically comparable). | "Last serial number must be >= first serial number." |
| VR-008-03-004 | (order_id, receipt_id) | Uniqueness | No duplicate allocations for the same material-order combination. | "Material already allocated to this order. Update existing allocation instead." |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-008-01 (Material Gate Checklist) | Only created when gate decision = APPROVED or CONDITIONAL_APPROVAL. Gate review fields auto-populate header. |
| **IN** ← | FM-008-02 (Physical Inspection) | PMI summary auto-populates if inspection was performed. |
| **OUT** → | FM-010-03 (Traceability Verification) | Traceability verification queries this matrix to confirm the complete chain: PO → material cert → goods receiving → traceability → production → inspection → CoC. |
| **OUT** → | FM-009-04 (MRB Index) | Traceability matrix is a required document in MRB Section 3. |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | Material Gate → Production handoff |
| **Triggered by** | Auto-created when gate decision = APPROVED or CONDITIONAL_APPROVAL in FM-008-01. Header fields auto-populated. |
| **Allocation timing** | Line items added when material is allocated to specific production orders (may be at material release or later during production planning). |
| **Updates** | `prod_status` auto-updates as order progresses through manufacturing. |

---

### 8.4 FM-008-04: Material Requirement Profile

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-008-04 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-008 — Incoming Material Review and Release |
| **Industry** | BOTH |
| **Pipeline Stage** | Pre-order (profile library) — used at Material Gate |
| **DB Entity** | `mrb.material_requirement_profile` |
| **Retention** | Life of profile + 5 years after last use |

#### Purpose

Captures customer-specific acceptance criteria for a specific material grade. One profile per customer-material combination. Used by FM-008-01 to evaluate incoming material certificates. Profiles are reusable across orders — once established for a customer-material pair, the same profile applies to all orders requiring that material. JSONB structures match AM-CT-001 Sections 7.3–7.6 exactly.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Profile ID | `material_requirement_profile.profile_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Profile Number | `material_requirement_profile.profile_number` | VARCHAR(30) | A | 30 | Auto-generated: `MRP-[YYYY]-[NNNNN]`. Sequential, never reused. |
| 3 | Customer | `material_requirement_profile.customer_id` | FK → `erp.customer` | R | — | Which customer. Lookup from customer master. |
| 4 | Material Grade | `material_requirement_profile.material_grade` | VARCHAR(100) | R | 100 | E.g., "ASTM A182 F316L", "EN 10269 35CrMo". |
| 5 | Material Specification | `material_requirement_profile.material_specification` | VARCHAR(200) | R | 200 | Governing standard: ASTM, EN, NORSOK, AMS, etc. |
| 6 | Industry | `material_requirement_profile.industry` | ENUM(`industry_class`) | AE | — | Auto-set from customer profile. Editable. |
| 7 | Certificate Type Required | `material_requirement_profile.cert_type_required` | ENUM(`cert_type`) | R | — | Minimum acceptable EN 10204 type. |
| 8 | Status | `material_requirement_profile.status` | ENUM (ACTIVE / INACTIVE / SUPERSEDED) | R | — | ACTIVE = current and usable. |
| 9 | Version | `material_requirement_profile.version_num` | INTEGER | A | — | Auto-incremented on update. History retained. |
| 10 | Effective Date | `material_requirement_profile.effective_date` | DATE | A | — | Auto-set to current date on activation. |
| 11 | Superseded By | `material_requirement_profile.superseded_by_id` | FK → `material_requirement_profile` | C | — | Links to newer version when SUPERSEDED. |
| 12 | **Chemical Limits** | `material_requirement_profile.chemical_limits` | JSONB | R | — | Per-element min/max: `{"C": {"min": null, "max": 0.030}, "Cr": {"min": 16.00, "max": 18.00}, ...}`. Must contain all elements relevant to the material grade. |
| 13 | **Mechanical Limits** | `material_requirement_profile.mechanical_limits` | JSONB | R | — | Per-property: `{"tensile_strength_mpa": {"min": 515, "max": null}, "yield_strength_mpa": {"min": 205, "max": null}, "elongation_pct": {"min": 30, "max": null}}`. |
| 14 | **Hardness Limits** | `material_requirement_profile.hardness_limits` | JSONB | R | — | `{"scale": "HBW", "min": null, "max": 217, "nace_mr0175_limit": true}`. When `nace_mr0175_limit` = true, NACE MR0175/ISO 15156 limits apply (sour service O&G). |
| 15 | Impact Test Required | `material_requirement_profile.impact_test_required` | BOOLEAN | R | — | Whether Charpy impact test is mandatory. |
| 16 | Impact Test Temperature | `material_requirement_profile.impact_test_temp_c` | NUMERIC(5,1) | C | — | Required if `impact_test_required` = true. Degrees Celsius (e.g., -46). |
| 17 | Impact Test Min Energy | `material_requirement_profile.impact_test_min_j` | NUMERIC(6,2) | C | — | Required if `impact_test_required` = true. Minimum Joules. |
| 18 | Grain Size Required | `material_requirement_profile.grain_size_required` | BOOLEAN | R | — | Must certificate report grain size? |
| 19 | Grain Size Min ASTM | `material_requirement_profile.grain_size_min_astm` | NUMERIC(4,1) | C | — | Required if `grain_size_required` = true. ASTM number >= this value. |
| 20 | **Supplementary Tests** | `material_requirement_profile.supplementary_tests` | JSONB | O | — | Array: `[{"test": "intergranular_corrosion", "standard": "ASTM A262 Practice E", "required": true, "acceptance": "No intergranular attack"}]`. |
| 21 | NORSOK MDS Reference | `material_requirement_profile.norsok_mds_ref` | VARCHAR(50) | O | 50 | NORSOK Material Data Sheet (O&G). E.g., "MDS D45". |
| 22 | PMI Required | `material_requirement_profile.pmi_required` | BOOLEAN | R | — | Positive Material Identification mandatory? |
| 23 | PMI Method | `material_requirement_profile.pmi_method` | ENUM(`pmi_method`) | C | — | Required if `pmi_required` = true. |
| 24 | Approved Suppliers | `material_requirement_profile.approved_suppliers` | JSONB | O | — | If set, restricts acceptable suppliers: `[{"supplier_id": "...", "supplier_name": "ArcelorMittal"}]`. |
| 25 | Created By | `material_requirement_profile.created_by` | FK → `auth.users` | A | — | Auto-populated. Read-only. |
| 26 | Created At | `material_requirement_profile.created_at` | TIMESTAMP | A | — | Auto-populated. Read-only. |
| 27 | Approved By | `material_requirement_profile.approved_by` | FK → `auth.users` | R | — | Quality Manager approval required before profile is ACTIVE. |
| 28 | Approved At | `material_requirement_profile.approved_at` | TIMESTAMP | C | — | Auto-populated when QM approves. |
| 29 | Notes | `material_requirement_profile.notes` | TEXT | O | 2000 | Customer-specific instructions. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-008-04-001 | status | Prerequisite | Cannot be ACTIVE until `approved_by` is set. | "Profile requires Quality Manager approval before activation." |
| VR-008-04-002 | chemical_limits | Structural | Must contain at least one element entry. | "Chemical limits must specify at least one element." |
| VR-008-04-003 | mechanical_limits | Structural | Must contain at least one property entry. | "Mechanical limits must specify at least one property." |
| VR-008-04-004 | impact_test_temp_c | Conditional | Required when `impact_test_required` = true. | "Impact test temperature required when impact testing is mandatory." |
| VR-008-04-005 | pmi_method | Conditional | Required when `pmi_required` = true. | "PMI method required when PMI is mandatory." |
| VR-008-04-006 | (on update) | Versioning | Profile updates create a new version. Old version marked SUPERSEDED with `superseded_by_id` pointing to new version. Orders referencing the old version retain that reference. | (System action.) |
| VR-008-04-007 | (customer_id, material_grade) | Uniqueness | Only one ACTIVE profile per customer-material combination. | "An active profile already exists for this customer-material combination." |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **OUT** → | FM-008-01 (Material Gate Checklist) | Provides the acceptance criteria (`chemical_limits`, `mechanical_limits`, `hardness_limits`, `supplementary_tests`) for every gate review. |
| **IN** ← | (Customer SDRL / PO) | Initial requirements extracted from customer purchase order or SDRL. |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | Pre-order (profile library). Profiles are created once and reused. |
| **Triggered by** | QA Engineer creates profile when a new customer-material combination is encountered. May also be created during SDRL parsing (FM-009-01) when new material requirements are identified. |
| **Activation** | Profile requires Quality Manager approval before status = ACTIVE. |
| **Versioning** | Updates create new version; old version SUPERSEDED. In-flight orders retain the profile version they started with. |

#### Industry Applicability

| Feature | Oil & Gas | Defence |
|---------|-----------|---------|
| NORSOK MDS Reference | Commonly used (MDS D45, D50, etc.) | Not applicable |
| PMI requirement | Mandatory for pressure-containing per NORSOK Z-CR-006 | Per customer specification |
| Impact test temperature | Typically -46°C for North Sea applications | Per customer / AMS specification |
| Supplementary tests | Intergranular corrosion (ASTM A262), ferrite content | Per NADCAP, AMS, customer spec |
| NACE MR0175 hardness limits | Common for sour service applications | Rare |

---

## 9. PR-009 Forms — SDRL Processing and MRB Management

### 9.1 FM-009-01: Order Requirement Matrix ★ Phase 0

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-009-01 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-009 — SDRL Processing and MRB Management |
| **Industry** | BOTH |
| **Pipeline Stage** | SDRL Intake |
| **DB Entity** | `mrb.sdrl` (header) + `mrb.sdrl_line_item` (line items) |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Captures all parsed SDRL requirements for an order. This is the structured representation of the customer's Supplier Document Requirement List — the "recipe" that defines which documents must be delivered with the manufactured product. Each line item becomes a tracked requirement in the MRB Index.

The form consists of a header section (SDRL-level metadata) and a line item table (one row per document requirement, stored as individual rows in `mrb.sdrl_line_item` per decision R8).

#### Field Definitions — Header

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | SDRL ID | `sdrl.sdrl_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Order Reference | `sdrl.order_id` | FK → `order` | R | — | Which order this SDRL belongs to. Lookup from open orders in state NEW or SDRL_RECEIVED. |
| 3 | PO Number | `order.po_number` | VARCHAR(50) | A | 50 | Auto-populated from order. Read-only. |
| 4 | Customer | `customer.name` | VARCHAR(200) | A | 200 | Auto-populated via order → customer. Read-only. |
| 5 | Industry Classification | `sdrl.industry_class` | ENUM(`industry_class`) | AE | — | Auto-populated from order. Determines section structure (7 sections for O&G, 8 for Defence). Editable if order has no prior classification. |
| 6 | SDRL Source File | `sdrl.raw_file_uri` | VARCHAR(500) | O | 500 | Storage URI of the uploaded original SDRL document (PDF/Excel). Optional if SDRL is entered manually. |
| 7 | Parse Method | `sdrl.parse_method` | ENUM(`sdrl_parse_method`) | R | — | How the SDRL was input: MANUAL entry, EXCEL_UPLOAD (structured import), PDF_EXTRACT (parsed from PDF), or PORTAL (customer submitted via portal). |
| 8 | Template Used | `sdrl.template_id` | VARCHAR(20) | AE | 20 | SDRL template ID from AM-CT-001 (e.g., SDRL-OG-001, SDRL-DEF-001). Auto-set based on industry_class. |
| 9 | Total Line Items | `sdrl.section_count` | INTEGER | A | — | Auto-calculated count of line items. Read-only. |
| 10 | FAIR Required | (derived) | BOOLEAN | A | — | Auto-calculated: true if any line item has doc_title containing "First Article" or line_item_id = DEF-06-01. |
| 11 | ITP Required | (derived) | BOOLEAN | A | — | Auto-calculated: true if any line item relates to ITP (line_item_id = OG-05-01 or doc_title contains "Inspection Test Plan"). |
| 12 | Parsed By | `sdrl.parsed_by` | FK → `auth.users` | A | — | Authenticated user. Read-only. |
| 13 | Parsed At | `sdrl.parsed_at` | TIMESTAMP | A | — | System timestamp on form submission. Read-only. |
| 14 | **Default Notification Lead Time (hrs)** | `sdrl.default_notification_lead_hours` | INTEGER | C | — | Order-level default for ITP point notification lead times. Required when `itp_required` = true. Pre-populates `itp_point.notification_lead_hours` for WITNESS and MONITOR points. Typical range: 48–72 hours. Period defined in PO/contract, varies per order. |

#### Field Definitions — Line Items (repeating table)

Each row is stored as one record in `mrb.sdrl_line_item`:

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 14 | Line ID | `sdrl_line_item.line_id` | UUID | A | — | Primary key per line item. Auto-generated. |
| 15 | SDRL ID (parent) | `sdrl_line_item.sdrl_id` | FK → `sdrl` | A | — | Links to parent SDRL. Auto-set. |
| 16 | Line Item ID | `sdrl_line_item.line_item_id` | VARCHAR(20) | R | 20 | Human-readable identifier. Format: `[OG\|DEF]-[section]-[sequence]` (e.g., OG-03-01, DEF-06-01). Auto-populated from template, editable for custom additions. |
| 17 | MRB Section | `sdrl_line_item.mrb_section` | INTEGER | R | — | Section number within the MRB (1–7 for O&G, 1–8 for Defence). |
| 18 | Document Title | `sdrl_line_item.doc_title` | VARCHAR(255) | R | 255 | What the document is. E.g., "Material Test Certificate (EN 10204 Type 3.1)". |
| 19 | Standard / Specification | `sdrl_line_item.standard_ref` | VARCHAR(255) | O | 255 | Applicable standard. E.g., "EN 10204", "ASME V", "NORSOK M-650". |
| 20 | Required Format | `sdrl_line_item.required_format` | ENUM(`required_format`) | R | — | PDF, PDF_A, NATIVE, or SIGNED. |
| 21 | Review Code | `sdrl_line_item.review_code` | ENUM(`review_code`) | R | — | FOR_INFO, FOR_REVIEW, or FOR_APPROVAL. Determines customer review level. |
| 22 | Criticality | `sdrl_line_item.criticality` | ENUM(`criticality`) | R | — | CRITICAL, MAJOR, or STANDARD. Affects validation stringency and escalation rules. |
| 23 | Data Source | `sdrl_line_item.data_source` | ENUM(`data_source`) | R | — | Where the document originates. Determines routing: CNC_INLINE (auto-generated), SUPPLIER (external), INSPECTION (QA team), etc. |
| 24 | Is Required | `sdrl_line_item.is_required` | BOOLEAN | R | — | True = mandatory for MRB completeness. False = optional/conditional. |
| 25 | Submission Timing | `sdrl_line_item.submission_timing` | ENUM(`submission_timing`) | R | — | When the document must be delivered: WITH_SHIPMENT, BEFORE_SHIPMENT, AT_MILESTONE, ON_REQUEST. |
| 26 | Notes | `sdrl_line_item.notes` | TEXT | O | 1000 | Free text for customer-specific instructions or clarifications. |
| 27 | Manually Added | `sdrl_line_item.manually_added` | BOOLEAN | A | — | True if QA Engineer added this line item manually (not from template). Auto-set. |
| 28 | Modified From Default | `sdrl_line_item.modified_from_default` | BOOLEAN | A | — | True if any field value differs from the template default. Auto-calculated on save. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-009-01-001 | line_item_id | Uniqueness | No duplicate `line_item_id` values within the same SDRL. | "Duplicate line item ID: {id}. Each line item must have a unique identifier." |
| VR-009-01-002 | mrb_section | Range | Must be 1–7 for OIL_GAS (standard), 1–8 for DEFENCE (standard). Sections above the standard range are permitted as custom sections when `mrb.section_count` has been extended. | "MRB section {n} is out of range for {industry_class} orders (standard: 1–{max}). Extend section count in MRB Initialization if custom sections are needed." |
| VR-009-01-003 | (all line items) | Completeness | At least one line item with `criticality` = CRITICAL must exist. | "Every SDRL must contain at least one CRITICAL line item." |
| VR-009-01-004 | (all line items) | Completeness | At least one line item must exist. | "SDRL must contain at least one line item." |
| VR-009-01-005 | doc_title | Known document | Unknown document titles (not matching the Document Type Registry) are flagged with a warning (not blocked). | Warning: "Document title '{title}' is not in the standard document type registry. Verify this is correct." |
| VR-009-01-006 | industry_class + line items | Consistency | If `industry_class` = OIL_GAS and ITP-related line items are present, FM-009-02 (ITP Tracker) becomes mandatory for this order. | Info: "ITP line items detected. ITP Tracker (FM-009-02) will be required for this order." |
| VR-009-01-007 | order.order_state | Prerequisite | Order must be in state NEW or SDRL_RECEIVED. | "SDRL can only be parsed for orders in state NEW or SDRL_RECEIVED." |

#### Auto-Population Specifications

| Field | Source Entity | Source Column | Trigger | Condition |
|-------|-------------|---------------|---------|-----------|
| PO Number | `mrb.order` | `po_number` | On `order_id` selection | Always |
| Customer | `erp.customer` | `name` | Via `order.customer_id` | Always |
| Industry Classification | `mrb.order` | `industry_class` | On `order_id` selection | When order has classification |
| Template line items | AM-CT-001 templates | All line item fields | On template selection | When `parse_method` = MANUAL and template selected |
| FAIR Required | (derived from line items) | — | On save | When qualifying line items exist |
| ITP Required | (derived from line items) | — | On save | When qualifying line items exist |
| Total Line Items | (count) | — | On save | Always |
| Parsed By | `auth.users` | Current session | On form open | Always |
| Parsed At | System | `NOW()` | On form submit | Always |
| Manually Added | (calculated) | — | On line item add | When line not from template |
| Modified From Default | (calculated) | — | On save | When field value differs from template |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | (External SDRL document) | Customer's SDRL is the source. Uploaded as `raw_file_uri` or entered manually. |
| **OUT** → | FM-009-03 (MRB Initialization Record) | SDRL parsing triggers MRB initialization. Line items define the MRB section structure. |
| **OUT** → | FM-009-04 (MRB Index) | Line items become the MRB Index rows. 1:1 mapping from `sdrl_line_item` to MRB Index entries. |
| **OUT** → | FM-009-02 (ITP Tracker) | When ITP-related line items are detected and `industry_class` = OIL_GAS, ITP Tracker is initialized. |
| **OUT** → | FM-008-01 (Material Gate Checklist) | Order context and industry classification feed into material gate reviews for this order. |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | SDRL Intake (PR-009, Section 6.2) |
| **Triggered by** | QA Engineer opens form from the order queue when a new SDRL is received from the customer. |
| **Order state requirement** | Order must be in state `NEW` or `SDRL_RECEIVED`. |
| **On submit** | Order state transitions: `NEW` or `SDRL_RECEIVED` → `SDRL_PARSED`. SDRL line items are committed to database. MRB initialization is triggered (FM-009-03). |
| **IF-008 update** | Triggers IF-008 (Order State Update) to notify ERP module that SDRL has been parsed. |

#### Industry Applicability

| Feature | Oil & Gas | Defence |
|---------|-----------|---------|
| Section structure | 7 sections per AM-CT-001 §4.2 | 8 sections per AM-CT-001 §5.2 |
| ITP detection | Yes — triggers FM-009-02 | No |
| FAIR detection | No (typically) | Yes — triggers AS9102 workflow |
| Default template | SDRL-OG-001 (30 line items) | SDRL-DEF-001 (25 line items) |
| Standard references | NORSOK, API, EN 10204 | AS9100, AQAP, NADCAP |

---

### 9.2 FM-009-02: ITP Tracker (Oil & Gas Only)

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-009-02 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-009 — SDRL Processing and MRB Management |
| **Industry** | OIL_GAS only |
| **Pipeline Stage** | SDRL Intake → Production (lives through manufacturing) |
| **DB Entity** | `mrb.itp_tracker` (header) + `mrb.itp_point` (line items) |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Tracks Inspection Test Plan (ITP) Hold, Witness, and Review points for Oil & Gas orders. HOLD points stop production until signed off. WITNESS points require customer notification and attendance. REVIEW points require documented approval before proceeding. The ITP is a contractual requirement linking manufacturing activities to specific inspection events with defined acceptance criteria.

#### Field Definitions — Header

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | ITP Tracker ID | `itp_tracker.tracker_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Order Reference | `itp_tracker.order_id` | FK → `order` | R | — | Must be OIL_GAS industry class. |
| 3 | PO Number | (from order) | VARCHAR(50) | A | 50 | Auto-populated. Read-only. |
| 4 | Customer | (from order → customer) | VARCHAR(200) | A | 200 | Auto-populated. Read-only. |
| 5 | ITP Document URI | `itp_tracker.itp_document_uri` | VARCHAR(500) | R | 500 | Storage path to uploaded ITP PDF. |
| 6 | Total ITP Points | (count) | INTEGER | A | — | Auto-calculated. Read-only. |
| 7 | Created By | `itp_tracker.created_by` | FK → `auth.users` | A | — | Auto-populated. Read-only. |
| 8 | Created At | `itp_tracker.created_at` | TIMESTAMP | A | — | Auto-populated. Read-only. |

#### Field Definitions — ITP Points (repeating table)

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 9 | Point ID | `itp_point.point_id` | UUID | A | — | Primary key. Auto-generated. |
| 10 | Item Number | `itp_point.item_number` | INTEGER | R | — | Sequential from ITP document. Unique per order. |
| 11 | Activity Description | `itp_point.activity_description` | TEXT | R | 1000 | What is being inspected. E.g., "Welding of main seam per WPS-001". |
| 12 | **Point Type** | `itp_point.point_type` | ENUM(`itp_point_type`) | R | — | HOLD (stops production), WITNESS (customer observer required), REVIEW (documented approval), MONITOR (customer has right to attend but not binding — standard O&G ITP point), SURVEILLANCE (supplier's own observations recorded). |
| 13 | Responsible Party | `itp_point.responsible_party` | ENUM (AURELIAN / CUSTOMER / THIRD_PARTY) | R | — | Who conducts the inspection. |
| 14 | Acceptance Criteria | `itp_point.acceptance_criteria` | TEXT | R | 2000 | What constitutes pass. E.g., "Weld per ASME V, no cracks > 2mm". |
| 15 | Reference Document | `itp_point.reference_doc` | VARCHAR(200) | O | 200 | Standard/spec/drawing reference. |
| 16 | Notification Lead Time (hrs) | `itp_point.notification_lead_hours` | INTEGER | C | — | Required for HOLD, WITNESS, and MONITOR points. Minimum 24 hours. Typical: 48–72 hours. Pre-populated from `sdrl.default_notification_lead_hours` when set. |
| 17 | **Point Status** | `itp_point.status` | ENUM (NOT_STARTED / SCHEDULED / IN_PROGRESS / HOLD_ACTIVE / SIGNED_OFF / CLOSED) | A | — | Auto-managed. Read-only for users. |
| 18 | Scheduled Date | `itp_point.scheduled_date` | DATE | O | — | Estimated date point will be reached. Auto-filled from production schedule; editable. |
| 19 | Actual Start Date | `itp_point.actual_start_date` | DATE | C | — | When inspection activity began. Set when status = IN_PROGRESS. |
| 20 | Sign-Off Date | `itp_point.sign_off_date` | DATE | C | — | When point approved. For HOLD points, blocks production until set. |
| 21 | Sign-Off Person Name | `itp_point.signoff_by_name` | VARCHAR(200) | C | 200 | Required when status = SIGNED_OFF. |
| 22 | Sign-Off Person Role | `itp_point.signoff_by_role` | VARCHAR(100) | C | 100 | E.g., "Equinor Inspector", "Quality Manager". |
| 23 | Witness Notification Sent | `itp_point.witness_notified` | BOOLEAN | A | — | Auto-set when notification email sent. Read-only. |
| 24 | Witness Notification Date | `itp_point.witness_notification_date` | TIMESTAMP | A | — | Auto-populated when notification sent. |
| 25 | Witness Attendee Name | `itp_point.witness_attendee_name` | VARCHAR(200) | C | 200 | Required when WITNESS point is reached. |
| 26 | Notes | `itp_point.notes` | TEXT | O | 2000 | Free text per ITP point. |

#### ITP Point Status Machine

```
NOT_STARTED → SCHEDULED (production plan reaches activity date)
            → IN_PROGRESS (inspection begins)
            → HOLD_ACTIVE (HOLD points only — production blocked)
            → SIGNED_OFF (approval documented, production may continue)
            → CLOSED (final document collected and validated)
```

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-009-02-001 | notification_lead_hours | Range | Must be >= 24 for HOLD, WITNESS, and MONITOR points. | "Notification lead time must be at least 24 hours for HOLD, WITNESS, and MONITOR points." |
| VR-009-02-002 | (HOLD points) | Business logic | Production cannot proceed past `scheduled_date` until `sign_off_date` is populated. | "HOLD point {item_number} must be signed off before production can continue." |
| VR-009-02-003 | signoff_by_name | Conditional | Required when status = SIGNED_OFF. | "Sign-off person name required." |
| VR-009-02-004 | acceptance_criteria | Completeness | Required for all HOLD and WITNESS points. | "Acceptance criteria required for HOLD and WITNESS points." |
| VR-009-02-005 | (HOLD/WITNESS/MONITOR) | Automation | When status → SCHEDULED and scheduled_date within notification_lead_hours, system auto-sends notification email to customer contact. Applies to HOLD, WITNESS, and MONITOR points. | (System action.) |
| VR-009-02-006 | (overdue HOLD) | Escalation | If `actual_start_date` exceeds `scheduled_date` by 5+ days without sign-off, escalation alert to Quality Manager. | Alert: "HOLD point {item_number} overdue by {n} days." |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-009-01 (Order Requirement Matrix) | ITP Tracker initialized when SDRL contains ITP-related line items. |
| **OUT** → | FM-009-04 (MRB Index) | ITP sign-off records are MRB Section 5 deliverables (OG-05-08 "ITP Hold/Witness/Review Point Sign-off Records"). |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | SDRL Intake through Production completion. Lives across manufacturing lifecycle. |
| **Triggered by** | FM-009-01 detecting ITP line items in the SDRL (OG-05-01). |
| **HOLD point enforcement** | Production order scheduling system respects HOLD points. Cannot advance past a HOLD without sign-off. |
| **HOLD/WITNESS/MONITOR notification** | Automatic email to customer contact when HOLD, WITNESS, or MONITOR point approaches within notification lead time window. |

---

### 9.3 FM-009-03: MRB Initialization Record

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-009-03 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-009 — SDRL Processing and MRB Management |
| **Industry** | BOTH |
| **Pipeline Stage** | SDRL Intake → MRB Initialization |
| **DB Entity** | `mrb.mrb` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Documents the creation and structural setup of a new Manufacturing Record Book instance. Establishes the MRB section structure based on the parsed SDRL, identifies the order classification (O&G or Defence), and determines which optional components (FAIR, ITP) are required. This form triggers generation of the MRB Index (FM-009-04) in DRAFT state.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | MRB ID | `mrb.mrb_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | MRB Number | `mrb.mrb_number` | VARCHAR(30) | A | 30 | Auto-generated: `AM-MRB-[YYYY]-[NNNNN]`. Sequential, never reused. |
| 3 | Order Reference | `mrb.order_id` | FK → `order` | R | — | Links to order. One MRB per order. |
| 4 | SDRL Reference | (from order) | FK → `sdrl` | A | — | Auto-populated from order. Must have been parsed (FM-009-01 complete). |
| 5 | PO Number | (from order) | VARCHAR(50) | A | 50 | Auto-populated. Read-only. |
| 6 | Customer | (from order → customer) | VARCHAR(200) | A | 200 | Auto-populated. Read-only. |
| 7 | Industry Classification | `mrb.industry_class` | ENUM(`industry_class`) | A | — | Auto-populated from SDRL. Read-only. Determines section structure. |
| 8 | Section Count | `mrb.section_count` | INTEGER | AE | — | Default: 7 for OIL_GAS, 8 for DEFENCE. Auto-set from industry_class. Editable by QA Engineer to add custom sections beyond the standard structure when customer requirements do not fit standard MRB sections. |
| 9 | MRB State | `mrb.mrb_state` | ENUM (initialized value) | A | — | Set to MRB_INITIALIZED on creation. Read-only. |
| 10 | FAIR Required | `mrb.fair_required` | BOOLEAN | A | — | Auto-derived from SDRL line items (FM-009-01). True if FAIR line items present. |
| 11 | ITP Required | `mrb.itp_required` | BOOLEAN | A | — | Auto-derived from SDRL. True if ITP line items present (O&G only). |
| 12 | Total Document Slots | `mrb.total_doc_slots` | INTEGER | A | — | Count of SDRL line items that become document slots in the MRB. Auto-calculated. |
| 13 | Initialized By | `mrb.initialized_by` | FK → `auth.users` | A | — | Auto-populated. Read-only. |
| 14 | Initialized At | `mrb.initialized_at` | TIMESTAMP | A | — | System timestamp. Read-only. |
| 15 | Notes | `mrb.init_notes` | TEXT | O | 2000 | Any special instructions for this MRB. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-009-03-001 | order.order_state | Prerequisite | Order must be in state SDRL_PARSED. | "MRB can only be initialized after SDRL is parsed." |
| VR-009-03-002 | (order_id) | Uniqueness | One MRB per order. No duplicate MRBs for the same order. | "An MRB already exists for this order." |
| VR-009-03-003 | (SDRL line items) | Structural | SDRL must have at least one required line item (`is_required` = true). | "Cannot initialize MRB: SDRL has no required document line items." |

#### Auto-Population Specifications

| Field | Source | Trigger | Condition |
|-------|--------|---------|-----------|
| All order/customer fields | `mrb.order` → `erp.customer` | On form creation | Always |
| Industry Classification | `mrb.sdrl` | Via order → SDRL | Always |
| Section Count | (derived from industry_class) | On creation | 7 for OIL_GAS, 8 for DEFENCE |
| FAIR Required | FM-009-01 line items | (derived) | When FAIR line items present |
| ITP Required | FM-009-01 line items | (derived) | When ITP line items present |
| Total Document Slots | Count of `sdrl_line_item` where `is_required` = true | On creation | Always |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-009-01 (Order Requirement Matrix) | SDRL parsing completion triggers MRB initialization. |
| **OUT** → | FM-009-04 (MRB Index) | MRB initialization creates the MRB Index in DRAFT state. Document slots created from SDRL line items. |
| **OUT** → | FM-009-02 (ITP Tracker) | If `itp_required` = true, ITP Tracker is also initialized. |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | MRB Initialization (PR-009, Section 6.3) |
| **Triggered by** | Automatic after FM-009-01 (SDRL parsing) is submitted. Can also be manually triggered by QA Engineer. |
| **On submit** | Order state transitions: `SDRL_PARSED` → `MRB_INITIALIZED`. MRB record created. MRB Index (FM-009-04) generated in DRAFT state. Document slots created for each required SDRL line item. IF-008 triggered (Order State Update). |

---

### 9.4 FM-009-04: MRB Index (SDRL-Derived) ★ Phase 0

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-009-04 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-009 — SDRL Processing and MRB Management |
| **Industry** | BOTH |
| **Pipeline Stage** | MRB Index (lives across the full pipeline — from initialization to assembly) |
| **DB Entity** | Materialized view joining `mrb.sdrl_line_item` + `mrb.mrb_document` + `mrb.validation` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. Final version embedded in MRB PDF/A-3. |

#### Purpose

The MRB Index is the master tracking document for each order. It is generated from the SDRL (FM-009-01) and tracks the status of every required document from PENDING through VALIDATED to INCLUDED in the final MRB. This is NOT a static form — it is a live dashboard view that evolves through the order lifecycle.

**Key design principle:** The MRB Index is a database view, not a separate table. It joins `sdrl_line_item` (static requirements from the SDRL) with `mrb_document` (dynamic document collection/validation state) and `validation` (layer results). This eliminates data duplication and ensures the index is always current.

#### MRB Index Lifecycle States

| State | Description | Editable Fields |
|-------|-------------|----------------|
| **DRAFT** | Generated from SDRL. All document statuses = PENDING. No documents received yet. | Line items can be added/modified/removed (with audit trail). |
| **LIVE** | First document received. Updated in real-time as documents are collected and validated. | Status, dates, and references update automatically. Line items locked (amendment requires formal change). |
| **FINAL** | MRB assembly begins. Page numbers assigned. Index locked for PDF generation. | Only page range fields editable. All other fields frozen. |

#### Field Definitions — Index Columns (per AM-CT-001, Section 6.2)

Each row in the MRB Index corresponds to one `sdrl_line_item` enriched with document collection status:

| # | Field | DB Source | Type | Phase | Description |
|---|-------|-----------|------|-------|-------------|
| 1 | Line Item | `sdrl_line_item.line_item_id` mapped to MRB notation | VARCHAR(10) | DRAFT | Section.sequential notation (e.g., 3.1, 3.2, 5.3). |
| 2 | MRB Section | `sdrl_line_item.mrb_section` | INTEGER | DRAFT | Section number (1–7 or 1–8). |
| 3 | Document Title | `sdrl_line_item.doc_title` | VARCHAR(255) | DRAFT | From SDRL parsing. |
| 4 | Standard / Spec | `sdrl_line_item.standard_ref` | VARCHAR(255) | DRAFT | Applicable specification. |
| 5 | Data Source | `sdrl_line_item.data_source` | ENUM(`data_source`) | DRAFT | Routing: CNC_INLINE, SUPPLIER, INSPECTION, etc. |
| 6 | Responsible | (derived from `data_source`) | VARCHAR(100) | DRAFT | Role responsible for delivering this document. Auto-derived from data_source routing table (PR-009, Section 6.3). |
| 7 | Format | `sdrl_line_item.required_format` | ENUM(`required_format`) | DRAFT | Required document format. |
| 8 | Review Code | `sdrl_line_item.review_code` | ENUM(`review_code`) | DRAFT | Customer review level. |
| 9 | Criticality | `sdrl_line_item.criticality` | ENUM(`criticality`) | DRAFT | Validation stringency. |
| 10 | **Status** | `mrb_document.validation_status` | ENUM(`validation_status`) | LIVE | Updated as documents are received and validated. Progression: PENDING → RECEIVED → VALIDATING → VALIDATED. |
| 11 | **Received Date** | `mrb_document.uploaded_at` | DATE | LIVE | Auto-populated when document is uploaded to this slot. |
| 12 | **Validated Date** | `validation.validated_at` (latest PASS across all layers) | DATE | LIVE | Auto-populated when document passes all applicable validation layers. |
| 13 | **Document Reference** | `mrb_document.artifact_uri` | VARCHAR(500) | LIVE | Supabase Storage path to the document file. Click to view. |
| 14 | **Page Range** | `mrb_document.page_range` | VARCHAR(20) | FINAL | Assigned during MRB assembly. E.g., "45–52". |
| 15 | Notes | `sdrl_line_item.notes` | TEXT | ALL | Free text. Editable in DRAFT and LIVE, frozen in FINAL. |

#### Additional Columns — Defence Orders Only

| # | Field | DB Source | Type | Description |
|---|-------|-----------|------|-------------|
| 16 | FAIR Reference | `mrb_document.fair_ref` | VARCHAR(50) | Links to AS9102 Form 3 characteristic numbers. Only shown when `industry_class` = DEFENCE and FAIR is required. |

#### Data Source → Responsible Routing Table

This mapping auto-populates the "Responsible" column based on data_source:

| Data Source | Default Responsible | Description |
|-------------|-------------------|-------------|
| `CNC_INLINE` | Production / CNC Operator | Auto-generated from CNC machine (dimensional reports, process sheets). |
| `METROLOGY` | QA Engineer / Metrology Lab | CMM reports, measurement data. |
| `INSPECTION` | QA Engineer | Visual inspection, hardness testing, dimensional verification. |
| `SUPPLIER` | Purchasing / Supplier | Material certificates, external test reports. Delivered via supplier or purchasing. |
| `SPECIAL_PROCESS` | QA Engineer / External Lab | NDT, heat treatment, surface treatment certificates. Often from NADCAP-approved external labs. |
| `INTERNAL_QA` | QA Engineer / Quality Manager | CoC, NCR summaries, compliance statements, MRB cover page. |
| `CUSTOMER` | Customer / Commercial Manager | Customer-furnished drawings, specifications, approved deviations. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-009-04-001 | Index state → FINAL | Prerequisite | All line items must have status VALIDATED, WAIVED, or NOT_APPLICABLE. No PENDING or RECEIVED items allowed. | "Cannot finalize MRB Index: {n} line items still pending validation." |
| VR-009-04-002 | Line item modification | State guard | When `index_state` = LIVE, line items cannot be added or removed without a formal amendment (logged in audit trail). | "MRB Index is LIVE. Line item changes require a formal amendment." |
| VR-009-04-003 | Index state → FINAL | Lock | When `index_state` = FINAL, all fields are frozen except `page_range`. | "MRB Index is FINAL. Only page range can be modified." |
| VR-009-04-004 | page_range | Format | Must match pattern `\d+–\d+` (e.g., "45–52"). Second number must be >= first. | "Page range must be in format 'start–end' (e.g., 45–52)." |
| VR-009-04-005 | Status progression | Order | Status can only progress forward: PENDING → RECEIVED → VALIDATING → VALIDATED. Regression only via REJECTED or CORRECTED. | "Document status cannot regress from {current} to {requested}." |

#### Auto-Population Specifications

| Field | Source | Trigger | Condition |
|-------|--------|---------|-----------|
| All DRAFT columns (1–9, 15) | `mrb.sdrl_line_item` | On MRB initialization (FM-009-03) | Always — 1:1 copy from SDRL line items |
| Responsible | Routing table (above) | On MRB initialization | Derived from `data_source` |
| Status | `mrb.mrb_document` | On document upload/validation events | Real-time — event-driven update |
| Received Date | `mrb.mrb_document` | On document upload | When `uploaded_at` is set |
| Validated Date | `mrb.validation` | On final validation pass | When all applicable layers = PASS |
| Document Reference | `mrb.mrb_document` | On document upload | When `artifact_uri` is set |
| Page Range | Manual / assembly tool | During MRB assembly (PR-012) | When index_state = FINAL |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-009-01 (Order Requirement Matrix) | SDRL line items populate the index rows. 1:1 mapping. |
| **IN** ← | FM-009-03 (MRB Initialization Record) | MRB initialization triggers index generation and sets state to DRAFT. |
| **IN** ← | FM-008-01 (Material Gate Checklist) | Gate decision APPROVED or CONDITIONAL_APPROVAL updates the status of material certificate line items (Section 3). |
| **IN** ← | FM-010-02 (Document Validation Log) | Validation results update the Status and Validated Date columns in real-time. |
| **OUT** → | FM-010-02 (Document Validation Log) | Each index line item triggers validation when a document is received for that slot. |
| **OUT** → | FM-010-01 (Correction Request) | When a document fails validation, the MRB Index status shows REJECTED and links to the CR. |
| **OUT** → | FM-010-04 (CoC Prerequisite Gate) | Gate check verifies all index line items are VALIDATED before CoC generation. |
| **OUT** → | FM-012-01 (MRB Assembly Checklist) | Assembly prerequisites reference the finalized MRB Index. |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | Lives across the full pipeline: initialized at SDRL Intake, updated during Document Collection and Validation, finalized at MRB Assembly. |
| **Index state machine** | DRAFT (on initialization) → LIVE (on first document receipt) → FINAL (on MRB assembly start). |
| **Order state sync** | Index state DRAFT aligns with order state MRB_INITIALIZED. Index going LIVE aligns with order entering COLLECTING. Index going FINAL aligns with order entering MRB_ASSEMBLY. |
| **Real-time updates** | Status, Received Date, Validated Date, and Document Reference update automatically via database triggers/events when documents are uploaded or validated. No manual refresh needed. |

#### Industry Applicability

| Feature | Oil & Gas | Defence |
|---------|-----------|---------|
| Section count | 7 standard (per AM-CT-001 §4.2), extendable with custom sections | 8 standard (per AM-CT-001 §5.2), extendable with custom sections |
| Typical line items | ~30 (SDRL-OG-001) | ~25 (SDRL-DEF-001) |
| FAIR Reference column | Hidden | Shown when FAIR required |
| ITP link | Links to FM-009-02 | Not applicable |
| Common core documents | CoC, material certs, dimensional inspection (CNC), NDT, PMI | CoC, material certs, dimensional inspection (CNC), NDT, FAIR |

---

## 10. PR-010 Forms — Document Validation and Verification

### 10.1 FM-010-01: Correction Request ★ Phase 0

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-010-01 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-010 — Document Validation and Verification |
| **Industry** | BOTH |
| **Pipeline Stage** | Document Validation |
| **DB Entity** | `mrb.correction_request` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Issued when a document fails any of the 5 validation layers (L1–L5) as defined in PR-010, Section 6.12. The correction request specifies the exact failure, the required corrective action, the responsible party, and tracks the correction lifecycle from issuance through resolution. Unresolved correction requests block CoC generation (FM-010-04).

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | CR ID | `correction_request.cr_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | CR Number | `correction_request.cr_number` | VARCHAR(20) | A | 20 | Auto-generated: `AM-CR-[YYYY]-[NNNNN]`. Sequential, never reused. |
| 3 | Order Reference | `correction_request.order_id` | FK → `order` | A | — | Auto-populated from the document's MRB → order chain. Read-only. |
| 4 | MRB Number | (derived) | VARCHAR(50) | A | 50 | Auto-populated from `mrb.mrb_id` display identifier. Read-only. |
| 5 | PO Number | (derived) | VARCHAR(50) | A | 50 | Auto-populated from order → PO. Read-only. |
| 6 | Customer | (derived) | VARCHAR(200) | A | 200 | Auto-populated from order → customer. Read-only. |
| 7 | Document Reference | `correction_request.doc_id` | FK → `mrb_document` | R | — | Which document failed validation. Lookup from documents in the order's MRB. |
| 8 | Document Type | (derived) | VARCHAR(100) | A | 100 | Auto-populated from `mrb_document.doc_type`. Read-only. |
| 9 | Document Title | (derived) | VARCHAR(255) | A | 255 | Auto-populated from the MRB Index line item. Read-only. |
| 10 | MRB Section | (derived) | INTEGER | A | — | Auto-populated from `mrb_document.section_no`. Read-only. |
| 11 | Validation Reference | `correction_request.validation_id` | FK → `validation` | R | — | Links to the specific validation run that failed. |
| 12 | **Validation Layer** | `correction_request.layer` | ENUM(`validation_layer`) | R | — | Which layer failed: L1_EXISTENCE through L5_TRACEABILITY. |
| 13 | **Failure Code** | `correction_request.failure_code` | ENUM(`failure_code`) | R | — | MISSING, FORMAT_ERROR, INCOMPLETE, NON_COMPLIANT, or TRACEABILITY_BREAK. |
| 14 | **Specific Finding** | `correction_request.description` | TEXT | R | 3000 | Detailed description of what specifically failed. E.g., "Material certificate does not include impact test results at -46°C as required by NORSOK M-650." |
| 15 | **Required Action** | `correction_request.required_action` | TEXT | R | 2000 | What must be done to correct the failure. E.g., "Request updated certificate from supplier including impact test data per ASTM A370." |
| 16 | Responsible Party | `correction_request.assigned_to` | FK → `auth.users` | R | — | Person assigned to resolve. Lookup filtered by role. |
| 17 | Responsible Role | `correction_request.assigned_role` | ENUM(`responsible_role`) | R | — | Role classification per PR-010 Section 6.12: QA_ENGINEER, PURCHASING, PRODUCTION, CUSTOMER, or SUPPLIER. Auto-suggested from document's `data_source`. |
| 18 | Due Date | `correction_request.due_date` | DATE | R | — | When the correction must be completed. |
| 19 | **Status** | `correction_request.status` | ENUM(`cr_status`) | R | — | OPEN → IN_PROGRESS → RESOLVED / ESCALATED / WAIVED. |
| 20 | Resolution Description | `correction_request.resolution_description` | TEXT | C | 3000 | Required when status = RESOLVED. Describes what was done to correct the issue. |
| 21 | Corrected Document URI | `correction_request.corrected_doc_uri` | VARCHAR(500) | C | 500 | Storage path to the replacement/corrected document. Required when status = RESOLVED. |
| 22 | Resolved By | `correction_request.resolved_by` | FK → `auth.users` | C | — | Auto-populated when status changes to RESOLVED. |
| 23 | Resolved At | `correction_request.resolved_at` | TIMESTAMP | C | — | System timestamp when RESOLVED. |
| 24 | Escalated To | `correction_request.escalated_to` | FK → `auth.users` | C | — | Quality Manager, when CR needs waiver or elevated decision. Required when status = ESCALATED. |
| 25 | Escalation Reason | `correction_request.escalation_reason` | TEXT | C | 2000 | Required when status = ESCALATED. |
| 26 | Waiver Reference | `correction_request.waiver_ref` | VARCHAR(100) | C | 100 | Customer approval reference when document requirement is waived. Required when status = WAIVED. |
| 27 | Waiver Approved By | `correction_request.waiver_approved_by` | VARCHAR(200) | C | 200 | Customer contact who approved the waiver. Required when status = WAIVED. |
| 28 | Waiver Reason | `correction_request.waiver_reason` | TEXT | C | 2000 | Justification for waiver. Required when status = WAIVED. |
| 29 | Created By | `correction_request.created_by` | FK → `auth.users` | A | — | Authenticated user who created the CR. Read-only. |
| 30 | Created At | `correction_request.created_at` | TIMESTAMP | A | — | System timestamp at creation. Read-only. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-010-01-001 | resolution_description | Conditional | Required when `status` = RESOLVED. | "Resolution description is required when closing a correction request." |
| VR-010-01-002 | corrected_doc_uri | Conditional | Required when `status` = RESOLVED and `failure_code` is not TRACEABILITY_BREAK. | "A corrected document must be uploaded when resolving a correction request." |
| VR-010-01-003 | waiver_ref, waiver_approved_by, waiver_reason | Conditional | All three required when `status` = WAIVED. | "Waiver requires: reference number, customer approver name, and justification." |
| VR-010-01-004 | escalated_to, escalation_reason | Conditional | Both required when `status` = ESCALATED. | "Escalation requires a target person and reason." |
| VR-010-01-005 | due_date | Range | Must be >= `created_at` date. | "Due date cannot be in the past." |
| VR-010-01-006 | status | Progression | Valid transitions: OPEN → IN_PROGRESS → RESOLVED/ESCALATED/WAIVED. ESCALATED → RESOLVED/WAIVED. No regression to OPEN after IN_PROGRESS. | "Invalid status transition from {current} to {requested}." |
| VR-010-01-007 | (on RESOLVED) | Trigger | When status changes to RESOLVED, the linked document (`doc_id`) must be re-submitted for full 5-layer re-validation. System auto-creates a new validation cycle. | (System action, no user error.) |
| VR-010-01-008 | cr_number | Uniqueness | Auto-generated and globally unique. Never reused even if CR is voided. | (System-enforced.) |

#### Auto-Population Specifications

| Field | Source Entity | Source Column | Trigger | Condition |
|-------|-------------|---------------|---------|-----------|
| Order Reference | `mrb.mrb_document` → `mrb.mrb` → `mrb.order` | `order_id` | On `doc_id` selection | Always |
| MRB Number | `mrb.mrb` | display identifier | Via `mrb_document.mrb_id` | Always |
| PO Number | `mrb.order` | `po_number` | Via order chain | Always |
| Customer | `erp.customer` | `name` | Via order → customer | Always |
| Document Type | `mrb.mrb_document` | `doc_type` | On `doc_id` selection | Always |
| Document Title | `mrb.sdrl_line_item` (via MRB Index join) | `doc_title` | On `doc_id` selection | Always |
| MRB Section | `mrb.mrb_document` | `section_no` | On `doc_id` selection | Always |
| CR Number | System | Auto-increment | On form creation | Always |
| Responsible Role | (derived) | — | On `doc_id` selection | Suggested from `mrb_document.data_source` mapping |
| Created By | `auth.users` | Current session | On form open | Always |
| Created At | System | `NOW()` | On form creation | Always |
| Resolved By | `auth.users` | Current session | On status change to RESOLVED | Always |
| Resolved At | System | `NOW()` | On status change to RESOLVED | Always |

#### Responsible Role Auto-Suggestion (from document data_source)

| Document Data Source | Suggested Role | Rationale |
|---------------------|---------------|-----------|
| `SUPPLIER` | `PURCHASING` | Purchasing contacts the supplier for corrected certificate. |
| `CNC_INLINE` | `PRODUCTION` | Production re-runs measurement or corrects machine output. |
| `METROLOGY` | `QA_ENGINEER` | QA re-measures or re-calibrates. |
| `INSPECTION` | `QA_ENGINEER` | QA re-inspects. |
| `SPECIAL_PROCESS` | `PURCHASING` or `QA_ENGINEER` | Depends on whether external (purchasing) or internal (QA). |
| `INTERNAL_QA` | `QA_ENGINEER` | QA corrects internal documentation. |
| `CUSTOMER` | `CUSTOMER` | Customer must provide corrected specification or drawing. |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-010-02 (Document Validation Log) | Validation failure triggers CR creation. The `validation_id` links to the failing validation run. |
| **IN** ← | FM-008-01 (Material Gate Checklist) | Gate decision REJECTED may trigger a CR for the material certificate. |
| **OUT** → | FM-009-04 (MRB Index) | CR status is reflected in the MRB Index: document shows REJECTED while CR is open, CORRECTED when resolved, WAIVED if waived. |
| **OUT** → | FM-010-04 (CoC Prerequisite Gate) | Unresolved CRs (status OPEN, IN_PROGRESS, or ESCALATED) block the CoC prerequisite gate. |
| **OUT** → | FM-010-02 (Document Validation Log) | When CR status = RESOLVED, the corrected document is re-submitted for validation, creating a new entry in the validation log. |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | Document Validation (PR-010, Section 6.12) |
| **Triggered by** | Validation failure at any layer (L1–L5). System auto-creates a CR draft when a validation result = FAIL. QA Engineer completes and submits. |
| **On RESOLVED** | Corrected document is uploaded and linked. System initiates re-validation of the corrected document through all 5 layers. MRB Index status for this document updates from REJECTED to VALIDATING. |
| **On WAIVED** | MRB Index status for this document updates to WAIVED. No re-validation needed. Waiver is recorded in audit trail. |
| **On ESCALATED** | Notification sent to Quality Manager. CR remains open until QM resolves or approves waiver. |
| **CoC blocking** | Any OPEN, IN_PROGRESS, or ESCALATED CR blocks CoC generation for the entire order. |

#### Industry Applicability

| Feature | Oil & Gas | Defence |
|---------|-----------|---------|
| All 30 fields | ✓ | ✓ |
| Waiver process | Customer approval required | Customer + sometimes government authority approval (AQAP) |
| Escalation path | QA Engineer → Quality Manager | QA Engineer → Quality Manager → Defence Customer Representative |
| Typical failure codes | FORMAT_ERROR (wrong cert type), INCOMPLETE (missing test data), NON_COMPLIANT (values outside NORSOK limits) | TRACEABILITY_BREAK (serial number gaps), MISSING (FAIR forms incomplete), NON_COMPLIANT (NADCAP lapse) |

---

### 10.2 FM-010-02: Document Validation Log

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-010-02 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-010 — Document Validation and Verification |
| **Industry** | BOTH |
| **Pipeline Stage** | Document Collection → Validation |
| **DB Entity** | `mrb.validation` (one row per document per validation layer) |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Records the validation status and results of every document collected for the order. Updated throughout the order lifecycle as documents are received, validated through all 5 layers (L1–L5), and either approved or rejected. Provides a real-time view of which documents are validated and which are outstanding.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Validation ID | `validation.validation_id` | UUID | A | — | Primary key. Auto-generated. One record per document per validation layer. |
| 2 | Document Reference | `validation.doc_id` | FK → `mrb_document` | R | — | Which document is being validated. |
| 3 | MRB Reference | (derived) | FK → `mrb` | A | — | Auto-populated from document. Read-only. |
| 4 | Order Reference | (derived) | FK → `order` | A | — | Auto-populated from MRB. Read-only. |
| 5 | Document Type | (derived) | VARCHAR(100) | A | 100 | Auto-populated from `mrb_document.doc_type`. Read-only. |
| 6 | Document Title | (derived from MRB Index) | VARCHAR(255) | A | 255 | Auto-populated. Read-only. |
| 7 | MRB Section | (derived) | INTEGER | A | — | Auto-populated. Read-only. |
| 8 | **Validation Layer** | `validation.layer` | ENUM(`validation_layer`) | R | — | L1_EXISTENCE, L2_FORMAT, L3_COMPLETENESS, L4_COMPLIANCE, L5_TRACEABILITY. |
| 9 | **Validation Result** | `validation.result` | ENUM(`validation_result`) | R | — | PASS, FAIL, or WAIVED. |
| 10 | Result Details | `validation.details` | JSONB | R | — | Layer-specific results. L1: `{"exists": true}`. L2: `{"mime_type": "application/pdf", "readable": true, "file_size_kb": 245}`. L3: `{"required_fields": ["heat_number", "tensile"], "present": ["heat_number", "tensile"], "missing": []}`. L4: `{"checks": [{"property": "tensile", "actual": 520, "min": 485, "result": "PASS"}]}`. L5: `{"chain": [{"link": "PO→cert", "status": "VERIFIED"}]}`. |
| 11 | Failure Details | `validation.failure_details` | TEXT | C | 2000 | Required when result = FAIL. Human-readable description of what failed. |
| 12 | Validator | `validation.validator_id` | FK → `auth.users` | A | — | Authenticated user or "SYSTEM" for automated checks. |
| 13 | Validated At | `validation.validated_at` | TIMESTAMP | A | — | System timestamp. |
| 14 | Validation Method | `validation.validation_method` | ENUM (AUTOMATIC / MANUAL / HYBRID) | A | — | How this layer was checked. L1–L3 typically AUTOMATIC, L4–L5 typically MANUAL or HYBRID. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-010-02-001 | failure_details | Conditional | Required when `result` = FAIL. | "Failure details required when validation fails." |
| VR-010-02-002 | layer sequence | Business logic | Layers must be validated in order: L1 before L2, L2 before L3, etc. A higher layer cannot be evaluated until all lower layers PASS or are WAIVED. | "Cannot validate L{n} until L{n-1} passes." |
| VR-010-02-003 | (on FAIL) | Trigger | When any layer result = FAIL, system auto-creates a Correction Request (FM-010-01) draft. | (System action.) |
| VR-010-02-004 | (on all PASS) | Trigger | When all applicable layers PASS for a document, `mrb_document.validation_status` updates to VALIDATED and MRB Index status updates. | (System action.) |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-009-04 (MRB Index) | Each MRB Index line item triggers a validation cycle when its document is received. |
| **OUT** → | FM-010-01 (Correction Request) | Validation FAIL triggers CR creation. |
| **OUT** → | FM-009-04 (MRB Index) | Validation results update the Status and Validated Date columns in the MRB Index. |
| **OUT** → | FM-010-04 (CoC Prerequisite Gate) | All documents must be VALIDATED before the CoC gate can pass. |

#### Workflow Integration

| Property | Value |
|----------|-------|
| **Pipeline stage** | Document Validation (PR-010, Sections 6.3–6.11) |
| **Triggered by** | Document upload to an MRB slot. System auto-initiates L1 validation. |
| **Automation** | L1 (existence) and L2 (format) are fully automatic. L3 (completeness) is partially automatic (JSON schema check). L4 (compliance) requires QA Engineer review for numeric checks. L5 (traceability) is manual cross-document verification. |
| **On all layers PASS** | Document status → VALIDATED. MRB Index updated. |

---

### 10.3 FM-010-03: Cross-Document Traceability Verification Record

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-010-03 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-010 — Document Validation and Verification |
| **Industry** | BOTH |
| **Pipeline Stage** | Validation (L5 — Traceability) |
| **DB Entity** | `mrb.traceability_verification` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Verifies the complete traceability chain across all documents in the MRB. Confirms that every link in the chain — from purchase order through material certificate, goods receiving, traceability matrix, production process, inspection reports, to CoC — references consistent identifiers (heat numbers, serial numbers, drawing revisions, PO numbers). This is the L5 validation layer applied at the order level, not per-document.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Verification ID | `traceability_verification.verification_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Order Reference | `traceability_verification.order_id` | FK → `order` | R | — | Which order is being verified. |
| 3 | MRB Reference | `traceability_verification.mrb_id` | FK → `mrb` | A | — | Auto-populated. Read-only. |
| 4 | PO Number | (derived) | VARCHAR(50) | A | 50 | Auto-populated. Read-only. |
| 5 | **PO → Material Cert Link** | `traceability_verification.check_po_cert` | ENUM (VERIFIED / FAILED / N_A) | R | — | PO references match material certificate references. |
| 6 | PO → Cert Details | `traceability_verification.check_po_cert_details` | TEXT | C | 1000 | Required if FAILED. Describe discrepancy. |
| 7 | **Cert → Goods Receiving Link** | `traceability_verification.check_cert_receiving` | ENUM (VERIFIED / FAILED / N_A) | R | — | Heat number on certificate matches goods receiving record. |
| 8 | Cert → Receiving Details | `traceability_verification.check_cert_receiving_details` | TEXT | C | 1000 | Required if FAILED. |
| 9 | **Receiving → Traceability Matrix Link** | `traceability_verification.check_receiving_trace` | ENUM (VERIFIED / FAILED / N_A) | R | — | Heat number allocated in FM-008-03 matches receiving record. |
| 10 | Receiving → Trace Details | `traceability_verification.check_receiving_trace_details` | TEXT | C | 1000 | Required if FAILED. |
| 11 | **Traceability → Production Link** | `traceability_verification.check_trace_production` | ENUM (VERIFIED / FAILED / N_A) | R | — | Serial numbers in traceability matrix match production records. |
| 12 | Trace → Production Details | `traceability_verification.check_trace_production_details` | TEXT | C | 1000 | Required if FAILED. |
| 13 | **Production → Inspection Link** | `traceability_verification.check_production_inspection` | ENUM (VERIFIED / FAILED / N_A) | R | — | Part serial numbers in inspection reports match production records. |
| 14 | Production → Inspection Details | `traceability_verification.check_production_inspection_details` | TEXT | C | 1000 | Required if FAILED. |
| 15 | **Inspection → CoC Link** | `traceability_verification.check_inspection_coc` | ENUM (VERIFIED / FAILED / N_A) | R | — | Serial numbers and drawing revisions in CoC match inspection reports. |
| 16 | Inspection → CoC Details | `traceability_verification.check_inspection_coc_details` | TEXT | C | 1000 | Required if FAILED. |
| 17 | **Chronological Date Check** | `traceability_verification.check_dates` | ENUM (VERIFIED / FAILED) | R | — | All dates in logical order: PO date → cert date → receiving date → production → inspection → CoC. |
| 18 | Date Check Details | `traceability_verification.check_dates_details` | TEXT | C | 1000 | Required if FAILED. |
| 19 | **Drawing Revision Consistency** | `traceability_verification.check_drawing_rev` | ENUM (VERIFIED / FAILED / N_A) | R | — | Same drawing revision referenced across all documents. |
| 20 | Drawing Rev Details | `traceability_verification.check_drawing_rev_details` | TEXT | C | 1000 | Required if FAILED. |
| 21 | **Overall Chain Integrity** | `traceability_verification.overall_result` | ENUM (PASS / FAIL) | R | — | PASS only if all checks are VERIFIED or N_A. Any FAILED → overall FAIL. |
| 22 | Verified By | `traceability_verification.verified_by` | FK → `auth.users` | A | — | Auto-populated. |
| 23 | Verified At | `traceability_verification.verified_at` | TIMESTAMP | A | — | Auto-populated. |
| 24 | Notes | `traceability_verification.notes` | TEXT | O | 2000 | Free text. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-010-03-001 | overall_result | Consistency | Cannot be PASS if any check is FAILED. | "Overall chain integrity cannot pass with failed links." |
| VR-010-03-002 | *_details | Conditional | Detail fields required when corresponding check = FAILED. | "Details required for failed traceability link." |
| VR-010-03-003 | (on FAIL) | Trigger | Overall FAIL triggers FM-010-01 (Correction Request) for each failed link. | (System action.) |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-008-03 (Traceability Matrix) | Material-to-serial-number chain data. |
| **IN** ← | FM-010-02 (Validation Log) | Individual document validation results feed into chain verification. |
| **OUT** → | FM-010-01 (Correction Request) | Failed links generate CRs. |
| **OUT** → | FM-010-04 (CoC Prerequisite Gate) | Traceability verification must PASS before CoC gate. |

---

### 10.4 FM-010-04: CoC Prerequisite Gate Checklist

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-010-04 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-010 — Document Validation and Verification |
| **Industry** | BOTH |
| **Pipeline Stage** | Validation → CoC (gate between PR-010 and PR-011) |
| **DB Entity** | `mrb.coc_prerequisite_gate` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Verification checklist confirming all prerequisites for CoC generation are met BEFORE the Certificate of Conformance can be generated. This is the final quality gate — it blocks CoC generation (FM-011-01) if any prerequisite fails. The gate checks: all MRB documents validated, all correction requests resolved, traceability verified, no open NCRs, FAIR complete (if Defence), and ITP signed off (if O&G).

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Gate ID | `coc_prerequisite_gate.gate_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Order Reference | `coc_prerequisite_gate.order_id` | FK → `order` | R | — | Which order. |
| 3 | MRB Reference | `coc_prerequisite_gate.mrb_id` | FK → `mrb` | A | — | Auto-populated. |
| 4 | Industry | (from order) | ENUM(`industry_class`) | A | — | Auto-populated. Determines which checks are applicable. |
| 5 | **Check 1: All Documents Validated** | `coc_prerequisite_gate.check_all_docs` | ENUM (PASS / FAIL) | A | — | Auto-calculated. PASS only if every required MRB Index line item has status VALIDATED or WAIVED. |
| 6 | Documents Outstanding | `coc_prerequisite_gate.docs_outstanding` | INTEGER | A | — | Count of line items not yet VALIDATED/WAIVED. Auto-calculated. |
| 7 | **Check 2: No Open CRs** | `coc_prerequisite_gate.check_no_open_cr` | ENUM (PASS / FAIL) | A | — | Auto-calculated. PASS only if all CRs for this order are RESOLVED or WAIVED (no OPEN, IN_PROGRESS, or ESCALATED). |
| 8 | Open CR Count | `coc_prerequisite_gate.open_cr_count` | INTEGER | A | — | Count of unresolved CRs. Auto-calculated. |
| 9 | **Check 3: Traceability Verified** | `coc_prerequisite_gate.check_traceability` | ENUM (PASS / FAIL / NOT_YET_RUN) | A | — | Auto-calculated from FM-010-03 result. |
| 10 | **Check 4: FAIR Complete** | `coc_prerequisite_gate.check_fair` | ENUM (PASS / FAIL / N_A) | A | — | N_A for Oil & Gas orders without FAIR. PASS if AS9102 FAIR forms are complete (Defence). |
| 11 | **Check 5: ITP Signed Off** | `coc_prerequisite_gate.check_itp` | ENUM (PASS / FAIL / N_A) | A | — | N_A for Defence orders. PASS if all HOLD and WITNESS points in FM-009-02 are SIGNED_OFF. |
| 12 | **Check 6: No Borderline Items** | `coc_prerequisite_gate.check_no_borderline` | ENUM (PASS / FAIL / OVERRIDE) | A | — | PASS if no gate reviews have unresolved BORDERLINE flags. OVERRIDE requires QM approval. |
| 13 | **Overall Gate Result** | `coc_prerequisite_gate.gate_result` | ENUM (PASS / FAIL) | A | — | PASS only if all applicable checks pass. Blocks CoC generation if FAIL. |
| 14 | Gate Evaluated By | `coc_prerequisite_gate.evaluated_by` | FK → `auth.users` | A | — | Auto-populated. QA Engineer or system. |
| 15 | Gate Evaluated At | `coc_prerequisite_gate.evaluated_at` | TIMESTAMP | A | — | Auto-populated. |
| 16 | QM Override | `coc_prerequisite_gate.qm_override` | BOOLEAN | O | — | Quality Manager can override FAIL gate with documented justification. |
| 17 | QM Override Reason | `coc_prerequisite_gate.qm_override_reason` | TEXT | C | 2000 | Required when `qm_override` = true. |
| 18 | QM Override By | `coc_prerequisite_gate.qm_override_by` | FK → `auth.users` | C | — | Must have Quality Manager role. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-010-04-001 | gate_result | Calculation | PASS only when all applicable checks (1–6) are PASS or N_A (or OVERRIDE for Check 6). | "CoC prerequisite gate failed: {failing checks}." |
| VR-010-04-002 | qm_override | Authorization | Only users with Quality Manager role can set `qm_override` = true. | "Only Quality Manager can override the CoC prerequisite gate." |
| VR-010-04-003 | qm_override_reason | Conditional | Required when `qm_override` = true. | "Override justification required." |
| VR-010-04-004 | (on PASS) | Trigger | Order state transitions: `VALIDATING` → `COC_PENDING`. Enables CoC generation (FM-011-01). | (System action.) |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-009-04 (MRB Index) | Document validation status feeds Check 1. |
| **IN** ← | FM-010-01 (Correction Request) | CR status feeds Check 2. |
| **IN** ← | FM-010-03 (Traceability Verification) | Chain integrity feeds Check 3. |
| **IN** ← | FM-009-02 (ITP Tracker) | ITP sign-off status feeds Check 5 (O&G). |
| **IN** ← | FM-008-01 (Material Gate) | Borderline flags feed Check 6. |
| **OUT** → | FM-011-01 (CoC Register) | Gate PASS enables CoC generation. |

---

## 11. PR-011 Forms — Certificate of Conformance

### 11.1 FM-011-01: CoC Register

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-011-01 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-011 — Certificate of Conformance |
| **Industry** | BOTH |
| **Pipeline Stage** | CoC Generation |
| **DB Entity** | `mrb.coc` |
| **Retention** | Permanent (lifetime of company) |

#### Purpose

Master registry of all issued Certificates of Conformance. Records CoC generation, signature, and status. Each CoC is a legally binding document certifying that manufactured products conform to all specified requirements. The register maintains a permanent audit trail of all CoCs — issued, revised, and voided.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | CoC ID | `coc.coc_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | CoC Number | `coc.coc_number` | VARCHAR(25) | A | 25 | Auto-generated: `AM-COC-[YYYY]-[NNNNN]`. Sequential, never reused. |
| 3 | MRB Reference | `coc.mrb_id` | FK → `mrb` | R | — | Which MRB this CoC belongs to. |
| 4 | Order Reference | (derived) | FK → `order` | A | — | Auto-populated from MRB. Read-only. |
| 5 | PO Number | (derived) | VARCHAR(50) | A | 50 | Auto-populated. Read-only. |
| 6 | Customer | (derived) | VARCHAR(200) | A | 200 | Auto-populated. Read-only. |
| 7 | Part Number | (from order) | VARCHAR(100) | A | 100 | Auto-populated. Read-only. |
| 8 | Drawing Revision | (from order) | VARCHAR(20) | A | 20 | Auto-populated. Read-only. |
| 9 | Quantity | (from order) | INTEGER | A | — | Number of parts covered. Auto-populated. |
| 10 | Serial Numbers | (from traceability) | TEXT | A | — | Range or list. Auto-populated from FM-008-03. |
| 11 | Template Type | `coc.template_type` | ENUM(`coc_template_type`) | AE | — | OIL_GAS_STANDARD, DEFENCE_STANDARD, DEFENCE_AQAP, CUSTOM. Auto-set from industry; editable. |
| 12 | CoC Prerequisite Gate | (link) | FK → `coc_prerequisite_gate` | A | — | Link to FM-010-04 gate that authorized this CoC. Read-only. |
| 13 | **Signed By** | `coc.signed_by` | FK → `auth.users` | R | — | Authorized signatory from FM-011-03 register. Must have appropriate authority level. |
| 14 | Signed At | `coc.signed_at` | TIMESTAMP | A | — | System timestamp when signature applied. |
| 15 | **Signature Hash** | `coc.signature_hash` | VARCHAR(64) | A | — | SHA-256 hash of the signed CoC document. Auto-generated. |
| 16 | **Signature Method** | `coc.signature_method` | ENUM(`signature_method`) | R | — | INTERNAL_PKI (Phase 0+), BANKID (optional add-on), MANUAL (Phase 0 fallback). Per decision R9. |
| 17 | PDF URI | `coc.pdf_uri` | VARCHAR(500) | A | 500 | Storage path to the signed CoC PDF. Auto-populated after generation. |
| 18 | PDF Checksum | `coc.checksum_sha256` | VARCHAR(64) | A | 64 | SHA-256 of the generated PDF file. Auto-calculated. |
| 19 | **Status** | `coc.status` | ENUM(`coc_status`) | R | — | ACTIVE, SUPERSEDED, or VOID. |
| 20 | Superseded By | `coc.superseded_by_coc_id` | FK → `coc` | C | — | Links to replacement CoC when SUPERSEDED. |
| 21 | Issue Date | `coc.issued_at` | TIMESTAMP | A | — | When CoC was first issued. Auto-populated. |
| 22 | Notes | `coc.notes` | TEXT | O | 2000 | Free text. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-011-01-001 | signed_by | Authorization | Signer must be in FM-011-03 (Authorized Signatory Register) with status ACTIVE and appropriate authority level. | "Signer is not an authorized signatory or authority level insufficient." |
| VR-011-01-002 | (prerequisite) | Business logic | CoC can only be created when FM-010-04 gate_result = PASS for this order. | "CoC prerequisite gate has not passed." |
| VR-011-01-003 | status change to VOID | Business logic | Voiding a CoC requires FM-011-02 (Revision/Void Record) with documented justification. | "CoC void requires a formal revision/void record." |
| VR-011-01-004 | coc_number | Uniqueness | Globally unique. Never reused even if VOID. | (System-enforced.) |
| VR-011-01-005 | (on ACTIVE) | Trigger | Order state transitions: `COC_PENDING` → `COC_SIGNED`. | (System action.) |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-010-04 (CoC Prerequisite Gate) | Gate PASS authorizes CoC generation. |
| **IN** ← | FM-011-03 (Authorized Signatory Register) | Signer must be in register with appropriate authority. |
| **OUT** → | FM-011-02 (CoC Revision/Void Record) | When CoC is revised or voided. |
| **OUT** → | FM-012-01 (MRB Assembly Checklist) | CoC must be issued before MRB assembly. |
| **OUT** → | FM-009-04 (MRB Index) | CoC is a required line item in MRB Section 6 (O&G) or Section 8 (Defence). |

---

### 11.2 FM-011-02: CoC Revision/Void Record

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-011-02 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-011 — Certificate of Conformance |
| **Industry** | BOTH |
| **Pipeline Stage** | CoC Lifecycle Management |
| **DB Entity** | `mrb.coc_revision` |
| **Retention** | Per order archival requirement: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. |

#### Purpose

Documents any revision or voiding of a previously issued Certificate of Conformance. Maintains historical record of why changes were made. Every CoC status change (ACTIVE → SUPERSEDED or ACTIVE → VOID) must be documented here.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Revision Record ID | `coc_revision.revision_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Original CoC Number | `coc_revision.original_coc_id` | FK → `coc` | R | — | Which CoC is being revised or voided. |
| 3 | Original CoC Number (display) | (derived) | VARCHAR(25) | A | 25 | Auto-populated. Read-only. |
| 4 | **Action** | `coc_revision.action` | ENUM (REVISION / VOID) | R | — | REVISION = replaced by new CoC. VOID = cancelled without replacement. |
| 5 | Reason | `coc_revision.reason` | TEXT | R | 2000 | Detailed justification for revision or void. |
| 6 | New CoC Number | `coc_revision.new_coc_id` | FK → `coc` | C | — | Required when action = REVISION. Links to the replacement CoC. |
| 7 | New CoC Number (display) | (derived) | VARCHAR(25) | A | 25 | Auto-populated when action = REVISION. |
| 8 | Customer Notified | `coc_revision.customer_notified` | BOOLEAN | R | — | Customer must be informed of CoC revision or void. |
| 9 | Customer Notification Date | `coc_revision.customer_notified_at` | TIMESTAMP | C | — | Required when `customer_notified` = true. |
| 10 | Authorized By | `coc_revision.authorized_by` | FK → `auth.users` | R | — | Quality Manager authorization required for all CoC changes. |
| 11 | Authorized At | `coc_revision.authorized_at` | TIMESTAMP | A | — | Auto-populated. |
| 12 | Created By | `coc_revision.created_by` | FK → `auth.users` | A | — | Auto-populated. |
| 13 | Created At | `coc_revision.created_at` | TIMESTAMP | A | — | Auto-populated. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-011-02-001 | new_coc_id | Conditional | Required when action = REVISION. | "Replacement CoC required for revision." |
| VR-011-02-002 | authorized_by | Authorization | Must have Quality Manager role. | "Only Quality Manager can authorize CoC revision or void." |
| VR-011-02-003 | (on save) | Trigger | Updates original CoC status: ACTIVE → SUPERSEDED (revision) or ACTIVE → VOID. | (System action.) |

---

### 11.3 FM-011-03: Authorized Signatory Register

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-011-03 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-011 — Certificate of Conformance |
| **Industry** | BOTH |
| **Pipeline Stage** | System-wide (lookup table, not per-order) |
| **DB Entity** | `mrb.authorized_signatory` |
| **Retention** | Current version + all previous versions (permanent) |

#### Purpose

Maintains the list of all persons authorized to sign Certificates of Conformance, their authority levels (1–3), and delegation dates. Only persons in this register with ACTIVE status can sign CoCs. This is a system-wide register, not per-order.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Signatory ID | `authorized_signatory.signatory_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Person | `authorized_signatory.user_id` | FK → `auth.users` | R | — | User account of the authorized person. |
| 3 | Person Name | (derived) | VARCHAR(200) | A | 200 | Auto-populated from user profile. |
| 4 | Title | `authorized_signatory.title` | VARCHAR(100) | R | 100 | Job title. E.g., "Quality Manager", "Senior QA Engineer". |
| 5 | **Authority Level** | `authorized_signatory.authority_level` | ENUM(`authority_level`) | R | — | LEVEL_1: Standard CoC (routine orders). LEVEL_2: Elevated CoC (high-value, Defence). LEVEL_3: Full authority (all orders including ITAR). |
| 6 | Signature Method | `authorized_signatory.signature_method` | ENUM(`signature_method`) | R | — | INTERNAL_PKI, BANKID, or MANUAL. Determines which signing mechanism this person uses. |
| 7 | PKI Certificate Reference | `authorized_signatory.pki_cert_ref` | VARCHAR(200) | C | 200 | Required when signature_method = INTERNAL_PKI. Internal PKI certificate ID. |
| 8 | BankID Reference | `authorized_signatory.bankid_ref` | VARCHAR(100) | C | 100 | Required when signature_method = BANKID. BankID personal identifier. |
| 9 | Delegation Date | `authorized_signatory.delegation_date` | DATE | R | — | When authority was granted. |
| 10 | Training Completion Date | `authorized_signatory.training_date` | DATE | R | — | When signing authority training was completed. Must be <= delegation_date. |
| 11 | **Status** | `authorized_signatory.status` | ENUM (ACTIVE / SUSPENDED / REVOKED) | R | — | ACTIVE = can sign. SUSPENDED = temporarily blocked. REVOKED = permanently removed. |
| 12 | Limitations | `authorized_signatory.limitations` | TEXT | O | 1000 | Any restrictions. E.g., "O&G orders only", "Quantities < 100 parts". |
| 13 | Revoked Date | `authorized_signatory.revoked_date` | DATE | C | — | Required when status = REVOKED. |
| 14 | Revoked Reason | `authorized_signatory.revoked_reason` | TEXT | C | 1000 | Required when status = REVOKED. |
| 15 | Approved By | `authorized_signatory.approved_by` | FK → `auth.users` | R | — | Quality Manager or Managing Director who approved the delegation. |
| 16 | Notes | `authorized_signatory.notes` | TEXT | O | 2000 | Free text. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-011-03-001 | training_date | Range | Must be <= `delegation_date`. | "Training must be completed before authority can be delegated." |
| VR-011-03-002 | pki_cert_ref | Conditional | Required when `signature_method` = INTERNAL_PKI. | "PKI certificate reference required for internal PKI signing." |
| VR-011-03-003 | revoked_date, revoked_reason | Conditional | Required when `status` = REVOKED. | "Revocation date and reason required." |
| VR-011-03-004 | (user_id) | Uniqueness | One active signatory record per user. Cannot have duplicate ACTIVE entries. | "User already has an active signatory record." |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **OUT** → | FM-011-01 (CoC Register) | FM-011-01 validates that the signer is in this register with ACTIVE status and sufficient authority level. |

---

## 12. PR-012 Forms — MRB Assembly and Release

### 12.1 FM-012-01: MRB Assembly Checklist (Prerequisites)

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-012-01 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-012 — MRB Assembly and Release |
| **Industry** | BOTH |
| **Pipeline Stage** | MRB Assembly |
| **DB Entity** | `mrb.assembly_checklist` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Verification that all prerequisites are met before MRB assembly begins. Checks that order state is correct, all documents are validated, CoC is issued, no critical NCRs are open, and the MRB Index is ready for finalization. This is a gate between validation and assembly.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Checklist ID | `assembly_checklist.checklist_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | MRB Reference | `assembly_checklist.mrb_id` | FK → `mrb` | R | — | Which MRB is being assembled. |
| 3 | Order Reference | (derived) | FK → `order` | A | — | Auto-populated. Read-only. |
| 4 | **Check 1: Order State** | `assembly_checklist.check_order_state` | ENUM (PASS / FAIL) | A | — | Auto-calculated. PASS if order state = COC_SIGNED. |
| 5 | **Check 2: All Docs Validated** | `assembly_checklist.check_docs_validated` | ENUM (PASS / FAIL) | A | — | Auto-calculated from MRB Index. PASS if all required items VALIDATED or WAIVED. |
| 6 | Docs Outstanding | `assembly_checklist.docs_outstanding` | INTEGER | A | — | Count of unvalidated documents. |
| 7 | **Check 3: CoC Issued** | `assembly_checklist.check_coc_issued` | ENUM (PASS / FAIL) | A | — | Auto-calculated. PASS if active CoC exists for this MRB. |
| 8 | CoC Number | (derived) | VARCHAR(25) | A | 25 | Auto-populated if CoC exists. |
| 9 | **Check 4: No Critical NCRs** | `assembly_checklist.check_no_ncr` | ENUM (PASS / FAIL) | A | — | Auto-calculated. PASS if no open, unresolved nonconformance reports. |
| 10 | **Check 5: MRB Index Ready** | `assembly_checklist.check_index_ready` | ENUM (PASS / FAIL) | A | — | Auto-calculated. PASS if index can transition to FINAL. |
| 11 | **Overall Result** | `assembly_checklist.overall_result` | ENUM (PASS / FAIL) | A | — | PASS only if all checks pass. |
| 12 | Evaluated By | `assembly_checklist.evaluated_by` | FK → `auth.users` | A | — | Auto-populated. |
| 13 | Evaluated At | `assembly_checklist.evaluated_at` | TIMESTAMP | A | — | Auto-populated. |
| 14 | Notes | `assembly_checklist.notes` | TEXT | O | 2000 | Free text. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-012-01-001 | overall_result | Calculation | PASS only when all 5 checks pass. | "MRB assembly prerequisites not met: {failing checks}." |
| VR-012-01-002 | (on PASS) | Trigger | Order state transitions: `COC_SIGNED` → `MRB_ASSEMBLY`. MRB Index state transitions: `LIVE` → `FINAL`. | (System action.) |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-011-01 (CoC Register) | Check 3 verifies CoC exists and is ACTIVE. |
| **IN** ← | FM-009-04 (MRB Index) | Check 2 and Check 5 verify all documents validated and index ready. |
| **OUT** → | FM-012-02 (Quality Check) | Assembly checklist PASS triggers MRB assembly and subsequent quality check. |

---

### 12.2 FM-012-02: MRB Quality Check and Release Record

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-012-02 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-012 — MRB Assembly and Release |
| **Industry** | BOTH |
| **Pipeline Stage** | MRB Assembly → Release |
| **DB Entity** | `mrb.quality_check` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

10-point quality check performed on the assembled MRB package before release. Verifies page count, bookmarks, legibility, cover page, index accuracy, section order, CoC presence, serial number correctness, completeness, and overall professional quality. The final quality gate before the MRB is delivered to the customer.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Quality Check ID | `quality_check.check_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | MRB Reference | `quality_check.mrb_id` | FK → `mrb` | R | — | Which assembled MRB. |
| 3 | MRB PDF URI | (from MRB) | VARCHAR(500) | A | 500 | Storage path to the assembled MRB PDF/A-3. Auto-populated. |
| 4 | MRB PDF Checksum | (from MRB) | VARCHAR(64) | A | 64 | SHA-256 of the assembled PDF. Auto-populated. |
| 5 | Total Page Count | `quality_check.page_count` | INTEGER | R | — | Verified page count of assembled MRB. |
| 6 | **QC-1: Page Count Correct** | `quality_check.qc_page_count` | ENUM (PASS / FAIL) | R | — | Verified page count matches expected (from MRB Index page ranges). |
| 7 | **QC-2: Bookmarks Present** | `quality_check.qc_bookmarks` | ENUM (PASS / FAIL) | R | — | PDF bookmarks exist for each section and major document. |
| 8 | **QC-3: All Pages Legible** | `quality_check.qc_legibility` | ENUM (PASS / FAIL) | R | — | No blank pages, no truncated text, no unreadable scans. |
| 9 | **QC-4: Cover Page Correct** | `quality_check.qc_cover` | ENUM (PASS / FAIL) | R | — | Cover page has correct customer, PO, part number, MRB number. |
| 10 | **QC-5: Index Matches Content** | `quality_check.qc_index` | ENUM (PASS / FAIL) | R | — | MRB Index page numbers match actual document locations. |
| 11 | **QC-6: Section Order Correct** | `quality_check.qc_section_order` | ENUM (PASS / FAIL) | R | — | Sections appear in correct sequence (1→7 or 1→8). |
| 12 | **QC-7: CoC Present and Signed** | `quality_check.qc_coc` | ENUM (PASS / FAIL) | R | — | CoC is included, signature is visible, CoC number matches register. |
| 13 | **QC-8: Serial Numbers Correct** | `quality_check.qc_serials` | ENUM (PASS / FAIL) | R | — | Serial numbers on CoC match traceability matrix and inspection reports. |
| 14 | **QC-9: Completeness** | `quality_check.qc_completeness` | ENUM (PASS / FAIL) | R | — | Every required SDRL line item has a corresponding document in the MRB. |
| 15 | **QC-10: Professional Quality** | `quality_check.qc_professional` | ENUM (PASS / FAIL) | R | — | Overall presentation quality: consistent formatting, no watermarks, no draft marks. |
| 16 | Corrective Actions | `quality_check.corrective_actions` | TEXT | C | 3000 | Required if any QC check = FAIL. Describes what was corrected and re-checked. |
| 17 | **Overall Result** | `quality_check.overall_result` | ENUM (PASS / FAIL) | R | — | PASS only if all 10 checks pass (after corrections if any). |
| 18 | **Release Type** | `quality_check.release_type` | ENUM(`release_type`) | R | — | STANDARD (routine) or ELEVATED (high-value, Defence, customer-specified). Elevated requires additional approver. |
| 19 | Released By | `quality_check.released_by` | FK → `auth.users` | R | — | QA Engineer or Quality Manager. |
| 20 | Released At | `quality_check.released_at` | TIMESTAMP | A | — | System timestamp. |
| 21 | Elevated Approver | `quality_check.elevated_approver` | FK → `auth.users` | C | — | Required when `release_type` = ELEVATED. Must be Quality Manager. |
| 22 | Elevated Approved At | `quality_check.elevated_approved_at` | TIMESTAMP | C | — | When elevated approval was granted. |
| 23 | Notes | `quality_check.notes` | TEXT | O | 2000 | Free text. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-012-02-001 | corrective_actions | Conditional | Required if any QC check = FAIL. | "Corrective actions required for failed quality checks." |
| VR-012-02-002 | overall_result | Consistency | Cannot be PASS if any QC check is still FAIL (must re-check after correction). | "Overall cannot pass with failing quality checks." |
| VR-012-02-003 | elevated_approver | Conditional | Required when `release_type` = ELEVATED. | "Elevated release requires Quality Manager approval." |
| VR-012-02-004 | (on PASS) | Trigger | Order state: `MRB_ASSEMBLY` → `MRB_RELEASED`. MRB is now ready for delivery. | (System action.) |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-012-01 (Assembly Checklist) | Assembly checklist PASS triggers MRB assembly and this quality check. |
| **OUT** → | FM-012-03 (Customer Pre-Shipment Approval) | If contract requires customer review before shipment. |
| **OUT** → | FM-012-04 (Delivery Confirmation) | After quality check PASS and optional customer approval. |

---

### 12.3 FM-012-03: Customer Pre-Shipment Approval Record

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-012-03 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-012 — MRB Assembly and Release |
| **Industry** | BOTH (when contractually required) |
| **Pipeline Stage** | MRB Release (conditional) |
| **DB Entity** | `mrb.customer_approval` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Documents customer review and approval of the MRB before shipment, when required by contract. Records submission date, customer comments, required changes, and final approval. Not all orders require this — only when the SDRL or contract specifies pre-shipment review.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Approval Record ID | `customer_approval.approval_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | MRB Reference | `customer_approval.mrb_id` | FK → `mrb` | R | — | Which MRB. |
| 3 | Customer | (derived) | VARCHAR(200) | A | 200 | Auto-populated. Read-only. |
| 4 | MRB Submitted To Customer | `customer_approval.submitted_at` | TIMESTAMP | R | — | When the MRB was sent to customer for review. |
| 5 | Submission Method | `customer_approval.submission_method` | ENUM (PORTAL / EMAIL / PHYSICAL) | R | — | How MRB was delivered for review. |
| 6 | Customer Acknowledged Date | `customer_approval.acknowledged_at` | TIMESTAMP | O | — | When customer confirmed receipt. |
| 7 | Customer Comments | `customer_approval.customer_comments` | TEXT | O | 3000 | Customer feedback or requested changes. |
| 8 | Changes Required | `customer_approval.changes_required` | BOOLEAN | R | — | True if customer requests changes before approval. |
| 9 | Changes Description | `customer_approval.changes_description` | TEXT | C | 2000 | Required if `changes_required` = true. What changes were requested. |
| 10 | Changes Implemented | `customer_approval.changes_implemented` | BOOLEAN | C | — | Required if `changes_required` = true. Whether changes have been made. |
| 11 | **Customer Approval Status** | `customer_approval.approval_status` | ENUM (PENDING / APPROVED / CONDITIONALLY_APPROVED / REJECTED) | R | — | Final customer decision. |
| 12 | Customer Approval Reference | `customer_approval.approval_reference` | VARCHAR(100) | C | 100 | Customer's approval document/email reference. Required when APPROVED. |
| 13 | Customer Approver Name | `customer_approval.approver_name` | VARCHAR(200) | C | 200 | Who approved. Required when APPROVED. |
| 14 | Approval Date | `customer_approval.approved_at` | TIMESTAMP | C | — | When approved. Required when APPROVED. |
| 15 | MRB Version Delivered | `customer_approval.mrb_version` | VARCHAR(10) | R | 10 | Version of MRB reviewed and approved. |
| 16 | Notes | `customer_approval.notes` | TEXT | O | 2000 | Free text. |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-012-02 (Quality Check) | Quality check PASS required before customer review. |
| **OUT** → | FM-012-04 (Delivery Confirmation) | Customer approval (when required) must precede final delivery. |

---

### 12.4 FM-012-04: MRB Delivery Confirmation

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-012-04 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-012 — MRB Assembly and Release |
| **Industry** | BOTH |
| **Pipeline Stage** | MRB Delivery |
| **DB Entity** | `mrb.delivery_confirmation` |
| **Retention** | Per industry default: 25 years (Oil & Gas), 30 years (Defence). Minimum ≥ 20 years. May be extended per customer contract. |

#### Purpose

Records delivery of the MRB with the product shipment. Confirms both physical and electronic delivery as applicable. Captures tracking references and recipient confirmation. This is the final operational record before archival (PR-013).

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Delivery ID | `delivery_confirmation.delivery_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | MRB Reference | `delivery_confirmation.mrb_id` | FK → `mrb` | R | — | Which MRB. |
| 3 | Order Reference | (derived) | FK → `order` | A | — | Auto-populated. Read-only. |
| 4 | Customer | (derived) | VARCHAR(200) | A | 200 | Auto-populated. Read-only. |
| 5 | Shipment Date | `delivery_confirmation.shipped_at` | TIMESTAMP | R | — | When product and MRB shipped. |
| 6 | **Delivery Method** | `delivery_confirmation.delivery_method` | ENUM(`delivery_method`) | R | — | PHYSICAL (printed with product), ELECTRONIC (portal/email), BOTH. |
| 7 | Physical Tracking Reference | `delivery_confirmation.physical_tracking` | VARCHAR(100) | C | 100 | Required when method = PHYSICAL or BOTH. Shipping tracking number. |
| 8 | Electronic Delivery URI | `delivery_confirmation.electronic_uri` | VARCHAR(500) | C | 500 | Required when method = ELECTRONIC or BOTH. Portal link or email reference. |
| 9 | Recipient Name | `delivery_confirmation.recipient_name` | VARCHAR(200) | R | 200 | Customer receiving contact. |
| 10 | Recipient Confirmed | `delivery_confirmation.recipient_confirmed` | BOOLEAN | O | — | Whether customer confirmed receipt. |
| 11 | Receipt Confirmation Date | `delivery_confirmation.confirmed_at` | TIMESTAMP | C | — | When customer confirmed. |
| 12 | MRB PDF Checksum | `delivery_confirmation.mrb_checksum` | VARCHAR(64) | A | 64 | SHA-256 of the delivered MRB PDF. Auto-populated. Ensures integrity. |
| 13 | Delivered By | `delivery_confirmation.delivered_by` | FK → `auth.users` | R | — | Who dispatched the delivery. |
| 14 | Notes | `delivery_confirmation.notes` | TEXT | O | 2000 | Free text. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-012-04-001 | physical_tracking | Conditional | Required when `delivery_method` = PHYSICAL or BOTH. | "Physical tracking reference required for physical delivery." |
| VR-012-04-002 | electronic_uri | Conditional | Required when `delivery_method` = ELECTRONIC or BOTH. | "Electronic delivery reference required for electronic delivery." |
| VR-012-04-003 | (on save) | Trigger | Order state: `MRB_RELEASED` → `SHIPPED`. Triggers archive record creation (FM-013-01). | (System action.) |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-012-02 (Quality Check) | MRB must be released (quality check PASS) before delivery. |
| **IN** ← | FM-012-03 (Customer Approval) | If pre-shipment approval required, must be APPROVED before delivery. |
| **OUT** → | FM-013-01 (Archive Register) | Delivery triggers archival process. |

---

## 13. PR-013 Forms — Document Archival and Retention

### 13.1 FM-013-01: Archive Register

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-013-01 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-013 — Document Archival and Retention |
| **Industry** | BOTH |
| **Pipeline Stage** | Archive |
| **DB Entity** | `mrb.archive_record` |
| **Retention** | Permanent (lifetime of company) |

#### Purpose

Master record of all archived MRBs. Permanent registry with complete metadata for each archived package. Tracks archive location, retention periods, backup status, and integrity checksums. One record per archived MRB.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Archive ID | `archive_record.archive_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | MRB Reference | `archive_record.mrb_id` | FK → `mrb` | R | — | Which MRB is archived. |
| 3 | MRB Number | (derived) | VARCHAR(30) | A | 30 | Auto-populated. Read-only. |
| 4 | CoC Number | (derived from MRB) | VARCHAR(25) | A | 25 | Auto-populated. Read-only. |
| 5 | Order Reference | (derived) | FK → `order` | A | — | Auto-populated. Read-only. |
| 6 | PO Number | (derived) | VARCHAR(50) | A | 50 | Auto-populated. Read-only. |
| 7 | Customer | (derived) | VARCHAR(200) | A | 200 | Auto-populated. Read-only. |
| 8 | Industry Classification | (from order) | ENUM(`industry_class`) | A | — | Auto-populated. Read-only. |
| 9 | Ship Date | `archive_record.ship_date` | DATE | A | — | Auto-populated from FM-012-04. Read-only. |
| 10 | Archive Date | `archive_record.archive_date` | TIMESTAMP | A | — | System timestamp. Auto-populated. |
| 11 | **Retention Period (Years)** | `archive_record.retention_years` | INTEGER | R | — | Minimum retention. Default: 25 years for Oil & Gas, 30 years for Defence. Minimum ≥ 20 years. May be extended per customer contract or regulatory requirement. Typical equipment lifetime is 20–30 years. |
| 12 | Retention Expiry | `archive_record.retention_expiry` | DATE | A | — | Auto-calculated: `archive_date` + `retention_years`. |
| 13 | Legal Hold | `archive_record.legal_hold` | BOOLEAN | R | — | True if record is under legal hold (cannot be disposed regardless of expiry). |
| 14 | Legal Hold Reason | `archive_record.legal_hold_reason` | TEXT | C | 1000 | Required if `legal_hold` = true. |
| 15 | **Archive Tier** | `archive_record.archive_tier` | ENUM(`archive_tier`) | R | — | ACTIVE (readily accessible, first 2 years) or DEEP (cold storage, after 2 years). |
| 16 | Archive URI | `archive_record.archive_uri` | VARCHAR(500) | A | 500 | Supabase Storage path. Auto-populated. Read-only. |
| 17 | Backup URI | `archive_record.backup_uri` | VARCHAR(500) | A | 500 | Secondary backup location (AWS eu-west-1). Auto-populated. |
| 18 | **MRB Checksum** | `archive_record.checksum_sha256` | VARCHAR(64) | A | 64 | SHA-256 of the archived MRB package. Auto-calculated. |
| 19 | File Size (KB) | `archive_record.file_size_kb` | INTEGER | A | — | Auto-calculated. Read-only. |
| 20 | Last Integrity Check | `archive_record.last_integrity_check` | TIMESTAMP | O | — | Updated by FM-013-05 (Annual Integrity Report). |
| 21 | Integrity Status | `archive_record.integrity_status` | ENUM (VERIFIED / UNVERIFIED / FAILED) | A | — | Updated by annual integrity check. |
| 22 | Archived By | `archive_record.archived_by` | FK → `auth.users` | A | — | Auto-populated. |
| 23 | Notes | `archive_record.notes` | TEXT | O | 2000 | Free text. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-013-01-001 | legal_hold_reason | Conditional | Required when `legal_hold` = true. | "Legal hold reason required." |
| VR-013-01-002 | retention_years | Range | Must be >= 20. | "Minimum retention period is 20 years." |
| VR-013-01-003 | (on create) | Trigger | Order state: `SHIPPED` → `ARCHIVED`. | (System action.) |
| VR-013-01-004 | checksum_sha256 | Integrity | Must match the checksum recorded at MRB release (FM-012-02). | "Archive checksum mismatch — file integrity compromised." |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-012-04 (Delivery Confirmation) | Shipment triggers archive record creation. |
| **OUT** → | FM-013-02 (Access Log) | All archive accesses logged. |
| **OUT** → | FM-013-03 (Disposition Request) | At retention expiry. |
| **OUT** → | FM-013-05 (Annual Integrity Report) | Sampled during annual check. |

---

### 13.2 FM-013-02: Archive Access Log

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-013-02 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-013 — Document Archival and Retention |
| **Industry** | BOTH |
| **Pipeline Stage** | Archive (ongoing) |
| **DB Entity** | `mrb.audit_log` (filtered for archive access events) |
| **Retention** | 10 years |

#### Purpose

Logs every access or retrieval of archived records. Maintains an audit trail of who accessed which MRB records, when, and for what purpose.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Access Log ID | `audit_log.log_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Archive Record | `audit_log.entity_id` | FK → `archive_record` | A | — | Which archived MRB was accessed. |
| 3 | MRB Number | (derived) | VARCHAR(30) | A | 30 | Auto-populated. Read-only. |
| 4 | Requester | `audit_log.user_id` | FK → `auth.users` | A | — | Who accessed the record. Auto-populated. |
| 5 | Access Timestamp | `audit_log.timestamp` | TIMESTAMP | A | — | When access occurred. Auto-populated. |
| 6 | Access Purpose | `audit_log.details.purpose` | VARCHAR(500) | R | 500 | Why the record was accessed. E.g., "Customer re-delivery request", "Warranty claim investigation". |
| 7 | Retrieval Method | `audit_log.details.method` | ENUM (ELECTRONIC / PHYSICAL) | R | — | How the record was retrieved. |
| 8 | IP Address | `audit_log.ip_address` | VARCHAR(45) | A | 45 | Auto-captured. Read-only. |

#### Validation Rules

- All fields auto-populated except `purpose` and `method`. These are required on access.
- Access log entries are immutable — no editing or deletion.

---

### 13.3 FM-013-03: Disposition Request

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-013-03 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-013 — Document Archival and Retention |
| **Industry** | BOTH |
| **Pipeline Stage** | Retention Expiry |
| **DB Entity** | `mrb.disposition_request` |
| **Retention** | 10 years after disposition |

#### Purpose

Formal request to dispose of (destroy) archived records after their retention period expires. Requires Quality Manager approval. Cannot be initiated while records are under legal hold.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Request ID | `disposition_request.request_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Archive Records | `disposition_request.archive_ids` | UUID[] | R | — | Array of archive record IDs to be disposed. |
| 3 | Record Count | (calculated) | INTEGER | A | — | Number of records in request. |
| 4 | MRB Numbers | (derived) | TEXT | A | — | List of MRB numbers. Auto-populated. Read-only. |
| 5 | Original Retention Period | (from archive) | INTEGER | A | — | Years. Auto-populated. Read-only. |
| 6 | Retention Expiry Date | (from archive) | DATE | A | — | Auto-populated. Must be in the past. |
| 7 | Legal Hold Check | (calculated) | ENUM (CLEAR / BLOCKED) | A | — | Auto-calculated. BLOCKED if any record has `legal_hold` = true. |
| 8 | Justification | `disposition_request.justification` | TEXT | R | 2000 | Why disposition is appropriate. |
| 9 | **Status** | `disposition_request.status` | ENUM (PENDING / APPROVED / REJECTED) | R | — | Quality Manager decision. |
| 10 | Approved By | `disposition_request.approved_by` | FK → `auth.users` | C | — | Quality Manager. Required when APPROVED. |
| 11 | Approved At | `disposition_request.approved_at` | TIMESTAMP | C | — | When approved. |
| 12 | Rejection Reason | `disposition_request.rejection_reason` | TEXT | C | 1000 | Required when REJECTED. |
| 13 | Requested By | `disposition_request.requested_by` | FK → `auth.users` | A | — | Auto-populated. |
| 14 | Requested At | `disposition_request.requested_at` | TIMESTAMP | A | — | Auto-populated. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-013-03-001 | retention_expiry | Prerequisite | All records must have retention_expiry in the past. | "Cannot dispose records before retention period expires." |
| VR-013-03-002 | legal_hold_check | Block | If any record has `legal_hold` = true, request is blocked. | "Cannot dispose records under legal hold." |
| VR-013-03-003 | approved_by | Authorization | Must have Quality Manager role. | "Only Quality Manager can approve disposition." |

#### Cross-Form References

| Direction | Form | Relationship |
|-----------|------|-------------|
| **IN** ← | FM-013-01 (Archive Register) | Archive records provide retention dates and legal hold status. |
| **OUT** → | FM-013-04 (Disposition Record) | Approved request triggers actual disposition. |

---

### 13.4 FM-013-04: Disposition Record

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-013-04 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-013 — Document Archival and Retention |
| **Industry** | BOTH |
| **Pipeline Stage** | Retention Expiry (post-approval) |
| **DB Entity** | `mrb.disposition_record` |
| **Retention** | 10 years after disposition |

#### Purpose

Documents the actual destruction/disposal of expired records after Quality Manager approval (FM-013-03). Records the destruction method, date, and certification of completion. Creates an immutable audit trail proving that records were properly disposed.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Disposition Record ID | `disposition_record.record_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Disposition Request | `disposition_record.request_id` | FK → `disposition_request` | R | — | Links to approved request. |
| 3 | Archive Records Destroyed | `disposition_record.archive_ids` | UUID[] | A | — | Auto-populated from request. |
| 4 | MRB Numbers Destroyed | (derived) | TEXT | A | — | List. Read-only. |
| 5 | **Destruction Method** | `disposition_record.method` | ENUM(`disposition_method`) | R | — | SECURE_DELETE (cryptographic erasure) or CRYPTO_SHRED (key destruction). |
| 6 | Destruction Date | `disposition_record.destroyed_at` | TIMESTAMP | R | — | When destruction was executed. |
| 7 | Primary Storage Destroyed | `disposition_record.primary_destroyed` | BOOLEAN | R | — | Confirmed primary storage cleared. |
| 8 | Backup Storage Destroyed | `disposition_record.backup_destroyed` | BOOLEAN | R | — | Confirmed backup storage cleared. |
| 9 | **Completion Certification** | `disposition_record.certification` | TEXT | R | 1000 | Written statement certifying complete destruction. |
| 10 | Destroyed By | `disposition_record.destroyed_by` | FK → `auth.users` | R | — | System admin or authorized person. |
| 11 | Witnessed By | `disposition_record.witnessed_by` | FK → `auth.users` | R | — | Second person verifying destruction. |
| 12 | Notes | `disposition_record.notes` | TEXT | O | 2000 | Free text. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-013-04-001 | primary_destroyed, backup_destroyed | Completeness | Both must be true for certification. | "Both primary and backup storage must be confirmed destroyed." |
| VR-013-04-002 | witnessed_by | Different person | Must differ from `destroyed_by`. | "Witness must be a different person than the destroyer." |
| VR-013-04-003 | (on save) | Trigger | Archive records marked as DISPOSED. Archive register updated. | (System action.) |

---

### 13.5 FM-013-05: Annual Archive Integrity Report

#### Document Control

| Field | Value |
|-------|-------|
| **Form ID** | FM-013-05 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Procedure** | PR-013 — Document Archival and Retention |
| **Industry** | BOTH |
| **Pipeline Stage** | Archive (annual) |
| **DB Entity** | `mrb.integrity_report` |
| **Retention** | 10 years |

#### Purpose

Annual verification that archived records remain intact and readable. Performs random sampling, checksum verification, readability checks, backup verification, and metadata accuracy assessment. Required by PR-013 to ensure long-term archive integrity.

#### Field Definitions

| # | Field | DB Column | Type | Req | Limit | Description |
|---|-------|-----------|------|-----|-------|-------------|
| 1 | Report ID | `integrity_report.report_id` | UUID | A | — | Primary key. Auto-generated. |
| 2 | Report Year | `integrity_report.report_year` | INTEGER | R | — | Calendar year being reported (e.g., 2026). |
| 3 | Report Date | `integrity_report.report_date` | DATE | R | — | Date report was completed. |
| 4 | Total Archive Records | `integrity_report.total_records` | INTEGER | A | — | Count of all active archive records. Auto-calculated. |
| 5 | **Sample Size** | `integrity_report.sample_size` | INTEGER | R | — | Number of records sampled. Minimum: 10% of archive or 20 records, whichever is greater. |
| 6 | Sampled MRB Numbers | `integrity_report.sampled_mrbs` | JSONB | R | — | Array of MRB numbers sampled: `["AM-MRB-2026-00001", "AM-MRB-2026-00015", ...]`. |
| 7 | **Checksum Verification Results** | `integrity_report.checksum_results` | JSONB | R | — | Per-sample: `[{"mrb_number": "...", "stored_checksum": "...", "computed_checksum": "...", "result": "MATCH"}]`. |
| 8 | Checksum Matches | `integrity_report.checksum_match_count` | INTEGER | A | — | Auto-calculated. |
| 9 | Checksum Failures | `integrity_report.checksum_fail_count` | INTEGER | A | — | Auto-calculated. |
| 10 | **Readability Verification** | `integrity_report.readability_results` | JSONB | R | — | Per-sample: `[{"mrb_number": "...", "pdf_opens": true, "text_searchable": true, "pages_intact": true, "result": "PASS"}]`. |
| 11 | Readability Pass Count | `integrity_report.readability_pass_count` | INTEGER | A | — | Auto-calculated. |
| 12 | **Backup Verification** | `integrity_report.backup_verified` | BOOLEAN | R | — | Confirms backup copies exist and match primary. |
| 13 | Backup Location Verified | `integrity_report.backup_location` | VARCHAR(200) | R | 200 | Backup storage location confirmed accessible. |
| 14 | **Metadata Accuracy** | `integrity_report.metadata_accurate` | BOOLEAN | R | — | Archive register metadata matches actual file contents (spot check). |
| 15 | Issues Found | `integrity_report.issues` | JSONB | O | — | Array of any problems: `[{"mrb_number": "...", "issue": "Checksum mismatch", "severity": "CRITICAL", "remediation": "Restored from backup"}]`. |
| 16 | Remediation Actions | `integrity_report.remediation` | TEXT | C | 3000 | Required if any issues found. What was done to fix problems. |
| 17 | **Overall Result** | `integrity_report.overall_result` | ENUM (PASS / PASS_WITH_ISSUES / FAIL) | R | — | PASS = no issues. PASS_WITH_ISSUES = minor issues remediated. FAIL = critical integrity failure. |
| 18 | Verified By | `integrity_report.verified_by` | FK → `auth.users` | R | — | QA Engineer or system administrator. |
| 19 | Approved By | `integrity_report.approved_by` | FK → `auth.users` | R | — | Quality Manager reviews and approves report. |
| 20 | Notes | `integrity_report.notes` | TEXT | O | 2000 | Free text. |

#### Validation Rules

| Rule ID | Field(s) | Rule Type | Condition | Error |
|---------|----------|-----------|-----------|-------|
| VR-013-05-001 | sample_size | Minimum | Must be >= MAX(total_records * 0.10, 20). | "Sample size must be at least 10% of archive or 20 records." |
| VR-013-05-002 | remediation | Conditional | Required if any issues found. | "Remediation actions required for identified issues." |
| VR-013-05-003 | (on FAIL) | Escalation | Critical integrity failure triggers immediate notification to Quality Manager and management. | Alert: "Archive integrity failure detected." |
| VR-013-05-004 | (on save) | Update | Updates `archive_record.last_integrity_check` and `integrity_status` for all sampled records. | (System action.) |

---

## 14. Auto-Population Source Matrix

Master cross-reference showing which database entities feed each form. Each row is a form, columns show the source entities.

| Form ID | Form Name | Primary DB Entity | Source Entities (auto-population) |
|---------|-----------|-------------------|----------------------------------|
| FM-008-01 | Material Gate Checklist ★ | `mrb.gate_review` | `material_receipt`, `material_requirement_profile`, `order`, `customer`, `supplier`, `auth.users` |
| FM-008-02 | Physical Inspection Report | `mrb.physical_inspection` | `gate_review`, `material_receipt`, `order` |
| FM-008-03 | Traceability Matrix | `mrb.material_traceability` | `material_receipt`, `gate_review`, `physical_inspection`, `order`, `customer` |
| FM-008-04 | Material Requirement Profile | `mrb.material_requirement_profile` | `customer` |
| FM-009-01 | Order Requirement Matrix ★ | `mrb.sdrl` + `mrb.sdrl_line_item` | `order`, `customer`, AM-CT-001 templates |
| FM-009-02 | ITP Tracker | `mrb.itp_tracker` + `mrb.itp_point` | `order`, `customer` |
| FM-009-03 | MRB Initialization | `mrb.mrb` | `order`, `sdrl`, `sdrl_line_item`, `customer` |
| FM-009-04 | MRB Index ★ | View: `sdrl_line_item` ⋈ `mrb_document` ⋈ `validation` | `sdrl_line_item`, `mrb_document`, `validation`, routing table |
| FM-010-01 | Correction Request ★ | `mrb.correction_request` | `mrb_document`, `validation`, `mrb`, `order`, `customer`, `sdrl_line_item` |
| FM-010-02 | Document Validation Log | `mrb.validation` | `mrb_document`, `mrb`, `order` |
| FM-010-03 | Traceability Verification | `mrb.traceability_verification` | `material_traceability`, `mrb_document`, `order` |
| FM-010-04 | CoC Prerequisite Gate | `mrb.coc_prerequisite_gate` | `mrb`, `mrb_document`, `correction_request`, `traceability_verification`, `itp_point`, `gate_review` |
| FM-011-01 | CoC Register | `mrb.coc` | `mrb`, `order`, `customer`, `material_traceability`, `coc_prerequisite_gate`, `authorized_signatory` |
| FM-011-02 | CoC Revision/Void | `mrb.coc_revision` | `coc` |
| FM-011-03 | Authorized Signatory Register | `mrb.authorized_signatory` | `auth.users` |
| FM-012-01 | Assembly Checklist | `mrb.assembly_checklist` | `mrb`, `mrb_document`, `coc`, `correction_request` |
| FM-012-02 | Quality Check | `mrb.quality_check` | `mrb`, `coc` |
| FM-012-03 | Customer Approval | `mrb.customer_approval` | `mrb`, `order`, `customer` |
| FM-012-04 | Delivery Confirmation | `mrb.delivery_confirmation` | `mrb`, `order`, `customer` |
| FM-013-01 | Archive Register | `mrb.archive_record` | `mrb`, `coc`, `order`, `customer`, `delivery_confirmation` |
| FM-013-02 | Archive Access Log | `mrb.audit_log` | `archive_record` |
| FM-013-03 | Disposition Request | `mrb.disposition_request` | `archive_record` |
| FM-013-04 | Disposition Record | `mrb.disposition_record` | `disposition_request`, `archive_record` |
| FM-013-05 | Annual Integrity Report | `mrb.integrity_report` | `archive_record` |

### New Database Entities Required (not in AM-TS-001 v1.1)

The following entities were identified during form template design and must be added to AM-TS-001 in the next revision:

| Entity | Form(s) | Purpose |
|--------|---------|---------|
| `mrb.physical_inspection` | FM-008-02 | PMI, visual, and dimensional inspection results |
| `mrb.material_traceability` + `detail` | FM-008-03 | Material-to-serial-number allocation tracking |
| `mrb.itp_tracker` + `mrb.itp_point` | FM-009-02 | ITP Hold/Witness/Review point tracking (O&G) |
| `mrb.traceability_verification` | FM-010-03 | Cross-document chain verification results |
| `mrb.coc_prerequisite_gate` | FM-010-04 | CoC prerequisite gate check results |
| `mrb.coc_revision` | FM-011-02 | CoC revision/void history |
| `mrb.authorized_signatory` | FM-011-03 | Signatory authority register |
| `mrb.assembly_checklist` | FM-012-01 | MRB assembly prerequisites |
| `mrb.quality_check` | FM-012-02 | MRB 10-point quality check |
| `mrb.customer_approval` | FM-012-03 | Customer pre-shipment approval |
| `mrb.delivery_confirmation` | FM-012-04 | MRB delivery tracking |
| `mrb.disposition_request` | FM-013-03 | Record disposition requests |
| `mrb.disposition_record` | FM-013-04 | Record destruction documentation |
| `mrb.integrity_report` | FM-013-05 | Annual archive integrity verification |

---

*End of AM-FM-001 — Form Template Specifications*
*24 forms defined across 6 procedures (PR-008 through PR-013)*
*Document revision: 1.0 — 21 February 2026*
