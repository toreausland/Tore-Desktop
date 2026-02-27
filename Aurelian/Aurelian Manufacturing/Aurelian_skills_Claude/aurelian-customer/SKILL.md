---
name: aurelian-customer
description: Customer-facing materials and sales skill for Aurelian Manufacturing — an autonomous CNC manufacturing company. Use this skill for ANY customer-facing question including technical capabilities, 50/50 profit-sharing model explanation, pricing strategy, RFQ responses, quality certifications, capacity planning, lead times, material capabilities, customer onboarding, partnership model, or any question about what Aurelian offers to manufacturing customers. Triggers on "customer pitch", "customer proposal", "RFQ", "quote", "pricing", "profit sharing", "capacity", "lead time", "quality", "ISO", "AS9100", "defense manufacturing", "CNC capabilities", "partnership model", or any customer-related query about Aurelian Manufacturing.
---

# Aurelian Manufacturing — Customer Materials Skill

### REFERENCE FORMAT FOR GENERATED DOCUMENTS (COPY — DO NOT RECONSTRUCT)

> **Rule: Never hardcode a revision number in generated documents (Word, PPT, PDF).** The master document is always the current revision. When a new revision is issued, all documents remain correct without needing updates. File paths retain the revision in the filename because that is the actual file on disk.

All financial figures in this skill originate from *02 Economic Tables & Projections* (VDR 02.04) — ABSOLUTE master.

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

---

## COMPANY POSITIONING FOR CUSTOMERS

Aurelian Manufacturing is establishing an autonomous CNC production facility in Våler, Østfold — designed for **Production as a Service** for defense, energy, maritime, and industrial customers requiring high-precision, low-to-medium volume (HMLV) machined components.

**Value proposition:** Guaranteed capacity, consistent quality, competitive pricing — with a profit-sharing model that aligns incentives.

**Location:** Våler, Østfold, Norway
**Production start:** Q3 2027
**Contact:** André Tandberg, CEO — andre@aurelian.no
**Contact:** Tore Ausland, VP Business Development — tore@aurelian.no

## TECHNICAL CAPABILITIES

### CNC Equipment
- **Machines:** MAZAK + DMG MORI (tier-1 global manufacturers)
- **Phase 1 (2027):** 5 CNC machines (Seed funding)
- **Phase 2 (2029-2030):** Scale to 20 CNC (Serie A, 3×5 tranches)
- **Phase 3 (2031+):** Scale to 25 CNC
- **Types:** Multi-axis milling and turning centers
- **Automation:** MAZAK MPP / PALLETECH pallet systems, robotic loading
- **Operation:** 24/7 lights-out capable (autonomous operation)

### Production Characteristics
- **Specialization:** High-Mix, Low-to-Medium Volume (HMLV)
- **Batch sizes:** 1 to 1,000+ parts
- **Materials:** Steel, stainless steel, aluminum, titanium, Inconel, specialty alloys
- **Tolerances:** Down to ±0.005 mm (precision machining)
- **Surface finishes:** Ra 0.4 and better
- **Part complexity:** 3-axis through 5-axis simultaneous
- **Maximum part size:** Varies by machine — contact for specific requirements

### Digital Infrastructure
- **CAD/CAM:** Full offline programming capability
- **Digital Twin:** Virtual process validation before first cut
- **MES (Manufacturing Execution System):** Real-time production tracking
- **ERP:** Full order-to-delivery management
- **SPC (Statistical Process Control):** Automated quality monitoring
- **Traceability:** Complete digital thread from order to delivery — critical for defense/aerospace

### Quality Systems (Planned Roadmap)
- **2027:** ISO 9001:2015 (Quality Management System)
- **2028:** AS9100 (Aerospace Quality Standard)
- **2028:** AQAP 2110 (NATO Quality Assurance)
- **Measurement:** CMM (Coordinate Measuring Machine) equipped
- **Inspection:** First Article Inspection (FAI) per AS9102
- **Documentation:** Full material certificates, dimensional reports, process documentation

## PRICING MODEL

