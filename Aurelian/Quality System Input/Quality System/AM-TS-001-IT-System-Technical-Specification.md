# IT/SYSTEM TECHNICAL SPECIFICATION — DIGITAL MRB BUILDER

| Field | Value |
|-------|-------|
| **Document No.** | AM-TS-001 |
| **Revision** | 1.3 |
| **Effective Date** | 2026-02-22 |
| **Approved By** | Technical Lead / Quality Manager |
| **Classification** | Internal — Engineering |
| **Status** | Draft — Post Founding Team Review (Tore) |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 0.1 | 2026-02-20 | Fredrik Vangsal | Advisory notes — tech stack and security recommendations |
| **1.0** | **2026-02-21** | **Technical Lead** | **Formal specification based on advisory input. Incorporates all QMS procedures, ERP interface spec, and SDRL requirements.** |
| **1.1** | **2026-02-21** | **Technical Lead** | **Post-Fredrik review: AWS hosting confirmed, Supabase Storage for PDF/A, KMS phased approach (Supabase Vault → HashiCorp Vault). Sections 6, 8, 14, 15, 17 updated.** |
| 1.2 | 2026-02-21 | Technical Lead | Post WP-3 (AM-FM-001) data model expansion: 14 new entities added to §7.2 identified during form template design. ENUM type registry added (§7.5). References to AM-FM-001 added. |
| **1.3** | **2026-02-22** | **Industry & Requirements Lead** | **Post founding team review (Tore). 3 findings: §10.3 ERP module evolution language clarified. §5+§9 shop floor expanded — humanoid robots + AMR (Autonomous Mobile Robots, from Q3 2027) added as Phase 1+ device types. §7.2 MRB entity updated — MRB delivery granularity per PO or per line item. Gate_Review decision ENUM updated: APPROVED/REJECTED/CONDITIONAL_APPROVAL. gate_check_result expanded with CONDITIONAL. itp_point_type expanded with MONITOR. document_review_response ENUM added.** |

---

## 1. Purpose

This document defines the complete technology architecture, infrastructure, security model, data model, and deployment strategy for the Aurelian Manufacturing Digital MRB Builder system.

It serves as the binding technical specification that:

- Translates the business rules defined in PR-008 through PR-013 into buildable system components
- Specifies the technology stack, database architecture, and API framework
- Defines security, availability, and disaster recovery requirements
- Maps each system component to the 5-phase implementation roadmap
- Provides the technical foundation for WP-4 (MVP Scope Definition) and sprint planning

**This is a gate blocker** — software development SHALL NOT commence until this specification is approved by the founding team.

## 2. Scope

This specification covers:

- Technology stack selection and justification
- System architecture and component design
- Data model (core entities and relationships)
- Security architecture (Zero Trust, access control, encryption, audit)
- Machine data integration (CNC, CMM, metrology via MQTT/OPC-UA)
- ERP integration architecture (based on AM-IF-001)
- Document and artifact management (PDF storage, metadata, lifecycle)
- Availability, redundancy, backup, and disaster recovery
- Customer portal architecture
- PDF/A-3 generation strategy
- Deployment and infrastructure (CI/CD, environments, hosting)
- Phase-by-phase component mapping
- Open decisions requiring founder input

This specification does NOT cover:

- Form template field definitions (covered under WP-3)
- Customer-facing SDRL templates (covered under WP-2)
- Work instructions and training materials (WP-5, WP-6)

### Key Architectural Decision: Integrated ERP

Aurelian Manufacturing will build its own ERP module as part of the unified platform, rather than purchasing a third-party ERP system. This ensures seamless data flow across the entire order-to-delivery lifecycle and eliminates the integration overhead of maintaining 20 external interfaces.

The 20 interfaces defined in AM-IF-001 remain valid as **internal module boundaries** — they define the data contracts between the business operations module (ERP) and the quality documentation module (MRB Builder), but they are now internal function calls within the same database and application, not external API calls between separate systems.

This decision means:
- **One unified PostgreSQL database** for both business data and quality documentation
- **No webhook/API overhead** — direct database queries and function calls between modules
- **Shared authentication and authorization** — one user, one session, one role model
- **Simpler deployment** — one application stack, not two separate systems to maintain
- **Full control** — no dependency on third-party ERP vendor roadmaps or API limitations

## 3. References

| Document | Title | Relevance |
|----------|-------|-----------|
| QM-001 Rev 2 Addendum | Quality Manual — Digital MRB Builder Integration | QMS framework and procedure index |
| PR-008 | Incoming Material Review and Release | Material Gate business rules |
| PR-009 | SDRL Processing and MRB Management | SDRL parsing, MRB lifecycle rules |
| PR-010 | Document Validation and Verification | 5-layer validation logic |
| PR-011 | Certificate of Conformance | CoC generation and signature rules |
| PR-012 | MRB Assembly and Release | MRB compilation and release rules |
| PR-013 | Document Archival and Retention | Archive, retention, and DR requirements |
| AM-IF-001 | ERP ↔ MRB Builder Interface Specification | 20 interface contracts |
| AM-CT-001 | Customer-Facing Templates | SDRL templates, MRB Index, Customer Requirement Profile |
| AM-FM-001 | Form Templates — Internal Quality Forms | 24 form specifications with field definitions, validation rules, auto-population specs. Source of Rev 1.2 entity additions. |
| AM-SDRL-2026-001 | Shipment Documentation Requirements (SDRL/MRB) | Industry requirements for Defence and Oil & Gas |
| — | MRB Builder Tech Stack Plan (F. Vangsal, 20 Feb 2026) | Advisory input — technology recommendations |

## 4. Definitions

| Term | Definition |
|------|-----------|
| **Supabase** | Open-source backend-as-a-service platform built on PostgreSQL. Provides database, authentication, object storage, and edge functions. Self-hostable for data sovereignty. |
| **PostgreSQL (Postgres)** | Open-source relational database. Primary data store for all structured MRB Builder data. |
| **RLS** | Row Level Security — PostgreSQL feature that enforces access control at the database row level, ensuring tenant and role isolation. |
| **PostgREST** | Automatically generates a RESTful API from a PostgreSQL schema. Part of the Supabase stack. |
| **Next.js** | React-based web application framework with server-side rendering, API routes, and TypeScript support. |
| **TypeScript** | Typed superset of JavaScript providing compile-time type safety. |
| **MQTT** | Lightweight publish-subscribe messaging protocol for IoT and machine data. Used for CNC/CMM → MRB Builder data ingestion. |
| **OPC-UA** | Open Platform Communications Unified Architecture — industrial automation protocol for machine-to-machine communication. |
| **MTConnect** | Open standard for manufacturing equipment data exchange. |
| **PDF/A-3** | ISO 19005-3 archival PDF format supporting embedded original files. Required for long-term MRB preservation. |
| **WORM** | Write Once Read Many — storage immutability pattern for compliance records. |
| **JSONB** | PostgreSQL binary JSON data type with indexing support. Used for flexible metadata storage. |
| **GraphQL** | Query language for APIs allowing clients to request specific data structures. Planned for Phase 2+ customer portal. |
| **Zero Trust** | Security model where no user, device, or network segment is implicitly trusted. All access must be authenticated, authorized, and logged. |
| **RBAC** | Role-Based Access Control — access permissions assigned by role. |
| **ABAC** | Attribute-Based Access Control — access decisions based on user attributes, resource attributes, and environmental conditions. |
| **RPO** | Recovery Point Objective — maximum acceptable data loss measured in time. |
| **RTO** | Recovery Time Objective — maximum acceptable downtime after a failure. |
| **ADR** | Architecture Decision Record — documented rationale for technical decisions. |
| **KMS** | Key Management Service — centralized management of encryption keys. |
| **CI/CD** | Continuous Integration / Continuous Deployment — automated build, test, and deployment pipeline. |

---

## 5. Architecture Overview

The Aurelian Manufacturing platform is a unified system with two logical modules sharing one database and one application stack:

```
                EXTERNAL SYSTEMS
                ────────────────
    CUSTOMERS ←──Portal──┐          ┌──Portal──→ SUPPLIERS
                         │          │
                         ▼          ▼
    ┌────────────────────────────────────────────────┐
    │                                                │
    │        AURELIAN PLATFORM (unified)             │
    │        ════════════════════════                 │
    │                                                │
    │   ┌─────────────────┐  ┌────────────────────┐  │
    │   │  ERP MODULE     │  │  MRB BUILDER       │  │
    │   │  (Aurelian-built)│  │  MODULE            │  │
    │   │                 │  │                    │  │
    │   │  Purchase Orders│  │  SDRL Parser       │  │
    │   │  Production Ord.│  │  Material Gate     │  │
    │   │  Inventory/Lots │  │  Document Validator│  │
    │   │  Supplier Mgmt  │  │  CoC Generator     │  │
    │   │  Customer CRM   │  │  MRB Assembler     │  │
    │   │  Quoting        │  │  Archive Engine    │  │
    │   │  Scheduling     │  │  Dashboards        │  │
    │   └────────┬────────┘  └─────────┬──────────┘  │
    │            │                     │              │
    │            └──────────┬──────────┘              │
    │                       │                         │
    │              Shared PostgreSQL                   │
    │              Shared Auth (RLS)                   │
    │              Internal Module Boundaries          │
    │              (AM-IF-001 as data contracts)       │
    │                                                │
    └───────────────────────┬────────────────────────┘
                            │
                     MQTT / OPC-UA
                     (Direct feed)
                            │
                 ┌──────────┴───────────┐
                 │  SHOP FLOOR          │
                 │                      │
                 │  CNC Machines (MAZAK)│
                 │  CMM (Zeiss / equiv) │
                 │  Metrology Systems   │
                 │  ─ ─ ─ ─ ─ ─ ─ ─ ─ │
                 │  Phase 1+ devices:   │
                 │  Humanoid Robots     │
                 │  AMR (from Q3 2027)  │
                 └──────────────────────┘
```

