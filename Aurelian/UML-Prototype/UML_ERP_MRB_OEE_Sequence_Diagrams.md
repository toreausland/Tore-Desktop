# UML Sequence Diagrams -- ERP <-> MRB Builder <-> OEE-A

**Aurelian Manufacturing AS**

Complete order lifecycle interface mapping based on AM-IF-001 (20 original interfaces + 8 OEE-A interfaces), PR-008 through PR-013, OEE-A automated integration, and ISA-95 Level 0--5+ architecture. Including industry-specific flows for Defence (AS9100/AQAP) and Oil & Gas (NORSOK/API).

**Document Reference:** AM-IF-001 | AM-TS-001 | PR-008--PR-013 | OEE-A Research

**CONFIDENTIAL -- 28 February 2026**

---

## 1. Full Order Lifecycle -- ERP <-> MRB Builder <-> OEE-A Sequence (Extended)

This diagram traces a single customer order from PO receipt through MRB archival, showing all 20 original interface events (IF-001 through IF-020), the 7-stage MRB pipeline, ISA-95 Level 3/Level 4 boundary, and the **NEW OEE-A integration** (MES/OEE participant, IF-021 through IF-028). Green elements indicate OEE-A additions.

### Participants

| Participant | Role |
|---|---|
| **CUSTOMER** | External party submitting POs and receiving MRB documentation |
| **ERP SYSTEM** | ISA-95 Level 4 enterprise backbone (finance, purchasing, production orders, inventory, HR, calibration, supplier approval) |
| **MRB BUILDER** | ISA-95 Level 3 digital quality layer (Aurelian-built) -- manages the 7-stage MRB pipeline |
| **MES / OEE** | NEW -- MES OEE Engine for automated OEE data processing (OEE-A addition) |
| **SHOP FLOOR** | ISA-95 Level 2/1/0 -- CNC machines, CMM, metrology, inspection |
| **SUPPLIER** | External material and certificate providers |

### Stage 0 -- Order Initiation

| Interface | Message | Details |
|---|---|---|
| -- | Purchase Order | Customer submits PO with SDRL requirements to ERP |
| **IF-001** | `purchase_order.confirmed` | ERP -> MRB: PO number, customer, industry_classification, order_lines |
| -- | (return) | MRB assigns mrb_number, state -> PARSING |
| **IF-002** | `document.attached` (SDRL) | ERP -> MRB: SDRL document_type, download_url, revision |

**Note:** PR-009: Parse SDRL -> Order Requirement Matrix + MRB Index.

**NEW (OEE-A):** ERP sends OEE production order parameters to MES/OEE -- ideal_cycle_time, planned_runtime, target_qty.

### Stage 1 -- Material Gate (PR-008)

| Interface | Message | Details |
|---|---|---|
| **IF-012** | `customer.requirements_update` | ERP -> MRB: governing_standards, material_profiles, chemical_overrides |
| **IF-019** | Supplier cert submission | Supplier -> ERP: Material certificate uploaded to ERP |
| **IF-003** | `goods_receipt.completed` | ERP -> MRB: receipt_number, heat_number, lot, target_orders[] |
| **IF-004** | `certificate.attached` | ERP -> MRB: EN 10204 type, download_url, heat_number |

**Material Gate -- 5-point check:**
1. Existence
2. Format
3. Completeness
4. Compliance
5. Traceability

| Interface | Message | Details |
|---|---|---|
| **IF-014** | GET supplier approval status | MRB -> ERP (return): Supplier approval check |
| **IF-005** | `material_gate.decision` | MRB -> ERP: APPROVED / REJECTED / CONDITIONAL per order |

### Stage 2 -- Production & Document Collection (PR-009 SS6.7) + OEE Data

| Interface | Message | Details |
|---|---|---|
| **IF-006** | `production_order.material_issued` | ERP -> MRB: prod_order, serial_range, machines_assigned[] |
| **IF-008** | `order_state` -> COLLECTING | MRB -> ERP: State transition |

