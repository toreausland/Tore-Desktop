---
name: aurelian-technical-dd
description: Technical Due Diligence skill for Aurelian Manufacturing covering CNC utilization validation, autonomous operations feasibility, supplier assessment, facility planning, technology risk, and operational readiness. Use this skill for ANY technical DD question including "how do you achieve 60-65% utilization", "validate autonomous operations", "technology risk assessment", "supplier dependency", "facility timeline", "lights-out manufacturing", "CNC technology choice", "MAZAK vs DMG MORI", "digital twin", "quality certifications", "ISO roadmap", or any question about Aurelian's technical execution capability and operational feasibility.
---

# Aurelian Manufacturing — Technical DD

Execution feasibility and technical validation for a pre-revenue autonomous CNC manufacturing platform. Primary technical validation source: Autonomous CNC Validation report (qualitative validation of autonomous CNC utilization in HMLV production, available in VDR section 04_Technical).

**Financial source:** *02 Economic Tables & Projections* (VDR 02.04) — ABSOLUTE master for all numbers.

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

## Core Technical Thesis

Aurelian's greenfield model targets 60-65% CNC utilization in HMLV production through autonomous design — not by retrofitting existing workshops. The key design insight: sub-linear staffing (design target 0.8 FTE/CNC at scale, vs industry-observed ~2.5 per CNC Benchmark VDR 03.02) is structurally difficult to achieve in brownfield environments due to legacy culture, equipment, and organization. All Aurelian figures below are design targets for a pre-revenue company unless otherwise noted.

## Utilization Validation

### Why 55-65% is the Design Target

Industry average OEE for general CNC workshops is ~60%. HMLV-specific achievable range is 55-65% according to vendor reference data. Three independent vendor sources support feasibility:

**DMG MORI Perspective:**
- CELOS X platform enables full digital thread from CAD to finished part
- Connected Machining eliminates manual data transfer bottlenecks
- Predictive maintenance reduces unplanned downtime
- Reference installations demonstrate 80% process time reduction with digital twin

**MAZAK Perspective:**
- iSMART Factory concept proven in own production facilities
- MAZATROL SmoothAi CNC control lowers programming skill barrier
- Multi-tasking machines (INTEGREX) combine operations, reducing setup time
- Modular automation cells enable gradual autonomy ramp-up

**Siemens Perspective:**
- Digital twin + CAD/CAM/CNC integration = 80% process time reduction
- NX CAM → SINUMERIK direct integration eliminates translation errors
- Closed-loop manufacturing: actual data feeds back to optimize future runs

### Norwegian Benchmark (Observed Data — CNC Benchmark VDR 03.02)

| Company | CNC Count | Utilization | Staff/CNC |
|---------|-----------|-------------|-----------|
| Rogaland Maskinering | 7 | 10% | ~2.5 |
| Lilaas | 15 | 19% | ~2.5 |
| Tamek | 8 | 20% | ~2.5 |
| Uvdal Maskinfabrikk | 11 | 37% | ~2.5 |
| Aarbakke | 55 | 38% | 2.5 |
| TP-Products | 14 | 40-45% | ~2.5 |
| Årdal Maskinering | 18 | 47% | 2.5 |

**Aurelian design targets (pre-revenue):** 20 CNC, 60-65% utilization, 0.8 FTE/CNC — enabled by greenfield autonomous design (24/7 scheduling, pallettesystem, robotic loading, no legacy constraints).

The best observed Norwegian operators reach 40-47%. Aurelian's target of 60-65% represents a structural step-change through greenfield design, not incremental improvement.

### Why Brownfield Retrofit is Structurally Difficult

Key barriers to retrofitting existing workshops for autonomous operation:

1. **Cultural inertia:** Existing operators resist unmanned production shifts
2. **Equipment legacy:** Machines not configured for palletized autonomous cells
3. **Layout constraints:** Buildings designed for manned workflow, not material flow automation
4. **IT/OT integration:** Legacy systems cannot support full digital thread
5. **Economic resistance:** Sunk costs in current setup discourage fundamental redesign

Aurelian's greenfield approach means every decision — from building layout to machine configuration to IT architecture — can be designed for autonomous operation from day one. This is a design opportunity, not a proven outcome.