### Architecture Principles

1. **Unified platform.** The ERP module and MRB Builder module share one PostgreSQL database, one authentication system, and one deployment. This eliminates integration overhead and ensures data consistency.
2. **Logical module separation.** Despite sharing a database, the ERP module and MRB Builder module maintain clear boundaries. The data contracts defined in AM-IF-001 serve as internal module interfaces — enforced by database schemas, views, and function signatures rather than external APIs.
3. **ERP module owns business data.** Purchase orders, production orders, inventory, supplier records, customer CRM, quoting, and scheduling live in the ERP module's schema.
4. **MRB Builder module owns quality documentation.** MRB Index, validation status, gate decisions, CoC records, assembled MRB packages, and archive metadata live in the MRB Builder module's schema.
5. **Machine data feeds directly into MRB Builder.** CNC, CMM, and metrology data flows via MQTT/OPC-UA into the MRB Builder module. The ERP module can read machine data status but does not own it. The architecture is extensible to support future shop floor device types including humanoid robots and Autonomous Mobile Robots (AMR, expected from Q3 2027) via the same MQTT/OPC-UA framework.
6. **Single source of truth.** Every data object has exactly one owning module. Cross-module access is via database views and functions, never by direct table access.
7. **Records vs Artifacts.** Structured data (orders, validations, status, metadata) is stored in PostgreSQL. Unstructured artifacts (PDFs, certificates, inspection reports, machine output files) are stored in object storage with metadata references in PostgreSQL.

---

## 6. Technology Stack

### 6.1 Core Platform — Supabase (Self-Hosted)

| Property | Specification |
|----------|--------------|
| **Platform** | Supabase (self-hosted) |
| **Database** | PostgreSQL 16+ |
| **Authentication** | Supabase Auth (JWT-based) |
| **Object Storage** | Supabase Storage (backed by AWS S3, eu-north-1) |
| **Edge Functions** | Supabase Edge Functions (Deno runtime) |
| **Hosting Location** | AWS eu-north-1 (Stockholm) — EEA-compliant |
| **Cloud Provider** | Amazon Web Services (AWS) |
| **Data Sovereignty** | All data stored within EEA. No data leaves EEA without explicit authorization. |

**Justification:** Supabase provides a batteries-included platform (auth, storage, real-time, API generation) while allowing full self-hosting for data sovereignty. PostgreSQL-first design aligns with the need for strong constraints, RLS, triggers, and transactional integrity across the MRB lifecycle.

### 6.2 Application Layer — Next.js + TypeScript

| Property | Specification |
|----------|--------------|
| **Framework** | Next.js 14+ (App Router) |
| **Language** | TypeScript (strict mode) |
| **Runtime** | Node.js 20 LTS |
| **Applications** | Internal QA UI, Customer Portal, Admin Dashboard |
| **Rendering** | Server-side rendering (SSR) for initial load, client-side for interactive workflows |

**Application structure (unified platform):**

| Application | Users | Purpose |
|-------------|-------|---------|
| **ERP Workbench** | Commercial Manager, Purchasing, Production Manager | PO management, customer/supplier CRM, inventory, production orders, scheduling |
| **QA Workbench** | QA Engineers, Quality Manager | Material gate review, SDRL parsing, document validation, CoC generation, MRB assembly |
| **Production Dashboard** | Production Manager, CNC Operators | Order status, machine data status, MRB progress per order |
| **Customer Portal** | External customers | MRB download, order documentation status, SDRL submission (Phase 2) |
| **Admin Console** | System administrators | User management, system configuration, audit log viewer |

All applications are built within one Next.js application using role-based routing. The customer portal is a separate deployment for security isolation (see Section 13).

### 6.3 API Layer

| Phase | Technology | Usage |
|-------|-----------|-------|
| **Phase 0–1** | PostgREST (auto-generated REST from Postgres schema) + Supabase RPC (custom functions) | All internal API calls. Internal module communication via DB functions. |
| **Phase 2+** | GraphQL gateway (read-only, over materialized views) | Customer portal data access. MRB view queries. Query complexity limits enforced. |

**API design principles:**

- Internal module boundaries follow the data contracts in AM-IF-001
- Idempotent operations for all state-changing endpoints
- Rate limiting on all external-facing endpoints (customer portal, supplier portal)
- API versioning from day one (URL path: `/api/v1/...`)
- Customer portal API is a separate, read-heavy API layer with strict RLS enforcement

### 6.4 Validation Engine

The validation engine implements the 5-layer document validation defined in PR-010:

| Layer | Validation | Implementation |
|-------|-----------|----------------|
| **L1 — Existence** | Document exists in MRB structure | Database constraint: document slot status check |
| **L2 — Format** | Correct file type, readable, not corrupted | Application-level file validator (MIME type, PDF readability, image integrity) |
| **L3 — Completeness** | All required fields present | JSON Schema validation against document type registry |
| **L4 — Compliance** | Values meet specification limits | Rule engine: DB-stored rules per document type + customer profile. PL/pgSQL functions for numeric range checks, unit conversion, borderline detection. |
| **L5 — Traceability** | Cross-document reference chain intact | Database queries: PO → material cert → goods receiving → traceability matrix → process sheet → inspection → CoC chain verification |

**Rule storage:**

- Validation rules are stored in the database as versioned rule sets
- Rules are scoped by: industry (Defence / Oil & Gas), customer, document type
- Customer-specific Material Requirement Profiles (PR-008) are stored as structured data in JSONB
- Rule changes are version-controlled with effective dates — no rule deletion, only new versions

### 6.5 Document and File Storage

| Data Type | Storage | Format |
|-----------|---------|--------|
| **Structured data** (orders, MRBs, validations, statuses, metadata) | PostgreSQL tables with JSONB for flexible attributes | Relational + JSONB |
| **Uploaded artifacts** (material certs, inspection reports, supplier docs) | S3-compatible object storage (Supabase Storage / MinIO) | Original format (PDF, XLSX, images) |
| **Generated artifacts** (CoC PDFs, assembled MRBs, cover pages) | S3-compatible object storage | PDF/A-3 (ISO 19005-3) |
| **Machine data artifacts** (CNC logs, CMM reports, metrology output) | S3-compatible object storage | Original format + normalized metadata in JSONB |

**Storage principles:**

- Every artifact gets a SHA-256 checksum at ingest, stored in the database
- Artifact metadata (document type, order reference, upload timestamp, uploader, checksum) is always in PostgreSQL — searchable without opening the file
- Object storage keys follow a deterministic path: `/{customer_id}/{order_id}/{mrb_section}/{document_type}/{filename}`
- Artifacts are immutable once validated. Corrections create new versions; originals are preserved.

### 6.6 Observability Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Metrics** | Prometheus | System and application metrics (request latency, error rates, queue depth, validation throughput) |
| **Logs** | Loki | Centralized log aggregation from all services |
| **Traces** | Tempo | Distributed tracing via OpenTelemetry |
| **Dashboards** | Grafana | Unified visualization for metrics, logs, and traces |
| **Alerting** | Grafana Alerting | Threshold alerts for system health, SLA violations, validation failures |

**Instrumentation:** All application code SHALL use OpenTelemetry SDK for consistent telemetry collection.

### 6.7 Testing Strategy

| Test Type | Technology | Scope | Trigger |
|-----------|-----------|-------|---------|
| **Unit tests** | Jest | Business logic, validation rules, data transformations | Every commit (CI) |
| **Integration tests** | Jest + Supertest | API endpoints, database operations, ERP interface contracts | Every PR (CI) |
| **End-to-end tests** | Playwright | Full user workflows (material gate → MRB release) | Nightly + pre-release |
| **Contract tests** | Pact / custom | Internal module boundary compliance (AM-IF-001 data contracts) | Every PR touching module boundaries |
| **Load tests** | k6 | Performance under expected load (concurrent users, MRB volume) | Monthly + pre-release |
| **Security tests** | SAST in CI + periodic DAST | Code vulnerabilities, dependency scanning | Every PR (SAST), quarterly (DAST/pentest) |

**Coverage targets:** Minimum 80% statement coverage for core business logic (validation engine, state machine, CoC generation).

### 6.8 Documentation

| Type | Platform | Content |
|------|----------|---------|
| **System documentation** | GitBook (or Docusaurus) | Architecture, API docs, deployment guides, runbooks |
| **Architecture decisions** | ADRs in Git repository | Rationale for all significant technical decisions |
| **API reference** | Auto-generated from PostgREST schema + OpenAPI | Endpoint documentation |
| **Procedure-to-code mapping** | In-repo markdown | Mapping from PR-xxx sections to code modules |

---

## 7. Data Model

### 7.1 Core Entities

