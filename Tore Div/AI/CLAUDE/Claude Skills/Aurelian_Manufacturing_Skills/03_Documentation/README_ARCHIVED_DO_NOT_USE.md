# Aurelian Manufacturing — DD Skills Package

## Claude Desktop Installation Guide

### Overview

This package contains 5 specialized Due Diligence skills for Aurelian Manufacturing's fundraising journey (Pre-Seed → Seed → Series A). Designed for Claude Desktop to enable rapid, consistent, and professional handling of investor DD processes.

### Skills Included

| Skill | Purpose | File Size |
|-------|---------|-----------|
| `aurelian-dd-coordinator` | Master DD orchestration, checklists, VDR structure, routing | ~10 KB |
| `aurelian-financial-dd` | Financial model defense, valuation, break-even, ROI, comparables | ~12 KB |
| `aurelian-technical-dd` | CNC utilization validation, autonomous ops, suppliers, facility | ~12 KB |
| `aurelian-market-dd` | TAM/SAM/SOM, competition, defense/energy markets, go-to-market | ~12 KB |
| `aurelian-legal-dd` | Cap table, governance, IP, contracts, compliance | ~8 KB |

### Installation — Claude Desktop

#### Step 1: Locate Skills Directory

On macOS:
```
~/Library/Application Support/Claude/skills/
```

On Windows:
```
%APPDATA%\Claude\skills\
```

If the `skills` directory doesn't exist, create it.

#### Step 2: Copy Skill Folders

Copy the entire `aurelian-dd-skills/` contents into your skills directory:

```
skills/
├── aurelian-dd-coordinator/
│   └── SKILL.md
├── aurelian-financial-dd/
│   └── SKILL.md
├── aurelian-technical-dd/
│   └── SKILL.md
├── aurelian-market-dd/
│   └── SKILL.md
└── aurelian-legal-dd/
    └── SKILL.md
```

#### Step 3: Verify in Claude Desktop

Restart Claude Desktop. You should see the skills available in settings or they will trigger automatically based on your queries.

### Usage Guide

#### Quick Start Triggers

| What You Want | What to Say | Skill Triggered |
|---------------|-------------|-----------------|
| Overall DD status | "Review DD readiness" | dd-coordinator |
| Financial model questions | "Explain revenue assumptions" | financial-dd |
| Technology validation | "How do you achieve 65% utilization?" | technical-dd |
| Market sizing | "What's the TAM?" | market-dd |
| Legal/Corporate | "Show me the cap table" | legal-dd |
| General DD prep | "What's missing for DD?" | dd-coordinator |
| Mock DD session | "Run a mock DD for Seed round" | dd-coordinator → routes |

#### Example DD Session Workflow

1. Start with: *"Start DD preparation for Seed round"*
   - dd-coordinator activates, shows Seed checklist with gaps highlighted

2. Investor asks: *"How do you justify 140 MNOK pre-money?"*
   - financial-dd provides three-factor defense with data

3. Follow-up: *"What if utilization is only 40%?"*
   - financial-dd shows scenario analysis, still profitable

4. Technical probe: *"Prove 65% utilization is achievable"*
   - technical-dd presents Vedlegg D validation, benchmark data

5. Market question: *"Who are your first customers?"*
   - market-dd explains pipeline strategy, acknowledges LOI gap

### Key Data Sources

All skills trace back to these master documents:

| Document | Purpose | Domain |
|----------|---------|--------|
| Finansieringsplan KOMPLETT | ALL financial numbers | Financial |
| Markedsanalyse Master V3 | Comprehensive market analysis | All |
| Vedlegg C | Comparable cases (Hadrian) | Financial, Market |
| Vedlegg D | CNC utilization validation | Technical |
| Vedlegg E | CNC resale value analysis | Financial |
| Vedlegg F | Team & governance | Legal |
| Vedlegg G | Facility strategy | Technical, Legal |
| Defence Market Research | Defense sector deep dive | Market |
| Energy Market Research | Energy sector deep dive | Market |
| Critical Markets Research | Cross-sector analysis | Market |
| Investor Pitch V3 | Presentation materials | All |

### Critical Reminders

1. **All financial numbers from Finansieringsplan KOMPLETT** — not Vedlegg A (which has different Pre-Seed numbers)
2. **Pre-revenue company** — Q3 2027 production start. Focus on assumption validation.
3. **55-65% utilization is validated** — see Vedlegg D for engineering proof
4. **3x labor efficiency is the moat** — 0.8 vs 2.5 people per CNC
5. **Founders retain 53.4% at exit** — strong alignment
6. **Exit: 2.3B NOK @ 10-11x EBITDA** — conservative end of Industrial IoT range

### Documentation Gaps to Fill

Before Seed DD, these must be resolved:

**CRITICAL:**
- [ ] Customer LOIs (2-3 anchor customers)
- [ ] Shareholder agreement

**HIGH:**
- [ ] MAZAK purchase LOI
- [ ] Executed Norbygg lease
- [ ] Founder vesting schedules
- [ ] IP assignment agreements
- [ ] Employment agreements
- [ ] Detailed financial model (Excel with formulas)

**MEDIUM:**
- [ ] Advisory agreements (formalized)
- [ ] Monthly cash flow projections (2027-2028)
- [ ] Trademark registration
- [ ] Insurance coverage plan

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-09 | Initial build — all 5 DD skills |

### Contact

For questions about these skills or the DD process:
- Andre Tandberg (CEO): Strategy, capital, overall DD coordination
- Tore Ausland (VP BD): Customer pipeline, market validation
- Henrik Strom (Board/CFO): Financial DD, bank dialogue

---

*Built for Aurelian Manufacturing's fundraising journey. Confidential.*
