# QUALITY MANUAL — REVISION 2 ADDENDUM

# Digital MRB Builder Integration

| Field | Value |
|-------|-------|
| **Document No.** | QM-001 (Addendum to Rev 1.0) |
| **Revision** | 2.0 |
| **Effective Date** | 2026-02-19 |
| **Approved By** | Managing Director |
| **Classification** | Internal / Controlled |
| **Supersedes** | QM-001 Rev 1.0 (in the sections listed below only) |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-01-15 | Quality Manager | Initial Release — QM-001 Quality Manual |
| **2.0** | **2026-02-19** | **Quality Manager** | **Addendum: Integration of Digital MRB Builder procedures (PR-008 through PR-013). New Sections 3.4A, 4.4.2A, 5.1A, 8.4A, 8.5.2A, 8.6A. Updated Procedure Index.** |

---

## 1. Purpose of This Addendum

This addendum formally integrates the Digital MRB Builder system into the Aurelian Manufacturing AS Quality Management System. It introduces six new procedures (PR-008 through PR-013) that govern the complete lifecycle of Manufacturing Record Books, from incoming material review through final archival.

This addendum SHALL be read in conjunction with QM-001 Rev 1.0. Where this addendum addresses a section of QM-001, this addendum takes precedence. All sections of QM-001 not addressed by this addendum remain in full effect.

**When QM-001 is next revised to a new full revision, the content of this addendum SHALL be incorporated into the main body and this addendum retired.**

---

## 2. Summary of Changes

### 2.1 New Procedures Added

| Procedure | Title | ISO 9001 Clause | Purpose |
|-----------|-------|-----------------|---------|
| **PR-008** | Incoming Material Review and Release | 8.4, 8.5.2, 8.6 | Pre-production quality gate for incoming materials. AI-assisted 5-point certificate validation, customer-specific requirement profiles, 3-way gate decision (RELEASED/REJECTED/REVIEW). |
| **PR-009** | SDRL Processing and MRB Management | 8.1, 8.2, 8.5.1 | Intake and parsing of Supplier Data Requirements Lists. Generation of order-specific MRB Index. MRB structure initialization. Document collection tracking. Order lifecycle management. |
| **PR-010** | Document Validation and Verification | 7.5, 8.6 | 5-layer validation of every document before MRB inclusion (Existence, Format, Completeness, Compliance, Traceability). Cross-document traceability chain verification. CoC prerequisite gate. |
| **PR-011** | Certificate of Conformance | 8.5.1, 8.6 | Generation, review, approval, and issuance of legally binding Certificates of Conformance for Defence and Oil & Gas deliveries. Signature authority management. |
| **PR-012** | MRB Assembly and Release | 8.6, 7.5.2, 7.5.3 | Final compilation of validated documents into a structured MRB package. Quality check. Release authorization. Delivery in electronic and physical formats. |
| **PR-013** | Document Archival and Retention | 7.5.2, 7.5.3 | Long-term preservation, backup, retrieval, and eventual disposition of all quality records. Minimum 15-year retention. Legal hold capability. |

### 2.2 Complete Procedure Index (Updated)

The following is the complete list of controlled procedures in the Aurelian Manufacturing AS Quality Management System:

| Procedure | Title | ISO 9001 Clause | Source |
|-----------|-------|-----------------|--------|
| PR-001 | Document Control | 7.5 | QM-001 Rev 1.0 |
| PR-002 | Internal Audit | 9.2 | QM-001 Rev 1.0 |
| PR-003 | Management Review | 9.3 | QM-001 Rev 1.0 |
| PR-004 | Nonconformance and CAPA | 10.2 | QM-001 Rev 1.0 |
| PR-005 | Production Planning | 8.1 | QM-001 Rev 1.0 |
| PR-006 | CNC Process Control | 8.5.1 | QM-001 Rev 1.0 |
| PR-007 | Customer Communication and Contract Review | 8.2 | QM-001 Rev 1.0 |
| **PR-008** | **Incoming Material Review and Release** | **8.4, 8.5.2, 8.6** | **This addendum** |
| **PR-009** | **SDRL Processing and MRB Management** | **8.1, 8.2, 8.5.1** | **This addendum** |
| **PR-010** | **Document Validation and Verification** | **7.5, 8.6** | **This addendum** |
| **PR-011** | **Certificate of Conformance** | **8.5.1, 8.6** | **This addendum** |
| **PR-012** | **MRB Assembly and Release** | **8.6, 7.5.2, 7.5.3** | **This addendum** |
| **PR-013** | **Document Archival and Retention** | **7.5.2, 7.5.3** | **This addendum** |

