---
name: aurelian-vdr-index
description: Virtual Data Room index for Aurelian Manufacturing tracking all documents across 9 categories with availability status. Use this skill when someone asks about document status, VDR setup, what documents exist, what's missing, data room organization, or when preparing to share documents with investors. Triggers on "data room", "VDR", "which documents", "do we have", "document status", "what's in the data room", "share with investor", "upload documents", or any question about document availability and organization for investor DD.
---

# Aurelian Manufacturing — Virtual Data Room Index

Complete document inventory with availability status. Aligned with master document numbers and actual VDR folder structure.

**All financial numbers from *02 Economic Tables & Projections* (VDR 02.04) — ABSOLUTE master.**

### REFERENCE FORMAT FOR GENERATED DOCUMENTS (COPY — DO NOT RECONSTRUCT)

> **Rule: Never hardcode a revision number in generated documents (Word, PPT, PDF).** The master document is always the current revision. When a new revision is issued, all documents remain correct without needing updates. File paths retain the revision in the filename because that is the actual file on disk.

**Full reference:** `*02 Economic Tables & Projections* (VDR 02.04)`
**Inline with section:** `Ref: 02 Economic Tables & Projections, §[number] (VDR 02.04)`

❌ Never in generated docs: any revision number (e.g. "REV6", "REV7"), or "VDR 02.04" alone without document name
✅ In generated docs: "*02 Economic Tables & Projections* (VDR 02.04)" — NO revision number

**Examples with current values:**
- Revenue 20 CNC @ 60% = ~315 MNOK → `Ref: 02 Economic Tables & Projections, §5.1 (VDR 02.04)`
- Seed: 51.3 MNOK equity + 29.3 MNOK debt = 80.6 MNOK total → `Ref: 02 Economic Tables & Projections, §4.1 (VDR 02.04)`
- Staffing 20 CNC: 16 ops + 4 admin = 20 total → `Ref: 02 Economic Tables & Projections, §1.3b (VDR 02.04)`
- EBIT 20 CNC @ 60% = ~222.3 MNOK → `Ref: 02 Economic Tables & Projections, §3.6 (VDR 02.04)`

### MANDATORY: Pre-Work Check (applies to EACH document request)

Before creating or revising ANY document in this skill's scope:
1. **READ** the master document: `Aurelian_VDR/02_Financial/2.4_Economic_Tables_Projections/02_Economic_Tables_Projections_REV6.pdf`
2. **READ** the design manual: `Design MAnual/aurelian-design-manual.md`
3. **CONFIRM** the 17 checkpoint values from the master document
4. **This check applies for EACH document request within a conversation — not just the first one**

## VDR Structure Overview

The VDR is organized into 9 top-level sections (00-08) plus a supplementary section (09):

| Section | Name | Purpose |
|---------|------|---------|
| 00 | Executive Summary | Investor-facing overview materials |
| 01 | Corporate Governance | Legal entity, shareholder agreements, cap table |
| 02 | Financial | Master document, projections, models, sensitivity |
| 03 | Commercial | Market research, pipeline, GTM, pricing |
| 04 | Technical | CNC specs, facility, quality, risk |
| 05 | Legal | Contracts, IP, compliance, insurance |
| 06 | Team | CVs, board, hiring plan |
| 07 | Presentations | Pitch deck, one-pagers |
| 08 | DD Checklists | Due diligence preparation |
| 09 | Supplementary | Supporting analyses, appendices |

---

## 00-EXECUTIVE SUMMARY/

| Document | Status | Priority | Notes |
|----------|--------|----------|-------|
| Executive Summary (2-page) | DRAFT | CRITICAL | Needs master document update (Seed 47>51.3, CNC 8>5, cap table) |
| Investment Teaser (1-page) | DRAFT | CRITICAL | Needs master document update |

---

## 01-CORPORATE GOVERNANCE/

