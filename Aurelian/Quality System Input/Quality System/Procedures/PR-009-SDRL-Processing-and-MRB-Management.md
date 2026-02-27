# SDRL PROCESSING AND MRB MANAGEMENT

| Field | Value |
|-------|-------|
| **Document No.** | PR-009 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-19 |
| **Approved By** | Quality Manager |
| **Classification** | Internal |
| **ISO 9001 Clause** | 8.1, 8.2, 8.5.1 |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2026-02-19 | Quality Manager | Initial Release |

---

## 1. Purpose

This procedure defines how Aurelian Manufacturing AS receives, parses, and manages Supplier Document Requirement Lists (SDRLs) from customers, and how the corresponding Manufacturing Record Book (MRB) structure is initialized and managed throughout the production lifecycle.

## 2. Scope

This procedure applies to:

- All customer Purchase Orders containing SDRL requirements
- Defence orders (AS9100/AQAP 2110 documentation requirements)
- Oil & Gas orders (NORSOK/API documentation requirements)
- Maritime and general engineering orders with documentation deliverables
- Initialization and lifecycle management of all MRBs

## 3. References

| Document | Title |
|----------|-------|
| QM-001 | Quality Manual |
| PR-007 | Customer Communication and Contract Review |
| PR-008 | Incoming Material Review and Release |
| PR-010 | Document Validation and Verification |
| PR-011 | Certificate of Conformance |
| PR-012 | MRB Assembly and Release |
| AM-SDRL-2026-001 | Shipment Documentation Requirements (SDRL/MRB) |
| AS9102 | First Article Inspection Requirement |
| EN 10204:2004 | Metallic Products — Types of Inspection Documents |

## 4. Definitions

| Term | Definition |
|------|-----------|
| **SDRL** | Supplier Document Requirement List — a contractual document specifying which documentation the supplier must provide with each delivery |
| **MRB** | Manufacturing Record Book — the comprehensive compilation of all quality records for a specific order/shipment |
| **MDR** | Manufacturing Data Record — Oil & Gas equivalent term for MRB |
| **ITP** | Inspection and Test Plan — defines Hold, Witness, and Review points for Oil & Gas orders |
| **FAIR** | First Article Inspection Report — AS9102 requirement for defence/aerospace orders |

## 5. Responsibilities

| Role | Responsibility |
|------|---------------|
| **Quality Manager** | Owns this procedure. Approves MRB template changes. Final escalation for classification disputes. |
| **QA Engineer** | Parses SDRL requirements. Initializes MRB structure. Tracks document collection status. Manages ITP scheduling. |
| **Commercial Manager** | Identifies SDRL requirements during contract review (PR-007). Communicates documentation requirements to customer. |
| **Production Manager** | Ensures production data (CNC, metrology) is captured and routed to the correct MRB. Coordinates with QA on ITP Hold Points. |

## 6. Procedure

### 6.1 SDRL Identification During Contract Review

During contract review (per PR-007), the Commercial Manager and QA Engineer identify:

1. Whether the PO contains SDRL requirements (explicit SDRL document, or documentation requirements embedded in PO terms)
2. Which industry the order falls under:

| If PO references... | Classification | MRB Template |
|---------------------|---------------|--------------|
| AS9100, AQAP, MIL-STD, STANAG, DEF-STAN | **DEFENCE** | 8-section (25 line items) |
| NORSOK, API, ASME, ASTM, DNV | **OIL & GAS** | 7-section (30 line items) |
| DNV, Bureau Veritas, Lloyd's (without O&G specs) | **MARITIME** | 7-section (adapted) |
| None of the above / unclear | **STANDARD** | Use the more stringent template; flag for clarification |

3. Whether FAIR is required (defence orders — see Section 6.4)
4. Whether an ITP is attached or required (Oil & Gas orders — see Section 6.5)

### 6.2 SDRL Parsing

**Step 1:** QA Engineer extracts each document requirement from the SDRL and records:

| Field | Description |
|-------|-------------|
| Line item ID | Unique identifier (e.g., DEF-03-01, OG-03-01) |
| Document title | What the document is (e.g., Material Test Certificate) |
| Standard/specification | What standard it must comply with (e.g., EN 10204 Type 3.1) |
| MRB section | Which section of the MRB it belongs to |
| Timing | When required: with shipment, before shipment, at milestone |
| Format | Required format: PDF/A, native, signed copy |
| Review code | FOR_INFO, FOR_REVIEW, FOR_APPROVAL |
| Data source | Where the document originates (see Section 6.3) |
| Criticality | CRITICAL, MAJOR, STANDARD |

**Step 2:** Record all parsed requirements in the **Order Requirement Matrix** (Form FM-009-01).

**Step 3:** If the SDRL is incomplete or ambiguous:
- Apply the full industry-standard checklist as default (over-document rather than under-document)
- Generate a clarification request for the customer via Commercial Manager
- Do NOT proceed with production until critical requirements are clarified

### 6.3 Data Source Routing

Each document requirement is assigned a data source route:

| Source Code | Description | Routing |
|-------------|-------------|---------|
| **CNC_INLINE** | In-machine dimensional data, tool wear, cycle times | Direct to order MRB |
| **METROLOGY** | Temperature, vibration, environmental monitoring | Direct to order MRB |
| **INSPECTION** | CMM reports, surface roughness, hardness tests | Direct to order MRB |
| **SUPPLIER** | Material certificates, sub-supplier declarations | Via ERP module to order MRB |
| **SPECIAL_PROCESS** | NDT reports, surface treatment, external heat treatment | Via ERP module to order MRB |
| **INTERNAL_QA** | Process sheets, FAIR, NCRs, CoC, MRB cover/index | Generated internally, placed in MRB |
| **CUSTOMER** | Drawings, specifications, contract documents | Received from customer, filed in MRB |

**Critical routing rule:** Supplier documents (material certs, special process certs) route through ERP first because the same document may serve multiple orders. ERP manages the one-to-many linkage. CNC, metrology, and inspection data route directly to the order-specific MRB.

### 6.4 FAIR Requirements (Defence Orders)

First Article Inspection per AS9102 is required when:

- First production of a new part number
- Design change affecting form, fit, or function
- Change in manufacturing process or location
- Change in raw material supplier (for critical characteristics)
- Production gap exceeding the customer-defined period (typically 2 years)
- Customer explicitly requests FAIR

When FAIR is required:
1. QA Engineer adds FAIR (Forms 1, 2, 3) to the Order Requirement Matrix
2. Form 3 characteristic data sources are defined (CNC_INLINE + INSPECTION)
3. Form 2 material data sources are linked to validated material certificates (from PR-008)
4. FAIR completion is tracked as part of MRB Section 6 (Inspection Documentation)

### 6.5 ITP Management (Oil & Gas Orders)

When an ITP is attached to or required by the order:

1. QA Engineer extracts all Hold (H), Witness (W), and Review (R) points
2. Each point is recorded in the **ITP Tracker** (Form FM-009-02):
   - Item number, activity description, point type (H/W/R/S)
   - Responsible party (Aurelian / Customer / Third Party)
   - Acceptance criteria and reference document
   - Required notification lead time (48-72 hours for Witness Points)
3. Hold Points are flagged in the production schedule — production STOPS at these points
4. Customer notifications are scheduled for Witness Points
5. ITP sign-off records are collected for MRB Section 5

### 6.6 MRB Structure Initialization and Index Generation

**Critical principle:** The SDRL defines the MRB Index. The MRB Index is NOT a fixed template — it is a variable, order-specific document generated directly from the parsed SDRL. Every order may have a different index because every SDRL specifies a different set of document requirements. The index generated at this stage becomes the master checklist that drives all downstream activities: document collection (Section 6.7), validation (PR-010), CoC generation (PR-011), and final MRB assembly (PR-012).

**Step 4:** Once the SDRL is parsed, QA Engineer initializes the MRB:

1. Assign MRB number: **AM-MRB-[YYYY]-[NNNNN]** (sequential, zero-padded)
2. Create the MRB folder structure matching the applicable template:

**Defence (8 sections):**

| Section | Title | Typical Contents |
|---------|-------|------------------|
| 1 | Identification and Index | Cover page, master index, revision history |
| 2 | Contract Documentation | PO copy, amendments, approved SDRL |
| 3 | Material Documentation | EN 10204 certs, composition, heat treatment, traceability matrix |
| 4 | Manufacturing Process | Process sheets, CNC program verification, tool/fixture records |
| 5 | Special Processes | NDT, welding records, surface treatment, external heat treatment |
| 6 | Inspection | FAIR, dimensional reports, in-process inspection, final inspection |
| 7 | Testing | Mechanical tests, hardness, pressure/leak, functional tests |
| 8 | Compliance Declarations | CoC, DoC, export compliance |

**Oil & Gas (7 sections):**

| Section | Title | Typical Contents |
|---------|-------|------------------|
| 1 | General Information | Index, Quality Plan/ITP, project spec compliance |
| 2 | Purchase and Technical | PO copy, material specs, deviation requests/approvals |
| 3 | Material Documentation | EN 10204 certs, PMI reports, traceability matrix, NORSOK M-650 |
| 4 | Manufacturing Records | Welding docs, heat treatment, machining parameters |
| 5 | Testing and Inspection | NDT, dimensional, pressure tests, functional tests, ITP sign-offs |
| 6 | Compliance Documentation | CoC, NCR log, NORSOK compliance statement, MDS |
| 7 | Preservation and Shipping | Preservation procedure/records, packing spec, transport docs |

3. **Generate the order-specific MRB Index** (Form FM-009-04) by mapping each parsed SDRL requirement from the Order Requirement Matrix into the applicable MRB section. The MRB Index is the SDRL expressed as a structured MRB document list:

