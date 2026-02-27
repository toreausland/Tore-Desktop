---
name: aurelian-cnc-pricing
description: Industri 4.0-basert prisingsmodell for CNC-operasjoner hos Aurelian Manufacturing. Bruk denne skill når du skal kalkulere, forklare eller bygge prismodeller for CNC-jobber — inkludert stykkpriser, batchpriser, maskinsatser, tilbudskalkulasjon, usikkerhetsanalyse (P50/P80), og Industri 4.0-integrering (TDABC, digital tvilling, OPC UA/MTConnect). Trigges på "pris en del", "CNC-kalkulator", "hva koster det å maskinere", "tilbudskalkulasjon", "machining quote", "syklustid", "maskinsats", "TDABC", "kostnadsbrudd CNC", "setup-kost", "QC-kostnad", "5-akse pris", "batch-kalkule", "dreiing pris", "fresing kost", "Industri 4.0 prising", "digitale tvillinger prising", eller enhver forespørsel om å prise eller kalkulere CNC-operasjoner.
---

# Aurelian Manufacturing — CNC Prisings-Skill (Industri 4.0)

Denne skill inneholder komplett faglig grunnlag for å kalkulere, forklare og kommunisere CNC-priser hos Aurelian Manufacturing. Kildegrunnlag: interne forskningsrapport *"Industri 4.0-baserte beregningsmodeller for prising av CNC-operasjoner"* (prosjektfil `grundig-research-rapport.md`).

---

## PRINSIPP 1: Hybridmodell — bottom-up + datadrevet kalibrering

Aurelian bruker alltid en **hybrid** av:

1. **Bottom-up prosesskost** — beregner aktivitet for aktivitet: setup, programmering, syklustid, etterarbeid, QC
2. **Datadrevet kalibrering** — digitale tvillinger og sensordata korrigerer tidsestimater og kapasitetsutnyttelse løpende

**Aldri bruk kun én modell alene.** Én modell alene gir ikke simultant: hastighet (tilbud på minutter), forklarbarhet (hvorfor prisen ble slik), og nøyaktighet (for 5-akse/høy presisjon).

---

## PRINSIPP 2: TDABC som "motor" for satser

Beregn **kapasitetskost per time** for hver ressurs, multiplisert med tidsdrivere for jobben.

### Formel: Maskinsats per maskin
```
R_m = (A_fixed / H_pr) + v_energy + v_cons
```
Hvor:
- `H_pr` = praktiske maskintimer/år (planlagt tid × tilgjengelighet × realistisk utnyttelse)
- `A_fixed` = årlige faste kost (avskrivning, service, vedlikehold, areal, IT/lisenser, indirekte)
- `v_energy` = energikost per time (målt eller modellert)
- `v_cons` = forbruksmateriell per time

---

## SEKSJON 1: STANDARD SATSER (Aurelian defaults — skal kalibreres)

Disse er **illustrative startverdier** basert på norsk verkstedmarked og Industri 4.0-forskning. Alle satser skal erstattes med Aurelians egne tall fra regnskap, MES og maskindata.

| Ressurs | Symbol | Eksempel sats (NOK/h) | Kommentar |
|---|---:|---:|---|
| 2-akse CNC-dreiebenk | R_m | 1 150 | Kapitalkost moderat |
| 3-akse VMC (vertikalt maskineringssenter) | R_m | 1 300 | Typisk "allround" |
| 5-akse maskineringssenter | R_m | 1 850 | Høy CAPEX + risiko + mer QA |
| Operatør (maskin) | R_op | 750 | Skift-/kompetanseavhengig |
| Programmering/CAM | R_eng | 900 | Inkl. indirekte ingeniørkost |
| QC/CMM | R_qc | 950 | Måleutstyr + kompetanse |

**Referansepunkt norsk marked:** Åpne norske prislister viser verkstedtimer på ~976–980 NOK/time eks. mva. for mekanisk arbeid (kilde: Selfa, 2024). Høypresisjonssegmentet (Olje & Gass, Forsvar) har typisk premium via økt QA-tid og krav til dokumentasjon/sertifisering.

---

## SEKSJON 2: INPUTPARAMETERE FOR KALKULATOR

En fullstendig CNC-kalkulasjon krever data fra fire grupper:

### Gruppe A: Deldata
| Parameter | Eksempler | Kilde |
|---|---|---|
| Materiale | Legering, hardhet, bearbeidbarhetsfaktor | ERP/innkjøp, materialdatabase |
| Geometri | Bounding box, fjernet volum, antall oppspenninger, 5-akse tilgangsvinkler | CAD/STEP, feature extraction |
| Toleranser | Toleranseklasse, overflatekrav, sporbarhetskrav | Kundekrav, QMS |

