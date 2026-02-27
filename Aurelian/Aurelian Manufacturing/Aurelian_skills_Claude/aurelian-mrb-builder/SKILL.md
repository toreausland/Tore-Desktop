---
name: aurelian-mrb-builder
description: Master orchestrator skill for Aurelian Manufacturing's Digital MRB Builder system. Coordinates the full Manufacturing Record Book lifecycle from order intake to final delivery, managing the pipeline between SDRL parsing, document collection, validation, CoC generation, and MRB assembly. Use this skill for any question about the overall MRB process, order status dashboards, MRB assembly, shipment readiness, digital MRB architecture, data flow design, ERP integration, system implementation roadmap, or orchestrating the complete documentation workflow. Triggers on "MRB status", "order documentation status", "MRB dashboard", "build MRB", "assemble MRB", "MRB ready", "shipment documentation", "documentation workflow", "MRB architecture", "digital MRB", "MRB system design", "document collection status", "what's missing for shipment", "MRB implementation", "Epicor integration", "ERP document flow", "production documentation", "quality records", "data flow", "manufacturing records", "MRB lifecycle", or any overarching question about Aurelian's documentation management system for manufacturing orders.
---

# Aurelian Manufacturing — MRB Builder Skill (Master Orchestrator)

Master orchestrator for the Digital MRB Builder system. Coordinates the entire Manufacturing Record Book lifecycle — from the moment a Purchase Order arrives to the moment a complete, validated MRB ships with the finished product.

**Source document:** AM-SDRL-2026-001 Rev 1.0 — Shipment Documentation Requirements (SDRL/MRB) located at `Quality System Input/Supplier Quality and Document requirements/Shipment_Documentation_Requirements_SDRL_MRB.pdf`

**Skill ecosystem:**
- `aurelian-sdrl-parser` → Stage 1: SDRL intake and requirement extraction
- `aurelian-doc-validator` → Stage 4: Document validation engine
- `aurelian-coc-generator` → Stage 5: Certificate of Conformance generation
- `aurelian-mrb-builder` (this skill) → Stages 1-7: Full lifecycle orchestration

---

## SECTION 1: SYSTEM ARCHITECTURE OVERVIEW

### 1.1 The 7-Stage MRB Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    DIGITAL MRB BUILDER                          │
│                    7-Stage Pipeline                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STAGE 1: SDRL INTAKE                                            │
│  ┌─────────────────────┐                                         │
│  │ Customer PO arrives  │──→ aurelian-sdrl-parser                │
│  │ SDRL extracted       │──→ Classification (Defence/Oil&Gas)    │
│  │ Requirements parsed  │──→ Requirement matrix generated        │
│  └─────────────────────┘                                         │
│           │                                                      │
│           ▼                                                      │
│  STAGE 2: REQUIREMENTS FLOW-DOWN                                 │
│  ┌─────────────────────┐                                         │
│  │ MRB structure init   │──→ Section folders created             │
│  │ Document slots       │──→ Expected document list per section  │
│  │ Source routing set    │──→ Each slot knows its data source     │
│  │ ITP tracker init     │──→ Hold/Witness/Review points (O&G)   │
│  └─────────────────────┘                                         │
│           │                                                      │
│           ▼                                                      │
│  STAGE 3: REAL-TIME DOCUMENT COLLECTION                          │
│  ┌─────────────────────────────────────────────┐                 │
│  │                                              │                │
│  │  ┌──────────┐   DIRECT TO MRB:               │                │
│  │  │ CNC      │──→ In-machine dimensions        │                │
│  │  │ Machine  │──→ Tool wear data               │                │
│  │  │ Data     │──→ Cycle time records            │                │
│  │  └──────────┘                                 │                │
│  │                                              │                │
│  │  ┌──────────┐   DIRECT TO MRB:               │                │
│  │  │Metrology │──→ Temperature monitoring        │                │
│  │  │ System   │──→ Vibration analysis            │                │
│  │  │          │──→ Environmental conditions      │                │
│  │  └──────────┘                                 │                │
│  │                                              │                │
│  │  ┌──────────┐   DIRECT TO MRB:               │                │
│  │  │Inspection│──→ CMM reports                   │                │
│  │  │  Room    │──→ Surface roughness             │                │
│  │  │          │──→ Hardness tests                │                │
│  │  └──────────┘                                 │                │
│  │                                              │                │
│  │  ┌──────────┐   VIA ERP → MRB:               │                │
│  │  │ Supplier │──→ Material certs (EN 10204)    │                │
│  │  │ Docs     │──→ Sub-supplier declarations    │                │
│  │  │ (Epicor) │──→ Special process certs        │                │
│  │  └──────────┘   (same cert → multiple orders) │                │
│  │                                              │                │
│  └─────────────────────────────────────────────┘                 │
│           │                                                      │
│           ▼                                                      │
│  STAGE 4: VALIDATION ENGINE                                      │
│  ┌─────────────────────┐                                         │
│  │ aurelian-doc-        │──→ 5-layer validation per document     │
│  │ validator             │──→ Existence/Format/Complete/          │
│  │                       │    Compliance/Traceability             │
│  │ Reject → correction  │──→ Failures generate action items      │
│  │ Accept → validated   │──→ Document enters MRB                 │
│  └─────────────────────┘                                         │
│           │                                                      │
│           ▼                                                      │
│  STAGE 5: COC GENERATION                                         │
│  ┌─────────────────────┐                                         │
│  │ aurelian-coc-        │──→ Prerequisite gate check             │
│  │ generator             │──→ Template selection (Def/O&G)       │
│  │                       │──→ Auto-populate from validated data   │
│  │ Output: Signed CoC   │──→ Authorized signature required       │
│  └─────────────────────┘                                         │
│           │                                                      │
│           ▼                                                      │
│  STAGE 6: MRB ASSEMBLY & EXPORT                                  │
│  ┌─────────────────────┐                                         │
│  │ Compile all validated│──→ Ordered by MRB section structure    │
│  │ documents into final │──→ Cover page + master index           │
│  │ MRB package          │──→ PDF/A archival format               │
│  │                       │──→ Bookmarked, hyperlinked PDF        │
│  └─────────────────────┘                                         │
│           │                                                      │
│           ▼                                                      │
│  STAGE 7: DELIVERY & ARCHIVE                                     │
│  ┌─────────────────────┐                                         │
│  │ Ship with product    │──→ Physical + electronic delivery      │
│  │ Customer portal      │──→ Customer download (when available)  │
│  │ Archive              │──→ PDF/A, ERP-linked, 15+ year retain  │
│  └─────────────────────┘                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Data Flow Principles