## Technology Platform

### CNC Machine Selection

Primary suppliers: **MAZAK** and **DMG MORI** — both are tier-1 global CNC manufacturers with:
- Proven track record in autonomous and multi-tasking operations
- Strong European service and support networks
- High resale values protecting downside (50-70% range per CNC Resale Value Analysis in VDR)
- Advanced automation-ready configurations

### Machine Deployment (

| Period | Event | CNC (EOY) | Funding |
|--------|-------|-----------|---------|
| Jun 2027 | 5 CNC delivered, commissioning | 5 | Seed |
| Aug 2027 | Production starts | 5 | Seed |
| Q4 2028 | Serie A Tranche 1 arrives | 5 (+5) | Serie A |
| Q1 2029 | Tranche 1 operational | 10 | Serie A |
| Q3 2029 | Tranche 2 operational | 15 | Serie A |
| Q3 2030 | Tranche 3 operational | 20 | Serie A |

### Automation Architecture

**Phase 1 (Seed — 5 CNC):**
- Palletized workholding systems per machine
- Automated tool management and presetting
- In-process measurement and quality verification
- Basic robotic loading/unloading where applicable
- MES (Manufacturing Execution System) for scheduling and tracking

**Phase 2 (Scale to 20 CNC via Serie A):**
- Automated material handling between machines
- Advanced fixture management system
- Full lights-out capability for routine operations
- Remote monitoring and alerting (24/7)
- Digital twin for offline programming and simulation

**Phase 3 (25 CNC — Full Scale):**
- AI-assisted process optimization
- Predictive maintenance integration
- Fully autonomous production cells
- Automated quality inspection (CMM/vision)
- Customer portal for real-time order tracking

### Digital Backbone

| System | Purpose | Integration |
|--------|---------|-------------|
| CAD/CAM (NX/Mastercam) | Part programming | → CNC via post-processor |
| MES | Production scheduling | → ERP, machines, quality |
| ERP | Business operations | → Finance, inventory, CRM |
| Digital Twin | Simulation & optimization | → CAM, MES, maintenance |
| Quality (SPC) | Statistical process control | → MES, customer reporting |
| IT/OT Security | Cyber protection | Network segmentation |

## Facility Strategy

### Norbygg Partnership

Aurelian leases rather than owns its facility — a deliberate capital discipline choice.

**Norbygg (developer partner):** Develops, owns, and manages the building. Adapts premises to Aurelian's functional requirements. Bears property investment and residual value risk.

**Aurelian (industrial tenant):** Defines layout requirements, technical specifications, and logistics flow. Leases through long-term commercial agreement. Avoids CAPEX on building infrastructure.

**Bank perspective benefits:**
- Lower capital commitment (no real estate CAPEX)
- OPEX-characterized costs (predictable)
- Higher financial flexibility during ramp-up
- Clear risk separation between industrial operations and property

### Facility Specifications

- **Location:** Våler, Østfold (strategic: rail + sea + road access)
- **First phase:** 2,635 m² on ~9,000 m² plot
- **Total buildable:** 30,000 m² (full site)
- **Annual lease:** ~5.2 MNOK (per master document, included in operating costs)
- **Timeline:** ~12 months from investment decision to production
- **Design:** Modular layout, palletized CNC cells, unmanned operation ready
- **Multi-modal logistics:** Production continues even if one transport mode disrupted

### Why Våler?

Not chosen for cost optimization or real estate speculation. Chosen for:
- **Logistical redundancy:** Railway + sea transport + road (truck)
- **Operational resilience:** Multi-modal access ensures delivery security
- **Defense relevance:** Proximity to strategic industrial corridors
- **Expansion potential:** 30,000 m² total site allows significant scaling

## CNC Machine Economics (

| Parameter | Value | Unit |
|-----------|-------|------|
| Cost per CNC incl. automation | **10,000,000** | NOK |
| Depreciation life | 8 | years |
| Annual depreciation per CNC | **1,250,000** | NOK |
| Debt interest rate | 7.5% | % |
| Debt per CNC (Seed, 50% EQ) | 5,000,000 | NOK |
| Debt per CNC (Serie A, 30% EQ) | 7,000,000 | NOK |
| Resale value (estimate) | 60% | % (50-70% range) |
| Shop base setup (per site) | 8,600,000 | NOK |