### Standard Pricing
- **Hourly rate:** NOK 3,000 (normalized, competitive with Norwegian market)
- **Quoting basis:** Estimated machining time × hourly rate + material + setup
- **Setup charges:** Minimized through offline programming and digital twin validation
- **Rush orders:** Premium applicable for expedited delivery
- **Prototype pricing:** Competitive rates for first-article and development work

### 50/50 Profit-Sharing Partnership Model

**For qualifying high-volume customers, Aurelian offers a unique partnership:**

**How it works:**
1. **Below 45% utilization:** Standard market rates apply. You pay competitive prices, 100% revenue to Aurelian.
2. **Above 45% utilization:** Marginal profit on your orders above the threshold is shared 50/50. You get automatic rebates as your volume grows.

**Qualification criteria:**
- Annual volume potential: 100,000+ CNC hours/year (~17-20 MNOK annual spend)
- Commitment: 12-24 month minimum agreement
- Forecast sharing: Rolling 6-month production forecasts
- Data collaboration: Production planning data for optimization

**What you get as a partner:**
- **Guaranteed capacity allocation** — your orders are prioritized
- **Automatic cost reduction** — the more you produce, the cheaper it gets
- **Price predictability** — no surprise increases, transparent cost model
- **Strategic alignment** — Aurelian succeeds when you succeed
- **Long-term planning security** — capacity reserved for your growth

**Example economics (illustrative):**

| Your annual volume | Standard cost | Partnership cost | Your savings |
|-------------------|--------------|-----------------|-------------|
| 50,000 hours | 150 MNOK | 150 MNOK (below threshold) | — |
| 100,000 hours | 300 MNOK | ~270 MNOK | ~30 MNOK (10%) |
| 150,000 hours | 450 MNOK | ~385 MNOK | ~65 MNOK (14%) |

*Savings increase with volume — the model rewards growth and loyalty.*

## TARGET CUSTOMER SEGMENTS

### Tier 1: Defense & Aerospace (Priority)
**Why Aurelian is your best choice:**
- Full digital traceability (NATO/defense compliance)
- AQAP 2110 certification planned (2028)
- AS9100 aerospace standard planned (2028)
- Norwegian-based, security-clearable workforce
- No foreign ownership or control concerns
- Capacity guarantee through partnership model
- Implicit preparedness value — qualified production ready for surge demand

**Typical components:** Weapon system housings, missile components, vehicle parts, optical mounts, aircraft brackets, munitions components

**Target customers:** Kongsberg Defence & Aerospace, Nammo, Andøya Space, Nordic defense primes (Saab, BAE Systems Hägglunds)

### Tier 2: Energy & Offshore
**Why Aurelian is your best choice:**
- NORSOK-compatible quality systems
- Experience with high-specification materials (Inconel, duplex stainless, titanium)
- Supply chain security (Norwegian production, no geopolitical risk)
- Capacity for large recurring orders
- Faster iterations than offshore alternatives (same time zone, proximity)

**Typical components:** Subsea valve bodies, wellhead components, turbine parts, heat exchanger plates, pipeline connectors

**Target customers:** Equinor, Aker Solutions, Vattenfall/Statkraft, offshore wind suppliers

### Tier 3: Maritime & Infrastructure
**Why Aurelian is your best choice:**
- High-volume capacity with consistent quality
- Norwegian supply chain preference
- Long-term partnership model suits infrastructure timelines
- Multi-material capability

**Typical components:** Ship engine components, propulsion parts, rail infrastructure brackets, structural connectors

**Target customers:** Vard, Ulstein, Bane NOR

## POSITIONING FOR CUSTOMERS

### vs. Traditional Norwegian CNC Shops

**Industry observed (CNC Benchmark, VDR 03.02):**
- Utilization: 20-45%, typically single/double shift
- Staffing: ~2.5 per CNC
- Digital traceability: Typically partial

**Aurelian design targets (pre-revenue):**
- Utilization: 60-65% at maturity (24/7 autonomous scheduling)
- Staffing: 0.8 FTE/CNC at scale (sub-linear model)
- Digital traceability: Complete digital thread from day 1
- Pricing: Partnership model with volume savings