```
CORE DATA FLOW RULES:

  RULE 1: DIRECT ROUTING (preferred)
    Machine-generated data routes DIRECTLY to the order-specific MRB.
    No intermediate system. Lowest latency, no manual handling.
    Applies to: CNC data, metrology data, inspection room data.

  RULE 2: ERP-MEDIATED ROUTING (for shared documents)
    External documents that may serve MULTIPLE orders route through ERP first.
    ERP manages the one-to-many relationship (one cert → many orders).
    Applies to: Supplier material certs, special process certs, sub-supplier docs.

  RULE 3: SINGLE SOURCE OF TRUTH
    Each document type has ONE authoritative source.
    No duplicate entry. No manual transcription between systems.
    The MRB is an ASSEMBLY of validated source documents, not a copy.

  RULE 4: REAL-TIME STATUS
    Every document slot has a live status visible to QA, production, and management.
    Status changes trigger notifications when relevant (e.g., all docs validated = CoC ready).

  RULE 5: AUDIT TRAIL
    Every document action (received, validated, rejected, corrected, signed) is logged
    with timestamp, user/system identity, and action details.
```

---

## SECTION 2: MRB STRUCTURE TEMPLATES

### 2.1 Defence MRB Structure (8 Sections)

```
AM-MRB-[YYYY]-[NNNNN] — DEFENCE
│
├── SECTION 1: IDENTIFICATION & INDEX
│   ├── 1.1 MRB Cover Page
│   ├── 1.2 Master Document Index
│   └── 1.3 Revision History / Change Log
│
├── SECTION 2: CONTRACT DOCUMENTATION
│   ├── 2.1 Purchase Order (copy)
│   ├── 2.2 Contract Amendments (if any)
│   └── 2.3 Approved SDRL
│
├── SECTION 3: MATERIAL DOCUMENTATION
│   ├── 3.1 EN 10204 Material Certificates (3.1 or 3.2)
│   ├── 3.2 Material Composition Reports
│   ├── 3.3 Heat Treatment Records
│   └── 3.4 Material Traceability Matrix
│
├── SECTION 4: MANUFACTURING PROCESS DOCUMENTATION
│   ├── 4.1 Manufacturing Process Sheets
│   ├── 4.2 CNC Program Verification Records
│   ├── 4.3 Tool and Fixture Records
│   └── 4.4 Setup Sheets / First-Off Records
│
├── SECTION 5: SPECIAL PROCESS DOCUMENTATION
│   ├── 5.1 NDT Reports (RT/UT/MT/PT as applicable)
│   ├── 5.2 Welding Records (WPS/PQR/WPQ)
│   ├── 5.3 Surface Treatment Certificates
│   └── 5.4 Heat Treatment Records (external)
│
├── SECTION 6: INSPECTION DOCUMENTATION
│   ├── 6.1 AS9102 FAIR (Forms 1-3) — if applicable
│   ├── 6.2 Dimensional Inspection Reports
│   ├── 6.3 In-Process Inspection Records
│   └── 6.4 Final Inspection Report
│
├── SECTION 7: TEST DOCUMENTATION
│   ├── 7.1 Mechanical Test Reports
│   ├── 7.2 Hardness Test Reports
│   ├── 7.3 Pressure/Leak Test Reports (if applicable)
│   └── 7.4 Functional Test Reports (if applicable)
│
└── SECTION 8: COMPLIANCE DECLARATIONS
    ├── 8.1 Certificate of Conformance (CoC)
    ├── 8.2 Declaration of Conformity (DoC) — if applicable
    └── 8.3 Export Compliance Declarations — if applicable
```

