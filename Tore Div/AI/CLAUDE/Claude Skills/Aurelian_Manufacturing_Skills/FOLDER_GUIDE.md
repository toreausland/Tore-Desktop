# Aurelian Manufacturing — Skills Backup Folder

**Created:** 2026-02-09
**Version:** 1.0

---

## Folder Structure

```
Aurelian_Manufacturing_Skills/
│
├── 01_DD_Skills/                        ← BACKUP: Raw skill files
│   ├── aurelian-dd-coordinator/SKILL.md    Master DD orchestration
│   ├── aurelian-financial-dd/SKILL.md      Financial DD (valuation, model)
│   ├── aurelian-technical-dd/SKILL.md      Technical DD (CNC, facility)
│   ├── aurelian-market-dd/SKILL.md         Market DD (TAM, competition)
│   └── aurelian-legal-dd/SKILL.md          Legal DD (cap table, governance)
│
├── 02_Upload_Ready_ZIPs/                ← UPLOAD THESE to Claude
│   ├── aurelian-dd-coordinator.zip
│   ├── aurelian-financial-dd.zip
│   ├── aurelian-technical-dd.zip
│   ├── aurelian-market-dd.zip
│   └── aurelian-legal-dd.zip
│
├── 03_Documentation/                    ← Reference docs
│   ├── README.md                           Installation guide
│   └── claude-desktop-config-snippet.json  Config reference
│
└── 04_Source_Documents/                 ← Place your source PDFs here
    ├── Financial/
    │   ├── (place) Finansieringsplan_KOMPLETT.pdf
    │   ├── (place) Grunnlag_for_verdisetting.pdf
    │   └── (place) Analyse_av_Europeisk_VCPraksis.pdf
    ├── Vedlegg/
    │   ├── (place) Vedlegg_B_Økonomiske_tabeller.pdf
    │   ├── (place) Vedlegg_C_Sammenligning_investeringscaser.pdf
    │   ├── (place) Vedlegg_D_Kvalitativ_validering.pdf
    │   ├── (place) Vedlegg_E_CNC_Resale_Value.pdf
    │   ├── (place) Vedlegg_F_Team_Styre_Governance.pdf
    │   └── (place) Vedlegg_G_Verksted_Eiendomsstrategi.pdf
    ├── Market_Research/
    │   ├── (place) Defence_Market_Research.pdf
    │   ├── (place) Energy_Market_Research.pdf
    │   ├── (place) Critical_Markets_Research.pdf
    │   └── (place) Market_Trends_Projections.pdf
    └── Pitch_Materials/
        ├── (place) Investor_Pitch_V3.pdf
        ├── (place) Markedsanalyse_Master_V3.pdf
        └── (place) ConseptNote.pdf
```

---

## How to Upload Skills to Claude

1. Open Claude (web or desktop app)
2. Go to **Settings → Capabilities**
3. Ensure **Code execution and file creation** is ON
4. Scroll to **Skills** section
5. Click **"Upload skill"**
6. Upload each ZIP from `02_Upload_Ready_ZIPs/`, one at a time
7. Toggle each skill ON after upload

---

## How to Update a Skill

1. Edit the SKILL.md in `01_DD_Skills/[skill-name]/`
2. Re-zip the folder: right-click → Compress
3. In Claude Settings → Capabilities → Skills: delete the old version
4. Upload the new ZIP
5. Keep the old ZIP in a versioned subfolder if you want history

---

## Skill Trigger Cheat Sheet

| You want to...                  | Say this to Claude                          |
|---------------------------------|---------------------------------------------|
| Start DD preparation            | "Start DD preparation for Seed round"       |
| Defend the valuation            | "How do we justify 140 MNOK pre-money?"     |
| Show break-even analysis        | "What's our break-even?"                    |
| Validate CNC utilization        | "How do we achieve 65% utilization?"        |
| Show market size                | "What's the TAM for Aurelian?"              |
| Review cap table                | "Show me the cap table evolution"           |
| Check DD readiness              | "What's missing for DD?"                    |
| Run mock investor session       | "Simulate a Seed DD investor Q&A"           |
| Review competitive landscape    | "Who are our competitors?"                  |
| Explain the Hadrian comparison  | "How do we compare to Hadrian?"             |

---

## Version Log

| Version | Date       | Changes                                |
|---------|------------|----------------------------------------|
| 1.0     | 2026-02-09 | Initial build — 5 DD skills            |
|         |            |                                        |

---

*Confidential — Aurelian Manufacturing AS*