The following entity model covers the full Aurelian Platform data domain. The ERP module and MRB Builder module share one PostgreSQL database with separate schemas. All entities below are owned by one module but accessible (read-only) by the other via views.

```
ERP MODULE ENTITIES                         MRB BUILDER MODULE ENTITIES
═══════════════════                         ═══════════════════════════

┌─────────────┐     ┌──────────────────┐     ┌────────────────┐
│  Customer    │────>│  Order           │────>│  MRB           │
│              │     │                  │     │                │
│  customer_id │     │  order_id        │     │  mrb_id        │
│  name        │     │  po_number       │     │  order_id (FK) │
│  org_number  │     │  customer_id(FK) │     │  industry_class│
│  industry    │     │  sdrl_id (FK)    │     │  mrb_state     │
│  contacts[]  │     │  order_state     │     │  mrb_index     │
│  req_profile │     │  created_at      │     │  section_count │
│  addresses[] │     │  quoted_at       │     │  created_at    │
└─────────────┘     │  delivery_date   │     └───────┬────────┘
                     └────────┬─────────┘             │
      ┌──────────────┐       │               ┌───────┴────────┐
      │  Supplier     │       │               │  MRB_Document  │
      │               │       │               │                │
      │  supplier_id  │       │               │  doc_id        │
      │  name         │       │               │  mrb_id (FK)   │
      │  approved     │       │               │  section_no    │
      │  cert_status  │       │               │  doc_type      │
      │  contacts[]   │       │               │  artifact_uri  │
      └──────────────┘       │               │  checksum      │
                              │               │  val_status    │
                              │               │  val_layer     │
                              │               │  uploaded_at   │
                              │               └───────┬────────┘
                              │                       │
                     ┌────────┴─────────┐    ┌───────┴────────┐
                     │  SDRL            │    │  MRB_Document  │
                     │                  │    │                │
                     │  sdrl_id         │    │  doc_id        │
                     │  raw_file_uri    │    │  mrb_id (FK)   │
                     │  industry_class  │    │  section_no    │
                     │  section_count   │    │  doc_type      │
                     │  parsed_at       │    │  artifact_uri  │
                     └────────┬─────────┘    │  checksum      │
                              │              │  val_status    │
                     ┌────────┴─────────┐    │                │
                     │ SDRL_Line_Item   │    │  review_code   │
                     │                  │    │  criticality   │
                     │  line_id (PK)    │    │  data_source   │
                     │  sdrl_id (FK)    │    │  required_fmt  │
                     │  line_item_id    │    │  standard_ref  │
                     │  mrb_section     │    │  notes         │
                     │  doc_title       │    │                │
                     │  standard_ref    │    │                │
                     │  required_format │    │                │
                     │  review_code     │    │                │
                     │  criticality     │    │                │
                     │  data_source     │    │                │
                     │  is_required     │    │                │
                     │  submission_time │    │                │
                     └──────────────────┘    │                │
                                             │  val_layer     │
                                             │  uploaded_at   │
                                             └───────┬────────┘
                                                     │
                                            ┌────────┴────────┐
                                            │  Validation     │
                                            │                 │
                                            │  validation_id  │
                                            │  doc_id (FK)    │
                                            │  layer (L1-L5)  │
                                            │  result         │
                                            │  details (JSONB)│
                                            │  validator_id   │
                                            │  validated_at   │
                                            └─────────────────┘
```

### 7.2 Complete Entity List

**ERP Module Entities (business operations):**

| Entity | Description | Key Fields |
|--------|-------------|------------|
| **Customer** | Customer master record | customer_id, name, org_number, industry, addresses (JSONB), contacts (JSONB), requirement_profile (JSONB), payment_terms |
| **Supplier** | Approved supplier record | supplier_id, name, org_number, approved_status, cert_status, approved_materials (JSONB), contacts (JSONB) |
| **Purchase_Order** | Customer PO received | po_id, po_number, customer_id, received_date, delivery_date, line_items (JSONB), commercial_terms (JSONB) |
| **Production_Order** | Internal manufacturing order | prod_order_id, po_id, part_number, drawing_rev, quantity, material_grade, routing (JSONB), scheduled_start, scheduled_end |
| **Inventory_Lot** | Material inventory tracking | lot_id, material_grade, heat_number, supplier_id, quantity_kg, location, status (AVAILABLE/RESERVED/CONSUMED) |
| **Quote** | Price quotation to customer | quote_id, customer_id, line_items (JSONB), total_price, currency, valid_until, status |

**MRB Builder Module Entities (quality documentation):**

| Entity | Description | Key Fields |
|--------|-------------|------------|
| **Order** | Order lifecycle tracking (linked to PO) | order_id, po_number, customer_id, sdrl_id, order_state, industry_class |
| **SDRL** | Parsed SDRL header | sdrl_id, raw_file_uri, industry_class, section_count, parsed_at |
| **SDRL_Line_Item** | Individual SDRL document requirement (relational — one row per line item) | line_id, sdrl_id (FK), line_item_id, mrb_section, doc_title, standard_ref, required_format (ENUM: PDF/PDF_A/NATIVE/SIGNED), review_code (ENUM: FOR_INFO/FOR_REVIEW/FOR_APPROVAL), criticality (ENUM: CRITICAL/MAJOR/STANDARD), data_source (ENUM: CNC_INLINE/METROLOGY/INSPECTION/SUPPLIER/SPECIAL_PROCESS/INTERNAL_QA/CUSTOMER), is_required (BOOLEAN), submission_timing (ENUM: WITH_SHIPMENT/BEFORE_SHIPMENT/AT_MILESTONE/ON_REQUEST), notes |
| **MRB** | Manufacturing Record Book instance. One MRB per order (default) or one MRB per PO line item (for large orders). Delivery granularity is configurable. Full normalization of PO line items planned for Phase 0.5. | mrb_id, order_id, po_line_item_ref (VARCHAR, nullable — set when MRB is per line item), industry_class, mrb_state, mrb_index (JSONB), section_count |
| **MRB_Document** | Individual document within an MRB | doc_id, mrb_id, section_no, line_item, doc_type, artifact_uri, checksum_sha256, validation_status, review_code, criticality, data_source, required_format, standard_ref, submission_timing, notes |
| **Validation** | Validation result per document per layer | validation_id, doc_id, layer, result (PASS/FAIL/WAIVED), details (JSONB), validator_id |
| **Material_Receipt** | Goods receiving record | receipt_id, order_id, material_grade, heat_number, supplier_id, cert_uri, gate_decision (ENUM: gate_decision) |
| **Material_Requirement_Profile** | Customer-specific material acceptance criteria | profile_id, customer_id, material_grade, cert_type_required, chemical_limits (JSONB), mechanical_limits (JSONB), supplementary_tests (JSONB) |
| **Gate_Review** | Material gate decision record (PR-008) | review_id, receipt_id, decision (APPROVED/REJECTED/CONDITIONAL_APPROVAL), check_results (JSONB), reviewer_id, qm_override (BOOLEAN), qm_decision (gate_decision, nullable) |
| **CoC** | Certificate of Conformance | coc_id, mrb_id, coc_number, template_type, signed_by, signed_at, signature_hash, signature_method (ENUM: INTERNAL_PKI/BANKID/MANUAL), pdf_uri, checksum_sha256 |
| **Correction_Request** | Validation failure correction tracking | cr_id, doc_id, validation_id, description, assigned_to, status, resolved_at |
| **Archive_Record** | Archival metadata | archive_id, mrb_id, archive_date, archive_tier (ACTIVE/DEEP), checksum_sha256, retention_expiry |
| **Machine_Event** | Normalized machine data event | event_id, machine_id, order_id, event_type, payload (JSONB), artifact_uri, checksum_sha256, recorded_at |
| **Audit_Log** | Immutable audit trail | log_id, user_id, action, entity_type, entity_id, details (JSONB), ip_address, timestamp |

**MRB Builder Module Entities — Extended (Rev 1.2, from AM-FM-001):**

The following 14 entities were identified during form template design (AM-FM-001) and support the full MRB lifecycle from physical inspection through archival disposition.