### 2.2 Oil & Gas MRB Structure (7 Sections)

```
AM-MRB-[YYYY]-[NNNNN] — OIL & GAS
│
├── SECTION 1: GENERAL INFORMATION
│   ├── 1.1 MRB/MDR Index
│   ├── 1.2 Quality Plan / ITP (Inspection and Test Plan)
│   └── 1.3 Project Specification Compliance Matrix
│
├── SECTION 2: PURCHASE & TECHNICAL REQUIREMENTS
│   ├── 2.1 Purchase Order (copy)
│   ├── 2.2 Material Specifications
│   └── 2.3 Technical Deviation Requests/Approvals (if any)
│
├── SECTION 3: MATERIAL DOCUMENTATION
│   ├── 3.1 EN 10204 Material Certificates (3.1 or 3.2)
│   ├── 3.2 PMI Reports
│   ├── 3.3 Material Traceability Matrix
│   └── 3.4 NORSOK M-650 Compliance Documentation
│
├── SECTION 4: MANUFACTURING RECORDS
│   ├── 4.1 Welding Documentation (WPS/PQR/WPQ) — if applicable
│   ├── 4.2 Heat Treatment Records
│   ├── 4.3 Machining Parameter Records
│   └── 4.4 Forming/Bending Records — if applicable
│
├── SECTION 5: TESTING & INSPECTION
│   ├── 5.1 NDT Reports (per ASME V)
│   ├── 5.2 Dimensional Inspection Reports
│   ├── 5.3 Hydrostatic/Pressure Test Reports (if applicable)
│   ├── 5.4 Functional Test Reports (if applicable)
│   ├── 5.5 ITP Sign-Off Records (all H/W/R points)
│   └── 5.6 Final Inspection Report
│
├── SECTION 6: COMPLIANCE DOCUMENTATION
│   ├── 6.1 Certificate of Conformance (CoC)
│   ├── 6.2 Deviation/NCR Log with Dispositions
│   ├── 6.3 NORSOK Compliance Statement
│   └── 6.4 Material Data Sheets (MDS) per NORSOK M-630
│
└── SECTION 7: PRESERVATION & SHIPPING
    ├── 7.1 Preservation Procedure and Records
    ├── 7.2 Packing Specification
    └── 7.3 Shipping/Transport Documentation
```

---

## SECTION 3: ORDER LIFECYCLE MANAGEMENT

### 3.1 Order States

```
ORDER LIFECYCLE:

  NEW           → PO received, not yet processed
  PARSING       → SDRL being extracted and parsed
  ACTIVE        → MRB structure initialized, production in progress, collecting docs
  COLLECTING    → Manufacturing complete, finalizing document collection
  VALIDATING    → All documents received, validation in progress
  COC_PENDING   → Validation complete, awaiting CoC generation and signature
  MRB_ASSEMBLY  → CoC signed, assembling final MRB package
  READY         → MRB complete, ready for shipment
  SHIPPED       → MRB delivered with product
  ARCHIVED      → Order complete, MRB in long-term archive

STATE TRANSITIONS:
  NEW → PARSING         (triggered by: PO entry into system)
  PARSING → ACTIVE      (triggered by: SDRL parsed successfully)
  ACTIVE → COLLECTING   (triggered by: production marked complete)
  COLLECTING → VALIDATING (triggered by: all documents received)
  VALIDATING → COC_PENDING (triggered by: all documents validated)
  COC_PENDING → MRB_ASSEMBLY (triggered by: CoC signed)
  MRB_ASSEMBLY → READY  (triggered by: MRB compiled and QA-released)
  READY → SHIPPED       (triggered by: shipment dispatched)
  SHIPPED → ARCHIVED    (triggered by: customer acceptance or retention period start)
```

### 3.2 Real-Time Document Collection Tracking