**LOOP [production duration] -- Shop Floor -> MRB Builder:**
- CNC inline data (MQTT/OPC-UA): Dimensional, tool wear, cycle times
- CMM / inspection reports: Surface roughness, hardness
- Metrology / environmental data: Temperature, vibration monitoring

> **ISA-95 Level 3 -> MRB:** Machine data bypasses ERP. Direct MQTT / OPC-UA connection.

**NEW -- OEE LOOP [continuous] -- Shop Floor -> MES/OEE:**

| Interface | Message | Details |
|---|---|---|
| **IF-021** | OPC UA Machine.Status | Running / Idle / Fault |
| **IF-021** | CycleTime & PartCount | Cycle-level production data |
| **IF-021** | StopEvent | stop_reason, duration_seconds |
| **IF-021** | QualityResult | GOOD / SCRAP |

**OEE Calculation:** A x P x Q (Availability x Performance x Quality)

| Interface | Message | Details |
|---|---|---|
| **IF-022** | Production confirm (B2MML) | MES -> ERP: completed_qty, good_qty, scrap_qty |

**Supplier documents:** Supplier submits NDT reports, sub-supplier certs -> ERP -> MRB via IF-004. One cert may serve many orders (ERP manages 1:N linkage).

### Stage 3 -- 5-Layer Document Validation (PR-010)

**5-Layer Validation Engine:**
- **L1** -- Existence check
- **L2** -- Format validation (PDF/A, structure)
- **L3** -- Completeness (all fields present)
- **L4** -- Compliance (values vs specification)
- **L5** -- Traceability (cross-document links)

| Interface | Message | Details |
|---|---|---|
| **IF-013** | GET calibration status | MRB -> ERP: instrument_id -> CURRENT / EXPIRED |
| **IF-015** | GET employee qualifications | MRB -> ERP: inspector NDT level, cert expiry |

**ALT [failure]:**

| Interface | Message | Details |
|---|---|---|
| **IF-007** | `ncr.created` (bidirectional) | NCR number, severity, disposition_required |

**NEW -- ALT [OEE scrap_rate > threshold]:**

| Interface | Message | Details |
|---|---|---|
| **IF-024** | OEE-triggered NCR | MES -> ERP -> MRB: Automated NCR from OEE quality component |

| Interface | Message | Details |
|---|---|---|
| **IF-008** | `order_state` -> VALIDATING | MRB -> ERP: State transition |

### Stage 3b -- Industry-Specific Validation Branch

#### ALT [industry_classification = DEFENCE]

**DEFENCE -- FAIR (AS9102):**
- Generate Form 1 (Part), Form 2 (Material), Form 3 (Characteristics)
- Link to CNC data
- AQAP 2110 compliance check, ECCN export control
- MRB: 8 sections, 25 line items
- EN 10204 Type 3.2 required
- Retention: 30 years
- Signature authority: LEVEL_2 minimum

#### ALT [industry_classification = OIL_GAS]

**OIL & GAS -- ITP Management:**
- Hold (H), Witness (W), Review (R), Surveillance (S) points
- Customer notification 48-72h for Witness Points
- NORSOK M-630/M-650, API compliance check
- ITP Witness/Hold Point notification to Customer (attendance required at Hold Points)
- MRB: 7 sections, 30 line items
- EN 10204 Type 3.1/3.2 accepted

### Stage 4 -- Certificate of Conformance (PR-011)

| Interface | Message | Details |
|---|---|---|
| **IF-008** | `order_state` -> COC_PENDING | MRB -> ERP: State transition |

**CoC Generation (PR-011):**
- Industry-specific template (Defence / Oil & Gas)
- Query all NCR dispositions for deviation declaration
- Signature authority: LEVEL_1 / LEVEL_2 / LEVEL_3

| Interface | Message | Details |
|---|---|---|
| **IF-010** | `coc.registered` | MRB -> ERP: coc_number, signed_by, authority_level, deviations_declared |
| **IF-008** | `order_state` -> COC_SIGNED | MRB -> ERP: State transition |

