# ERP ↔ MRB BUILDER INTERFACE SPECIFICATION

| Field | Value |
|-------|-------|
| **Document No.** | AM-IF-001 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-19 |
| **Approved By** | Technical Lead / Quality Manager |
| **Classification** | Internal — Engineering |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | 2026-02-19 | Technical Lead | Initial Release |

---

## 1. Purpose

This document defines every data exchange between the Aurelian Manufacturing ERP system and the Aurelian-built Digital MRB Builder. It is ERP-agnostic — the interfaces are defined as contracts that any ERP with API capabilities must satisfy.

This specification serves as the binding agreement between:

- **The ERP** — the operational backbone handling finance, purchasing, production orders, inventory, HR, CRM, and supplier/customer management
- **The MRB Builder** — the Aurelian-developed digital layer handling SDRL parsing, material gate review, document validation, CoC generation, MRB assembly, and archival

## 2. Architecture Principle

```
                    EXTERNAL SYSTEMS
                    ────────────────
    CUSTOMERS ←──API──┐          ┌──API──→ SUPPLIERS
                      │          │
                      ▼          ▼
               ┌──────────────────────┐
               │                      │
               │    ERP SYSTEM        │
               │    (Bought)          │
               │                      │
               │  Finance             │
               │  Purchasing / SCM    │
               │  Production Orders   │
               │  Inventory / Lots    │
               │  CRM / Sales         │
               │  HR / Payroll        │
               │  Document Mgmt      │
               │  Quality Module      │
               │  Compliance          │
               │                      │
               └──────────┬───────────┘
                          │
                   API LAYER (this document)
                   REST / Webhooks / Event Bus
                          │
               ┌──────────┴───────────┐
               │                      │
               │  MRB BUILDER         │
               │  (Aurelian-built)    │
               │                      │
               │  Material Gate       │
               │  SDRL Parser         │
               │  Doc Validator       │
               │  CoC Generator       │
               │  MRB Assembler       │
               │  Archive Engine      │
               │  Customer Portal     │
               │  Dashboards          │
               │                      │
               └──────────┬───────────┘
                          │
                   DIRECT INTEGRATION
                   MQTT / OPC-UA / MTConnect
                          │
              ┌───────────┼───────────┐
              │           │           │
         CNC MACHINES  METROLOGY  INSPECTION
         (MAZAK)       (CMM)      ROOM
```

### 2.1 Core Design Rules

| Rule | Description |
|------|-------------|
| **Single source of truth** | Each data object has ONE authoritative system. No duplication. |
| **ERP owns business data** | POs, inventory, customer records, supplier records, production orders, finance — all live in ERP. |
| **MRB Builder owns quality documentation** | MRB Index, validation status, gate decisions, CoC generation, MRB packages — all live in MRB Builder. |
| **Shared documents live in ERP** | Material certs, supplier docs that may serve multiple orders — stored in ERP document management. MRB Builder references them, does not copy them. |
| **Order-specific documents live in MRB Builder** | CNC data, inspection reports, FAIR forms, CoCs, assembled MRBs — stored in MRB Builder. |
| **Machine data bypasses ERP** | CNC, metrology, and inspection room data flows directly to MRB Builder. ERP does not mediate machine data. |
| **API-first** | All integrations use documented APIs. No database-level coupling. No shared file folders as a permanent interface (acceptable only in Phase 1 MVP). |
| **Event-driven where possible** | Systems notify each other of state changes via webhooks or event bus. Polling is a fallback, not the design target. |

---

## 3. Interface Register

### 3.1 Summary of All Interfaces