| Entity | Description | Key Fields | Source Form |
|--------|-------------|------------|-------------|
| **Physical_Inspection** | PMI, visual, and dimensional inspection results | inspection_id, receipt_id (FK→Material_Receipt), order_id (FK), inspection_type (ENUM: VISUAL/DIMENSIONAL/PMI/NDT), pmi_method (ENUM: XRF/OES/LABORATORY), result (PASS/FAIL/CONDITIONAL), measurements (JSONB), inspector_id, inspected_at | FM-008-02 |
| **Material_Traceability** | Material-to-serial-number allocation header | traceability_id, order_id (FK), material_grade, heat_number, total_quantity_kg, allocated_quantity_kg, gate_review_id (FK→Gate_Review), created_at | FM-008-03 |
| **Material_Traceability_Detail** | Individual serial number allocation within a traceability record | detail_id, traceability_id (FK→Material_Traceability), serial_number, part_number, allocated_kg, production_order_id, created_at | FM-008-03 |
| **ITP_Tracker** | Inspection Test Plan header (Oil & Gas only) | itp_id, order_id (FK), itp_number, customer_id (FK), total_points (INTEGER), completed_points (INTEGER), status (ACTIVE/COMPLETED/SUSPENDED), created_at | FM-009-02 |
| **ITP_Point** | Individual ITP hold/witness/review point | point_id, itp_id (FK→ITP_Tracker), point_number, description, point_type (ENUM: HOLD/WITNESS/REVIEW/SURVEILLANCE), manufacturing_stage, customer_witness_required (BOOLEAN), status (ENUM: PENDING/SCHEDULED/COMPLETED/WAIVED), completed_at, signed_by, customer_representative, notes | FM-009-02 |
| **Traceability_Verification** | Cross-document reference chain verification | verification_id, mrb_id (FK), verified_by, verification_date, chain_results (JSONB — array of {doc_id, chain_status, missing_links[]}), overall_result (PASS/FAIL), failed_chains (INTEGER), total_chains (INTEGER) | FM-010-03 |
| **CoC_Prerequisite_Gate** | 6-check gate blocking CoC generation | gate_id, mrb_id (FK), checked_by, checked_at, all_docs_validated (BOOLEAN), no_open_crs (BOOLEAN), traceability_verified (BOOLEAN), fair_complete (BOOLEAN), itp_signed_off (BOOLEAN), no_borderline_items (BOOLEAN), overall_result (PASS/FAIL), notes | FM-010-04 |
| **CoC_Revision** | CoC revision and void history | revision_id, coc_id (FK→CoC), action (ENUM: REVISION/VOID), reason, previous_status (ENUM: ACTIVE/SUPERSEDED/VOID), new_coc_id (FK→CoC, nullable), actioned_by, actioned_at | FM-011-02 |
| **Authorized_Signatory** | Signatory authority register | signatory_id, user_id (FK→auth.users), authority_level (ENUM: LEVEL_1/LEVEL_2/LEVEL_3), signature_method (ENUM: INTERNAL_PKI/BANKID/MANUAL), scope (TEXT), max_coc_value (NUMERIC, nullable), valid_from (DATE), valid_to (DATE, nullable), status (ACTIVE/SUSPENDED/REVOKED), approved_by | FM-011-03 |
| **Assembly_Checklist** | MRB assembly prerequisites verification | checklist_id, mrb_id (FK), all_documents_present (BOOLEAN), all_validations_passed (BOOLEAN), coc_signed (BOOLEAN), no_open_corrections (BOOLEAN), index_matches_sdrl (BOOLEAN), page_numbering_complete (BOOLEAN), checked_by, checked_at, result (PASS/FAIL) | FM-012-01 |
| **Quality_Check** | MRB 10-point quality check and release record | check_id, mrb_id (FK), check_results (JSONB — 10 check items with pass/fail), release_type (ENUM: STANDARD/ELEVATED), overall_result (PASS/FAIL), checked_by, approved_by (nullable, for elevated release), released_at | FM-012-02 |
| **Customer_Approval** | Customer pre-shipment approval record | approval_id, mrb_id (FK), order_id (FK), customer_id (FK), submitted_at, customer_representative, approval_status (ENUM: PENDING/APPROVED/APPROVED_WITH_COMMENTS/REJECTED), response_at (nullable), comments (TEXT, nullable), conditions (TEXT, nullable) | FM-012-03 |
| **Delivery_Confirmation** | MRB delivery tracking | delivery_id, mrb_id (FK), order_id (FK), delivery_method (ENUM: PHYSICAL/ELECTRONIC/BOTH), physical_tracking (TEXT, nullable), electronic_portal_ref (TEXT, nullable), delivered_at, received_by (TEXT, nullable), receipt_confirmed (BOOLEAN), confirmed_at (nullable) | FM-012-04 |
| **Disposition_Request** | Archive record disposition request | request_id, archive_id (FK→Archive_Record), requested_by, requested_at, reason, disposition_method (ENUM: SECURE_DELETE/CRYPTO_SHRED), legal_review_by (nullable), legal_review_at (nullable), legal_approved (BOOLEAN, nullable), status (ENUM: PENDING/APPROVED/REJECTED/EXECUTED) | FM-013-03 |
| **Disposition_Record** | Physical/electronic record destruction documentation | record_id, request_id (FK→Disposition_Request), archive_id (FK→Archive_Record), executed_by, executed_at, method_used (ENUM: SECURE_DELETE/CRYPTO_SHRED), verification_hash (TEXT), witness (TEXT, nullable) | FM-013-04 |
| **Integrity_Report** | Annual archive integrity verification | report_id, report_year (INTEGER), checked_by, checked_at, total_records (INTEGER), records_checked (INTEGER), checksum_matches (INTEGER), checksum_mismatches (INTEGER), unreadable (INTEGER), overall_result (ENUM: MATCH/MISMATCH/UNREADABLE), discrepancy_details (JSONB, nullable), corrective_actions (TEXT, nullable) | FM-013-05 |

**Entity Count Summary (Rev 1.2):**

| Module | Count | Entities |
|--------|-------|----------|
| ERP Module | 6 | Customer, Supplier, Purchase_Order, Production_Order, Inventory_Lot, Quote |
| MRB Builder — Core (Rev 1.0) | 14 | Order, SDRL, SDRL_Line_Item, MRB, MRB_Document, Validation, Material_Receipt, Material_Requirement_Profile, Gate_Review, CoC, Correction_Request, Archive_Record, Machine_Event, Audit_Log |
| MRB Builder — Extended (Rev 1.2) | 16 | Physical_Inspection, Material_Traceability, Material_Traceability_Detail, ITP_Tracker, ITP_Point, Traceability_Verification, CoC_Prerequisite_Gate, CoC_Revision, Authorized_Signatory, Assembly_Checklist, Quality_Check, Customer_Approval, Delivery_Confirmation, Disposition_Request, Disposition_Record, Integrity_Report |
| **Total** | **36** | |

### 7.3 Order State Machine

The order lifecycle follows a strict state machine (defined in PR-009):

```
NEW → SDRL_RECEIVED → SDRL_PARSED → MRB_INITIALIZED → COLLECTING
  → VALIDATING → COC_PENDING → COC_SIGNED → MRB_ASSEMBLY
  → MRB_RELEASED → SHIPPED → ARCHIVED
```

State transitions are enforced at the database level via constraints and triggers. Each transition is logged in the Audit_Log. The ERP module reads order state via the `mrb.order_status` view.

### 7.4 MRB Document States

```
PENDING → RECEIVED → VALIDATING → VALIDATED → INCLUDED_IN_MRB
                   → FAILED → CORRECTION_REQUESTED → RECEIVED (re-submit)
                   → WAIVED (customer approval)
                   → NOT_APPLICABLE (SDRL exception)
```

### 7.5 PostgreSQL ENUM Type Registry (Rev 1.2)

All custom types below are PostgreSQL ENUM types. Adding new values requires a database migration. Removing values is prohibited (soft-deprecation only). The authoritative source for ENUM definitions across all 24 forms is AM-FM-001 §6 (Master ENUM Registry).

**Order and Classification ENUMs:**

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `industry_class` | OIL_GAS, DEFENCE, MARITIME, STANDARD | Order, MRB, SDRL, all industry-dependent entities |
| `order_state` | NEW, SDRL_RECEIVED, SDRL_PARSED, MRB_INITIALIZED, COLLECTING, VALIDATING, COC_PENDING, COC_SIGNED, MRB_ASSEMBLY, MRB_RELEASED, SHIPPED, ARCHIVED | Order (12-state machine) |
| `mrb_index_state` | DRAFT, LIVE, FINAL | MRB Index view state tracking |

**Material and Certificate ENUMs:**

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `cert_type` | EN_10204_2_1, EN_10204_2_2, EN_10204_3_1, EN_10204_3_2 | Material_Receipt, Material_Requirement_Profile, Gate_Review |
| `gate_decision` | APPROVED, REJECTED, CONDITIONAL_APPROVAL | Gate_Review, Material_Receipt. System-wide terminology for all reviewable entities. |
| `gate_check_result` | PASS, FAIL, CONDITIONAL, BORDERLINE, N_A | Gate_Review (check_results JSONB). CONDITIONAL = QA Engineer marks as conditionally passed. |
| `pmi_method` | XRF, OES, LABORATORY | Physical_Inspection, Material_Requirement_Profile |

**SDRL and Document ENUMs:**

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `required_format` | PDF, PDF_A, NATIVE, SIGNED | SDRL_Line_Item, MRB_Document |
| `review_code` | FOR_INFO, FOR_REVIEW, FOR_APPROVAL | SDRL_Line_Item, MRB_Document |
| `criticality` | CRITICAL, MAJOR, STANDARD | SDRL_Line_Item, MRB_Document, Correction_Request |
| `data_source` | CNC_INLINE, METROLOGY, INSPECTION, SUPPLIER, SPECIAL_PROCESS, INTERNAL_QA, CUSTOMER | SDRL_Line_Item, MRB_Document |
| `submission_timing` | WITH_SHIPMENT, BEFORE_SHIPMENT, AT_MILESTONE, ON_REQUEST | SDRL_Line_Item, MRB_Document |
| `sdrl_parse_method` | MANUAL, EXCEL_UPLOAD, PDF_EXTRACT, PORTAL | SDRL |
| `itp_point_type` | HOLD, WITNESS, REVIEW, MONITOR, SURVEILLANCE | ITP_Point. MONITOR = customer has right to attend but not binding. |
| `document_review_response` | APPROVED, APPROVED_WITH_COMMENTS, CONDITIONAL_APPROVAL, REJECTED, REVISE_AND_RESUBMIT | Customer_Approval (FM-012-03). Captures customer feedback on submitted documents. |

