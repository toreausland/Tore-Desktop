---
name: aurelian-coc-generator
description: Certificate of Conformance (CoC) generation skill for Aurelian Manufacturing's Digital MRB Builder system. Generates industry-specific Certificates of Conformance for Defence (AS9100/AQAP) and Oil & Gas (NORSOK/API) deliveries after all MRB documents are validated. Produces legally binding compliance declarations with full traceability to inspection data, material certificates, and manufacturing records. Use this skill when generating a CoC, preparing shipment documentation, creating compliance declarations, or any question about CoC content, format, signatures, or legal requirements. Triggers on "generate CoC", "certificate of conformance", "compliance certificate", "shipment certificate", "declaration of conformity", "DoC", "release certificate", "conformance declaration", "sign off order", "ready to ship", "final documentation", "export declaration", or any request to produce the formal compliance certificate for a manufacturing order.
---

# Aurelian Manufacturing — CoC Generator Skill

Generates legally binding Certificates of Conformance for Defence and Oil & Gas deliveries. The CoC is the final compliance declaration that accompanies every shipment, certifying that all products conform to the contractual requirements.

**Source document:** AM-SDRL-2026-001 Rev 1.0 — Shipment Documentation Requirements (SDRL/MRB), Appendix C: Certificate of Conformance Templates, located at `Quality System Input/Supplier Quality and Document requirements/Shipment_Documentation_Requirements_SDRL_MRB.pdf`

**Related MRB Builder skills:**
- `aurelian-sdrl-parser` — Provides order classification and requirement context
- `aurelian-doc-validator` — Must confirm all prerequisites BEFORE CoC generation
- `aurelian-mrb-builder` — Places the generated CoC in the final MRB package

---

## SECTION 1: COC FUNDAMENTALS

### 1.1 Legal Significance

The Certificate of Conformance is a **legally binding document**. When Aurelian's authorized representative signs the CoC, the company:

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

### 1.2 CoC vs DoC

| Document | Full Name | Purpose | Scope |
|----------|-----------|---------|-------|
| **CoC** | Certificate of Conformance | Product conforms to PO/contract specifications | Specific to order/shipment |
| **DoC** | Declaration of Conformity | Product meets regulatory/directive requirements | CE marking, EU directives, export compliance |

Defence orders typically require BOTH a CoC (contractual compliance) and applicable DoCs (regulatory compliance). Oil & Gas orders primarily require a CoC with NORSOK compliance statements.

---

## SECTION 2: PREREQUISITE GATE

### 2.1 Mandatory Pre-Generation Check

The CoC generator WILL NOT produce a certificate until `aurelian-doc-validator` confirms ALL prerequisites:

```
COC GENERATION GATE:

  QUERY aurelian-doc-validator FOR ORDER [order_id]:

  DEFENCE orders — ALL must be TRUE:
    ✅ MRB Section 1 (Identification) → VALIDATED
    ✅ MRB Section 2 (Contract Documentation) → VALIDATED
    ✅ MRB Section 3 (Material Documentation) → VALIDATED or N/A
    ✅ MRB Section 4 (Manufacturing Process) → VALIDATED
    ✅ MRB Section 5 (Special Processes) → VALIDATED or N/A
    ✅ MRB Section 6 (Inspection) → VALIDATED
    ✅ MRB Section 7 (Testing) → VALIDATED or N/A
    ✅ FAIR complete (if required) → VALIDATED
    ✅ No open CRITICAL NCRs → CONFIRMED
    ✅ All material certs validated → CONFIRMED
    ✅ Export compliance cleared → CONFIRMED (if applicable)

  OIL & GAS orders — ALL must be TRUE:
    ✅ MRB Section 1 (General Info) → VALIDATED
    ✅ MRB Section 2 (Purchase/Technical) → VALIDATED
    ✅ MRB Section 3 (Material Documentation) → VALIDATED
    ✅ MRB Section 4 (Manufacturing Records) → VALIDATED
    ✅ MRB Section 5 (Testing/Inspection) → VALIDATED
    ✅ All ITP Hold Points signed off → CONFIRMED
    ✅ All ITP Witness Points addressed → CONFIRMED
    ✅ PMI completed (if required) → VALIDATED
    ✅ Hydrostatic/pressure test (if required) → VALIDATED
    ✅ No open CRITICAL NCRs → CONFIRMED
    ✅ NORSOK MDS completed (if required) → CONFIRMED

  IF ANY prerequisite is FALSE:
    → BLOCK CoC generation
    → RETURN list of blocking items
    → DO NOT generate partial or conditional CoC
```