### Stage 5 -- MRB Assembly & Release (PR-012)

**MRB Assembly -- 10-point quality check:**

1. MRB Index complete
2. All docs validated
3. CoC signed
4. Cover page generated
5. Bookmarks inserted
6. NCR dispositions closed
7. Traceability matrix verified
8. Page numbering correct
9. PDF/A-3 compiled
10. SHA-256 checksum

| Interface | Message | Details |
|---|---|---|
| **IF-009** | `mrb.released` | MRB -> ERP: mrb_number, document_count, total_pages, PDF/A package |
| **IF-008** | `order_state` -> READY | MRB -> ERP: State transition |

ERP notifies Customer: Order documentation complete -- ready for shipment.

### Stage 6 -- Shipment & Delivery

| Interface | Message | Details |
|---|---|---|
| **IF-011** | `shipment.dispatched` | ERP -> MRB: shipment_number, tracking, physical_mrb_included |
| **IF-011** | `mrb.delivered` (electronic) | MRB -> ERP: delivery_method: CUSTOMER_PORTAL |
| **IF-016** | Customer MRB Delivery | MRB -> Customer: Customer downloads MRB, CoC via portal |
| **IF-008** | `order_state` -> SHIPPED | MRB -> ERP: State transition |

Customer returns: recipient_confirmed: true.

### Stage 7 -- Archival (PR-013)

| Interface | Message | Details |
|---|---|---|
| **IF-020** | `mrb.archived` | MRB -> ERP: archive_location, retention_expiry, checksum_sha256 |
| **IF-008** | `order_state` -> ARCHIVED | MRB -> ERP: State transition |
| **IF-026** | OEE shift summary archived (NEW) | MES -> ERP: Historical KPIs: A, P, Q per machine per shift |

**Archival Tiers (PR-013):**
- ACTIVE archive: 2 years (hot storage)
- DEEP archive: long-term (WORM storage)
  - Defence: 30 years
  - Oil & Gas: 25 years
- SHA-256 integrity verification

### Key Architecture Principles

> **Key architecture principle:** Machine data (CNC, CMM, metrology) flows directly from ISA-95 Level 3 to the MRB Builder via MQTT/OPC-UA -- bypassing the ERP entirely. Supplier documents route through ERP because one certificate may serve multiple orders (1:N allocation managed by ERP).

> **OEE-A integration principle:** OEE data streams (IF-021) flow from Shop Floor through Edge Gateway to the MES/OEE Engine. Production confirmations (IF-022) and quality feedback (IF-024) flow from MES to ERP. Scrap detection above threshold automatically triggers NCR creation in the MRB Builder via ERP.

---

## 2. Industry-Specific Branching -- Defence vs Oil & Gas

The MRB Builder handles both industries through a single pipeline with industry-specific branching at three critical control points: SDRL parsing (MRB template selection), validation (FAIR vs ITP), and CoC generation (template + signature authority).

### Participants

| Participant | Role |
|---|---|
| **ERP** | Enterprise resource planning system |
| **SDRL PARSER** | Parses supplier document requirements list and classifies industry |
| **DEFENCE PATH** | Defence-specific processing (AS9100/AQAP) |
| **OIL & GAS PATH** | Oil & Gas-specific processing (NORSOK/API) |
| **MRB ASSEMBLER** | Final MRB package assembly |

### Branch 1 -- SDRL Classification

IF-001 + IF-002 (PO + SDRL) arrive at SDRL Parser, which classifies the industry:
- AS9100 / AQAP -> **DEFENCE**
- NORSOK / API -> **OIL & GAS**

**Defence path:** Initialize 8-section MRB template, 25 line items, FAIR required.

**Oil & Gas path:** Initialize 7-section MRB template, 30 line items, ITP required.

#### Defence MRB (8 sections)
1. Identification & Index
2. Contract Documentation
3. Material Documentation
4. Manufacturing Process
5. Special Processes
6. Inspection (incl. FAIR)
7. Testing
8. Compliance Declarations