| IF-ID | Name | Direction | Trigger | Simulation (Ph 0) | Live From |
|-------|------|-----------|---------|-------------------|-----------|
| **IF-001** | New Purchase Order | ERP → MRB | PO created/confirmed | ✓ Simulated | Phase 1 |
| **IF-002** | SDRL Attachment | ERP → MRB | SDRL document attached to PO | ✓ Simulated | Phase 1 |
| **IF-003** | Goods Receiving Notification | ERP → MRB | Material received and booked | ✓ Simulated | Phase 1 |
| **IF-004** | Material Certificate Attached | ERP → MRB | Supplier cert attached to receipt | ✓ Simulated | Phase 1 |
| **IF-005** | Material Gate Decision | MRB → ERP | Gate review completed | ✓ Simulated | Phase 1 |
| **IF-006** | Production Order Link | ERP → MRB | Production order created / material issued | ✓ Simulated | Phase 1 |
| **IF-007** | NCR Created / Updated | Bidirectional | NCR raised in either system | — | Phase 1 |
| **IF-008** | Order State Update | MRB → ERP | Order progresses through MRB lifecycle | ✓ Internal | Phase 1 |
| **IF-009** | MRB Completion Notification | MRB → ERP | MRB assembled and released | ✓ Dry run | Phase 1 |
| **IF-010** | CoC Registered | MRB → ERP | CoC signed and registered | ✓ Dry run | Phase 1 |
| **IF-011** | Shipment Release | Bidirectional | Product + MRB ready for dispatch | — | Phase 1 |
| **IF-012** | Customer Requirement Profile | ERP → MRB | Customer-specific material requirements | ✓ Samples | Phase 1 |
| **IF-013** | Calibration Status Query | MRB → ERP | Validator checks instrument calibration | ✓ Mock | Phase 2 |
| **IF-014** | Supplier Approval Status | MRB → ERP | Material gate checks approved supplier list | ✓ Mock | Phase 2 |
| **IF-015** | Employee Qualification Query | MRB → ERP | Validator checks inspector/operator qualifications | — | Phase 2 |
| **IF-016** | Customer Portal — MRB Delivery | MRB → Customer | Customer downloads MRB/CoC | — | Phase 2 |
| **IF-017** | Customer Portal — SDRL Submission | Customer → MRB | Customer submits SDRL electronically | — | Phase 2 |
| **IF-018** | Customer Portal — Requirement Profile | Customer → MRB | Customer provides material requirements via API | — | Phase 2 |
| **IF-019** | Supplier Portal — Certificate Submission | Supplier → ERP | Supplier submits certs digitally | — | Phase 2 |
| **IF-020** | Archive Metadata Sync | MRB → ERP | Archived MRB metadata synced to ERP for record | ✓ Mock | Phase 2 |

---

## 4. Interface Specifications

### IF-001: New Purchase Order

**Purpose:** When a new customer PO is created in the ERP, the MRB Builder is notified to begin the SDRL/MRB lifecycle.

| Field | Value |
|-------|-------|
| Direction | ERP → MRB Builder |
| Trigger | PO status changes to CONFIRMED (or equivalent) |
| Method | Webhook (ERP fires event) or REST POST from ERP to MRB |
| Frequency | Per event (each new PO) |
| Procedure | PR-009 (SDRL Processing) |

**Payload:**

```json
{
  "event": "purchase_order.confirmed",
  "timestamp": "2027-08-15T09:23:00Z",
  "data": {
    "po_number": "PO-2027-001",
    "customer": {
      "id": "CUST-KDA",
      "name": "Kongsberg Defence & Aerospace",
      "industry_classification": "DEFENCE"
    },
    "order_lines": [
      {
        "line": 1,
        "part_number": "AM-1001",
        "part_name": "Precision Housing",
        "drawing_number": "DWG-1001",
        "drawing_revision": "C",
        "material_spec": "AMS 4078 (7075-T651)",
        "quantity": 50,
        "delivery_date": "2027-11-15"
      }
    ],
    "contract_reference": "KDA-FW-2027-042",
    "sdrl_attached": true,
    "sdrl_document_id": "DOC-ERP-2027-08421",
    "special_requirements": [
      "AQAP 2110 applies",
      "FAIR required (first production)",
      "Export control: ECCN 9A010"
    ]
  }
}
```

**MRB Builder response:**

```json
{
  "status": "accepted",
  "mrb_number": "AM-MRB-2027-00001",
  "order_state": "PARSING",
  "message": "Order registered. SDRL parsing initiated."
}
```

---

### IF-002: SDRL Attachment

**Purpose:** Delivers the actual SDRL document to the MRB Builder for parsing.

| Field | Value |
|-------|-------|
| Direction | ERP → MRB Builder |
| Trigger | SDRL document attached to PO in ERP document management |
| Method | Webhook with document reference, or document API pull |
| Frequency | Per event (once per PO, may update if SDRL revised) |
| Procedure | PR-009 (SDRL Processing) |

**Payload:**

```json
{
  "event": "document.attached",
  "timestamp": "2027-08-15T09:25:00Z",
  "data": {
    "po_number": "PO-2027-001",
    "document": {
      "erp_document_id": "DOC-ERP-2027-08421",
      "document_type": "SDRL",
      "filename": "KDA-SDRL-FW-2027-042.pdf",
      "format": "PDF",
      "size_bytes": 245780,
      "revision": "A",
      "download_url": "/api/v1/documents/DOC-ERP-2027-08421/content"
    }
  }
}
```

