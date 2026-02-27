# MVP SCOPE DEFINITION — DIGITAL MRB BUILDER PHASE 0

| Field | Value |
|-------|-------|
| **Document No.** | AM-MVP-001 |
| **Revision** | 1.1 |
| **Effective Date** | 2026-02-22 |
| **Approved By** | Technical Lead / Quality Manager |
| **Classification** | Internal — Engineering |
| **Status** | Draft — Post Founding Team Review (Tore) |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-21 | Technical Lead | Initial release. 11 epics, 58 user stories and capability statements covering Phase 0 (Q2–Q4 2026). Derived from AM-TS-001 Rev 1.2, AM-FM-001, AM-CT-001, and PR-008–010. |
| **1.1** | **2026-02-22** | **Industry & Requirements Lead** | **Post founding team review (Tore). 3 findings implemented: §2.2 Industry Focus updated — Defence is commercial top priority, O&G remains Phase 0 test scenario. AI-assisted cert pre-review (LLM-based) moved from Phase 2+ to Phase 0.5 with auto-fill stub in Phase 0. System-wide gate decision terminology unified: APPROVED/REJECTED/CONDITIONAL_APPROVAL replaces RELEASED/REJECTED/REVIEW throughout all user stories.** |

---

## 1. Purpose

This document defines the complete scope of **Phase 0 — Simulation & Build** for the Digital MRB Builder. It translates the quality system specifications (AM-TS-001, AM-CT-001, AM-FM-001) and business procedures (PR-008 through PR-013) into implementable user stories, capability statements, and acceptance criteria.

It answers one question for the development team: **What exactly do we build in Phase 0?**

This document does NOT define HOW to build — that is covered by AM-TS-001 (architecture, data model, security). It does NOT define the business rules — those are in PR-008 through PR-013. It defines WHAT the user sees, WHAT the system does, and HOW we verify it works.

---

## 2. Scope

### 2.1 Phase 0 Objective

**Phase 0: Simulation & Build (Q2–Q4 2026)**

Build the core MRB engine using simulated data. Validate the complete order-to-MRB pipeline from purchase order receipt through SDRL parsing, material gate review, document collection, and L1–L3 validation. All testing uses seed data — no production customer data.

**Phase 0 is complete when:**

- An Oil & Gas order can be processed end-to-end from PO receipt through SDRL parsing, material gate review, document upload, and L1–L3 validation using the seed data tool
- The order state machine transitions correctly through all reachable Phase 0 states (NEW through VALIDATING)
- The customer portal allows a customer user to log in and view order status
- All data resides in AWS eu-north-1 with RLS policies enforced

### 2.2 Industry Focus

**Commercial priority:** Defence is the primary commercial market for Aurelian Manufacturing. Oil & Gas is a strong secondary market.

**Phase 0 technical priority:** Oil & Gas is the primary Phase 0 test scenario because realistic O&G data (SDRLs, EN 10204 certificates, NORSOK requirements) is available for simulation. Defence data is more restricted and will follow. Both sectors are technically prepared in parallel — the system architecture, SDRL templates, MRB structures, and seed data tools cover both industries equally.

| Priority | Industry | Phase 0 Coverage | Commercial Role |
|----------|----------|-----------------|-----------------|
| **Phase 0 Primary** | Oil & Gas | Full pipeline simulation. NORSOK/API requirements. 7-section MRB. ITP hold points. EN 10204 Type 3.1/3.2 certificates. Primary test scenario due to data availability. | Strong secondary market |
| **Phase 0 Secondary** | Defence | SDRL template built (SDRL-DEF-001). 8-section MRB structure defined. Seed data available (`mrb-seed defence-aqap`). Defence seed data (E04-C03) should be expanded for thorough Phase 0 testing. | **Commercial top priority** — first target customers |

### 2.3 Timeline

| Milestone | Target | Description |
|-----------|--------|-------------|
| Sprint 0 | Q2 2026, Week 1–2 | Infrastructure (EPIC-01) and Data Model (EPIC-02) |
| Sprint 1–2 | Q2 2026, Week 3–8 | ERP MVP (EPIC-03), Seed Data (EPIC-04), Object Storage (EPIC-08) |
| Sprint 3–5 | Q3 2026 | SDRL Parser (EPIC-05), Material Gate (EPIC-06), Validation Engine (EPIC-07) |
| Sprint 6–7 | Q3–Q4 2026 | Customer Portal (EPIC-09), Observability (EPIC-11), integration testing |
| Sprint 8 | Q4 2026 | End-to-end dry run with seed data. Phase 0 acceptance testing. |

---

## 3. References

| Document | Title | Relevance |
|----------|-------|-----------|
| AM-TS-001 | IT/System Technical Specification | Architecture, data model (36 entities), security, infrastructure, phase mapping |
| AM-CT-001 | Customer-Facing Templates | SDRL templates (O&G: 39 items, Defence: 31 items), MRB Index columns, Customer Requirement Profile |
| AM-FM-001 | Form Templates — Internal Quality Forms | 24 form specifications. Phase 0 critical: FM-008-01, FM-009-01, FM-009-04, FM-010-01 |
| AM-IF-001 | ERP ↔ MRB Builder Interface Specification | 20 module boundary interfaces. Phase 0: IF-001 through IF-010 |
| PR-008 | Incoming Material Review and Release | Material Gate 5-point check business rules |
| PR-009 | SDRL Processing and MRB Management | SDRL parsing, MRB Index lifecycle, 12-state order machine |
| PR-010 | Document Validation and Verification | 5-layer validation framework, correction request process |
| PR-011 | Certificate of Conformance | CoC generation rules — NOT in Phase 0 (Phase 0.5) |
| PR-012 | MRB Assembly and Release | MRB compilation rules — NOT in Phase 0 (Phase 0.5) |
| PR-013 | Document Archival and Retention | Archive rules — NOT in Phase 0 (Phase 0.5) |
| QM-001 | Quality Manual — Rev 2 Addendum | QMS framework, phased deployment table |

---

## 4. Definitions

| Term | Definition |
|------|-----------|
| **Epic** | A major functional area of the system. Each epic contains user stories (for UI workflows) or capability statements (for infrastructure/engine work). |
| **User Story** | A description of a feature from an actor's perspective: "As a [role], I want to [action], so that [benefit]." Used for epics with user-facing workflows. |
| **Capability Statement** | A description of what the system can do, without a specific user role. Used for infrastructure, data model, and engine epics where there is no direct user interaction. |
| **Acceptance Criteria** | Testable checklist items that define when a story/capability is complete. Pass/fail, not subjective. |
| **Phase 0** | Simulation & Build (Q2–Q4 2026). Seed data only. Oil & Gas primary. |
| **Phase 0.5** | Integration & Testing (Q1–Q2 2027). Real CNC data, end-to-end dry runs, UAT. |
| **Phase 1** | Production MVP (Q3 2027). First real customer orders processed. |
| **Seed Data** | Realistic but synthetic data generated by the seed data CLI tool. Tagged with `is_seed_data = true`. |
| **MRB** | Manufacturing Record Book — complete quality documentation package per order. |
| **SDRL** | Supplier Document Requirement List — customer-contractual document defining required MRB contents. |
| **Gate Review** | Material acceptance/rejection decision based on 5-point certificate check (PR-008). |
| **L1–L5** | Five validation layers: L1 Existence, L2 Format, L3 Completeness, L4 Compliance, L5 Traceability. Phase 0 implements L1–L3 only. |
| **ITP** | Inspection Test Plan — Oil & Gas specific. Defines Hold/Witness/Review/Monitor/Surveillance points. |
| **RLS** | Row Level Security — PostgreSQL feature enforcing tenant isolation at database level. |

---

## 5. Exclusions — What Is NOT In Phase 0

### 5.1 Explicitly Excluded Features

These features are **not built, not stubbed, and not implemented** in Phase 0:

| Feature | Reason | Planned Phase |
|---------|--------|--------------|
| **CoC generation and signing (PR-011)** | Requires all documents validated and signed-off. Phase 0 stops at validation. | Phase 0.5 |
| **MRB Assembly and release (PR-012)** | Requires CoC and 10-point quality check. Depends on PR-011. | Phase 0.5 |
| **Document Archival (PR-013)** | Requires completed MRB. No production records to archive in Phase 0. | Phase 0.5 |
| **L4 Compliance validation** | Numeric range checking, unit conversion, borderline detection via PL/pgSQL rules. Complex — requires real data to calibrate. | Phase 0.5 |
| **L5 Traceability validation** | Cross-document reference chain verification. Depends on L4 being operational. | Phase 0.5 |
| **Machine data integration (MQTT/OPC-UA)** | CNC machines arrive Q2 2027. No hardware to integrate with. | Phase 0.5 |
| **Electronic signatures (INTERNAL_PKI)** | Phase 0 uses MANUAL approval. PKI infrastructure built in Phase 0.5. | Phase 0.5 |
| **BankID integration** | Depends on INTERNAL_PKI being operational first. Norway-only. | Phase 2+ |
| **AI-assisted certificate pre-review (LLM-based)** | LLM-based document parsing: AI reads PDF certificate, extracts chemical/mechanical values, compares against Material Requirement Profile, generates pre-review report for QA Engineer confirmation. Phase 0 designs the manual flow with auto-fill stub for seamless AI integration. Customer requirements remain the authoritative source. | Phase 0.5 |
| **Customer SDRL submission via portal** | Portal is read-only in Phase 0. Customer upload in Phase 2. | Phase 2 |
| **Customer MRB download via portal** | No released MRBs to download in Phase 0. | Phase 1 |
| **ERP quoting module** | Not needed for Phase 0 pipeline (POs are seeded, not quoted). | Phase 1+ |
| **ERP scheduling/finance** | Not needed for Phase 0 pipeline. | Phase 2+ |
| **Real-time notifications** | No production workflow to notify about. | Phase 2 |
| **GraphQL API** | REST-first in Phase 0. GraphQL planned for customer portal Phase 2+. | Phase 2+ |

### 5.2 Features Present but Limited in Phase 0

| Feature | Phase 0 State | Full Implementation |
|---------|--------------|-------------------|
| **Order state machine** | All 12 states exist in DB. UI workflows reach NEW → VALIDATING only. States COC_PENDING through ARCHIVED are structurally present but not reachable via UI. | Phase 0.5–1 |
| **Defence SDRL processing** | Template built (SDRL-DEF-001, 8-section MRB). Seed data available. Not the primary test scenario. | Phase 0.5 |
| **ITP Tracker (FM-009-02)** | ITP requirement detected during SDRL parsing. Flag only — full ITP form not a Phase 0 critical form. | Phase 0.5 |
| **Customer portal** | Login + order list + MRB status view. No document download, no SDRL submission, no profile input. | Phase 1–2 |
| **Material Requirement Profile** | Basic CRUD for profiles. Full NORSOK MDS integration deferred. | Phase 1 |

---

## 6. Roles and Actors

### 6.1 Internal Roles

| Role | Description | Phase 0 Access |
|------|-------------|---------------|
| **QA Engineer** | Primary system user. Performs SDRL parsing, material gate reviews, document upload, validation review, correction request management. | Full access to MRB Builder module. Read access to ERP data via views. |
| **Quality Manager** | Reviews escalated gate decisions (QM override). Approves waivers. Signs CoCs (Phase 0.5+). | QA Engineer access plus QM override queue. |
| **Admin** | Manages customer/supplier master data. Manages Material Requirement Profiles. System configuration. | Full access to ERP module. Read access to MRB data. |
| **Production** | Views order status and material gate results. Provides process sheets and in-process records. | Read access to assigned orders. Document upload to assigned order MRB slots. |

### 6.2 External Actors

| Role | Description | Phase 0 Access |
|------|-------------|---------------|
| **Customer Portal User** | Customer representative viewing order status and MRB progress. | Read-only: order list + MRB status for own orders only (RLS-enforced). |

### 6.3 System Actors

| Actor | Description |
|-------|-------------|
| **Validation Engine** | Automated system that runs L1–L3 checks on document upload. Creates validation records. Triggers correction requests on failure. |
| **Seed Data CLI** | Command-line tool that generates realistic test data for all entities. Used for development and testing. |

---

## 7. Epic Breakdown

> **Format convention:**
> - Infrastructure/engine epics use **Capability Statements** (ID: `Exx-Cyy`)
> - Workflow epics use **User Stories** (ID: `Exx-USyy`)
> - All acceptance criteria are testable checklists referencing source specifications

---

### EPIC-01: Infrastructure & DevOps

**Type:** Capability Statements | **Source:** AM-TS-001 §6, §15 | **Sprint:** 0 | **Dependencies:** None (first epic)

| ID | Capability | Acceptance Criteria | Source |
|----|-----------|-------------------|--------|
| E01-C01 | **Self-hosted Supabase on AWS eu-north-1** | Supabase services running on AWS eu-north-1 (Stockholm): PostgreSQL 16+, GoTrue Auth, Storage (S3-backed), PostgREST, Realtime. HTTPS endpoint accessible. Health check returns 200. All data remains in EEA. | AM-TS-001 §6.1, §15.4 |
| E01-C02 | **Docker Compose local development** | Single `docker-compose up` starts complete local stack: Supabase (PostgreSQL, Auth, Storage, PostgREST), Next.js application, Grafana + Prometheus + Loki. Developer README documents setup in < 30 minutes from fresh clone. | AM-TS-001 §15.2 |
| E01-C03 | **CI/CD pipeline operational** | GitHub Actions pipeline with stages: lint (ESLint), type-check (TypeScript strict), unit tests (Vitest), contract tests (module boundary), SAST (CodeQL), Docker build, deploy to staging, E2E tests (Playwright), manual approval gate → production. All stages pass on green build. | AM-TS-001 §15.3 |
| E01-C04 | **Staging environment operational** | Staging mirrors production topology on AWS. Accessible to founding team via VPN or IP whitelist. Uses real AWS services (S3, RDS). Deployment via CI/CD (no manual deploys). | AM-TS-001 §15.1, §15.4 |
| E01-C05 | **Secret management via Supabase Vault** | All application secrets (database passwords, JWT signing key, API keys, S3 access keys) stored in Supabase Vault (`pgsodium`). No secrets in source code, environment files committed to git, or CI config. Vault-encrypted secrets accessible via `vault.decrypted_secrets` view. | AM-TS-001 §8.4, Decision R7 |

**Definition of Done:** A developer can clone the repo, run `docker-compose up`, access the local application at `localhost:3000`, and see the login screen. Staging deploys automatically on merge to `main`.

---

### EPIC-02: Data Model & Database

**Type:** Capability Statements | **Source:** AM-TS-001 §7 | **Sprint:** 0 | **Dependencies:** EPIC-01