---

## SECTION 3: DEFENCE COC TEMPLATE

### 3.1 Defence Certificate of Conformance Format

Based on Appendix C of the source document, adapted for Aurelian Manufacturing:

```
╔══════════════════════════════════════════════════════════════════╗
║                CERTIFICATE OF CONFORMANCE                       ║
║                Defence / Aerospace                               ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  SUPPLIER INFORMATION                                            ║
║  ─────────────────────                                           ║
║  Company:        Aurelian Manufacturing AS                       ║
║  Org. Number:    835 679 632                                     ║
║  Address:        [Facility address, Valer, Ostfold, Norway]      ║
║  QMS Standard:   AS9100D / ISO 9001:2015                         ║
║  AQAP:           AQAP 2110 (if applicable)                       ║
║  Certificate No: AM-COC-[YYYY]-[Sequential]                      ║
║                                                                  ║
║  CUSTOMER INFORMATION                                            ║
║  ─────────────────────                                           ║
║  Customer:       [Customer name]                                 ║
║  Purchase Order: [PO number]                                     ║
║  PO Date:        [Date]                                          ║
║  Contract Ref:   [If applicable]                                 ║
║                                                                  ║
║  PRODUCT INFORMATION                                             ║
║  ─────────────────────                                           ║
║  Part Number:    [Part number]                                   ║
║  Part Name:      [Description]                                   ║
║  Drawing:        [Drawing number, Revision]                      ║
║  Material:       [Material specification]                        ║
║  Quantity:       [Delivered quantity]                             ║
║  Serial Numbers: [List or range]                                 ║
║                                                                  ║
║  CONFORMANCE DECLARATION                                         ║
║  ─────────────────────────                                       ║
║  Aurelian Manufacturing AS hereby certifies that the products    ║
║  described above have been manufactured, inspected, and tested   ║
║  in accordance with the following requirements:                  ║
║                                                                  ║
║  ☐ Purchase Order [PO number] and all referenced specifications  ║
║  ☐ Drawing [Drawing number, Rev X]                               ║
║  ☐ Material Specification [e.g., AMS 4078 / ASTM A182]          ║
║  ☐ Quality Management System: AS9100D                            ║
║  ☐ AQAP 2110 (if contractually required)                         ║
║  ☐ First Article Inspection per AS9102 (if applicable)           ║
║  ☐ [Additional customer-specific requirements]                   ║
║                                                                  ║
║  MATERIAL TRACEABILITY                                           ║
║  ─────────────────────────                                       ║
║  Material Certificate: EN 10204 Type [3.1/3.2]                   ║
║  Heat/Lot Number(s):  [List]                                     ║
║  Supplier:             [Material supplier name]                  ║
║                                                                  ║
║  DEVIATIONS / CONCESSIONS                                        ║
║  ─────────────────────────                                       ║
║  ☐ No deviations from specified requirements                     ║
║  ☐ Deviations as documented:                                     ║
║    [NCR/Deviation number — customer-approved disposition]         ║
║                                                                  ║
║  SPECIAL PROCESSES (if applicable)                               ║
║  ─────────────────────────                                       ║
║  [List of special processes performed with cert references]      ║
║                                                                  ║
║  EXPORT COMPLIANCE (if applicable)                               ║
║  ─────────────────────────                                       ║
║  ☐ Items are not subject to ITAR/EAR restrictions                ║
║  ☐ Items are subject to [regulation] — classification: [ECCN]    ║
║  ☐ Export license: [License number if applicable]                ║
║                                                                  ║
║  MRB REFERENCE                                                   ║
║  ─────────────────                                               ║
║  Manufacturing Record Book: AM-MRB-[YYYY]-[Number]               ║
║  MRB contains complete quality records for this shipment.        ║
║                                                                  ║
║  AUTHORIZED SIGNATURE                                            ║
║  ─────────────────────                                           ║
║                                                                  ║
║  Signature: ___________________________                          ║
║  Name:      [Authorized Quality Representative]                  ║
║  Title:     [Quality Manager / Authorized Inspector]             ║
║  Date:      [DD Month YYYY]                                      ║
║                                                                  ║
║  This certificate is issued under the authority of               ║
║  Aurelian Manufacturing AS quality management system.            ║
║  Any reproduction requires written authorization.                ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## SECTION 4: OIL & GAS COC TEMPLATE

### 4.1 Oil & Gas Certificate of Conformance Format

```
╔══════════════════════════════════════════════════════════════════╗
║                CERTIFICATE OF CONFORMANCE                       ║
║                Oil & Gas / Energy                                ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  SUPPLIER INFORMATION                                            ║
║  ─────────────────────                                           ║
║  Company:        Aurelian Manufacturing AS                       ║
║  Org. Number:    835 679 632                                     ║
║  Address:        [Facility address, Valer, Ostfold, Norway]      ║
║  QMS Standard:   ISO 9001:2015                                   ║
║  NORSOK:         M-650 qualified (when applicable)               ║
║  Certificate No: AM-COC-[YYYY]-[Sequential]                      ║
║                                                                  ║
║  CUSTOMER INFORMATION                                            ║
║  ─────────────────────                                           ║
║  Customer:       [Customer name]                                 ║
║  Purchase Order: [PO number]                                     ║
║  PO Date:        [Date]                                          ║
║  Project:        [Project name/number if applicable]             ║
║                                                                  ║
║  PRODUCT INFORMATION                                             ║
║  ─────────────────────                                           ║
║  Part Number:    [Part number]                                   ║
║  Part Name:      [Description]                                   ║
║  Drawing:        [Drawing number, Revision]                      ║
║  Material Spec:  [Material specification, e.g., ASTM A182 F316L]║
║  Quantity:       [Delivered quantity]                             ║
║  Tag Numbers:    [If applicable — oil & gas specific]            ║
║  Heat Numbers:   [Material heat numbers]                         ║
║                                                                  ║
║  APPLICABLE STANDARDS                                            ║
║  ─────────────────────                                           ║
║  ☐ NORSOK M-650 (Qualification of Manufacturers)                 ║
║  ☐ API [specification number, e.g., API 6A]                      ║
║  ☐ ASME [section/standard, e.g., B16.34]                         ║
║  ☐ ASTM [standard, e.g., A182]                                   ║
║  ☐ DNV [specification if applicable]                             ║
║  ☐ [Additional customer/project specifications]                  ║
║                                                                  ║
║  CONFORMANCE DECLARATION                                         ║
║  ─────────────────────────                                       ║
║  Aurelian Manufacturing AS hereby certifies that the products    ║
║  described above have been manufactured, inspected, and tested   ║
║  in accordance with the purchase order requirements and the      ║
║  standards listed above.                                         ║
║                                                                  ║
║  All manufacturing, inspection, and testing activities have      ║
║  been performed in accordance with the approved Inspection       ║
║  and Test Plan (ITP): [ITP reference number]                     ║
║                                                                  ║
║  MATERIAL TRACEABILITY                                           ║
║  ─────────────────────────                                       ║
║  Material Certificate: EN 10204 Type [3.1/3.2]                   ║
║  Heat Number(s):       [List]                                    ║
║  Material Supplier:    [Supplier name]                           ║
║  PMI Verified:         ☐ Yes  ☐ Not Required                     ║
║  PMI Report Ref:       [Reference number]                        ║
║                                                                  ║
║  TESTING SUMMARY                                                 ║
║  ─────────────────                                               ║
║  ☐ Dimensional inspection completed — Report: [ref]              ║
║  ☐ NDT completed — Report: [ref]  (if applicable)               ║
║  ☐ Hydrostatic/pressure test — Report: [ref] (if applicable)    ║
║  ☐ Functional test — Report: [ref] (if applicable)              ║
║  ☐ Hardness test — Report: [ref] (if applicable)                ║
║  ☐ PMI verification — Report: [ref] (if applicable)             ║
║                                                                  ║
║  DEVIATIONS / NON-CONFORMANCES                                   ║
║  ─────────────────────────────                                   ║
║  ☐ No deviations from specified requirements                     ║
║  ☐ Approved deviations:                                          ║
║    [NCR number — disposition — customer approval reference]       ║
║                                                                  ║
║  NORSOK COMPLIANCE STATEMENT                                     ║
║  ─────────────────────────────                                   ║
║  Products manufactured in compliance with NORSOK requirements    ║
║  as specified in the purchase order. Material Data Sheets (MDS)  ║
║  per NORSOK M-630 enclosed where applicable.                     ║
║                                                                  ║
║  PRESERVATION STATUS                                             ║
║  ─────────────────────                                           ║
║  Preservation applied per: [Procedure reference]                 ║
║  Preservation valid until: [Date]                                ║
║                                                                  ║
║  ITP REFERENCE                                                   ║
║  ─────────────────                                               ║
║  ITP Ref:     [ITP document number]                              ║
║  ITP Status:  All Hold/Witness/Review points completed           ║
║                                                                  ║
║  MRB/MDR REFERENCE                                               ║
║  ─────────────────                                               ║
║  Manufacturing Data Record: AM-MRB-[YYYY]-[Number]               ║
║  MDR contains complete quality records for this shipment.        ║
║                                                                  ║
║  AUTHORIZED SIGNATURE                                            ║
║  ─────────────────────                                           ║
║                                                                  ║
║  Signature: ___________________________                          ║
║  Name:      [Authorized Quality Representative]                  ║
║  Title:     [Quality Manager / Authorized Inspector]             ║
║  Date:      [DD Month YYYY]                                      ║
║                                                                  ║
║  This certificate is issued under the authority of               ║
║  Aurelian Manufacturing AS quality management system.            ║
║  Any reproduction requires written authorization.                ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## SECTION 5: COC NUMBER SYSTEM