**MRB Builder action:** Downloads the SDRL from ERP document management, parses it per PR-009, generates the Order Requirement Matrix and MRB Index.

---

### IF-003: Goods Receiving Notification

**Purpose:** When material arrives and is booked into ERP inventory, the MRB Builder is notified to initiate the Material Gate review (PR-008).

| Field | Value |
|-------|-------|
| Direction | ERP → MRB Builder |
| Trigger | Goods receipt completed in ERP |
| Method | Webhook |
| Frequency | Per goods receipt |
| Procedure | PR-008 (Incoming Material Review and Release) |

**Payload:**

```json
{
  "event": "goods_receipt.completed",
  "timestamp": "2027-09-01T14:30:00Z",
  "data": {
    "receipt_number": "GR-2027-00421",
    "purchase_order": "SUP-PO-2027-0089",
    "supplier": {
      "id": "SUP-SANDVIK",
      "name": "Sandvik Materials Technology"
    },
    "material": {
      "grade": "ASTM A182 F316L",
      "form": "Round bar",
      "dimensions": "dia. 150mm x 3000mm",
      "heat_number": "H-42891",
      "lot_number": "LOT-2027-0891",
      "quantity": 12,
      "unit": "bars",
      "weight_kg": 2400
    },
    "target_orders": [
      { "po_number": "PO-2027-003", "quantity": 6 },
      { "po_number": "PO-2027-007", "quantity": 4 },
      { "allocation": "STOCK", "quantity": 2 }
    ],
    "certificate_attached": true,
    "certificate_document_id": "DOC-ERP-2027-09102"
  }
}
```

---

### IF-004: Material Certificate Attached

**Purpose:** Delivers the material certificate to the MRB Builder for parsing and gate review.

| Field | Value |
|-------|-------|
| Direction | ERP → MRB Builder |
| Trigger | Supplier certificate attached to goods receipt or PO in ERP |
| Method | Webhook with document reference |
| Frequency | Per certificate attachment |
| Procedure | PR-008 (Material Gate) |

**Payload:**

```json
{
  "event": "certificate.attached",
  "timestamp": "2027-09-01T14:32:00Z",
  "data": {
    "receipt_number": "GR-2027-00421",
    "heat_number": "H-42891",
    "certificate": {
      "erp_document_id": "DOC-ERP-2027-09102",
      "type": "EN_10204_3_1",
      "supplier_cert_number": "SMT-2027-84521",
      "filename": "Sandvik_H-42891_3.1_cert.pdf",
      "download_url": "/api/v1/documents/DOC-ERP-2027-09102/content"
    }
  }
}
```

**MRB Builder action:** Downloads the certificate, parses it (chemical, mechanical, supplementary tests, signatures), identifies which customer profiles to validate against based on target orders from IF-003.

---

### IF-005: Material Gate Decision

**Purpose:** Returns the gate decision to ERP so inventory status is updated and material is released, quarantined, or held.

| Field | Value |
|-------|-------|
| Direction | MRB Builder → ERP |
| Trigger | Material Gate review completed (PR-008) |
| Method | REST POST to ERP API |
| Frequency | Per material/order combination reviewed |
| Procedure | PR-008 (Material Gate) |

**Payload:**

```json
{
  "event": "material_gate.decision",
  "timestamp": "2027-09-01T15:10:00Z",
  "data": {
    "gate_reference": "MG-2027-00042",
    "receipt_number": "GR-2027-00421",
    "heat_number": "H-42891",
    "decisions": [
      {
        "target_order": "PO-2027-003",
        "customer": "Equinor",
        "profile_used": "PROF-EQN-F316L-NORSOK",
        "decision": "REJECTED",
        "reason": "Certificate type 3.1 does not meet requirement for 3.2",
        "borderline_flags": ["P at 0.023% vs limit 0.025% (8% margin)"],
        "action_required": "Request EN 10204 Type 3.2 certificate from Sandvik",
        "erp_material_status": "QUARANTINED"
      },
      {
        "target_order": "PO-2027-007",
        "customer": "TechnipFMC",
        "profile_used": "PROF-TFMC-F316L-STD",
        "decision": "RELEASED",
        "reason": "All checks passed",
        "borderline_flags": [],
        "action_required": null,
        "erp_material_status": "QC_APPROVED",
        "mrb_prestage": {
          "mrb_number": "AM-MRB-2027-00007",
          "mrb_section": "3",
          "document_slot": "3.1"
        }
      },
      {
        "target_order": null,
        "allocation": "STOCK",
        "decision": "RELEASED_TO_STOCK",
        "reason": "Meets base specification ASTM A182",
        "note": "Must re-validate against customer profile when allocated to order",
        "erp_material_status": "QC_APPROVED_STOCK"
      }
    ]
  }
}
```