| ID | Capability | Acceptance Criteria | Source |
|----|-----------|-------------------|--------|
| E02-C01 | **ERP schema created (6 entities)** | Schema `erp` with tables: `customer`, `supplier`, `purchase_order`, `production_order`, `inventory_lot`, `quote`. All columns, types, and constraints per AM-TS-001 §7.2 (ERP Module Entities). Foreign keys enforced. JSONB columns for addresses, contacts, line_items, routing. | AM-TS-001 §7.2 |
| E02-C02 | **MRB core schema created (14 entities)** | Schema `mrb` with tables: `order`, `sdrl`, `sdrl_line_item`, `mrb`, `mrb_document`, `validation`, `material_receipt`, `material_requirement_profile`, `gate_review`, `coc`, `correction_request`, `archive_record`, `machine_event`, `audit_log`. All columns per AM-TS-001 §7.2. | AM-TS-001 §7.2 |
| E02-C03 | **MRB extended entities created (Phase 0 subset)** | Tables needed for Phase 0 forms: `physical_inspection` (FM-008-02 stub), `material_traceability` + `material_traceability_detail` (FM-008-03 stub). Remaining 13 extended entities (AM-TS-001 §7.2 Rev 1.2) created as empty tables with correct schemas — populated in Phase 0.5. | AM-TS-001 §7.2, AM-FM-001 §14 |
| E02-C04 | **29 ENUM types created** | All PostgreSQL ENUM types from AM-TS-001 §7.5 created: `industry_class`, `order_state`, `cert_type`, `gate_decision` (APPROVED/REJECTED/CONDITIONAL_APPROVAL), `gate_check_result` (PASS/FAIL/CONDITIONAL/BORDERLINE/N_A), `required_format`, `review_code`, `criticality`, `data_source`, `submission_timing`, `validation_status`, `validation_layer`, `validation_result`, `failure_code`, `cr_status`, `responsible_role`, `signature_method`, `coc_status`, `authority_level`, `archive_tier`, `disposition_method`, `integrity_check_result`, `delivery_method`, `release_type`, `pmi_method`, `itp_point_type` (incl. MONITOR), `sdrl_parse_method`, `mrb_index_state`, `document_review_response` (new). | AM-TS-001 §7.5, AM-FM-001 §6 |
| E02-C05 | **Order state machine enforced at DB level** | 12-state machine (NEW → SDRL_RECEIVED → SDRL_PARSED → MRB_INITIALIZED → COLLECTING → VALIDATING → COC_PENDING → COC_SIGNED → MRB_ASSEMBLY → MRB_RELEASED → SHIPPED → ARCHIVED). CHECK constraint or trigger blocks invalid transitions. Each transition inserts a row in `audit_log` with previous_state, new_state, user_id, timestamp. | AM-TS-001 §7.3, PR-009 §6.8 |
| E02-C06 | **MRB document state machine enforced** | Document status progression: PENDING → RECEIVED → VALIDATING → VALIDATED → INCLUDED_IN_MRB. Alternative paths: → REJECTED → CORRECTED → RECEIVED (re-submit); → WAIVED; → NOT_APPLICABLE. Regression blocked except via defined paths. | AM-TS-001 §7.4 |
| E02-C07 | **RLS policies for 4 roles** | Policies created for: `qa_engineer` (read all, write assigned orders), `quality_manager` (read/write all MRB data), `customer` (read own orders only — customer_id match), `admin` (full ERP access, read MRB). Cross-tenant access test: customer A cannot see customer B's orders (verified by test). | AM-TS-001 §8.3, §8.6 |
| E02-C08 | **Cross-schema views for module boundaries** | ERP reads MRB order status via `erp.v_order_status` view. MRB reads customer/supplier data via `mrb.v_customer`, `mrb.v_supplier` views. No direct cross-schema table access. Views match AM-IF-001 interface contracts IF-001 through IF-010. | AM-TS-001 §5, AM-IF-001 |
| E02-C09 | **Immutable audit_log table** | `mrb.audit_log` table with NO UPDATE, NO DELETE permissions for any role including `admin`. Append-only. Columns: log_id (UUID), user_id, action, entity_type, entity_id, details (JSONB), ip_address, timestamp. Retention: lifetime of associated records. | AM-TS-001 §8.5 |

**Definition of Done:** Database migrations run successfully. `psql` queries confirm all 36 tables exist with correct columns. RLS test script demonstrates cross-tenant isolation. State machine trigger blocks an invalid transition (e.g., NEW → VALIDATING) and raises an error.

---

### EPIC-03: ERP Module MVP

**Type:** User Stories | **Source:** AM-TS-001 §10.3–10.4, AM-IF-001 | **Sprint:** 1–2 | **Dependencies:** EPIC-01, EPIC-02

#### User Stories

| ID | As a... | I want to... | So that... |
|----|---------|-------------|-----------|
| E03-US01 | Admin | create and manage customer records | I can associate orders with customers |
| E03-US02 | Admin | create and manage supplier records | I can track approved suppliers and their certification status |
| E03-US03 | QA Engineer | create and view Purchase Orders | I can track incoming customer orders and initiate the MRB lifecycle |
| E03-US04 | QA Engineer | record a material receipt against an order | I can trigger the material gate review process |
| E03-US05 | Admin | manage Material Requirement Profiles per customer | material gate checks have customer-specific criteria to compare against |

#### Acceptance Criteria

**E03-US01 — Customer Management:**

- [ ] Customer list view: table with columns Name, Org Number, Industry, Contact Count, Actions
- [ ] Create customer form: name (required), org_number (required, unique), industry (ENUM dropdown), payment_terms
- [ ] Contacts sub-form: JSONB array — add/remove rows for name, email, phone, role
- [ ] Addresses sub-form: JSONB array — add/remove rows for street, city, postal_code, country
- [ ] Search/filter by name, org_number, industry
- [ ] Edit existing customer — all fields editable
- [ ] Delete blocked if customer has associated orders

**E03-US02 — Supplier Management:**

- [ ] Supplier list view: table with columns Name, Org Number, Approved Status, Cert Status, Actions
- [ ] Create supplier form: name (required), org_number (required, unique), approved_status (ENUM dropdown: APPROVED/CONDITIONAL/REJECTED), cert_status (ENUM dropdown: ISO9001/NADCAP/ISO17025/OTHER)
- [ ] Approved materials sub-form: JSONB array of material grade strings
- [ ] Contacts sub-form: JSONB array — same structure as customer contacts
- [ ] Delete blocked if supplier has associated material receipts

**E03-US03 — Purchase Order Management:**

- [ ] PO list view: table with columns PO Number, Customer (name), Received Date, Delivery Date, Order State, Actions
- [ ] Create PO form: po_number (required, unique per customer), customer_id (FK lookup/dropdown), received_date, delivery_date, commercial_terms (JSONB)
- [ ] Line items sub-form: JSONB array — part_number, quantity, material_grade, drawing_rev per line
- [ ] On PO save: system automatically creates `mrb.order` record with state = NEW. Logged in audit_log.
- [ ] PO detail view shows linked order state and MRB progress

**E03-US04 — Material Receipt:**

- [ ] Create receipt: order_id (FK dropdown filtered to COLLECTING/MRB_INITIALIZED orders), material_grade (text), heat_number (text), supplier_id (FK dropdown filtered to APPROVED/CONDITIONAL), cert_uri (file upload → Supabase Storage)
- [ ] On receipt save: gate_decision defaults to PENDING. Material receipt appears in Material Gate queue (EPIC-06)
- [ ] Receipt list view per order: shows all receipts with gate_decision status
- [ ] Links to inventory_lot (optional, for traceability)

**E03-US05 — Material Requirement Profile:**

- [ ] Profile list view per customer: table with Material Grade, Cert Type Required, Actions
- [ ] Create/edit profile form per AM-FM-001 FM-008-04:
  - customer_id (FK), material_grade (text), cert_type_required (ENUM: EN_10204_2_1/2_2/3_1/3_2)
  - chemical_limits: JSONB — per-element min/max (C, Mn, Si, P, S, Cr, Ni, Mo, etc.)
  - mechanical_limits: JSONB — per-property min/max with unit (tensile_strength, yield_strength, elongation, hardness, impact_energy)
  - supplementary_tests: JSONB array of test requirement objects
- [ ] Profile lookup available from Material Gate form (EPIC-06) — auto-populated by customer + material_grade match

#### Screen Descriptions