**Validation and Correction ENUMs:**

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `validation_status` | PENDING, RECEIVED, VALIDATING, VALIDATED, REJECTED, CORRECTED, WAIVED, NOT_APPLICABLE | MRB_Document, Validation |
| `validation_layer` | L1_EXISTENCE, L2_FORMAT, L3_COMPLETENESS, L4_COMPLIANCE, L5_TRACEABILITY | Validation, Correction_Request |
| `validation_result` | PASS, FAIL, WAIVED | Validation |
| `failure_code` | MISSING, FORMAT_ERROR, INCOMPLETE, NON_COMPLIANT, TRACEABILITY_BREAK | Correction_Request |
| `cr_status` | OPEN, IN_PROGRESS, RESOLVED, ESCALATED, WAIVED | Correction_Request |
| `responsible_role` | QA_ENGINEER, PURCHASING, PRODUCTION, CUSTOMER, SUPPLIER | Correction_Request |

**CoC and Signature ENUMs:**

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `signature_method` | INTERNAL_PKI, BANKID, MANUAL | CoC, Authorized_Signatory |
| `coc_status` | ACTIVE, SUPERSEDED, VOID | CoC, CoC_Revision |
| `authority_level` | LEVEL_1, LEVEL_2, LEVEL_3 | Authorized_Signatory |
| `coc_template_type` | OIL_GAS_STANDARD, DEFENCE_STANDARD, DEFENCE_AQAP, CUSTOM | CoC |

**Archive and Disposition ENUMs:**

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `archive_tier` | ACTIVE, DEEP | Archive_Record |
| `disposition_method` | SECURE_DELETE, CRYPTO_SHRED | Disposition_Request, Disposition_Record |
| `integrity_check_result` | MATCH, MISMATCH, UNREADABLE | Integrity_Report |

**Delivery and Release ENUMs:**

| ENUM Name | Values | Used By |
|-----------|--------|---------|
| `delivery_method` | PHYSICAL, ELECTRONIC, BOTH | Delivery_Confirmation |
| `release_type` | STANDARD, ELEVATED | Quality_Check |

**Total:** 27 ENUM types across 7 groups. All types are shared between AM-TS-001 (data model) and AM-FM-001 (form templates) to ensure consistency.

---

## 8. Security Architecture

### 8.1 Zero Trust Principles

The MRB Builder handles export-controlled information (ITAR/EAR for defence), proprietary customer drawings, and legally binding certificates. The security architecture follows Zero Trust:

1. **Identity-first:** All access requires strong authentication (MFA). No anonymous access. No shared accounts.
2. **Least privilege:** Users receive the minimum permissions required for their role. Permissions are never inherited implicitly.
3. **Verify explicitly:** Every request is authenticated and authorized, regardless of network location.
4. **Assume breach:** System design assumes compromise of any single component. Blast radius is limited by isolation.

### 8.2 Authentication

| Phase | Technology | Details |
|-------|-----------|---------|
| **Phase 0–1** | Supabase Auth (email + password + MFA) | Low friction for initial team. JWT tokens with short expiry (1 hour access, 7 day refresh). |
| **Phase 2+** | Auth adapter layer → WorkOS or Entra ID (SSO) | Enterprise SSO when customer organizations require it. SCIM provisioning for automated user management. |

**Auth adapter pattern:** The application SHALL interact with authentication through an abstraction layer (`AuthAdapter` interface) so the underlying provider can be swapped without application changes. This is a firm architectural requirement — not a Phase 2 consideration.

### 8.3 Authorization — RBAC + ABAC via Postgres RLS

| Layer | Mechanism | Scope |
|-------|-----------|-------|
| **Application level** | Role-Based Access Control (RBAC) | Coarse-grained: QA Engineer, Production Manager, Commercial Manager, Admin, Customer (portal) |
| **Database level** | Attribute-Based Access Control (ABAC) via PostgreSQL Row Level Security (RLS) | Fine-grained: customer_id, order_id, role, clearance level |

**RLS policies ensure:**

- A customer portal user can ONLY see data where `customer_id` matches their authenticated customer
- A QA Engineer can see all orders but can only modify orders assigned to their team
- Archive records are read-only for all users (no DELETE, no UPDATE after archive)
- CoC records are immutable after signing (no UPDATE — only VOID creates a new record)

### 8.4 Encryption

| Layer | Specification |
|-------|--------------|
| **In transit** | TLS 1.3 for all connections (application, database, object storage, MQTT broker) |
| **At rest — database** | AES-256 encryption on disk (AWS EBS encryption with AWS-managed keys) |
| **At rest — object storage** | AES-256 server-side encryption (AWS S3 SSE). Customer-specific KMS keys evaluated for Phase 2+ (high-sensitivity ITAR material). |
| **Secrets — Phase 0–1** | No secrets in code or CI configuration. All secrets managed via **Supabase Vault** (built-in secret management using Postgres `pgsodium` extension). |
| **Secrets — Phase 2+** | Migration to **HashiCorp Vault** for centralized KMS when multi-tenant Defence data and ITAR classification handling are required. |

### 8.5 Audit Trail

An immutable audit log captures ALL security-relevant events:

- User login/logout (success and failure)
- Every document read/download (who, when, which document, from which IP)
- Every validation status change
- Every gate decision (APPROVED/REJECTED/CONDITIONAL_APPROVAL)
- Every CoC signature event
- Every MRB release event
- Every archive access
- All permission changes
- All configuration changes

The audit log table has NO UPDATE or DELETE permissions for any user or role. Append-only. Retained for the lifetime of the associated records (15–30+ years per PR-013).

### 8.6 Tenant Isolation

- All data rows include `customer_id` and `order_id` foreign keys
- PostgreSQL RLS policies enforce isolation at every query
- The customer portal runs as a separate application instance with separate authentication policies, separate rate limiting, and no access to internal QA functions
- Customer A cannot see Customer B's orders, documents, or MRB packages — enforced at the database level, not just the application level

### 8.7 Export Control (ITAR/EAR)

For defence orders subject to ITAR/EAR:

- ECCN classification is stored as an order attribute
- Access to ITAR-controlled documents requires additional clearance attribute on the user record
- All access to ITAR material is logged with enhanced audit detail
- ITAR documents are stored in a logically separated storage bucket with additional access controls
- Data residency is enforced (no storage or processing outside approved jurisdictions)

---

## 9. Machine Data Integration

### 9.1 Architecture

```
Phase 0.5+ (current devices):
CNC Machine (MAZAK)  ──→  MQTT Broker  ──→  MRB Builder Ingestion Service
CMM (Zeiss / equiv)  ──→  (on-prem)    ──→  Artifact Storage + Metadata in DB
Metrology Systems    ──→              ──→

Phase 1+ (future devices, from Q3 2027):
Humanoid Robots      ──→  MQTT Broker  ──→  MRB Builder Ingestion Service
AMR (Autonomous      ──→  (on-prem)    ──→  (material tracking, logistics events)
 Mobile Robots)
```

### 9.2 Protocol Stack

| Source | Protocol | Data Type | Phase |
|--------|----------|-----------|-------|
| CNC machines (MAZAK) | MTConnect (preferred, native MAZAK support) or OPC-UA | Job completion events, cycle data, tool data, program references | Phase 0.5 |
| CMM inspection | File-based export (DMIS/QIF format) or OPC-UA | Dimensional measurement results, tolerance pass/fail | Phase 0.5 |
| Metrology systems | Vendor-specific export + MQTT wrapper | Surface finish, hardness, PMI results | Phase 0.5 |
| Humanoid robots | OPC-UA or vendor API + MQTT wrapper | Assembly verification, quality hold confirmations, process data | Phase 1+ |
| AMR (Autonomous Mobile Robots) | MQTT (fleet management API) | Material movement events, lot tracking, delivery confirmations | Phase 1+ (Q3 2027) |

### 9.3 Canonical Event Schema

All machine data is normalized to a canonical internal format before storage:

```json
{
  "event_id": "uuid",
  "event_type": "JOB_COMPLETE | MEASUREMENT_RESULT | INSPECTION_REPORT",
  "machine_id": "MAZAK-001",
  "order_id": "ORD-2027-0042",
  "operation_id": "OP-030",
  "timestamp_utc": "2027-07-15T14:32:00Z",
  "operator_id": "EMP-012",
  "artifact_uri": "s3://machine-data/MAZAK-001/2027-07-15/job_report.pdf",
  "artifact_checksum_sha256": "a3f2...",
  "payload": {
    "program_name": "PRG-4521-REV3",
    "cycle_time_seconds": 342,
    "tool_changes": 4,
    "parts_produced": 1,
    "serial_number": "SN-2027-0042-001"
  }
}
```

### 9.4 Edge Buffer and Resilience

- The MQTT broker runs on-premises, physically close to the machines
- Messages are persisted to disk queue (QoS 2 — exactly-once delivery)
- If network connectivity to the cloud-hosted MRB Builder is lost, the edge broker queues events locally
- When connectivity is restored, events are replayed in chronological order
- The ingestion service is idempotent — duplicate events (same event_id) are ignored

