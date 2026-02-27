# DOCUMENT ARCHIVAL AND RETENTION

| Field | Value |
|-------|-------|
| **Document No.** | PR-013 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-19 |
| **Approved By** | Quality Manager |
| **Classification** | Internal |
| **ISO 9001 Clause** | 7.5.2, 7.5.3 |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-19 | Quality Manager | Initial Release |

---

## 1. Purpose

This procedure defines the archival, retention, protection, retrieval, and eventual disposition of all quality records generated throughout the manufacturing and documentation lifecycle. It ensures that Manufacturing Record Books (MRBs), material certificates, inspection records, Certificates of Conformance, and all associated quality documents are preserved in a manner that meets contractual, regulatory, and legal requirements.

This is Stage 7 of the Digital MRB Builder pipeline — the final stage ensuring long-term preservation and retrievability of complete quality records.

## 2. Scope

This procedure applies to:

- All completed and shipped Manufacturing Record Books (MRBs/MDRs)
- All Certificates of Conformance (CoCs) and Declarations of Conformity (DoCs)
- All material certificates (EN 10204) retained for traceability
- All inspection and test reports
- All AS9102 FAIR packages
- All ITP sign-off records
- All PMI reports
- All NCR and CAPA records associated with production orders
- Material Requirement Profiles (PR-008)
- Order Requirement Matrices (PR-009)
- Validation logs and Correction Requests (PR-010)
- ERP-linked quality records
- Quality Management System documents (manuals, procedures, work instructions, forms)

## 3. References

| Document | Title |
|----------|-------|
| QM-001 | Quality Manual |
| PR-001 | Document Control |
| PR-004 | Nonconformance and CAPA |
| PR-008 | Incoming Material Review and Release |
| PR-009 | SDRL Processing and MRB Management |
| PR-010 | Document Validation and Verification |
| PR-011 | Certificate of Conformance |
| PR-012 | MRB Assembly and Release |
| ISO 9001:2015 | Clause 7.5 — Documented Information |
| AS9100D | Clause 7.5 — Documented Information (Aviation, Space, Defence) |
| AQAP 2110 | NATO Quality Assurance Requirements |
| NORSOK Z-001 | Documentation for Operation (DFO) |
| ISO 19005-3:2012 | PDF/A-3 — Document Management |
| Norwegian Bookkeeping Act | Bokforingsloven — retention of business records |
| Norwegian Archives Act | Arkivlova — public records retention |
| EU GDPR | General Data Protection Regulation (personal data in records) |

## 4. Definitions

| Term | Definition |
|------|-----------|
| **Archive** | The long-term storage of completed quality records in a secure, retrievable, and protected environment |
| **Retention Period** | The minimum time a record must be preserved before it may be considered for disposition |
| **Disposition** | The authorized destruction or transfer of records after the retention period has expired |
| **Active Archive** | Records for orders shipped within the last 2 years, stored for rapid retrieval |
| **Deep Archive** | Records for orders older than 2 years, stored for long-term retention with standard retrieval |
| **Legal Hold** | A directive to preserve records beyond the normal retention period due to litigation, audit, or regulatory investigation |
| **PDF/A** | An ISO-standardized archival PDF format designed for long-term preservation and readability |
| **Backup** | A secondary copy of records stored in a physically and logically separate location |

## 5. Responsibilities

| Role | Responsibility |
|------|---------------|
| **Quality Manager** | Owns this procedure. Sets retention policies. Authorizes disposition of expired records. Responds to legal hold requests. Manages access controls for the archive. |
| **QA Engineer** | Transfers completed MRBs to the archive. Maintains the Archive Register. Retrieves records upon authorized request. Performs annual archive integrity checks. |
| **IT Manager / System Administrator** | Maintains archive infrastructure (servers, backup systems, cloud storage). Ensures data integrity, redundancy, and security. Manages PDF/A migration when technology changes. |
| **Commercial Manager** | Identifies customer-specific retention requirements during contract review (PR-007). Coordinates with customer on record retrieval requests. |
| **Managing Director** | Authorizes legal hold directives. Final authority on archive policy exceptions. |

## 6. Procedure

### 6.1 Retention Periods

