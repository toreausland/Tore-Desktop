# MRB ASSEMBLY AND RELEASE

| Field | Value |
|-------|-------|
| **Document No.** | PR-012 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-19 |
| **Approved By** | Quality Manager |
| **Classification** | Internal |
| **ISO 9001 Clause** | 8.6, 7.5.2, 7.5.3 |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-19 | Quality Manager | Initial Release |

---

## 1. Purpose

This procedure defines the assembly, quality check, release, and delivery of the final Manufacturing Record Book (MRB) or Manufacturing Data Record (MDR). The MRB is the comprehensive compilation of all validated quality records for a specific order, assembled into a structured package that accompanies the product to the customer.

This is Stage 6 of the Digital MRB Builder pipeline — the final compilation step after all documents have been validated (PR-010) and the Certificate of Conformance has been signed (PR-011).

## 2. Scope

This procedure applies to:

- Assembly of Defence MRBs (8-section structure, AS9100/AQAP 2110)
- Assembly of Oil & Gas MDRs (7-section structure, NORSOK/API)
- Assembly of Maritime and general engineering MRBs
- Quality check of assembled MRBs before release
- Release decision and authorization
- Delivery in electronic and/or physical format
- Handover to PR-013 (Document Archival and Retention)

## 3. References

| Document | Title |
|----------|-------|
| QM-001 | Quality Manual |
| PR-009 | SDRL Processing and MRB Management |
| PR-010 | Document Validation and Verification |
| PR-011 | Certificate of Conformance |
| PR-013 | Document Archival and Retention |
| AM-SDRL-2026-001 | Shipment Documentation Requirements (SDRL/MRB) |
| ISO 19005-3:2012 | Document Management — PDF/A-3 |

## 4. Definitions

| Term | Definition |
|------|-----------|
| **MRB** | Manufacturing Record Book — the comprehensive compilation of all quality records for a specific Defence or general engineering order |
| **MDR** | Manufacturing Data Record — Oil & Gas equivalent term for MRB, used interchangeably in this procedure |
| **MRB Package** | The final assembled MRB in its delivery format (PDF/A, structured folder, or physical hardcopy) |
| **Section Divider** | A page inserted at the beginning of each MRB section identifying the section number and title |
| **Master Document Index** | The table at the front of the MRB listing every document with its reference, revision, page count, and status |
| **PDF/A-3** | An ISO-standardized archival PDF format that allows embedded original files and ensures long-term readability |
| **MRB Release** | The formal decision that the assembled MRB is complete, accurate, and ready for delivery with the product |

## 5. Responsibilities

| Role | Responsibility |
|------|---------------|
| **Quality Manager** | Owns this procedure. Approves MRB release for complex/critical orders. Reviews MRBs for first-time customers. Resolves disputes on MRB content. |
| **QA Engineer** | Assembles the MRB. Generates cover page and master index. Performs quality check. Releases standard MRBs. Coordinates delivery format with customer. |
| **Commercial Manager** | Communicates MRB delivery requirements with customer (format, delivery method, number of copies). Notifies customer when MRB is ready. |
| **Production Manager** | Confirms all production data has been submitted and validated before MRB assembly. Coordinates shipment timing with MRB readiness. |
| **Shipping/Logistics** | Delivers physical MRB with product shipment. Manages packaging of physical MRB copies. |

## 6. Procedure

### 6.1 Assembly Prerequisites

MRB assembly SHALL NOT commence until:

1. Order state is **MRB_ASSEMBLY** (set when CoC is signed per PR-011)
2. All documents in the MRB structure have status **VALIDATED**, **WAIVED**, or **NOT_APPLICABLE** (per PR-010)
3. The signed CoC is available (per PR-011)
4. No open CRITICAL NCRs exist for the order

The QA Engineer verifies these prerequisites using Form FM-012-01 (MRB Assembly Checklist).

### 6.2 MRB Numbering

MRB numbers are assigned during MRB initialization (PR-009 Section 6.6):

```
FORMAT: AM-MRB-[YYYY]-[NNNNN]

  AM       = Aurelian Manufacturing
  MRB      = Manufacturing Record Book
  YYYY     = Year of order entry
  NNNNN    = Sequential number (5 digits, zero-padded)
```

One MRB per order/shipment. The MRB number is referenced on the CoC for traceability.

### 6.3 Assembly Step 1 — Collect All Validated Documents