### 5.1 Certificate Numbering Convention

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
  - Revised CoCs get new number with reference to superseded number
  - Register maintained in ERP for audit trail
```

### 5.2 MRB Numbering Convention

```
FORMAT: AM-MRB-[YYYY]-[NNNNN]

  Follows same convention as CoC numbering.
  One MRB per order/shipment.
  MRB number referenced on the CoC for traceability.
```

---

## SECTION 6: COC GENERATION LOGIC

### 6.1 Field Population Rules

```
FIELD POPULATION:

  AUTOMATIC (from parsed SDRL / order data):
    - Supplier information (constant — Aurelian details)
    - Customer name and PO number (from aurelian-sdrl-parser)
    - Part number, drawing, material spec (from order data)
    - Quantity and serial numbers (from manufacturing records)
    - Applicable standards (from parsed SDRL classification)
    - Certificate number (auto-generated sequential)
    - MRB reference number (auto-generated)

  FROM VALIDATED DOCUMENTS (via aurelian-doc-validator):
    - Heat/lot numbers (from validated material certificates)
    - Material supplier name (from validated material certificates)
    - Material certificate type (3.1 or 3.2)
    - Testing report references (from validated inspection/test reports)
    - PMI status and reference (from validated PMI reports)
    - ITP reference (from validated ITP)
    - Deviation/NCR references (from validated NCR dispositions)
    - FAIR reference (from validated FAIR package)
    - Special process references (from validated special process certs)

  MANUAL (requires human input):
    - Authorized signatory name and title
    - Signature (physical or qualified electronic)
    - Export classification (if not pre-determined)
    - Preservation details (if not in standard procedure)
    - Customer-specific declarations