**Customer List Screen:**
- Header: "Customers" (36pt Bold)
- Action bar: search input + industry filter dropdown + "+ New Customer" button (Aurelian Red)
- Table: standard Aurelian table style (dark header row #2B2B2B, alternating body rows #FFFFFF/#F5F5F5, horizontal borders only)
- Row click → Customer Detail

**Purchase Order Detail Screen:**
- Header card: PO Number (large), Customer name, Received/Delivery dates
- Line items table: part_number, quantity, material_grade, drawing_rev
- Linked order card: order state badge (color-coded), MRB progress percentage
- Material receipts table: heat_number, material_grade, supplier, gate_decision badge (APPROVED green, REJECTED red, CONDITIONAL_APPROVAL amber, PENDING gray)

### EPIC-04: Seed Data Tool

**Type:** Capability Statements | **Source:** AM-TS-001 §10.4, §16, Decision R3 | **Sprint:** 1–2 (built incrementally alongside EPIC-03) | **Dependencies:** EPIC-01, EPIC-02

| ID | Capability | Acceptance Criteria | Source |
|----|-----------|-------------------|--------|
| E04-C01 | **`mrb-seed full-lifecycle` command** | CLI command generates one complete O&G order lifecycle: 1 customer, 1 supplier, 1 PO with 3 line items, 1 SDRL (39 line items per SDRL-OG-001 template), MRB initialized with 7 sections, 3 material receipts with EN 10204 certificates (realistic chemical/mechanical data with min+max ranges), gate reviews (2 APPROVED, 1 REJECTED), documents uploaded to MRB slots, L1–L3 validation results, 1 correction request for the failed document. All order state transitions logged in audit_log. | AM-TS-001 §10.4, §16 |
| E04-C02 | **`mrb-seed oilgas-norsok` command** | Generates 3 O&G orders at different lifecycle stages: Order A at COLLECTING (partial documents), Order B at VALIDATING (all documents, mixed validation results), Order C at MRB_INITIALIZED (empty MRB, fresh SDRL). Includes realistic NORSOK requirements: EN 10204 Type 3.1 and 3.2 certificates with per-element chemical data (C, Mn, Si, P, S, Cr, Ni, Mo), mechanical properties (tensile, yield, elongation, hardness), ITP with 3 Hold points and 2 Witness points, PMI requirements per NORSOK M-650. | AM-TS-001 §16, AM-CT-001 §4.2, Decisions R2/R3 |
| E04-C03 | **`mrb-seed defence-aqap` command** | Generates 1 Defence order: 8-section MRB structure, AQAP 2110 references, FAIR requirement (AS9102), SDRL-DEF-001 template (31 line items). Order at MRB_INITIALIZED stage. Defence-specific section headers per PR-009 §6.6 Defence table. | AM-CT-001 §5.2 |
| E04-C04 | **`mrb-seed error-scenarios` command** | Generates edge case data for testing: (a) certificate with BORDERLINE values — chemical elements within 5% of limits, (b) certificate with wrong cert type — 2.1 supplied when 3.1 required, (c) integrity red flags — identical chemical values across 3 different heat numbers, (d) missing supplementary test when profile requires it, (e) traceability break — heat number on cert does not match receipt. Each scenario creates a separate order with descriptive notes. | PR-008 §6.3, AM-FM-001 VR-008-01 rules |
| E04-C05 | **Idempotent and resettable** | Running any seed command on a populated database clears previous seed data (where `is_seed_data = true`) and re-seeds. Non-seed data is unaffected. Seed records are tagged with `is_seed_data = true` column on all seeded tables. `mrb-seed reset` command clears all seed data without re-seeding. | — |

**Definition of Done:** Running `mrb-seed full-lifecycle` populates all Phase 0 tables with realistic data. The QA Engineer can log into the application and see orders, receipts, MRB documents, and validation results in the UI. Running `mrb-seed reset && mrb-seed full-lifecycle` produces identical results (idempotent).

**Note:** Real SDRL data from Oil & Gas customers (per Decision R3) should be incorporated into the seed tool as soon as available, replacing synthetic SDRL templates with real customer requirements.

---

### EPIC-05: SDRL Parser (PR-009)

**Type:** User Stories | **Source:** PR-009 §6.1–6.6, AM-FM-001 FM-009-01 + FM-009-04, AM-CT-001 §4 + §8 | **Sprint:** 3–4 | **Dependencies:** EPIC-01, EPIC-02, EPIC-03, EPIC-08

#### User Stories

| ID | As a... | I want to... | So that... |
|----|---------|-------------|-----------|
| E05-US01 | QA Engineer | upload a customer SDRL file (Excel) | the system can extract document requirements automatically |
| E05-US02 | QA Engineer | manually enter SDRL line items | I can process SDRLs that are not in Excel format (PDF, email) |
| E05-US03 | QA Engineer | review and confirm parsed SDRL requirements | I can verify parser output before the system commits the MRB structure |
| E05-US04 | QA Engineer | see the generated MRB Index after SDRL parsing | I can verify the MRB structure matches customer requirements |
| E05-US05 | QA Engineer | see industry-specific MRB section structure | Oil & Gas orders get 7 sections and Defence orders get 8 sections, each with correct headers |

#### Acceptance Criteria

**E05-US01 — SDRL Upload:**

- [ ] Upload button on order detail screen (visible when order state = NEW or SDRL_RECEIVED)
- [ ] Accepts .xlsx and .csv files
- [ ] Parser maps Excel columns per AM-CT-001 §8.2 column mapping specification
- [ ] Unknown columns flagged as warnings (not blocking)
- [ ] Uploaded file stored in Supabase Storage at `aurelian-mrb/{customer_id}/{order_id}/source/sdrl_original.*`
- [ ] On successful upload: order state transitions to SDRL_RECEIVED. Logged in audit_log.
- [ ] Parse errors displayed inline with row/column reference

**E05-US02 — Manual SDRL Entry:**

- [ ] Manual entry form accessible from order detail screen
- [ ] Industry template selector: SDRL-OG-001 (Oil & Gas, 39 default items) or SDRL-DEF-001 (Defence, 31 default items) per AM-CT-001 §4.2/§5.2
- [ ] Selecting a template pre-populates default line items — QA Engineer can add, modify, remove rows
- [ ] All line item fields per FM-009-01 fields 14–28:
  - line_item_id (auto-incremented)
  - mrb_section (dropdown: 1–7 for O&G, 1–8 for Defence)
  - doc_title (text)
  - standard_ref (text, e.g., "EN 10204")
  - required_format (ENUM dropdown: PDF/PDF_A/NATIVE/SIGNED)
  - review_code (ENUM dropdown: FOR_INFO/FOR_REVIEW/FOR_APPROVAL)
  - criticality (ENUM dropdown: CRITICAL/MAJOR/STANDARD)
  - data_source (ENUM dropdown: CNC_INLINE/METROLOGY/INSPECTION/SUPPLIER/SPECIAL_PROCESS/INTERNAL_QA/CUSTOMER)
  - is_required (checkbox, default true)
  - submission_timing (ENUM dropdown: WITH_SHIPMENT/BEFORE_SHIPMENT/AT_MILESTONE/ON_REQUEST)
  - notes (optional textarea)
- [ ] parse_method set to MANUAL

**E05-US03 — SDRL Review and Confirmation:**

- [ ] Review screen shows: Order header card (FM-009-01 fields 1–13: order_id, po_number, customer, industry, sdrl_id, template_used, total_line_items, critical_count, major_count, standard_count, parse_method, parsed_by, parsed_at)
- [ ] Line items table: all columns from fields 14–28 — sortable, editable inline
- [ ] Auto-populated fields (from order/customer) are pre-filled but editable
- [ ] "Confirm and Parse" button: validates all line items, then commits SDRL to database
- [ ] On confirmation: order state transitions SDRL_RECEIVED → SDRL_PARSED. Logged in audit_log.

**E05-US04 — MRB Index Generation:**

- [ ] After SDRL confirmation: MRB record created with auto-generated mrb_number (format: AM-MRB-YYYY-NNNNN)
- [ ] MRB Index generated as database view (join of `sdrl_line_item` + `mrb_document` + `validation`) per FM-009-04 specification
- [ ] Index columns match AM-CT-001 §6.2: Line#, Section, Document Title, Standard Ref, Required Format, Review Code, Criticality, Data Source, Status, Received Date, Validated Date, Document Ref, Remarks
- [ ] All document statuses = PENDING
- [ ] MRB Index state = DRAFT
- [ ] Order state transitions SDRL_PARSED → MRB_INITIALIZED. Logged in audit_log.
- [ ] MRB Index is visible immediately from order detail screen

**E05-US05 — Industry-Specific Sections:**

- [ ] Oil & Gas MRB: 7 sections per PR-009 §6.6:
  1. Contract & Order Documentation
  2. Quality Plan / ITP
  3. Material Certificates
  4. Manufacturing Records
  5. Testing and Inspection
  6. Compliance Documentation
  7. Preservation and Shipping
- [ ] Defence MRB: 8 sections per PR-009 §6.6:
  1. Contract & Regulatory Documentation
  2. First Article Inspection
  3. Material Certificates
  4. Process Documentation
  5. Inspection & Test Results
  6. Quality Conformance
  7. Configuration Management
  8. Packaging, Handling, Shipping
- [ ] Section headers displayed in MRB Index view as group dividers
- [ ] Line items correctly grouped under their assigned section

#### Validation Rules (from AM-FM-001 FM-009-01)

| Rule ID | Description |
|---------|-------------|
| VR-009-01-001 | No duplicate line_item_id within same SDRL |
| VR-009-01-002 | mrb_section must be in range 1–7 (O&G) or 1–8 (Defence) |
| VR-009-01-003 | At least one CRITICAL line item required per SDRL |
| VR-009-01-004 | At least one line item required (SDRL cannot be empty) |
| VR-009-01-005 | Unknown doc_title values flagged as warning (not blocking) |
| VR-009-01-006 | ITP-related line items detected → flag for ITP Tracker requirement (Phase 0: flag only) |
| VR-009-01-007 | Order must be in state NEW or SDRL_RECEIVED for SDRL entry |

#### Screen Descriptions

**SDRL Upload Screen:**
- Header: "SDRL Processing" (36pt Bold) with order context card (PO number, customer, industry badge)
- Two-column layout: Left — file upload dropzone (drag-and-drop or click). Right — manual entry button + template selector dropdown
- Upload progress bar and parse status messages
- Error panel: shows parse errors with row/column references

**SDRL Review Screen:**
- Header card: Order info (PO number, customer, industry) + SDRL metadata (template used, total items, parse method)
- Stats bar: total line items, CRITICAL count (red badge), MAJOR count (amber badge), STANDARD count (gray badge)
- Full-width line item table: all columns, inline editable, sortable by section/criticality
- Action bar: "Add Row" button, "Confirm SDRL" button (Aurelian Red), "Cancel" button

**MRB Index View (FM-009-04):**
- Header card: MRB number (AM-MRB-YYYY-NNNNN), order info, MRB state badge (DRAFT/LIVE/FINAL), completion percentage
- Full-width table with columns A–N per AM-CT-001 §6.2
- Status column color-coded: PENDING (gray #6B6B6B), RECEIVED (steel blue #8EAEC5), VALIDATING (amber #C47F17), VALIDATED (green #1C6E3D), REJECTED (red #F50537), WAIVED (medium gray), NOT_APPLICABLE (light gray)
- Section dividers: dark row (#2B2B2B, white text) for each MRB section header
- Footer: summary row showing total/received/validated/rejected/pending counts

### EPIC-06: Material Gate (PR-008)

**Type:** User Stories | **Source:** PR-008 §6.1–6.6, AM-FM-001 FM-008-01 (33 fields, 11 validation rules) | **Sprint:** 3–5 | **Dependencies:** EPIC-01, EPIC-02, EPIC-03, EPIC-08

#### User Stories

| ID | As a... | I want to... | So that... |
|----|---------|-------------|-----------|
| E06-US01 | QA Engineer | open a Material Gate review for a pending receipt | I can evaluate the material certificate against customer requirements |
| E06-US02 | QA Engineer | perform the 5-point certificate check | I can systematically evaluate material conformance |
| E06-US03 | QA Engineer | see borderline flags automatically calculated | I do not miss values near specification limits |
| E06-US04 | QA Engineer | make a gate decision (APPROVED / REJECTED / CONDITIONAL_APPROVAL) | the material can proceed to or be blocked from production |
| E06-US05 | Quality Manager | review and resolve an escalated gate decision | materials flagged for QM override get a final decision |
| E06-US06 | QA Engineer | record integrity red flags on suspicious certificates | patterns like identical values across heat numbers are documented |

#### Acceptance Criteria

**E06-US01 — Open Gate Review:**

- [ ] Material Gate queue: list of material receipts with gate_decision = PENDING, grouped by order. Decision statuses: APPROVED (green), REJECTED (red), CONDITIONAL_APPROVAL (amber), PENDING (gray)
- [ ] Click receipt → opens FM-008-01 form with all 33 fields per AM-FM-001
- [ ] Auto-populated fields load from linked entities:
  - Fields 4–5 (order_id, po_number) from `mrb.order`
  - Fields 6–7 (customer, industry_class) from `erp.customer` via view
  - Field 8 (material_grade) from `mrb.material_receipt`
  - Field 12 (cert_type_required) from `mrb.material_requirement_profile` (lookup by customer + material_grade)
- [ ] Certificate viewer: inline PDF viewer for the uploaded certificate (cert_uri from material_receipt)
- [ ] Material Requirement Profile card: displays the applicable profile (chemical_limits, mechanical_limits, supplementary_tests) for reference during checks

**E06-US02 — 5-Point Certificate Check:**

Per PR-008 §6.3:

- [ ] **Check 1 — Certificate Type:** Dropdown for actual_cert_type received. System auto-compares against required cert_type per hierarchy (3.2 > 3.1 > 2.2 > 2.1). Result: PASS if actual ≥ required, FAIL if actual < required. Per VR-008-01-011.
- [ ] **Check 2 — Chemical Analysis:** Dynamic table — one row per element from profile's chemical_limits JSONB. Columns: Element, Min (from profile), Max (from profile), Actual (input), Result (auto-calculated PASS/FAIL/BORDERLINE). Auto-compare actual against min/max. Per PR-008 §6.3 Check 2.
- [ ] **Check 3 — Mechanical Properties:** Dynamic table — one row per property from profile's mechanical_limits JSONB. Columns: Property, Min, Max, Unit, Actual (input), Result (auto-calculated). Includes tensile strength, yield strength, elongation, hardness, impact energy (if required). Per PR-008 §6.3 Check 3.
- [ ] **Check 4 — Supplementary Tests:** Conditional — only displayed when profile has supplementary_tests entries. Checklist of required tests with present/absent toggle. Per PR-008 §6.3 Check 4.
- [ ] **Check 5 — Traceability & Integrity:** Checklist items per PR-008 §6.3 Check 5: heat number traceable, cert signature present, cert not expired, supplier on approved list, no integrity red flags. Overall result: PASS/FAIL/FLAG.

**E06-US03 — Borderline Flags:**

- [ ] After entering chemical/mechanical values, system auto-calculates borderline_flags (JSONB) per VR-008-01-010
- [ ] Borderline threshold: value within 5% of the specification limit
- [ ] Visual indicator: amber/yellow highlight on flagged values in the check table
- [ ] Borderline flags are informational — they do not block APPROVED decision but are recorded for audit trail
- [ ] Borderline_flags JSONB structure: `[{element: "C", actual: 0.048, limit: 0.050, margin_pct: 4.0}]`

**E06-US04 — Gate Decision:**

- [ ] Decision section enabled only after all 5 checks have a value (VR-008-01-001)
- [ ] APPROVED decision blocked when any check = FAIL (VR-008-01-002)
- [ ] Decision dropdown: APPROVED / REJECTED / CONDITIONAL_APPROVAL
- [ ] Decision reason: required text field for all decisions (VR-008-01-003)
- [ ] On APPROVED:
  - `material_receipt.gate_decision` = APPROVED
  - `gate_review` record created with decision, check_results (JSONB), reviewer_id, timestamp
  - MRB Index Section 3 document status updates (material cert document → RECEIVED)
  - Audit log entry
- [ ] On REJECTED:
  - `material_receipt.gate_decision` = REJECTED
  - System auto-creates draft Correction Request (FM-010-01) linked to the gate review
  - QA Engineer completes CR details (failure code, required action, responsible party)
- [ ] On CONDITIONAL_APPROVAL:
  - `material_receipt.gate_decision` = CONDITIONAL_APPROVAL
  - Material may proceed to production with documented conditions
  - System auto-creates Correction Request (FM-010-01) documenting the conditions to be resolved
  - Conditions tracked until closure — does not block production but requires follow-up
- [ ] QM Escalation (optional):
  - QA Engineer sets `gate_review.qm_override` = true to escalate to Quality Manager
  - Gate review appears in Quality Manager's pending review queue (E06-US05)
  - QA Engineer cannot proceed — awaits QM decision

**E06-US05 — QM Override:**

- [ ] Quality Manager sees "Pending QM Reviews" queue on their dashboard
- [ ] QM opens the gate review — sees all 5 check results, borderline flags, QA Engineer's notes
- [ ] QM can select APPROVED, REJECTED, or CONDITIONAL_APPROVAL (VR-008-01-008)
- [ ] QM decision recorded in fields 30–33: qm_decision, qm_decision_reason, qm_reviewer_id, qm_reviewed_at
- [ ] QM decision triggers same downstream effects as E06-US04 (APPROVED, REJECTED, or CONDITIONAL_APPROVAL path)

**E06-US06 — Integrity Red Flags:**

- [ ] Optional integrity_flags JSONB field on gate review form
- [ ] Free-form entry: flag description + severity (LOW/MEDIUM/HIGH)
- [ ] When Check 5 result = FLAG: physical_inspection_required auto-set to true (VR-008-01-009)
- [ ] Integrity flags are preserved in gate_review record for audit trail
- [ ] Example flags: "Identical chemical values across 3 heat numbers", "Certificate date pre-dates supplier approval date"

#### Screen Description

**Material Gate Form (FM-008-01):**
- Three-section layout with expandable panels:
  - **Top panel (read-only):** Receipt info card — order, PO, customer, material grade, heat number, supplier, cert type required. Certificate viewer button (opens inline PDF).
  - **Middle panel (interactive):** 5 tabbed check sections. Each tab shows the dynamic check table. Active tab highlighted in Aurelian Red. Completed checks show green checkmark on tab. Failed checks show red X.
    - Chemical check tab: element table with actual value inputs, auto-calculated results
    - Mechanical check tab: property table with actual value inputs, auto-calculated results
    - Borderline flags: amber highlight on values within 5% of limits
  - **Bottom panel:** Decision section. Decision dropdown + reason textarea + integrity flags (collapsible). Submit button (Aurelian Red). Disabled until all 5 checks completed.
  - **QM Override section:** Appears conditionally when qm_override = true. Shows QM decision dropdown, reason, and approve button.

---

### EPIC-07: Validation Engine L1–L3 (PR-010)

**Type:** Mixed (Capabilities + User Stories) | **Source:** PR-010 §6.1–6.4 + §6.12, AM-FM-001 FM-010-01 + FM-010-02 | **Sprint:** 4–5 | **Dependencies:** EPIC-01, EPIC-02, EPIC-05, EPIC-08

#### Capabilities (Validation Engine)

| ID | Capability | Acceptance Criteria | Source |
|----|-----------|-------------------|--------|
| E07-C01 | **L1 — Existence check** | For each `sdrl_line_item` where `is_required = true`, system checks whether a `mrb_document` has been uploaded to that slot. Missing documents: validation record created with layer = L1_EXISTENCE, result = FAIL, failure_code = MISSING. Present documents: result = PASS. | PR-010 §6.2 (L1) |
| E07-C02 | **L2 — Format check** | Uploaded document checked against `required_format` from SDRL line item. Checks: (a) MIME type matches expected type (PDF → application/pdf, etc.), (b) file is readable and not corrupted (not zero-byte, valid structure), (c) if required_format = PDF_A, PDF/A conformance validated. Failure: layer = L2_FORMAT, result = FAIL, failure_code = FORMAT_ERROR, details include specific format issue. | PR-010 §6.2 (L2) |
| E07-C03 | **L3 — Completeness check** | Document content checked against Document Type Registry validation schema (AM-TS-001 §11.1). For EN 10204 certificates: mandatory fields present (heat number, chemical composition table, mechanical properties table, authorized signature, test date). For dimensional reports: part number, drawing revision, measurement results, inspector. Failure: layer = L3_COMPLETENESS, result = FAIL, failure_code = INCOMPLETE, details list missing fields. | PR-010 §6.2 (L3), §6.4 |
| E07-C04 | **Automatic validation on document upload** | When a document is uploaded to an MRB slot via the document upload screen: L1, L2, L3 run in sequence. On first failure, validation halts at that layer and document status becomes REJECTED. On all-pass through L3, status becomes VALIDATED. Results stored in `mrb.validation` table with layer, result, and details (JSONB). Document's `validation_layer` field updated to highest passed layer. | PR-010 §6.1 |
| E07-C05 | **MRB Index real-time status update** | Validation results propagate to MRB Index view automatically. Status column, received_date, and validated_date update via database view recalculation. No manual refresh required. Completion percentage recalculates (validated / total required × 100). | AM-FM-001 FM-009-04 |

#### User Stories (Correction Requests — FM-010-01)

| ID | As a... | I want to... | So that... |
|----|---------|-------------|-----------|
| E07-US01 | QA Engineer | see auto-generated correction requests when validation fails | I can act on validation failures immediately |
| E07-US02 | QA Engineer | manage correction request lifecycle | I can track failures from detection through resolution |
| E07-US03 | QA Engineer | view all open correction requests for an order | I can see what is blocking MRB completion |

#### Acceptance Criteria

**E07-US01 — Auto-Generated Correction Request:**

- [ ] On validation FAIL (any layer): system auto-creates a draft CR with auto-populated fields per FM-010-01 fields 1–12:
  - cr_number: auto-generated (AM-CR-YYYY-NNNNN)
  - order_id, mrb_id, doc_id: from context
  - document_title, mrb_section: from SDRL line item
  - validation_layer: layer where failure occurred
  - validation_result: FAIL
  - validation_details: from validation record details JSONB
  - created_at, created_by: system timestamp and current user
- [ ] QA Engineer fills remaining fields 13–18:
  - failure_code (ENUM: MISSING/FORMAT_ERROR/INCOMPLETE/NON_COMPLIANT/TRACEABILITY_BREAK)
  - specific_finding (text — description of what is wrong)
  - required_action (text — what needs to be done)
  - responsible_party (text — who needs to act)
  - responsible_role (ENUM: QA_ENGINEER/PURCHASING/PRODUCTION/CUSTOMER/SUPPLIER)
  - due_date (date — deadline for resolution)
- [ ] CR saved with status = OPEN

**E07-US02 — Correction Request Lifecycle:**

- [ ] Status progression: OPEN → IN_PROGRESS → RESOLVED / ESCALATED / WAIVED
- [ ] Validation rules from AM-FM-001 VR-010-01:
  - VR-010-01-001: Status can only progress forward (no regression from IN_PROGRESS to OPEN)
  - VR-010-01-002: RESOLVED requires: corrected_doc_uri (new document uploaded), resolution_notes, resolved_by, resolved_at
  - VR-010-01-003: On RESOLVED — corrected document triggers re-validation (L1–L3 re-run automatically)
  - VR-010-01-004: WAIVED requires: waiver_reference, waiver_approver (must be Quality Manager role), waiver_reason
  - VR-010-01-005: ESCALATED requires: escalation_reason, escalated_to (user)
  - VR-010-01-006: Re-validation after correction: if PASS, CR status remains RESOLVED and document status → VALIDATED. If FAIL again, new CR auto-created.
  - VR-010-01-007: Only QA_ENGINEER or QUALITY_MANAGER can change CR status
  - VR-010-01-008: due_date cannot be in the past when setting
- [ ] All status changes logged in audit_log

**E07-US03 — Correction Request List View:**

- [ ] CR list view filtered by order (accessible from order detail and MRB Index)
- [ ] Table columns: CR Number, Document Title, Layer, Failure Code, Status (color-coded badge), Assigned To, Due Date, Days Open
- [ ] Sort by: due date (default), status, criticality
- [ ] Filter by: status (OPEN/IN_PROGRESS/RESOLVED/ESCALATED/WAIVED), responsible_role
- [ ] Summary bar: total CRs, open count, overdue count (past due_date and not RESOLVED/WAIVED)
- [ ] Click CR → opens CR detail form with all fields

#### Document Upload Screen (shared with EPIC-08)

- [ ] Accessible from MRB Index view — click on a PENDING document slot
- [ ] File upload dropzone: drag-and-drop or click to select
- [ ] On upload: file stored in Supabase Storage, SHA-256 checksum computed, L1–L3 validation runs automatically
- [ ] Validation progress indicator: shows L1 → L2 → L3 with pass/fail per layer
- [ ] On all-pass: document status → VALIDATED, green confirmation, MRB Index updates
- [ ] On fail: document status → REJECTED, red error panel with failure details, CR auto-created
- [ ] Multiple documents can be uploaded in sequence (batch upload for different MRB slots)

### EPIC-08: Object Storage & Document Management

**Type:** Capability Statements | **Source:** AM-TS-001 §6.5, §11, §14.2 | **Sprint:** 1–2 | **Dependencies:** EPIC-01, EPIC-02

| ID | Capability | Acceptance Criteria | Source |
|----|-----------|-------------------|--------|
| E08-C01 | **Supabase Storage bucket structure** | Bucket `aurelian-mrb` created in Supabase Storage (AWS S3 backend, eu-north-1). Path structure: `/{customer_id}/{order_id}/{stage}/` where stage = `source` (original uploads), `validated` (post-validation), `mrb` (assembled MRB), `coc` (CoC documents). | AM-TS-001 §14.2 |
| E08-C02 | **Document upload with SHA-256 checksum** | On file upload: file stored in Supabase Storage at correct path. SHA-256 checksum computed server-side and stored in `mrb_document.checksum_sha256`. Metadata stored in PostgreSQL: filename, MIME type, file size (bytes), upload timestamp, uploader user_id. `mrb_document.artifact_uri` set to Storage path. | AM-TS-001 §11 |
| E08-C03 | **RLS-based access control** | Storage RLS policies: customer role can only access files under their `customer_id` path. QA Engineer can access all files. Quality Manager can access all files. Admin can access ERP-related files. Production can access files for assigned orders. Cross-tenant access test: customer A cannot download files from customer B's path. | AM-TS-001 §8.3, §8.6 |
| E08-C04 | **Document immutability after validation** | Documents with `validation_status = VALIDATED` cannot be overwritten or deleted via application logic. Correction flow: new version uploaded as separate file, linked to original via `previous_doc_id`. Original preserved with status SUPERSEDED. Version history maintained in `mrb_document` table. | AM-TS-001 §11.3 |
| E08-C05 | **Inline document viewer** | PDF files viewable inline in the application via embedded PDF viewer component. Viewer accessible from: Material Gate form (certificate viewing), MRB Index (click document ref), Document upload confirmation screen. Non-PDF files: download link displayed instead of viewer. | — |

**Definition of Done:** A QA Engineer can upload a PDF to an MRB document slot, see the checksum in the document record, view the PDF inline, and confirm that a customer portal user cannot access another customer's documents.

---

### EPIC-09: Customer Portal MVP

**Type:** User Stories | **Source:** AM-TS-001 §13 | **Sprint:** 6–7 | **Dependencies:** EPIC-01, EPIC-02, EPIC-10

#### User Stories

| ID | As a... | I want to... | So that... |
|----|---------|-------------|-----------|
| E09-US01 | Customer Portal User | log in securely with email, password, and MFA | I can access my order information with confidence |
| E09-US02 | Customer Portal User | see a list of my orders | I know which orders are in progress and their status |
| E09-US03 | Customer Portal User | view MRB status for a specific order | I can track documentation progress without calling the manufacturer |

#### Acceptance Criteria

**E09-US01 — Secure Login:**

- [ ] Separate Next.js application instance from internal QA application (different deployment, shared Supabase backend)
- [ ] Login form: email + password + MFA (TOTP via authenticator app)
- [ ] MFA is mandatory — no bypass option
- [ ] Supabase Auth with `customer` role
- [ ] JWT: 1-hour access token, 7-day refresh token
- [ ] Rate limiting: 100 requests/minute per customer session
- [ ] Failed login attempts: lock account after 5 failures, require email reset
- [ ] All login events logged in audit_log (LOGIN_SUCCESS, LOGIN_FAIL, MFA_VERIFY)

**E09-US02 — Order List:**

- [ ] Dashboard showing customer's orders only (RLS-enforced — `customer_id` matches auth token)
- [ ] Table columns: PO Number, Order State (color-coded badge), MRB Completion (percentage bar), Delivery Date, Last Updated
- [ ] Sort by: delivery date (default), last updated, completion percentage
- [ ] No access to: internal notes, correction requests, validation details, QA Engineer assignments
- [ ] Click order → Order MRB Status view (E09-US03)

**E09-US03 — MRB Status View:**

- [ ] Read-only MRB Index view showing: line items, document status per slot, received/validated dates
- [ ] Status column: same color coding as internal MRB Index view (PENDING/RECEIVED/VALIDATED etc.)
- [ ] No access to: actual document files (Phase 1), internal validation failure details, correction request data, QA Engineer names
- [ ] Completion summary card: X of Y documents validated, overall percentage
- [ ] Order state badge displayed in header

**Explicitly NOT in Phase 0 Customer Portal:**

- No document download (Phase 1 — per AM-TS-001 §13.1)
- No SDRL submission (Phase 2 — per IF-017)
- No requirement profile input (Phase 2 — per IF-018)
- No real-time notifications (Phase 2)
- No self-service account creation (Admin creates customer portal accounts)

#### Screen Descriptions

**Customer Portal — Order List:**
- Clean, minimal design. Aurelian logo top-left. Customer name and logout button top-right.
- Table: standard Aurelian table style. Order state as colored badge. MRB completion as horizontal progress bar (Aurelian Red fill).
- Mobile-responsive: table collapses to card layout on small screens.

**Customer Portal — MRB Status:**
- Header: PO Number (large), order state badge, delivery date, completion percentage circle
- MRB Index table: read-only, section dividers, status badges
- No action buttons — purely informational view

---

### EPIC-10: Order State Machine

**Type:** Capability Statements | **Source:** AM-TS-001 §7.3, PR-009 §6.8 | **Sprint:** 0 (built with EPIC-02) + tested via EPIC-05/06/07 | **Dependencies:** EPIC-02

| ID | Capability | Acceptance Criteria | Source |
|----|-----------|-------------------|--------|
| E10-C01 | **12-state lifecycle enforced at DB level** | States: NEW, SDRL_RECEIVED, SDRL_PARSED, MRB_INITIALIZED, COLLECTING, VALIDATING, COC_PENDING, COC_SIGNED, MRB_ASSEMBLY, MRB_RELEASED, SHIPPED, ARCHIVED. Invalid transitions raise PostgreSQL error. Valid transitions defined as adjacency list in CHECK constraint or trigger function. | AM-TS-001 §7.3 |
| E10-C02 | **Phase 0 reachable states: NEW → VALIDATING** | Phase 0 UI workflows can transition orders through: NEW → SDRL_RECEIVED → SDRL_PARSED → MRB_INITIALIZED → COLLECTING → VALIDATING. States COC_PENDING through ARCHIVED exist in schema but are not reachable via Phase 0 UI (no CoC generation, no MRB assembly). Seed data tool (EPIC-04) can create orders in ALL 12 states for testing. | AM-TS-001 §16 |
| E10-C03 | **Every transition logged in audit_log** | Transition audit record includes: entity_type = 'order', entity_id = order_id, action = 'STATE_TRANSITION', details JSONB = {previous_state, new_state, trigger}, user_id, timestamp, ip_address. | AM-TS-001 §8.5 |
| E10-C04 | **MRB Index state syncs with order state** | MRB_INITIALIZED → MRB Index state = DRAFT. First document uploaded (any slot) → MRB Index state = LIVE, order enters COLLECTING. All documents VALIDATED and no open CRs → order can transition to VALIDATING → COC_PENDING (Phase 0.5). | AM-FM-001 FM-009-04 |
| E10-C05 | **Order state visible throughout application** | Order state displayed as badge/chip on: order list table, order detail page header, MRB Index header, Material Gate form header, Correction Request list header, Customer Portal order list. Color coding per state: NEW (gray), SDRL_RECEIVED–SDRL_PARSED (steel blue), MRB_INITIALIZED–COLLECTING (amber), VALIDATING (Aurelian Red), COC_PENDING onwards (green when applicable in Phase 0.5+). | — |

**Definition of Done:** Create an order via seed data. Verify the order progresses through NEW → SDRL_RECEIVED → SDRL_PARSED → MRB_INITIALIZED → COLLECTING → VALIDATING via the UI. Verify that attempting to skip a state (e.g., NEW → COLLECTING) raises an error. Verify that all transitions appear in the audit_log.

---

### EPIC-11: Observability & Monitoring

**Type:** Capability Statements | **Source:** AM-TS-001 §6.6, §16 | **Sprint:** 6–7 | **Dependencies:** EPIC-01

| ID | Capability | Acceptance Criteria | Source |
|----|-----------|-------------------|--------|
| E11-C01 | **Grafana + Prometheus + Loki deployed** | Docker containers running alongside application stack. Grafana accessible via browser at dedicated port. Prometheus scraping application metrics endpoint (/metrics). Loki ingesting structured application logs (JSON format). | AM-TS-001 §6.6 |
| E11-C02 | **System health dashboards** | Grafana dashboards: (a) **System Health** — database connection pool usage, API response time (p50/p95/p99), storage usage (GB), error rate (5xx/min). (b) **MRB Pipeline** — orders by state (bar chart), documents by validation status, open CRs count, avg time per validation layer. Basic alerts: database connection pool > 80%, error rate > 10/min, storage usage > 80% of quota. | AM-TS-001 §6.6, §16 |

**Definition of Done:** Grafana is accessible, dashboards show live metrics from the staging environment, and at least one alert fires correctly when simulated.

---

## 8. Cross-Epic Dependencies

### Dependency Diagram

```
EPIC-01 (Infrastructure)
   │
   ▼
EPIC-02 (Data Model + State Machine) ──────► EPIC-11 (Observability)
   │
   ├──────────┬──────────┬──────────┐
   ▼          ▼          ▼          ▼
EPIC-03    EPIC-08    EPIC-10    EPIC-04
(ERP MVP)  (Storage)  (SM test)  (Seed Data)
   │          │                     │
   ├──────────┤                     │
   ▼          ▼                     ▼
EPIC-05 (SDRL Parser) ◄────── seed data
   │
   ▼
EPIC-06 (Material Gate) ◄──── seed data
   │
   ▼
EPIC-07 (Validation Engine L1–L3)

EPIC-09 (Customer Portal) ← depends on EPIC-02, EPIC-10
```

### Recommended Sprint Sequence

| Sprint | Epics | Focus |
|--------|-------|-------|
| **Sprint 0** (Week 1–2) | EPIC-01, EPIC-02, EPIC-10 | Infrastructure, data model, state machine. Foundation for everything. |
| **Sprint 1** (Week 3–4) | EPIC-03 (start), EPIC-08, EPIC-04 (start) | ERP CRUD screens, object storage, seed data tool (basic). |
| **Sprint 2** (Week 5–6) | EPIC-03 (complete), EPIC-04 (complete) | ERP module done. Full seed data tool operational. |
| **Sprint 3** (Week 7–8) | EPIC-05 | SDRL Parser: upload, manual entry, review, MRB Index generation. |
| **Sprint 4** (Week 9–10) | EPIC-06 | Material Gate: 5-point check, gate decision, QM override. |
| **Sprint 5** (Week 11–12) | EPIC-07 | Validation Engine L1–L3, correction requests, document upload. |
| **Sprint 6** (Week 13–14) | EPIC-09, EPIC-11 | Customer Portal MVP, observability dashboards. |
| **Sprint 7** (Week 15–16) | Integration testing | End-to-end dry run with seed data. Fix integration issues. |
| **Sprint 8** (Week 17–18) | Acceptance testing | Phase 0 acceptance criteria verification. Documentation. |

---

## 9. Non-Functional Requirements (Phase 0)

| Category | Requirement | Verification | Source |
|----------|------------|-------------|--------|
| **Authentication** | MFA mandatory for all users (internal and portal). JWT: 1-hour access token, 7-day refresh. | Auth config test | AM-TS-001 §8.2 |
| **Authorization** | RLS policies enforced on all tables. Cross-tenant access blocked. | RLS test suite | AM-TS-001 §8.3 |
| **Audit** | Immutable audit_log. NO UPDATE/DELETE permissions. All state transitions, login events, and data access logged. | Audit log verification script | AM-TS-001 §8.5 |
| **Data sovereignty** | All data in AWS eu-north-1 (Stockholm). No data replication outside EEA. | Infrastructure config review | AM-TS-001 §6.1 |
| **Encryption in transit** | TLS 1.3 for all connections. HTTPS-only. No HTTP fallback. | SSL Labs test | AM-TS-001 §8.4 |
| **Encryption at rest** | AES-256 for S3 storage. PostgreSQL tablespace encryption. | AWS config review | AM-TS-001 §8.4 |
| **Document integrity** | SHA-256 checksums for all uploaded artifacts. Checksum stored in PostgreSQL. | Checksum verification test | AM-TS-001 §11 |
| **Performance** | API response time < 500ms p95 for standard queries. File upload < 10s for 50MB document. | Load test (k6 or similar) | — |
| **Availability** | Staging environment: 99% uptime during business hours (Mon–Fri 08:00–18:00 CET). | Uptime monitoring | — |

---

## 10. Acceptance Test Strategy

### 10.1 Per-Epic Acceptance

Each epic's acceptance criteria form the primary test checklist. An epic is complete when all acceptance criteria checkboxes pass. Testing is performed against the staging environment using seed data.

### 10.2 Procedure Coverage Verification

Per AM-TS-001 §18.1: every section of PR-008, PR-009, and PR-010 (the Phase 0 procedures) must have a corresponding system capability.

| Procedure | Sections | Covered By |
|-----------|----------|-----------|
| PR-008 §6.1–6.3 | Material receipt, 5-point check, gate decision | EPIC-06 |
| PR-008 §6.4–6.6 | Physical inspection, traceability, requirement profiles | EPIC-06 (basic), EPIC-03 (profiles) |
| PR-009 §6.1–6.3 | SDRL receipt, parsing, template selection | EPIC-05 |
| PR-009 §6.4–6.6 | MRB initialization, Index generation, section structure | EPIC-05 |
| PR-009 §6.7–6.8 | Document collection, order lifecycle states | EPIC-07 (upload), EPIC-10 (states) |
| PR-010 §6.1–6.3 | L1–L3 validation layers | EPIC-07 |
| PR-010 §6.12 | Correction request process | EPIC-07 |

### 10.3 Module Boundary Tests

Per AM-TS-001 §18.2: automated contract tests verify:

- [ ] Cross-schema views return correct data (ERP reads MRB order status, MRB reads customer data)
- [ ] State machine triggers fire correctly on valid transitions
- [ ] State machine blocks invalid transitions
- [ ] Module isolation: direct cross-schema table access fails (only views allowed)
- [ ] Interface contracts IF-001 through IF-010 function correctly

### 10.4 Security Verification

Per AM-TS-001 §18.3:

- [ ] RLS policies: customer A cannot see customer B's data (orders, documents, MRB)
- [ ] QA Engineer cannot access admin-only screens
- [ ] Customer portal user cannot access internal application
- [ ] Audit log: all state transitions, logins, and data access events present
- [ ] Audit log: UPDATE and DELETE operations on audit_log fail
- [ ] MFA bypass attempt fails

### 10.5 End-to-End Seed Data Test

The seed data tool (EPIC-04) serves as the integration test harness:

- [ ] `mrb-seed reset` clears all seed data cleanly
- [ ] `mrb-seed full-lifecycle` runs without errors and populates all Phase 0 tables
- [ ] After seeding: orders visible in order list, receipts visible, MRB Index populated, validation results present, CRs created for failures
- [ ] Customer portal user can log in and see seeded orders
- [ ] Re-running `mrb-seed full-lifecycle` is idempotent (reset + re-seed produces identical state)

---

## 11. Delivery Milestones

| Milestone | Target | Deliverable | Acceptance Gate |
|-----------|--------|-------------|----------------|
| **M1: Foundation** | End of Sprint 0 (Week 2) | Infrastructure operational, data model deployed, state machine tested | Developer can access local and staging environments. All 36 tables exist. State machine blocks invalid transition. |
| **M2: Data Layer** | End of Sprint 2 (Week 6) | ERP CRUD screens, object storage, seed data tool | `mrb-seed full-lifecycle` generates realistic data visible in UI. File upload works with checksums. |
| **M3: Core Pipeline** | End of Sprint 5 (Week 12) | SDRL Parser, Material Gate, Validation Engine L1–L3 | O&G order can be processed: SDRL uploaded → MRB Index generated → material gate reviewed → documents uploaded → L1–L3 validation runs → CRs created for failures. |
| **M4: Portal & Monitoring** | End of Sprint 7 (Week 16) | Customer Portal MVP, Grafana dashboards | Customer can log in and see order status. System health dashboards operational. |
| **M5: Phase 0 Complete** | End of Sprint 8 (Week 18) | All epics done, integration tested, acceptance criteria verified | Full end-to-end dry run with seed data passes. Procedure coverage verified. Security tests pass. |

---

## 12. References

| VDR Ref | Document |
|---------|----------|
| — | AM-TS-001, IT/System Technical Specification (master document) |
| — | AM-CT-001, Customer-Facing Templates (master document) |
| — | AM-FM-001, Form Templates — Internal Quality Forms (master document) |
| — | AM-IF-001, ERP ↔ MRB Builder Interface Specification (master document) |
| — | PR-008, Incoming Material Review and Release (master document) |
| — | PR-009, SDRL Processing and MRB Management (master document) |
| — | PR-010, Document Validation and Verification (master document) |
| — | PR-011, Certificate of Conformance (master document) |
| — | PR-012, MRB Assembly and Release (master document) |
| — | PR-013, Document Archival and Retention (master document) |
| — | QM-001 Rev 2 Addendum, Quality Manual — Digital MRB Builder Integration (master document) |

---

*This document is the single source of truth for Phase 0 scope. Features not listed here are not in Phase 0. Acceptance criteria are testable — pass or fail, not subjective. Every story and capability traces back to a source specification.*