### Gruppe B: Operasjonsdata
| Parameter | Eksempler | Kilde |
|---|---|---|
| Maskintype | 3-akse/5-akse, turn-mill, arbeidsrom, palett/robot | Maskinregister |
| Verktøy | Skjærehastighet, verktøylevetid, kjølevæske | CAM, verktøydatabase |
| Tider | Setup, syklustid, håndtering, etterarbeid, QC | CAM sim + OPC UA/MTConnect + MES |

### Gruppe C: Ressurs-/kostsentre
| Parameter | Eksempler | Kilde |
|---|---|---|
| Økonomi | Vedlikehold, avskrivning, energipris, OEE/utnyttelse | Regnskap, MES |
| Kapasitet | Praktiske timer/år, operatørkost, indirekte kost | HR, regnskap |

### Gruppe D: Risiko og krav
| Parameter | Eksempler | Kilde |
|---|---|---|
| Risiko | Skraprate, rework-rate, kollisjonsrisiko | Historikk, ML-modell |
| Krav | AQAP-nivå (Forsvar), NORSOK-regime (Olje & Gass), NDT, coating | Kontrakt, QMS |

---

## SEKSJON 3: KJERNFORMLER — TOTAL KOSTNAD

### Variabeldefinisjon

**Ordre/del:**
- `N` = batchstørrelse
- `s` = skraprate (andel, f.eks. 0.05 = 5%)
- `r` = rework-rate (andel)
- `C_mat` = materialkost (råemne + svinn)

**Tider (timer):**
- `t_prog` = programmering (CAM/NC, simulering, dokumentasjon)
- `t_setup` = oppspenning/omstilling
- `t_cycle` = syklustid per del (maskin)
- `t_hand` = manuell håndtering per del
- `t_post` = etterarbeid per del (deburr, vask, merking)
- `t_qc` = kvalitetskontroll per del (inkl. førsteartikkel)

**Satser (NOK/time):** R_m, R_op, R_qc, R_eng (se Seksjon 1)

**Andre kostnader:**
- `C_tool` = verktøykost per batch
- `C_ext` = eksterne prosesser (HT, NDT, coating, overflatebehandling)

### Batchkostnad
```
C_batch =
  R_eng × t_prog
  + (R_m + R_op) × t_setup
  + N × (R_m × t_cycle + R_op × t_hand + R_op × t_post + R_qc × t_qc)
  + C_tool + C_mat + C_ext
```

### Skrap/rework-justering
```
N_eff = N × (1 - s)                    # effektivt antall godkjente deler
t_re  = r × t_cycle × k                # rework-tid (k = rework-faktor, typisk 0.5–1.0)
```

### Stykkpris (internkost)
```
C_stk = C_batch / N_eff
```

### Tilbudspris med margin og risikotillegg
```
P_stk = C_stk × (1 + m) + risikotillegg
```
Hvor `m` er målmargin (typisk 12–25% avhengig av segment og risiko).

---

## SEKSJON 4: USIKKERHETSANALYSE — P50/P80

Aurelian bør alltid oppgi **P50 (most likely) og P80 (konservativt)** i stedet for kun punktestimat. Dette er spesielt kritisk for 5-akse/høypresisjon og prototyper.

### Fremgangsmåte
1. Bruk triangulære eller lognormale fordelinger for `t_setup`, `t_cycle`, `t_qc` basert på historiske avvik per maskin/materiale
2. Kjør Monte Carlo-simulering for å få fordeling på `C_stk`
3. Presenter resultat som P50 og P80
4. La kommersiell policy velge prisnivå (typisk: P50 for serieproduksjon, P80 for prototyper/forsvar)

**Hva som typisk driver variasjon:**
- Syklustidsvariasjon for 5-akse (CAM-simulering er systematisk optimistisk uten kalibrering)
- Setup-variasjon for nye deler/fixturinger
- QC-tid for komplekse geometrier og strenge toleranser

---

## SEKSJON 5: CASE-BEREGNINGER (maler)

### Case A: Enkeltstykke, høypresis 5-akse fresing

**Scenario:** N=1, høylegert materiale, stram toleranse, AQAP/forsvarskrav

| Kostelement | Tid | Sats (NOK/h) | Kost (NOK) |
|---|---:|---:|---:|
| Programmering/CAM | 6,0 h | 900 | 5 400 |
| Setup maskin | 2,0 h | 1 850 | 3 700 |
| Setup operatør | 2,0 h | 750 | 1 500 |
| Maskintid syklus | 1,2 h | 1 850 | 2 220 |
| Operatør under kjøring | 0,8 h | 750 | 600 |
| Etterarbeid (deburr/vask) | 0,5 h | 750 | 375 |
| QC (førsteartikkel + rapport) | 1,5 h | 950 | 1 425 |
| Verktøyslitasje/spesial | — | — | 1 200 |
| Material + svinn | — | — | 1 800 |
| **Sum internkost** | | | **18 220** |