#### 6.1.1 Order-Specific Quality Records

| Record Type | Minimum Retention | Basis |
|-------------|-------------------|-------|
| Manufacturing Record Book (MRB/MDR) | **15 years** from shipment date, or per customer contract if longer | AS9100D, AQAP 2110, industry standard |
| Certificate of Conformance (CoC) | **15 years** from date of issue | AS9100D, AQAP 2110 |
| Material certificates (EN 10204) | **15 years** from shipment date | Industry standard, traceability requirement |
| AS9102 FAIR packages | **15 years** from shipment date | AS9100D |
| Inspection and test reports | **15 years** from shipment date | AS9100D, NORSOK |
| NDT reports | **15 years** from shipment date | ASME, EN ISO standards |
| ITP records and sign-offs | **15 years** from shipment date | NORSOK, customer contract |
| PMI reports | **15 years** from shipment date | Industry standard |
| NCR and CAPA records | **15 years** from closure date | ISO 9001, AS9100D |

#### 6.1.2 Customer-Specific Overrides

| Industry | Typical Customer Requirement | Action |
|----------|------------------------------|--------|
| **Defence/Aerospace** | Product lifetime + 5 years (often 25–30 years total) | Apply customer requirement if longer than 15-year minimum |
| **Nuclear** | Product lifetime + 10 years (40+ years possible) | Apply customer requirement |
| **Oil & Gas** | 15 years (NORSOK standard) or field design life + 5 years | Apply whichever is longer |
| **Maritime** | Class society retention requirements (typically 10–15 years) | Apply class society requirement if specified |

**Rule:** The retention period applied is ALWAYS the longest of: (a) the minimum in Section 6.1.1, (b) any customer-specific requirement from the contract, or (c) any regulatory requirement.

#### 6.1.3 QMS Records

| Record Type | Retention Period | Basis |
|-------------|-----------------|-------|
| Quality Manual (QM-001) | Current version + all previous versions: permanent | ISO 9001 |
| Procedures (PR-xxx) | Current version + 2 previous versions active; all versions archived permanently | ISO 9001 |
| Work Instructions (WI-xxx) | Current version + 1 previous version active; all versions archived 10 years | ISO 9001 |
| Internal audit reports | 10 years from audit date | ISO 9001, AS9100D |
| Management review records | 10 years from review date | ISO 9001 |
| Calibration records | Life of instrument + 5 years | ISO 9001, AS9100D |
| Training records | Duration of employment + 10 years | ISO 9001, AS9100D |
| Supplier evaluation records | Duration of supplier relationship + 5 years | ISO 9001 |
| Customer complaint records | 15 years from resolution | Product liability |

#### 6.1.4 Material Requirement Profiles

| Record Type | Retention Period | Basis |
|-------------|-----------------|-------|
| Material Requirement Profiles (PR-008) | Life of profile + 5 years after last use | Traceability to historical orders |
| Profile version history | All versions retained permanently | Audit trail |

### 6.2 Archive Structure

#### 6.2.1 Digital Archive Organization

```
ARCHIVE ROOT
│
├── ACTIVE_ARCHIVE/          (Orders shipped within last 2 years)
│   ├── [YYYY]/              (Year of shipment)
│   │   ├── AM-MRB-[YYYY]-[NNNNN]/
│   │   │   ├── MRB_Package.pdf     (Complete MRB as PDF/A)
│   │   │   ├── MRB_Package/        (Individual source files by section)
│   │   │   ├── CoC/                (Signed CoC PDF)
│   │   │   ├── Validation_Log/     (PR-010 records)
│   │   │   ├── Gate_Review/        (PR-008 records)
│   │   │   └── Metadata.json       (Order metadata, retention date, classification)
│   │   └── ...
│   └── ...
│
├── DEEP_ARCHIVE/            (Orders older than 2 years)
│   ├── [YYYY]/
│   │   ├── AM-MRB-[YYYY]-[NNNNN]/
│   │   │   └── (same structure as active)
│   │   └── ...
│   └── ...
│
├── QMS_ARCHIVE/             (Quality Management System documents)
│   ├── Manuals/
│   ├── Procedures/
│   ├── Work_Instructions/
│   ├── Audits/
│   ├── Management_Reviews/
│   └── Training/
│
├── SUPPLIER_ARCHIVE/        (Supplier-related records)
│   ├── Approved_Supplier_List/
│   ├── Supplier_Evaluations/
│   └── Material_Requirement_Profiles/
│
└── COC_REGISTER/            (Master CoC index)
    └── AM-COC-Register.xlsx  (or ERP-maintained)
```