```

### 6.2 Conformance Statement Generation

```
STATEMENT CONSTRUCTION:

  BASE STATEMENT (always included):
    "Aurelian Manufacturing AS hereby certifies that the products
     described above have been manufactured, inspected, and tested
     in accordance with [requirements list]."

  REQUIREMENTS LIST — built dynamically from parsed SDRL:
    IF classification == "DEFENCE":
      + "Purchase Order [PO] and all referenced specifications"
      + "Drawing [number, Rev X]"
      + "Material Specification [spec]"
      + "Quality Management System: AS9100D"
      IF aqap_required: + "AQAP 2110"
      IF fair_performed: + "First Article Inspection per AS9102"
      FOR EACH customer_specific_req: + "[requirement text]"

    IF classification == "OIL_GAS":
      + "Purchase Order [PO] and all referenced specifications"
      + "Drawing [number, Rev X]"
      + "Material Specification [spec]"
      + "Quality Management System: ISO 9001:2015"
      FOR EACH applicable_standard: + "[standard reference]"
      IF itp_exists: + "Inspection and Test Plan [ITP ref]"
      IF norsok_required: + "NORSOK [applicable standards]"
      FOR EACH customer_specific_req: + "[requirement text]"
```

---

## SECTION 7: DEVIATION HANDLING ON COC

### 7.1 When Deviations Exist

If any non-conformances were dispositioned as "use-as-is" or "repair" with customer approval:

```
DEVIATION DOCUMENTATION ON COC:

  RULE: ALL accepted deviations MUST be declared on the CoC.
        Omitting a known deviation is falsification.

  FORMAT:
    "Deviations as documented:"
    - NCR-[number]: [Brief description] — Disposition: [Use-as-is/Repair]
      Customer approval: [Reference to customer acceptance document]

  EXAMPLE:
    - NCR-2027-042: Dimension X at 25.12mm vs 25.00 +/-0.05mm
      Disposition: Use-as-is
      Customer approval: Email from [Customer QA], dated [date], ref [email ID]

  CRITICAL RULES:
    - Never issue CoC with undisclosed deviations
    - Customer approval documentation must be VALIDATED before CoC generation
    - If deviation affects form/fit/function: escalate to engineering for review
    - If deviation affects safety: STOP — requires formal customer engineering disposition
