# CERTIFICATE OF CONFORMANCE

| Field | Value |
|-------|-------|
| **Document No.** | PR-011 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-19 |
| **Approved By** | Quality Manager |
| **Classification** | Internal |
| **ISO 9001 Clause** | 8.5.1, 8.6 |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-19 | Quality Manager | Initial Release |

---

## 1. Purpose

This procedure defines the generation, review, approval, and issuance of Certificates of Conformance (CoC) and Declarations of Conformity (DoC) for all manufacturing orders. The CoC is a legally binding document certifying that products conform to contractual requirements.

The CoC is generated ONLY after all MRB documents have been validated (per PR-010). It is the final quality declaration before the MRB is assembled (per PR-012).

## 2. Scope

This procedure applies to:

- All Certificates of Conformance for Defence/Aerospace deliveries (AS9100/AQAP 2110)
- All Certificates of Conformance for Oil & Gas/Energy deliveries (NORSOK/API)
- All Certificates of Conformance for Maritime and general engineering deliveries
- Declarations of Conformity (DoC) when required by regulation (CE marking, EU directives, export compliance)

## 3. References

| Document | Title |
|----------|-------|
| QM-001 | Quality Manual |
| PR-004 | Nonconformance and CAPA |
| PR-009 | SDRL Processing and MRB Management |
| PR-010 | Document Validation and Verification |
| PR-012 | MRB Assembly and Release |
| AS9100D | Quality Management Systems — Requirements for Aviation, Space, and Defence Organizations |
| AQAP 2110 | NATO Quality Assurance Requirements for Design, Development and Production |
| NORSOK M-650 | Qualification of Manufacturers |
| EN 10204:2004 | Metallic Products — Types of Inspection Documents |

## 4. Definitions

| Term | Definition |
|------|-----------|
| **CoC** | Certificate of Conformance — a legally binding document certifying that products conform to the requirements specified in the Purchase Order and referenced specifications |
| **DoC** | Declaration of Conformity — a regulatory compliance declaration required for CE marking, EU directives, or export regulations |
| **Conformance Statement** | The formal declaration section of the CoC listing all requirements to which the product conforms |
| **Authorized Signatory** | A person authorized by Aurelian Manufacturing to sign CoCs, documented in the Authorized Signatory Register |
| **Voided CoC** | A CoC that has been cancelled after issuance, retaining its number with "VOID" stamp |

## 5. Responsibilities

| Role | Responsibility |
|------|---------------|
| **Quality Manager** | Owns this procedure. Maintains the Authorized Signatory Register. Signs CoCs for critical/complex orders. Approves CoC template changes. |
| **QA Engineer** | Generates CoC from validated data. Performs pre-signature review. Signs CoCs within delegated authority. Maintains the CoC Register. |
| **Commercial Manager** | Reviews customer-specific CoC requirements during contract review (PR-007). Communicates CoC content disputes with customer. |
| **Production Manager** | Provides manufacturing data (serial numbers, quantities, batch records) required for CoC population. |

## 6. Procedure

### 6.1 Legal Significance

The Certificate of Conformance is a legally binding document. When an authorized representative signs the CoC, Aurelian Manufacturing AS:

- **Certifies** that ALL products listed conform to the specified requirements
- **Accepts liability** for the accuracy of all referenced documentation
- **Warrants** that the manufacturing process, materials, and inspections met contractual standards
- **Declares** compliance with applicable industry standards and regulations

A false or inaccurate CoC can result in:

- Contract breach and financial penalties
- Criminal liability (particularly in defence/aerospace for falsified records)
- Loss of quality certifications (AS9100, ISO 9001)
- Debarment from government/defence contracts
- Product liability exposure

### 6.2 CoC vs DoC

| Document | Full Name | Purpose | Scope |
|----------|-----------|---------|-------|
| **CoC** | Certificate of Conformance | Product conforms to PO/contract specifications | Specific to order/shipment |
| **DoC** | Declaration of Conformity | Product meets regulatory/directive requirements | CE marking, EU directives, export compliance |

