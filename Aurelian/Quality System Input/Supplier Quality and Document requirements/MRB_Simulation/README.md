# MRB-Simulation

> **This repository is REFERENCE DATA for the Aurelian Manufacturing pilot application.**
> All content herein shall be treated as the authoritative source for MRB structure, document types, SDRL categories, SDL formatting, and PO-driven documentation workflows — applicable across **both Customer View and Aurelian (Supplier) View** wherever technical documentation is displayed, generated, validated, or managed.

---

## What Is This Repository?

A complete, simulated Manufacturing Record Book (MRB) package for a realistic subsea manufacturing order. It contains all the documents a CNC machining workshop (Aurelian Manufacturing) would produce for a customer (Nordic Subsea Solutions) under a single Purchase Order.

**Every file is a working HTML document** rendered in A4 format with correct branding, and every HTML file has a corresponding `.md` file containing structured metadata.

---

## Order Context (Simulation)

| Field | Value |
|-------|-------|
| **Customer** | Nordic Subsea Solutions AS (NSS) |
| **Supplier** | Aurelian Manufacturing AS |
| **PO Number** | NSS-PO-2026-0042 |
| **Product** | Subsea Connector Assembly SCA-300 |
| **Tag Number** | NSS-BSP2-SCA-001 |
| **Material** | Super Duplex UNS S32750 (SAF 2507) |
| **PO Date** | 04 March 2026 |
| **Delivery** | 19 August 2026 |
| **Scope** | CNC machining, NDE, surface treatment (no welding) |

---

## Repository Structure

```
MRB-Simulation/
│
├── README.md                              ← This file
│
├── PO/
│   ├── NSS-PO-2026-0042.html             ← Purchase Order (5-page, NSS branding)
│   └── NSS-PO-2026-0042.md               ← Metadata
│
├── SDRL/
│   ├── NSS-SDRL-2026-0042.html           ← Supplier Document Requirements List (NSS branding)
│   └── NSS-SDRL-2026-0042.md             ← Metadata + category definitions
│
├── SDL/
│   ├── AM-SDL-2026-0042-001.html         ← Supplier Document List (Aurelian branding)
│   └── AM-SDL-2026-0042-001.md           ← Metadata
│
├── MRB/
│   ├── 01_Inspection_Test_Plan.html       ← ITP (Sec 1)
│   ├── 01_Inspection_Test_Plan.md
│   ├── 02_QMS_Certificates.html           ← QMS Certs (Sec 2)
│   ├── 02_QMS_Certificates.md
│   ├── 04_Material_Traceability.html      ← Material Traceability (Sec 4)
│   ├── 04_Material_Traceability.md
│   ├── 05_Material_Certificates.html      ← Material Certs EN 10204 3.2 (Sec 5)
│   ├── 05_Material_Certificates.md
│   ├── 06_Weld_NDT_Log.html              ← NDT Log (Sec 6)
│   ├── 06_Weld_NDT_Log.md
│   ├── 09_Visual_Inspection.html          ← Visual Inspection (Sec 9)
│   ├── 09_Visual_Inspection.md
│   ├── 10_NDE_Reports.html               ← NDE Reports RT+PT (Sec 10)
│   ├── 10_NDE_Reports.md
│   ├── 11_NDE_Operator_Certificates.html  ← NDE Operator Certs (Sec 11)
│   ├── 11_NDE_Operator_Certificates.md
│   ├── 12_Surface_Treatment.html          ← Surface Treatment (Sec 12)
│   ├── 12_Surface_Treatment.md
│   ├── 13_Dimensional_Inspection.html     ← Dimensional Inspection (Sec 13)
│   ├── 13_Dimensional_Inspection.md
│   ├── 14_Weight_Certificate.html         ← Weight Certificate (Sec 14)
│   ├── 14_Weight_Certificate.md
│   ├── 20_Non_Conformance_Records.html    ← NCR Records (Sec 20)
│   ├── 20_Non_Conformance_Records.md
│   ├── 21_Certificate_of_Conformance.html ← CoC (Sec 21)
│   ├── 21_Certificate_of_Conformance.md
│   ├── 22_As_Built_Drawings.html          ← As-Built Drawings (Sec 22)
│   ├── 22_As_Built_Drawings.md
│   ├── 24_Mechanical_Completion_Dossier.html ← MCD (Sec 24)
│   └── 24_Mechanical_Completion_Dossier.md
│
├── MRB_Simulation_Changelog.html          ← Endringsrapport (Norwegian)
├── MRB_Simulation_Changelog.md
├── UML_ERP_MRB_Sequence_Diagrams.html     ← ERP-MRB interface diagrams
└── UML_ERP_MRB_Sequence_Diagrams.md
```