**ERP action required:**
- Update material lot status per `erp_material_status`
- Block quarantined material from production allocation
- Create supplier non-conformance record for REJECTED decisions
- Notify Purchasing for corrective action

---

### IF-006: Production Order Link

**Purpose:** When a production order is created in ERP and material is issued, the MRB Builder is notified to link production data to the correct MRB.

| Field | Value |
|-------|-------|
| Direction | ERP → MRB Builder |
| Trigger | Production order created and material issued |
| Method | Webhook |
| Frequency | Per production order |
| Procedure | PR-009 (MRB Management) |

**Payload:**

```json
{
  "event": "production_order.material_issued",
  "timestamp": "2027-09-05T08:00:00Z",
  "data": {
    "production_order": "PROD-2027-00031",
    "customer_po": "PO-2027-007",
    "mrb_number": "AM-MRB-2027-00007",
    "part_number": "AM-2005",
    "part_name": "Pump Housing",
    "drawing_number": "DWG-2005",
    "drawing_revision": "B",
    "quantity": 25,
    "serial_range": { "from": "SN-2027-00101", "to": "SN-2027-00125" },
    "material_issued": [
      {
        "lot_number": "LOT-2027-0891",
        "heat_number": "H-42891",
        "quantity": 4,
        "unit": "bars",
        "gate_reference": "MG-2027-00042"
      }
    ],
    "machines_assigned": ["MAZAK-001", "MAZAK-003"],
    "scheduled_start": "2027-09-08",
    "scheduled_end": "2027-09-22"
  }
}
```

**MRB Builder action:**
- Link production order to MRB
- Register serial number range for traceability
- Expect CNC data tagged with this production order from machine data gateway
- Update MRB dashboard with production schedule

---

### IF-007: NCR Created / Updated

**Purpose:** Bidirectional synchronization of Non-Conformance Reports. NCRs may originate in either system but must be visible in both.

| Field | Value |
|-------|-------|
| Direction | Bidirectional |
| Trigger | NCR created or disposition updated |
| Method | REST POST (both directions) |
| Frequency | Per NCR event |
| Procedure | PR-004 (NCR/CAPA), PR-010 (Validation), PR-011 (CoC) |

**ERP → MRB (NCR created in ERP):**

```json
{
  "event": "ncr.created",
  "data": {
    "ncr_number": "NCR-2027-00015",
    "source": "ERP",
    "related_order": "PO-2027-007",
    "part_number": "AM-2005",
    "serial_numbers": ["SN-2027-00108", "SN-2027-00112"],
    "description": "Dimensional out-of-tolerance on bore diameter",
    "disposition": "PENDING",
    "severity": "MAJOR"
  }
}
```

**MRB → ERP (NCR created in MRB Builder):**

```json
{
  "event": "ncr.created",
  "data": {
    "ncr_number": "NCR-2027-00016",
    "source": "MRB_BUILDER",
    "related_order": "PO-2027-003",
    "description": "Material certificate traceability break: heat number on cert does not match goods receiving record",
    "disposition": "PENDING",
    "severity": "CRITICAL"
  }
}
```

**Disposition sync (both directions):**

```json
{
  "event": "ncr.disposition_updated",
  "data": {
    "ncr_number": "NCR-2027-00015",
    "disposition": "USE_AS_IS",
    "customer_approval_ref": "KDA-DEV-2027-042-01",
    "customer_approved": true,
    "note": "Customer accepted deviation within extended tolerance"
  }
}
```

**Critical for CoC:** PR-011 queries all NCRs for an order before generating the CoC. All "USE_AS_IS" and "REPAIR" dispositions MUST appear on the CoC deviation section.

---

### IF-008: Order State Update

**Purpose:** The MRB Builder notifies the ERP of order state transitions so production planning and customer-facing systems reflect documentation status.