Defence orders typically require BOTH a CoC (contractual compliance) and applicable DoCs (regulatory compliance). Oil & Gas orders primarily require a CoC with NORSOK compliance statements.

### 6.3 Prerequisite Gate

CoC generation SHALL NOT commence until PR-010 (Document Validation and Verification) confirms that all required documents are validated.

**The QA Engineer verifies the CoC Prerequisite Gate Checklist (Form FM-010-04) before proceeding.**

If any prerequisite is not met:

- CoC generation is BLOCKED
- QA Engineer identifies all blocking items
- No partial or conditional CoCs are generated
- Order state remains at VALIDATING until all prerequisites are satisfied

### 6.4 CoC Numbering Convention

```
FORMAT: AM-COC-[YYYY]-[NNNNN]

  AM       = Aurelian Manufacturing
  COC      = Certificate of Conformance
  YYYY     = Year of issue
  NNNNN    = Sequential number (5 digits, zero-padded)

EXAMPLES:
  AM-COC-2027-00001  (first CoC issued)
  AM-COC-2027-00002  (second CoC)
  AM-COC-2028-00001  (first CoC of 2028 — resets annually)

RULES:
  - Numbers are sequential and never reused
  - Voided CoCs retain their number with "VOID" stamp
  - Revised CoCs get a new number with reference to the superseded number
  - CoC Register maintained in ERP for audit trail
```

### 6.5 Defence Certificate of Conformance

#### 6.5.1 Template Content

The Defence CoC SHALL contain the following sections:

**A — Supplier Information:**

| Field | Source |
|-------|--------|
| Company name | Aurelian Manufacturing AS (constant) |
| Organization number | 835 679 632 (constant) |
| Address | Facility address, Valer, Ostfold, Norway (constant) |
| QMS standard | AS9100D / ISO 9001:2015 |
| AQAP reference | AQAP 2110 (if contractually required) |
| Certificate number | Auto-generated per Section 6.4 |

**B — Customer Information:**

| Field | Source |
|-------|--------|
| Customer name | From PO / SDRL (PR-009) |
| Purchase Order number | From PO |
| PO date | From PO |
| Contract reference | From PO (if applicable) |

**C — Product Information:**

| Field | Source |
|-------|--------|
| Part number | From PO / drawing |
| Part name / description | From PO / drawing |
| Drawing number and revision | From PO / drawing |
| Material specification | From PO / drawing |
| Quantity delivered | From manufacturing/shipping records |
| Serial numbers | From manufacturing records |

**D — Conformance Declaration:**

The conformance statement is built dynamically from the parsed SDRL requirements (PR-009):

- Purchase Order [PO number] and all referenced specifications
- Drawing [number, Rev X]
- Material Specification [specification]
- Quality Management System: AS9100D
- AQAP 2110 (if contractually required)
- First Article Inspection per AS9102 (if performed)
- [Additional customer-specific requirements as applicable]

**E — Material Traceability:**

| Field | Source |
|-------|--------|
| Material certificate type | EN 10204 Type 3.1 or 3.2 (from validated certificate) |
| Heat/lot numbers | From validated material certificates |
| Material supplier | From validated material certificates |

**F — Deviations/Concessions:**

- If NO deviations: "No deviations from specified requirements"
- If deviations exist: List each NCR number, customer-approved disposition reference

**G — Special Processes (if applicable):**

- List of special processes performed with certificate references

**H — Export Compliance (if applicable):**

- ITAR/EAR status
- ECCN classification
- Export license reference (if applicable)

**I — MRB Reference:**

- MRB number: AM-MRB-[YYYY]-[NNNNN]

**J — Authorized Signature:**

- Signature, name, title, date
- Authority statement: "This certificate is issued under the authority of Aurelian Manufacturing AS quality management system."

### 6.6 Oil & Gas Certificate of Conformance

#### 6.6.1 Template Content

The Oil & Gas CoC SHALL contain all sections A through E and J from Section 6.5, PLUS the following Oil & Gas-specific sections:

**K — Applicable Standards:**