| Document | Status | Notes |
|----------|--------|-------|
| Stiftelsesdokument (foundation) | Exists | In VDR |
| Firmaattest (company extract) | Exists | In VDR |
| Aksjonaeavtale (shareholder agreement) | Exists (signed) | Bilingual, interim agreement |
| Vesting Schedule (4yr cliff) | Exists | In VDR |
| Acceleration Terms (double-trigger) | Exists | In VDR |
| Cap Table Pro Forma (all rounds) | Exists | **Needs master document update** |
| Organization chart | Missing | MEDIUM priority |
| Board minutes | Missing | LOW — Serie A priority |
| Board rules of procedure | Missing | MEDIUM priority |

**Cap table (master document values — use these):**

| Shareholder | Current | Post PreSeed | Post Seed | Post Serie A |
|-------------|---------|-------------|-----------|-------------|
| Eier A (Holen Industrier AS) | 53.125% | 44.27% | 31.74% | 26.90% |
| Eier B (Quality Group Invest AS) | 31.875% | 26.56% | 19.05% | 16.14% |
| Eier C (STAH Invest AS) | 10.00% | 8.33% | 5.97% | 5.06% |
| Eier D (Roadcode AS) | 5.00% | 4.17% | 2.99% | 2.53% |
| PreSeed investors | — | 16.67% | 11.95% | 10.12% |
| Seed investors | — | — | 28.30% | 23.98% |
| Serie A investors | — | — | — | 15.25% |
| **Founders total** | **100%** | **83.33%** | **59.74%** | **50.60%** |

---

## 02-FINANCIAL/

| Document | Status | Notes |
|----------|--------|-------|
| *02 Economic Tables & Projections* (VDR 02.04) | Exists | **MASTER SOURCE** for all numbers |
| Valuation Methodology | Exists | Needs master document alignment check |
| Model Assumptions & Valuation | Exists | Needs master document alignment check |
| Founder Contribution PreSeed Valuation | Exists | Probably OK |
| VC-Praksis Analyse | Exists | European benchmarks |
| Comparable Investment Cases (Hadrian) | Exists | Still valid |
| CNC Resale Value Analysis | Exists | Still valid |
| Detailed Financial Model (Excel) | Missing | CRITICAL — generate from master document |
| Monthly Cash Flow 2027-28 | Missing | MEDIUM |
| Sensitivity Analysis (Excel) | Missing | Generate from master document Section 5 |
| Financing Plan | Missing in folder | Generate from master document Section 4 |
| Use of Funds | Missing in folder | Generate from master document Section 7 |

**Revenue projections ( MASTER numbers):**

| Year | CNC | Utilization | Revenue MNOK | Cost MNOK | Aurelian Profit MNOK |
|------|-----|-------------|-------------|-----------|---------------------|
| 2027 H2 | 5 | 20% | 10.9 | 13.4 | -2.5 |
| 2028 | 5 | 37.5% | 49.3 | 34.1 | 15.2 |
| 2029 | 12 | 42.5% | 134 | 61.1 | 72.9 |
| 2030 | 17 | 47.5% | 212 | 80.2 | 131.8 |
| 2031 | 20 | 52.5% | 276 | 92.8 | 166.8 |
| 2032 | 20 | 57.5% | 302 | 92.4 | 182.3 |
| 2033 | 22 | 60% | 347 | 98.0 | 207.0 |
| 2034 | 24 | 62.5% | 394 | 103.8 | 232.6 |
| 2035 | 25 | 65% | 427 | 107.2 | 247.8 |

Revenue formula: CNC x 8,760 hours x Utilization% x 3,000 NOK/hr.

---

## 03-COMMERCIAL/

| Document | Status | Notes |
|----------|--------|-------|
| Markedsanalyse Master V3 | Exists | Comprehensive |
| Defence Market Research | Exists | NATO, Kongsberg |
| Energy Market Research | Exists | Equinor, transition |
| Critical Markets Research | Exists | Cross-sector |
| Market Trends & Projections | Exists | Forward-looking |
| Physical Robotics LOI | Exists | In VDR |
| Competitive Landscape doc | Missing in folder | Generate from market-dd + investor skills |
| Customer Pipeline tracker | Missing | Needs real customer data |
| Go-to-Market plan | Missing in folder | Generate from gtm skill |
| Pricing & Revenue Model doc | Missing in folder | Generate from master document Section 1 |

