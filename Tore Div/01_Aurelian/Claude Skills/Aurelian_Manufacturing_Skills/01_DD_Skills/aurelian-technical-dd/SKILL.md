---
name: aurelian-technical-dd
description: Technical Due Diligence skill for Aurelian Manufacturing covering CNC utilization validation, autonomous operations feasibility, supplier assessment, facility planning, technology risk, and operational readiness. Use this skill for ANY technical DD question including "how do you achieve 60-65% utilization", "validate autonomous operations", "technology risk assessment", "supplier dependency", "facility timeline", "lights-out manufacturing", "CNC technology choice", "MAZAK vs DMG MORI", "digital twin", "quality certifications", "ISO roadmap", or any question about Aurelian's technical execution capability and operational feasibility.
---

# Aurelian Manufacturing — Technical DD

Execution feasibility and technical validation for a pre-revenue autonomous CNC manufacturing platform. Primary technical validation source: Vedlegg D (Kvalitativ validering av autonom CNC-utnyttelse i HMLV-produksjon).

## Core Technical Thesis

Aurelian achieves 60-65% CNC utilization in HMLV production through **greenfield autonomous design** — not by retrofitting existing workshops. The key insight: sub-linear staffing (0.8 vs 2.5 people per CNC) is structurally impossible to achieve in brownfield environments due to legacy culture, equipment, and organization.

## Utilization Validation (Vedlegg D)

### Why 55-65% is Realistic, Not Aspirational

Industry average OEE for CNC workshops is ~60%. HMLV-specific achievable range is 55-65%. This is validated by three independent sources:

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

### Norwegian Benchmark Comparison

| Company | CNC Count | Utilization | Staff/CNC |
|---------|-----------|-------------|-----------|
| Rogaland Maskinering | 7 | 10% | ~2.5 |
| Lilaas | 15 | 19% | ~2.5 |
| Tamek | 8 | 20% | ~2.5 |
| Uvdal Maskinfabrikk | 11 | 37% | ~2.5 |
| Aarbakke | 55 | 38% | 2.5 |
| TP-Products | 14 | 40-45% | ~2.5 |
| Årdal Maskinering | 18 | 47% | 2.5 |
| **Aurelian (target)** | **20** | **60-65%** | **0.8** |

The best Norwegian operators top out at 40-47%. Aurelian's target of 60-65% represents a step-change enabled by greenfield autonomous design, not incremental improvement on existing operations.

### Why Brownfield Cannot Compete

Key barriers to retrofitting existing workshops:

1. **Cultural inertia:** Existing operators resist unmanned production shifts
2. **Equipment legacy:** Machines not configured for palletized autonomous cells
3. **Layout constraints:** Buildings designed for manned workflow, not material flow automation
4. **IT/OT integration:** Legacy systems cannot support full digital thread
5. **Economic resistance:** Sunk costs in current setup discourage fundamental redesign

Aurelian's greenfield advantage means every decision — from building layout to machine configuration to IT architecture — is optimized for autonomous operation from day one.

## Technology Platform

### CNC Machine Selection

Primary suppliers: **MAZAK** and **DMG MORI** — both are tier-1 global CNC manufacturers with:
- Proven track record in autonomous and multi-tasking operations
- Strong European service and support networks
- High resale values protecting downside (see Vedlegg E)
- Advanced automation-ready configurations

### Automation Architecture

**Phase 1 (Seed — 8 CNC):**
- Palletized workholding systems per machine
- Automated tool management and presetting
- In-process measurement and quality verification
- Basic robotic loading/unloading where applicable
- MES (Manufacturing Execution System) for scheduling and tracking

**Phase 2 (Scale to 20 CNC):**
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

## Facility Strategy (Vedlegg G)

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
- **Annual lease:** ~4 MNOK (estimated, included in operating costs)
- **Timeline:** ~12 months from investment decision to production
- **Design:** Modular layout, palletized CNC cells, unmanned operation ready
- **Multi-modal logistics:** Production continues even if one transport mode disrupted

### Why Våler?

Not chosen for cost optimization or real estate speculation. Chosen for:
- **Logistical redundancy:** Railway + sea transport + road (truck)
- **Operational resilience:** Multi-modal access ensures delivery security
- **Defense relevance:** Proximity to strategic industrial corridors
- **Expansion potential:** 30,000 m² total site allows significant scaling

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

## Technical DD Q&A (Top 15)

**Q1: How do you achieve 60-65% utilization when the best Norwegian shops are at 40-47%?**
A: Greenfield autonomous design. Every element — layout, machines, IT, staffing — is optimized for unmanned operation. Existing shops cannot retrofit this because of cultural, equipment, and structural constraints. See Vedlegg D for detailed validation.

**Q2: What if autonomous operations fail?**
A: Gradual ramp-up plan: manned shifts first, then extending to lights-out evenings, then nights, then weekends. Proven technology from DMG MORI and MAZAK. Fallback to manned operation at any point — still profitable at lower utilization.

**Q3: Why greenfield instead of acquiring an existing shop?**
A: Sub-linear staffing (0.8 vs 2.5 people per CNC) is impossible to retrofit. Brownfield constraints include legacy culture, equipment, layout, and IT systems. Building new is faster and cheaper than transforming existing operations.

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

For additional technical Q&A, read `references/technical-qa-extended.md`.