### 9.5 Integrity

- SHA-256 checksum is generated for every artifact file at the point of ingest (edge broker)
- The checksum is stored in the database alongside the artifact URI
- Document validation (PR-010) can verify file integrity by recalculating the checksum
- Annual archive integrity checks (PR-013) compare stored checksums against recalculated values

---

## 10. Internal Module Integration (ERP ↔ MRB Builder)

### 10.1 Design Principles

Since both the ERP module and MRB Builder module are built by Aurelian and share one PostgreSQL database, the 20 interfaces defined in AM-IF-001 are implemented as **internal module boundaries** rather than external API calls:

1. **Shared database, separate schemas.** The ERP module uses schema `erp.*` and the MRB Builder uses schema `mrb.*`. Cross-module access is via database views and functions — never direct table access.
2. **Data contracts preserved.** The data payloads defined in AM-IF-001 remain valid as the field-level contracts between modules. This ensures the architecture could be decoupled in the future if needed.
3. **Event-driven internally.** Module-to-module communication uses PostgreSQL NOTIFY/LISTEN or an internal event bus. When the ERP module creates a new PO, it emits an event that the MRB Builder module consumes to trigger SDRL processing.
4. **State machine enforced.** The order state machine is enforced at the database level via constraints and triggers. Both modules respect the same state transitions.
5. **Simulation still valuable.** During Phase 0, seed scripts populate the ERP module tables with simulated POs, SDRLs, and material receipts, allowing end-to-end lifecycle testing before real data is available.

### 10.2 Module Boundary Implementation

| AM-IF-001 Interface | Internal Implementation |
|---------------------|----------------------|
| IF-001 New Purchase Order | ERP module INSERT → PostgreSQL trigger emits `new_order` event → MRB module listens and initializes order tracking |
| IF-002 SDRL Attachment | ERP module stores SDRL file → MRB module reads via `erp.sdrl_attachments` view |
| IF-003 Goods Receiving | ERP module records receipt → trigger notifies MRB module → Material Gate review initiated |
| IF-004 Material Certificate | ERP module stores cert → MRB module accesses via view for validation |
| IF-005 Material Gate Decision | MRB module writes decision → ERP module reads via `mrb.gate_decisions` view → updates inventory status |
| IF-006 Production Order Link | ERP module creates prod order → MRB module links to MRB structure |
| IF-008 Order State Update | MRB module updates state → trigger notifies ERP module |
| IF-009 MRB Complete | MRB module sets MRB_RELEASED → ERP module reads for shipment clearance |
| IF-010 CoC Registered | MRB module registers CoC → ERP module reads for shipment documentation |
| IF-011 Shipment Release | Coordinated update: ERP confirms shipment → MRB confirms documentation complete |
| IF-012–020 | Implemented progressively as internal functions per Phase mapping (Section 16) |

### 10.3 ERP Module Scope (Phase 0–1 MVP)

The ERP module is designed for progressive expansion from Phase 0 core capabilities (PO management, basic inventory, customer/supplier CRUD) to a full manufacturing ERP. In Phase 0–1, it covers the minimum business operations needed to support MRB production. The architecture supports incremental feature addition without structural changes:

| Function | Phase 0 | Phase 1 | Phase 2+ |
|----------|---------|---------|----------|
| Purchase Order management | Simulated (seed data) | Manual entry UI | Full PO workflow |
| Customer management | Basic CRUD | Full CRM | Portal integration |
| Supplier management | Basic CRUD | Approved supplier list | Supplier portal |
| Material inventory | Simulated lots | Basic lot tracking | Full inventory with reservations |
| Production order management | Simulated | Basic scheduling | Full routing and scheduling |
| Quoting | — | — | Quote-to-order workflow |
| Finance/invoicing | — | — | Basic invoicing or integration |

**Note:** The ERP module scope will be detailed in a separate specification document. This section defines only the integration architecture with the MRB Builder module.

### 10.4 Phase 0 Seed Data Tool

A seed data tool SHALL be built as the first development deliverable:

- `mrb-seed full-lifecycle` — populates ERP tables with a complete simulated order (PO, SDRL, material receipt, production order) and triggers MRB Builder lifecycle
- `mrb-seed oilgas-norsok` — Oil & Gas lifecycle with NORSOK requirements and ITP hold points (primary Phase 0 scenario)
- `mrb-seed defence-aqap` — Defence lifecycle with AQAP requirements and FAIR (secondary Phase 0 scenario)
- `mrb-seed error-scenarios` — rejected material, failed validation, correction requests, voided CoCs

Seed data SHALL be based on real SDRL structures from Oil & Gas customers (available within weeks) to ensure realistic testing.

---

## 11. Document and Artifact Management

### 11.1 Document Type Registry

A central registry defines all document types the system handles:

| Property | Description |
|----------|-------------|
| `doc_type_id` | Unique identifier (e.g., `EN10204_3_1`, `AS9102_FAIR`, `DIMENSIONAL_REPORT`) |
| `display_name` | Human-readable name |
| `industry` | DEFENCE, OIL_GAS, BOTH |
| `mrb_section` | Default MRB section number |
| `accepted_formats` | Allowed MIME types (e.g., `application/pdf`, `image/tiff`) |
| `validation_schema` | JSON Schema reference for L3 (completeness) validation |
| `compliance_rules` | Reference to L4 compliance rule set |
| `retention_years` | Minimum retention period |

### 11.2 Storage Lifecycle

```
UPLOAD → QUARANTINE → INGESTED → VALIDATED → ACTIVE_ARCHIVE → DEEP_ARCHIVE → DISPOSITION
```

- **QUARANTINE:** Newly uploaded files are virus-scanned and checksum-generated before acceptance
- **INGESTED:** File accepted into object storage with metadata in database
- **VALIDATED:** File has passed all applicable validation layers
- **ACTIVE_ARCHIVE:** Included in a released MRB. Rapid retrieval (< 1 second). Retained for 2 years after shipment.
- **DEEP_ARCHIVE:** Moved to lower-cost storage tier. Retrieval within 4 hours. Retained for full retention period (15–30+ years).
- **DISPOSITION:** Retention period expired. Disposition request and approval required (PR-013). Cryptographic erasure.

### 11.3 Immutability and Versioning

- Validated documents are immutable. No overwrite, no delete.
- Corrections create a new version linked to the original. The original is preserved with an `SUPERSEDED` status.
- CoC PDFs are immutable after signature. A voided CoC retains its number with `VOID` status; a new CoC gets a new number.
- Archive records are append-only. No deletion without authorized disposition process.

---

## 12. Availability, Redundancy, and Disaster Recovery

### 12.1 Availability Targets

| Metric | Target | Justification |
|--------|--------|---------------|
| **RPO** (Recovery Point Objective) | 15 minutes | Maximum 15 minutes of data loss in a disaster scenario. Achieved via streaming replication. |
| **RTO** (Recovery Time Objective) | 2 hours | System operational within 2 hours of a major failure. Manual failover in Phase 0–1, automated in Phase 2+. |
| **Uptime target** | 99.5% (Phase 0–1), 99.9% (Phase 2+) | Excludes planned maintenance windows. |

### 12.2 Backup Strategy — 3-2-1 Rule

| Copy | Location | Retention |
|------|----------|-----------|
| **Primary** | AWS eu-north-1 (Stockholm) | Live |
| **Replica** | AWS eu-west-1 (Ireland) — EEA-compliant secondary | Streaming replication, 15-minute lag max |
| **Off-site** | Encrypted backup to separate AWS account | Daily snapshots, 90-day retention. Annual full backup retained for 5 years. |

- PostgreSQL: WAL-based streaming replication to secondary AWS region
- Object storage: S3 Cross-Region Replication (CRR) to eu-west-1
- Backup integrity: monthly restore test in staging environment. Measure actual RTO/RPO.

### 12.3 Failover

| Phase | Failover Type | Process |
|-------|--------------|---------|
| **Phase 0–1** | Manual failover | Runbook-driven. Manual DNS switch + database promotion. Target: 2-hour RTO. |
| **Phase 2+** | Semi-automated | Automated health check detection + manual approval before failover execution. Target: 30-minute RTO. |

**DR exercises:** Quarterly failover drill (primary → secondary) with checklist and post-mortem. Results documented and reviewed in management review (PR-003).

### 12.4 Hybrid On-Premises (Future Phase)

- Cloud runs the primary Supabase stack and object storage
- On-premises runs a standby PostgreSQL replica and minimal portal cache for local availability
- On-premises is a **later phase** — do not introduce until baseline cloud deployment is stable and team has operational experience
- On-premises adds value when: (1) factory floor requires LAN-speed access to MRB data, (2) customers or regulations require on-premises data residency for specific projects

---

## 13. Customer Portal

### 13.1 Scope — Minimal Viable Portal (Phase 0–1)

The customer portal is built from Phase 0 as a separate application with limited scope:

| Feature | Phase 0 | Phase 1 | Phase 2+ |
|---------|---------|---------|----------|
| Login (email + password + MFA) | Yes | Yes | SSO option |
| View order list | Yes | Yes | Yes |
| View MRB status per order | Yes | Yes | Yes |
| Download released MRB (PDF) | — | Yes | Yes |
| Submit SDRL | — | — | Yes (IF-017) |
| Submit requirements profile | — | — | Yes (IF-018) |
| Real-time notifications | — | — | Yes |

