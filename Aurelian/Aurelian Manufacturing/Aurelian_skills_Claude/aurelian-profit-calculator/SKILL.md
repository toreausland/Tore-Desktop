---
name: aurelian-profit-calculator
description: Interactive investor profit calculator for Aurelian Manufacturing. Use this skill to build, update, or extend the web-based profit calculator that lets investors explore how CNC count, utilization %, and variable cost % affect revenue, cost, and profit. Triggers on "profit calculator", "investor calculator", "build calculator", "interactive model", "sensitivity explorer", "profit simulator", "what-if tool", or any request to create an investor-facing interactive financial exploration tool. This skill provides the EXACT formulas, design spec, variable ranges, cost structure, and UI requirements — all traceable to the master document.
---

# Aurelian Manufacturing — Profit Calculator Skill

> **Purpose:** Build and maintain an interactive, investor-facing profit calculator web application. Investors log in and adjust three variables to see real-time profit impact. All numbers trace to *02 Economic Tables & Projections* (VDR 02.04).

---

## 1. MASTER SOURCE

All financial numbers MUST trace to the master document:

| Priority | Document | Role |
|----------|----------|------|
| **1** | ***02 Economic Tables & Projections* (VDR 02.04)** | ABSOLUTE master for ALL financial numbers |
| **2** | **Design Manual** (aurelian-design-manual.md v2.0) | Visual formatting, brand identity |

### READ-BEFORE-BUILD RULE

Before building, updating, or modifying any part of this calculator:
1. **READ** the master document: `Aurelian_VDR/02_Financial/2.4_Economic_Tables_Projections/02_Economic_Tables_Projections_REV8.docx`
2. **READ** the design manual: `Design MAnual/aurelian-design-manual.md`
3. **VERIFY** the 17 checkpoint values
4. If you cannot read the master document: **STOP and inform the user**

---

## 2. THREE INVESTOR VARIABLES

The calculator exposes exactly three sliders/inputs. All other parameters are locked constants derived from the master document.

### 2.1 Variable: CNC Machine Count

| Property | Value |
|----------|-------|
| **Label** | Number of CNC Machines |
| **Range** | 5 – 25 |
| **Step** | 1 |
| **Default** | 20 (base case steady state) |
| **Type** | Integer slider with numeric input |

This drives: revenue capacity, depreciation, finance cost, staffing, other opex.

### 2.2 Variable: Utilization %

| Property | Value |
|----------|-------|
| **Label** | Asset Utilization (% of 8,760 hours) |
| **Range** | 10% – 70% |
| **Step** | 1% (slider), 0.1% (input field) |
| **Default** | 60% (base case target) |
| **Type** | Percentage slider with numeric input |

This is the **primary profit driver**. Utilization always refers to percentage of 8,760 theoretical hours per CNC per year. There is NO intermediate "available hours" concept.

### 2.3 Variable: Variable Cost %

| Property | Value |
|----------|-------|
| **Label** | Variable Cost (% of Revenue) |
| **Range** | 8% – 13% |
| **Step** | 0.25% (slider), 0.01% (input field) |
| **Default** | 8% (mature steady state) |
| **Type** | Percentage slider with numeric input |

**Maturity context labels (displayed alongside slider):**

| Position | Label |
|----------|-------|
| 13% | Startup (2027–2028) |
| 11.75% | Year 3 (2029) |
| 10.50% | Year 4 (2030) |
| 9.25% | Year 5 (2031) |
| 8% | Mature (2032+) |

---

## 3. LOCKED CONSTANTS (from Master Document)

These values are NOT adjustable by the investor. They are hardcoded into the calculator engine and displayed as reference.

### 3.1 Revenue Constants

| Parameter | Value | Source |
|-----------|-------|--------|
| Theoretical hours per CNC/year | 8,760 | Master doc §1.1 |
| Normalized hourly rate | 3,000 NOK | Master doc §1.1 |

### 3.2 Cost Constants

| Parameter | Value | Source |
|-----------|-------|--------|
| CAPEX per CNC (incl. automation) | 10,000,000 NOK | Master doc §1.2 |
| Depreciation life | 8 years | Master doc §1.2 |
| Annual depreciation per CNC | 1,250,000 NOK | 10M / 8yr |
| Shop base setup (one-time) | 8,600,000 NOK | Master doc §1.2c |
| Shop base depreciation | 1,075,000 NOK/year | 8.6M / 8yr |
| Facility lease (annual) | 5,200,000 NOK | Master doc §1.4 |
| Opex scaling factor | 150,000 NOK/CNC/year | Master doc §1.4 |
| Debt interest rate | 7.5% | Master doc §1.2 |
| Avg operational salary (incl. social) | 1,100,000 NOK/year | Master doc §1.3 |
| Avg admin salary (incl. social) | 1,400,000 NOK/year | Master doc §1.3 |
| Admin FTEs (constant) | 4 | Master doc §1.3 |
| Customer Program threshold | 45% utilization | Master doc §1.1 |
| Customer Program split | 50% above threshold | Master doc §1.1 |

