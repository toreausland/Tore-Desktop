---
name: aurelian-sdrl-parser
description: SDRL intake and parsing skill for Aurelian Manufacturing's Digital MRB Builder system. Parses Supplier Document Requirement Lists (SDRLs) for Defence (AS9100/AQAP) and Oil & Gas (NORSOK/API) contracts into structured requirement sets. Use this skill when receiving a new customer order/contract, parsing SDRL documents, extracting document requirements from purchase orders, setting up MRB requirement matrices, or any question about what documentation is required for a specific contract type. Triggers on "parse SDRL", "new order", "document requirements", "what documents do we need", "MRB requirements", "SDRL checklist", "defence documentation", "oil and gas documentation", "contract documentation", "purchase order requirements", "AQAP documents", "NORSOK documents", "AS9100 documentation", "API documentation", "customer requirements", or any request to identify and structure the documentation deliverables for a manufacturing order.
---

# Aurelian Manufacturing — SDRL Parser Skill

Intake and parsing engine for Supplier Document Requirement Lists. Transforms customer contract requirements into structured, actionable document requirement sets that feed the Digital MRB Builder pipeline.

**Source document:** AM-SDRL-2026-001 Rev 1.0 — Shipment Documentation Requirements (SDRL/MRB) located at `Quality System Input/Supplier Quality and Document requirements/Shipment_Documentation_Requirements_SDRL_MRB.pdf`

**Related MRB Builder skills:**
- `aurelian-doc-validator` — Validates collected documents against parsed requirements
- `aurelian-coc-generator` — Generates Certificates of Conformance
- `aurelian-mrb-builder` — Master orchestrator for MRB assembly

---

## SECTION 1: SDRL CONCEPT AND PURPOSE

### 1.1 What is an SDRL?

A Supplier Document Requirement List (SDRL) is a contractual document — typically attached to or embedded in a Purchase Order (PO) — that specifies exactly what documentation the supplier (Aurelian) must provide with each delivery. It defines:

- **Which documents** are required (e.g., material certificates, inspection reports, test records)
- **What standard/specification** each document must comply with (e.g., EN 10204 Type 3.1, AS9102)
- **When** each document must be delivered (with shipment, before shipment, at milestones)
- **In what format** (PDF/A, native, signed/stamped copies)
- **Review/approval workflow** (for information, for review, for approval)

### 1.2 Why Parsing Matters

Every customer sends SDRLs in different formats — some as structured Excel matrices, some as Word tables, some embedded in PO terms. Aurelian's Digital MRB Builder must normalize ALL incoming SDRL formats into a single internal requirement structure to enable automated document collection and validation.

---

## SECTION 2: INDUSTRY-SPECIFIC SDRL TEMPLATES

### 2.1 Defence SDRL (AS9100 / AQAP 2110)

Defence MRBs follow an 8-section structure with 25 standard line items (Appendix A of source document):

| Section | Contents | Key Documents |
|---------|----------|---------------|
| **1. Identification & Index** | MRB cover page, document index, revision log | Cover page, Master index, Revision history |
| **2. Contract Documentation** | PO, contract amendments, SDRL itself | Purchase Order copy, Contract amendments, Approved SDRL |
| **3. Material Documentation** | Material certs, composition, heat treatment | EN 10204 certs (3.1/3.2), Material composition reports, Heat treatment records |
| **4. Manufacturing Process** | Process sheets, CNC programs, tool lists | Manufacturing process sheets, CNC program verification, Tool/fixture records, Setup sheets |
| **5. Special Processes** | NDT, welding, surface treatment | NDT reports (RT/UT/MT/PT), Welding records (WPS/PQR/WPQ), Surface treatment certs |
| **6. Inspection** | FAIR, dimensional, in-process | AS9102 FAIR (Forms 1-3), Dimensional inspection reports, In-process inspection records |
| **7. Testing** | Mechanical, hardness, pressure, functional | Mechanical test reports, Hardness test reports, Pressure/leak test reports, Functional test reports |
| **8. Compliance Declarations** | CoC, DoC, export declarations | Certificate of Conformance, Declaration of Conformity, Export compliance declarations |