1. QA Engineer queries the Document Validation Log (Form FM-010-02) for all documents with status VALIDATED for this order
2. Verify the count of validated documents matches the expected count from the Order Requirement Matrix (Form FM-009-01)
3. Include the signed CoC from PR-011
4. Include any customer-approved waivers for documents with status WAIVED
5. Confirm all NOT_APPLICABLE designations have documented justification

### 6.4 Assembly Step 2 — Generate Cover Page

The cover page is the first page of the MRB and SHALL contain:

| Field | Content |
|-------|---------|
| Title | MANUFACTURING RECORD BOOK (Defence) or MANUFACTURING DATA RECORD (Oil & Gas) |
| MRB Number | AM-MRB-[YYYY]-[NNNNN] |
| Order Reference | Purchase Order number |
| Customer | Customer name |
| Part Number | Part number from PO/drawing |
| Part Name | Description from PO/drawing |
| Drawing | Drawing number and revision |
| Material | Material specification |
| Quantity | Delivered quantity |
| Serial Numbers | List or range |
| Classification | DEFENCE / OIL & GAS / MARITIME / STANDARD |
| Date | Date of MRB assembly (DD Month YYYY format) |
| Company | Aurelian Manufacturing AS |
| Org. Number | 835 679 632 |
| Location | Valer, Ostfold, Norway |
| Marking | "CONFIDENTIAL" (for investor/defence documents) |

### 6.5 Assembly Step 3 — Finalize the Master Document Index

**Critical principle:** The MRB Index is NOT created at assembly time. It was generated from the SDRL at MRB initialization (PR-009 Section 6.6) and has been the live tracking document throughout the order lifecycle. The SDRL defines the index — every order has a different index because every SDRL specifies a different set of document requirements.

At assembly, the QA Engineer **finalizes** the existing MRB Index (Form FM-009-04) into the Master Document Index for inclusion in the MRB:

**Finalization actions:**

1. Take the live MRB Index (which has been updated throughout collection and validation)
2. Confirm all line items have final status: VALIDATED, WAIVED, or NOT_APPLICABLE (no PENDING or RECEIVED items remaining)
3. Add the following assembly-time fields to each line item:

| Column | Content | When Added |
|--------|---------|------------|
| Item | MRB line item number (e.g., 1.1, 3.2, 6.1) | At initialization (PR-009) |
| Section | MRB section number | At initialization (PR-009) |
| Document Title | Title of the document | At initialization (PR-009) |
| Document Reference | Unique document reference number | At validation (PR-010) |
| Revision | Document revision | At validation (PR-010) |
| **Pages** | **Number of pages in the compiled MRB** | **At assembly (this step)** |
| **Page Start** | **Starting page number in the compiled MRB** | **At assembly (this step)** |
| Status | VALIDATED / WAIVED / N/A | At validation (PR-010) |

4. Format the finalized index for inclusion as the first content page(s) of the MRB

**The finalized Master Document Index is order-specific — it reflects exactly the SDRL requirements for this order, no more and no less.**

The index is organized by the MRB section structure applicable to the order classification:

**Defence (8 sections):**

| Section | Title |
|---------|-------|
| 1 | Identification and Index |
| 2 | Contract Documentation |
| 3 | Material Documentation |
| 4 | Manufacturing Process Documentation |
| 5 | Special Process Documentation |
| 6 | Inspection Documentation |
| 7 | Test Documentation |
| 8 | Compliance Declarations |

**Oil & Gas (7 sections):**

| Section | Title |
|---------|-------|
| 1 | General Information |
| 2 | Purchase and Technical Requirements |
| 3 | Material Documentation |
| 4 | Manufacturing Records |
| 5 | Testing and Inspection |
| 6 | Compliance Documentation |
| 7 | Preservation and Shipping |

**Note:** Sections with no applicable documents (all items N/A) may be omitted from the index with documented justification, or retained with "No documents applicable" notation — per customer preference.

### 6.6 Assembly Step 4 — Compile Documents in Section Order

1. Each MRB section starts on a new page
2. A **Section Divider Page** is inserted before each section containing:
   - Section number
   - Section title
   - Number of documents in section
3. Documents are ordered within each section per the template structure defined in PR-009
4. Page numbers are continuous through the entire MRB (starting from cover page = page 1)
5. Each document retains its original formatting — documents are NOT reformatted

### 6.7 Assembly Step 5 — Create PDF/A Package

The primary MRB delivery format is a single PDF/A file:

1. Merge all documents (cover page → index → section 1 → ... → final section) into a single PDF
2. Ensure PDF/A-3 compliance (ISO 19005-3:2012):
   - All fonts embedded
   - No external references or links
   - Color spaces properly defined
   - Metadata complete (title, author, creation date)
3. Add **bookmarks** for:
   - Cover page
   - Master document index
   - Each section divider
   - Each individual document
4. Add **internal hyperlinks** from the master document index to each document location
5. Verify PDF/A compliance using a validation tool
6. Check file size — optimize for electronic transmission if necessary (target: < 50 MB; split if larger)

**Embedded originals (PDF/A-3 feature):**

Where technically feasible, embed the original source files (native Excel, CMM output, etc.) within the PDF/A-3 as embedded file attachments. This allows customers with compatible readers to extract original files.

### 6.8 Assembly Step 6 — Quality Check

Before release, the QA Engineer performs a quality check on the assembled MRB:

| Check | Criteria | Result |
|-------|----------|--------|
| Page count | Total page count matches expected (index + all documents) | PASS / FAIL |
| Bookmarks | All bookmarks functional and correctly linked | PASS / FAIL |
| Legibility | All pages legible (no blank pages, no corrupted content) | PASS / FAIL |
| Cover page | All fields correct and complete | PASS / FAIL |
| Index accuracy | Index matches actual MRB contents (every listed document is present at the listed location) | PASS / FAIL |
| Section order | Documents in correct section and correct order per template | PASS / FAIL |
| CoC present | Signed CoC is included in the correct section | PASS / FAIL |
| CoC references | MRB number on CoC matches this MRB | PASS / FAIL |
| Serial numbers | Serial numbers on CoC match inspection reports and manufacturing records | PASS / FAIL |
| Completeness | No PENDING or RECEIVED documents remaining (all VALIDATED, WAIVED, or N/A) | PASS / FAIL |

Record quality check results on Form FM-012-02 (MRB Quality Check Record).

If ANY check fails: correct the issue and re-check. Do NOT release an MRB with known deficiencies.

### 6.9 Assembly Step 7 — Release Decision

**Standard Release (QA Engineer authority):**

For standard and repeat orders with no deviations:

1. QA Engineer confirms all quality checks PASS
2. QA Engineer signs the MRB release on Form FM-012-02
3. Order state updated: MRB_ASSEMBLY → READY

**Elevated Release (Quality Manager review required):**

Quality Manager review and approval is required for:

- First order from a new customer
- Defence/AQAP orders
- Orders with accepted deviations (use-as-is or repair dispositions)
- Orders where the customer has specified "document review before shipment"
- Orders where any documents have WAIVED status

For elevated release:

1. QA Engineer presents the assembled MRB to Quality Manager
2. Quality Manager reviews the MRB with focus on:
   - Deviation declarations and customer approvals
   - WAIVED document justifications
   - Overall MRB completeness and presentation quality
3. Quality Manager signs the MRB release on Form FM-012-02
4. Order state updated: MRB_ASSEMBLY → READY

### 6.10 Delivery Formats

| Format | Description | When Used |
|--------|-------------|-----------|
| **PDF/A (primary)** | Single bookmarked, hyperlinked PDF/A-3 file | All orders (standard electronic delivery) |
| **Structured folder** | Individual files per document, organized by section, delivered as ZIP archive | When customer systems require individual files for ingestion |
| **Physical hardcopy** | Printed, bound, delivered with shipment; signed CoC original enclosed | Defence contracts that require physical MRB; customer request |
| **Customer portal** | Electronic upload to customer documentation portal | When customer provides portal access |

**Delivery rules:**

1. The QA Engineer confirms the required delivery format(s) from the SDRL (parsed in PR-009)
2. If physical hardcopy is required, specify the number of copies (typically: 1 with shipment, 1 to customer quality department, 1 retained by Aurelian)
3. Physical MRBs are printed single-sided on A4 paper, bound with cover, and clearly marked with MRB number on the spine
4. Electronic delivery via email: maximum 25 MB per attachment; split into volumes if necessary
5. All delivery formats contain identical content

### 6.11 Customer Pre-Shipment Review

When the customer or contract requires document review BEFORE shipment:

1. QA Engineer prepares the MRB in electronic format
2. Commercial Manager transmits the MRB to the customer for review
3. Customer review period per contract terms (typically 5–10 business days)
4. If customer approves: proceed with shipment
5. If customer requests corrections:
   - QA Engineer identifies the corrections needed
   - Corrections are made and documents re-validated (per PR-010)
   - MRB is re-assembled with corrected documents
   - New quality check performed
   - Revised MRB re-submitted to customer