**Prissetting:**
- Skraprisiko 10% → C_stk / (1 – 0.10) ≈ 20 244 NOK
- + 20% margin → **~24 300 NOK** (avrundet tilbudspris)

---

### Case B: Liten serie, turn-mill / 3-akse + dreiing

**Scenario:** N=20, moderat toleranse

| Kostelement | Tid/mengde | Sats | Kost (NOK) |
|---|---:|---:|---:|
| Programmering/CAM | 4,0 h | 900 | 3 600 |
| Setup maskin | 2,5 h | 1 300 | 3 250 |
| Setup operatør | 2,5 h | 750 | 1 875 |
| Syklustid (0,35 h × 20) | 7,0 h | 1 300 | 9 100 |
| Operatør/håndtering (0,10 h × 20) | 2,0 h | 750 | 1 500 |
| Etterarbeid (0,05 h × 20) | 1,0 h | 750 | 750 |
| QC (0,20 h × 20) | 4,0 h | 950 | 3 800 |
| Verktøy | — | — | 1 000 |
| Material | — | — | 4 000 |
| **Sum internkost** | | | **28 875** |

- Stykkpris internkost: 28 875 / 20 = **1 444 NOK/stk**
- + 15% margin → **~1 660 NOK/stk**, batch ≈ **~33 200 NOK**

---

### Case C: Stor serie, 3-akse med palett/automatisering

**Scenario:** N=500, god repeterbarhet, lav toleransekompleksitet

| Kostelement | Tid/mengde | Sats | Kost (NOK) |
|---|---:|---:|---:|
| Programmering/CAM | 10,0 h | 900 | 9 000 |
| Setup maskin | 4,0 h | 1 300 | 5 200 |
| Setup operatør | 4,0 h | 750 | 3 000 |
| Syklustid (0,08 h × 500) | 40,0 h | 1 300 | 52 000 |
| Operatør/håndtering (0,02 h × 500) | 10,0 h | 750 | 7 500 |
| QC/SPC (0,01 h × 500) | 5,0 h | 950 | 4 750 |
| Verktøy/forbruk | — | — | 6 000 |
| Material | — | — | 25 000 |
| **Sum internkost** | | | **112 450** |

- Stykkpris internkost: 112 450 / 500 = **225 NOK/stk**
- + 12% margin → **~252 NOK/stk**, batch ≈ **~126 000 NOK**

---

## SEKSJON 6: PREMIUMDRIVERE FOR FORSVAR OG OLJE & GASS

### Forsvar (AQAP / NATO-krav)
Følgende elementer gir merkostnad i forsvarsleveranser og **skal alltid legges inn eksplisitt** i kalkulasjonen:

- **AQAP-2110 / AQAP-2310:** QC/inspeksjon, dokumentasjonspakker og revisjonsberedskap gir mer tid per batch
- **Sporbarhet og sertifikater:** materialsertifikater, NC-programversjon, fixture-ID, operatørlogg
- **Førsteartikkelinspeksjon (FAIR):** alltid separat QC-linje i kalkulator
- **Rework-risiko øker** når dokumentasjonskrav forsterkes (alt må dokumenteres på nytt)

**Praktisk:** Legg til 15–35% på QC-tid og 10–20% på indirekte kost for forsvarsjobber.

### Olje & Gass (NORSOK / Achilles JQS)
- **NORSOK-regime:** strengere prosess- og inspeksjonskrav enn standard industriell praksis
- **Leverandørkvalifisering:** Achilles JQS pre-kvalifisering gir overhead per jobb
- **Sporbarhet:** materialsertifikater (3.1/3.2), traceability per komponent
- **Lavere fleksibilitet:** mer overhead per jobb, vanskeligere å komprimere QC

**Praktisk:** Legg til 10–25% på QC-tid og 5–15% på indirekte kost for NORSOK-jobber.

---

## SEKSJON 7: INDUSTRI 4.0-KOMPONENTER

### Digital tvilling (ISO 23247)
- Holder maskinspesifikk syklustidsmodell (inkl. akselerasjon, kontrollerbegrensninger, verktøyskift)
- Sammenligner CAM/NC-simulert tid mot målt maskintid
- Lærer korrigeringsfaktorer per maskin, materiale og strategi over tid

### Maskindata via OPC UA og MTConnect
- **OPC UA (IEC 62541):** semantisk interoperabilitet, vertikal/horisontal kommunikasjon
- **MTConnect:** read-only, XML over HTTP — status, syklusstart/slutt, stopp, alarmer, feed-override
- Gir automatisk tidsmåling uten manuelle tidsstudier