### 3.3 Debt Structure (Phase-Specific)

| CNC Range | Debt per CNC | Rationale |
|-----------|-------------|-----------|
| 1–5 (Seed) | 5,000,000 NOK | 50% equity requirement |
| 6–20 (Serie A) | 7,000,000 NOK | 30% equity, proven ops |
| 21–25 (expansion) | 7,000,000 NOK | Same as Serie A terms |

**Shop base debt:** 4,300,000 NOK (50% of 8.6M)

**Total debt formula:**
```
total_debt = min(CNC, 5) * 5,000,000
           + max(0, CNC - 5) * 7,000,000
           + 4,300,000  (shop base)
finance_cost = total_debt * 0.075
```

### 3.4 Staffing Model (Sub-Linear)

Operational FTEs scale sub-linearly. Use this lookup/interpolation:

| CNC | Operational FTEs | Admin FTEs | Total |
|-----|-----------------|------------|-------|
| 5 | 6 | 4 | 10 |
| 10 | 10 | 4 | 14 |
| 15 | 13 | 4 | 17 |
| 20 | 16 | 4 | 20 |
| 25 | 20 | 4 | 24 |

**Interpolation:** Linear between points. For CNC values between table rows, interpolate operational FTEs linearly.

```
// Interpolation function
function getOperationalFTEs(cnc) {
    const table = [
        { cnc: 5, fte: 6 },
        { cnc: 10, fte: 10 },
        { cnc: 15, fte: 13 },
        { cnc: 20, fte: 16 },
        { cnc: 25, fte: 20 }
    ];
    // Clamp and interpolate
    if (cnc <= 5) return 6;
    if (cnc >= 25) return 20;
    for (let i = 0; i < table.length - 1; i++) {
        if (cnc >= table[i].cnc && cnc <= table[i + 1].cnc) {
            const ratio = (cnc - table[i].cnc) / (table[i + 1].cnc - table[i].cnc);
            return table[i].fte + ratio * (table[i + 1].fte - table[i].fte);
        }
    }
}
```

---

## 4. CALCULATION ENGINE (Exact Formulas)

### 4.1 Revenue

```
revenue = CNC * 8760 * (utilization / 100) * 3000
```

**Validation:** 20 CNC * 8,760 * 0.60 * 3,000 = 315,360,000 NOK (~315 MNOK)

### 4.2 Fixed Costs

```
personnel_ops = getOperationalFTEs(CNC) * 1,100,000
personnel_admin = 4 * 1,400,000  // = 5,600,000
total_personnel = personnel_ops + personnel_admin

depreciation_cnc = CNC * 1,250,000
depreciation_shop = 1,075,000

total_debt = min(CNC, 5) * 5,000,000 + max(0, CNC - 5) * 7,000,000 + 4,300,000
finance_cost = total_debt * 0.075

facility = 5,200,000
other_opex = CNC * 150,000

total_fixed = total_personnel + depreciation_cnc + depreciation_shop
            + finance_cost + facility + other_opex
```

### 4.3 Variable Costs

```
variable_costs = revenue * (variable_cost_pct / 100)
```

### 4.4 Total Costs

```
total_costs = total_fixed + variable_costs
```

### 4.5 Gross Profit

```
gross_profit = revenue - total_costs
```

### 4.6 Customer Program (50/50 Sharing)

```
if (utilization > 45) {
    revenue_at_threshold = CNC * 8760 * 0.45 * 3000
    revenue_above = revenue - revenue_at_threshold
    profit_above = revenue_above * (1 - variable_cost_pct / 100)
    customer_share = profit_above * 0.50
} else {
    customer_share = 0
}
```

### 4.7 Aurelian Profit (Final Output)

```
aurelian_profit = gross_profit - customer_share
```

### 4.8 Derived Metrics (Display)

```
ebit_margin = (aurelian_profit / revenue) * 100
revenue_per_cnc = revenue / CNC
break_even_util = // solve for utilization where gross_profit = 0
hours_sold = CNC * 8760 * (utilization / 100)
staff_ratio = (getOperationalFTEs(CNC) + 4) / CNC
```

### 4.9 Validation Checkpoints

The calculator MUST reproduce these master document values exactly:

| Input | Expected Output |
|-------|----------------|
| 20 CNC, 60%, 8% var | Revenue ~315 MNOK, Total cost ~92.75 MNOK, EBIT ~222.3 MNOK |
| 5 CNC, 24%, 13% var | Approximately break-even (~0 MNOK profit) |
| 20 CNC, 15%, 8% var | Revenue ~78.8 MNOK, EBIT ~5.0 MNOK |
| 20 CNC, 65%, 8% var | Revenue ~341.6 MNOK, EBIT ~246.8 MNOK |

---

## 5. UI OUTPUTS (What the Investor Sees)

### 5.1 Primary KPI Cards (always visible)

| KPI | Format | Example (20 CNC, 60%, 8%) |
|-----|--------|--------------------------|
| **Annual Revenue** | XXX MNOK | 315 MNOK |
| **Annual Profit** | XXX MNOK | ~222 MNOK |
| **EBIT Margin** | XX% | ~71% |
| **Break-Even Utilization** | XX% | ~14% |

### 5.2 Cost Breakdown Panel

| Component | Value |
|-----------|-------|
| Personnel (ops + admin) | XX.X MNOK |
| CNC Depreciation | XX.X MNOK |
| Shop Base Depreciation | X.X MNOK |
| Finance Cost | XX.X MNOK |
| Facility Lease | X.X MNOK |
| Variable Costs | XX.X MNOK |
| Other OpEx | X.X MNOK |
| **Total Cost** | **XX.X MNOK** |

### 5.3 Customer Program Panel (shown when util > 45%)

| Item | Value |
|------|-------|
| Revenue above 45% threshold | XX MNOK |
| Customer share (50/50) | XX MNOK |
| Aurelian retained profit | XX MNOK |

### 5.4 Visual Chart

**Stacked/waterfall chart** showing: Revenue → Fixed Costs → Variable Costs → Customer Program → Aurelian Profit

Or a **sensitivity line chart** showing profit across the utilization range (10–70%) at the currently selected CNC count and variable cost %.

### 5.5 Reference Data (Collapsed/Expandable)

| Data | Purpose |
|------|---------|
| Staffing table | Shows FTE count at selected CNC |
| Debt structure | Shows total debt and finance cost |
| Assumptions list | All locked constants with source refs |
| Master document reference | *02 Economic Tables & Projections* (VDR 02.04) |

---

## 6. DESIGN SPECIFICATION (Aurelian Brand)

### 6.1 Colors

| Element | Color | Hex |
|---------|-------|-----|
| Primary accent | Aurelian Red | `#F50537` |
| Primary text | Near-black | `#2B2B2B` |
| Secondary text | Medium gray | `#6B6B6B` |
| Panel backgrounds | Light gray | `#F5F5F5` |
| Dividers | Divider gray | `#D3D3D3` |
| Dark panels / hero section | Pure black | `#000000` |
| Dark overlay on background image | Near-black 70% | `#2B2B2B` at 70% opacity |
| Chart axis | Axis gray | `#888888` |
| Dark theme cards | Navy card | `#253B52` |
| Dark theme accent text | Steel blue | `#8EAEC5` |

### 6.2 Typography

| Element | Font | Weight | Size |
|---------|------|--------|------|
| Display title | Calibri, sans-serif | Bold | 54px (hero) |
| Section headings | Calibri, sans-serif | Bold | 36px |
| Sub-headings | Calibri, sans-serif | Bold | 20px |
| KPI numbers | Calibri, sans-serif | Bold | 28–36px |
| KPI labels | Calibri, sans-serif | Regular | 12–14px |
| Body text | Calibri, sans-serif | Regular | 14px |
| Small/caption | Calibri, sans-serif | Regular | 11–12px |
| Chart labels | Arial, sans-serif | Regular/Bold | 10–11px |

### 6.3 Number Display Rules

- **NEVER display numbers in red text** — red numbers imply negative values
- KPI numbers: White text on `#F50537` background badge (Option A from design manual)
- Or: `#2B2B2B` text with small red accent element adjacent (Option B)
- Negative numbers: Use parentheses, e.g., `(2.5)` — NEVER red text
- Format: Use `#,##0` for integers, `#,##0.0` for one decimal in MNOK
- Percentages: Always with `%` symbol, no space

### 6.4 Slider Design

- Track: `#D3D3D3` background, `#F50537` filled portion
- Thumb: `#F50537` circle with white border
- Value label: Bold, `#2B2B2B`, displayed above or beside slider
- Range labels: `#6B6B6B`, at slider endpoints

### 6.5 Background Image / Hero Section

- **Background:** High-resolution image of modern CNC machine shop with automation/robotics
- **Treatment:** Image with `#2B2B2B` overlay at 70% opacity (per design manual §8.1)
- **Text on image:** `#FFFFFF` primary, `#F50537` accent highlights
- **Purpose:** Hero section at top of calculator page — "Profit Calculator" title over industrial imagery