### 13.2 Portal Security

- Separate Next.js application instance from internal QA UI
- Separate Supabase Auth policy (customer role, customer-scoped RLS)
- Rate limiting: 100 requests/minute per customer session
- All downloads logged in audit trail
- No access to internal validation details, correction requests, or internal notes

---

## 14. PDF/A Generation

### 14.1 Requirements

The MRB assembler (PR-012) must generate PDF/A-3 compliant packages:

| Requirement | Specification |
|-------------|--------------|
| **Standard** | ISO 19005-3:2012 (PDF/A-3) |
| **Structure** | Cover page → Master Document Index → Section dividers → Documents (each section) |
| **Bookmarks** | PDF bookmarks for each section and document |
| **Embedded originals** | Original source files embedded as attachments (PDF/A-3 feature) |
| **Page numbering** | Sequential across entire MRB package |
| **Searchable** | All text must be searchable (OCR for scanned documents) |
| **File size** | Optimized — target < 50 MB for typical MRB (compression, image optimization) |

### 14.2 Storage and Access Architecture

**Decision (2026-02-21, Fredrik Vangsal):** PDF/A storage and management uses Supabase Storage with database-driven structure and access control.

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Object storage** | Supabase Storage (AWS S3 backend, eu-north-1) | Physical storage of PDF/A-3 files and source artifacts |
| **Database structure** | PostgreSQL tables (`mrb.document_artifacts`) | Metadata, versioning, checksums, lifecycle state, retention dates |
| **Access control** | Supabase Storage RLS policies + signed URLs | Per-customer, per-order access enforcement |
| **Encryption** | AWS S3 SSE (AES-256) + Supabase Vault for signing keys | At-rest encryption, key management |

**Storage bucket structure:**

```
aurelian-mrb/
├── {customer_id}/
│   ├── {order_id}/
│   │   ├── source/           -- Uploaded source documents (certificates, reports)
│   │   ├── validated/        -- Post-validation copies with checksums
│   │   ├── mrb/              -- Assembled MRB package (PDF/A-3)
│   │   └── coc/              -- Signed CoC documents
│   └── profiles/             -- Customer requirement profiles
└── templates/                -- SDRL templates, MRB Index templates
```

**Access control rules:**
- Customer portal users: signed URLs with expiry, scoped to their `customer_id` bucket
- QA Engineers: full read/write to `source/` and `validated/`, read on `mrb/` and `coc/`
- Archive: `mrb/` and `coc/` become immutable after MRB release (no DELETE, no overwrite)
- All access logged to audit trail (PR-013)

### 14.3 PDF/A-3 Generation Library

Library selection is delegated to the development team for Phase 0 prototyping:

| Library | Language | License | PDF/A-3 Support | Notes |
|---------|----------|---------|-----------------|-------|
| **pdf-lib** | TypeScript/Node | MIT | Partial (needs extension) | Good for simple generation. May need supplementation for full PDF/A-3. |
| **PDFBox (Apache)** | Java | Apache 2.0 | Full | Proven for PDF/A. Requires Java runtime (microservice or serverless function). |
| **ReportLab** | Python | BSD | Full (with commercial license) | Proven. Python microservice for PDF generation. |
| **Gotenberg** | Go (Docker service) | MIT | Via LibreOffice/Chromium | Conversion service. Good for HTML → PDF/A. Containerized. |

**Recommended approach:** Evaluate Gotenberg (containerized, language-agnostic) for Phase 0 prototyping. If PDF/A-3 compliance requires deeper control, implement a dedicated PDF microservice using PDFBox or ReportLab. Final library selection after Phase 0 prototyping.

---

## 15. Deployment and Infrastructure

### 15.1 Environments

| Environment | Purpose | Data |
|-------------|---------|------|
| **Local (dev)** | Developer workstations | Synthetic seed data, Docker Compose |
| **Staging** | Integration testing, UAT, DR drills | Anonymized copy of production data (refreshed monthly) |
| **Production** | Live system | Real customer data |

### 15.2 Containerization

All services run as Docker containers orchestrated by Docker Compose (Phase 0–1) or Kubernetes (Phase 2+):

| Service | Container |
|---------|-----------|
| Supabase (PostgreSQL, Auth, Storage, PostgREST, Realtime) | Official Supabase self-hosted Docker images |
| Next.js application(s) | Custom Docker image (Node.js 20 LTS base) |
| MQTT Broker | Eclipse Mosquitto or EMQX |
| PDF Generator | Gotenberg / custom microservice |
| Grafana + Prometheus + Loki + Tempo | Official Docker images |

### 15.3 CI/CD Pipeline

```
Developer Push → GitHub Actions
                     │
              ┌──────┴──────┐
              │   Lint +     │
              │   Type Check │
              │   (TypeScript)│
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │  Unit Tests  │
              │  (Jest)      │
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │  Contract    │
              │  Tests       │
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │  SAST Scan   │
              │  (CodeQL)    │
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │  Build Docker│
              │  Images      │
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │  Deploy to   │
              │  Staging     │
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │  E2E Tests   │
              │  (Playwright)│
              └──────┬──────┘
                     │
              ┌──────┴──────────┐
              │  Manual Approval │
              │  → Deploy Prod   │
              └──────────────────┘
```

### 15.4 Hosting

**Decision (2026-02-21, Fredrik Vangsal): AWS (eu-north-1, Stockholm).**

| Property | Specification |
|----------|--------------|
| **Provider** | Amazon Web Services (AWS) |
| **Region** | eu-north-1 (Stockholm, Sweden) — EEA-compliant |
| **Compute** | EC2 or ECS (containerized) for Supabase stack |
| **Database** | Self-hosted PostgreSQL on EC2 (Supabase-managed) or Amazon RDS PostgreSQL |
| **Object storage** | Supabase Storage backed by Amazon S3 |
| **CDN** | CloudFront for customer portal static assets (Phase 2+) |
| **DNS** | Route 53 |
| **KMS** | Supabase Vault (Phase 0–1) → HashiCorp Vault (Phase 2+) |

**Rationale:** AWS provides the most mature ecosystem for the Supabase self-hosted stack. S3-native compatibility eliminates storage abstraction layers. eu-north-1 ensures EEA data sovereignty. AWS KMS and IAM provide enterprise-grade access control for ITAR-sensitive data when Defence customers are onboarded in Phase 0.5.

---

## 16. Phase Mapping — Component Build Sequence

### Phase 0 — Simulation & Build (Q2–Q4 2026) — Oil & Gas Primary

| Component | Deliverable |
|-----------|-------------|
| **Infrastructure** | Self-hosted Supabase deployed on AWS eu-north-1 (staging). Docker Compose setup for local dev. CI/CD pipeline. Supabase Vault for secret management. |
| **Data model** | Full entity model: ERP module entities (Customer, Supplier, PO, Production_Order, Inventory_Lot) + MRB Builder entities (Order, SDRL, MRB, MRB_Document, Material_Receipt, Gate_Review). RLS policies for basic roles. Separate schemas (`erp.*`, `mrb.*`). |
| **ERP module (MVP)** | Basic PO entry, customer/supplier CRUD, material lot tracking. Seed data tool for populating realistic Oil & Gas orders. |
| **Seed data tool** | `mrb-seed oilgas-norsok` — based on real SDRL data from Oil & Gas customers. Full lifecycle from PO receipt to MRB delivery. |
| **Material Gate** | PR-008 workflow: upload EN 10204 Type 3.1/3.2 certificate, 5-point check against NORSOK requirements, gate decision (APPROVED/REJECTED/CONDITIONAL_APPROVAL). |
| **SDRL Parser** | PR-009 workflow: upload Oil & Gas SDRL, parse 7-section structure, generate MRB Index, initialize document slots. |
| **Validation (L1–L3)** | PR-010 layers 1–3: existence check, format validation, completeness check against document type registry. Focus on Oil & Gas document types (EN 10204, dimensional reports, PMI, ITP records). |
| **Object storage** | Supabase Storage (AWS S3). Artifact upload, checksum generation, metadata storage. RLS-based access control per customer/order. |
| **Customer Portal** | Login + order list + MRB status view (no download yet). |
| **Observability** | Grafana + Prometheus + Loki deployed. Basic dashboards for system health. |

### Phase 0.5 — Integration & Testing (Q1–Q2 2027)

| Component | Deliverable |
|-----------|-------------|
| **ERP module expansion** | Production order management, basic scheduling, expanded inventory tracking. Internal module integration fully tested with real data flows. |
| **Defence templates** | 8-section MRB structure (AS9100/AQAP), FAIR templates, Defence CoC template added alongside Oil & Gas. |
| **Machine data** | MQTT broker deployed on-premises. First CNC data ingestion from MAZAK machines (Q2 2027 delivery). Canonical event schema validated with real data. |
| **Validation (L4–L5)** | Compliance checking (numeric range validation, unit conversion, borderline detection). Traceability chain verification. |
| **CoC generation** | PR-011 workflow: prerequisite gate check, template population, signature workflow. |
| **MRB assembly** | PR-012 workflow: index finalization, PDF/A-3 generation (prototype), 10-point quality check, release. |
| **DR drills** | First failover exercise. Measure actual RPO/RTO. |
| **UAT** | QA engineers test full lifecycle with realistic data. |