- NORSOK M-650 (if applicable)
- API [specification number]
- ASME [section/standard]
- ASTM [standard]
- DNV [specification if applicable]
- Customer/project-specific specifications

**L — Testing Summary:**

For each test/inspection performed, reference the validated report:

- Dimensional inspection — Report reference
- NDT — Report reference (if applicable)
- Hydrostatic/pressure test — Report reference (if applicable)
- Functional test — Report reference (if applicable)
- Hardness test — Report reference (if applicable)
- PMI verification — Report reference (if applicable)

**M — NORSOK Compliance Statement:**

"Products manufactured in compliance with NORSOK requirements as specified in the purchase order. Material Data Sheets (MDS) per NORSOK M-630 enclosed where applicable."

**N — Preservation Status:**

- Preservation procedure reference
- Preservation validity date

**O — ITP Reference:**

- ITP document number
- ITP status: "All Hold/Witness/Review points completed"

**P — MRB/MDR Reference:**

- MDR number: AM-MRB-[YYYY]-[NNNNN]

### 6.7 Field Population Rules

| Population Method | Fields | Description |
|-------------------|--------|-------------|
| **AUTOMATIC** (from order data) | Supplier info, customer name, PO number, part number, drawing, material spec, quantity, serial numbers, applicable standards, CoC number, MRB number | Populated from parsed SDRL and manufacturing records |
| **FROM VALIDATED DOCUMENTS** (via PR-010) | Heat/lot numbers, material supplier, certificate type, test report references, PMI status, ITP reference, NCR/deviation references, FAIR reference, special process references | Extracted from documents that passed validation |
| **MANUAL** (human input required) | Authorized signatory name/title, signature, export classification (if not pre-determined), preservation details, customer-specific declarations | Requires human review and input |

### 6.8 Deviation Handling

All deviations accepted during manufacturing MUST be declared on the CoC:

1. QA Engineer queries PR-004 (NCR system) for all NCRs associated with the order
2. For each NCR with disposition "Use-as-is" or "Repair":
   - Verify customer approval exists (approval reference documented)
   - Include NCR number and disposition on CoC deviation section
3. NCRs with disposition "Rework" or "Scrap/Replace" are NOT listed (product was corrected)
4. If customer approval for a deviation is missing: CoC generation is BLOCKED

**Critical rule:** A CoC SHALL NOT declare "No deviations" if there are any use-as-is or repair dispositions on the order. This would be a false declaration.

### 6.9 Signature Authority

| Authority Level | Authorized To Sign | Conditions |
|----------------|-------------------|------------|
| **Level 1: Quality Manager** | All CoCs | No restrictions — full authority |
| **Level 2: Senior QA Engineer** | Standard and Oil & Gas CoCs | After training and documented delegation by Quality Manager |
| **Level 3: QA Engineer** | Standard (non-defence, non-critical) CoCs only | After training and documented delegation. Defence CoCs require Level 1 or 2. |

**Authorized Signatory Register:**

- Maintained by Quality Manager
- Lists each authorized person with name, title, authority level, signature specimen, and delegation date
- Updated when personnel changes occur
- Reviewed annually during Management Review (PR-003)

### 6.10 CoC Generation Workflow

**Step 1:** QA Engineer confirms CoC Prerequisite Gate (PR-010) is satisfied.

**Step 2:** QA Engineer selects applicable CoC template (Defence or Oil & Gas) based on order classification (PR-009).

**Step 3:** QA Engineer populates automatic fields from order data and manufacturing records.

**Step 4:** QA Engineer populates document reference fields from validated documents (PR-010).

**Step 5:** QA Engineer adds manual fields:
- Builds the conformance statement from SDRL requirements
- Adds deviation declarations (if any)
- Adds export compliance declarations (if applicable)
- Adds customer-specific declarations

**Step 6:** QA Engineer performs pre-signature review:
- All fields populated (no blanks)
- All references correct and traceable
- Conformance statement matches actual SDRL requirements
- Deviation section accurately reflects NCR status
- Serial numbers and quantities match manufacturing records