---

## 04-TECHNICAL/

| Document | Status | Notes |
|----------|--------|-------|
| Autonomous CNC Validation | Exists | Core technical proof |
| Concept Note (facility) | Exists | High-level facility plan |
| Real Estate Strategy (Norbygg) | Exists | Partnership strategy |
| CNC Equipment Specifications (Mazak) | Exists | Machine specs doc |
| Mazak LOI / purchase agreement | Missing | HIGH — need actual agreement |
| Norbygg lease / term sheet | Missing | HIGH — need actual agreement |
| ISO Certification Roadmap | Missing | Generate from technical-dd skill |
| Production Timeline / Gantt | Missing | Generate from master document Section 2 |
| Risk Register | Missing | Generate from master document Section 5.5 |
| Facility architectural plans | Missing | MEDIUM |

---

## 05-LEGAL/

| Document | Status | Notes |
|----------|--------|-------|
| IP Assignment Agreement | DRAFT (unsigned) | In VDR — needs execution |
| Founder Employment Agreements | Missing | HIGH priority |
| Advisory Agreements | Missing | MEDIUM priority |
| ESOP / Option Plan | Missing | Master doc: 10% per daughter company (site-level) |
| Export Control Assessment | Missing | MEDIUM |
| Insurance Overview | Missing | LOW — Serie A priority |

---

## 06-TEAM/

| Document | Status | Notes |
|----------|--------|-------|
| Tore Ausland CV | Exists | In VDR |
| Andre Tandberg CV | Missing in VDR | Data available in team-profile skill |
| Henrik Strom CV | Exists | In VDR |
| Fredrik Vangsal CV | Exists | In VDR |
| Advisory Board profiles | Missing | MEDIUM |
| Recruitment Plan | Missing | MEDIUM |
| CTO / Technical Lead Plan | Missing | HIGH |

---

## 07-PRESENTATIONS/

| Document | Status | Notes |
|----------|--------|-------|
| Investor Pitch Deck V3 | Exists | **Needs master document update** |
| Q&A Database | In skills | Can generate document |

---

## 08-DD CHECKLISTS/

| Document | Status | Notes |
|----------|--------|-------|
| DD Checklist PreSeed Round | Exists | In VDR |
| Seed DD Checklist | Missing | Generate when ready |

---

## Document Access Rules

**For ALL investors (immediately after NDA):**
- 00 Executive Summary
- 07 Presentations (pitch deck)
- 03 Commercial: Market research (Markedsanalyse, Defence, Energy, Critical, Trends)
- 02 Financial: master document summary, VC-Praksis, Comparable Cases

**After initial interest confirmed:**
- 02 Financial: Full folder
- 04 Technical: CNC Validation doc, Concept Note, Real Estate Strategy
- 06 Team: CVs

**During formal DD only:**
- 01 Corporate: Cap table details, shareholder agreement
- 05 Legal: All legal documents
- 03 Commercial: Customer LOIs, pipeline data

**Never share without specific request:**
- Board minutes
- Individual employment terms
- Detailed advisory compensation

---

## Pre-Seed Package (Priority Documents)

For closing the Pre-Seed round, investors need at minimum:

| Priority | Document | Status |
|----------|----------|--------|
| MUST | Executive Summary (master document aligned) | DRAFT — needs update |
| MUST | Pitch Deck (master document aligned) | Exists — needs update |
| MUST | master document or financial summary | Exists |
| MUST | Cap Table Pro Forma | Exists — needs master document update |
| MUST | Aksjonaeavtale | Exists (signed) |
| SHOULD | Market Research (any 2-3 docs) | Exists |
| SHOULD | Autonomous CNC Validation | Exists |
| SHOULD | Real Estate Strategy (Norbygg) | Exists |
| SHOULD | Team CVs (at least founders) | Partial (Tore only in VDR) |

---

## Updating This Index

When a new document is added:
1. Update status in the relevant table above
2. Add the actual filename
3. Upload to the corresponding VDR folder
4. Verify all financial numbers against master document before uploading
5. Apply Aurelian design profile (#F50537, Calibri, proper formatting)