#### 6.2.2 Archive Metadata

Every archived MRB SHALL have an associated metadata record containing:

| Field | Content |
|-------|---------|
| MRB Number | AM-MRB-[YYYY]-[NNNNN] |
| CoC Number | AM-COC-[YYYY]-[NNNNN] |
| Order Reference | PO number |
| Customer | Customer name |
| Classification | DEFENCE / OIL_GAS / MARITIME / STANDARD |
| Part Number | Part number |
| Ship Date | Date of shipment |
| Retention Period | Number of years |
| Retention Expiry | Calculated date (ship date + retention period) |
| Legal Hold | Yes/No (if Yes: hold reference) |
| Archive Location | Active/Deep + server path |
| Backup Location | Backup server/cloud path |
| File Size | Total archive size |
| Checksum | SHA-256 hash of MRB PDF/A for integrity verification |

### 6.3 Archival Process

**Step 1:** After shipment (order state = SHIPPED), the QA Engineer initiates the archival process.

**Step 2:** QA Engineer prepares the archive package:

1. Collect the final MRB PDF/A package from PR-012
2. Collect all supporting records (validation logs, gate reviews, correction requests)
3. Collect the CoC and any DoCs
4. Generate the metadata record
5. Calculate and record the SHA-256 checksum of the MRB PDF/A file

**Step 3:** QA Engineer places the archive package in the ACTIVE_ARCHIVE directory, organized by year and MRB number.

**Step 4:** QA Engineer updates the Archive Register (Form FM-013-01) with:

- MRB number, CoC number, order reference
- Customer and classification
- Retention period and expiry date
- Archive location and backup location
- Checksum

**Step 5:** QA Engineer updates the order state: SHIPPED → ARCHIVED.

**Step 6:** Automated backup system creates a secondary copy in the backup location (see Section 6.5).

### 6.4 Migration from Active to Deep Archive

Records are migrated from Active Archive to Deep Archive automatically:

- **Trigger:** 2 years after shipment date
- **Action:** Move archive package from ACTIVE_ARCHIVE/[YYYY]/ to DEEP_ARCHIVE/[YYYY]/
- **Verification:** Checksum verified before and after migration
- **Metadata:** Updated with new archive location

This migration does NOT affect the retention period. It is an operational optimization for storage management and retrieval speed.

### 6.5 Backup and Redundancy

#### 6.5.1 Backup Strategy

| Backup Type | Frequency | Location | Purpose |
|-------------|-----------|----------|---------|
| **Real-time replication** | Continuous | Secondary on-site server | Protection against primary server failure |
| **Daily incremental** | Every 24 hours | Off-site cloud storage (encrypted) | Protection against site-level disaster |
| **Weekly full backup** | Every 7 days | Off-site cloud storage (encrypted) | Full recovery point |
| **Annual archive snapshot** | Yearly | Separate cloud region + physical media (if required) | Long-term preservation insurance |

#### 6.5.2 Backup Requirements

1. All backups SHALL be encrypted at rest (AES-256 minimum)
2. All backups SHALL be encrypted in transit (TLS 1.2 minimum)
3. Backup integrity verified weekly (checksum comparison)
4. Backup restoration tested quarterly (random sample of 5 MRBs restored and verified)
5. Backup locations SHALL be in a different physical location from the primary archive
6. Cloud storage provider SHALL meet ISO 27001 or equivalent security certification
7. Cloud storage SHALL be located within the EEA (EU GDPR compliance for any personal data)

#### 6.5.3 Disaster Recovery

In the event of primary archive loss:

1. IT Manager activates disaster recovery procedure
2. Most recent verified backup is identified
3. Archive is restored from backup to replacement infrastructure
4. Checksum verification performed on all restored MRBs
5. Any gap between backup and loss is identified
6. Gap records are reconstructed from ERP and production systems where possible
7. Customers are notified if any records cannot be recovered (per Commercial Manager)