### 2.3 New Forms Added

| Form | Title | Procedure |
|------|-------|-----------|
| FM-008-01 | Material Receiving and Inspection Record | PR-008 |
| FM-008-02 | Material Requirement Profile | PR-008 |
| FM-008-03 | Gate Decision Record | PR-008 |
| FM-008-04 | Multi-Order Material Allocation Record | PR-008 |
| FM-009-01 | Order Requirement Matrix | PR-009 |
| FM-009-02 | ITP Tracker (Oil & Gas) | PR-009 |
| FM-009-03 | MRB Initialization Record | PR-009 |
| FM-009-04 | MRB Index (order-specific, SDRL-derived) | PR-009 |
| FM-010-01 | Correction Request | PR-010 |
| FM-010-02 | Document Validation Log | PR-010 |
| FM-010-03 | Cross-Document Traceability Verification Record | PR-010 |
| FM-010-04 | CoC Prerequisite Gate Checklist | PR-010 |
| FM-011-01 | CoC Register | PR-011 |
| FM-011-02 | CoC Revision/Void Record | PR-011 |
| FM-011-03 | Authorized Signatory Register | PR-011 |
| FM-012-01 | MRB Assembly Checklist (Prerequisites) | PR-012 |
| FM-012-02 | MRB Quality Check and Release Record | PR-012 |
| FM-012-03 | Customer Pre-Shipment Approval Record | PR-012 |
| FM-012-04 | MRB Delivery Confirmation | PR-012 |
| FM-013-01 | Archive Register | PR-013 |
| FM-013-02 | Archive Access Log | PR-013 |
| FM-013-03 | Disposition Request | PR-013 |
| FM-013-04 | Disposition Record | PR-013 |
| FM-013-05 | Annual Archive Integrity Report | PR-013 |

---

## 3. QM-001 Section Updates

The following sections of QM-001 Rev 1.0 are supplemented by this addendum.

### 3.1 Section 3.4 — Scope: Documentation and Delivery (Supplement)

**QM-001 Rev 1.0 Section 3.4** states that the QMS scope includes SDRL and MRB documentation requirements. This addendum formalizes and operationalizes that statement through six dedicated procedures.

**Add to Section 3.4:**

> The Digital MRB Builder system is an integrated component of the QMS, providing structured management of Manufacturing Record Books from order intake to final archival. The system supports two primary industry frameworks:
>
> - **Defence/Aerospace:** AS9100D / AQAP 2110 — 8-section MRB structure with AS9102 FAIR, EN 10204 3.1/3.2 certificates, and export compliance declarations
> - **Oil & Gas/Energy:** NORSOK M-650 / API — 7-section MDR structure with ITP Hold/Witness/Review points, PMI verification, and NORSOK Material Data Sheets
>
> The MRB lifecycle is governed by PR-008 through PR-013, which collectively ensure that every shipped product is accompanied by a complete, validated, traceable documentation package.

### 3.2 Section 4.4.2 — Context of the Organization: Documented Information (Supplement)

**Add to Section 4.4.2:**

> The QMS document hierarchy is extended with order-specific documentation:
>
> | Level | Document Type | Example |
> |-------|--------------|---------|
> | Level 1 | Quality Manual | QM-001 |
> | Level 2 | Procedures | PR-001 through PR-013 |
> | Level 3 | Work Instructions | WI-xxx (to be developed) |
> | Level 4 | Forms and Records | FM-xxx (per procedure) |
> | **Level 5** | **Order-Specific Documents** | **MRB Index (FM-009-04), MRB Package, CoC** |
>
> Order-specific documents (Level 5) are generated per order from the SDRL and are variable from order to order. They are controlled through the procedures that generate them (PR-009 through PR-012) and retained per PR-013.