**Note:** In customer-facing materials, present Aurelian capabilities as what the facility is *designed for*, not as proven performance. Use "designed for 24/7 operation" rather than "we operate 24/7".

### vs. Eastern European / Asian Suppliers
| Factor | Offshore Supplier | Aurelian |
|--------|------------------|----------|
| Supply chain security | Geopolitical risk | Norwegian/EU based |
| Iteration speed | Weeks (shipping, time zones) | Days (proximity) |
| IP protection | Variable | Norwegian legal framework |
| Compliance | Complex export control | NATO-aligned, defense-cleared |
| Communication | Language/cultural barriers | Direct, Norwegian/English |
| Quality system | Varies | ISO 9001/AS9100/AQAP planned |

### vs. Building In-House Manufacturing
| Factor | In-House | Aurelian Partnership |
|--------|----------|---------------------|
| CAPEX | 50-200 MNOK | Zero (OPEX model) |
| Time to production | 18-24 months | Immediate (from Q3 2027) |
| Utilization risk | Your problem | Aurelian's problem |
| Scaling flexibility | Fixed capacity | Scale with demand |
| Technology updates | Your investment | Included in service |
| Staffing | Your recruitment challenge | Aurelian handles |

## CUSTOMER ONBOARDING PROCESS

### Phase 1: Discovery (2-4 weeks)
- Initial capability presentation
- Technical requirements review
- Volume and timeline discussion
- NDA execution (if needed for drawings/specifications)
- Preliminary pricing indication

### Phase 2: Qualification (4-8 weeks)
- Detailed RFQ response with pricing
- Process planning for representative parts
- Material sourcing confirmation
- Quality plan proposal
- Partnership model discussion (if qualifying volume)

### Phase 3: Pilot Production (1-3 months)
- First Article Inspection (FAI) on representative parts
- Quality approval process
- Process optimization based on results
- Formal supplier qualification (per customer requirements)

### Phase 4: Production Ramp-Up
- Production scheduling integration
- Forecast sharing setup
- Regular quality reviews
- Partnership agreement execution (if applicable)

## RFQ RESPONSE TEMPLATE

When responding to customer RFQs, include:

1. **Technical compliance matrix** — part-by-part confirmation of specifications
2. **Process plan summary** — machining strategy, fixtures, measurement plan
3. **Material sourcing** — certified suppliers, material certificates included
4. **Pricing breakdown** — machining time, setup, material, finishing, inspection
5. **Lead time commitment** — first article timeline + production delivery schedule
6. **Quality documentation** — what reports/certificates are included
7. **Capacity confirmation** — available capacity for requested volumes
8. **Partnership option** — if volume qualifies, present 50/50 model benefits

## CAPACITY PLANNING

### Available Capacity (by phase — per current master document)

| Phase | CNC Count | Annual Capacity (hours) | At 60% Util |
|-------|-----------|------------------------|-------------|
| Phase 1 (2027-2028) | 5 | 43,800 | 26,280 |
| Phase 2 (2029-2030) | 10-20 | 87,600-175,200 | 52,560-105,120 |
| Phase 3 (2031+) | 20-25 | 175,200-219,000 | 105,120-131,400 |

### Anchor Customer Model
- 5-8 strategic customers providing >70% of initial utilization
- Remaining capacity for spot orders and smaller accounts
- Partnership customers get priority scheduling
- Capacity expansion triggered by documented demand

## FACILITY DETAILS

- **Location:** Våler, Østfold — strategic multi-modal logistics
  - Rail access for heavy/bulk transport
  - Sea port proximity for international shipping
  - Road network for regional delivery
  - Reduced vulnerability — multiple transport channels
- **Facility:** Purpose-built by Norbygg, optimized for autonomous CNC
- **Phase 1:** 2,635 m² production + office space
- **Scalability:** 30,000 m² site for future expansion
- **Security:** Designed for defense-grade requirements
- **Environmental:** Modern facility with energy efficiency focus

## CUSTOMER-FACING Q&A — TOP 10