### 6.6 Access Control

#### 6.6.1 Access Levels

| Level | Who | Access |
|-------|-----|--------|
| **Full** | Quality Manager | Read, write, modify metadata, authorize disposition |
| **Standard** | QA Engineers | Read, add new archives, update metadata |
| **Read-only** | Production Manager, Commercial Manager | Read and retrieve for customer requests |
| **Restricted** | Other personnel | No access unless specifically authorized by Quality Manager |

#### 6.6.2 Access Rules

1. All archive access is logged (who, when, what record, action)
2. Bulk downloads or exports require Quality Manager approval
3. Customer requests for archived records are processed through Commercial Manager → QA Engineer
4. Third-party auditor access is granted temporarily for audit duration, then revoked
5. No archive record SHALL be modified after archival — only metadata updates are permitted
6. Deletion of archive records requires Managing Director approval (disposition process only)

### 6.7 Record Retrieval

When a record is requested (by customer, auditor, internal need):

**Step 1:** Requester submits a retrieval request specifying:
- Record type (MRB, CoC, specific document)
- Order reference (PO number, MRB number, or CoC number)
- Reason for retrieval
- Required format (electronic, physical copy)

**Step 2:** QA Engineer locates the record:
- Search by MRB number, CoC number, PO number, or customer name
- Active archive: immediate retrieval
- Deep archive: retrieval within 4 business hours

**Step 3:** QA Engineer verifies the integrity of the retrieved record:
- Checksum matches the stored checksum
- PDF/A opens correctly and all content is readable

**Step 4:** Record is provided to the requester:
- Electronic: PDF/A copy via secure method (encrypted email, customer portal)
- Physical: printed copy stamped "ARCHIVE COPY — [Date]"

**Step 5:** Retrieval is logged in the Archive Access Log (Form FM-013-02).

**Retrieval time targets:**

| Archive | Target Retrieval Time |
|---------|----------------------|
| Active archive (< 2 years old) | < 1 hour |
| Deep archive (> 2 years old) | < 4 business hours |
| Backup (disaster recovery) | < 24 hours |

### 6.8 Technology Migration

Digital archives must survive technology changes over 15–30+ year retention periods:

#### 6.8.1 Format Preservation

1. PDF/A is the primary archival format because it is ISO-standardized for long-term preservation
2. If PDF/A standard evolves (e.g., PDF/A-4), existing archives SHALL be migrated when:
   - Current format readers become unavailable
   - Quality Manager determines migration is necessary for continued readability
3. Migration process:
   - Convert to new format
   - Verify content integrity (visual comparison + checksum)
   - Retain original file alongside new format for transition period
   - Update metadata with format version

#### 6.8.2 Storage Medium Migration

1. Storage media SHALL be evaluated every 5 years for continued viability
2. If media technology becomes obsolete (e.g., specific server hardware, tape format):
   - Migrate to current technology
   - Verify all records accessible after migration
   - Document migration in the Archive Register

#### 6.8.3 ERP System Migration

When ERP modules are upgraded or replaced:

1. All quality records linked to the ERP SHALL be exported before decommission
2. Records verified in the new system or standalone archive
3. ERP metadata (order links, material links) preserved or mapped to new system

### 6.9 Disposition of Expired Records

When a record's retention period expires:

**Step 1:** QA Engineer identifies records eligible for disposition (retention expiry date reached).

**Step 2:** QA Engineer verifies:
- No legal hold in effect
- No pending customer claim or warranty issue
- No ongoing audit or investigation
- Customer contract does not require extended retention

**Step 3:** QA Engineer prepares a Disposition Request (Form FM-013-03) listing:
- Record identifiers (MRB numbers, CoC numbers)
- Original retention period and expiry date
- Confirmation that no holds or extensions apply

**Step 4:** Quality Manager reviews and approves the Disposition Request.

**Step 5:** If approved:
- Electronic records: secure deletion (overwrite, not just delete)
- Physical records: shredding or secure destruction
- Backups: deletion from all backup locations
- Archive Register updated: status changed to DISPOSED with date and authorization reference