6. Customer approval documented on Form FM-012-03

**Important:** The order state remains at READY until shipment occurs. Customer pre-shipment review does not change the order state.

### 6.12 Shipment Release

When the MRB is ready and customer approval obtained (if required):

1. Production Manager confirms product is ready for shipment
2. QA Engineer confirms MRB is released (order state = READY)
3. Shipping/Logistics packages the physical MRB with the product (if physical delivery required)
4. Electronic MRB is transmitted to customer per agreed method
5. Delivery confirmation recorded:
   - Physical: shipping document reference, courier tracking
   - Electronic: email delivery receipt, portal upload confirmation
6. Order state updated: READY → SHIPPED
7. MRB package handed over to PR-013 (Document Archival and Retention)

### 6.13 Post-Delivery Corrections

If the customer identifies a document issue after MRB delivery:

1. Customer notification is logged as a formal Correction Request
2. QA Engineer investigates the reported issue
3. If a document error exists:
   - Corrected document is validated per PR-010
   - A **Supplementary MRB Package** is issued containing only the corrected document(s) and an updated index
   - Supplementary package is numbered: AM-MRB-[YYYY]-[NNNNN]-SUP-[N]
   - Original MRB is NOT recalled (it is marked "Supplemented" in the archive)
4. If a CoC correction is needed: new CoC is issued per PR-011 Section 6.11
5. Post-delivery corrections are tracked as a KPI and fed back into the validation process improvement

## 7. Records

| Form | Title | Retention |
|------|-------|-----------|
| FM-012-01 | MRB Assembly Checklist (Prerequisites) | Per order archival requirement (minimum 15 years) |
| FM-012-02 | MRB Quality Check and Release Record | Per order archival requirement (minimum 15 years) |
| FM-012-03 | Customer Pre-Shipment Approval Record | Per order archival requirement (minimum 15 years) |
| FM-012-04 | MRB Delivery Confirmation | Per order archival requirement (minimum 15 years) |

## 8. Key Performance Indicators

| KPI | Target | Measured |
|-----|--------|----------|
| MRB assembly cycle time | < 2 business days from CoC signature to MRB release | Monthly |
| MRB quality check first-pass rate | > 95% of MRBs pass quality check without corrections | Monthly |
| Customer pre-shipment review rejection rate | < 5% of MRBs rejected at customer review | Quarterly |
| Post-delivery corrections | < 2% of shipped MRBs require supplementary packages | Quarterly |
| Shipment delay due to MRB | 0 shipments delayed due to MRB not ready | Monthly |

## 9. Flowchart

```
CoC signed (PR-011)
Order state = MRB_ASSEMBLY
            │
            ▼
┌─────────────────────────┐
│ Verify Assembly          │──FAIL──→ Resolve prerequisites
│ Prerequisites            │
└───────────┬─────────────┘
            │ PASS
            ▼
┌─────────────────────────┐
│ Step 1: Collect all      │
│ validated documents      │
│ Step 2: Generate cover   │
│ Step 3: Finalize index   │
│ Step 4: Compile in order │
│ Step 5: Create PDF/A     │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Step 6: Quality Check    │──FAIL──→ Correct and re-check
│ (10-point verification)  │
└───────────┬─────────────┘
            │ PASS
            ▼
┌─────────────────────────┐
│ Step 7: Release Decision │
│ Standard → QA Engineer   │
│ Elevated → Quality Mgr   │
└───────────┬─────────────┘
            │ RELEASED
            ▼
   Order state → READY
            │
            ▼
   Customer pre-shipment
   review required?
      │           │
     YES          NO
      │           │
      ▼           │
   Submit to      │
   customer       │
      │           │
   Approved? ──NO─→ Correct and re-submit
      │
     YES
      │           │
      ▼           ▼
   Ship product + MRB
   (physical and/or electronic)
            │
            ▼
   Order state → SHIPPED
            │
            ▼
   Handover to PR-013 (Archive)
```

## 10. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Prepared By | Quality Manager | _______ | _______ |
| Reviewed By | Production Manager | _______ | _______ |
| Approved By | Managing Director | _______ | _______ |

This document is controlled. Printed copies are uncontrolled unless stamped "CONTROLLED COPY" in red.