| MRB Index Field | Populated From |
|-----------------|----------------|
| Line item number | Assigned per MRB section (e.g., 3.1, 3.2, 6.1) |
| MRB section | From SDRL parsing — "MRB section" field (Step 1) |
| Document title | From SDRL parsing — "Document title" field |
| Standard/specification | From SDRL parsing — "Standard/specification" field |
| Data source | From SDRL parsing — "Data source" field (Section 6.3) |
| Responsible party | Derived from data source routing |
| Required format | From SDRL parsing — "Format" field |
| Review code | From SDRL parsing — "Review code" field |
| Criticality | From SDRL parsing — "Criticality" field |
| Status | Initialized as **PENDING** |

**The MRB Index is order-specific. Two orders from the same customer may have different indices if the SDRLs differ. Two orders from different industries will always have different indices.**

4. Populate each MRB section folder with the document slots defined in the index
5. Each document slot shows: required document, status (PENDING), source, and responsible party
6. The MRB Index becomes the live tracking document — updated as documents are received, validated, or rejected
7. Record MRB initialization on Form FM-009-03

**Index lifecycle:**

| Phase | Index State | Description |
|-------|------------|-------------|
| **Initialization** (PR-009) | DRAFT | Generated from SDRL. All document slots PENDING. |
| **Collection** (PR-009 §6.7) | LIVE | Updated in real-time as documents arrive. Status changes from PENDING → RECEIVED. |
| **Validation** (PR-010) | LIVE | Status changes from RECEIVED → VALIDATED or REJECTED. |
| **Assembly** (PR-012) | FINAL | Page numbers added, final status confirmed. Becomes the Master Document Index in the MRB. |

**Note:** If the customer modifies the SDRL during the order (amendment, deviation, waiver), the MRB Index is updated accordingly. Changes to the index are revision-controlled and logged.

### 6.7 Document Collection Tracking

Throughout production, the QA Engineer tracks document collection status:

| Status | Meaning |
|--------|---------|
| **PENDING** | Document not yet received |
| **RECEIVED** | Document received, not yet validated |
| **VALIDATED** | Document passed validation (per PR-010) |
| **REJECTED** | Document failed validation — correction required |
| **NOT APPLICABLE** | Requirement waived or not relevant |

**Tracking frequency:**
- Weekly review of MRB completion percentage
- Immediate notification when a document is received or validated
- Alert to Production Manager and Commercial Manager when MRB completion reaches 80% and production is nearing completion
- Escalation to Quality Manager if blocking documents are overdue

### 6.8 Order Lifecycle States

Each order progresses through defined states:

```
NEW → SDRL_RECEIVED → SDRL_PARSED → MRB_INITIALIZED → COLLECTING
  → VALIDATING → COC_PENDING → COC_SIGNED → MRB_ASSEMBLY
  → MRB_RELEASED → SHIPPED → ARCHIVED
```

| State | Trigger | Description |
|-------|---------|-------------|
| NEW | PO received | Order entered into system |
| SDRL_RECEIVED | SDRL document received | SDRL attached to order, awaiting parsing |
| SDRL_PARSED | SDRL parsing complete | All line items extracted, requirement matrix populated |
| MRB_INITIALIZED | MRB structure created | MRB Index generated from SDRL, document slots created |
| COLLECTING | Production starts | Documents flowing in from CNC, suppliers, inspection |
| VALIDATING | All documents received | 5-layer validation in progress (PR-010) |
| COC_PENDING | All documents validated | Awaiting CoC generation and signature (PR-011) |
| COC_SIGNED | CoC signed | Certificate of Conformance issued and signed |
| MRB_ASSEMBLY | MRB compilation starts | Final MRB package being assembled (PR-012) |
| MRB_RELEASED | MRB quality check passed | MRB approved for shipment |
| SHIPPED | Dispatched | MRB delivered with product |
| ARCHIVED | Complete | Long-term retention initiated (PR-013) |

> **Note:** State transitions are enforced at the database level (see AM-TS-001 §7.3). Each transition is logged in the immutable Audit_Log.

## 7. Records

| Form | Title | Retention |
|------|-------|-----------|
| FM-009-01 | Order Requirement Matrix | Per order archival requirement |
| FM-009-02 | ITP Tracker (Oil & Gas orders) | Per order archival requirement |
| FM-009-03 | MRB Initialization Record | Per order archival requirement |
| FM-009-04 | MRB Index (order-specific, SDRL-derived) | Per order archival requirement |

## 8. Key Performance Indicators

| KPI | Target | Measured |
|-----|--------|----------|
| SDRL parsing time | < 2 business days from PO acceptance | Monthly |
| MRB completion at production end | > 70% of documents collected | Monthly |
| ITP Hold Point notification compliance | 100% of Hold Points notified on time | Per order |
| Customer documentation clarification requests | < 10% of orders require clarification | Quarterly |

## 9. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Prepared By | Quality Manager | _______ | _______ |
| Reviewed By | Production Manager | _______ | _______ |
| Approved By | Managing Director | _______ | _______ |

This document is controlled. Printed copies are uncontrolled unless stamped "CONTROLLED COPY" in red.