**Step 7:** QA Engineer presents CoC to authorized signatory for review and signature.

**Step 8:** Authorized signatory reviews CoC and:
- Signs the CoC (physical or qualified electronic signature)
- Date of signature recorded

**Step 9:** Signed CoC is:
- Registered in the CoC Register (Form FM-011-01)
- Filed in the MRB (Section 8 for Defence, Section 6 for Oil & Gas)
- Order state updated: COC_PENDING → MRB_ASSEMBLY
- Production Manager and Commercial Manager notified

**Step 10:** CoC is available for MRB assembly (PR-012).

### 6.11 CoC Revision and Voiding

**Revision:**

If a signed CoC requires correction (error discovered before shipment):

1. Original CoC is stamped "SUPERSEDED" with date and reference to new CoC
2. New CoC is generated with a NEW certificate number
3. New CoC states: "This certificate supersedes AM-COC-[old number]"
4. Both original and revised CoC are retained in the MRB
5. Reason for revision documented on Form FM-011-02

**Voiding:**

If a CoC must be cancelled (e.g., order cancelled after CoC signed):

1. Original CoC is stamped "VOID" with date and reason
2. Voided CoC is retained in records — never deleted
3. CoC Register updated to show voided status
4. Quality Manager approval required for voiding

### 6.12 Declarations of Conformity (DoC)

When regulatory DoCs are required (in addition to the CoC):

1. QA Engineer identifies applicable DoC requirements from the SDRL/contract
2. DoC template is selected based on the applicable regulation:
   - EU Declaration of Conformity (CE marking)
   - Export compliance declarations
   - Customer-specific regulatory declarations
3. DoC is populated with product and regulation-specific data
4. DoC is reviewed and signed by authorized signatory
5. DoC is included in MRB Section 8 (Defence) or Section 6 (Oil & Gas)

## 7. Records

| Form | Title | Retention |
|------|-------|-----------|
| FM-011-01 | CoC Register | Permanent (lifetime of company) |
| FM-011-02 | CoC Revision/Void Record | Per order archival requirement (minimum 15 years) |
| FM-011-03 | Authorized Signatory Register | Current + all previous versions (permanent) |

## 8. Key Performance Indicators

| KPI | Target | Measured |
|-----|--------|----------|
| CoC generation cycle time | < 4 hours from prerequisite gate clearance to signed CoC | Monthly |
| CoC first-time accuracy | > 95% of CoCs require no revision after signing | Monthly |
| CoC prerequisite gate wait time | < 1 business day from last document validated to CoC generated | Monthly |
| Post-shipment CoC corrections | 0 CoC corrections required by customer | Per incident |
| Deviation declaration accuracy | 100% of accepted deviations declared on CoC | Per order |

## 9. Flowchart

```
PR-010 confirms all documents validated
            │
            ▼
┌─────────────────────────┐
│ CoC Prerequisite Gate    │──BLOCKED──→ Return to PR-010
│ All sections validated?  │            Identify blocking items
└───────────┬─────────────┘
            │ PASS
            ▼
┌─────────────────────────┐
│ Select CoC template      │
│ (Defence / Oil & Gas)    │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Populate fields:         │
│ - Automatic (order data) │
│ - From validated docs    │
│ - Manual (declarations)  │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Pre-signature review     │──FAIL──→ Correct and re-review
│ All fields correct?      │
└───────────┬─────────────┘
            │ PASS
            ▼
┌─────────────────────────┐
│ Authorized signatory     │
│ reviews and signs CoC    │
└───────────┬─────────────┘
            │
            ▼
   Register in CoC Register
   File in MRB
   Update order state → MRB_ASSEMBLY
            │
            ▼
   Proceed to PR-012 (MRB Assembly)
```

## 10. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Prepared By | Quality Manager | _______ | _______ |
| Reviewed By | Production Manager | _______ | _______ |
| Approved By | Managing Director | _______ | _______ |

This document is controlled. Printed copies are uncontrolled unless stamped "CONTROLLED COPY" in red.