### 3.3 Section 5.1 — Leadership: Roles and Responsibilities (Supplement)

**Add the following Digital MRB Builder responsibilities to existing roles:**

| Role | Additional Responsibilities (MRB Builder) |
|------|------------------------------------------|
| **Quality Manager** | Owns PR-008 through PR-013. Maintains Authorized Signatory Register (FM-011-03). Approves elevated MRB releases. Authorizes record disposition. Signs defence CoCs. Manages Material Requirement Profiles. |
| **QA Engineer** | Parses SDRLs. Generates MRB Index. Validates documents (5-layer framework). Generates CoCs. Assembles and releases MRBs. Maintains archive. Issues Correction Requests. Performs pre-production material gate review. |
| **Production Manager** | Ensures production-generated documents (CNC data, process sheets, in-process records) are submitted for validation. Coordinates shipment timing with MRB readiness. Confirms production data completeness. |
| **Commercial Manager** | Communicates SDRL/MRB requirements during contract review. Coordinates customer-specific Material Requirement Profiles. Manages customer pre-shipment review. Handles waiver communications. |
| **Purchasing** | Manages incoming supplier documentation. Coordinates with suppliers on material certificate corrections. Ensures material certificates are registered in ERP upon goods receiving. |

### 3.4 Section 8.4 — Control of Externally Provided Processes, Products and Services (Supplement)

**Add to Section 8.4:**

> All incoming materials and their associated documentation are subject to the pre-production Material Gate review defined in PR-008. No material shall be released to manufacturing until:
>
> 1. The material certificate (EN 10204) has been received and registered in the ERP
> 2. The 5-point certificate check has been completed (certificate type, chemical composition, mechanical properties, supplementary tests, traceability/integrity)
> 3. A gate decision has been recorded (RELEASED, REJECTED, or REVIEW)
> 4. Physical inspection (visual, dimensional, PMI if required) confirms the material matches the certificate
>
> Material Requirement Profiles define customer-specific acceptance criteria. The same material may require different validation against different customer requirements. PR-008 governs this process.

### 3.5 Section 8.5.2 — Identification and Traceability (Supplement)

**Add to Section 8.5.2:**

> Traceability is maintained from raw material receipt through final delivery via the Digital MRB Builder:
>
> ```
> Material Certificate (heat number)
>     → Goods Receiving Record (PR-008)
>         → Material Traceability Matrix (ERP)
>             → Manufacturing Records (CNC data, process sheets)
>                 → Inspection Reports (dimensional, NDT, hardness)
>                     → FAIR Form 3 (if defence)
>                         → Certificate of Conformance (PR-011)
>                             → Manufacturing Record Book (PR-012)
> ```
>
> Cross-document traceability is verified as part of the 5-layer validation (PR-010 Section 6.11). The traceability chain is verified at minimum across: PO number, part number, drawing revision, material heat numbers, serial numbers, and chronological date consistency.
>
> Where a single material serves multiple orders, the ERP manages the one-to-many relationship (one certificate → multiple orders), and each order's MRB receives a validated copy linked to that specific order (PR-008 Section 6.6).

### 3.6 Section 8.6 — Release of Products and Services (Supplement)

**Add to Section 8.6:**

> Product release requires BOTH production completion AND documentation completion:
>
> | Gate | Requirement | Procedure |
> |------|------------|-----------|
> | Material release (pre-production) | Material gate decision = RELEASED | PR-008 |
> | Document validation complete | All MRB documents = VALIDATED, WAIVED, or N/A | PR-010 |
> | CoC signed | Certificate of Conformance issued and signed by authorized signatory | PR-011 |
> | MRB released | Assembled MRB passes quality check and is formally released | PR-012 |
>
> No product shall ship without a released MRB accompanying it (electronically and/or physically as specified in the SDRL).
>
> The order state machine (PR-009 Section 6.8) tracks the progression: NEW → PARSING → ACTIVE → COLLECTING → VALIDATING → COC_PENDING → MRB_ASSEMBLY → READY → SHIPPED → ARCHIVED.