### Maskinlæring — hva det brukes til
1. **Syklustidsestimat** fra NC-program/CAM-sim (sekvensmodeller, dyp læring)
2. **Ikke-skjærende tid** (oppspenning, manuell håndtering, verktøyskift, måling, rework) — høy variasjon, lav transparens i tradisjonelle modeller
3. **Forklarbar AI (XAI)** — knytter CAD-geometri til kostnad og synliggjør hva som driver prisen

**Anbefaling:** Bruk ML som kalibrerings- og forslagssystem (P50/P80) oppå en forklarbar bottom-up/TDABC-kjerne.

### Minimum datakrav for Industri 4.0-prising
En hendelsesmodell (event log) per jobb som minimum inneholder:
- Maskin-events: `cycle_start`, `cycle_end`, `idle_reason`
- Operatør-events: `setup_start/end`, `QC_start/end`, `rework_start/end`
- Kobling til ordre, operasjon og NC-programversjon

---

## SEKSJON 8: ALTERNATIVER FOR PRISINGSENHETER

| Enhet | Beste bruksområde | Kommentar |
|---|---|---|
| **Stykkpris/batchpris** | Produksjonskontrakter | Krever god amortisering av setup/programmering |
| **Timepris (maskin)** | Internkontroll, kapasitetsstyring | Mindre egnet kommersielt alene |
| **Enhetspris med fallback-time** | Service/vedlikeholdskontrakter | Standard i offentlig sektor (ref. Forsvarsbygg) |
| **Value-based pricing** | Forsvar/O&G, kritiske toleranser | Krever moden kommersiell policy, dokumentert leveranserisiko |

---

## SEKSJON 9: SYSTEMARKITEKTUR (referansemodell)

```
CAD/tegning + toleranser → Feature extraction → Kostmotor (TDABC/bottom-up)
CAM sim/NC-program → Simulert tid ────────────────────↗
Maskindata (OPC UA/MTConnect) → Faktisk syklus/stopp → Kalibrering plan vs. faktisk → ↗
ERP/MES (ordre, routing, material, operatørlogg) → Jobbdatamart ────────────────────↗

Kostmotor → Prisforslag + kostnadsbrudd
          → Usikkerhet P50/P80 + sensitivitet
          → Tilbuds-UI/API → ERP (ordrelinje/tilbud)
```

---

## SEKSJON 10: PRISINGSOUTPUT — HVA SOM ALLTID SKAL LEVERES

Enhver kalkyle fra Aurelian skal inneholde:

1. **Kostnadsbrudd** (programmering, setup, maskintid, operatør, verktøy, QC, etterarbeid, material, ekstern prosess)
2. **Tilbudspris** — P50 (most likely) og P80 (konservativt) med anbefalt risikotillegg
3. **Sensitivitet** — hvilke parametere driver kostnad mest (typisk: syklustid, setup, materialsvinn)
4. **Forutsetninger** — hvilke satser og tider er brukt, og om de er estimerte eller historisk kalibrerte

---

## SEKSJON 11: IMPLEMENTERINGSTIDSLINJE (referanse)

| Fase | Innhold | Estimert varighet |
|---|---|---|
| Datagrunnlag | Datamodell + kostsentre, minimum logging (maskin + MES) | 6 uker |
| Kalkulator v1 | Bottom-up + TDABC satser, rapport/tilbudseksport | 6 uker |
| Industri 4.0-lag | OPC UA/MTConnect ingest, kalibrering plan vs. faktisk | 12 uker |
| ML og kontinuerlig forbedring | ML for syklus + ikke-skjærende tid, governance | 12 uker |

---

## HURTIGREFERANSE: TYPISKE TIDSNØKLER

| Operasjon | Typisk tid | Variasjon |
|---|---|---|
| Setup, enkel 3-akse | 1–2 timer | Lav |
| Setup, 5-akse kompleks/fixture | 2–4 timer | Høy |
| Programmering, enkel del | 2–4 timer | Moderat |
| Programmering, 5-akse/kompleks | 6–12+ timer | Høy |
| QC, enkel stikkprøve | 0,1–0,2 h/del | Lav |
| QC, førsteartikkel + rapport | 1,5–3 timer | Moderat |
| Etterarbeid (deburr/vask) | 0,25–0,75 h/del | Moderat |

---

## VIKTIGE ADVARSLER

- **Åpne markedspriser for høypresisjons CNC i Forsvar/O&G er sjelden offentlig tilgjengelig.** Bruk egne historiske data for kalibrering fremfor konkurrentpriser.
- **CAM-simulert syklustid for 5-akse er systematisk optimistisk** uten kalibrering mot faktisk maskintid — alltid legg til korreksjonsfaktor fra historikk.
- **Timepris alene er ikke nok kommersielt** — kunden kjøper en del, ikke en time. Presenter alltid stykkpris/batchpris.
- **Ikke legg for mye indirekte kost på atypiske jobber** (prototyper, single-off) — disse har høy setup/QC per del og vil overprise standard produksjon hvis samme rate brukes.