```
ORDER DASHBOARD (per order):

  ┌──────────────────────────────────────────────────────────┐
  │ ORDER: PO-2027-001 | Kongsberg KDA | DEFENCE             │
  │ Status: ACTIVE | Parts: 50x Precision Housing             │
  │ Production: 60% complete | MRB: 45% complete              │
  ├──────────────────────────────────────────────────────────┤
  │                                                           │
  │ SECTION 1: Identification     ████████░░ 80%  (4/5)      │
  │ SECTION 2: Contract           ██████████ 100% (3/3)      │
  │ SECTION 3: Material           ██████░░░░ 60%  (3/5)      │
  │ SECTION 4: Manufacturing      ████░░░░░░ 40%  (2/5)      │
  │ SECTION 5: Special Process    ░░░░░░░░░░ 0%   (0/2)      │
  │ SECTION 6: Inspection         ██░░░░░░░░ 20%  (1/5)      │
  │ SECTION 7: Testing            ░░░░░░░░░░ 0%   (0/3)      │
  │ SECTION 8: Compliance         ░░░░░░░░░░ 0%   (0/3)      │
  │                                                           │
  │ OVERALL: 13/31 documents | 3 validated | 10 received      │
  │ BLOCKING: Material cert for heat H-42891 (supplier)       │
  │ NEXT ACTION: CMM inspection of serial range 001-025       │
  │                                                           │
  └──────────────────────────────────────────────────────────┘
```

### 3.3 Multi-Order Dashboard

```
MRB BUILDER DASHBOARD (all active orders):

  ┌──────────────────────────────────────────────────────────────┐
  │ ACTIVE ORDERS: 12 | READY TO SHIP: 2 | OVERDUE: 1           │
  ├──────────────────────────────────────────────────────────────┤
  │                                                               │
  │ PO-2027-001 | KDA        | DEFENCE | ACTIVE      | 45% ████ │
  │ PO-2027-002 | Equinor    | OIL_GAS | VALIDATING  | 90% ████ │
  │ PO-2027-003 | Nammo      | DEFENCE | COC_PENDING | 95% ████ │
  │ PO-2027-004 | Aker       | OIL_GAS | COLLECTING  | 70% ████ │
  │ PO-2027-005 | BAE        | DEFENCE | ACTIVE      | 30% ███░ │
  │ PO-2027-006 | Phys.Robot | MARITIME| READY       |100% ████ │
  │ PO-2027-007 | TechnipFMC | OIL_GAS | ACTIVE      | 55% ████ │
  │ PO-2027-008 | Saab       | DEFENCE | PARSING     |  5% █░░░ │
  │ ...                                                           │
  │                                                               │
  │ ALERTS:                                                       │
  │ ⚠ PO-2027-001: Material cert overdue (supplier: Sandvik)     │
  │ ⚠ PO-2027-004: ITP Hold Point #3 needs customer scheduling   │
  │ ✅ PO-2027-003: All docs validated — CoC ready for signature  │
  │ ✅ PO-2027-006: MRB complete — ready for shipment             │
  │                                                               │
  └──────────────────────────────────────────────────────────────┘
```

---

## SECTION 4: MRB ASSEMBLY PROCESS

### 4.1 Assembly Procedure

```
MRB ASSEMBLY (Stage 6):

  PREREQUISITE: Order state = COC_PENDING → MRB_ASSEMBLY
                (i.e., CoC has been signed)

  STEP 1: COLLECT all validated documents
    → Query aurelian-doc-validator for all documents with status VALIDATED
    → Verify count matches expected count from aurelian-sdrl-parser
    → Include the signed CoC from aurelian-coc-generator

  STEP 2: GENERATE cover page
    ┌────────────────────────────────────────────┐
    │     MANUFACTURING RECORD BOOK              │
    │                                            │
    │     MRB Number: AM-MRB-[YYYY]-[NNNNN]     │
    │     Order:      [PO Number]                │
    │     Customer:   [Customer Name]            │
    │     Part:       [Part Number / Name]       │
    │     Drawing:    [Drawing Number, Rev]      │
    │     Quantity:   [Qty]                      │
    │     Serial:     [Range or list]            │
    │     Class:      [DEFENCE / OIL_GAS]        │
    │     Date:       [DD Month YYYY]            │
    │                                            │
    │     Aurelian Manufacturing AS              │
    │     Org.nr: 835 679 632                    │
    │     Valer, Ostfold, Norway                 │
    │                                            │
    │     CONFIDENTIAL                           │
    └────────────────────────────────────────────┘

  STEP 3: GENERATE master document index
    │ Item │ Document Title │ Doc Ref │ Rev │ Pages │ Status │
    │──────│───────────────│─────────│─────│───────│────────│
    │ 1.1  │ MRB Cover     │ ...     │ 0   │ 1     │ ✓      │
    │ 1.2  │ Master Index  │ ...     │ 0   │ 2     │ ✓      │
    │ 3.1  │ Material Cert │ ...     │ 0   │ 3     │ ✓      │
    │ ...  │ ...           │ ...     │ ... │ ...   │ ...    │

  STEP 4: COMPILE documents in section order
    → Each section starts on a new page
    → Section divider pages with section title
    → Documents ordered per template structure
    → Page numbers continuous through entire MRB

  STEP 5: CREATE PDF/A package
    → Merge all documents into single PDF/A
    → Add bookmarks for each section and document
    → Add internal hyperlinks from index to documents
    → Verify PDF/A compliance
    → File size check (optimize if needed for transmission)

  STEP 6: QUALITY CHECK
    → Final page count verification
    → All bookmarks functional
    → All pages legible
    → Cover page information correct
    → Index matches actual contents
    → CoC present and signed

  STEP 7: RELEASE
    → QA release sign-off
    → Update order state: MRB_ASSEMBLY → READY
    → Notify shipping and sales
    → Generate electronic copy for customer portal
```