### 2.2 Oil & Gas SDRL (NORSOK / API)

Oil & Gas MRBs follow a 7-section structure with 30 standard line items (Appendix B of source document):

| Section | Contents | Key Documents |
|---------|----------|---------------|
| **1. General Information** | Document index, quality plan, project specs | MRB/MDR index, Quality Plan/ITP, Project specification compliance |
| **2. Purchase & Technical** | PO, material specs, deviations | Purchase Order copy, Material specifications, Technical deviation requests/approvals |
| **3. Material Documentation** | Material certs, PMI, traceability | EN 10204 certs (3.1/3.2), PMI reports, Material traceability matrix, NORSOK M-650 compliance |
| **4. Manufacturing Records** | Welding, heat treatment, machining | WPS/PQR/WPQ, Heat treatment records, Machining parameter records, Forming/bending records |
| **5. Testing & Inspection** | NDT, dimensional, hydro, functional | NDT reports per ASME V, Dimensional reports, Hydrostatic/pressure test, Functional test, ITP sign-offs |
| **6. Compliance** | CoC, deviation log, NORSOK compliance | Certificate of Conformance, Deviation/NCR log, NORSOK compliance statement, Material Data Sheets (MDS) |
| **7. Preservation & Shipping** | Preservation, packing, shipping | Preservation procedure + records, Packing specification, Shipping/transport documentation |

### 2.3 Key Differences Between Industries

| Aspect | Defence | Oil & Gas |
|--------|---------|-----------|
| Governing standards | AS9100, AQAP 2110, MIL-STDs | NORSOK, API, ASME, ASTM |
| Material cert requirement | EN 10204 3.1 minimum; 3.2 for critical | EN 10204 3.1/3.2 + PMI mandatory |
| First Article | AS9102 FAIR (3 forms) mandatory | Typically only for new products |
| Inspection framework | Customer source inspection common | ITP with Hold/Witness/Review points |
| Special processes | NADCAP accreditation often required | Per ASME/NORSOK qualification |
| Traceability | Part serial → raw material lot | Heat number → final product |
| Preservation | MIL-STD packaging | NORSOK-specific preservation |
| Export control | ITAR/EAR compliance required | Typically not applicable |
| Archival period | 7-10 years minimum | Equipment lifetime + 5-10 years |
| Digital format | PDF/A preferred, structured data growing | PDF/A for archival, native for review |

---

## SECTION 3: SDRL PARSING PROCEDURE

### 3.1 Step 1 — Identify Contract Type

When a new order/contract arrives, determine the industry classification:

```
INPUT:  Customer PO / Contract / RFQ
OUTPUT: Industry classification

RULES:
  IF customer is in defence/aerospace sector (Kongsberg, Nammo, Saab, BAE, FFI, FMA)
    OR PO references AS9100 / AQAP / MIL-STD / STANAG / DEF-STAN
    → CLASSIFICATION = "DEFENCE"
    → Use 8-section MRB template (25 line items)

  IF customer is in energy/oil & gas sector (Equinor, Aker, Vattenfall, TechnipFMC)
    OR PO references NORSOK / API / ASME / ASTM / DNV
    → CLASSIFICATION = "OIL_GAS"
    → Use 7-section MRB template (30 line items)

  IF customer is in maritime/infrastructure (Vard, Ulstein, Bane NOR)
    OR PO references DNV / Bureau Veritas / Lloyd's
    → CLASSIFICATION = "MARITIME" (use Oil & Gas template as base, adapt)

  IF unclear or hybrid
    → FLAG for manual review
    → Default to the MORE stringent template
```

### 3.2 Step 2 — Extract Document Requirements

Parse the incoming SDRL/PO for each required document. Extract into this normalized structure:

```
FOR EACH document requirement in the SDRL:

  EXTRACT:
    - doc_id:           Unique line item number (e.g., "DEF-03-01" or "OG-03-01")
    - doc_title:        Document name (e.g., "Material Test Certificate")
    - doc_standard:     Required standard (e.g., "EN 10204 Type 3.1")
    - mrb_section:      Which MRB section it belongs to (1-8 for defence, 1-7 for oil & gas)
    - timing:           When required ("with_shipment", "before_shipment", "at_milestone", "on_request")
    - format:           Required format ("pdf_a", "native", "both")
    - review_code:      Approval workflow ("FOR_INFO", "FOR_REVIEW", "FOR_APPROVAL")
    - source:           Where document originates:
                        - "CNC_INLINE"     → Direct from CNC machine measurement
                        - "METROLOGY"      → From metrology monitoring system
                        - "INSPECTION"     → From inspection room (CMM etc.)
                        - "SUPPLIER"       → From external supplier (via ERP)
                        - "INTERNAL_QA"    → Generated by Aurelian QA
                        - "SPECIAL_PROCESS"→ From subcontractor/special process house
                        - "CUSTOMER"       → Provided by customer (specifications, drawings)
    - criticality:      "CRITICAL" / "MAJOR" / "STANDARD"
    - notes:            Any special instructions from the customer

OUTPUT: Structured requirement set (JSON-like internal format)
```

### 3.3 Step 3 — Map to Data Sources

For each parsed requirement, assign the data source routing:

```
DATA SOURCE ROUTING:

  CNC_INLINE sources (route DIRECT to order MRB):
    - In-machine dimensional verification data
    - Tool wear measurements
    - Spindle load monitoring data
    - Cycle time records
    - Surface finish verification (in-process)

  METROLOGY sources (route DIRECT to order MRB):
    - Real-time temperature monitoring
    - Vibration analysis records
    - Coolant condition monitoring
    - Environmental condition logs (temperature, humidity)

  INSPECTION sources (route DIRECT to order MRB):
    - CMM measurement reports
    - Surface roughness measurements (Ra, Rz)
    - Hardness test results
    - Visual inspection records
    - Dimensional inspection reports (AS9102 characteristic data)

  SUPPLIER sources (route via ERP → then to order MRB):
    - EN 10204 material certificates (3.1/3.2)
    - Raw material composition reports
    - Heat treatment certificates from material supplier
    - PMI reports from material supplier
    - Sub-supplier compliance declarations
    NOTE: Same material cert can serve MULTIPLE orders — ERP manages this linkage

  INTERNAL_QA sources (route DIRECT to order MRB):
    - Manufacturing process sheets
    - AS9102 FAIR reports (compiled from inspection data)
    - Non-Conformance Reports (NCRs)
    - Certificate of Conformance (generated by aurelian-coc-generator)
    - MRB cover page and index

  SPECIAL_PROCESS sources (route via ERP → then to order MRB):
    - NDT reports (RT, UT, MT, PT)
    - Surface treatment certificates
    - Welding documentation (WPS, PQR, WPQ)
    - NADCAP certificates
    - Heat treatment records (external)
```

### 3.4 Step 4 — Generate Requirement Matrix

Output a complete requirement matrix for the order:

```
ORDER REQUIREMENT MATRIX

Order:          [PO Number]
Customer:       [Customer Name]
Classification: [DEFENCE / OIL_GAS / MARITIME]
Template:       [8-section / 7-section]
Total items:    [Count of required documents]
Critical items: [Count of CRITICAL documents]

| Line | Doc Title | Standard | Section | Source | Timing | Status |
|------|-----------|----------|---------|--------|--------|--------|
| DEF-01-01 | MRB Cover Page | Internal | 1 | INTERNAL_QA | with_shipment | PENDING |
| DEF-03-01 | Material Test Cert | EN 10204 3.1 | 3 | SUPPLIER | with_shipment | PENDING |
| ... | ... | ... | ... | ... | ... | ... |

Status values: PENDING / IN_PROGRESS / COLLECTED / VALIDATED / REJECTED
```

---

## SECTION 4: EN 10204 MATERIAL CERTIFICATE TYPES