**Step 6:** Disposition is documented on Form FM-013-04 (Disposition Record).

**Important:** Records SHALL NOT be disposed of automatically. Disposition always requires human review and Quality Manager approval.

### 6.10 Legal Hold

When a legal hold is issued (litigation, regulatory investigation, customer claim):

1. Managing Director or Quality Manager issues a Legal Hold Directive specifying:
   - Scope (which orders, customers, time periods, record types)
   - Reason for hold
   - Duration (until further notice, or specific date)
2. QA Engineer identifies all records within scope
3. Records are flagged in the Archive Register with LEGAL_HOLD status
4. Retention period is suspended — records SHALL NOT be disposed of regardless of expiry date
5. When the legal hold is lifted:
   - Managing Director or Quality Manager issues a Hold Release
   - Records return to normal retention schedule
   - If retention period has expired during hold: disposition review per Section 6.9

### 6.11 Annual Archive Integrity Check

Once per year, the QA Engineer performs an integrity check on the archive:

1. **Sample selection:** Random sample of 10% of archived MRBs (minimum 5, maximum 50)
2. **Checksum verification:** SHA-256 checksum of each sampled MRB PDF/A compared to stored checksum
3. **Readability check:** Open each sampled MRB and verify content is readable and complete
4. **Backup verification:** Verify that backup copies exist and checksums match
5. **Metadata accuracy:** Verify that Archive Register entries match actual archive contents
6. **Results:** Recorded on Form FM-013-05 (Annual Archive Integrity Report)
7. **Failures:** Any integrity failure triggers immediate investigation and restoration from backup

## 7. Records

| Form | Title | Retention |
|------|-------|-----------|
| FM-013-01 | Archive Register | Permanent (lifetime of company) |
| FM-013-02 | Archive Access Log | 10 years |
| FM-013-03 | Disposition Request | 10 years after disposition |
| FM-013-04 | Disposition Record | 10 years after disposition |
| FM-013-05 | Annual Archive Integrity Report | 10 years |

## 8. Key Performance Indicators

| KPI | Target | Measured |
|-----|--------|----------|
| Archive completeness | 100% of shipped orders archived within 5 business days of shipment | Monthly |
| Active archive retrieval time | < 1 hour | Per request |
| Deep archive retrieval time | < 4 business hours | Per request |
| Annual integrity check pass rate | 100% of sampled records pass checksum and readability verification | Annually |
| Backup restoration success rate | 100% of quarterly test restorations successful | Quarterly |
| Disposition compliance | 0 records disposed of without Quality Manager approval | Per incident |

## 9. Flowchart

```
Order state = SHIPPED
            │
            ▼
┌─────────────────────────┐
│ Prepare archive package  │
│ - MRB PDF/A              │
│ - Supporting records     │
│ - Generate metadata      │
│ - Calculate checksum     │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Store in ACTIVE_ARCHIVE  │
│ Update Archive Register  │
└───────────┬─────────────┘
            │
            ▼
   Automated backup
   (real-time + daily + weekly)
            │
            ▼
   Order state → ARCHIVED
            │
            ▼
   ┌────────────────────────────────────┐
   │         ONGOING LIFECYCLE          │
   ├────────────────────────────────────┤
   │                                    │
   │  After 2 years:                    │
   │  → Migrate to DEEP_ARCHIVE        │
   │  → Verify checksum                 │
   │                                    │
   │  Annually:                         │
   │  → Integrity check (10% sample)   │
   │  → Backup verification             │
   │                                    │
   │  When technology changes:          │
   │  → Format migration                │
   │  → Storage medium migration        │
   │                                    │
   │  When retention expires:           │
   │  → Disposition review              │
   │  → QM approval required            │
   │  → Secure destruction              │
   │                                    │
   │  If legal hold issued:             │
   │  → Freeze disposition              │
   │  → Preserve until hold released    │
   │                                    │
   └────────────────────────────────────┘
```

## 10. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Prepared By | Quality Manager | _______ | _______ |
| Reviewed By | Production Manager | _______ | _______ |
| Approved By | Managing Director | _______ | _______ |

This document is controlled. Printed copies are uncontrolled unless stamped "CONTROLLED COPY" in red.