### 4.2 MRB Package Formats

```
OUTPUT FORMATS:

  PRIMARY: Single PDF/A file
    → Bookmarked, hyperlinked
    → Cover page → Index → Section 1 → ... → Section 8/7
    → Suitable for electronic delivery and archival
    → PDF/A-3 preferred (allows embedded original files)

  SECONDARY: Structured folder package
    → Individual files per document, organized by section
    → Useful for customer systems that ingest individual files
    → ZIP archive for transmission

  PHYSICAL: Printed hardcopy
    → Some defence contracts still require physical MRB
    → Printed, bound, delivered with shipment
    → Signed CoC original enclosed
```

---

## SECTION 5: ERP INTEGRATION (EPICOR)

### 5.1 Epicor ERP Document Flow

```
EPICOR INTEGRATION POINTS:

  INCOMING (External → Epicor → MRB):
  ┌──────────────────────────────────────────────┐
  │ Supplier sends material cert                  │
  │    ↓                                          │
  │ Goods receiving in Epicor                     │
  │    ↓                                          │
  │ Cert attached to PO receipt                   │
  │    ↓                                          │
  │ Cert linked to material lot/heat number       │
  │    ↓                                          │
  │ Material issued to production order(s)        │
  │    ↓                                          │
  │ MRB Builder queries: "which certs apply       │
  │ to order PO-2027-001?"                        │
  │    ↓                                          │
  │ Epicor returns: cert linked to heat H-42891   │
  │ which was issued to PO-2027-001               │
  │    ↓                                          │
  │ Cert routed to MRB Section 3                  │
  └──────────────────────────────────────────────┘

  KEY EPICOR MODULES:
    - Quality Management → NCR tracking, inspection results
    - DocStar Integration → Document management and retrieval
    - Advanced MES → Production tracking, machine data
    - Material Requirements → Material traceability
    - Purchase Management → PO receipts, supplier certs

  CRITICAL DESIGN DECISION:
    The MRB Builder does NOT duplicate documents stored in Epicor.
    It REFERENCES and RETRIEVES documents from Epicor when assembling the MRB.
    Single source of truth remains in Epicor for shared documents.
    Order-specific documents (CNC data, inspection reports) live in MRB directly.
```

### 5.2 Machine Data Integration

```
CNC/METROLOGY → MRB (Direct Route):

  MACHINE DATA COLLECTOR:
  ┌──────────────────────────────────────────────┐
  │ CNC Machine (e.g., MAZAK INTEGREX)            │
  │    ↓ (MQTT / OPC-UA / MTConnect)              │
  │ Machine Data Gateway                          │
  │    ↓                                          │
  │ Data tagged with:                             │
  │    - Machine ID                               │
  │    - Production Order number                  │
  │    - Part serial number                       │
  │    - Timestamp                                │
  │    - Operation number                         │
  │    ↓                                          │
  │ MRB Builder receives tagged data              │
  │    ↓                                          │
  │ Data placed in correct order's MRB:           │
  │    - Section 4 (manufacturing parameters)     │
  │    - Section 6 (in-process measurements)      │
  └──────────────────────────────────────────────┘

  METROLOGY DATA:
  ┌──────────────────────────────────────────────┐
  │ Metrology System (temp, vibration, etc.)       │
  │    ↓                                          │
  │ Continuous monitoring during production        │
  │    ↓                                          │
  │ Filtered for relevant events:                 │
  │    - Out-of-range alerts (logged)             │
  │    - Process stability records                │
  │    - Environmental condition logs             │
  │    ↓                                          │
  │ Tagged with production order + timestamp       │
  │    ↓                                          │
  │ Routed to order-specific MRB Section 4        │
  └──────────────────────────────────────────────┘

  INSPECTION ROOM DATA:
  ┌──────────────────────────────────────────────┐
  │ CMM (Coordinate Measuring Machine)             │
  │    ↓                                          │
  │ Measurement program executed per drawing       │
  │    ↓                                          │
  │ Results tagged with:                          │
  │    - Part serial number                       │
  │    - Drawing revision                         │
  │    - Inspection date and operator             │
  │    ↓                                          │
  │ Routed to order-specific MRB Section 6        │
  │ Also feeds: AS9102 FAIR Form 3 (if FAIR req) │
  └──────────────────────────────────────────────┘
```