| Field | Value |
|-------|-------|
| Direction | MRB Builder → ERP |
| Trigger | Order state changes in MRB lifecycle |
| Method | Webhook / REST POST |
| Frequency | Per state change |
| Procedure | PR-009 (Order Lifecycle) |

**Payload:**

```json
{
  "event": "order_state.changed",
  "timestamp": "2027-10-01T16:45:00Z",
  "data": {
    "po_number": "PO-2027-007",
    "mrb_number": "AM-MRB-2027-00007",
    "previous_state": "VALIDATING",
    "new_state": "COC_PENDING",
    "message": "All documents validated. Ready for CoC generation.",
    "mrb_completion_pct": 95,
    "blocking_items": []
  }
}
```

**State values:** NEW, PARSING, ACTIVE, COLLECTING, VALIDATING, COC_PENDING, MRB_ASSEMBLY, READY, SHIPPED, ARCHIVED

**ERP use:** Update order status visible to sales/CRM. Notify Commercial Manager when order reaches READY. Prevent shipping department from dispatching if state is not READY.

---

### IF-009: MRB Completion Notification

**Purpose:** Final notification that the MRB is assembled, released, and ready for shipment.

| Field | Value |
|-------|-------|
| Direction | MRB Builder → ERP |
| Trigger | MRB released (order state = READY) |
| Method | REST POST |
| Frequency | Once per order |
| Procedure | PR-012 (MRB Assembly and Release) |

**Payload:**

```json
{
  "event": "mrb.released",
  "timestamp": "2027-10-05T11:00:00Z",
  "data": {
    "po_number": "PO-2027-007",
    "mrb_number": "AM-MRB-2027-00007",
    "coc_number": "AM-COC-2027-00007",
    "customer": "TechnipFMC",
    "classification": "OIL_GAS",
    "document_count": 28,
    "total_pages": 142,
    "delivery_formats": ["PDF_A", "STRUCTURED_FOLDER"],
    "mrb_download_url": "/api/v1/mrb/AM-MRB-2027-00007/package",
    "released_by": "QA Engineer Name",
    "release_type": "STANDARD"
  }
}
```

**ERP action:** Mark order as documentation-complete. Enable shipment dispatch. Update CRM with delivery readiness.

---

### IF-010: CoC Registered

**Purpose:** Registers the signed CoC in the ERP's certificate register for audit trail and financial linkage.

| Field | Value |
|-------|-------|
| Direction | MRB Builder → ERP |
| Trigger | CoC signed and registered (PR-011) |
| Method | REST POST |
| Frequency | Once per CoC |
| Procedure | PR-011 (Certificate of Conformance) |

**Payload:**

```json
{
  "event": "coc.registered",
  "timestamp": "2027-10-04T14:30:00Z",
  "data": {
    "coc_number": "AM-COC-2027-00007",
    "po_number": "PO-2027-007",
    "mrb_number": "AM-MRB-2027-00007",
    "signed_by": "Quality Manager Name",
    "authority_level": "LEVEL_1",
    "deviations_declared": false,
    "coc_document_url": "/api/v1/documents/coc/AM-COC-2027-00007",
    "classification": "OIL_GAS"
  }
}
```

---

### IF-011: Shipment Release

**Purpose:** Bidirectional coordination of physical shipment with documentation delivery.

| Field | Value |
|-------|-------|
| Direction | Bidirectional |
| Trigger | Shipment dispatch confirmed |
| Method | REST POST (both directions) |
| Frequency | Per shipment |
| Procedure | PR-012 (MRB Delivery) |

**ERP → MRB (Shipment dispatched):**

```json
{
  "event": "shipment.dispatched",
  "data": {
    "shipment_number": "SHIP-2027-00089",
    "po_number": "PO-2027-007",
    "shipping_date": "2027-10-06",
    "courier": "DHL Express",
    "tracking_number": "DHL-1234567890",
    "physical_mrb_included": true
  }
}
```

**MRB → ERP (Electronic MRB delivered):**

```json
{
  "event": "mrb.delivered",
  "data": {
    "mrb_number": "AM-MRB-2027-00007",
    "delivery_method": "CUSTOMER_PORTAL",
    "delivery_timestamp": "2027-10-06T09:15:00Z",
    "recipient_confirmed": true
  }
}
```

**MRB Builder action:** Update order state READY → SHIPPED. Initiate archival process (PR-013).

---

### IF-012: Customer Requirement Profile

**Purpose:** Customer-specific material acceptance criteria are managed as profiles. ERP is the master for customer data; MRB Builder is the master for the profile content.

