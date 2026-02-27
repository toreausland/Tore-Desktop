# INCOMING MATERIAL REVIEW AND RELEASE

| Field | Value |
|-------|-------|
| **Document No.** | PR-008 |
| **Revision** | 1.0 |
| **Effective Date** | 2026-02-19 |
| **Approved By** | Quality Manager |
| **Classification** | Internal |
| **ISO 9001 Clause** | 8.4, 8.5.2, 8.6 |

## Document Control Information

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2026-02-19 | Quality Manager | Initial Release |

---

## 1. Purpose

This procedure defines the process for reviewing and releasing incoming raw materials before they are released to the production floor. It ensures that all materials and their accompanying documentation meet customer-specific requirements before any manufacturing begins.

The Material Gate is the first quality intervention point in the manufacturing process. Catching material non-conformances at goods receiving prevents wasted machine time, tooling costs, and potential shipment rejections.

## 2. Scope

This procedure applies to:

- All raw materials received from external suppliers (bar stock, plate, forgings, castings)
- All material certificates (EN 10204 Types 2.1, 2.2, 3.1, 3.2)
- All incoming inspection activities (visual, dimensional, PMI)
- Material release decisions for all production orders

This procedure does NOT apply to:

- Customer-supplied material (covered under PR-007 Section 8.5.3)
- Consumables (tooling, coolant, packaging materials)
- Purchased finished components (covered under PR-008 supplier quality section)

## 3. References

| Document | Title |
|----------|-------|
| QM-001 | Quality Manual |
| PR-004 | Nonconformance and CAPA |
| PR-005 | Production Planning and Control |
| PR-007 | Customer Communication and Contract Review |
| PR-009 | SDRL Processing and MRB Management |
| EN 10204:2004 | Metallic Products — Types of Inspection Documents |
| ASTM E8/E8M | Standard Test Methods for Tension Testing |
| ASTM E18 | Standard Test Methods for Rockwell Hardness |
| ASTM E140 | Standard Hardness Conversion Tables |
| NORSOK M-630 | Material Data Sheets for Piping |
| NORSOK M-650 | Qualification of Manufacturers |

## 4. Definitions

| Term | Definition |
|------|-----------|
| **Material Gate** | The pre-production quality checkpoint where incoming material and its documentation are validated against customer requirements before release to manufacturing |
| **Material Requirement Profile** | A structured data set defining the specific acceptance criteria for a material grade on a specific customer order |
| **EN 10204 Type 3.1** | Inspection certificate issued by the manufacturer's authorized inspection representative, with specific test results from the actual production lot |
| **EN 10204 Type 3.2** | Inspection certificate with specific test results verified by an independent or customer-designated inspector |
| **PMI** | Positive Material Identification — physical verification of material composition using XRF, OES, or laboratory analysis |
| **Heat Number** | Unique identifier assigned to a specific batch/melt of material by the manufacturer |
| **Material Traceability Matrix** | Record linking material heat numbers to specific production orders and part serial numbers |

## 5. Responsibilities

| Role | Responsibility |
|------|---------------|
| **Quality Manager** | Owns this procedure. Approves Material Requirement Profiles. Resolves escalated material decisions. Maintains Approved Supplier List. |
| **QA Engineer** | Performs material gate review. Creates and maintains Material Requirement Profiles. Performs or supervises incoming inspection. Makes RELEASE/REJECT/REVIEW decisions. |
| **Goods Receiving / Warehouse** | Receives material shipments. Verifies quantities and packaging condition. Notifies QA of material arrival. Segregates material pending QA release. |
| **Production Manager** | Cannot issue material to production without QA release. Reports any material discrepancies found during manufacturing. |
| **Purchasing** | Communicates material specifications to suppliers. Ensures Purchase Orders include correct material and certificate requirements. Manages supplier non-conformances. |

## 6. Procedure

### 6.1 Material Arrival and Segregation

**Step 1:** Goods Receiving receives material shipment from supplier.

**Step 2:** Goods Receiving performs initial checks:
- Verify material against Purchase Order (PO number, quantity, material grade, dimensions)
- Check packaging condition (no damage, contamination, or exposure)
- Verify supplier delivery note matches PO
- Collect all accompanying documentation (material certificates, test reports)