---

## SECTION 6: IMPLEMENTATION ROADMAP

### 6.1 Phase 1 — Minimum Viable MRB (Production Start: August 2027)

```
PHASE 1 SCOPE (MVP — Aug 2027):

  WHAT'S BUILT:
    ✅ SDRL parsing: Template-based (Defence + Oil & Gas)
    ✅ Requirement matrix: Structured checklist per order
    ✅ Document collection: Manual upload to shared folder structure
    ✅ Validation: Checklist-driven with QA engineer review
    ✅ CoC generation: Template-based, semi-automated population
    ✅ MRB assembly: Manual compilation with standard structure
    ✅ PDF/A output: Single merged PDF with bookmarks

  WHAT'S MANUAL:
    ⚙ SDRL parsing requires QA engineer to extract requirements
    ⚙ Document collection involves manual file naming and placement
    ⚙ Validation uses checklist (not automated content checking)
    ⚙ CNC data manually exported and filed
    ⚙ ERP integration limited (may use shared network folders initially)

  TOOLS:
    → Claude Code skills (this skill ecosystem) for guidance and templates
    → Shared folder structure on network/SharePoint for document staging
    → Excel/SharePoint for status tracking
    → Word/PDF tools for CoC generation
    → Manual PDF merger for MRB assembly

  EXPECTED VOLUME: ~5-15 MRBs per month (5 CNC machines, initial orders)
```

### 6.2 Phase 2 — Semi-Automated MRB (Q1 2028)

```
PHASE 2 SCOPE (6 months after production start):

  UPGRADES:
    ✅ Epicor ERP operational → supplier docs flow through ERP
    ✅ Document collection: ERP-integrated for supplier documents
    ✅ CNC data: Automated export via machine data gateway
    ✅ CMM data: Automated export from inspection room
    ✅ Validation: Semi-automated (format and existence checks automated)
    ✅ CoC generation: Auto-populated from validated data
    ✅ MRB assembly: Template-driven with automated PDF compilation
    ✅ Status dashboard: Real-time order documentation status

  STILL MANUAL:
    ⚙ SDRL parsing for non-standard customer formats
    ⚙ Compliance validation (L4) — QA engineer review
    ⚙ Cross-document traceability verification (L5) — QA engineer
    ⚙ CoC signature (physical or basic electronic)

  TOOLS:
    → Epicor ERP with DocStar document management
    → Machine data gateway (MQTT/OPC-UA)
    → CMM software integration
    → SharePoint/OneDrive for document staging
    → Power Automate or similar for workflow automation
    → Custom dashboard (web-based)

  EXPECTED VOLUME: ~15-30 MRBs per month
```

### 6.3 Phase 3 — Intelligent MRB (Q3 2028)

```
PHASE 3 SCOPE (12 months after production start):

  UPGRADES:
    ✅ SDRL parsing: OCR + AI-assisted for any format
    ✅ Document collection: Fully automated for all machine-generated data
    ✅ Validation: Automated L1-L4 (content extraction and compliance check)
    ✅ Cross-reference: Automated traceability chain verification
    ✅ CoC generation: Fully automated with electronic signature
    ✅ MRB assembly: One-click compilation
    ✅ Customer portal: Self-service document access
    ✅ Predictive: Alerts for upcoming documentation needs

  STILL MANUAL:
    ⚙ Exception handling (non-standard requirements, disputes)
    ⚙ Customer-specific adaptations
    ⚙ NCR dispositions requiring engineering judgment

  TOOLS:
    → All Phase 2 tools
    → AI/ML document parsing (OCR + content extraction)
    → Digital signature platform (eIDAS compliant)
    → Customer portal (web application)
    → Advanced analytics and reporting

  EXPECTED VOLUME: ~30-60 MRBs per month (scaling to 20 CNC)
```

### 6.4 Phase 4 — Autonomous MRB (2029+)