### 3.7 Section 7.5.3 — Control of Documented Information: Retention (Supplement)

**Add to Section 7.5.3:**

> Retention of order-specific quality records (MRBs, CoCs, material certificates, inspection reports) is governed by PR-013. Minimum retention is 15 years from shipment date, with customer-specific and regulatory extensions:
>
> | Industry | Typical Retention |
> |----------|-------------------|
> | Defence/Aerospace | Product lifetime + 5 years (25–30 years typical) |
> | Oil & Gas | 15 years or field design life + 5 years |
> | Nuclear | Product lifetime + 10 years (40+ years) |
> | Maritime | Class society requirements (10–15 years typical) |
>
> Archive integrity is verified annually through sampling (10% of archived MRBs, checksum and readability verification). Backup strategy: real-time replication + daily incremental + weekly full + annual snapshot.
>
> Disposition of expired records requires Quality Manager approval and verification that no legal hold, customer claim, or ongoing audit applies (PR-013 Section 6.9).

---

## 4. MRB Pipeline Integration Map

The following shows how the new procedures (PR-008 through PR-013) integrate with the existing QMS procedures (PR-001 through PR-007) and the order lifecycle:

```
CUSTOMER ORDER ARRIVES
        │
        ▼
PR-007: Contract Review
  └── SDRL identified and captured
        │
        ▼
PR-009: SDRL Processing ──→ MRB Index generated (order-specific)
  └── MRB structure initialized
  └── Document collection tracking begins
        │
        ├── Materials ordered ──→ PR-008: Material Gate
        │                          └── 5-point certificate check
        │                          └── Gate decision: RELEASED/REJECTED/REVIEW
        │                          └── Material released to production
        │
        ├── Production starts ──→ PR-005: Production Planning
        │                          PR-006: CNC Process Control
        │                          └── CNC data, process sheets → direct to MRB
        │
        ├── Documents collected ──→ PR-010: Document Validation
        │                            └── 5-layer validation per document
        │                            └── Correction Requests issued for failures
        │                            └── Cross-document traceability verified
        │
        ├── NCRs (if any) ──→ PR-004: Nonconformance and CAPA
        │                      └── Dispositions fed to CoC deviation section
        │
        ▼
All documents validated
        │
        ▼
PR-011: CoC Generation
  └── Prerequisite gate verified
  └── CoC populated from validated data
  └── Authorized signatory signs
        │
        ▼
PR-012: MRB Assembly
  └── MRB Index finalized (page numbers added)
  └── Documents compiled into PDF/A
  └── Quality check (10 points)
  └── Release decision
        │
        ▼
SHIPMENT (product + MRB)
        │
        ▼
PR-013: Archival
  └── MRB archived (Active → Deep after 2 years)
  └── 15+ year retention
  └── Annual integrity checks

SUPPORTING (continuous):
  PR-001: Document Control (governs all QMS documents)
  PR-002: Internal Audit (audits all procedures including PR-008–013)
  PR-003: Management Review (reviews KPIs from all procedures)
```

---

## 5. Implementation Notes

### 5.1 Phased Deployment

The new procedures are designed for phased implementation that begins well before first production. The MRB Builder system shall be developed and tested during the facility build period (Q2 2026 – Q2 2027) so that a well-tested, validated system is operational at production start (Q3 2027).