---

## SDRL Document Type Categories

The SDRL defines **8 standard categories** for classifying all technical documentation. These categories are the **authoritative classification** that must be used throughout the pilot application — in database enums, API responses, UI groupings, filters, and validation logic.

| # | Key | Display Name | Description |
|---|-----|-------------|-------------|
| 1 | `GENERAL` | General | Administrative & project management (SDL, progress reports) |
| 2 | `TECHNICAL` | Technical | Bid documentation & technical submittals (ITP, quality plan) |
| 3 | `ENGINEERING` | Engineering | Design & engineering outputs (drawings, data sheets, BOM) |
| 4 | `DISPATCH` | Dispatch, Receipt, Storage & Installation | Logistics, packing, preservation, delivery schedules |
| 5 | `USER_MANUAL` | User Manual | Operation & maintenance documentation |
| 6 | `CERTIFICATES` | Certificates | Manufacturing & verification certificates (material, weight, NDE operator) |
| 7 | `PROCEDURES` | Procedures | Manufacturing & verification procedures (fabrication, NDE, coating) |
| 8 | `REPORTS` | Reports | Manufacturing & verification reports (CoC, NCR, inspection, NDE, MCD) |

### Category-to-MRB Mapping

| MRB Sec | Document | SDRL No. | Category |
|---------|----------|----------|----------|
| 1 | Inspection & Test Plan (ITP) | 2.2 | TECHNICAL |
| 2 | QMS Certificates | 8.10 | REPORTS |
| 4 | Material Traceability List | 8.2 | REPORTS |
| 5 | Material Certificates (EN 10204 3.2) | 6.1 | CERTIFICATES |
| 6 | NDT Log | 8.6 | REPORTS |
| 9 | Visual Inspection Reports | 8.4 | REPORTS |
| 10 | NDE Reports (RT + PT) | 8.5 | REPORTS |
| 11 | NDE Operator Certificates | 6.6 | CERTIFICATES |
| 12 | Surface Treatment Inspection Report | 8.7 | REPORTS |
| 13 | Dimensional Inspection Record | 8.4 | REPORTS |
| 14 | Weight Certificate | 6.3 | CERTIFICATES |
| 20 | Non-Conformance / Concession Records | 8.3 | REPORTS |
| 21 | Certificate of Conformance | 8.1 | REPORTS |
| 22 | As-Built Drawings / Mark-Ups | 3.6 | ENGINEERING |
| 24 | Mechanical Completion Dossier (MCD) | 8.11 | REPORTS |

### N/A Sections (not applicable for CNC machining scope)

| MRB Sec | Document | Reason |
|---------|----------|--------|
| 3 | Quality Plan | Covered by ITP |
| 7 | WPS / WPQR / PWHT | No welding — machining only |
| 8 | Welder Certificates | No welding — machining only |
| 15 | Lifting Certificate | No certified lifts required |
| 16 | Pressure Test Traceability | Not applicable |
| 17 | Pressure Test Procedure | Not applicable |
| 18 | Pressure Test Certificate | Not applicable |
| 19 | Sub-Supplier Documentation | No sub-suppliers on scope |

---

## MRB Standard Index (24 Sections)

The full MRB index as defined in the SDRL. The **In Use** column shows which sections are active for this order:

| Sec | Document Type | Status |
|-----|--------------|--------|
| 1 | Inspection & Test Plan (ITP) | In Use |
| 2 | QMS Certificates | In Use |
| 3 | Quality Plan | N/A |
| 4 | Material Traceability List / Record | In Use |
| 5 | Material Certificates / PMI Reports | In Use |
| 6 | NDT Log | In Use |
| 7 | WPS / WPQR / PWHT | N/A |
| 8 | Welder Certificates | N/A |
| 9 | Visual Inspection Reports | In Use |
| 10 | NDE Reports | In Use |
| 11 | NDE Operator Certificates | In Use |
| 12 | Surface Treatment Inspection Reports | In Use |
| 13 | Dimensional Inspection Record | In Use |
| 14 | Weighing Certificate | In Use |
| 15 | Lifting Certificate | N/A |
| 16 | Pressure Test Traceability Certificate | N/A |
| 17 | Pressure Test Procedure / FAT Procedure | N/A |
| 18 | Pressure Test Certificate / FAT Report | N/A |
| 19 | Documentation from Sub-Suppliers | N/A |
| 20 | Non-Conformance / Concession Records | In Use |
| 21 | Certificate of Conformance | In Use |
| 22 | As-Built Drawings / Mark-Ups | In Use |
| 23 | Photos of Equipment / Testing / Marking | In Use |
| 24 | Mechanical Completion Dossier (MCD) | In Use |

---

## Document Relationships

```
PO (NSS-PO-2026-0042)
 │
 ├── defines scope, requirements, timeline
 │
 ├── SDRL (NSS-SDRL-2026-0042)          ← Customer specifies required documents
 │    └── 8 categories, ~46 document types
 │         └── MRB Standard Index (24 sections, In Use / N/A per order)
 │
 ├── SDL (AM-SDL-2026-0042-001)          ← Supplier tracks submitted documents
 │    └── mirrors SDRL categories
 │    └── tracks revision, date, status, transmittal, MRB inclusion
 │
 └── MRB                                 ← The deliverable documentation package
      └── 15 active sections for this order
      └── each section = one or more documents from the SDL
```

---

## Key Standards Referenced

| Standard | Description |
|----------|-------------|
| ISO 9001:2015 | Quality Management System |
| NORSOK M-001 | Materials selection |
| NORSOK M-630 | Material data sheets for piping |
| NORSOK M-650 | Qualification of manufacturers of special materials |
| NORSOK M-501 | Surface preparation and protective coating |
| EN 10204 Type 3.2 | Metallic products — inspection documents |
| ISO 2768-mK | General tolerances (medium/coarse) |
| ISO 17636 | Non-destructive testing — radiographic testing |
| ISO 3452 | Non-destructive testing — penetrant testing |
| ISO 17637 | Non-destructive testing — visual testing |
| ISO 9712 | Qualification and certification of NDT personnel |

---

## Branding in Documents

| Document Owner | Branding | Primary Color |
|---------------|----------|---------------|
| Nordic Subsea Solutions (customer) | NSS blue | `#0057A0` |
| Aurelian Manufacturing (supplier) | Aurelian red | `#F50537` |

- **PO and SDRL** use NSS branding (customer-issued documents)
- **SDL and all MRB documents** use Aurelian branding (supplier-issued documents)

---

## For Developers

> **This repo is reference data — not application code.**
>
> When building any part of the pilot that handles technical documentation, MRB packages, document types, SDRL parsing, SDL generation, or document validation:
>
> 1. **Use the 8 SDRL categories** (General, Technical, Engineering, Dispatch, User Manual, Certificates, Procedures, Reports) as the primary document classification — in database enums, API schemas, and UI groupings.
>
> 2. **Use the MRB Standard Index** (24 sections) as the structural template for MRB assembly, completeness validation, and section-level tracking.
>
> 3. **Use the HTML files** as visual reference for how each document type should look when rendered (layout, content structure, data fields, branding).
>
> 4. **Use the .md files** as machine-readable metadata (document number, SDRL reference, category, MRB section, applicable standards).
>
> 5. **Both Customer View and Aurelian View** must reflect this structure. The SDRL is the customer's specification; the SDL and MRB are the supplier's response. The pilot must support both perspectives on the same underlying data.
>
> 6. **N/A sections are order-specific**, not global. The MRB Standard Index has 24 sections — which ones are "In Use" vs "N/A" depends on the order scope (this simulation: CNC machining, no welding/pressure testing).

---

## Changelog

| Date | Change |
|------|--------|
| 03 Mar 2026 | Initial simulation created — welding/pressure test content removed, dates aligned to PO 04 Mar 2026, MD files added for all documents |

See `MRB_Simulation_Changelog.html` for detailed modification log.

---

*Aurelian Manufacturing AS — Production as a Service*