```
PHASE 4 SCOPE (24+ months after production start):

  VISION:
    ✅ Zero-touch MRB for repeat orders with no deviations
    ✅ AI validates all documents including content compliance
    ✅ Digital twin integration: MRB updated in real-time during production
    ✅ Customer portal with real-time MRB status
    ✅ Predictive documentation: system knows what's needed before production starts
    ✅ Multi-site support (if Aurelian expands)
    ✅ API integration with customer systems (Kongsberg PLM, Equinor STID, etc.)

  HUMAN ROLE:
    → Exception handling only
    → Customer relationship and dispute resolution
    → Continuous improvement and system optimization
    → Audit response and certification maintenance

  EXPECTED VOLUME: ~60-100+ MRBs per month (20-25 CNC at scale)
```

---

## SECTION 7: QUALITY SYSTEM INTEGRATION

### 7.1 QMS Procedures Required

```
QMS PROCEDURES (to be created as part of ISO 9001/AS9100 implementation):

  AM-QP-MRB-001: MRB Management Procedure
    → Defines MRB structure, responsibilities, lifecycle
    → References this skill ecosystem for operational guidance

  AM-QP-MRB-002: SDRL Processing Procedure
    → How incoming SDRLs are received, parsed, and initialized
    → Roles: QA Engineer (owner), Production Manager (reviewer)

  AM-QP-MRB-003: Document Validation Procedure
    → 5-layer validation methodology
    → Accept/reject criteria per document type
    → Roles: QA Inspector (validator), QA Engineer (reviewer for exceptions)

  AM-QP-MRB-004: Certificate of Conformance Procedure
    → CoC generation, review, signature authority
    → Roles: QA Manager (signatory), QA Engineer (preparer)

  AM-QP-MRB-005: MRB Assembly and Release Procedure
    → Compilation, quality check, release, distribution
    → Roles: QA Engineer (assembler), QA Manager (releaser)

  AM-QP-MRB-006: Document Archival Procedure
    → Retention periods, format requirements, retrieval
    → Roles: Document Controller (custodian)
```

### 7.2 Certification Alignment

```
CERTIFICATION TIMELINE vs MRB CAPABILITY:

  ISO 9001 (Target: Q4 2027):
    → Phase 1 MRB capability sufficient
    → Checklist-based validation acceptable
    → Manual processes with documented procedures

  AS9100D (Target: Q3-Q4 2028):
    → Phase 2 MRB capability required
    → FAIR support mandatory (AS9102)
    → Configuration management integrated
    → Product safety and risk management documented

  AQAP 2110 (Target: Q3-Q4 2028):
    → Phase 2 MRB capability required
    → Government Quality Assurance (GQA) provisions
    → Counterfeit parts prevention measures
    → Flow-down requirements to sub-suppliers

  NORSOK M-650 (Target: Q2 2028):
    → Phase 2 MRB capability required
    → Manufacturer qualification documentation
    → ITP management operational
    → PMI procedures established
```

---

## SECTION 8: EXTERNAL SYSTEM CANDIDATES

### 8.1 Software Ecosystem Map

```
CORE SYSTEMS:

  ERP: Epicor Kinetic (initial candidate)
    → Manufacturing, inventory, purchasing, quality module
    → DocStar for document management
    → Advanced MES for production tracking

  CAD/CAM: Siemens NX or Mastercam
    → Drawing revision control feeds MRB Section 2/4
    → CNC program generation and verification

  CMM Software: PC-DMIS, Calypso, or PolyWorks
    → Measurement data export → MRB Section 6
    → AS9102 FAIR Form 3 data source

  Machine Monitoring: MAZAK iSMART / Smooth Monitor
    → Real-time CNC data → MRB Section 4
    → OPC-UA/MTConnect protocol

COMPLEMENTARY TOOLS (evaluate for Phase 2-3):

  DocBoss (O&G SDRL management):
    → Industry standard for oil & gas document control
    → SDRL parsing and tracking
    → Customer portal for document delivery
    → Consider if O&G volume justifies investment

  Net-Inspect (Aerospace FAIR):
    → AS9102 FAIR management
    → Integration with CMM data
    → Aerospace-specific compliance tracking
    → Consider if defence volume justifies investment

  Qualio / MasterControl (QMS):
    → Electronic quality management system
    → Document control, CAPA, NCR management
    → Audit trail and compliance reporting
    → Alternative: Epicor Quality module may suffice initially

  Power Automate / n8n:
    → Workflow automation for document routing
    → Integration glue between systems
    → Notification and escalation workflows
```

### 8.2 Build vs Buy Decision Framework

