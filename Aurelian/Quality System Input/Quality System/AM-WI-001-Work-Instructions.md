# WORK INSTRUCTIONS — DIGITAL MRB BUILDER

| Field | Value |
|-------|-------|
| **Document No.** | AM-WI-001 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-21 |
| **Approved By** | Quality Manager / Technical Lead |
| **Classification** | Internal — Controlled |
| **Status** | Draft — Founding Team Review |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| **1.0** | **2026-02-21** | **Quality Manager** | **Initial release. 13 work instructions covering Phase 0 (Q2–Q4 2026). Covers order setup, SDRL processing, material gate review, document collection, validation, and correction request workflows.** |

---

## 1. Purpose

This document provides step-by-step operator instructions for performing tasks in the Digital MRB Builder system. Each Work Instruction (WI) translates a procedure requirement (PR-xxx) into a specific sequence of actions: what screen to open, what fields to fill, what buttons to click, and what to expect from the system.

**This document answers:** "I need to do [task] — what exactly do I click?"

Work Instructions are Level 3 documents in the Aurelian Manufacturing quality hierarchy, bridging the gap between:

- **Procedures (PR-xxx, Level 2)** — define WHAT to do and WHY
- **Form Templates (FM-xxx, Level 4)** — define WHAT data to capture
- **Work Instructions (WI-xxx, Level 3)** — define HOW to do it, step by step

---

## 2. Scope

### 2.1 Phase 0 Coverage

This document covers **Phase 0 (Simulation & Build, Q2–Q4 2026)** workflows only. Phase 0 processes orders from state **NEW** through **VALIDATING**. Work instructions for later pipeline stages (CoC generation, MRB assembly, archival) will be added when those features are built.

### 2.2 Work Instruction Index

| WI# | Title | Role | Procedure | Section |
|-----|-------|------|-----------|---------|
| WI-001 | Registering a New Purchase Order | Admin | PR-009 §6.1 | §6.1 |
| WI-002 | Creating a Customer Record | Admin | PR-009 §6.1 | §6.2 |
| WI-003 | Setting Up a Material Requirement Profile | Admin / QM | PR-008 §6.4 | §6.3 |
| WI-004 | Processing an SDRL — Upload Method | QA Engineer | PR-009 §6.2 | §7.1 |
| WI-005 | Processing an SDRL — Manual Entry Method | QA Engineer | PR-009 §6.2 | §7.2 |
| WI-006 | Reviewing and Confirming SDRL Parse Results | QA Engineer | PR-009 §6.3 | §7.3 |
| WI-007 | Performing a Material Gate Review | QA Engineer | PR-008 §6.1–6.3 | §8.1 |
| WI-008 | Handling a QM Override (Escalated Gate) | Quality Manager | PR-008 §6.5 | §8.2 |
| WI-009 | Uploading Documents to MRB Slots | QA Engineer | PR-009 §6.5 | §9.1 |
| WI-010 | Reviewing Validation Results (L1–L3) | QA Engineer | PR-010 §6.2–6.4 | §9.2 |
| WI-011 | Managing Correction Requests | QA Engineer | PR-010 §6.12 | §10.1 |
| WI-012 | Viewing Order Status (Customer Portal) | Customer | AM-TS-001 §13 | §11.1 |
| WI-013 | Using the Seed Data Tool | Developer / QA | AM-TS-001 §10.4 | §12.1 |

### 2.3 Phase 0 Critical Work Instructions

The following seven WIs (marked ★) cover the core MRB pipeline and are the most frequently used during Phase 0 operations. Quick Reference Cards for these WIs are provided in §13.

★ WI-004, WI-005, WI-006, WI-007, WI-009, WI-010, WI-011

### 2.4 Workflow Chain

For a typical Oil & Gas order, work instructions are executed in this sequence:

```
WI-002 (Create Customer)        — one-time setup per customer
    ↓
WI-003 (Material Req Profile)   — one-time per customer + material grade
    ↓
WI-001 (Register PO)            — per order
    ↓
WI-004 or WI-005 (SDRL)         — per order (upload or manual entry)
    ↓
WI-006 (SDRL Review & Confirm)  — per order
    ↓                               Order state: NEW → SDRL_PARSED → MRB_INITIALIZED
WI-007 (Material Gate)           — per material receipt (1–N per order)
    ↓
WI-008 (QM Override)             — conditional: only if gate decision = REVIEW
    ↓
WI-009 (Upload Documents)       — per MRB document slot (~30 per O&G order)
    ↓
WI-010 (Review Validation)      — per uploaded document (automatic L1–L3)
    ↓
WI-011 (Correction Requests)    — conditional: only if validation fails
```

---

## 3. References

| Document | Title | Relevance |
|----------|-------|-----------|
| AM-MVP-001 | MVP Scope Definition | Screen descriptions, user stories, acceptance criteria |
| AM-FM-001 | Form Template Specifications | Field definitions, validation rules, auto-population specs |
| AM-TS-001 | IT/System Technical Specification | Architecture, data model, security, customer portal |
| AM-CT-001 | Customer-Facing Templates | SDRL templates, MRB section structures |
| AM-IF-001 | ERP ↔ MRB Builder Interface Specification | Module boundary interfaces |
| PR-008 | Incoming Material Review and Release | Material Gate procedure |
| PR-009 | SDRL Processing and MRB Management | SDRL parsing, MRB lifecycle |
| PR-010 | Document Validation and Verification | 5-layer validation, correction requests |
| QM-001 | Quality Manual — Rev 2 Addendum | QMS framework, roles |

---

## 4. Definitions

| Term | Definition |
|------|-----------|
| **Work Instruction (WI)** | A step-by-step guide for performing a specific task in the MRB Builder system. |
| **Screen** | A distinct page or view in the MRB Builder application. |
| **Form** | A data entry interface corresponding to a form template (FM-xxx). |
| **Auto-populated** | A field value that the system fills automatically from linked data — the user does not enter it. |
| **State transition** | A change in the order lifecycle state (e.g., NEW → SDRL_RECEIVED). Triggered by specific actions. |
| **Gate decision** | The outcome of a Material Gate review: RELEASED, REJECTED, or REVIEW (escalated). |
| **Validation layer** | One of 5 levels of document validation (L1–L5). Phase 0 implements L1–L3 only. |
| **Correction Request (CR)** | A formal record of a document validation failure, tracking the failure from detection through resolution. |
| **MRB Index** | The master tracking document for each order, listing every required document and its status. |
| **SDRL** | Supplier Document Requirement List — customer's specification of required MRB contents. |
| **Borderline flag** | An automatic alert when a measured value falls within 5% of a specification limit. |

---

## 5. General Conventions

### 5.1 Instruction Format

Each work instruction follows a consistent structure:

| Section | Purpose |
|---------|---------|
| **Header table** | WI number, role, procedure reference, forms, state transitions, estimated time |
| **Purpose** | One sentence explaining why this task is performed |
| **Prerequisites** | Numbered conditions that must be true before starting |
| **Steps** | Numbered actions in execution order |
| **Expected Result** | What the system state looks like when the task is complete |
| **Common Errors** | Known error conditions with causes and resolutions |
| **Related WIs** | Links to work instructions that precede or follow this one |

### 5.2 Step Format

Each step in a work instruction uses this pattern:

> **Step N:** [Action — what to click, enter, or select]
>
> *System response:* [What the screen shows after the action]
>
> *If error:* [What to do when something goes wrong] *(only included when relevant)*

### 5.3 Role Indicators

| Badge | Role | Description |
|-------|------|-------------|
| **[ADMIN]** | Administrator | System configuration, master data management |
| **[QA]** | QA Engineer | Primary system user — SDRL processing, material gate, validation |
| **[QM]** | Quality Manager | Oversight — escalated decisions, waivers, approvals |
| **[CUSTOMER]** | Customer Portal User | Read-only external access |
| **[DEV]** | Developer / QA | CLI tools, testing, seed data |

### 5.4 Screen Reference Convention

Screen names in this document match the screen descriptions in AM-MVP-001. Format: **Screen Name** (EPIC-xx reference).

Example: "Navigate to **Material Gate Form** (EPIC-06, FM-008-01)."

### 5.5 Field Reference Convention