**Step 3:** Goods Receiving places material in the **INCOMING INSPECTION** area.
- Material is physically segregated from released stock
- Material is labelled with: PO number, supplier, material grade, date received, status **"PENDING QA REVIEW"**
- Material SHALL NOT be released to production or stored with approved stock

**Step 4:** Goods Receiving notifies QA Engineer that material has arrived and provides:
- Supplier delivery note
- Material certificate(s)
- Any accompanying test reports
- PO reference number

### 6.2 Material Requirement Profile Identification

**Step 5:** QA Engineer identifies which production order(s) the material is intended for.

**Step 6:** QA Engineer loads the applicable **Material Requirement Profile**:

- **If profile exists:** Load the customer-specific profile for this material grade and customer combination
- **If profile does not exist:** Create a new profile following Section 7 of this procedure

**Note:** The same material lot may be allocated to multiple orders with different customers. Each customer's requirements must be checked independently. Material can be RELEASED for one order and REJECTED for another.

### 6.3 Certificate Review — Five-Point Check

The QA Engineer performs the following five checks on each material certificate:

#### Check 1: Certificate Type Verification

| Requirement | Action |
|-------------|--------|
| Customer requires Type 3.2, supplier provides 3.2 | PASS |
| Customer requires Type 3.1, supplier provides 3.1 or 3.2 | PASS (3.2 exceeds 3.1) |
| Customer requires Type 3.2, supplier provides 3.1 | FAIL — certificate type insufficient |
| Customer requires Type 3.1, supplier provides 2.2 or 2.1 | FAIL — certificate type insufficient |

Record result on Form FM-008-01.

#### Check 2: Chemical Composition Verification

For each element specified in the Material Requirement Profile:

1. Read the **actual** value from the certificate (not typical values)
2. Compare against the customer's specification limits (min/max)
3. Record actual value and PASS/FAIL on Form FM-008-01

**Critical rules:**
- "Typical" or "nominal" values are NOT acceptable — actual test results are required
- If an element specified in the profile is **not reported** on the certificate, it is a FAIL
- If a value is within 5% of any specification limit, flag as **BORDERLINE** for additional review
- Use the **customer's** specification limits, not just the base material standard

#### Check 3: Mechanical Property Verification

For each property specified in the Material Requirement Profile:

1. Read the actual value from the certificate
2. Normalize units if necessary (ksi to MPa: multiply by 6.895)
3. Compare against customer's minimum/maximum requirements
4. For impact tests: verify test temperature matches requirement, check both average AND single minimum
5. Record actual value and PASS/FAIL on Form FM-008-01

**Unit conversion reference:**

| From | To | Factor |
|------|----|--------|
| ksi | MPa | x 6.895 |
| ft-lbf | Joules | x 1.356 |
| HRC to HB | Use ASTM E140 conversion table |

#### Check 4: Supplementary Requirements Verification

For each supplementary test required by the Material Requirement Profile:

| Test | Verify |
|------|--------|
| Impact/Charpy | Temperature, specimen size, average and single values |
| Intergranular corrosion (IGC) | Test method (A262 Practice), result/acceptance |
| Ultrasonic testing (UT) | Standard, acceptance criteria, result |
| Grain size | Method (ASTM E112), ASTM grain size number |
| Ferrite content | Method, measured value vs. acceptance range |
| Heat treatment | Condition, temperature, cooling method per specification |

Record presence and result on Form FM-008-01. If a required test is absent, it is a FAIL.

#### Check 5: Traceability and Integrity Verification

| Check | Criteria | Result |
|-------|----------|--------|
| Heat number present | Heat/lot number clearly stated on certificate | PASS / FAIL |
| Signature present | Authorized representative signature present | PASS / FAIL |
| For Type 3.2: Third-party stamp | Independent inspector identification and stamp | PASS / FAIL |
| Supplier on Approved Supplier List | If customer requires approved sources | PASS / FAIL / N/A |
| Material specification matches PO | Grade on certificate matches what was ordered | PASS / FAIL |
| Certificate completeness | All mandatory fields populated, no blank sections | PASS / FAIL |
| Integrity indicators | No signs of alteration, suspicious values, or poor quality scan | PASS / FLAG |

