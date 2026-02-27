# Aurelian Manufacturing AS

## Industri 4.0 - Smart Factory CNC — Strategisk produksjonskapasitet for norsk forsvarsindustri

**Kapabilitetsmemorandum | Februar 2026 | KONFIDENSIELT**

---

## Hva vi bygger

Aurelian Manufacturing etablerer en greenfield Smart Factory for autonom CNC-produksjon i Våler, Østfold. Fabrikken bygges fra grunnen for presisjonsmaskinerig i High-Mix Low-Volume — segmentet som kjennetegner forsvarsindustriens produksjonsbehov: komplekse geometrier, krevende legeringer, strenge krav til sporbarhet og dokumentasjon, og varierende ordrevolumer.

Aurelian er et DeepTech-Industri selskap. Vi utvikler og eier programvarestacken som binder CNC-maskinene sammen med produksjonsplanlegging, kvalitetsstyring og kapasitetsoptimalisering. Denne vertikale integreringen er ikke et tillegg til driften — den er selve designgrunnlaget for fabrikken.

Ved full utbygging vil anlegget romme 25 CNC-maskiner med full automasjon og systemintegrering. Det gir en årlig reell produksjonskapasitet på inntil 140 000 spindeltimer.

---

## Vertikal integrering av programvarestacken

Aurelian bygger en gjennomgående dataarkitektur fra CNC-kontrollernivå til virksomhetsstyring. Arkitekturen følger ISA-95-rammeverket og bruker standardiserte industriprotokoller (OPC UA, MTConnect) for maskin-til-system-kommunikasjon. Hele stacken utvikles og eies internt.

I praksis betyr dette fire ting:

### Sanntidsdata fra maskin til styringssystem

Hver CNC-maskin rapporterer tilstand, syklustider, verktøyslitasje, alarmer og prosessparametere gjennom standardiserte grensesnitt. Dataene normaliseres og er tilgjengelige for planleggings- og styringssystemene i sanntid — ikke som manuelle rapporter etter skiftslutt, men som kontinuerlig datastrøm.

### Lukket optimaliseringssløyfe

Planlagt produksjonstid sammenlignes kontinuerlig med faktisk målt tid per maskin, materiale og operasjonstype. Avvik identifiseres automatisk og brukes til å korrigere fremtidige produksjonsplaner og tidsestimater. Systemet kalibrerer seg selv — det blir mer presist med hver produserte del.

### Sublineær bemanning

Fordi overvåkning, datainnsamling, hendelseshåndtering og produksjonsrapportering er automatisert, vokser bemanningsbehovet vesentlig saktere enn maskinparken. Å doble antall maskiner krever ikke dobbelt mannskap. Dette er en direkte konsekvens av den vertikale integreringen og en forutsetning for å drive 25 maskiner med høy utnyttelse i HMLV.

### Digital tråd fra ordre til leveranse

Hvert produsert emne kan spores gjennom hele verdikjeden: ordremottak, NC-programmering, oppspenning, maskinering, kvalitetskontroll, måledata, materialinformasjon og leveranse. Sporbarhetskravet er ikke et kompromiss vi gjør med effektiviteten — det er bygget inn i systemets grunnarkitektur.

---

## Produksjonskapasitet

| Parameter | Verdi |
|---|---|
| Maksimalt antall CNC-maskiner | 25 |
| Årlig kapasitet per maskin | 8 760 timer |
| Oppnåelig kapasitetsutnyttelse (design) | 65 % |
| OEE-A (tilgjengelighet) i HMLV | 80–85 % |
| **Årlig reell produksjonskapasitet ved full utbygging** | **ca. 140 000 timer** |

En OEE-A på 80–85 % i HMLV er vesentlig over det som er vanlig i segmentet. I konvensjonelle verksteder taper man tilgjengelighet til manuelle omstillinger, informasjonsflaskehalser mellom skift, uplanlagt verktøysvikt og venting på programmer, tegninger eller materialer. Aurelians Smart Factory-arkitektur adresserer hver av disse tapskildene systematisk:

- **Omstillingstid** reduseres gjennom standardiserte oppspenningsløsninger og automatisert verktøyhåndtering
- **Informasjonsflyt** er digitalisert — Numerical Control-programmer, arbeidsinstrukser og kvalitetsplaner følger ordren automatisk
- **Verktøyslitasje** overvåkes i sanntid og utløser planlagt bytte før svikt
- **Materialhåndtering** er integrert i cellelogistikken fra arkitektfasen

65 % kapasitetsutnyttelse er et designmål som tar høyde for planlagt vedlikehold, omstilling mellom ordrer, og den iboende variasjonen i HMLV-produksjon. Faktisk spindelkjøretid per tilgjengelig time er høyere, nettopp fordi OEE-A er designet til 80–85 %. Likevel krever slike mål gode samarbeid med våre største kunder, vi tror på å bygge verdier sammen.