Critical knowledge for parsing material documentation requirements:

| Type | Description | Issued By | Content | When Required |
|------|-------------|-----------|---------|---------------|
| **2.1** | Declaration of compliance | Manufacturer | Statement of compliance only | Low-criticality items |
| **2.2** | Test report | Manufacturer | Test results from non-specific inspection | Standard commercial |
| **3.1** | Inspection certificate | Manufacturer's authorized inspector | Specific test results from actual production lot | **Defence minimum**, Oil & Gas standard |
| **3.2** | Inspection certificate | Independent/customer inspector | Specific test results verified by third party | **Critical safety items**, customer-specified |

```
PARSING RULE:
  IF SDRL specifies "3.1" → Material cert must include:
    - Heat/lot number
    - Chemical composition (actual, not typical)
    - Mechanical properties (actual test results)
    - Manufacturer's authorized representative signature
    - Reference to specific standard (e.g., ASTM A182, EN 10088-3)

  IF SDRL specifies "3.2" → All of 3.1 PLUS:
    - Third-party inspector identification
    - Independent verification of test results
    - Third-party stamp/signature
```

---

## SECTION 5: AS9102 FAIR PARSING (DEFENCE)

First Article Inspection Report requirements for defence contracts:

### 5.1 FAIR Structure (3 Forms)

| Form | Title | Purpose | Data Source |
|------|-------|---------|-------------|
| **Form 1** | Part Number Accountability | Lists all part numbers, drawing revisions, materials | INTERNAL_QA (from PO + drawings) |
| **Form 2** | Product Accountability | Sub-assembly and raw material traceability | SUPPLIER (material certs) + INTERNAL_QA |
| **Form 3** | Characteristic Accountability | Every dimension/tolerance with actual measured values | CNC_INLINE + INSPECTION (CMM data) |

### 5.2 FAIR Trigger Rules

```
FAIR IS REQUIRED WHEN:
  - First production of a new part number
  - Design change affecting form/fit/function
  - Change in manufacturing process
  - Change in manufacturing location
  - Change in supplier of raw material (for critical characteristics)
  - Production gap exceeding customer-defined period (typically 2 years)
  - Customer explicitly requests FAIR

FAIR DATA FLOW:
  Form 3 characteristic data ← CNC in-machine measurement + CMM inspection
  Form 2 material data ← Supplier EN 10204 certs (via ERP)
  Form 1 part data ← Contract/PO information + drawing revision control

  All 3 forms → INTERNAL_QA compiles → validated by aurelian-doc-validator → placed in MRB Section 6
```

---

## SECTION 6: OIL & GAS ITP PARSING

Inspection and Test Plan requirements for oil & gas contracts:

### 6.1 ITP Point Types

| Code | Type | Meaning | Action Required |
|------|------|---------|-----------------|
| **H** | Hold Point | Production STOPS until customer/third-party inspects | Schedule inspection, halt production, notify customer |
| **W** | Witness Point | Customer invited to witness; production can continue if absent | Notify customer 48-72h in advance |
| **R** | Review Point | Documentation submitted for review; production can continue | Submit docs, log acknowledgement |
| **S** | Surveillance | Random or periodic oversight | Log surveillance visits |

### 6.2 ITP Parsing Structure

```
FOR EACH ITP line item:

  EXTRACT:
    - itp_item:      Item number
    - activity:       Manufacturing/inspection activity description
    - reference_doc:  Applicable standard or procedure
    - point_type:     H / W / R / S
    - responsible:    Who performs (Aurelian / Customer / Third Party)
    - acceptance:     Acceptance criteria
    - record:         What record is generated
    - mrb_section:    Which MRB section receives the record

OUTPUT: ITP tracker with real-time status per Hold/Witness/Review point
```

---

## SECTION 7: PMI (POSITIVE MATERIAL IDENTIFICATION) PARSING

Required for Oil & Gas orders and sometimes defence critical items:

### 7.1 PMI Methods