### 6.6 Layout Structure

```
┌─────────────────────────────────────────────────────┐
│  HERO SECTION (background image + dark overlay)     │
│  "Aurelian Manufacturing"                           │
│  "Profit Calculator" — #F50537                      │
│  "Explore how utilization, scale, and maturity      │
│   drive profitability" — #FFFFFF                    │
├─────────────────────────────────────────────────────┤
│  THREE SLIDERS (horizontal, full-width)             │
│  [CNC Machines: 5 ▬▬▬▬●▬▬ 25]                     │
│  [Utilization: 10% ▬▬▬▬●▬▬ 70%]                   │
│  [Variable Cost: 8% ▬▬●▬▬▬▬ 13%]                  │
├─────────────────────────────────────────────────────┤
│  KPI CARDS (4 across, white on red or black)        │
│  [Revenue] [Profit] [EBIT Margin] [Break-Even]     │
├─────────────────────────────────────────────────────┤
│  CHART (profit waterfall or sensitivity line)       │
├─────────────────────────────────────────────────────┤
│  COST BREAKDOWN (expandable panel, table format)    │
├─────────────────────────────────────────────────────┤
│  CUSTOMER PROGRAM (shown when util > 45%)           │
├─────────────────────────────────────────────────────┤
│  ASSUMPTIONS & REFERENCES (collapsed by default)    │
│  CONFIDENTIAL | February 2026 | Aurelian Mfg       │
└─────────────────────────────────────────────────────┘
```

### 6.7 Responsive Behavior

- Desktop: 3-column KPI layout, side-by-side chart + cost breakdown
- Tablet: 2-column KPI, stacked sections
- Mobile: Single column, sliders full-width

---

## 7. AUTHENTICATION (Simple Investor Login)

### 7.1 Requirements

- Simple login gate before accessing the calculator
- No self-registration — admin creates investor credentials
- Session-based (no sensitive financial data stored client-side)
- "CONFIDENTIAL" watermark visible on all screens

### 7.2 Recommended Implementation

| Component | Recommendation |
|-----------|---------------|
| Auth provider | Supabase Auth (free tier) or simple JWT with hashed passwords |
| Storage | Supabase (PostgreSQL) or JSON file for small investor list |
| Session | HTTP-only cookie or localStorage JWT |
| UI | Modal login form with Aurelian branding |

### 7.3 Login Screen Design

- Background: Same CNC shop image with dark overlay
- Centered card: White, rounded corners, `#F50537` top accent bar
- Fields: Email + Password
- Button: `#F50537` background, white text, "Sign In"
- Logo: Aurelian Manufacturing logo above form
- Footer: "CONFIDENTIAL — Authorized Investors Only"

---

## 8. DISCLAIMERS (Always Visible)

The calculator MUST display these disclaimers:

**Bottom of calculator (always visible):**
> All projections are based on design targets for a pre-revenue company and are not guarantees of future performance. Numbers derived from *02 Economic Tables & Projections* (VDR 02.04). The hourly rate of 3,000 NOK is a conservative floor — defense and energy sector rates are typically higher. The Customer Program (50/50 sharing above 45% utilization) is modeled fleet-wide; actual application is per-customer, resulting in higher Aurelian profit retention than shown.

**Expandable "About This Model" section:**
- Revenue formula: CNC count x 8,760 hours x utilization% x 3,000 NOK
- Variable cost declines from 13% (startup) to 8% (mature) as operations optimize
- Staffing scales sub-linearly (0.8 FTE/CNC design target at scale)
- All costs from *02 Economic Tables & Projections* (VDR 02.04)
- Break-even at 5 CNC (Seed configuration): ~24% utilization

---

## 9. TECH STACK OPTIONS

| Option | Stack | Best For |
|--------|-------|----------|
| **A (Recommended)** | Next.js + Tailwind + Supabase | Full-featured, deployable, auth built-in |
| **B** | Single HTML file + vanilla JS | Quick prototype, zero dependencies |
| **C** | React SPA + Firebase Auth | Familiar stack, fast auth |

All options must use Calibri/Arial fonts, Aurelian color palette, and pass the 4 validation checkpoints in §4.9.

---

## 10. CLAIMS DISCIPLINE (From Project Instructions §2.2)

The calculator is an investor-facing tool. Every label and tooltip must follow claims discipline:

- Use "Design target" not "We achieve"
- Use "The model projects" not "Revenue will be"
- Label all outputs as "Projected" or "Model estimate"
- Include source reference to master document
- Separate projections from established facts

---

*This skill is the single source of truth for the Aurelian Profit Calculator. All implementations must adhere to these specifications without exception.*
