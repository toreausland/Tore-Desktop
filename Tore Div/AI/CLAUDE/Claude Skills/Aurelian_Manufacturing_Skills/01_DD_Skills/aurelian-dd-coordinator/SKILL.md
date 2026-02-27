---
name: aurelian-dd-coordinator
description: Master orchestrator for Aurelian Manufacturing's Due Diligence process across Pre-Seed, Seed, and Series A rounds. Use this skill whenever someone mentions DD preparation, investor due diligence, DD checklist, DD readiness review, data room setup, investor Q&A preparation, or anything related to coordinating the DD process. This is the entry point — if unsure which DD skill to use, start here. Also triggers for "what's missing for DD", "prepare for investor meetings", "DD status", "VDR structure", or any general DD coordination question.
---

# Aurelian Manufacturing — DD Coordinator

Master orchestration skill for investor Due Diligence. This skill routes DD queries to the right specialist skill and maintains overall DD readiness.

## Critical Context

Aurelian Manufacturing is a **pre-revenue** autonomous CNC manufacturing company targeting Q3 2027 production start. All DD materials must reflect pre-revenue status — focus on assumption validation, not historical performance.

**Master financial source:** `Aurelian_Finansieringsplan_KOMPLETT.pdf` — use this for ALL numbers.

## Fundraising Rounds

| Round | Amount | Pre-Money | Dilution | Target ROI | Status |
|-------|--------|-----------|----------|------------|--------|
| Pre-Seed | 5 MNOK | 25 MNOK | 16.7% | 49x | Active |
| Seed | 47 MNOK | 140 MNOK | 25.1% | 10.5x | Planning |
| Series A | 42 MNOK | 250 MNOK | 14.4% | 7.9x | Future |

**Exit scenario:** 2.3B NOK @ 10-11x EBITDA (222 MNOK EBIT after 50/50 sharing)
**Founders retain 53.4% at exit** — strong alignment, control maintained throughout.

## Routing Logic

When a DD question arrives, determine the domain and route:

- **Financial questions** (valuation, revenue model, break-even, CAPEX, sensitivities, ROI) → Read `references/financial-dd-guide.md`
- **Technical questions** (CNC utilization, autonomous ops, suppliers, facility, technology risk) → Read `references/technical-dd-guide.md`
- **Market questions** (TAM/SAM/SOM, competition, customer pipeline, go-to-market) → Read `references/market-dd-guide.md`
- **Legal/Corporate questions** (cap table, IP, contracts, governance, compliance) → Read `references/legal-dd-guide.md`
- **General DD coordination** (checklists, readiness, VDR, timeline) → Continue in this skill

## DD Checklists by Round

### Pre-Seed DD (Light — Founder-Friendly, 2-4 weeks)

Investors at this stage focus on team, concept, and market size.

**Required:**
- [ ] Corporate structure documentation (shareholders, board composition)
- [ ] Founder backgrounds (CVs, industry experience, references)
- [ ] Market research and competitive analysis (Markedsanalyse Master V3)
- [ ] High-level financial projections (3-year view from Finansieringsplan)
- [ ] Technology concept validation (Vedlegg D — autonomous CNC feasibility)
- [ ] Key team member commitments (Vedlegg F)
- [ ] Investor pitch deck (V3 — 12 slides)

**Available now:** Pitch Deck V3, Markedsanalyse Master V3, Vedlegg C/D/E/F/G, Finansieringsplan

### Seed DD (Institutional VC Standard, 4-8 weeks)

**All Pre-Seed items plus:**
- [ ] Cap table with pre/post-money per round (from Finansieringsplan KOMPLETT)
- [ ] Detailed financial model (5-7 year, with sensitivities)
- [ ] Customer discovery evidence (interviews, LOIs) — **GAP: Need customer LOIs**
- [ ] Supplier commitments — **GAP: Need Mazak LOI, Norbygg term sheet**
- [ ] Technology validation report (Vedlegg D)
- [ ] Comparable investment cases (Vedlegg C — Hadrian comparison)
- [ ] CNC resale value analysis (Vedlegg E — bank collateral)
- [ ] Facility plans and timeline (Vedlegg G — Norbygg partnership)
- [ ] Risk register with mitigation strategies (from Markedsanalyse Ch.10)
- [ ] Legal entity documents (articles, shareholder agreement)
- [ ] Material contracts (employment, advisory, leases) — **GAP: Need executed agreements**
- [ ] IP strategy and protection plan — **GAP: Need IP assignment docs**
- [ ] Regulatory compliance roadmap (ISO 9001 → AS9100 → AQAP)
- [ ] Defence/Energy market research (dedicated research reports)

### Series A DD (Full Diligence, 8-12 weeks)

**All Seed items plus:**
- [ ] 12+ months operational data (actual utilization, revenue, quality metrics)
- [ ] Customer contracts and active pipeline
- [ ] Actual vs projected financials (variance analysis)
- [ ] Quality certifications achieved (ISO 9001 minimum)
- [ ] Employee roster and organizational development
- [ ] Banking relationships and credit facilities
- [ ] Insurance coverage (liability, property, key person)
- [ ] Environmental compliance documentation

## Documentation Status