| Method | Technique | Accuracy | Application |
|--------|-----------|----------|-------------|
| **XRF** | X-ray Fluorescence | Good for most alloys | Standard field verification |
| **OES** | Optical Emission Spectroscopy | High (incl. carbon, nitrogen) | When carbon content critical |
| **Lab Analysis** | Wet chemistry / ICP | Highest | Referee method, disputes |

### 7.2 PMI Requirement Parsing

```
IF SDRL requires PMI:
  - Determine method required (XRF default, OES if carbon-critical)
  - Map to inspection room data source (INSPECTION)
  - Link to material certificate heat number (from SUPPLIER via ERP)
  - Record in MRB Section 3 (Material Documentation)
  - Cross-reference with material traceability matrix

PMI DATA FLOW:
  Raw material arrives → Goods receiving → PMI test in inspection room
  → PMI report generated → Linked to heat number in ERP
  → Routed to ALL orders using that material batch
```

---

## SECTION 8: SDRL OUTPUT FORMAT

### 8.1 Parsed SDRL JSON Structure

The parser outputs a structured format consumed by downstream skills:

```json
{
  "order_id": "PO-2027-001",
  "customer": "Kongsberg Defence & Aerospace",
  "classification": "DEFENCE",
  "template_version": "DEF-8SEC-V1",
  "total_requirements": 25,
  "critical_count": 8,
  "parse_date": "2027-08-15",
  "sections": [
    {
      "section_id": 1,
      "section_name": "Identification & Index",
      "requirements": [
        {
          "doc_id": "DEF-01-01",
          "doc_title": "MRB Cover Page",
          "standard": "AM-QMS-MRB-001",
          "source": "INTERNAL_QA",
          "timing": "with_shipment",
          "format": "pdf_a",
          "review_code": "FOR_INFO",
          "criticality": "STANDARD",
          "status": "PENDING",
          "assigned_to": null,
          "collected_date": null,
          "validated": false
        }
      ]
    }
  ],
  "itp": null,
  "fair_required": true,
  "pmi_required": false,
  "special_processes": ["NDT_UT", "SURFACE_TREATMENT"],
  "archival_years": 10,
  "digital_format": "pdf_a"
}
```

### 8.2 Handoff to Downstream Skills

```
PARSED SDRL → aurelian-doc-validator
  Provides: Complete requirement set with expected standards, sources, and criticality
  Validator uses this to check each collected document meets requirements

PARSED SDRL → aurelian-coc-generator
  Provides: Classification (DEFENCE/OIL_GAS), customer info, requirements summary
  CoC generator uses this to produce the correct industry-specific certificate

PARSED SDRL → aurelian-mrb-builder
  Provides: Full requirement matrix with section mapping
  MRB builder uses this as the master checklist for assembly
```

---

## SECTION 9: COMMON SDRL PARSING SCENARIOS

### 9.1 Scenario A — Defence Part (Kongsberg KDA)

```
INPUT:  PO from Kongsberg Defence & Aerospace for 50x precision housings
        PO references: AS9100D, AQAP 2110, drawing rev C
        Material: 7075-T6 aluminium (AMS 4078)

PARSE RESULT:
  Classification: DEFENCE
  Template: 8-section, 25 line items
  FAIR required: YES (new part number)
  PMI required: NO (aluminium not typically PMI'd unless specified)
  Special processes: Anodize (Type III hard coat)
  Material cert: EN 10204 Type 3.1 minimum
  Critical docs: FAIR, Material certs, Dimensional inspection, CoC
  Archival: 10 years minimum

DATA ROUTING:
  CNC dimensional data → Direct to MRB (Section 6)
  CMM inspection data → Direct to MRB (Section 6)
  Material certs → ERP (batch-level) → MRB (Section 3)
  Anodize certs → ERP (external subcontractor) → MRB (Section 5)
  FAIR compilation → Internal QA → MRB (Section 6)
  CoC → aurelian-coc-generator → MRB (Section 8)
```

### 9.2 Scenario B — Oil & Gas Component (Equinor)