| Phase | Timing | Procedures Active | Capability |
|-------|--------|-------------------|------------|
| **Phase 0: Simulation & Build** | Q2–Q4 2026 | PR-009, PR-010, PR-013 (simulated) | Core MRB engine development. Simulated SDRLs, material certificates, and mock MRB lifecycle runs. QMS procedure dry-runs. ERP selection and API design. All simulation-based — no production data. |
| **Phase 0.5: Integration & Testing** | Q1–Q2 2027 | All PR-008 through PR-013 (test mode) | ERP integration testing. Real CNC data available when machines arrive (Q2 2027). End-to-end dry runs. UAT with QA engineers. Material Gate live testing with sample materials. System validated and ready by Q3 2027. |
| **Phase 1: Production MVP** | Q3 2027 (first production) | All PR-008 through PR-013 (live) | Tested system goes live with first real MRBs. Semi-automated SDRL parsing. Assisted validation (L1–L3). 5 CNC machines, 5–15 MRBs/month. |
| **Phase 2: Intelligent** | Q1–Q3 2028 | All, with automation enhancements | Full ERP + CNC auto-export. AI-assisted SDRL parsing and L1–L4 validation. Electronic signatures. Real-time dashboards. Customer portal (pilot). 15–30 MRBs/month. |
| **Phase 3: Autonomous** | 2029+ | All, fully integrated | Zero-touch for repeat orders. Digital twin integration. Customer system APIs. Full customer and supplier portals. Event bus architecture. Multi-site support. 60–100+ MRBs/month. |

### 5.2 Training Requirements

All personnel with MRB Builder responsibilities SHALL be trained on the applicable procedures before executing tasks:

| Role | Required Training |
|------|-------------------|
| QA Engineers | PR-008 through PR-013 (all procedures) |
| Quality Manager | PR-008 through PR-013 (all procedures) |
| Production Manager | PR-008 (material release awareness), PR-009 (document submission), PR-012 (shipment coordination) |
| Commercial Manager | PR-007 (existing, SDRL capture), PR-009 (SDRL awareness), PR-011 (CoC customer requirements) |
| Purchasing | PR-008 (material gate, supplier coordination) |
| CNC Operators | Awareness training: what data goes to the MRB and when |

Training records maintained per QM-001 Section 7.2 requirements.

### 5.3 Internal Audit Integration

PR-002 (Internal Audit) audit schedule SHALL include coverage of PR-008 through PR-013. Suggested audit frequency:

| Procedure | Audit Frequency | Focus Areas |
|-----------|----------------|-------------|
| PR-008 | Annually | Gate decision accuracy, profile currency, rejected material handling |
| PR-009 | Annually | SDRL parsing accuracy, MRB Index completeness, order state tracking |
| PR-010 | Semi-annually | Validation layer effectiveness, Correction Request closure time, traceability integrity |
| PR-011 | Annually | CoC accuracy, deviation declaration completeness, signatory authority compliance |
| PR-012 | Annually | MRB quality check effectiveness, customer rejection rate, delivery timeliness |
| PR-013 | Annually | Archive integrity, backup verification, retention compliance |

### 5.4 Management Review Inputs

PR-003 (Management Review) SHALL include the following additional inputs from the MRB Builder system:

| Input | Source | Frequency |
|-------|--------|-----------|
| Material gate KPIs (cycle time, first-pass rate, post-release NCRs) | PR-008 | Quarterly |
| SDRL processing metrics | PR-009 | Quarterly |
| Document validation KPIs (first-pass rate, CR closure time, traceability integrity) | PR-010 | Quarterly |
| CoC KPIs (cycle time, first-time accuracy, post-shipment corrections) | PR-011 | Quarterly |
| MRB assembly KPIs (cycle time, quality check pass rate, customer rejection rate) | PR-012 | Quarterly |
| Archive KPIs (completeness, retrieval time, integrity check results) | PR-013 | Annually |

---

## 6. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Prepared By | Quality Manager | _______ | _______ |
| Reviewed By | Production Manager | _______ | _______ |
| Approved By | Managing Director | _______ | _______ |

This document is controlled. Printed copies are uncontrolled unless stamped "CONTROLLED COPY" in red.

---

**Distribution:**

- Quality Manager (controlled copy)
- Production Manager (controlled copy)
- Commercial Manager (controlled copy)
- Engineering Manager (controlled copy)
- Managing Director (controlled copy)
- All QA Engineers (controlled copy)
- Document control archive (master)