| Field | Value |
|-------|-------|
| Direction | ERP → MRB Builder (customer context), MRB → ERP (profile status) |
| Trigger | New customer onboarded, PO with special requirements |
| Method | REST API |
| Frequency | Per customer/material combination |
| Procedure | PR-008 (Material Requirement Profiles) |

**ERP → MRB (Customer context for profile creation):**

```json
{
  "event": "customer.requirements_update",
  "data": {
    "customer_id": "CUST-EQN",
    "customer_name": "Equinor ASA",
    "governing_standards": ["NORSOK M-630", "NORSOK M-650"],
    "approved_suppliers": ["Sandvik", "Outokumpu", "Vallourec"],
    "default_cert_type": "3.2",
    "pmi_policy": "MANDATORY",
    "material_profiles": [
      {
        "material_spec": "ASTM A182 F316L",
        "profile_id": "PROF-EQN-F316L-NORSOK",
        "chemical_overrides": {
          "P": { "max": 0.025 },
          "S": { "max": 0.015 },
          "N": { "min": 0.04, "max": 0.10 }
        },
        "mechanical_overrides": {
          "impact_test": { "temperature_c": -46, "min_average_j": 45 }
        },
        "supplementary_tests_required": ["IGC_A262_E"]
      }
    ]
  }
}
```

---

### IF-013: Calibration Status Query

**Purpose:** MRB Builder (PR-010 validation) checks whether inspection instruments referenced in reports have current calibration.

| Field | Value |
|-------|-------|
| Direction | MRB Builder → ERP (query/response) |
| Trigger | During document validation (L5 traceability) |
| Method | REST GET |
| Frequency | Per instrument referenced in a report |
| Procedure | PR-010 (Document Validation) |

**Request:**

```
GET /api/v1/calibration/status?instrument_id=CMM-001&date=2027-10-01
```

**Response:**

```json
{
  "instrument_id": "CMM-001",
  "description": "Zeiss Contura CMM",
  "calibration_status": "CURRENT",
  "last_calibration_date": "2027-07-15",
  "next_calibration_due": "2028-01-15",
  "calibration_cert_ref": "CAL-2027-CMM001-042"
}
```

---

### IF-014: Supplier Approval Status

**Purpose:** Material Gate (PR-008) checks whether a material supplier is on the customer's approved supplier list.

| Field | Value |
|-------|-------|
| Direction | MRB Builder → ERP (query/response) |
| Trigger | During material gate review |
| Method | REST GET |
| Frequency | Per supplier/customer combination |
| Procedure | PR-008 (Material Gate) |

**Request:**

```
GET /api/v1/suppliers/SUP-SANDVIK/approval?customer_id=CUST-EQN
```

**Response:**

```json
{
  "supplier_id": "SUP-SANDVIK",
  "supplier_name": "Sandvik Materials Technology",
  "customer_id": "CUST-EQN",
  "approved": true,
  "approval_scope": "All stainless steel and nickel alloys",
  "approval_date": "2025-03-15",
  "approval_expiry": "2028-03-14",
  "qualification_ref": "EQN-ASL-2025-SANDVIK"
}
```

---

### IF-015: Employee Qualification Query

**Purpose:** MRB Builder validates that inspectors, NDT technicians, and signatories referenced in documents are qualified.

| Field | Value |
|-------|-------|
| Direction | MRB Builder → ERP (query/response) |
| Trigger | During document validation (L4/L5) and CoC signature |
| Method | REST GET |
| Frequency | Per person referenced |
| Procedure | PR-010 (Validation), PR-011 (CoC Signature Authority) |

**Request:**

```
GET /api/v1/employees/EMP-042/qualifications?type=NDT_UT_LEVEL_II
```

**Response:**

```json
{
  "employee_id": "EMP-042",
  "name": "Inspector Name",
  "qualification": "NDT_UT_LEVEL_II",
  "status": "CURRENT",
  "cert_number": "PCN-UT-2-042891",
  "expiry_date": "2028-06-30",
  "issuing_body": "PCN (BINDT)"
}
```

---

### IF-016 to IF-018: Customer Portal Interfaces

These interfaces connect the MRB Builder's customer portal directly to external customers. They do NOT go through the ERP.

