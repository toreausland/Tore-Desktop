# INSTRUKS TIL CLAUDE (Cowork) — Generer Word-dokumenter for Aurelian VDR

> **Kopier alt under denne linjen og lim inn som første melding i Cowork-sesjonen.**
> **Last opp filene listet i Steg 1 FØR du sender meldingen.**

---

## Oppdrag

Du skal generere **profesjonelle Word-dokumenter (.docx)** for de 9 VDR-dokumentene som er vedlagt som markdown-filer (+ 1 .docx/.pdf). Hvert dokument skal følge Aurelian Manufacturing sin design manual nøyaktig.

---

## Steg 1 — Last opp disse filene

Last opp følgende filer til denne samtalen **før du starter**:

### Master-dokument (MUST READ FIRST):
1. `02_Economic_Tables_Projections_REV6.pdf` — dette er master-dokumentet for ALLE tall

### Design Manual:
2. `aurelian-design-manual.md` — komplett stilguide for alle dokumenter

### De 9 VDR-dokumentene som skal bli Word-filer:
3. `00_Executive_Summary_2page_V1.md` (VDR 00.01)
4. `07_Investment_Teaser_OnePager_V1.md` (VDR 00.02)
5. `02_Sensitivity_Analysis_V1.md` (VDR 02.05)
6. `02_Use_of_Funds_Seed_V1.md` (VDR 02.06)
7. `03_Competitive_CNC_Benchmark.md` (VDR 03.02)
8. `03_Go_To_Market_Strategy_V1.md` (VDR 03.04)
9. `03_Pricing_Revenue_Model_V1.md` (VDR 03.05)
10. `06_Key_Hires_Plan_V1.md` (VDR 06.04)
11. `03_Market_Trends_Projections.docx` ELLER `.pdf` (VDR 03.06) — **NYTT DOKUMENT, se spesialinstruks nedenfor**

> **Merk:** Dokumentene 04_Quality_Certification_Roadmap_V1.md (VDR 04.05), 04_Production_Timeline_V1.md (VDR 04.06), og 04_Risk_Register_V1.md (VDR 04.07) er også tilgjengelige om du vil inkludere dem — men de 9 over er prioritet.

### VIKTIG — Dokument 11: 03_Market_Trends_Projections (VDR 03.06)

**Bakgrunn:** Dette dokumentet erstatter det utgåtte `DRAFT_03_Market_Analysis_Master_Report` som lå under `3.1_Market_Analysis/`. Det nye dokumentet er den offisielle markedsanalysen og investor-rapporten.

**Spesialinstrukser for dette dokumentet:**
- Originalen er skrevet på **norsk**. Generer Word-versjonen på **engelsk** (som alle andre VDR-dokumenter).
- Dokumentet er vesentlig lengre (~11 kapitler) enn de andre .md-filene. Det dekker: markedssammenligning, CNC-utnyttelse benchmark, forretningsmodell, økonomisk analyse, investerings-/finansieringsplan, avkastning, kundesegmentering, implementering og risiko.
- **§2.2-regelen er spesielt viktig her:** Dokumentet inneholder side-om-side sammenligninger av Aurelians design targets vs. observerte industritall. Sørg for at dette er tydelig merket i Word-versjonen (f.eks. med fotnoter eller callout-bokser som sier "Design target — pre-revenue" vs. "Observed industry data").
- **Noen tall i dette dokumentet avviker fra master-dokumentet.** Bruk ALLTID tallene fra master-dokumentet. Kjente avvik:
  - Dokumentet bruker 4 CNC i 2028 → master doc sier 5 CNC (Seed)
  - Dokumentet bruker ramp-up 4+4+6+6 → master doc bruker 5 (Seed) + 15 i 3x5 transjer (Serie A)
  - Dokumentet viser ~102.5 MNOK totalkost → master doc viser ~92.75 MNOK
  - Dokumentet viser admin 4.2 MNOK → master doc viser 5.6 MNOK (4 FTE x 1.4 MNOK)
  - Når det er tvil: **master-dokumentet vinner alltid**
- **Vedlegg-referanser:** Dokumentet refererer til "Vedlegg A-G". Disse skal oversettes til VDR-seksjonsnummer i Word-versjonen:
  - Vedlegg B (Økonomiske tabeller) → *02 Economic Tables & Projections* (VDR 02.04)
  - Vedlegg E (CNC Resale Value) → VDR 02.05 Sensitivity Analysis
  - Vedlegg F (Team) → VDR 06
  - Vedlegg G (Verksted) → VDR 04.04

---

## Steg 2 — Obligatoriske regler