```

---

## SECTION 8: SIGNATURE AUTHORITY

### 8.1 Who Can Sign

```
SIGNATURE AUTHORITY LEVELS:

  LEVEL 1 — Quality Manager:
    Can sign: ALL CoCs
    Required for: First articles, customer-escalated NCRs, export-controlled items

  LEVEL 2 — Senior Quality Engineer:
    Can sign: Standard production CoCs
    Cannot sign: First articles, export-controlled items

  LEVEL 3 — Quality Inspector (limited):
    Can sign: Repeat orders with no deviations only
    Cannot sign: First articles, deviations, export items, new customers

  RULE: Signature authority must be formally delegated and documented in QMS.
        The authorized signatory list is maintained as a controlled document.
        At production start (Phase 1), all CoCs should be signed by Quality Manager.
```

### 8.2 Electronic Signature Requirements

```
ELECTRONIC SIGNATURE (when implemented):

  Must comply with:
    - eIDAS Regulation (EU electronic signatures)
    - Customer-specific e-signature requirements
    - AS9100D document control requirements

  Minimum requirements:
    - Unique to signatory
    - Signatory identity verifiable
    - Linked to signed data (tamper-evident)
    - Timestamp from trusted source
    - Audit trail maintained

  Phase 1 (Launch): Wet signature on printed CoC, then scanned to PDF/A
  Phase 2 (6 months): Qualified electronic signature with audit trail
```

---

## SECTION 9: COC ARCHIVAL AND DISTRIBUTION

### 9.1 Distribution

```
COC DISTRIBUTION:

  ORIGINAL (signed):
    → Customer (with shipment or advance electronic copy)

  COPIES:
    → MRB package (Section 8 for Defence, Section 6 for Oil & Gas)
    → Aurelian QMS archive (per retention policy)
    → ERP system (linked to sales order for invoicing)
    → Customer portal (when implemented)

  FORMAT:
    → Physical: Printed, signed, enclosed with shipment
    → Electronic: PDF/A scan of signed original
    → Both: Many customers require both physical and electronic copies
```

### 9.2 Retention

```
ARCHIVAL REQUIREMENTS:

  DEFENCE:
    → Minimum 7-10 years (per contract terms)
    → Some NATO contracts: 25+ years or contract life
    → Format: PDF/A for long-term readability

  OIL & GAS:
    → Equipment lifetime + 5-10 years
    → Subsea equipment: potentially 25-30+ years
    → Format: PDF/A for long-term readability

  AURELIAN STANDARD: Retain ALL CoCs for minimum 15 years unless contract specifies longer.
```

---

## SECTION 10: COC GENERATION WORKFLOW SUMMARY

```
COMPLETE WORKFLOW:

  1. ORDER ARRIVES
     → aurelian-sdrl-parser classifies order and generates requirement matrix
     → MRB structure initialized with required document slots

  2. PRODUCTION & COLLECTION
     → Documents collected from all sources:
        CNC in-machine → direct to MRB
        Metrology → direct to MRB
        Inspection room → direct to MRB
        Supplier docs → ERP → routed to order MRB
        Special processes → ERP → routed to order MRB

  3. VALIDATION
     → aurelian-doc-validator validates each document as received
     → Status tracked: PENDING → RECEIVED → VALIDATED / REJECTED
     → Rejected documents trigger correction requests

  4. COC READINESS CHECK
     → aurelian-doc-validator confirms ALL prerequisites met
     → IF ready: proceed to step 5
     → IF not ready: report blocking items, wait for resolution

  5. COC GENERATION
     → aurelian-coc-generator populates template:
        - Auto-fills from order data and validated documents
        - Selects correct template (Defence / Oil & Gas)
        - Constructs conformance statement
        - Lists all applicable standards
        - Documents any deviations
        - Assigns certificate number
        - References MRB number

  6. REVIEW AND SIGNATURE
     → Generated CoC presented to authorized signatory
     → Signatory reviews and signs (physical or electronic)
     → Signed CoC archived

  7. MRB ASSEMBLY
     → Signed CoC → aurelian-mrb-builder for final MRB compilation
     → CoC placed in correct MRB section (8 for Defence, 6 for Oil & Gas)

  8. DELIVERY
     → Complete MRB package with signed CoC delivered to customer
     → Advance electronic copy if contractually required
     → Archive copy retained per retention policy
```