---

## Maskinplattform

**Mazak** er valgt som CNC-leverandør, levert gjennom Ravema AS — autorisert nordisk distributør med full service, opplæring- og applikasjonskapasitet.

Plattformen omfatter blandt annet:

- Multi-tasking turn/mill-sentre for kombinert dreiing og fresing i samme oppspenning
- 5-akse simultanbearbeidingssentre for komplekse geometrier
- Dreisentre med drevet verktøy for effektiv produksjon av rotasjonssymmetriske komponenter
- Alle maskiner leveres automasjonsforberedt — designet for robotisert materialinnmating, palettløsninger og integrering mot fabrikkstyringssystemet

### Kundeinnflytelse på cellekonfigurasjon

Kunder som inngår samarbeid innen **august 2026** kan påvirke CNC-cellenes maskinsammensetning og konfigurasjon. Det betyr mulighet til å tilpasse:

- Maskintyper og arbeidsrom til egne komponentprofiler
- Verktøymagasin og oppspenningsløsninger til spesifikke materialer og geometrier
- Automasjonsgrad og cellelogistikk til forventet ordremønster

Denne muligheten eksisterer fordi maskinbestillinger er i sluttfasen og anlegget ennå ikke er bygget. Det er et viktig tidsvindu — en invitasjon og oppfordring til våre kunder om å delta aktivt.

---

## Anlegget

Aurelian bygger et nytt verksted på en **byggeklar tomt på 30 000 m²** i Våler, Østfold. Verkstedbygningen er på 2 635 m² (verkstedet har utvidelsespotensiale på 1000m²) og er tegnet spesifikt for Smart Factory-drift. Det er ytterligere 21000m² byggeklar industritomt med ledetid 12 måneder.

**Formålsdesignet, ikke ombygd.** MInfrastruktur, maskinplasseringer, kraner - gulvbæring, krafttilførsel, datakabelføring og ventilasjonslogistikk er integrert fra Smart Factory arkitektfasen. Det betyr at automasjon, materialflyt og systemintegrering ikke er noe som legges til etterpå — det er premisser for byggets utforming. Det legges stor vekt på tilgangskontroll til produksjonsarealer som begrenset innsyn til berettige.

**12 måneders ledetid.** Fra investeringsbeslutning til produksjonsstart er ledetiden 12 måneder. Byggestart er planlagt Q3 2026, med maskiner levert Q2 2027 og produksjonsstart august 2027.

**Skalert for full utbygging.** Anleggsarealet er dimensjonert for 25 CNC-maskiner med tilhørende automasjon, materiallagring, metrologilab, teknisk verksted og kontorfasiliteter.

---

## Industriklynge Våler

Utover Aurelians eget anlegg er ytterligere **180 mål (180 000 m²) regulert til industriformål** i umiddelbar nærhet. Store deler av arealet forventes byggeklart innen ett år.

Området har kvaliteter som er relevante for industriell etablering:

- **Gode kraftforhold** for energikrevende produksjon
- **Tilgjengelig areal** i en skala som tillater flere virksomheter
- **Strategisk beliggenhet** med nærhet til innenlandshavn, vei, jernbane og sjøtransport og militær flyplass på Rygge.
- **Rekrutteringsgrunnlag** i en region med industriell tradisjon og rimelig avstand til teknologimiljøer i Oslo-regionen
- **Ytterligere arealer** i nærområdet kan reguleres til industriformål ved behov

### Invitasjon til industrielle samarbeidspartnere

Aurelian søker industrielle partnere som ønsker å etablere virksomhet i Våler-området og investere i utviklingen av det vi mener kan bli en ny norsk industri-hub for forsvarsrelatert produksjon.

Visjonen er et klyngemiljø der komplementær produksjonskapasitet, spesialistkompetanse og felles infrastruktur samles på ett sted. For forsvarsindustrien betyr samlokalisering kortere interne forsyningslinjer, enklere sikkerhetshåndtering og et sterkere grunnlag for nasjonal forsyningssikkerhet.

Vi er i en tidlig fase — og det er nettopp derfor partnere som kommer inn nå har reell mulighet til å forme miljøet.

---

## Tidslinje

| Milepæl | Tidspunkt |
|---|---|
| Byggeprosjekt start | Q2 2026 |
| CNC maskin bestilling | Q3 2026 |
| Bygg ferdigstilt | Q2 2027 |
| CNC-maskiner levert og installasjon startes | Q2 2027 |
| **Produksjonsstart** | **August 2027** |

---

## Kontakt

| | |
|---|---|
| **Tore Ausland** | VP Business Development |
| | tore@aurelian.no |

---

*Aurelian Manufacturing AS | Våler, Østfold | KONFIDENSIELT | Februar 2026*