### A. MASTER DOCUMENT REGEL
- **"02 Economic Tables & Projections"** (VDR 02.04) er det permanente master-dokumentet for ALLE finansielle tall — uavhengig av revisjon.
- Filen som skal leses heter `02_Economic_Tables_Projections_REV6.pdf` (nåværende revisjon på disk).
- Kryss-sjekk ALLE tall i markdown-filene mot PDF-en. Hvis det er avvik, bruk tallene fra PDF-en.
- **ALDRI skriv revisjonsnummer i selve Word-dokumentene.** Referér til master-dokumentet slik i all brødtekst:
  - ✅ *02 Economic Tables & Projections* (VDR 02.04)
  - ✅ Ref: 02 Economic Tables & Projections, §5.1 (VDR 02.04)
  - ❌ ~~02 Economic Tables & Projections REV6~~ (VDR 02.04)
  - ❌ ~~REV6~~
- **Grunn:** Når en ny revisjon kommer, skal alle dokumenter fortsatt være korrekte uten å oppdatere referanser.

### B. KRITISKE 17 KONTROLLPUNKTER (verifiser mot PDF)

| # | Parameter | Verdi |
|---|-----------|-------|
| 1 | Omsetning ved 20 CNC, 60% utnyttelse | ~315 MNOK |
| 2 | Total kostnad ved 20 CNC steady state | ~92.75 MNOK (8% var.) |
| 3 | Break-even ved 5 CNC (Seed) | ~24% utnyttelse |
| 4 | Bemanningsratio ved skala | 0.8 FTE/CNC |
| 5 | Variable kostnader (2032+ steady state) | 8% av omsetning |
| 6 | Variable kostnader (2027-2028 oppstart) | 13% av omsetning |
| 7 | Exit-verdsettelse (base case) | 2.3 mrd NOK (10x EBITDA) |
| 8 | Founders post-Serie A | 50.60% |
| 9 | Akkumulert resultat 2027-2035 | ~1,254 MNOK |
| 10 | Seed pre-money verdsettelse | 130 MNOK |
| 11 | CAPEX per CNC (inkl. automasjon) | 10 MNOK |
| 12 | Første omsetning | August 2027 |
| 13 | Seed-maskiner | 5 CNC |
| 14 | Serie A-maskiner | 15 CNC (3x5 transjer) |
| 15 | Total egenkapital (alle runder) | 101.3 MNOK |
| 16 | Shop base oppsett (per anlegg) | 8.6 MNOK |
| 17 | Timepris (konservativt gulv) | 3,000 NOK |

### C. KJENTE FEIL-VERDIER (BRUK ALDRI DISSE)

| Feil | Korrekt |
|------|---------|
| 47 MNOK seed | **51.3 MNOK** |
| 53.4% founders | **50.60%** |
| 140 MNOK pre-money | **130 MNOK** |
| 8 CNC seed | **5 CNC** |
| 4.0 MNOK facility lease | **5.2 MNOK** |
| 8 MNOK per CNC | **10 MNOK** |

### D. §2.2-REGELEN (Claims Discipline)
- Aurelians tall er **DESIGN TARGETS** for et pre-revenue selskap.
- Industritall er **OBSERVERTE DATA**.
- ALDRI presenter dem side om side som sammenlignbare datatyper uten tydelig merking.

---

## Steg 3 — Word Document Design Manual (forenklet)

Følg disse reglene for HVERT dokument:

### Sideformat
- A4 portrett, 2.5 cm marginer på alle sider
- Header: "Aurelian Manufacturing" høyrejustert, 9pt Calibri Regular, `#6B6B6B`
- Footer: Sidetall sentrert, "CONFIDENTIAL" venstrejustert, dato høyrejustert — alt 9pt `#6B6B6B`
- Første side: 3pt `#F50537` horisontal linje øverst som brand-element

### Typografi (KUN Calibri)
| Element | Størrelse | Vekt | Farge |
|---------|-----------|------|-------|
| Tittel | 28pt | Bold | `#2B2B2B` |
| Heading 1 | 22pt | Bold | `#2B2B2B` |
| Heading 2 | 16pt | Bold | `#F50537` |
| Heading 3 | 13pt | Bold | `#2B2B2B` |
| Brødtekst | 11pt | Regular | `#2B2B2B` |
| Bildetekst | 9pt | Regular | `#6B6B6B` |

- Linjeavstand: 1.15 for brødtekst, 1.0 for overskrifter
- 6pt mellomrom etter avsnitt

### Fargepalett
| Farge | Hex | Bruk |
|-------|-----|------|
| Aurelian Red | `#F50537` | Heading 2, aksentdetaljer, merker |
| Near-black | `#2B2B2B` | Primær tekst |
| Medium Gray | `#6B6B6B` | Sekundær tekst, fotnoter |
| Panel Gray | `#F5F5F5` | Kortbakgrunner, tabellrader |
| Divider Gray | `#D3D3D3` | Skillelinjer, tabellkanter |