```
INPUT:  PO from Equinor for 20x valve bodies
        PO references: NORSOK M-650, API 6A, ASME B16.34
        Material: F316L stainless steel (ASTM A182)
        ITP attached with 3 Hold points, 5 Witness points

PARSE RESULT:
  Classification: OIL_GAS
  Template: 7-section, 30 line items
  FAIR required: NO (unless first article specified)
  PMI required: YES (stainless steel, safety-critical)
  Special processes: None specified
  Material cert: EN 10204 Type 3.2 (third-party verified for pressure equipment)
  ITP: 3H + 5W + multiple R points
  NORSOK MDS: Required
  Hydrostatic test: Required per API 6A
  Archival: Equipment lifetime + 10 years

DATA ROUTING:
  CNC dimensional data → Direct to MRB (Section 5)
  PMI results → Direct to MRB (Section 3)
  CMM inspection data → Direct to MRB (Section 5)
  Hydrostatic test data → Direct to MRB (Section 5)
  Material certs (3.2) → ERP (batch-level) → MRB (Section 3)
  ITP sign-offs → Direct to MRB (Section 5) at each H/W/R point
  CoC → aurelian-coc-generator → MRB (Section 6)
```

---

## SECTION 10: REFERENCE STANDARDS INDEX

Standards commonly referenced in SDRLs that the parser must recognize:

### 10.1 Defence Standards

| Standard | Full Name | Relevance |
|----------|-----------|-----------|
| AS9100D | Quality Management Systems — Aerospace | Core QMS for aerospace/defence |
| AS9102B | First Article Inspection | FAIR format and requirements |
| AQAP 2110 | NATO Quality Assurance | NATO supplier quality requirements |
| EN 10204 | Metallic products — Inspection documents | Material certificate types |
| NADCAP | National Aerospace and Defense Contractors Accreditation | Special process accreditation |
| AMS | Aerospace Material Specifications | Material specifications |
| MIL-STD-130 | Identification Marking | Part identification |
| MIL-STD-1916 | Acceptance Sampling | Statistical sampling plans |

### 10.2 Oil & Gas Standards

| Standard | Full Name | Relevance |
|----------|-----------|-----------|
| NORSOK M-650 | Qualification of Manufacturers | Supplier qualification |
| NORSOK Z-CR-006 | Documentation Requirements | Document control for O&G |
| NORSOK M-630 | Material Data Sheets | Material documentation |
| API 6A | Wellhead and Christmas Tree Equipment | Valve body requirements |
| ASME B16.34 | Valves — Flanged, Threaded, Welding End | Valve design standards |
| ASME Section V | Nondestructive Examination | NDT methods and acceptance |
| ASME Section IX | Welding, Brazing, Fusing | Welding qualification |
| ASTM A182 | Forged/Rolled Alloy and Stainless Steel | Material standard |
| DNV-OS-F101 | Submarine Pipeline Systems | Pipeline component docs |

---

## SECTION 11: ERROR HANDLING AND EDGE CASES

### 11.1 Incomplete SDRL

```
IF incoming SDRL is incomplete or ambiguous:
  1. FLAG missing requirements
  2. APPLY industry-standard defaults based on classification
  3. GENERATE clarification request for customer
  4. DO NOT proceed to MRB assembly until clarified

  DEFENCE DEFAULT: Apply full 25-item checklist (over-document rather than under)
  OIL_GAS DEFAULT: Apply full 30-item checklist + request ITP
```

### 11.2 Multi-Industry Order

```
IF customer operates across industries (e.g., Kongsberg has both defence and maritime):
  → Classification is PER ORDER LINE, not per customer
  → Parse each line item against correct template
  → Flag mixed-classification orders for QA review
```

### 11.3 Customer-Specific Extensions

```
IF SDRL contains requirements BEYOND the standard template:
  → ADD as custom line items with source "CUSTOMER_SPECIFIC"
  → Map to nearest MRB section
  → Flag for aurelian-doc-validator as non-standard requirement
```