#### Oil & Gas MRB (7 sections)
1. General Information & ITP
2. Purchase & Technical
3. Material Documentation
4. Manufacturing Records
5. Testing & Inspection
6. Compliance Documentation
7. Preservation & Shipping

### Branch 2 -- Industry-Specific Validation

#### FAIR -- First Article Inspection (Defence)

AS9102 Forms 1, 2, 3:
- **Form 1:** Part Number Accountability
- **Form 2:** Material/Special Process
- **Form 3:** Characteristic Accountability

Triggered by:
- First production of part
- Design change
- Process/supplier change
- 2+ year production gap

#### ITP -- Inspection & Test Plan (Oil & Gas)

Hold / Witness / Review / Surveillance points:
- **(H) Hold Point:** Production STOPS. Customer must attend.
- **(W) Witness Point:** 48-72h customer notification.
- **(R) Review Point:** Documentation review only.
- **(S) Surveillance Point:** Random verification.

### Branch 3 -- Certificate & Compliance Requirements

| Aspect | Defence | Oil & Gas |
|---|---|---|
| EN 10204 Type | 3.2 (mandatory) | 3.1 or 3.2 |
| Standards | AS9100, AQAP 2110 | NORSOK, API, ASME |
| Export | ECCN classification required | Not applicable |
| Signature | LEVEL_2 minimum | Per ITP authority |
| CoC template | Defence (AS9100/AQAP) | Oil & Gas (NORSOK/API) |
| Special | MIL-STD, STANAG, DEF-STAN | DNV approval, MDS required |
| Retention | 30 years | 25 years |

### Branch 4 -- CoC Generation & MRB Assembly

- Defence CoC (AS9100/AQAP template): AQAP deviation declarations, ECCN compliance statement -> MRB Assembler
- Oil & Gas CoC (NORSOK/API template): NORSOK compliance statement, ITP completion sign-off -> MRB Assembler

Both paths converge at the MRB Assembler:
- MRB Assembly (PR-012): 10-point quality check, PDF/A-3 compilation + SHA-256
- IF-009 `mrb.released` -> ERP (same event structure regardless of industry -- classification tag included)

### Defence Summary

| Property | Value |
|---|---|
| Standards | AS9100, AQAP 2110, MIL-STD, STANAG, DEF-STAN |
| MRB Template | 8 sections, 25 line items |
| Key Document | FAIR (AS9102 Forms 1/2/3) |
| Certificate | EN 10204 Type 3.2 (mandatory) |
| Signature | LEVEL_2 minimum authority |
| Export | ECCN classification required |
| Retention | 30 years (WORM storage) |
| CoC Template | Defence (AS9100/AQAP) |
| Special Req | AQAP compliance, NATO codification |
| Trigger | First article, design change, supplier change, 2yr gap |

### Oil & Gas Summary

| Property | Value |
|---|---|
| Standards | NORSOK M-630/M-650, API, ASME, DNV |
| MRB Template | 7 sections, 30 line items |
| Key Document | ITP (Hold / Witness / Review points) |
| Certificate | EN 10204 Type 3.1 or 3.2 (flexible) |
| Signature | Per ITP authority definition |
| PMI Policy | Mandatory per NORSOK (Positive Material ID) |
| Retention | 25 years (WORM storage) |
| CoC Template | Oil & Gas (NORSOK/API) |
| Special Req | DNV approval, MDS (Material Data Sheet) |
| Trigger | ITP Hold Points stop production, Witness Points notify 48-72h |

---

## 3. ISA-95 Architecture -- ERP / MRB / MES OEE / Shop Floor (Extended to Level 5+)

Extended ISA-95 architecture showing Level 0 through Level 5+ with OEE-A MES Engine, Edge Gateway layer (Level 2.5), and Cloud/BI Analytics. Based on Siemens Industry 4.0 research, AM-TS-001, RAMI 4.0 (DIN SPEC 91345), and OEE-A Research.

### Level 5+ -- Cloud / BI Analytics (NEW)