**Q1: When can you start delivering?**
A: First production capability Q3 2027. Pilot projects and supplier qualification can begin immediately upon facility commissioning. We recommend starting the onboarding process 6 months before to be ready for first delivery.

**Q2: What quality certifications will you have?**
A: ISO 9001:2015 targeted for 2027 (production start). AS9100 (aerospace) and AQAP 2110 (NATO) both targeted for 2028. We can work with customer-specific quality requirements from day one.

**Q3: How does the 50/50 profit-sharing work in practice?**
A: Simple. Below 45% utilization threshold — standard pricing, nothing changes. Above 45% — the marginal profit on your orders is shared equally. You get automatic volume rebates. No complicated formulas — just transparent cost sharing that rewards your loyalty.

**Q4: Can you handle defense/classified work?**
A: Our facility is designed for defense-grade requirements. Norwegian ownership, security-clearable workforce, full digital traceability, and AQAP 2110 certification planned. No foreign ownership concerns. We are building implicit preparedness value — qualified capacity ready when you need it.

**Q5: What materials can you machine?**
A: Full range of metals: steel, stainless steel (including duplex/super duplex), aluminum (all grades), titanium (Grade 2, 5, 23), Inconel, Hastelloy, and specialty alloys. We source from certified Norwegian and European suppliers with full material traceability.

**Q6: How do your prices compare?**
A: Our normalized rate of NOK 3,000/hour is competitive with the Norwegian market. Where we differentiate: (1) Partnership customers get volume-based savings of 10-14%, (2) Our higher utilization means lower overhead per part, (3) 24/7 operation means faster delivery. For offshore alternatives, we're slightly higher on pure price but dramatically better on lead time, IP protection, and compliance.

**Q7: What if I need to scale volume quickly?**
A: Our autonomous operation model means capacity scales without proportional staffing increases. We can add shifts (already 24/7 capable) or allocate additional machines to your work. Partnership customers get priority access to expansion capacity.

**Q8: How do you ensure quality consistency in lights-out operation?**
A: Multiple layers: (1) Digital twin validates every program before cutting, (2) In-process monitoring with automated SPC, (3) CMM measurement integrated into production flow, (4) Complete digital traceability — every parameter logged and auditable. Autonomous ≠ unmonitored. It means digitally monitored 24/7.

**Q9: Can you handle prototypes and development work?**
A: Yes. Our offline programming and digital twin capabilities mean fast turnaround on new parts. We can go from 3D model to first article in days, not weeks. Competitive prototype pricing, and if your product moves to production, you're already qualified.

**Q10: Why should I consider Aurelian as a supplier?**
A: Three reasons: (1) Capacity design — our facility is designed for 24/7 autonomous operation, providing available capacity when traditional single-shift shops are constrained. (2) Cost trajectory — our partnership model means your costs decrease as volume grows. (3) Future-proofing — full digital traceability, defense compliance, and Norwegian supply chain security increasingly required by end customers.

## COMMUNICATION GUIDELINES

When communicating with customers:

**Tone:** Professional, technically confident, solution-oriented
**Language:** Norwegian for domestic customers, English for international
**Focus areas:**
- Lead with capability and capacity (what we can do for them)
- Present partnership model as optional benefit (not pressure)
- Emphasize Norwegian production, supply chain security
- Quality systems and traceability as differentiators
- Defense/energy sector expertise and compliance

**Avoid:**
- Discussing internal financial projections or investor information
- Sharing cap table or ownership details (refer to CEO)
- Making delivery commitments before production start (Q3 2027)
- Promising specific certifications before achieved (say "planned" or "targeted")
- Discussing other customer volumes or pricing (confidential)

## DOCUMENT REFERENCES

- ***02 Economic Tables & Projections* (VDR 02.04)** — ABSOLUTE master for all financial numbers
- **Investor Pitch V3** — Technical capabilities and competitive positioning
- **Concept Note** — Customer-Anchored Capacity model and facility details
- **Real Estate Strategy (Norbygg)** — Facility and real estate strategy
- **Markedsanalyse Master V3** — Market sizing and customer segment analysis
- **Defence/Energy/Critical Markets Research** — Sector-specific demand data