Field references use the form template field numbers from AM-FM-001. Format: *Field Name* (FM-xxx-xx, field #N).

Example: "Enter *Chemical Analysis Results* (FM-008-01, field #17)."

### 5.6 State Transition Notation

State transitions are shown as: `CURRENT_STATE` → `NEW_STATE`

Example: `NEW` → `SDRL_RECEIVED`

### 5.7 Requirement Level Indicators

| Indicator | Meaning |
|-----------|---------|
| **(R)** | Required — field must have a value before the form can be submitted |
| **(O)** | Optional — field may be left blank |
| **(A)** | Auto-populated — system fills this value; user does not enter it |
| **(C)** | Conditional — required only when a specific condition is met |

---

## 6. System Administration Work Instructions

---

### 6.1 WI-001: Registering a New Purchase Order

| Field | Value |
|-------|-------|
| **WI Number** | WI-001 |
| **Role** | [ADMIN] or [QA] |
| **Procedure** | PR-009 §6.1 — SDRL Identification During Contract Review |
| **Forms** | ERP Module — Purchase Order form (EPIC-03, E03-US03) |
| **Prerequisite State** | Customer record must exist (see WI-002) |
| **Result State** | New `mrb.order` record created with state = `NEW` |
| **Estimated Time** | 5 minutes |

#### Purpose

Register a customer Purchase Order in the ERP module so that the MRB lifecycle can begin.

#### Prerequisites

1. Customer record exists in the system (if not, perform WI-002 first).
2. You have the Purchase Order document from the customer (PO number, line items, delivery date).
3. You are logged in with Admin or QA Engineer role.

#### Steps

**Step 1:** Navigate to the **Purchase Orders** screen from the left sidebar menu.

*System response:* PO list view displays with columns: PO Number, Customer, Received Date, Delivery Date, Order State, Actions.

**Step 2:** Click the **"+ New PO"** button (top right, Aurelian Red).

*System response:* The Purchase Order creation form opens with empty fields.

**Step 3:** Enter the following required fields:

| Field | Format | Notes |
|-------|--------|-------|
| **PO Number** (R) | Text, max 50 characters | Must be unique per customer. Enter exactly as shown on the customer's PO document. Example: `PO-2026-00451` |
| **Customer** (R) | Dropdown / search | Select from existing customer records. If customer not found, perform WI-002 first. |
| **Received Date** (R) | Date picker | Date the PO was received by Aurelian. Defaults to today. |
| **Delivery Date** (O) | Date picker | Customer-requested delivery date, if specified on PO. |
| **Commercial Terms** (O) | JSON structure | Payment terms, Incoterms, special conditions. Can be updated later. |

**Step 4:** Add line items. Click **"+ Add Line Item"** for each product line on the PO.

For each line item, enter:

| Field | Format | Notes |
|-------|--------|-------|
| **Part Number** (R) | Text, max 100 characters | Customer's part number or drawing number |
| **Quantity** (R) | Integer | Number of parts ordered |
| **Material Grade** (R) | Text, max 100 characters | E.g., "AISI 316L", "Inconel 625", "F22". Must match material grades used in Material Requirement Profiles (WI-003). |
| **Drawing Revision** (O) | Text, max 20 characters | E.g., "Rev C", "Issue 3" |

*System response:* Each line item appears as a row in the line items table below the header fields.

**Step 5:** Review all entered data for accuracy against the customer's PO document.

**Step 6:** Click **"Save"** (bottom right).

*System response:*
- PO record saved to `erp.purchase_order` table.
- System automatically creates a linked `mrb.order` record with state = `NEW`.
- Audit log entry created: action = `ORDER_CREATED`, details include PO number and customer.
- Screen redirects to PO Detail view showing the new PO with its linked order state badge (`NEW` — gray).

*If error: "PO Number already exists for this customer"* — The PO number must be unique per customer. Verify you are not creating a duplicate. Check the PO list for existing entries.

#### Expected Result

- Purchase Order record exists in the ERP module with all line items.
- A linked order record exists in the MRB module with state `NEW`.
- The order appears in the QA Engineer's order queue, ready for SDRL processing (WI-004 or WI-005).

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "PO Number already exists" | Duplicate PO number for this customer | Verify PO number. Check if this PO was already registered. |
| "Customer not found" | Customer record does not exist | Perform WI-002 to create the customer record first. |
| "At least one line item required" | No line items added | Add at least one line item with part number, quantity, and material grade. |
| Delivery date in the past | Date entry error | Verify the delivery date from the customer PO. System allows past dates but displays a warning. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-002 | Customer record must exist before creating a PO |
| **After** | WI-004 or WI-005 | After PO is registered, process the SDRL |

---

### 6.2 WI-002: Creating a Customer Record

| Field | Value |
|-------|-------|
| **WI Number** | WI-002 |
| **Role** | [ADMIN] |
| **Procedure** | PR-009 §6.1 — SDRL Identification During Contract Review |
| **Forms** | ERP Module — Customer form (EPIC-03, E03-US01) |
| **Prerequisite State** | None — customer creation is independent of order state |
| **Result State** | New `erp.customer` record created |
| **Estimated Time** | 3 minutes |

#### Purpose

Create a customer record in the ERP module so that Purchase Orders and Material Requirement Profiles can be associated with this customer.

#### Prerequisites

1. You have the customer's legal name, organization number, and industry classification.
2. You have at least one contact person's details (name, email, phone, role).
3. You are logged in with Admin role.

#### Steps

**Step 1:** Navigate to the **Customers** screen from the left sidebar menu.

*System response:* Customer list view displays with columns: Name, Org Number, Industry, Contact Count, Actions. Search bar and industry filter dropdown available in the action bar.

**Step 2:** Click the **"+ New Customer"** button (top right, Aurelian Red).

*System response:* Customer creation form opens with empty fields.

**Step 3:** Enter the following fields:

| Field | Format | Notes |
|-------|--------|-------|
| **Company Name** (R) | Text, max 200 characters | Full legal name. E.g., "Equinor Energy AS", "Kongsberg Defence & Aerospace AS" |
| **Organization Number** (R) | Text, unique | Norwegian org number (9 digits) or international equivalent. Must be unique across all customers. |
| **Industry** (R) | ENUM dropdown | Select: `OIL_GAS`, `DEFENCE`, `MARITIME`, or `GENERAL`. This determines the default SDRL template and MRB section structure for this customer's orders. |
| **Payment Terms** (O) | Text | E.g., "Net 30 days", "60 days EOM" |

**Step 4:** Add at least one contact. Click **"+ Add Contact"** in the Contacts section.

For each contact, enter:

| Field | Format | Notes |
|-------|--------|-------|
| **Contact Name** (R) | Text | Full name of the contact person |
| **Email** (R) | Email format | Business email address |
| **Phone** (O) | Text | Include country code. E.g., "+47 999 88 777" |
| **Role** (R) | Text | E.g., "Quality Manager", "Project Engineer", "Procurement" |

*System response:* Contact appears in the contacts table below the header fields.

**Step 5:** Optionally add an address. Click **"+ Add Address"** in the Addresses section.

| Field | Format | Notes |
|-------|--------|-------|
| **Street** (R) | Text | Street address |
| **City** (R) | Text | City name |
| **Postal Code** (R) | Text | Postal / ZIP code |
| **Country** (R) | Text | Country name or ISO code |

**Step 6:** Click **"Save"** (bottom right).

*System response:*
- Customer record saved to `erp.customer` table.
- Audit log entry created.
- Screen redirects to Customer Detail view showing the new customer with empty order list.

*If error: "Organization number already exists"* — A customer with this org number is already registered. Navigate to the customer list and search for the existing record.

#### Expected Result

- Customer record exists in the ERP module with at least one contact.
- Customer appears in the customer dropdown when creating Purchase Orders (WI-001).
- Customer appears in the customer filter when creating Material Requirement Profiles (WI-003).

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "Organization number already exists" | Duplicate customer | Search the customer list for the existing record. Use the existing record instead. |
| "At least one contact required" | No contacts added | Add at least one contact with name, email, and role. |
| "Invalid email format" | Email address is malformed | Enter a valid email address (e.g., `name@company.com`). |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **After** | WI-001 | After creating the customer, register their Purchase Order |
| **After** | WI-003 | After creating the customer, set up Material Requirement Profiles for their typical material grades |

---

### 6.3 WI-003: Setting Up a Material Requirement Profile

| Field | Value |
|-------|-------|
| **WI Number** | WI-003 |
| **Role** | [ADMIN] or [QM] |
| **Procedure** | PR-008 §6.4 — Material Requirement Profiles |
| **Forms** | Material Requirement Profile form (EPIC-03, E03-US05, FM-008-04) |
| **Prerequisite State** | Customer record must exist (see WI-002) |
| **Result State** | New `mrb.material_requirement_profile` record created |
| **Estimated Time** | 10–15 minutes (depends on number of chemical elements and mechanical properties) |

#### Purpose

Define customer-specific acceptance criteria for a material grade. When a QA Engineer performs a Material Gate review (WI-007), the system auto-loads the applicable profile to compare actual certificate values against required limits.

#### Prerequisites

1. Customer record exists in the system (WI-002).
2. You have the customer's material specification or purchase order requirements, including:
   - Required certificate type (EN 10204 Type 2.1, 2.2, 3.1, or 3.2)
   - Chemical composition limits (per element: min/max percentages)
   - Mechanical property limits (tensile strength, yield strength, elongation, hardness, impact energy — with units)
   - Any supplementary test requirements (PMI, NDT, Charpy impact at specific temperature)
3. You are logged in with Admin or Quality Manager role.

#### Steps

**Step 1:** Navigate to the **Customers** screen. Find and click the customer record.

*System response:* Customer Detail view opens, showing customer information and tabs for Orders, Contacts, Material Profiles.

**Step 2:** Click the **"Material Profiles"** tab.

*System response:* Profile list view displays with columns: Material Grade, Cert Type Required, Chemical Elements, Mechanical Properties, Actions. May be empty if no profiles exist yet.

**Step 3:** Click **"+ New Profile"** (Aurelian Red button).

*System response:* Material Requirement Profile creation form opens.

**Step 4:** Enter the header fields:

| Field | Format | Notes |
|-------|--------|-------|
| **Customer** (A) | Auto-populated | Shows the customer name. Read-only — inherited from the customer you navigated from. |
| **Material Grade** (R) | Text, max 100 characters | E.g., "AISI 316L", "Inconel 625", "F22 Cl.3", "S355J2+N". Must match the material_grade values used in Purchase Order line items (WI-001, Step 4). |
| **Certificate Type Required** (R) | ENUM dropdown | Select the minimum certificate type required: `EN_10204_2_1`, `EN_10204_2_2`, `EN_10204_3_1`, `EN_10204_3_2`. For Oil & Gas (NORSOK), typically 3.1 or 3.2. For Defence, typically 3.1. |

**Step 5:** Define chemical composition limits. Click **"+ Add Element"** for each chemical element that has specification limits.

For each element, enter:

| Field | Format | Notes |
|-------|--------|-------|
| **Element** (R) | Text | Chemical symbol: C, Mn, Si, P, S, Cr, Ni, Mo, V, Ti, Cu, N, Nb, etc. |
| **Min %** (O) | Decimal (4 places) | Minimum acceptable percentage. Leave blank if no minimum. E.g., `0.0000` |
| **Max %** (R) | Decimal (4 places) | Maximum acceptable percentage. E.g., `0.0300` for max 0.03% Carbon |

*System response:* Each element appears as a row in the Chemical Limits table. Data stored as JSONB in `chemical_limits` column.

**Example — AISI 316L per NORSOK M-630:**

| Element | Min % | Max % |
|---------|-------|-------|
| C | — | 0.030 |
| Mn | — | 2.000 |
| Si | — | 1.000 |
| P | — | 0.045 |
| S | — | 0.030 |
| Cr | 16.000 | 18.000 |
| Ni | 10.000 | 14.000 |
| Mo | 2.000 | 3.000 |
| N | — | 0.100 |

**Step 6:** Define mechanical property limits. Click **"+ Add Property"** for each required mechanical property.

For each property, enter:

| Field | Format | Notes |
|-------|--------|-------|
| **Property** (R) | Text | E.g., "tensile_strength", "yield_strength", "elongation", "hardness", "impact_energy" |
| **Min** (O) | Decimal | Minimum acceptable value. E.g., `485` for min tensile strength |
| **Max** (O) | Decimal | Maximum acceptable value. E.g., `690` for max tensile strength |
| **Unit** (R) | Text | E.g., "MPa", "%", "HB", "J" |

*System response:* Each property appears as a row in the Mechanical Limits table. Data stored as JSONB in `mechanical_limits` column.

**Example — AISI 316L mechanical properties:**

| Property | Min | Max | Unit |
|----------|-----|-----|------|
| tensile_strength | 485 | 690 | MPa |
| yield_strength | 170 | — | MPa |
| elongation | 40 | — | % |
| hardness | — | 217 | HB |

**Step 7:** Optionally define supplementary test requirements. Click **"+ Add Supplementary Test"** if the customer requires tests beyond standard chemical and mechanical.

For each test, enter:

| Field | Format | Notes |
|-------|--------|-------|
| **Test Name** (R) | Text | E.g., "Charpy Impact -46°C", "PMI Verification", "Intergranular Corrosion per ASTM A262 Practice E" |
| **Standard** (O) | Text | Applicable standard. E.g., "ASTM A370", "NORSOK M-650 §6.3" |
| **Acceptance Criteria** (R) | Text | What constitutes a pass. E.g., "Average ≥ 27J, single ≥ 20J at -46°C" |

*System response:* Test requirements stored as JSONB array in `supplementary_tests` column.

**Step 8:** Review all entered limits against the customer's specification document.

**Step 9:** Click **"Save"** (bottom right).

*System response:*
- Profile saved to `mrb.material_requirement_profile` table.
- Profile is now available for auto-lookup during Material Gate reviews (WI-007).
- When a QA Engineer opens a Material Gate form for an order from this customer with matching material grade, the chemical and mechanical limits are auto-loaded into the check tables.

*If error: "Profile already exists for this customer and material grade"* — A profile with this exact customer + material_grade combination already exists. Edit the existing profile instead.

#### Expected Result

- Material Requirement Profile exists for the specified customer and material grade.
- Chemical limits define per-element min/max percentages.
- Mechanical limits define per-property min/max with units.
- Supplementary tests list additional requirements (if any).
- Profile auto-populates when a Material Gate review (WI-007) matches this customer and material grade.

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "Profile already exists" | Duplicate customer + material_grade | Navigate to the existing profile and edit it instead. |
| "At least one chemical or mechanical limit required" | No limits entered | Enter at least one chemical element limit or one mechanical property limit. A profile without any limits is meaningless. |
| Borderline flags not triggering in gate reviews | Max/min values entered incorrectly | Verify that limit values match the customer specification. Borderline detection uses a 5% threshold from the limit value. |
| Profile not auto-loading in gate review | Material grade mismatch | Ensure the `material_grade` text in the profile matches exactly (case-sensitive) the `material_grade` in the Purchase Order line items and material receipts. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-002 | Customer record must exist before creating profiles |
| **After** | WI-007 | Profiles are consumed during Material Gate reviews |

#### Industry Notes

| Industry | Typical Requirements |
|----------|---------------------|
| **Oil & Gas** | NORSOK M-630 Material Data Sheets define limits per material grade. EN 10204 Type 3.1 or 3.2 certificates typically required. Charpy impact testing at low temperatures (-46°C for arctic applications) is common. |
| **Defence** | AS9100D / AQAP 2110 requirements. EN 10204 Type 3.1 standard. NADCAP-approved labs for special process testing. Material traceability per serial number required. |

---

## 7. SDRL Processing Work Instructions (PR-009)

---

### 7.1 WI-004: Processing an SDRL — Upload Method ★

| Field | Value |
|-------|-------|
| **WI Number** | WI-004 |
| **Role** | [QA] |
| **Procedure** | PR-009 §6.2 — SDRL Parsing |
| **Forms** | FM-009-01 — Order Requirement Matrix |
| **Prerequisite State** | Order must be in state `NEW` or `SDRL_RECEIVED` |
| **Result State** | Order transitions to `SDRL_RECEIVED` (file uploaded); then proceed to WI-006 for confirmation |
| **Estimated Time** | 5–10 minutes |

#### Purpose

Upload a customer's SDRL file (Excel or CSV) so the system can automatically extract document requirements and generate the MRB structure.

#### Prerequisites

1. Purchase Order is registered (WI-001) and the linked order is in state `NEW` or `SDRL_RECEIVED`.
2. You have the customer's SDRL file in `.xlsx` or `.csv` format.
3. The SDRL file follows the column structure defined in AM-CT-001 §8.2 (or a recognizable variant).
4. You are logged in with QA Engineer role.

#### Steps

**Step 1:** Navigate to the **Purchase Orders** screen. Find and click the relevant PO.

*System response:* PO Detail view opens showing the PO header, line items, and linked order card with state badge.

**Step 2:** Click the **order state badge** or the **"Process SDRL"** link on the order card.

*System response:* The **SDRL Processing** screen opens (EPIC-05). The screen shows:
- Header: "SDRL Processing" (36pt Bold)
- Order context card: PO Number, Customer name, Industry badge (OIL_GAS / DEFENCE)
- Two-column layout: Left — file upload dropzone. Right — manual entry button + template selector.

**Step 3:** Drag the SDRL file onto the **upload dropzone** (or click the dropzone and select the file from your computer).

*System response:*
- Upload progress bar appears.
- File is stored in Supabase Storage at `aurelian-mrb/{customer_id}/{order_id}/source/sdrl_original.xlsx`.
- Parser begins processing the file.
- Parse status messages appear below the dropzone.

*If error: "Unsupported file format"* — Only `.xlsx` and `.csv` files are accepted. Convert the SDRL to Excel format first.

**Step 4:** Wait for the parser to complete. The parser maps Excel columns per AM-CT-001 §8.2:

| Expected Column | Maps To |
|----------------|---------|
| Line Item ID / Item No. | `line_item_id` |
| Document Title / Description | `doc_title` |
| Standard / Specification | `standard_ref` |
| MRB Section / Section No. | `mrb_section` |
| Format / Required Format | `required_format` |
| Review Code | `review_code` |
| Criticality | `criticality` |
| Data Source / Responsibility | `data_source` |
| Required (Y/N) | `is_required` |
| Timing / Submission | `submission_timing` |
| Notes / Remarks | `notes` |

*System response:* On successful parse:
- Total line items count displayed.
- Summary bar: CRITICAL count (red badge), MAJOR count (amber badge), STANDARD count (gray badge).
- Any unknown columns flagged as warnings (amber panel) — these are informational, not blocking.
- Any parse errors shown in the error panel with row/column references.

*If error: "Parse errors detected"* — Review the error panel. Common issues:
- Missing required columns → check that the Excel has the expected column headers
- Invalid ENUM values → values like "HIGH" need to be mapped to "CRITICAL"
- Row errors → specific rows with missing or malformed data

**Step 5:** If parse errors exist, correct the SDRL file and re-upload (repeat from Step 3). If only warnings exist (unknown columns), these can be ignored.

**Step 6:** On successful parse, order state transitions: `NEW` → `SDRL_RECEIVED`. Logged in audit_log.

**Step 7:** Proceed to **WI-006 (Reviewing and Confirming SDRL Parse Results)** to review and confirm the parsed data.

#### Expected Result

- SDRL file uploaded and stored in Supabase Storage.
- SDRL line items parsed and loaded into the review screen.
- Order state = `SDRL_RECEIVED`.
- Parsed data is ready for review and confirmation (WI-006).

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "Unsupported file format" | File is not .xlsx or .csv | Convert the file to Excel format. PDF SDRLs must be processed via manual entry (WI-005). |
| "No data rows found" | Excel file is empty or has only headers | Verify the file has data rows below the header row. |
| "Column mapping failed" | Column headers don't match expected format | Check AM-CT-001 §8.2 for expected column names. Rename columns to match, or use manual entry (WI-005). |
| "Order is not in a valid state" | Order is not in state NEW or SDRL_RECEIVED | Verify the order state. Only NEW or SDRL_RECEIVED orders can have SDRLs processed (VR-009-01-007). |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-001 | Purchase Order must exist with linked order in state NEW |
| **Alternative** | WI-005 | Use manual entry if the SDRL is not in Excel format |
| **After** | WI-006 | Review and confirm the parsed SDRL results |

---

### 7.2 WI-005: Processing an SDRL — Manual Entry Method ★

| Field | Value |
|-------|-------|
| **WI Number** | WI-005 |
| **Role** | [QA] |
| **Procedure** | PR-009 §6.2 — SDRL Parsing |
| **Forms** | FM-009-01 — Order Requirement Matrix |
| **Prerequisite State** | Order must be in state `NEW` or `SDRL_RECEIVED` |
| **Result State** | SDRL line items entered; proceed to WI-006 for confirmation |
| **Estimated Time** | 15–30 minutes (depends on number of line items) |

#### Purpose

Manually enter SDRL requirements when the customer's SDRL is not in a machine-readable format (PDF, email, or non-standard Excel). Uses industry templates as a starting point.

#### Prerequisites

1. Purchase Order is registered (WI-001) and the linked order is in state `NEW` or `SDRL_RECEIVED`.
2. You have the customer's SDRL document (in any format — PDF, email, paper).
3. You know the customer's industry classification (Oil & Gas or Defence).
4. You are logged in with QA Engineer role.

#### Steps

**Step 1:** Navigate to the **SDRL Processing** screen (same as WI-004, Steps 1–2).

**Step 2:** Click the **"Manual Entry"** button (right side of the two-column layout).

*System response:* The template selector dropdown appears.

**Step 3:** Select the appropriate industry template from the dropdown:

| Template | Industry | Default Line Items | Source |
|----------|----------|-------------------|--------|
| **SDRL-OG-001** | Oil & Gas | 39 line items across 7 MRB sections | AM-CT-001 §4.2 |
| **SDRL-DEF-001** | Defence | 31 line items across 8 MRB sections | AM-CT-001 §5.2 |

*System response:*
- Template line items are pre-populated into the line item table.
- Each row shows: line_item_id, mrb_section, doc_title, standard_ref, required_format, review_code, criticality, data_source, is_required, submission_timing.
- `parse_method` is set to `MANUAL`.
- All fields are editable.

**Step 4:** Compare the template line items against the customer's SDRL document. For each line item:

- **If the customer requires it as shown** → leave unchanged.
- **If the customer requires it with different settings** → modify the fields (e.g., change review_code from FOR_INFO to FOR_APPROVAL, or change criticality from STANDARD to CRITICAL).
- **If the customer does NOT require it** → uncheck the **"Required"** checkbox (sets `is_required` = false). Do NOT delete the row — keep it for reference.
- **If the customer requires something NOT in the template** → click **"+ Add Row"** and enter the custom line item.

**Step 5:** For each line item, verify the following fields per FM-009-01 fields 14–28:

| Field | How to Set |
|-------|-----------|
| **Line Item ID** (A) | Auto-generated from template. Editable for custom items. Format: `OG-SS-NN` or `DEF-SS-NN` where SS = section, NN = sequence. |
| **MRB Section** (R) | Dropdown: 1–7 for Oil & Gas, 1–8 for Defence. Must match the section where this document belongs. |
| **Document Title** (R) | Descriptive name. E.g., "Material Test Certificate (EN 10204 Type 3.1)". |
| **Standard / Spec** (O) | Applicable standard. E.g., "EN 10204", "ASME V", "NORSOK M-650". |
| **Required Format** (R) | Dropdown: `PDF`, `PDF_A`, `NATIVE`, `SIGNED`. |
| **Review Code** (R) | Dropdown: `FOR_INFO`, `FOR_REVIEW`, `FOR_APPROVAL`. |
| **Criticality** (R) | Dropdown: `CRITICAL`, `MAJOR`, `STANDARD`. |
| **Data Source** (R) | Dropdown: `CNC_INLINE`, `METROLOGY`, `INSPECTION`, `SUPPLIER`, `SPECIAL_PROCESS`, `INTERNAL_QA`, `CUSTOMER`. |
| **Is Required** (R) | Checkbox. True = mandatory for MRB completeness. |
| **Submission Timing** (R) | Dropdown: `WITH_SHIPMENT`, `BEFORE_SHIPMENT`, `AT_MILESTONE`, `ON_REQUEST`. |
| **Notes** (O) | Customer-specific instructions or clarifications. |

**Step 6:** Verify that at least one line item has criticality = `CRITICAL` (VR-009-01-003).

**Step 7:** Verify that line_item_id values are unique within this SDRL (VR-009-01-004).

**Step 8:** Proceed to **WI-006 (Reviewing and Confirming SDRL Parse Results)** to review and confirm.

#### Expected Result

- SDRL line items entered from template with customer-specific modifications.
- Parse method recorded as MANUAL.
- Data is ready for review and confirmation (WI-006).

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| Wrong template selected | Customer is Oil & Gas but Defence template was chosen | Start over with the correct template. The section structure differs (7 vs 8 sections). |
| "No CRITICAL line items" | All items set to MAJOR or STANDARD | At least one item must be CRITICAL per VR-009-01-003. Material certificates and CoC are typically CRITICAL. |
| "Duplicate line item ID" | Two rows have the same line_item_id | VR-009-01-001 requires unique IDs. Modify the duplicate. |
| Unknown document title warning | doc_title not in Document Type Registry | Informational warning only (VR-009-01-005). The document title is valid but not standard. Verify it is correct. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-001 | Purchase Order must exist |
| **Alternative** | WI-004 | Use upload method if SDRL is in Excel format |
| **After** | WI-006 | Review and confirm the entered SDRL |

---

### 7.3 WI-006: Reviewing and Confirming SDRL Parse Results ★

| Field | Value |
|-------|-------|
| **WI Number** | WI-006 |
| **Role** | [QA] |
| **Procedure** | PR-009 §6.3 — SDRL Confirmation and MRB Initialization |
| **Forms** | FM-009-01 (confirmation), FM-009-04 (MRB Index — generated) |
| **Prerequisite State** | SDRL line items loaded (from WI-004 or WI-005). Order in state `NEW` or `SDRL_RECEIVED`. |
| **Result State** | Order transitions: `SDRL_RECEIVED` → `SDRL_PARSED` → `MRB_INITIALIZED`. MRB Index generated. |
| **Estimated Time** | 5–10 minutes |

#### Purpose

Review parsed SDRL line items for accuracy, then confirm to trigger MRB initialization. This is the point of no return — after confirmation, the MRB structure is created and document collection can begin.

#### Prerequisites

1. SDRL line items have been loaded via upload (WI-004) or manual entry (WI-005).
2. You have the customer's original SDRL document open for comparison.
3. You are logged in with QA Engineer role.

#### Steps

**Step 1:** The **SDRL Review** screen should be displayed after completing WI-004 or WI-005. If not, navigate to the order and click "Review SDRL".

*System response:* SDRL Review screen shows:
- Header card: Order info (PO number, customer, industry) + SDRL metadata (template used, total items, parse method)
- Stats bar: total line items, CRITICAL count (red badge), MAJOR count (amber badge), STANDARD count (gray badge)
- Full-width line item table with all columns, inline editable, sortable

**Step 2:** Review the **stats bar** for reasonableness:
- Oil & Gas orders typically have ~30 line items (SDRL-OG-001 template: 39 default)
- Defence orders typically have ~25 line items (SDRL-DEF-001 template: 31 default)
- At least one CRITICAL item must exist
- If numbers seem wrong, review the line items in detail

**Step 3:** Review each line item against the customer's SDRL document:
- Verify document titles match customer terminology
- Verify criticality levels match customer priority designations
- Verify review codes match customer requirements (FOR_INFO vs FOR_REVIEW vs FOR_APPROVAL)
- Verify data sources are correctly assigned (determines who is responsible for each document)

**Step 4:** Make any necessary inline edits. Click a cell to edit. Changes are highlighted.

**Step 5:** If additional line items are needed, click **"+ Add Row"** in the action bar. If a line item should be removed, uncheck its "Required" checkbox rather than deleting it.

**Step 6:** When satisfied, click **"Confirm SDRL"** (Aurelian Red button in the action bar).

*System response:* The system validates all line items:
- VR-009-01-001: No duplicate line_item_id values
- VR-009-01-002: All mrb_section values in valid range (1–7 for O&G, 1–8 for Defence)
- VR-009-01-003: At least one CRITICAL item exists
- VR-009-01-004: At least one line item exists
- VR-009-01-005: Unknown doc_title values flagged (warning only)
- VR-009-01-006: ITP-related line items detected → flag for ITP Tracker
- VR-009-01-007: Order in valid state

*If validation fails:* Error panel shows specific issues. Fix the problems and click "Confirm SDRL" again.

**Step 7:** On successful confirmation, the system performs:
1. SDRL line items committed to `mrb.sdrl_line_item` table.
2. Order state transitions: `SDRL_RECEIVED` → `SDRL_PARSED`.
3. MRB record created with auto-generated number: `AM-MRB-YYYY-NNNNN`.
4. MRB Index generated from SDRL line items:
   - All document statuses set to `PENDING`
   - MRB Index state set to `DRAFT`
   - Section dividers created for each MRB section
5. Order state transitions: `SDRL_PARSED` → `MRB_INITIALIZED`.
6. All state transitions logged in audit_log.
7. IF-008 triggered (Order State Update to ERP).

*System response:* Screen redirects to the **MRB Index View** showing the newly created MRB:
- Header: MRB number (e.g., AM-MRB-2026-00001), order info, MRB state badge (`DRAFT` — amber)
- Full-width table with columns per AM-CT-001 §6.2
- All status cells show `PENDING` (gray)
- Footer: summary row with total/pending/received/validated counts (all pending)
- Completion percentage: 0%

**Step 8:** Verify the MRB Index looks correct:
- Correct number of sections (7 for O&G, 8 for Defence)
- Section headers in correct order
- Line items grouped under correct sections
- MRB number generated correctly

#### Expected Result

- SDRL is confirmed and committed to database.
- MRB record created with unique MRB number.
- MRB Index generated with all document slots in PENDING state.
- Order state = `MRB_INITIALIZED`.
- QA Engineer can now begin document collection (WI-009) and material gate reviews (WI-007).

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "Duplicate line item ID" | Two line items have the same ID | Edit one of the duplicate IDs to make it unique. |
| "MRB section out of range" | Section number > 7 (O&G) or > 8 (Defence) | Correct the section number. Sections must be 1–7 for Oil & Gas, 1–8 for Defence. |
| "No CRITICAL line items" | All criticality values are MAJOR or STANDARD | Set at least one item to CRITICAL (typically material certificates and CoC). |
| "SDRL must contain at least one line item" | All line items were removed | Restore at least one required line item. |
| ITP flag notification | ITP-related line items detected | Informational. In Phase 0, this is a flag only — the ITP Tracker (FM-009-02) will be implemented in Phase 0.5. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-004 or WI-005 | SDRL must be loaded before it can be reviewed |
| **After** | WI-007 | Begin material gate reviews for incoming materials |
| **After** | WI-009 | Begin uploading documents to MRB slots |

---

## 8. Material Gate Work Instructions (PR-008)

---

### 8.1 WI-007: Performing a Material Gate Review ★

| Field | Value |
|-------|-------|
| **WI Number** | WI-007 |
| **Role** | [QA] |
| **Procedure** | PR-008 §6.1–6.3 — Material Arrival, Certificate Check, Gate Decision |
| **Forms** | FM-008-01 — Material Gate Checklist (33 fields, 11 validation rules) |
| **Prerequisite State** | Material receipt exists with `gate_decision` = `PENDING`. Order in state `MRB_INITIALIZED` or later. |
| **Result State** | Gate decision recorded: `RELEASED`, `REJECTED`, or `REVIEW` (escalated) |
| **Estimated Time** | 15–25 minutes (depends on number of chemical elements and mechanical properties) |

#### Purpose

Evaluate an incoming material certificate against customer-specific requirements using the 5-point certificate check. This is the first quality gate — no material enters production without passing this review.

#### Prerequisites

1. Order is in state `MRB_INITIALIZED` or later.
2. Material receipt has been recorded (WI-001, Step: E03-US04) with `gate_decision` = `PENDING`.
3. Material certificate (EN 10204) has been uploaded to the material receipt record.
4. Material Requirement Profile exists for this customer + material grade (WI-003). If no profile exists, the system cannot auto-populate limits — you must create one first.
5. You are logged in with QA Engineer role.

#### Steps

**Step 1:** Navigate to the **Material Gate Queue** from the left sidebar (or from the dashboard "Pending Reviews" card).

*System response:* The Material Gate queue displays all material receipts with `gate_decision` = `PENDING`, grouped by order. Columns: Order/PO, Customer, Material Grade, Heat Number, Supplier, Received Date, Actions.

**Step 2:** Click the receipt you want to review.

*System response:* The **Material Gate Form** (FM-008-01) opens with three panels:

- **Top panel (read-only):** Receipt info card showing:
  - Order / PO Number (FM-008-01, fields 4–5, auto-populated)
  - Customer and Industry (fields 6–7, auto-populated)
  - Material Grade (field 8, from receipt)
  - Heat Number (field 9, from receipt)
  - Supplier (field 10, from receipt)
  - Certificate Type Required (field 12, auto-populated from Material Requirement Profile)
  - **Certificate Viewer** button — click to open the uploaded certificate PDF inline
  - **Material Requirement Profile** card — shows the applicable chemical/mechanical limits

- **Middle panel (interactive):** 5 tabbed check sections (see Steps 3–7)

- **Bottom panel (locked until all checks complete):** Decision section

**Step 3: Check 1 — Certificate Type** (PR-008 §6.3, Check 1)

Click the **"Certificate Type"** tab.

| Action | Detail |
|--------|--------|
| Select the actual certificate type received | Dropdown: `EN_10204_2_1`, `EN_10204_2_2`, `EN_10204_3_1`, `EN_10204_3_2` |
| System auto-compares | Hierarchy: 3.2 > 3.1 > 2.2 > 2.1. PASS if actual ≥ required. FAIL if actual < required. (VR-008-01-011) |

*System response:* Result displayed next to dropdown: green "PASS" or red "FAIL".

*Example:* Required = 3.1, Actual = 3.1 → PASS. Required = 3.1, Actual = 2.2 → FAIL.

**Step 4: Check 2 — Chemical Analysis** (PR-008 §6.3, Check 2)

Click the **"Chemical Analysis"** tab.

*System response:* Dynamic table with one row per element from the Material Requirement Profile's `chemical_limits`. Columns:

| Column | Source |
|--------|--------|
| Element | From profile (auto-populated) |
| Min % | From profile (auto-populated) |
| Max % | From profile (auto-populated) |
| **Actual %** | **Enter from certificate** |
| Result | Auto-calculated: PASS / FAIL / BORDERLINE |

**For each element:** Read the actual value from the material certificate and enter it in the "Actual %" column.

*System response:* After each entry, the system auto-calculates:
- **PASS** (green): value within limits
- **FAIL** (red): value outside limits
- **BORDERLINE** (amber): value within 5% of a limit (per VR-008-01-010)

*Example:* Max Carbon = 0.030%. Actual = 0.028% → BORDERLINE (within 5% of limit: 0.030 × 0.95 = 0.0285). Actual = 0.025% → PASS. Actual = 0.035% → FAIL.

**Step 5: Check 3 — Mechanical Properties** (PR-008 §6.3, Check 3)

Click the **"Mechanical Properties"** tab.

*System response:* Dynamic table with one row per property from the Material Requirement Profile's `mechanical_limits`. Columns:

| Column | Source |
|--------|--------|
| Property | From profile (auto-populated) |
| Min | From profile |
| Max | From profile |
| Unit | From profile |
| **Actual** | **Enter from certificate** |
| Result | Auto-calculated |

**For each property:** Read the actual value from the material certificate and enter it.

*Example:* Tensile Strength: Min = 485 MPa, Max = 690 MPa. Actual = 520 MPa → PASS.

**Step 6: Check 4 — Supplementary Tests** (PR-008 §6.3, Check 4)

Click the **"Supplementary Tests"** tab.

*System response:* This tab is only visible if the Material Requirement Profile has supplementary test entries. If no supplementary tests are required, this tab shows "No supplementary tests required — PASS" and auto-passes.

If supplementary tests exist, a checklist appears with one row per test requirement:

| Column | Action |
|--------|--------|
| Test Name | From profile (read-only) |
| Standard | From profile (read-only) |
| Acceptance Criteria | From profile (read-only) |
| **Present on Certificate?** | Toggle: Yes / No |
| **Meets Criteria?** | Toggle: Pass / Fail (enabled only if Present = Yes) |

**For each test:** Check if the certificate includes the test results. If yes, verify the results meet the acceptance criteria.

**Step 7: Check 5 — Traceability & Integrity** (PR-008 §6.3, Check 5)

Click the **"Traceability & Integrity"** tab.

*System response:* Checklist of verification items:

| Check Item | Action |
|------------|--------|
| Heat number traceable on certificate | Toggle: Yes / No |
| Certificate signature/authorization present | Toggle: Yes / No |
| Certificate date is current (not expired) | Toggle: Yes / No |
| Supplier is on Approved Supplier List | Auto-checked from `erp.supplier.approved_status` |
| No integrity red flags detected | Toggle: Yes / No / FLAG |

If any item = No → Check 5 result = FAIL.
If any item = FLAG → Check 5 result = FLAG. The field `physical_inspection_required` auto-sets to true (VR-008-01-009).

**Optional:** Enter integrity flags in the collapsible **"Integrity Flags"** section:
- Flag description (text)
- Severity: LOW / MEDIUM / HIGH
- Example: "Identical chemical values across 3 different heat numbers from this supplier"

**Step 8: Gate Decision** (PR-008 §6.3, Decision)

After all 5 checks have values, the **Decision section** at the bottom unlocks.

Review the check summary:

| Check | Result |
|-------|--------|
| Check 1 — Certificate Type | PASS / FAIL |
| Check 2 — Chemical Analysis | PASS / FAIL / BORDERLINE |
| Check 3 — Mechanical Properties | PASS / FAIL / BORDERLINE |
| Check 4 — Supplementary Tests | PASS / FAIL / N/A |
| Check 5 — Traceability | PASS / FAIL / FLAG |

**Make your decision:**

| Decision | When | Effect |
|----------|------|--------|
| **RELEASED** | All checks PASS (borderline is acceptable) | Material released to production. MRB Index Section 3 updates. |
| **REJECTED** | Any check = FAIL | Material blocked. Correction Request auto-created (FM-010-01). |
| **REVIEW** | You need Quality Manager input | Gate review escalated to QM queue (WI-008). You cannot proceed. |

**Rules:**
- RELEASED is blocked if any check = FAIL (VR-008-01-002)
- Decision reason is required for ALL decisions (VR-008-01-003)
- REVIEW triggers QM override flow (VR-008-01-007)

**Step 9:** Select the decision from the dropdown and enter the **Decision Reason** (required text field).

**Step 10:** Click **"Submit Gate Decision"** (Aurelian Red button).

*System response:*

**If RELEASED:**
- `material_receipt.gate_decision` = RELEASED
- `gate_review` record created with all check results (JSONB), reviewer_id, timestamp
- MRB Index Section 3 document status updates (material cert → RECEIVED)
- Audit log entry created
- Green confirmation banner: "Material RELEASED — gate review complete"

**If REJECTED:**
- `material_receipt.gate_decision` = REJECTED
- System auto-creates a draft Correction Request (FM-010-01)
- You are prompted to complete the CR details (see WI-011):
  - Failure code, specific finding, required action, responsible party, due date
- Red notification: "Material REJECTED — Correction Request CR-YYYY-NNNNN created"

**If REVIEW:**
- `gate_review.qm_override` = true
- Gate review appears in Quality Manager's pending queue
- Amber notification: "Gate review escalated to Quality Manager for override"
- You cannot make further changes until QM decides (WI-008)

#### Expected Result

- Gate review record exists with all 5 check results documented.
- Material receipt has a gate decision (RELEASED, REJECTED, or REVIEW).
- If RELEASED: material cleared for production, MRB Index updated.
- If REJECTED: Correction Request created, supplier or purchasing must resolve.
- If REVIEW: escalated to Quality Manager queue.

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "All 5 checks must be completed" | One or more check tabs not visited | Complete all 5 check tabs before making a decision. |
| "Cannot RELEASE with failing checks" | Attempting RELEASED when a check = FAIL | Either correct the failing check value, select REJECTED, or escalate to REVIEW. |
| "Decision reason required" | Reason field is empty | Enter a reason for your decision (required for all decisions). |
| "No Material Requirement Profile found" | No profile for this customer + material_grade | Create a profile first (WI-003). Without a profile, chemical/mechanical checks cannot auto-populate limits. |
| Certificate PDF won't open | PDF is corrupted or not a valid PDF | Ask the supplier for a replacement certificate. Re-upload to the material receipt record. |
| Borderline values showing | Values within 5% of limits | Borderline is informational only — it does not block RELEASED. Document in the decision reason that borderline values were reviewed. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-003 | Material Requirement Profile must exist for the customer + material grade |
| **Before** | WI-001 / WI-006 | Order must be initialized with MRB structure |
| **Conditional** | WI-008 | If decision = REVIEW, QM Override is required |
| **Conditional** | WI-011 | If decision = REJECTED, a Correction Request must be managed |

---

### 8.2 WI-008: Handling a QM Override (Escalated Gate)

| Field | Value |
|-------|-------|
| **WI Number** | WI-008 |
| **Role** | [QM] |
| **Procedure** | PR-008 §6.5 — Quality Manager Override |
| **Forms** | FM-008-01 — Material Gate Checklist (QM Override section, fields 30–33) |
| **Prerequisite State** | Gate review exists with `qm_override` = true and `gate_decision` = `REVIEW` |
| **Result State** | QM decision recorded: `RELEASED` or `REJECTED` |
| **Estimated Time** | 5–10 minutes |

#### Purpose

Make a final decision on a material gate review that was escalated by the QA Engineer. Quality Manager has the authority to release material that the QA Engineer was uncertain about, or to reject it definitively.

#### Prerequisites

1. A gate review has been escalated with decision = `REVIEW` (from WI-007).
2. You are logged in with Quality Manager role.

#### Steps

**Step 1:** Navigate to the **Pending QM Reviews** queue on the Quality Manager dashboard (or via the notification indicator).

*System response:* Queue displays all gate reviews with `qm_override` = true and no QM decision yet. Columns: Order/PO, Customer, Material Grade, Heat Number, QA Engineer's Notes, Escalated Date.

**Step 2:** Click the escalated gate review.

*System response:* The Material Gate Form opens in QM Override mode. The form shows:
- All 5 check results from the QA Engineer (read-only)
- Borderline flags (if any) highlighted in amber
- Integrity flags (if any) highlighted in red
- QA Engineer's decision reason
- Certificate viewer (click to open PDF inline)
- Material Requirement Profile card (reference)
- **QM Override section** (bottom, editable)

**Step 3:** Review all 5 check results carefully. Pay particular attention to:
- Borderline values (within 5% of limits) — are these acceptable for this customer and application?
- Integrity flags — are the concerns valid?
- Check 1 failures — is a lower certificate type acceptable?

**Step 4:** Open the certificate PDF and verify the QA Engineer's findings.

**Step 5:** In the **QM Override section**, select your decision:

| Decision | When |
|----------|------|
| **RELEASED** | You are satisfied the material meets requirements despite QA concerns. Borderline values are acceptable. Integrity flags are explainable. |
| **REJECTED** | You confirm the material does not meet requirements. Corrective action is needed. |

**Note:** Quality Manager can only select RELEASED or REJECTED — not REVIEW (VR-008-01-008). The QM is the final authority.

**Step 6:** Enter the **QM Decision Reason** (required text field). Be specific about why you are overriding the QA Engineer's uncertainty.

**Step 7:** Click **"Submit QM Decision"**.

*System response:*
- QM decision recorded in fields 30–33: `qm_decision`, `qm_decision_reason`, `qm_reviewer_id`, `qm_reviewed_at`
- Same downstream effects as WI-007 Step 10 (RELEASED or REJECTED path)
- Gate review removed from QM queue
- QA Engineer notified of QM decision

#### Expected Result

- QM decision recorded with full justification.
- Material either RELEASED (proceeds to production) or REJECTED (CR created).
- Gate review complete — no longer in pending queue.

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "Only RELEASED or REJECTED allowed" | Attempting to select REVIEW | QM is the final authority — must make a definitive decision. |
| "QM decision reason required" | Reason field is empty | Enter a detailed justification for your decision. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-007 | QA Engineer must escalate a gate review for QM override |
| **Conditional** | WI-011 | If QM decision = REJECTED, a Correction Request must be managed |

---

## 9. Document Collection Work Instructions (PR-009 / PR-010)

---

### 9.1 WI-009: Uploading Documents to MRB Slots ★

| Field | Value |
|-------|-------|
| **WI Number** | WI-009 |
| **Role** | [QA] or [PRODUCTION] |
| **Procedure** | PR-009 §6.5 — Document Collection |
| **Forms** | FM-009-04 — MRB Index (document slot selection) |
| **Prerequisite State** | Order in state `MRB_INITIALIZED` or `COLLECTING`. MRB Index exists. |
| **Result State** | Document uploaded. MRB Index slot status transitions: `PENDING` → `RECEIVED` → `VALIDATING` → `VALIDATED` (or `REJECTED`). MRB Index state transitions from `DRAFT` to `LIVE` on first document receipt. |
| **Estimated Time** | 2–5 minutes per document |

#### Purpose

Upload quality documents (certificates, inspection reports, test reports) to their designated slots in the MRB Index. Each uploaded document is automatically validated through L1–L3 checks.

#### Prerequisites

1. MRB Index exists for this order (WI-006 completed).
2. You have the document file ready (PDF preferred; other formats accepted based on `required_format` in the SDRL line item).
3. You know which MRB slot this document belongs to (match document title to MRB Index line item).
4. You are logged in with QA Engineer or Production role.

#### Steps

**Step 1:** Navigate to the order's **MRB Index View**. From the order detail page, click the MRB card or "View MRB Index".

*System response:* MRB Index View displays:
- Header: MRB number, order info, MRB state badge (DRAFT or LIVE), completion percentage
- Full-width table with all document slots
- Status column color-coded: PENDING (gray), RECEIVED (steel blue), VALIDATING (amber), VALIDATED (green), REJECTED (red)
- Section dividers (dark rows) for each MRB section

**Step 2:** Find the document slot you want to populate. Locate it by:
- MRB Section (e.g., Section 3 = Material Certificates)
- Document Title (e.g., "Material Test Certificate (EN 10204 Type 3.1)")
- Line Item ID (e.g., OG-03-01)

**Step 3:** Click on the **PENDING** status cell (or the document title) for that slot.

*System response:* The **Document Upload** panel opens (slide-out or modal):
- Header: Document title, MRB section, required format, review code, criticality
- File upload dropzone: drag-and-drop area with supported format indicator
- Format requirement indicator (e.g., "Required: PDF" or "Required: PDF/A")

**Step 4:** Drag the document file onto the dropzone (or click to select from your computer).

*System response:*
- Upload progress bar appears
- File stored in Supabase Storage at `aurelian-mrb/{customer_id}/{order_id}/validated/{doc_type}/`
- SHA-256 checksum computed and stored in `mrb_document.checksum_sha256`
- Metadata recorded: filename, MIME type, file size, upload timestamp, uploader user_id
- `mrb_document.artifact_uri` set to Storage path

**Step 5:** Automatic validation begins immediately (L1 → L2 → L3):

*System response:* Validation progress indicator shows each layer:

| Layer | Check | Auto/Manual |
|-------|-------|-------------|
| **L1 — Existence** | File exists in the MRB slot | Automatic |
| **L2 — Format** | MIME type matches required_format. File is readable, not corrupted. PDF/A compliance if required. | Automatic |
| **L3 — Completeness** | Document content checked against Document Type Registry schema. For EN 10204: heat number, chemical composition table, mechanical properties table, authorized signature, test date must be present. | Automatic |

Progress indicator updates in real-time:
- L1: ✓ PASS → L2: ✓ PASS → L3: ✓ PASS → **VALIDATED** (green confirmation)
- L1: ✓ PASS → L2: ✗ FAIL → **REJECTED** (red error, stops at failed layer)

**Step 6a — If all layers PASS:**

*System response:*
- Document status → `VALIDATED`
- Green confirmation banner: "Document validated (L1–L3 PASS)"
- MRB Index updates automatically:
  - Status column: `VALIDATED` (green)
  - Received Date: today
  - Validated Date: today
  - Document Reference: clickable link to the uploaded file
- Completion percentage recalculates
- Validation record created in `mrb.validation` table

**Step 6b — If any layer FAILS:**

*System response:*
- Document status → `REJECTED`
- Red error panel with specific failure details:
  - Which layer failed (L1, L2, or L3)
  - What specifically failed (e.g., "L2: File is not a valid PDF", "L3: Missing chemical composition table")
- Correction Request (FM-010-01) auto-created in draft status (see WI-011)
- MRB Index status shows `REJECTED` (red)

**Step 7:** If this is the first document uploaded for this MRB, the MRB Index state transitions from `DRAFT` to `LIVE`. The order state transitions from `MRB_INITIALIZED` to `COLLECTING`.

**Step 8:** Repeat Steps 2–6 for each document in the MRB. You can upload multiple documents in sequence.

#### Expected Result

- Document stored in Supabase Storage with integrity checksum.
- Validation results recorded (L1–L3).
- MRB Index updated with status, dates, and document reference.
- If validated: document slot is complete.
- If rejected: Correction Request created for follow-up (WI-011).

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "L2 FAIL: File is not a valid PDF" | File is corrupted, renamed, or wrong format | Obtain a valid PDF from the source. Check the MIME type. |
| "L2 FAIL: PDF/A compliance required" | Document is standard PDF but slot requires PDF/A | Convert the PDF to PDF/A format, or ask the source to provide PDF/A. |
| "L3 FAIL: Missing heat number" | Certificate doesn't contain the expected fields | The certificate is incomplete. Issue a Correction Request to the supplier (WI-011). |
| "L3 FAIL: Missing authorized signature" | Certificate not signed | Request a signed certificate from the supplier. |
| Wrong slot selected | Document uploaded to incorrect MRB line item | The document will fail L3 validation (content mismatch). Upload to the correct slot instead. |
| Upload times out | File too large or network issues | Retry the upload. Maximum file size is configured in Supabase Storage settings. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-006 | MRB Index must exist before documents can be uploaded |
| **Before** | WI-007 | Material certificates should pass the gate before being uploaded to MRB slots |
| **After** | WI-010 | Review detailed validation results if needed |
| **Conditional** | WI-011 | If validation fails, manage the Correction Request |

---

### 9.2 WI-010: Reviewing Validation Results (L1–L3) ★

| Field | Value |
|-------|-------|
| **WI Number** | WI-010 |
| **Role** | [QA] |
| **Procedure** | PR-010 §6.2–6.4 — Validation Layers L1–L3 |
| **Forms** | FM-010-02 — Document Validation Log |
| **Prerequisite State** | At least one document has been uploaded and validated (WI-009) |
| **Result State** | No state change — this is a review/monitoring activity |
| **Estimated Time** | 5–10 minutes per order review |

#### Purpose

Review the detailed validation results for documents in an order's MRB. Understand why documents passed or failed, and identify any outstanding validation issues.

#### Prerequisites

1. At least one document has been uploaded for this order (WI-009).
2. You are logged in with QA Engineer role.

#### Steps

**Step 1:** Navigate to the order's **MRB Index View**.

*System response:* MRB Index with status column showing the validation state of each document slot.

**Step 2:** To view overall order progress, check the **summary row** at the bottom of the MRB Index:
- Total required documents
- Received count
- Validated count
- Rejected count
- Pending count
- Completion percentage

**Step 3:** To view detailed validation results for a specific document, click the **Status badge** for that document slot.

*System response:* The **Document Validation Detail** panel opens showing:
- Document metadata: title, MRB section, data source, required format
- Validation history table (one row per validation layer):

| Layer | Result | Details | Method | Validator | Date |
|-------|--------|---------|--------|-----------|------|
| L1 — Existence | PASS / FAIL | File exists in slot | AUTOMATIC | SYSTEM | timestamp |
| L2 — Format | PASS / FAIL | MIME type, readability, PDF/A compliance | AUTOMATIC | SYSTEM | timestamp |
| L3 — Completeness | PASS / FAIL | Required fields present/missing list | AUTOMATIC | SYSTEM | timestamp |

**Step 4:** For failed validations, review the **failure details**:
- L1 failures: document not uploaded → upload the document (WI-009)
- L2 failures: format issues → obtain correct format from source
- L3 failures: missing content → request complete document from source

Each failure links to its associated Correction Request (if one was auto-created).

**Step 5:** To see all validation activity across an order, navigate to the **Validation Log** tab on the order detail page.

*System response:* Full validation log showing all validation events for this order:
- Sortable by: document, layer, result, date
- Filterable by: layer (L1/L2/L3), result (PASS/FAIL/WAIVED)
- Each row shows: Document Title, Layer, Result, Details, Method, Validator, Date

**Step 6:** To review only failures, apply the filter: Result = **FAIL**.

*System response:* Filtered list of all failed validations. Each links to the associated Correction Request.

#### Expected Result

- Understanding of which documents are validated, which are pending, and which have failed.
- Ability to identify and address outstanding validation issues.

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| Status shows VALIDATING for extended time | Validation engine is processing | Wait for validation to complete. If stuck, check system logs. |
| Same document fails repeatedly | Underlying issue with document quality | Review the failure details carefully. The source document may genuinely be deficient. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-009 | Documents must be uploaded before validation results exist |
| **After** | WI-011 | If failures exist, manage Correction Requests |

---

## 10. Correction Request Work Instructions (PR-010)

---

### 10.1 WI-011: Managing Correction Requests ★

| Field | Value |
|-------|-------|
| **WI Number** | WI-011 |
| **Role** | [QA] (create, manage) and [QM] (waiver approval) |
| **Procedure** | PR-010 §6.12 — Correction Request Process |
| **Forms** | FM-010-01 — Correction Request (30 fields) |
| **Prerequisite State** | Correction Request exists (auto-created from validation failure or gate rejection) |
| **Result State** | CR status progresses: `OPEN` → `IN_PROGRESS` → `RESOLVED` / `ESCALATED` / `WAIVED` |
| **Estimated Time** | 5 minutes (initial completion) + variable (resolution tracking) |

#### Purpose

Track document validation failures from detection through resolution. Correction Requests ensure that every failure is documented, assigned, tracked, and resolved before the MRB can be completed.

#### Prerequisites

1. A Correction Request has been auto-created by the system (from validation failure in WI-009/WI-010, or from gate rejection in WI-007).
2. You are logged in with QA Engineer role (or Quality Manager for waivers).

#### Part A: Completing a Draft Correction Request

When a validation fails or a gate decision is REJECTED, the system auto-creates a draft CR with fields 1–12 pre-populated. The QA Engineer must complete fields 13–18.

**Step 1:** Navigate to the **Correction Requests** list. Access from:
- The notification banner after a validation failure
- The order detail page → "Correction Requests" tab
- The MRB Index → click a REJECTED status → "View CR" link
- The left sidebar → "Correction Requests"

*System response:* CR list view displays:
- Columns: CR Number, Document Title, Layer, Failure Code, Status (color-coded badge), Assigned To, Due Date, Days Open
- Summary bar: total CRs, open count, overdue count
- Filter by: status, responsible_role
- Sort by: due date (default), status

**Step 2:** Click the draft CR (status = `OPEN`).

*System response:* Correction Request form opens with:
- **Auto-populated fields (read-only):**
  - CR Number (e.g., AM-CR-2026-00001)
  - Order Reference, MRB Number, PO Number, Customer
  - Document Reference, Document Type, Document Title, MRB Section
  - Validation Reference, Validation Layer
  - Created By, Created At

- **Fields requiring QA input (editable):**

**Step 3:** Complete the following fields:

| Field | Format | Notes |
|-------|--------|-------|
| **Failure Code** (R) | ENUM dropdown | Select: `MISSING` (document not provided), `FORMAT_ERROR` (wrong format/type), `INCOMPLETE` (missing required content), `NON_COMPLIANT` (values outside limits), `TRACEABILITY_BREAK` (identifier mismatch) |
| **Specific Finding** (R) | Text, max 3000 chars | Describe exactly what failed. Be specific. E.g., "Material certificate does not include impact test results at -46°C as required by NORSOK M-650." |
| **Required Action** (R) | Text, max 2000 chars | What must be done. E.g., "Request updated certificate from supplier including impact test data per ASTM A370." |
| **Responsible Party** (R) | User dropdown | Select the person responsible for resolving this CR. Filtered by role. |
| **Responsible Role** (R) | ENUM dropdown | Auto-suggested from document data_source: SUPPLIER → PURCHASING, CNC_INLINE → PRODUCTION, INSPECTION → QA_ENGINEER, etc. Override if needed. |
| **Due Date** (R) | Date picker | Deadline for resolution. Must be today or later (VR-010-01-005). |

**Step 4:** Click **"Save"** to confirm the CR.

*System response:* CR saved with status = `OPEN`. Assigned person receives notification.

#### Part B: Tracking CR Progress

**Step 5:** As work progresses on the correction, update the CR status:

| Status Transition | When | Fields Required |
|-------------------|------|----------------|
| `OPEN` → `IN_PROGRESS` | Responsible party has begun working on the correction | None additional |
| `IN_PROGRESS` → `RESOLVED` | Corrected document available | Resolution Description (R), Corrected Document URI (R — upload the new document) |
| `IN_PROGRESS` → `ESCALATED` | Issue needs Quality Manager decision | Escalated To (R — select QM), Escalation Reason (R) |
| `IN_PROGRESS` → `WAIVED` | Customer approves waiving the requirement | Waiver Reference (R), Waiver Approved By (R), Waiver Reason (R) — requires QM role |
| `ESCALATED` → `RESOLVED` or `WAIVED` | QM makes decision | Same as above |

**Status progression rules (VR-010-01-006):**
- Status can only progress forward. No regression from IN_PROGRESS to OPEN.
- Only QA_ENGINEER or QUALITY_MANAGER can change status (VR-010-01-007).

**Step 6:** To resolve a CR:

1. Click **"Resolve"** button on the CR form.
2. Enter **Resolution Description** — what was done to fix the issue.
3. Upload the **corrected document** — the replacement file.
4. Click **"Submit Resolution"**.

*System response:*
- CR status → `RESOLVED`
- Resolved By and Resolved At auto-populated
- **Corrected document automatically submitted for re-validation** (L1–L3 re-run)
- If re-validation PASS: document status → VALIDATED, MRB Index updates
- If re-validation FAIL: new CR auto-created for the new failure

**Step 7:** To waive a CR (requires QM role):

1. Click **"Waive"** button on the CR form.
2. Enter **Waiver Reference** — customer's approval document/email reference number.
3. Enter **Waiver Approved By** — name of customer contact who approved the waiver.
4. Enter **Waiver Reason** — justification for waiving the requirement.
5. Click **"Submit Waiver"**.

*System response:*
- CR status → `WAIVED`
- Document status in MRB Index → `WAIVED`
- No re-validation needed
- Waiver recorded in audit trail

**Step 8:** To escalate a CR:

1. Click **"Escalate"** button on the CR form.
2. Select **Escalated To** — the Quality Manager.
3. Enter **Escalation Reason** — why QM decision is needed.
4. Click **"Submit Escalation"**.

*System response:*
- CR status → `ESCALATED`
- Quality Manager receives notification
- CR appears in QM's pending decisions queue

#### Expected Result

- Correction Request fully documented with failure details and required action.
- Responsible party assigned and notified.
- CR tracked through lifecycle until resolved or waived.
- On resolution: corrected document re-validated automatically.
- Unresolved CRs are visible in the CR list and block CoC generation (Phase 0.5+).

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "Due date cannot be in the past" | Date entered is before today | Select today or a future date. |
| "Resolution description required" | Attempting to resolve without explanation | Enter what was done to correct the issue. |
| "Corrected document required" | Attempting to resolve without uploading replacement | Upload the corrected document (unless failure_code = TRACEABILITY_BREAK). |
| "Waiver requires all three fields" | Missing waiver reference, approver, or reason | All three waiver fields are mandatory. Get customer approval documentation first. |
| "Only QA Engineer or QM can change status" | Logged in with wrong role | Switch to QA Engineer or Quality Manager role. |
| Re-validation fails after resolution | Corrected document still has issues | A new CR is auto-created. Review the new failure and correct again. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **Before** | WI-009 | Validation failure during document upload triggers CR |
| **Before** | WI-007 | Gate rejection triggers CR for material certificate |
| **After** | WI-009 | Corrected document is re-uploaded and re-validated |

---

## 11. Customer Portal Work Instructions

---

### 11.1 WI-012: Viewing Order Status (Customer Portal)

| Field | Value |
|-------|-------|
| **WI Number** | WI-012 |
| **Role** | [CUSTOMER] |
| **Procedure** | AM-TS-001 §13 — Customer Portal |
| **Forms** | Portal screens (EPIC-09) |
| **Prerequisite State** | Customer portal account exists (created by Admin). At least one order exists for this customer. |
| **Result State** | No state change — read-only activity |
| **Estimated Time** | 2–5 minutes |

#### Purpose

Allow customer representatives to view the status of their orders and MRB documentation progress without contacting Aurelian Manufacturing directly.

#### Prerequisites

1. Your customer portal account has been created by an Aurelian administrator (customer accounts are not self-service in Phase 0).
2. You have your login credentials (email, password) and MFA authenticator app configured.
3. You have at least one order in the system.

#### Steps

**Step 1:** Navigate to the Aurelian Manufacturing customer portal URL (separate from the internal application).

*System response:* Login page displayed with email and password fields.

**Step 2:** Enter your **email** and **password**, then click **"Sign In"**.

*System response:* MFA challenge screen appears. "Enter the 6-digit code from your authenticator app."

**Step 3:** Open your authenticator app (Google Authenticator, Authy, etc.) and enter the **6-digit TOTP code**.

*System response:* On successful authentication:
- Dashboard loads showing your order list
- Session established: 1-hour access token, 7-day refresh token

*If error: "Invalid credentials"* — Verify email and password. After 5 failed attempts, the account is locked and requires an email reset.

*If error: "Invalid MFA code"* — Verify the code hasn't expired (codes rotate every 30 seconds). Try the next code. Contact Aurelian admin if MFA is not working.

**Step 4:** The **Order List** dashboard displays your orders:

| Column | Description |
|--------|-------------|
| PO Number | Your purchase order number |
| Order State | Color-coded status badge (NEW, COLLECTING, VALIDATING, etc.) |
| MRB Completion | Percentage bar showing documentation progress |
| Delivery Date | Expected delivery date |
| Last Updated | When the order was last modified |

*Note:* You can only see your own orders. RLS (Row Level Security) ensures you cannot access other customers' data.

**Step 5:** Click an order row to view the **MRB Status View**.

*System response:* Read-only MRB Index showing:
- Line items with document titles
- Document status per slot (PENDING/RECEIVED/VALIDATED — same color coding as internal view)
- Received and validated dates
- Completion summary card: X of Y documents validated, overall percentage
- Order state badge in header

**What you CAN see:**
- Document titles and required standards
- Document status (PENDING, RECEIVED, VALIDATED, WAIVED)
- Completion percentage
- Dates (received, validated)

**What you CANNOT see (Phase 0):**
- Actual document files (document download is Phase 1)
- Internal validation failure details
- Correction Request data
- QA Engineer names or internal notes

**Step 6:** To log out, click your profile icon (top right) → **"Sign Out"**.

#### Expected Result

- Successfully logged in and viewed order status.
- MRB completion percentage visible for each order.
- No ability to modify any data (read-only portal).

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "Account locked" | 5+ failed login attempts | Contact Aurelian admin to reset your account via email. |
| "No orders found" | No orders associated with your customer account | Contact your Aurelian commercial representative to verify order status. |
| "Session expired" | Access token expired (1-hour limit) | Re-authenticate. The page will redirect to login automatically. |
| Cannot see recently placed order | Order not yet registered in system | New orders appear after the admin registers the PO (WI-001). |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| (Internal) | WI-001 | Admin registers POs that appear in the customer portal |
| (Internal) | WI-009 | Document uploads update the MRB status visible in the portal |

---

## 12. Developer / Testing Work Instructions

---

### 12.1 WI-013: Using the Seed Data Tool

| Field | Value |
|-------|-------|
| **WI Number** | WI-013 |
| **Role** | [DEV] or [QA] |
| **Procedure** | AM-TS-001 §10.4, §16 — Seed Data and Phase Mapping |
| **Forms** | CLI tool (no UI form) |
| **Prerequisite State** | Application running locally or on staging. Database initialized with schemas (EPIC-01, EPIC-02). |
| **Result State** | Database populated with realistic test data. All `is_seed_data = true`. |
| **Estimated Time** | 1–3 minutes per command |

#### Purpose

Generate realistic test data for development and testing. The seed data tool creates customers, suppliers, orders, material receipts, certificates, SDRL data, MRB structures, and validation results — enabling the QA team to test the full pipeline without real customer data.

#### Prerequisites

1. The application is running (local `docker-compose up` or staging environment).
2. Database schemas are created (EPIC-01 and EPIC-02 migrations have run).
3. You have CLI access to the application server (terminal for local, SSH for staging).

#### Steps

**Step 1:** Open a terminal in the application root directory.

**Step 2:** Choose the seed command based on what data you need:

| Command | What it Creates | Orders | Use When |
|---------|----------------|--------|----------|
| `mrb-seed full-lifecycle` | Complete O&G order lifecycle: customer, supplier, PO, SDRL, MRB, receipts, gate reviews, documents, validations, 1 CR | 1 order (all stages) | First-time setup, full pipeline testing |
| `mrb-seed oilgas-norsok` | 3 O&G orders at different stages: COLLECTING (partial), VALIDATING (mixed results), MRB_INITIALIZED (empty) | 3 orders | Testing NORSOK requirements, multiple-order views |
| `mrb-seed defence-aqap` | 1 Defence order: 8-section MRB, AQAP references, FAIR requirement, SDRL-DEF-001 template | 1 order | Defence pipeline testing |
| `mrb-seed error-scenarios` | Edge cases: borderline values, wrong cert type, integrity red flags, missing tests, traceability breaks | 5 separate orders | Validation and error handling testing |
| `mrb-seed reset` | Removes all seed data (where `is_seed_data = true`). Non-seed data unaffected. | — | Clean slate before re-seeding |

**Step 3:** Run the chosen command:

```
npx mrb-seed full-lifecycle
```

*System response:*
- Progress output showing each entity being created
- Summary: "Created 1 customer, 1 supplier, 1 PO, 3 line items, 1 SDRL (39 line items), 1 MRB (7 sections), 3 material receipts, 3 gate reviews (2 RELEASED, 1 REJECTED), documents uploaded, L1–L3 validation results, 1 correction request. All tagged with is_seed_data = true."
- Execution time

*If error: "Database connection failed"* — Verify the application is running and database is accessible. Check `.env` for correct database URL.

*If error: "Schema not found"* — Run database migrations first: `npx supabase db push` or equivalent migration command.

**Step 4:** Verify seed data by logging into the application:

- Navigate to **Purchase Orders** — should see seeded POs
- Navigate to **Orders** — should see orders at various states
- Navigate to **Material Gate Queue** — should see pending receipts (if any)
- Navigate to **MRB Index** — should see document slots with various statuses

**Step 5:** To reset and re-seed (idempotent):

```
npx mrb-seed reset && npx mrb-seed full-lifecycle
```

*System response:* Previous seed data cleared. Fresh seed data created. Result is identical to running `full-lifecycle` on an empty database.

**Step 6:** To add additional scenarios without resetting:

```
npx mrb-seed oilgas-norsok
npx mrb-seed error-scenarios
```

*System response:* Additional orders created alongside existing seed data. All new records tagged with `is_seed_data = true`.

#### Expected Result

- Database populated with realistic test data.
- QA Engineer can log in and see orders, receipts, MRB documents, and validation results.
- All seed records have `is_seed_data = true` for easy identification and cleanup.
- Real (non-seed) data is never affected by seed operations.

#### Common Errors and Resolution

| Error | Cause | Resolution |
|-------|-------|-----------|
| "Database connection failed" | App not running or wrong DB URL | Start the application (`docker-compose up`) and verify `.env` configuration. |
| "Schema not found: erp" | Database migrations haven't run | Run migrations: `npx supabase db push`. |
| "Unique constraint violation" | Seed data already exists from a previous run | Run `mrb-seed reset` first, then re-seed. |
| Seed data missing in UI | Logged in with wrong role | Log in as QA Engineer or Admin. Customer role can only see their own orders. |
| "Permission denied" | RLS blocking seed data operations | Seed tool runs with service_role key (bypasses RLS). Verify the SUPABASE_SERVICE_ROLE_KEY is set in `.env`. |

#### Related Work Instructions

| Direction | WI | Relationship |
|-----------|-----|-------------|
| **After** | All WIs | Seed data provides test scenarios for practicing all other work instructions |

---

## 13. Quick Reference Cards

The following condensed summaries cover the 7 critical (★) work instructions. Print these for use at the workstation or keep them open as a reference tab.

---

### QRC-004: SDRL Upload (WI-004)

**Role:** QA Engineer | **Time:** 5–10 min | **State:** `NEW` → `SDRL_RECEIVED`

1. Open PO → click "Process SDRL"
2. Drag SDRL Excel file (.xlsx / .csv) onto upload dropzone
3. Wait for parser to complete
4. Review parse summary — check for errors (red) and warnings (amber)
5. If parse errors → fix file and re-upload
6. Proceed to **WI-006** to review and confirm

**Key validation:** VR-009-01-007 — order must be NEW or SDRL_RECEIVED

---

### QRC-005: SDRL Manual Entry (WI-005)

**Role:** QA Engineer | **Time:** 15–30 min | **State:** `NEW` → `SDRL_RECEIVED`

1. Open PO → click "Process SDRL" → click "Manual Entry"
2. Select template: SDRL-OG-001 (O&G, 39 items) or SDRL-DEF-001 (Defence, 31 items)
3. Compare template vs customer SDRL document
4. Modify, add, or uncheck items as needed
5. Ensure ≥ 1 CRITICAL item exists
6. Proceed to **WI-006** to review and confirm

**Key rule:** At least one CRITICAL line item required (VR-009-01-003)

---

### QRC-006: SDRL Review & Confirm (WI-006)

**Role:** QA Engineer | **Time:** 5–10 min | **State:** `SDRL_RECEIVED` → `MRB_INITIALIZED`

1. Review stats bar (total, CRITICAL, MAJOR, STANDARD counts)
2. Spot-check line items against customer SDRL
3. Verify section assignments (1–7 for O&G, 1–8 for Defence)
4. Click **"Confirm SDRL"** (Aurelian Red)
5. System creates MRB (AM-MRB-YYYY-NNNNN), generates MRB Index, transitions state
6. Verify MRB Index on redirect — correct sections, all PENDING

**Result:** MRB exists. Document collection and material gate can begin.

---

### QRC-007: Material Gate Review (WI-007)

**Role:** QA Engineer | **Time:** 15–25 min | **State:** gate_decision `PENDING` → `RELEASED` / `REJECTED` / `REVIEW`

1. Open Material Gate Queue → click pending receipt
2. Review top panel: order info, certificate viewer, Material Requirement Profile
3. **Check 1 — Cert Type:** Select actual type. System compares to required. (3.2 > 3.1 > 2.2 > 2.1)
4. **Check 2 — Chemical:** Enter actual % per element from certificate. Watch for BORDERLINE (amber, 5% of limit).
5. **Check 3 — Mechanical:** Enter actual values per property from certificate.
6. **Check 4 — Supplementary:** Mark tests as present/absent, pass/fail.
7. **Check 5 — Traceability:** Verify heat number, signature, date, supplier status, integrity.
8. **Decision:** RELEASED (all pass), REJECTED (any fail), or REVIEW (escalate to QM).
9. Enter reason (required) → Submit.

**Key rules:**
- Cannot RELEASE with any FAIL (VR-008-01-002)
- BORDERLINE is informational, does not block RELEASED
- REVIEW → goes to QM queue (WI-008)

---

### QRC-009: Document Upload (WI-009)

**Role:** QA Engineer | **Time:** 2–5 min per document | **State:** MRB Index slot `PENDING` → `VALIDATED` or `REJECTED`

1. Open MRB Index View
2. Click PENDING slot for the document to upload
3. Drag file onto upload dropzone
4. System runs L1 → L2 → L3 automatically
5. **All PASS:** green ✓, status → VALIDATED, MRB Index updates
6. **Any FAIL:** red ✗, status → REJECTED, Correction Request auto-created → go to WI-011
7. First upload transitions MRB Index: DRAFT → LIVE, order: MRB_INITIALIZED → COLLECTING

**Tip:** Upload in section order (Section 1 → Section 7) for cleaner tracking.

---

### QRC-010: Validation Review (WI-010)

**Role:** QA Engineer | **Time:** 5–10 min per order | **No state change**

1. Open MRB Index View — check summary row (total/validated/rejected/pending)
2. Click any status badge for detailed validation results
3. Review per-layer results (L1, L2, L3) with PASS/FAIL details
4. Filter by FAIL to see all outstanding issues
5. Each failure links to its Correction Request

**Focus on:** L3 failures (completeness) — most common issue is missing certificate fields.

---

### QRC-011: Correction Requests (WI-011)

**Role:** QA Engineer / Quality Manager | **Time:** 5 min initial + variable | **State:** CR `OPEN` → `RESOLVED` / `WAIVED`

1. Open CR list (from notification, MRB Index, or sidebar)
2. Complete draft CR: failure code, specific finding, required action, responsible party, due date
3. Save → status = OPEN, assigned person notified
4. Track progress: OPEN → IN_PROGRESS → ...
5. **To resolve:** upload corrected document + resolution description → system re-validates automatically
6. **To waive (QM only):** enter waiver reference, approver name, reason
7. **To escalate:** select QM, enter escalation reason

**Key rule:** Unresolved CRs block CoC generation (Phase 0.5+)

**Status flow:** OPEN → IN_PROGRESS → RESOLVED / ESCALATED / WAIVED (no backwards)

---

## 14. References

| VDR Ref | Document |
|---------|----------|
| — | AM-MVP-001 — MVP Scope Definition (master document) |
| — | AM-FM-001 — Form Template Specifications (master document) |
| — | AM-TS-001 — IT/System Technical Specification (master document) |
| — | AM-CT-001 — Customer-Facing Templates (master document) |
| — | AM-IF-001 — ERP ↔ MRB Builder Interface Specification (master document) |
| — | PR-008 — Incoming Material Review and Release |
| — | PR-009 — SDRL Processing and MRB Management |
| — | PR-010 — Document Validation and Verification |
| — | QM-001 — Quality Manual — Rev 2 Addendum |

---

*End of AM-WI-001 — Work Instructions*
*13 work instructions covering Phase 0 (Q2–Q4 2026)*
*7 Quick Reference Cards for critical workflows*
*Document revision: 1.0 — 21 February 2026*