**Integrity red flags** (trigger additional review, not automatic rejection):
- All mechanical values exactly at specification minimums
- Chemical composition values all at round numbers
- Multiple heats with identical test results
- Certificate appears to be a photocopy of a photocopy
- Date inconsistencies

### 6.4 Incoming Physical Inspection

**Step 7:** If required by the Material Requirement Profile or triggered by certificate red flags:

#### PMI (Positive Material Identification)

Perform when:
- Customer requirement profile specifies PMI mandatory
- Certificate integrity flags were raised
- Material is for safety-critical application (pressure equipment, defence)
- Material grade cannot be visually distinguished from other stock

PMI procedure:
1. Select testing method: XRF (standard), OES (when carbon content is critical)
2. Verify instrument calibration is current
3. Test material at accessible location
4. Record elemental results on Form FM-008-02
5. Compare PMI results against certificate values — correlation check:
   - For major elements (Cr, Ni, Mo): difference should be < 1.0% absolute
   - If difference exceeds expected variation: **QUARANTINE material immediately**

#### Visual and Dimensional Check

1. Visual inspection for surface defects, corrosion, contamination
2. Verify material dimensions match PO requirements
3. Verify material marking matches certificate (heat number stamped/painted on material)
4. Record on Form FM-008-02

### 6.5 Gate Decision

**Step 8:** Based on the five-point certificate check and any physical inspection results, the QA Engineer makes the gate decision:

#### RELEASED

All conditions met:
- All five certificate checks PASS
- Physical inspection PASS (if performed)
- PMI correlates with certificate (if performed)

**Actions:**
1. Stamp/label material **"QA RELEASED"** with date and QA Engineer initials
2. Update ERP material status to **RELEASED**
3. Material moved to approved stock area
4. Certificate linked to material lot in ERP document management
5. Certificate **pre-staged** for MRB Section 3 (Material Documentation) for all allocated orders
6. Record gate decision on Form FM-008-01
7. Notify Production that material is available

#### REJECTED

One or more critical failures:
- Wrong material grade
- Certificate type insufficient
- Chemical or mechanical values outside specification limits
- Required tests missing
- Unsigned or invalid certificate
- PMI does not correlate with certificate

**Actions:**
1. Label material **"QUARANTINED — DO NOT USE"** with date and reason
2. Move material to quarantine/rejection area (physically segregated)
3. Update ERP material status to **QUARANTINED**
4. Raise NCR per PR-004 (Nonconformance and CAPA)
5. Notify Purchasing for supplier action (replacement, credit, return)
6. Record gate decision and specific failure reasons on Form FM-008-01
7. Notify Production if material was expected for an active order

#### REVIEW (Escalation)

Borderline or ambiguous findings requiring human judgment:
- Values within 5% of specification limits
- Certificate partially illegible
- Integrity red flags that need investigation
- Material grade is acceptable alternate but not exact match
- Customer requirement is ambiguous

**Actions:**
1. Label material **"ON HOLD — QA REVIEW"** with date
2. Update ERP material status to **ON HOLD**
3. QA Engineer documents specific findings requiring review
4. Quality Manager reviews and makes final decision
5. If needed: contact customer for clarification or deviation approval
6. Final decision recorded as RELEASED or REJECTED with justification

### 6.6 Multi-Order Allocation

When the same material lot is allocated to multiple production orders:

1. QA Engineer identifies ALL orders that will use the material
2. Material is validated against EACH order's Material Requirement Profile independently
3. Results recorded per order:
   - Material can be **RELEASED** for Order A and **REJECTED** for Order B (different customer requirements)
4. ERP allocation records show which orders are approved for which material lots
5. Certificate is pre-staged for MRB Section 3 of each approved order

**Critical rule:** Material SHALL NOT be issued to any production order for which it has not been specifically validated and released.

## 7. Material Requirement Profiles

### 7.1 Profile Creation

When no existing profile matches a new customer/material/specification combination:

1. QA Engineer extracts material requirements from:
   - Purchase Order and referenced specifications
   - Customer SDRL (via PR-009)
   - Customer-specific material specifications or data sheets
   - Industry standard requirements (NORSOK MDS, AMS specs, etc.)

2. QA Engineer creates a new profile containing:
   - Customer name and profile ID
   - Material specification(s) and grade
   - Certificate type required
   - Chemical composition limits (per element: min/max)
   - Mechanical property limits (per property: min/max, unit, test method)
   - Supplementary test requirements (which tests, methods, acceptance criteria)
   - PMI requirement (yes/no)
   - Approved supplier list (if applicable)
   - Special requirements (heat treatment conditions, restrictions)

3. Quality Manager reviews and approves the profile

4. Profile saved in the profile library for reuse

### 7.2 Profile Library Structure

Profiles are organized in three tiers:

| Tier | Description | Example |
|------|-------------|---------|
| **Industry Base** | Default limits from the base material standard | ASTM A182 F316L standard limits |
| **Customer-Specific** | Customer's additional or tighter requirements | Equinor NORSOK MDS requirements for F316L |
| **Order-Specific Override** | One-time requirements unique to a specific PO | Extra impact test at -60C for PO-2027-042 |

**Resolution order:** Order-specific override (if exists) > Customer-specific profile > Industry base profile

### 7.3 Profile Maintenance

- Profiles are reviewed when a customer issues new specifications or changes requirements
- Profiles are version-controlled: changes create a new version, old version retained for historical orders
- Annual review of all active profiles during Management Review (PR-003)

## 8. Records

| Form | Title | Retention |
|------|-------|-----------|
| FM-008-01 | Material Gate Review Checklist | Per order archival requirement (minimum 15 years) |
| FM-008-02 | Incoming Physical Inspection Report (PMI/Visual/Dimensional) | Per order archival requirement (minimum 15 years) |
| FM-008-03 | Material Requirement Profile | Life of profile + 5 years after last use |
| FM-008-04 | Material Traceability Matrix | Per order archival requirement (minimum 15 years) |

## 9. Key Performance Indicators

| KPI | Target | Measured |
|-----|--------|----------|
| Material Gate cycle time | < 4 hours from arrival to decision | Monthly |
| First-pass release rate | > 90% of material lots released on first review | Monthly |
| Supplier certificate rejection rate | < 5% | Quarterly |
| Post-release material non-conformance | 0 (no material issues found after gate release) | Per incident |
| PMI mismatch rate | < 1% of PMI tests | Quarterly |

## 10. Flowchart

```
Material Arrives at Goods Receiving
            │
            ▼
┌─────────────────────────┐
│ Initial Receipt Check    │
│ (PO, qty, condition)    │
└───────────┬─────────────┘
            │
            ▼
   Segregate to INCOMING
   INSPECTION area
            │
            ▼
   Notify QA Engineer
            │
            ▼
┌─────────────────────────┐
│ Load Material Requirement│
│ Profile for target       │
│ order(s)                 │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ 5-POINT CERTIFICATE      │
│ CHECK:                   │
│ 1. Certificate type      │
│ 2. Chemical composition  │
│ 3. Mechanical properties │
│ 4. Supplementary tests   │
│ 5. Traceability/integrity│
└───────────┬─────────────┘
            │
            ▼
   Physical inspection
   required?
      │           │
     YES          NO
      │           │
      ▼           │
  PMI / Visual /  │
  Dimensional     │
      │           │
      ▼           ▼
┌─────────────────────────┐
│     GATE DECISION        │
├─────────┬───────┬────────┤
│RELEASED │REVIEW │REJECTED│
│         │       │        │
│ Label   │ Hold  │Quarant.│
│ "QA OK" │ Escal.│ NCR    │
│ ERP upd │ QM    │ Purch. │
│ Pre-    │decides│notified│
│ stage   │       │        │
│ for MRB │       │        │
└─────────┴───────┴────────┘
```

## 11. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Prepared By | Quality Manager | _______ | _______ |
| Reviewed By | Production Manager | _______ | _______ |
| Approved By | Managing Director | _______ | _______ |

This document is controlled. Printed copies are uncontrolled unless stamped "CONTROLLED COPY" in red.