### Phase 1 — Production MVP (Q3 2027)

| Component | Deliverable |
|-----------|-------------|
| **Go-live** | First real MRBs produced and shipped with products. |
| **Customer portal** | MRB download enabled for first customers. |
| **All Phase 1 interfaces** | IF-001 through IF-012 live with ERP. |
| **Archive** | PR-013: active archive operational. Checksum verification. Backup tested. |
| **Monitoring** | SLO dashboards. Alerting for validation failures, system errors. |

### Phase 2 — Intelligent (Q1–Q3 2028)

| Component | Deliverable |
|-----------|-------------|
| **AI-assisted validation** | L4 compliance rules augmented with ML-based anomaly detection on material certificates. |
| **Electronic signatures** | PKI-based PDF signing for CoCs. |
| **Customer portal extended** | SDRL submission (IF-017), requirement profile input (IF-018), real-time notifications. |
| **GraphQL API** | Customer-facing read API for MRB views. |
| **Extended interfaces** | IF-013 through IF-020 live. |
| **Enterprise SSO** | WorkOS or Entra ID integration via auth adapter. |

### Phase 3 — Autonomous (2029+)

| Component | Deliverable |
|-----------|-------------|
| **Zero-touch MRB** | Repeat orders processed without manual intervention. |
| **Digital twin** | MRB data feeds digital twin model. |
| **Multi-site** | Support for multiple manufacturing locations. |
| **Hybrid on-prem** | On-premises standby deployment. |
| **Event bus** | Full event-driven architecture for all integrations. |

---

## 17. Open Decisions and Resolved Decisions

### 17.1 Resolved Decisions

The following decisions have been made by the founding team:

| # | Decision | Resolution | Date | Impact |
|---|----------|-----------|------|--------|
| R1 | **ERP strategy** | **Build own ERP module** as part of unified Aurelian Platform. No third-party ERP purchase. | 2026-02-21 | Fundamental — eliminates external integration overhead. AM-IF-001 becomes internal module boundaries. Architecture updated throughout this document. |
| R2 | **Industry priority for Phase 0** | **Oil & Gas first.** Real SDRL data from O&G customers will be available within weeks. Defence (AQAP/AS9100) follows as secondary priority. | 2026-02-21 | Phase 0 simulation starts with NORSOK/API 7-section MRB structure, ITP hold points, EN 10204 Type 3.2 certificates. Defence templates built in parallel or shortly after. |
| R3 | **Phase 0 simulation data** | **Real SDRLs** from Oil & Gas customers will be obtained. Includes full PO documentation — from receipt of PO with all technical and commercial requirements through to delivery. | 2026-02-21 | Eliminates the need for synthetic SDRL generation. Real edge cases and customer-specific requirements will be captured from day one. |
| R4 | **PDF/A-3 generation library** | **Technical decision — delegated to development team.** Will be prototyped during Phase 0. Not a business decision. | 2026-02-21 | Dev team evaluates Gotenberg, PDFBox, or ReportLab during early Phase 0 and selects based on PDF/A-3 compliance testing. |
| R5 | **Cloud hosting provider** | **AWS (eu-north-1, Stockholm).** Mature ecosystem, native S3 compatibility for Supabase Storage, EEA-compliant. | 2026-02-21 | Sections 6.1, 12.2, 15.4 updated. Deployment scripts target AWS. Cost model based on EC2/S3/RDS pricing. |
| R6 | **PDF/A storage and access** | **Supabase Storage** (backed by AWS S3) with PostgreSQL-driven structure and RLS-based access control. | 2026-02-21 | Section 14 updated. Storage bucket structure defined. Access control via Supabase Storage RLS + signed URLs. |
| R7 | **KMS and secret management** | **Phased approach:** Supabase Vault (built-in `pgsodium`) for Phase 0–1. Migration to **HashiCorp Vault** planned for Phase 2+ when multi-tenant Defence data and ITAR classification handling are required. | 2026-02-21 | Section 8.4 updated. No additional infrastructure needed for Phase 0. Vault migration planned as part of Defence onboarding. |
| R8 | **SDRL data storage model** | **Relational.** SDRL line items stored as individual rows in `mrb.sdrl_line_item` table with typed columns (ENUMs for review_code, criticality, data_source, required_format, submission_timing). SDRLs are structurally predictable across orders — limited practical variation makes JSONB unnecessary. | 2026-02-21 | Data model updated: new SDRL_Line_Item entity added. MRB_Document entity extended with matching fields. Consistency issue #3 from cross-document audit resolved. Aligns AM-TS-001 with AM-CT-001 field definitions. |
| R9 | **E-signature methodology** | **Custom internal PKI e-signature** with full audit trail. BankID available as optional add-on for Norwegian customers who require it. Custom approach ensures international customer compatibility — cannot rely on a Norway-only identity provider for global defence/O&G customers. | 2026-02-21 | CoC entity updated with signature_hash and signature_method ENUM (INTERNAL_PKI/BANKID/MANUAL). Phase 0 uses MANUAL approval. Phase 0.5 implements INTERNAL_PKI. BankID integration evaluated for Phase 2+ based on customer demand. |
| R10 | **Data model expansion (AM-FM-001)** | **16 new entities added** to the MRB Builder module based on form template design. Covers physical inspection, material traceability detail, ITP tracking, cross-document verification, CoC prerequisite gates, CoC revision history, authorized signatories, MRB assembly/quality/delivery workflow, and archive disposition. Total entity count: 36 (6 ERP + 30 MRB). 27 ENUM types formalized. | 2026-02-21 | Section 7.2 extended with new entity table. Section 7.5 added (ENUM Type Registry). AM-FM-001 added to References. Data model now covers the full form lifecycle from FM-008-01 through FM-013-05. |

### 17.2 Open Decisions

The following item requires further discussion but does not block Phase 0 start:

| # | Question | Context | Needed By | Impact |
|---|----------|---------|-----------|--------|
| F4 | **ERP module architecture depth** | Now that we are building our own ERP: How deep should the ERP module go in Phase 0–1? Minimum viable (PO + inventory + supplier list) or broader (quoting, scheduling, finance)? Fredrik's tech stack plan assumed a bought ERP — this changes the scope significantly. | Before Phase 0 start | Affects development scope, team sizing, and timeline. Critical input needed. |

### 17.3 Decision Timeline

| Decision | Blocking? | Needed By |
|----------|-----------|-----------|
| F4 (ERP scope) | **Partially** — affects team planning | Before Phase 0 sprint planning |

---

## 18. Verification and Test Strategy

### 18.1 Procedure Coverage Verification

Before Phase 0 development is considered complete, every section of every procedure SHALL have a corresponding system capability:

| Procedure | Key Sections to Verify |
|-----------|----------------------|
| PR-008 | 5-point certificate check executes correctly. Material Requirement Profile lookup works. Gate decision recorded and synced to ERP (IF-005). |
| PR-009 | SDRL upload and parsing generates correct MRB Index. Industry classification (Defence vs Oil & Gas) determines correct section template. Order state machine transitions correctly. |
| PR-010 | All 5 validation layers execute in sequence. Correction Request generated on failure. Cross-document traceability chain verified. CoC prerequisite gate blocks CoC generation when documents are not validated. |
| PR-011 | CoC generated only after prerequisite gate passes. Industry-specific template used. Authorized signatory check enforced. CoC register maintained. |
| PR-012 | MRB assembly blocked until all documents validated and CoC signed. PDF/A-3 generated with bookmarks and embedded originals. 10-point quality check executed. Release authorization recorded. |
| PR-013 | Archive record created on MRB release. Checksum verified. Retention period calculated and stored. Active → Deep archive transition works. Disposition requires authorization. |

### 18.2 Module Boundary Tests

All 20 internal module boundaries (AM-IF-001) SHALL have automated tests that verify:

- Cross-schema views return correct data
- Database functions enforce correct data contracts
- State machine accepts transitions in the expected sequence
- Module isolation is maintained (ERP module cannot directly access MRB tables, and vice versa)
- Event propagation (NOTIFY/LISTEN) triggers correct downstream actions

### 18.3 Security Verification

- RLS policies tested: attempt cross-tenant data access (must fail)
- Audit log verified: all security-relevant events captured
- ITAR document access: attempt access without clearance attribute (must fail)
- Token expiry: verify expired JWTs are rejected
- Rate limiting: verify portal rate limits enforce

### 18.4 Recovery Verification

- Monthly restore test: PostgreSQL + object storage restored in staging. SHA-256 checksums verified for sample of artifacts.
- Quarterly DR drill: full failover to secondary region. Measure actual RTO/RPO. Document results.

---

*This specification is a living document. It will be updated as technology decisions are finalized and Phase 0 development progresses. All changes follow the document control process defined in PR-001.*

*Key architectural decisions (2026-02-21): Aurelian builds own ERP module as part of unified platform. AM-IF-001 interfaces become internal module boundaries. Oil & Gas is primary Phase 0 industry, with Defence following. AWS eu-north-1 for hosting. Supabase Storage for PDF/A management. Supabase Vault → HashiCorp Vault for KMS.*

*Companion documents: PR-008 through PR-013 (procedures) · AM-IF-001 (internal module boundary spec) · QM-001 Rev 2 Addendum · MRB Builder Tech Stack Plan (F. Vangsal)*