### Tabeller
- Header-rad: `#2B2B2B` bakgrunn, hvit tekst, 11pt Bold
- Annenhver rad: `#FFFFFF` / `#F5F5F5`
- KUN horisontale skillelinjer (0.5pt `#D3D3D3`), INGEN vertikale
- Tall høyrejustert
- Sum-rad: Bold med 1.5pt `#2B2B2B` topplinje

### Nøkkeltall / KPI-er
- **ALDRI** vis tall i rød tekst (impliserer negativt)
- Bruk hvit tekst på rød bakgrunn (`#F50537`) for KPI-merker
- Eller svart tekst (`#2B2B2B`) med rød aksent ved siden av

### Callout-bokser
- Bakgrunn: `#F5F5F5`
- Venstre kant: 3pt solid `#F50537`
- Padding: 12pt
- Tekst: 11pt Calibri Regular `#2B2B2B`

### E. REFERANSELISTE I SLUTTEN AV HVERT DOKUMENT

Hvert Word-dokument SKAL ha en **"References"**-seksjon på siste side, som lister alle VDR-dokumenter som er sitert i dokumentet. Format:

```
References

| VDR ref | Document |
|---------|----------|
| 02.04 | 02 Economic Tables & Projections (master document) |
| 03.02 | CNC Benchmark & Competitive Landscape |
| 03.05 | Pricing & Revenue Model |
```

- Bruk Heading 2-stil (`#F50537`, 16pt Bold) for "References"
- Bruk standard tabell-stil (dark header, alternating rows)
- Inkluder KUN dokumenter som faktisk er referert i teksten
- **INGEN revisjonsnummer** i referanselisten — kun dokumentnavn og VDR-ref

### F. OBLIGATORISK SJEKK FØR HVERT DOKUMENT

Før du oppretter eller reviderer HVERT enkelt dokument i denne oppgaven:
1. Les master-dokumentet på nytt (`02_Economic_Tables_Projections_REV6.pdf`)
2. Les design-manualen (`aurelian-design-manual.md`)
3. Bekreft at de 17 kontrollpunktene stemmer
4. **Denne sjekken gjelder for HVER ny dokumentforespørsel i samtalen — ikke bare den første**

---

## Steg 4 — Filnavn

Bruk dette formatet for hvert dokument:

```
[VDR-ref]_[Dokument_Navn]_V1.docx
```

Eksempler:
- `00.01_Executive_Summary_V1.docx`
- `00.02_Investment_Teaser_OnePager_V1.docx`
- `02.05_Sensitivity_Analysis_V1.docx`
- `02.06_Use_of_Funds_Seed_V1.docx`
- `03.02_CNC_Benchmark_Competitive_Landscape_V1.docx`
- `03.04_Go_To_Market_Strategy_V1.docx`
- `03.05_Pricing_Revenue_Model_V1.docx`
- `03.06_Market_Trends_Projections_V1.docx`
- `06.04_Key_Hires_Plan_V1.docx`

---

## Steg 5 — Leveranse

For hvert dokument:
1. Les markdown-filen nøye
2. Kryss-sjekk alle tall mot master PDF-en
3. Generer Word-dokument med korrekt formatering
4. Bekreft at alle 17 kontrollpunkter er riktige der de forekommer
5. Lever som nedlastbar .docx-fil

**Prioritert rekkefølge:**
1. Executive Summary (VDR 00.01) — viktigst, dette er "first impression"
2. Investment Teaser One-Pager (VDR 00.02)
3. Use of Funds (VDR 02.06)
4. Sensitivity Analysis (VDR 02.05)
5. Pricing & Revenue Model (VDR 03.05)
6. Market Trends & Projections (VDR 03.06) — **nytt dokument, oversettes NO→EN, krysssjekk mot master doc**
7. Go-To-Market Strategy (VDR 03.04)
8. CNC Benchmark (VDR 03.02)
9. Key Hires Plan (VDR 06.04)

---

## Språk

Alle dokumenter skal være på **engelsk**. Bruk profesjonell, presis tone. Skandinavisk minimalisme — la tallene snakke.

---

## Viktig sluttmerknad

Når du er ferdig med alle 9, gi meg en oppsummering med:
- Filnavn for hvert dokument
- Antall sider
- Eventuelle avvik funnet mellom kildedokumenter og master PDF (spesielt for VDR 03.06)
- Eventuelle designvalg du tok
- For VDR 03.06: Liste over tall som ble korrigert fra originaldokument til master-dokument-verdier