## Quality Certification Roadmap

| Certification | Target | Purpose |
|--------------|--------|---------|
| ISO 9001 | 2027 | General quality management (market entry) |
| AS9100 | 2028 | Aerospace/defense supply chain standard |
| AQAP 2110 | 2028 | NATO quality assurance requirements |
| ISO 14001 | 2029 | Environmental management (optional) |

**ISO 9001** is the minimum requirement for serious industrial customers. **AS9100** and **AQAP** are prerequisites for defense and aerospace contracts — Aurelian's primary target segments.

## Technology Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| CNC downtime | Medium | High | Premium suppliers, service agreements, spare parts, multi-machine redundancy |
| Autonomous operation instability | Medium | Medium | Gradual ramp-up (manned → lights-out), fallback procedures, 24/7 remote monitoring |
| IT/OT cyber incident | Low | High | Segmented architecture, industrial security standards, regular audits, backup systems |
| Software integration failures | Medium | Medium | Experienced integrators, proven platforms (MAZAK SMOOTH), extensive pre-launch testing |
| Skilled labor shortage | High | Medium | MAZATROL conversational programming (lowers bar), competitive compensation, training |
| Supplier delivery delays | Medium | Medium | Early order placement, close Mazak Norway relationship, alternative suppliers identified |
| Customer qualification delays | Medium | Medium | Early engagement during Pre-Seed/Seed, focus on known segments, reference installations |

## Technical DD Q&A (Top 10)

**Q1: How do you target 60-65% utilization when the best Norwegian shops are at 40-47%?**
A: Greenfield autonomous design. Every element — layout, machines, IT, staffing — is designed for unmanned operation from day one. Existing shops face structural barriers to retrofitting this (cultural, equipment, layout constraints). The Autonomous CNC Validation report (VDR 04_Technical) details feasibility assessment from DMG MORI, MAZAK, and Siemens vendor data. 60-65% is the design target at maturity, not a launch assumption — master document models 20% in H2 2027, ramping to 37.5% in 2028.

**Q2: What if autonomous operations fail?**
A: Gradual ramp-up plan: manned shifts first, then extending to lights-out evenings, then nights, then weekends. Proven technology from DMG MORI and MAZAK. Fallback to manned operation at any point — still profitable at lower utilization.

**Q3: Why greenfield instead of acquiring an existing shop?**
A: The design target of sub-linear staffing (0.8 FTE/CNC at scale) requires layout, culture, IT/OT architecture, and automation to be designed from scratch. Brownfield environments carry legacy constraints that make this structurally difficult. Building new is assessed as faster and lower total cost than transforming existing operations.

**Q4: What's the technology readiness level?**
A: All core technology is commercially available and proven. MAZAK iSMART Factory and DMG MORI CELOS X are production-ready platforms. Aurelian's innovation is in system integration and operational design, not in developing new technology.

**Q5: How do you handle HMLV (High-Mix Low-Volume) complexity?**
A: Digital twin for offline programming (no machine downtime for setup), standardized fixturing systems, automated tool management, and MAZATROL conversational programming for rapid changeover.

**Q6: What's your supplier dependency risk?**
A: Both MAZAK and DMG MORI are global tier-1 suppliers with European support. Not dependent on a single supplier — can source from either or both. Service agreements ensure priority support.

**Q7: How long from investment to first production?**
A: ~12 months. Facility buildout and machine installation parallel-tracked. Norbygg handles building, Aurelian handles equipment and commissioning.

**Q8: What about cybersecurity for autonomous operations?**
A: IT/OT network segmentation, industrial-grade security protocols, regular audits, backup systems. NIS2 Directive compliance if designated critical infrastructure.

**Q9: Can you prove the 3,000 NOK/hour rate is achievable?**
A: Market rate for HMLV precision CNC in Norway. Comparable operators charge 2,500-3,500 NOK/hour. Aurelian's full traceability and defense certifications support premium pricing.

**Q10: What happens if a machine breaks down during unmanned production?**
A: Multi-machine redundancy (work redistributed), 24/7 remote monitoring with automated alerts, service agreements with MAZAK/DMG MORI for rapid response, spare parts inventory on-site.