| IF-ID | Name | Direction | Description |
|-------|------|-----------|-------------|
| IF-016 | MRB Delivery | MRB → Customer | Customer downloads completed MRB, CoC, individual documents |
| IF-017 | SDRL Submission | Customer → MRB | Customer submits SDRL electronically at PO time |
| IF-018 | Requirement Profile | Customer → MRB | Customer provides/updates material requirements via API |

These are the customer-facing APIs described in the `aurelian-material-gate` skill Section 8. They follow the tiered model:

| Tier | Method | Phase |
|------|--------|-------|
| Tier 1 (Kongsberg, Equinor, Aker) | REST API | Phase 3 |
| Tier 2 (Nammo, Saab, BAE) | Structured Excel/web form | Phase 2 |
| Tier 3 (smaller customers) | PO parsing by MRB Builder | Phase 1 |

---

### IF-019: Supplier Portal — Certificate Submission

**Purpose:** Suppliers submit material certificates digitally, feeding directly into ERP document management.

| Field | Value |
|-------|-------|
| Direction | Supplier → ERP |
| Trigger | Supplier ships material / completes goods receipt |
| Method | Supplier portal upload or API |
| Phase | Phase 2 |

This interface feeds INTO the ERP, which then triggers IF-004 (certificate attached) to the MRB Builder.

---

### IF-020: Archive Metadata Sync

**Purpose:** When the MRB Builder archives an order (PR-013), it syncs the archive metadata to ERP for cross-system retrievability.

| Field | Value |
|-------|-------|
| Direction | MRB Builder → ERP |
| Trigger | Order archived |
| Method | REST POST |
| Frequency | Once per archived order |
| Procedure | PR-013 (Archival) |

**Payload:**

```json
{
  "event": "mrb.archived",
  "data": {
    "mrb_number": "AM-MRB-2027-00007",
    "coc_number": "AM-COC-2027-00007",
    "po_number": "PO-2027-007",
    "customer": "TechnipFMC",
    "archived_date": "2027-10-10",
    "retention_expiry": "2042-10-10",
    "archive_location": "ACTIVE_ARCHIVE/2027/AM-MRB-2027-00007",
    "checksum_sha256": "a1b2c3d4e5f6...",
    "total_pages": 142
  }
}
```

---

## 5. Data Ownership Matrix

| Data Object | Owner (Source of Truth) | Consumer | Interface |
|-------------|------------------------|----------|-----------|
| Purchase Order | ERP | MRB Builder | IF-001 |
| Customer master data | ERP | MRB Builder | IF-001, IF-012 |
| Supplier master data | ERP | MRB Builder | IF-003, IF-014 |
| Inventory / material lots | ERP | MRB Builder | IF-003 |
| Material certificates (files) | ERP (document mgmt) | MRB Builder | IF-004 |
| Material lot status (QC) | **Bidirectional** | Both | IF-005 (MRB sets status, ERP enforces) |
| Production orders | ERP | MRB Builder | IF-006 |
| NCRs / CAPAs | **Bidirectional** | Both | IF-007 |
| SDRL (parsed) | MRB Builder | ERP (status only) | IF-002 |
| MRB Index | MRB Builder | — | Internal to MRB |
| Document validation status | MRB Builder | ERP (order state) | IF-008 |
| CoC | MRB Builder | ERP (register) | IF-010 |
| MRB package | MRB Builder | ERP (notification), Customer | IF-009, IF-016 |
| Order state | MRB Builder | ERP | IF-008 |
| Calibration records | ERP | MRB Builder | IF-013 |
| Employee qualifications | ERP (HR module) | MRB Builder | IF-015 |
| Approved supplier list | ERP | MRB Builder | IF-014 |
| Customer requirement profiles | **MRB Builder** (content) / ERP (customer context) | Both | IF-012 |
| Archive records | MRB Builder | ERP (metadata) | IF-020 |
| CNC machine data | MRB Builder (direct) | — | Not ERP (MQTT/OPC-UA) |
| CMM inspection data | MRB Builder (direct) | — | Not ERP (direct integration) |
| Metrology/environmental data | MRB Builder (direct) | — | Not ERP (direct integration) |

---

## 6. Technical Requirements

### 6.1 API Standards

| Requirement | Specification |
|-------------|---------------|
| Protocol | REST over HTTPS (TLS 1.2 minimum) |
| Data format | JSON (UTF-8) |
| Authentication | API key (Phase 1-2), OAuth 2.0 (Phase 3), Mutual TLS (defence customers) |
| Rate limiting | Configurable per endpoint — minimum 100 req/min for event-driven interfaces |
| Versioning | URL-based versioning: `/api/v1/`, `/api/v2/` |
| Error handling | Standard HTTP status codes + structured error response body |
| Retry policy | Exponential backoff, max 3 retries for transient failures |
| Idempotency | All POST/PUT operations must support idempotency keys |
| Logging | All API calls logged with timestamp, source, payload hash, response code |