- Cross-enterprise OEE benchmarks
- AI/ML predictive maintenance
- Long-term data warehouse
- Protocols: REST API, Cloud storage, Data lake (Parquet/Delta)

### Level 4 -- Enterprise Logistics

**ERP System** (ISA-95 Level 4 enterprise backbone):
- Finance & Costing
- Purchasing / SCM
- Production Orders
- Inventory / Lot Tracking
- CRM / Sales
- HR / Qualifications
- Calibration Records
- Supplier Approval
- Document Management (material certs, supplier docs)
- OEE Quality Feedback: NCR triggered by scrap detection

**External interfaces:**
- **Customers** (KDA, Equinor, TechnipFMC): PO + SDRL submission
- **Suppliers** (Sandvik, Outokumpu): Material certs -> ERP

### Level 3 -- Manufacturing Operations

**MRB Builder** (Aurelian-built, Digital Quality Layer):

| Module | Procedure |
|---|---|
| MATERIAL GATE | PR-008 |
| SDRL PARSER | PR-009 |
| VALIDATOR | PR-010 |
| CoC ENGINE | PR-011 |
| ASSEMBLER | PR-012 |
| ARCHIVE | PR-013 |

API Layer: AM-IF-001 -- 20 interfaces (bidirectional with ERP via Level 3/4 boundary).

**MES OEE Engine** (NEW -- Automated OEE Data Processing):

| Module | Function |
|---|---|
| OEE CALCULATOR | A x P x Q |
| DOWNTIME TRACKER | Stop event categorisation |
| QUALITY MONITOR | Good/scrap/rework tracking |
| DASHBOARD SERVER | Real-time KPI display |
| ORDER DISPATCH | Production order management |

Protocols: REST API, MQTT subscriber, B2MML/XML, WebSocket.

MES to ERP interfaces: IF-022 through IF-028.

### Level 2.5 -- Edge Gateway (NEW)

- OPC UA Client
- Data filtering & noise reduction
- Local buffering
- Pre-aggregation

Data flows upward:
- MQTT / REST -> MES OEE Engine
- MQTT / OPC-UA -> MRB Builder

### Level 2/1/0 -- Control & Sensors (Shop Floor)

| Equipment | Type | Protocol |
|---|---|---|
| CNC Machines | MAZAK (5-axis) | OPC-UA / MTConnect |
| CMM / Metrology | Zeiss Contura | Direct integration |
| Inspection Room | Hardness, surface, visual | MQTT events |

Protocols: MQTT, OPC-UA, MTConnect.

Real-time data: dimensional, tool wear, cycle times, temperature, vibration.

Machine data flows to Edge Gateway, then to MRB Builder + MES OEE Engine.

### Key Architecture Decisions

1. Machine data -> Edge -> MRB + MES (not ERP)
2. OEE calc at Level 3 (MES), KPIs to Level 4
3. Edge Gateway for noise reduction + buffering

---

## 4. OEE-A Data Flow Sequence (NEW)

This diagram shows the complete OEE-A specific data lifecycle from CNC machine sensors through Edge Gateway processing, MES OEE calculation, ERP integration, quality feedback to MRB, predictive maintenance alerts, and shift reporting. All elements in this diagram are new OEE-A additions.

### Participants

| Participant | Role |
|---|---|
| **CNC MACHINE** | Shop floor equipment generating raw sensor data |
| **EDGE GATEWAY** | Intermediate filtering and buffering layer (Level 2.5) |
| **MES (OEE ENGINE)** | OEE calculation and data processing engine |
| **ERP SYSTEM** | Enterprise backbone for production tracking |
| **MRB BUILDER** | Quality documentation system |
| **CLOUD / BI** | Long-term analytics and AI/ML training |

### Phase 1 -- Data Collection (IF-021)

**OEE STREAM loop [continuous] -- CNC Machine -> Edge Gateway:**