### Available Documents (13 total)
| Document | Type | DD Domain |
|----------|------|-----------|
| Investor Pitch V3 | Presentation | All |
| Markedsanalyse Master V3 | Analysis | Market, Financial, Technical |
| Defence Market Research | Research | Market |
| Energy Market Research | Research | Market |
| Critical Markets Research | Research | Market |
| Market Trends & Projections | Research | Market |
| Vedlegg C — Comparable Cases | Analysis | Financial, Market |
| Vedlegg E — CNC Resale Values | Analysis | Financial, Technical |
| Vedlegg F — Team & Governance | Documentation | Legal, Team |
| Vedlegg G — Facility Strategy | Documentation | Technical, Legal |
| DD Skills Architecture | Internal | Coordination |
| DD Skills Transfer Summary | Internal | Coordination |
| Document Inventory | Internal | Coordination |

### Critical Gaps (Must fill before Seed DD)
1. **Customer LOIs / MOUs** — No anchor customer documentation yet
2. **Mazak purchase LOI** — Referenced but not documented
3. **Norbygg lease agreement** — Referenced but not executed
4. **Shareholder agreement** — Needed for legal DD
5. **Founder vesting schedules** — Standard VC requirement
6. **IP assignment agreements** — Critical for technical/legal DD
7. **Detailed financial model (Excel)** — With formulas, not just PDF
8. **Advisory agreements** — Fredrik, Bjørnar, Andreas
9. **Monthly cash flow projections** — 2027-2028

## Virtual Data Room Structure

```
/aurelian-vdr/
├── 01-corporate/
│   ├── articles-of-incorporation
│   ├── shareholder-agreement
│   ├── board-minutes/
│   ├── cap-table.xlsx
│   └── organizational-chart
├── 02-financial/
│   ├── financial-model.xlsx
│   ├── financing-plan-komplett.pdf
│   ├── economic-tables-vedlegg-b.pdf
│   ├── valuation-basis.pdf
│   ├── cnc-resale-analysis-vedlegg-e.pdf
│   └── sensitivities/
├── 03-commercial/
│   ├── market-research/
│   │   ├── markedsanalyse-master-v3.pdf
│   │   ├── defence-market-research.pdf
│   │   ├── energy-market-research.pdf
│   │   ├── critical-markets-research.pdf
│   │   ├── market-trends-projections.pdf
│   │   ├── comparable-cases-vedlegg-c.pdf
│   │   └── vc-praksis-analyse.pdf
│   ├── customer-discovery/
│   │   ├── interview-notes/
│   │   └── lois/
│   └── competitive-analysis/
├── 04-technical/
│   ├── facility/
│   │   ├── concept-note.pdf
│   │   ├── facility-strategy-vedlegg-g.pdf
│   │   └── norbygg-lease-agreement
│   ├── equipment/
│   │   ├── mazak-loi
│   │   ├── cnc-utilization-validation-vedlegg-d.pdf
│   │   └── equipment-specifications/
│   └── quality/
│       └── iso-certification-roadmap
├── 05-legal/
│   ├── ip/
│   ├── contracts/
│   │   ├── employment-agreements/
│   │   ├── advisory-agreements/
│   │   └── supplier-contracts/
│   └── compliance/
├── 06-team/
│   ├── team-governance-vedlegg-f.pdf
│   ├── founders/
│   │   ├── cvs/
│   │   └── references/
│   └── advisors/
└── 07-presentations/
    ├── investor-pitch-v3.pdf
    └── executive-summary
```

## Investor Types & Their DD Focus

| Investor Type | Primary Focus | Depth | Timeline |
|---------------|--------------|-------|----------|
| Pre-Seed Angels | Team, market, concept | Light | 2-4 weeks |
| Seed VC | Market, business model, financials | Medium | 4-8 weeks |
| Series A VC | Financials, operations, scalability | Deep | 8-12 weeks |
| Strategic Corporate | Technology fit, synergy | Very deep | 12-16 weeks |
| Family Office | Team integrity, long-term vision | Medium-deep | 6-10 weeks |

## DD Best Practices

**Before DD starts:** Organize VDR, run internal pre-DD with advisors, fill documentation gaps, prepare top-50 Q&A document, set up secure data room.

**During DD:** Respond within 24 hours, track all questions in a log (question, answer, source doc, responder, date), over-communicate, flag issues proactively, maintain single source of truth.

**After DD:** Debrief on questions asked, update documentation, improve VDR for next round, archive all Q&A.

## Red Flags to Avoid

**Financial:** Overly aggressive projections without justification, unrealistic assumptions, missing sensitivity analyses, unclear use of funds, cap table complexity.

**Technical:** Unproven technology without validation, single supplier dependency without backup, unrealistic timeline, no risk mitigation.

**Team:** Founder conflicts or unclear roles, lack of relevant experience, weak advisory board, high turnover.

**Legal:** Unclear IP ownership, no founder vesting, undocumented material agreements, regulatory gaps.

## Key Messages (Consistent across all DD)

1. **55-65% CNC utilization is validated** — not aspirational. See Vedlegg D (DMG MORI, MAZAK, Siemens reference data).
2. **3x labor efficiency is the moat** — 0.8 vs 2.5 people per CNC. Impossible to retrofit in brownfield.
3. **Pre-revenue by design** — Q3 2027 production start. All projections are forward-looking with validated assumptions.
4. **Capital discipline** — Phased investment, leased facility, strong CNC resale values (Vedlegg E).
5. **European answer to Hadrian** — Same structural need, different capital philosophy (Vedlegg C).
6. **Founders retain control** — 53.4% ownership at exit, active board participation.