```
DECISION MATRIX:

  BUILD (custom within Epicor/middleware):
    → MRB assembly logic (unique to Aurelian's dual-industry model)
    → SDRL parser (Aurelian-specific requirement normalization)
    → Cross-industry CoC generator (Defence + O&G templates)
    → Real-time status dashboard
    → Machine data gateway routing logic

  BUY (commercial off-the-shelf):
    → ERP core (Epicor — don't build ERP)
    → CMM software (PC-DMIS/Calypso — don't build measurement software)
    → Document management/archival (DocStar or similar)
    → Electronic signature platform
    → PDF/A generation and merging tools

  EVALUATE (Phase 2-3 decision):
    → DocBoss for O&G (if volume >10 O&G orders/month)
    → Net-Inspect for aerospace (if volume >10 defence orders/month)
    → Full QMS platform (if Epicor Quality module insufficient)
```

---

## SECTION 9: RISK MANAGEMENT FOR MRB SYSTEM

### 9.1 MRB System Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Late document collection delays shipment | HIGH | MEDIUM | Real-time tracking dashboard, early warnings at 80% production complete |
| Invalid material cert accepted | HIGH | LOW | 5-layer validation, cross-reference checks, QA review |
| Wrong cert linked to wrong order (ERP error) | HIGH | LOW | Heat number verification, traceability chain validation |
| CNC data not captured (connectivity issue) | MEDIUM | MEDIUM | Manual backup procedure, store-and-forward data collection |
| Customer rejects MRB (missing requirement) | HIGH | LOW | Comprehensive SDRL parsing, pre-shipment customer review option |
| System failure during MRB assembly | MEDIUM | LOW | Cloud backup, manual assembly fallback procedure |
| Falsified documentation in supply chain | CRITICAL | LOW | Supplier audit program, PMI verification, EN 10204 3.2 for critical items |
| Regulatory change invalidates templates | MEDIUM | LOW | Annual review of standards, industry association membership |

### 9.2 Contingency: Manual Fallback

```
IF DIGITAL SYSTEM FAILS:

  The MRB Builder MUST have a fully manual fallback:
    1. Paper-based SDRL checklist (printed from Section 2 templates)
    2. Physical document collection in labelled folder per order
    3. Manual validation using printed checklists
    4. Word-based CoC template (pre-formatted)
    5. Manual PDF compilation using Adobe Acrobat
    6. Physical MRB binder for hardcopy delivery

  This fallback ensures:
    → No shipment is ever delayed because of IT failure
    → Quality of documentation is maintained regardless of system status
    → ISO 9001/AS9100 compliance is not dependent on specific software
```

---

## SECTION 10: METRICS AND KPIs

### 10.1 MRB Performance Metrics

```
OPERATIONAL KPIS:

  MRB Cycle Time:
    Definition: Days from PO receipt to MRB-ready
    Target (Phase 1): ≤ Production lead time + 3 days
    Target (Phase 3): ≤ Production lead time + 0 days (real-time)

  First-Pass Validation Rate:
    Definition: % of documents passing validation on first submission
    Target (Phase 1): > 80%
    Target (Phase 3): > 95%

  Customer Rejection Rate:
    Definition: % of MRBs rejected by customer
    Target: < 2% (industry benchmark: 5-10%)

  Document Collection Completeness at Production End:
    Definition: % of required documents collected when last part machined
    Target (Phase 1): > 70%
    Target (Phase 3): > 95%

  CoC Generation Time:
    Definition: Hours from validation-complete to signed CoC
    Target (Phase 1): ≤ 4 hours
    Target (Phase 3): ≤ 30 minutes (automated)

  MRB Assembly Time:
    Definition: Hours from signed CoC to final MRB package
    Target (Phase 1): ≤ 8 hours
    Target (Phase 3): ≤ 1 hour (automated)
```

---

## SECTION 11: REFERENCE DOCUMENTS

| Document | Location | Relevance |
|----------|----------|-----------|
| AM-SDRL-2026-001 Rev 1.0 | `Quality System Input/Supplier Quality and Document requirements/Shipment_Documentation_Requirements_SDRL_MRB.pdf` | Master SDRL/MRB requirements (81 pages) |
| Quality Certification Roadmap | `Aurelian_VDR/04_Technical/4.5_.../Quality_Certification_Roadmap_V1.md` | ISO 9001, AS9100, AQAP timeline |
| Production Timeline | `Aurelian_VDR/04_Technical/4.6_.../Production_Timeline_V1.md` | Production start and scaling milestones |
| Risk Register | `Aurelian_VDR/04_Technical/4.7_.../Risk_Register_V1.md` | Enterprise risk management |
| *02 Economic Tables & Projections* (VDR 02.04) | `Aurelian_VDR/02_Financial/2.4_.../02_Economic_Tables_Projections_REV8.docx` | Master financial document |