| Signal | Data |
|---|---|
| OPC UA: Machine.Status | Running / Idle / Fault / Setup |
| OPC UA: CycleTime + PartCount | Per-cycle production metrics |
| OPC UA: StopEvent | stop_reason, duration_seconds |
| OPC UA: QualityResult | GOOD / SCRAP / REWORK |

### Phase 2 -- Edge Processing

**Edge Gateway Processing:**
- Filter noise
- Buffer data locally
- Pre-aggregate per cycle
- Forward to MES

Edge Gateway -> MES: REST/MQTT filtered OEE data (pre-aggregated cycle records).

### Phase 3 -- OEE Calculation

**OEE Calculation Engine:**
- A = actual_run_time / planned_time
- P = (ideal_cycle x total_count) / actual_run
- Q = good_count / total_count
- **OEE = A x P x Q** (real-time update)

**IF-027 Dashboard Push:** WebSocket real-time KPIs to dashboard server.

### Phase 4 -- ERP Integration (IF-022, IF-023)

| Interface | Message | Details |
|---|---|---|
| **IF-022** | Production confirmation (B2MML) | MES -> ERP: completed_qty, good_qty, scrap_qty, cycle_data |
| **IF-023** | OEE KPI Summary (daily) | MES -> ERP: machine_id, OEE%, availability%, performance%, quality% |

ACK: KPI stored in ERP production module.

### Phase 5 -- Quality Feedback (IF-024)

**ALT [scrap_rate > threshold]:**

| Interface | Message | Details |
|---|---|---|
| **IF-024** | OEE scrap threshold breach | MES -> ERP: Scrap rate exceeded configured threshold |
| **IF-007** | `ncr.created` (OEE-triggered) | ERP -> MRB: Auto-NCR with scrap_rate, machine_id, affected_orders[] |

MRB Builder links NCR to active MRB packages and re-validates affected documents.

### Phase 6 -- Predictive Maintenance (IF-025)

| Interface | Message | Details |
|---|---|---|
| **IF-025** | Predictive maintenance alert | MES -> ERP: tool_wear_index, vibration_anomaly, predicted_failure_window |
| **IF-028** | Tool wear + vibration data -> Cloud | MES -> Cloud/BI: Historical ML training data for prediction models |

ERP response: Schedule maintenance, create work order, reserve parts, notify production planner.

### Phase 7 -- Shift Reporting (IF-026, IF-028)

**Shift Aggregation:** Per machine -> per line -> plant OEE. Top losses, Pareto analysis.

| Interface | Message | Details |
|---|---|---|
| **IF-026** | Shift report -> ERP | MES -> ERP: shift_id, machine_oee[], line_oee, plant_oee, top_losses[] |
| **IF-028** | Historical archive -> Cloud/BI | MES -> Cloud/BI: Long-term OEE trends, benchmarking data |

> **OEE-A key insight:** The seven phases above form a closed loop: raw sensor data is collected, filtered at the edge, calculated into OEE KPIs, fed back to ERP for production tracking, triggers quality actions in MRB when thresholds are breached, drives predictive maintenance, and archives to cloud for long-term analytics and AI/ML model training.

---

## 5. Interface Register -- All 28 Interfaces (20 Original + 8 OEE-A)

### Original Interfaces (IF-001 through IF-020)