### 6.2 Event Bus (Target Architecture)

For Phase 3+ when event volume increases:

| Requirement | Specification |
|-------------|---------------|
| Technology | Message queue (RabbitMQ, Azure Service Bus, or similar) |
| Pattern | Publish/subscribe for state change events |
| Delivery guarantee | At-least-once delivery |
| Message ordering | Per-order ordering guaranteed |
| Dead letter queue | Failed messages retained for investigation |
| Monitoring | Queue depth, processing latency, error rate dashboards |

### 6.3 Security

| Requirement | Specification |
|-------------|---------------|
| Encryption in transit | TLS 1.2+ for all API calls |
| Encryption at rest | AES-256 for all stored documents |
| Access control | Role-based — only authorized systems/services can call each endpoint |
| Audit trail | Every API call logged: who, when, what, from where |
| Customer data isolation | Each customer's data (profiles, MRBs, certs) logically isolated |
| Defence data | AQAP-applicable data subject to additional handling per contract |

### 6.4 Availability and Performance

| Requirement | Target |
|-------------|--------|
| API availability | 99.5% (production hours) |
| Webhook delivery latency | < 5 seconds from trigger event |
| Query response time | < 500ms for single-record queries (IF-013, IF-014, IF-015) |
| Document download | < 10 seconds for documents up to 50 MB |
| Batch operations | Support for bulk queries (e.g., all NCRs for an order) |

---

## 7. Phase Alignment

The MRB Builder development starts in Q2 2026 with simulation, progresses through integration testing, and delivers a production-ready system by Q3 2027. Each interface matures across five phases.

| Interface | Phase 0 (Q2–Q4 2026) Simulation | Phase 0.5 (Q1–Q2 2027) Integration | Phase 1 (Q3 2027) Production MVP | Phase 2 (Q1–Q3 2028) Intelligent | Phase 3 (2029+) Autonomous |
|-----------|--------------------------------|-------------------------------------|----------------------------------|----------------------------------|---------------------------|
| IF-001 PO | Simulated PO payloads | ERP test connection | Manual / file-based | API | API + event bus |
| IF-002 SDRL | Mock SDRL documents | ERP document pull test | Manual upload / API pull | API + AI parsing | Autonomous |
| IF-003 Goods Receiving | Simulated receipts | ERP webhook test | Webhook | Webhook | Event bus |
| IF-004 Certificate | Mock certificates | Download pipeline test | Webhook + download | Webhook + download | Supplier portal → auto |
| IF-005 Gate Decision | Simulated decisions | ERP status update test | API POST | API POST | Autonomous |
| IF-006 Prod Order | Simulated orders | ERP webhook test | Webhook | Webhook | Event bus |
| IF-007 NCR | N/A | Sync protocol test | Separate systems | API sync | Real-time sync |
| IF-008 Order State | Internal state machine | Dashboard prototype | Dashboard + API POST | API POST | Event bus |
| IF-009 MRB Complete | Mock MRB assembly | End-to-end dry run | Email notification | API POST | Event bus |
| IF-010 CoC Register | Mock CoC generation | CoC template testing | Manual entry | API POST | Autonomous |
| IF-011 Shipment | N/A | N/A | Manual coordination | API (both) | Integrated |
| IF-012 Customer Profile | Sample profiles | Profile validation test | Excel/manual | API + customer portal | Customer self-service |
| IF-013 Calibration | Mock calibration data | ERP query test | Manual check | API query | Automated |
| IF-014 Supplier Approval | Mock supplier list | ERP query test | Manual check | API query | Automated |
| IF-015 Qualification | N/A | N/A | Manual check | API query | Automated |
| IF-016-018 Customer | N/A | N/A | Email/manual | Portal + API (pilot) | Full portal + API |
| IF-019 Supplier | N/A | N/A | Email | Portal upload | Supplier API |
| IF-020 Archive | Mock archive writes | Archive integrity test | File-based | API POST | Automated |

---

## 8. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Prepared By | Technical Lead | _______ | _______ |
| Reviewed By | Quality Manager | _______ | _______ |
| Approved By | Managing Director | _______ | _______ |
