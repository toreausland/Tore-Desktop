---
name: aurelian-startup
description: Full VDR session initialization skill for Aurelian Manufacturing. Loads all VDR documents, master financial document, design manual, and project instructions. Use this skill when starting a new session, or when the user says "load project", "start session", or "/aurelian-startup".
---

# Aurelian Startup — Session Initialization

> **Basic startup is automatic** via SessionStart hook in `.claude/settings.local.json`.
> **This skill** is for FULL document load (reads all VDR docs + master PDF + design manual).
> **Trigger:** User says "load project", "start session", or "/aurelian-startup"

---

## PROCEDURE (Execute in order)

### Step 1: Read the Master Document
Read the master financial document:
```
Aurelian_VDR/02_Financial/2.4_Economic_Tables_Projections/02_Economic_Tables_Projections_REV6.pdf
```
Read ALL pages. Confirm the 17 checkpoint values match MEMORY.md. If any value differs, STOP and alert the user — the master document may have been updated.

### Step 2: Read All VDR Documents
Read these 10 .md documents (use parallel reads for speed):

1. `Aurelian_VDR/00_Executive_Summary/Executive_Summary_2page_V1.md`
2. `Aurelian_VDR/00_Executive_Summary/Investment_Teaser_One_Pager_V1.md`
3. `Aurelian_VDR/02_Financial/2.5_Sensitivity_Analysis/Sensitivity_Analysis_V1.md`
4. `Aurelian_VDR/02_Financial/2.6_Use_of_Funds/Use_of_Funds_V1.md`
5. `Aurelian_VDR/03_Commercial_Market/3.2_Competitive_Landscape/CNC_Benchmark_Competitive_Landscape_V1.md`
6. `Aurelian_VDR/03_Commercial_Market/3.4_Go_To_Market_Strategy/Go_To_Market_Strategy_V1.md`
7. `Aurelian_VDR/03_Commercial_Market/3.5_Pricing_Revenue_Model/Pricing_Revenue_Model_V1.md`
8. `Aurelian_VDR/04_Technical_Operations/4.5_Quality_Certifications/Quality_Certification_Roadmap_V1.md`
9. `Aurelian_VDR/04_Technical_Operations/4.6_Production_Timeline/Production_Timeline_V1.md`
10. `Aurelian_VDR/04_Technical_Operations/4.7_Risk_Register/Risk_Register_V1.md`
11. `Aurelian_VDR/06_Team/6.4_Key_Hires_Plan/Key_Hires_Plan_V1.md`

### Step 3: Read the Design Manual
```
Design MAnual/aurelian-design-manual.md
```

### Step 4: Read the Project Instructions
```
claude-project-instructions.md
```

### Step 5: Confirm to User
After loading, report:
- "Session initialized. Loaded: master document, 10 VDR documents, design manual, project instructions."
- Flag any files that could not be read
- Flag any values that differ from MEMORY.md checkpoints

---

## RULES

- **NEVER skip the master document.** If it cannot be read, do not proceed with any financial work.
- **Read files in parallel** where possible to minimize load time.
- **Do not summarize or interpret** during loading — just read and confirm.
- **If a new .md document has been added** to the VDR since this skill was written, the user should update the file list above.

---

## REFERENCE FORMAT (from §3.3)

Full reference: `*02 Economic Tables & Projections* (VDR 02.04)`
Inline reference: `Ref: 02 Economic Tables & Projections, §[section] (VDR 02.04)`

**Examples with actual master document values:**
- Revenue 20 CNC @ 60% = ~315 MNOK → `Ref: 02 Economic Tables & Projections, §5.1 (VDR 02.04)`
- Seed: 51.3 MNOK equity + 29.3 MNOK debt = 80.6 MNOK total → `Ref: 02 Economic Tables & Projections, §4.1 (VDR 02.04)`
- Staffing 20 CNC: 16 ops + 4 admin = 20 total → `Ref: 02 Economic Tables & Projections, §1.3b (VDR 02.04)`
- EBIT 20 CNC @ 60% = ~222.3 MNOK → `Ref: 02 Economic Tables & Projections, §3.6 (VDR 02.04)`