| IF-ID | Name | Direction | Trigger | Procedure | Stage |
|---|---|---|---|---|---|
| **IF-001** | New Purchase Order | ERP -> MRB | PO confirmed | PR-009 | 0 |
| **IF-002** | SDRL Attachment | ERP -> MRB | SDRL attached to PO | PR-009 | 0 |
| **IF-003** | Goods Receiving Notification | ERP -> MRB | Material received | PR-008 | 1 |
| **IF-004** | Material Certificate Attached | ERP -> MRB | Cert attached to receipt | PR-008 | 1 |
| **IF-005** | Material Gate Decision | MRB -> ERP | Gate review completed | PR-008 | 1 |
| **IF-006** | Production Order Link | ERP -> MRB | Prod order created | PR-009 | 2 |
| **IF-007** | NCR Created / Updated | Bidirectional | NCR raised | PR-004/010 | 3 |
| **IF-008** | Order State Update | MRB -> ERP | State transition | PR-009 | All |
| **IF-009** | MRB Completion | MRB -> ERP | MRB released | PR-012 | 5 |
| **IF-010** | CoC Registered | MRB -> ERP | CoC signed | PR-011 | 4 |
| **IF-011** | Shipment Release | Bidirectional | Dispatch confirmed | PR-012 | 6 |
| **IF-012** | Customer Requirement Profile | ERP -> MRB | Customer onboarded | PR-008 | 1 |
| **IF-013** | Calibration Status Query | MRB -> ERP | L5 validation | PR-010 | 3 |
| **IF-014** | Supplier Approval Status | MRB -> ERP | Material gate check | PR-008 | 1 |
| **IF-015** | Employee Qualification | MRB -> ERP | L4/L5 validation | PR-010/011 | 3--4 |
| **IF-016** | Customer MRB Delivery | MRB -> Cust | MRB released | PR-012 | 6 |
| **IF-017** | Customer SDRL Submission | Cust -> MRB | PO submitted | PR-009 | 0 |
| **IF-018** | Customer Requirement Profile | Cust -> MRB | Profile update | PR-008 | 1 |
| **IF-019** | Supplier Cert Submission | Supp -> ERP | Material shipped | PR-008 | 1 |
| **IF-020** | Archive Metadata Sync | MRB -> ERP | Order archived | PR-013 | 7 |

### OEE-A Interfaces (IF-021 through IF-028) -- NEW

| IF-ID | Name | Direction | Trigger | Procedure | Stage |
|---|---|---|---|---|---|
| **IF-021** | OEE Data Stream | Shop -> MES via Edge | Continuous (OPC UA) | OEE-A | 2 |
| **IF-022** | Production Confirmation | MES -> ERP | Cycle complete | OEE-A / B2MML | 2 |
| **IF-023** | OEE KPI Summary | MES -> ERP | Daily aggregate | OEE-A | 2 |
| **IF-024** | OEE-triggered NCR | MES -> ERP -> MRB | Scrap threshold breach | OEE-A / PR-004 | 3 |
| **IF-025** | Predictive Maintenance Alert | MES -> ERP | Failure prediction | OEE-A | 2 |
| **IF-026** | Shift Report | MES -> ERP | Shift end | OEE-A | 7 |
| **IF-027** | Dashboard Push | MES -> Dashboard | Real-time update | OEE-A | 2 |
| **IF-028** | Cloud Analytics Export | MES -> Cloud/BI | Historical archive | OEE-A | 7 |

---

## 6. Industry Comparison -- Defence vs Oil & Gas

### What Differs Between Industries?

The core ERP <-> MRB pipeline is identical for both industries. The same 20 interfaces, the same 7-stage pipeline, and the same 5-layer validation engine apply. However, the **content** within each stage differs significantly at four branching points.

| Aspect | Defence | Oil & Gas | Impact on Sequence |
|---|---|---|---|
| Governing Standards | AS9100, AQAP 2110, MIL-STD, STANAG, DEF-STAN | NORSOK M-630/M-650, API, ASME, DNV | Determines which validation rules are applied at L4 (Compliance) |
| MRB Template | 8 sections, 25 line items | 7 sections, 30 line items | Different MRB Index generated from SDRL at Stage 0 |
| Key Quality Document | FAIR (AS9102 Forms 1/2/3) | ITP (Hold/Witness/Review points) | Defence: additional document slots in Section 6. Oil & Gas: production stops at Hold Points, customer notifications for Witness Points |
| Certificate Type | EN 10204 Type 3.2 (mandatory) | EN 10204 Type 3.1 or 3.2 | Material Gate (PR-008) applies stricter acceptance for Defence -- may REJECT cert type 3.1 |
| Signature Authority | LEVEL_2 minimum | Per ITP authority definition | IF-015 Employee Qualification query validates different authority thresholds |
| Export Controls | ECCN classification required | Not applicable | Defence: additional compliance check in CoC (PR-011) -- ECCN statement |
| PMI Requirement | Per contract specification | Mandatory per NORSOK | Oil & Gas: PMI report always required in MRB Section 3 |
| CoC Template | Defence (AS9100/AQAP) | Oil & Gas (NORSOK/API) | Different CoC document generated at Stage 4 -- different deviation declaration format |
| Preservation & Shipping | Embedded in MRB Section 8 (if required) | Dedicated MRB Section 7 | Oil & Gas: separate preservation records, packing spec, transport docs |
| Retention Period | 30 years (WORM) | 25 years (WORM) | Different retention_expiry in IF-020 archive metadata |
| Customer Interaction | FAIR approval cycle, design review | ITP Hold/Witness attendance, 48-72h notification | Oil & Gas: more real-time customer involvement during production |

### What Stays the Same?

> **Shared pipeline infrastructure:** All 20 ERP <-> MRB interfaces (AM-IF-001) are used by both industries. The 7-stage pipeline (Material Gate -> SDRL Parse -> Collect -> Validate -> CoC -> Assemble -> Archive) is identical. The 5-layer validation engine (L1-L5) runs for both. The technology stack (PostgreSQL, Supabase, Next.js, MQTT/OPC-UA) is shared. The ISA-95 Level 3/4 boundary is the same. Only the *content* -- templates, rules, standards, and thresholds -- differs. The OEE-A integration (IF-021 through IF-028) applies equally to both industries.

### Defence (AS9100/AQAP) Characteristics

- Product traceability to individual serial numbers
- First Article Inspection for new/changed parts
- Export control compliance (ECCN/ITAR)
- Stricter certificate requirements (Type 3.2)
- Longer retention (30 years for audit trail)
- NATO codification may apply
- Customer approval cycle for FAIR

**Typical customers:** Kongsberg Defence & Aerospace, Nammo, Saab, BAE Systems

### Oil & Gas (NORSOK/API) Characteristics

- Material traceability to heat/lot numbers
- ITP with Hold/Witness/Review points
- Mandatory PMI (Positive Material Identification)
- Preservation & shipping documentation
- DNV/Bureau Veritas third-party involvement
- NORSOK M-630/M-650 material standards
- Real-time customer involvement at Hold Points

**Typical customers:** Equinor, TechnipFMC, Aker Solutions, Nordic Subsea Solutions

---

## 7. References

| Document ID | Document |
|---|---|
| AM-IF-001 | ERP <-> MRB Builder Interface Specification (20 interfaces) |
| AM-TS-001 | IT System Technical Specification (technology stack, architecture) |
| AM-FM-001 | Form Templates (24 quality forms, ENUM registry) |
| PR-008 | Incoming Material Review and Release (Material Gate) |
| PR-009 | SDRL Processing and MRB Management |
| PR-010 | Document Validation and Verification (5-layer engine) |
| PR-011 | Certificate of Conformance |
| PR-012 | MRB Assembly and Release |
| PR-013 | Document Archival and Retention |
| -- | ERP-Industri4.0-grundig-research-rapport (Siemens / Fraunhofer analysis) |
| -- | MRB_Simulation (NSS-PO-2026-0042, NSS-SDRL-2026-0042, 19 MRB documents) |
| OEE-A Research (NEW) | OEE-A Research Report (Aurelian internal -- automated OEE architecture) |
| DIN SPEC 91345 (NEW) | RAMI 4.0 -- Reference Architecture Model Industrie 4.0 |
| IEC 62541 (NEW) | OPC Unified Architecture |
| VDI 5600 (NEW) | Manufacturing Execution Systems (MES) |
| IEC 62443 (NEW) | Industrial communication networks -- IT security |
| B2MML (NEW) | Business To Manufacturing Markup Language (ISA-95 XML schema) |

---

CONFIDENTIAL -- Aurelian Manufacturing AS -- 28 February 2026
UML Sequence Diagrams: ERP <-> MRB Builder <-> OEE-A Integrated Architecture
