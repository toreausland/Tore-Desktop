# Aurelian Manufacturing — Design Manual & Document Style Guide

> **Version:** 2.0 — February 2026
> **Scope:** All company documents — presentations, Word documents, reports, proposals, data room materials, internal memos, and investor communications.
> **Purpose:** This file is a Claude skill. When loaded, it ensures every generated document follows Aurelian Manufacturing's visual identity precisely and consistently.

---

## 1. BRAND IDENTITY

**Company:** Aurelian Manufacturing AS
**Tagline:** Production as a Service — Autonomous, Data-Driven, and Scalable
**Industry:** Defense & Aerospace Autonomous Manufacturing
**Tone of voice:** Precise, confident, technical but accessible. No fluff. Data-driven claims backed by numbers. Professional Scandinavian minimalism.

---

## 2. COLOR PALETTE

### 2.1 Primary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Aurelian Red** | `#F50537` | 245, 5, 55 | Primary accent (Pantone 032 C). Headlines, CTAs, icons, highlights, chart series, numbered markers, decorative bars |
| **Aurelian Black** | `#2B2B2B` | 43, 43, 43 | Primary text color. Dark panels, overlays, headings on light backgrounds |
| **Pure Black** | `#000000` | 0, 0, 0 | Title/cover slide backgrounds, closing slide backgrounds only |
| **White** | `#FFFFFF` | 255, 255, 255 | Default page/slide background, text on dark backgrounds |

### 2.2 Secondary / Neutral Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Medium Gray** | `#6B6B6B` | 107, 107, 107 | Secondary text, captions, footers, metadata, muted labels |
| **Panel Gray** | `#F5F5F5` | 245, 245, 245 | Card backgrounds, table header fills, sidebar panels, callout boxes |
| **Divider Gray** | `#D3D3D3` | 211, 211, 211 | Horizontal rules, table borders, separator lines |
| **Chart Axis Gray** | `#888888` | 136, 136, 136 | Chart axis lines, gridlines |

### 2.3 Dark Theme Palette (use only for special feature slides or dark-mode sections)

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Deep Charcoal** | `#1A1A1A` | 26, 26, 26 | Dark section backgrounds |
| **Dark Navy** | `#1C2D3F` | 28, 45, 63 | Dark section panels |
| **Navy Card** | `#253B52` | 37, 59, 82 | Card backgrounds on dark sections |
| **Slate Line** | `#3D5A7A` | 61, 90, 122 | Dividers on dark sections |
| **Steel Blue** | `#8EAEC5` | 142, 174, 197 | Accent text on dark sections |
| **Dark Red** | `#D0042E` | 208, 4, 46 | Red accent variant for dark backgrounds (higher contrast) |

### 2.4 Color Rules

- **NEVER** use colors outside this palette unless explicitly approved.
- **Aurelian Red `#F50537`** is the signature color. It must appear on every page/slide — even if only as a thin accent bar or a single highlighted word.
- **Text on white backgrounds:** Use `#2B2B2B` for primary, `#6B6B6B` for secondary, `#F50537` for selective accent details.
- **Text on black/dark backgrounds:** Use `#FFFFFF` for primary, `#F50537` for accent highlights.
- **Text on red backgrounds:** Use `#FFFFFF` only. Red background panels (`#F50537`) may be used sparingly for extra visual impact.
- **Never place red text on dark backgrounds smaller than 14pt** — use `#FFFFFF` instead and reserve red for shapes/icons.
- **NUMBERS AND FINANCIAL DATA:** Never display numbers in red text — red numbers universally imply negative values. Instead, use white text on red background badges, or black `#2B2B2B` text with adjacent red accent elements. Red (`#F50537`) may only be used as a background color behind numbers, never as the text color for numbers.
- **Charts:** Primary data series is always `#F50537` (this is acceptable as chart series colors are not read as "negative"). If multiple series are needed, use: `#F50537`, `#2B2B2B`, `#6B6B6B`, `#D3D3D3` in that order.
- **Transparency:** Use `#2B2B2B` at 70% opacity for overlay bars on images.

### 2.5 Presentation Color Philosophy

The overall presentation style is **readable and clean**, not dark-heavy:

| Priority | Background | Text | When to use |
|----------|-----------|------|-------------|
| **Primary** | `#FFFFFF` (white) | `#2B2B2B` (black) | All standard content slides — the default |
| **Feature** | `#000000` (black) | `#FFFFFF` + `#F50537` | Cover slide, closing slide, and occasional visual emphasis panels |
| **Accent** | `#F50537` (red) | `#FFFFFF` (white) | Sparingly — small panels, badges, highlight bars for extra visual touch |

- **Most slides should be white background with black text.** This is the primary, readable format.
- **Black backgrounds** are reserved for the first slide (cover), last slide (closing/CTA), and occasional feature panels within content slides.
- **Red backgrounds** may be used in small doses — a highlight bar, a badge, a stat panel — never as full-slide background.
- **Red text on white backgrounds** is used selectively for key details: important numbers, highlighted keywords, accent headings.
- The goal is **Scandinavian minimalism**: clean white space, sharp black typography, with red as a precise visual punctuation mark.

---

## 3. TYPOGRAPHY

### 3.1 Primary Typeface

**Calibri** — used for ALL document text across all formats (presentations, Word, reports).

| Role | Font | Weight | Size (Presentations) | Size (Word/A4) | Color |
|------|------|--------|---------------------|-----------------|-------|
| **Display title** | Calibri | Bold | 54pt | 28–32pt | `#FFFFFF` on black bg |
| **Slide title** | Calibri | Bold | 36pt | 24–26pt | `#2B2B2B` |
| **Section heading** | Calibri | Bold | 20pt | 18pt | `#F50537` |
| **Sub-heading** | Calibri | Bold Italic | 18pt | 14–16pt | `#F50537` or `#2B2B2B` |
| **Card/panel title** | Calibri | Bold | 15pt | 13pt | `#2B2B2B` |
| **Body text** | Calibri | Regular | 14pt | 11pt | `#2B2B2B` |
| **Description/caption** | Calibri | Regular | 11–12pt | 9–10pt | `#6B6B6B` |
| **Footer/metadata** | Calibri | Regular | 12pt | 8–9pt | `#6B6B6B` |
| **Small/fine print** | Calibri | Regular | 9–10pt | 8pt | `#6B6B6B` |

### 3.2 Secondary Typeface (Charts Only)

**Arial** — used exclusively for chart axis labels and data labels when Calibri renders poorly in chart engines.

- Chart axis labels: Arial, 10pt Regular, `#6B6B6B`
- Chart data labels: Arial, 11pt Bold, `#2B2B2B`

### 3.3 Typography Rules

- **Never use more than 2 typefaces** in any single document (Calibri + Arial for charts).
- **Bold** for all headings and emphasis. Never use underline for emphasis.
- **Italic** reserved for subtitles, taglines, and brief descriptive phrases. Never for body paragraphs.
- **ALL CAPS** may be used sparingly for section labels (e.g., "THE PROBLEM", "WHY NOW") at 20pt bold in `#F50537`. Never for body text.
- **Letter spacing:** Default. Do not artificially track/kern body text.
- **Line spacing in Word documents:** 1.15 for body text, 1.0 for headings, add 6pt space after paragraphs.
- **Line spacing in presentations:** Single (1.0) for all text.
- **Minimum readable size:** 9pt in presentations, 8pt in Word documents.
- **Kerning:** Enable at 12pt and above (standard Calibri kerning).

---

## 4. DOCUMENT LAYOUTS

### 4.1 Presentations (16:9 Widescreen)

**Slide dimensions:** 10.0" × 5.625" (25.4 cm × 14.29 cm)
**Aspect ratio:** 16:9

#### Content Zones

```
┌──────────────────────────────────────────────────────┐
│  0.5" margin                                    0.5" │
│  ┌──────────────────────────────────────────────┐    │
│  │  TITLE ZONE (y: 0.4")                        │    │
│  │  36pt Bold, #2B2B2B                          │    │
│  ├──────────────────────────────────────────────┤    │
│  │  SUBTITLE ZONE (y: 0.85"–1.1")              │    │
│  │  18pt Bold Italic, #F50537                   │    │
│  ├──────────────────────────────────────────────┤    │
│  │                                              │    │
│  │  CONTENT ZONE (y: 1.2"–4.5")                │    │
│  │  9.0" usable width                           │    │
│  │                                              │    │
│  ├──────────────────────────────────────────────┤    │
│  │  FOOTER ZONE (y: 4.8"–5.3")                 │    │
│  │  12pt Regular, #6B6B6B                       │    │
│  └──────────────────────────────────────────────┘    │
│                                                 0.5" │
└──────────────────────────────────────────────────────┘
```

- **Margins:** 0.5 inches (1.27 cm) on all sides
- **Usable content width:** 9.0 inches (22.86 cm)
- **Title position:** 0.4" from top edge
- **Content starts:** 1.2" from top edge
- **Footer area:** 4.8" from top edge

#### Slide Types

**Cover Slide (black):**
- Background: `#000000`
- Logo: Centered, white version, 60–80px
- Company name: 54pt Bold, `#FFFFFF`, centered
- Red decorative bar: 3" wide × 0.05" tall, `#F50537`, centered below title
- Tagline: 24pt Italic, `#F50537`, centered below bar
- Date: 12pt Regular, `#6B6B6B`, right-aligned at bottom
- "CONFIDENTIAL" label: 12pt Regular, `#6B6B6B`, bottom left

**Content Slide — standard (white):**
- Background: `#FFFFFF`
- Title: 36pt Bold, `#2B2B2B`, left-aligned at 0.5" from left, 0.4" from top
- Subtitle: 18pt Bold Italic, `#F50537`
- Body text: 14pt Regular, `#2B2B2B`
- Key numbers/highlights: `#F50537` for selective emphasis
- Footer: 12pt Regular, `#6B6B6B`
- This is the **default slide type** — used for the majority of slides

**Content Slide — with dark panel (white + black):**
- Background: `#FFFFFF`
- May include a dark panel (`#2B2B2B` or `#000000`) for a stats section, quote, or visual feature
- Dark panel text: `#FFFFFF` and `#F50537`
- Rest of slide: standard white content rules
- Use for visual variety on key slides (1–2 per presentation max)

**Content Slide — with red accent panel (white + red):**
- Background: `#FFFFFF`
- May include a small red panel (`#F50537`) as badge, stat highlight, or accent bar
- Red panel text: `#FFFFFF` only
- Use sparingly for extra visual touch

**Closing/CTA Slide (black):**
- Background: `#000000`
- Heading: 42pt Bold, `#FFFFFF`, centered
- Key figure (e.g., funding amount): 42pt Bold, `#FFFFFF` on `#F50537` badge/panel — never red text alone
- Detail text: 14–16pt, `#FFFFFF`
- Deal terms cards: `#2B2B2B` background, white text for values, white labels
- Divider line: 1pt, `#6B6B6B`

### 4.2 Word Documents (A4 Portrait)

**Page dimensions:** 210mm × 297mm (8.27" × 11.69")

#### Page Setup

| Property | Value |
|----------|-------|
| **Top margin** | 2.5 cm (1.0") |
| **Bottom margin** | 2.5 cm (1.0") |
| **Left margin** | 2.5 cm (1.0") |
| **Right margin** | 2.5 cm (1.0") |
| **Header space** | 1.25 cm (0.5") |
| **Footer space** | 1.25 cm (0.5") |
| **Columns** | Single column (default), two-column for comparison layouts |

#### Heading Hierarchy for Word

| Level | Style | Size | Weight | Color | Spacing Before | Spacing After |
|-------|-------|------|--------|-------|---------------|--------------|
| **Title** | Title | 28pt | Bold | `#2B2B2B` | 0pt | 12pt |
| **Heading 1** | Section | 22pt | Bold | `#2B2B2B` | 24pt | 6pt |
| **Heading 2** | Subsection | 16pt | Bold | `#F50537` | 18pt | 6pt |
| **Heading 3** | Sub-subsection | 13pt | Bold | `#2B2B2B` | 12pt | 4pt |
| **Heading 4** | Minor heading | 11pt | Bold | `#6B6B6B` | 12pt | 4pt |
| **Body** | Normal | 11pt | Regular | `#2B2B2B` | 0pt | 6pt |
| **Body Small** | Caption | 9pt | Regular | `#6B6B6B` | 0pt | 4pt |

#### Header & Footer (Word)

- **Header:** Company name "Aurelian Manufacturing" in 9pt Calibri Regular `#6B6B6B`, right-aligned. Optional thin `#F50537` underline (0.5pt).
- **Footer:** Page number centered, 9pt Calibri Regular `#6B6B6B`. "CONFIDENTIAL" left-aligned when applicable. Document date right-aligned.
- **First page:** May omit header. Include a 3pt `#F50537` horizontal rule 2cm from top as decorative element.

---

## 5. COMPONENT PATTERNS

### 5.1 Cards / Info Panels

Used to present 2–4 equal pieces of information side by side.

**Presentation version:**
- Background fill: `#F5F5F5`
- Size: ~2.8" wide × 2.0" tall (for 3-column)
- Title: 15pt Bold, `#2B2B2B`, centered
- Body: 10pt Regular, `#2B2B2B`, centered
- Equal horizontal spacing between cards
- No border, no shadow

**Word document version:**
- Background fill: `#F5F5F5`
- Padding: 12pt all sides
- Title: 13pt Bold, `#2B2B2B`
- Body: 11pt Regular, `#2B2B2B`
- No border (or 0.5pt `#D3D3D3` if needed for clarity)

### 5.2 Numbered Steps / Process Flow

**Presentation version:**
- Circle marker: 0.4" diameter, fill `#F50537`
- Number inside: 20pt Bold, `#FFFFFF`, centered
- Step title (right of circle): 14pt Bold, `#2B2B2B`
- Step description: 11pt Regular, `#6B6B6B`
- Vertical spacing: ~0.95" between steps

**Word document version:**
- Use a red bold number `①` `②` `③` in `#F50537` or a bold number followed by a period
- Step title: 13pt Bold, `#2B2B2B`, same line or next line
- Step description: 11pt Regular, `#6B6B6B`
- 12pt space between steps

### 5.3 Horizontal Dividers

- **Standard divider:** 1pt solid line, `#D3D3D3`
- **Accent divider:** 3" wide × 0.05" tall solid bar, `#F50537` (centered, for cover/section breaks)
- **Footer divider:** 1pt solid line, `#6B6B6B`

### 5.4 Callout / Highlight Box

- Background: `#F5F5F5`
- Left border: 3pt solid `#F50537`
- Padding: 12pt
- Text: 11pt Calibri Regular, `#2B2B2B`
- Use for key takeaways, important notes, or quoted statistics

### 5.5 Key Metric / Big Number

**IMPORTANT: Never display financial numbers or KPIs in red text.** Red numbers are universally associated with negative values in accounting/finance. Instead, use one of these approaches:

**Option A — White on red badge (preferred):**
- Background: `#F50537`, rounded corners (4–6px), padding 8–12pt
- Number: 28–36pt Bold, `#FFFFFF`
- Label below badge: 12–14pt Regular, `#6B6B6B`
- Creates strong visual impact without negative connotation

**Option B — Black number with red accent element:**
- Number: 28–36pt Bold, `#2B2B2B`
- Small red underline, left bar, or decorative element adjacent to the number
- Label below: 12–14pt Regular, `#6B6B6B`
- More subtle, Scandinavian minimal approach

**Option C — Black number on light panel:**
- Background: `#F5F5F5`, padding 12pt
- Number: 28–36pt Bold, `#2B2B2B`
- Label below: 12–14pt Regular, `#6B6B6B`
- Clean and neutral

- Centered in its container
- Use to highlight KPIs, financial figures, or impressive statistics
- **On dark panels (`#2B2B2B`):** Numbers in `#FFFFFF`, not `#F50537`
- **On black slides (cover/closing):** White numbers are standard; red badges (`#F50537` bg + white text) may be used for the hero number (e.g., funding ask)

---

## 6. TABLES

### 6.1 Standard Table Style

| Property | Value |
|----------|-------|
| **Header row background** | `#2B2B2B` |
| **Header row text** | 11pt Bold, `#FFFFFF` |
| **Body row background** | `#FFFFFF` (odd rows), `#F5F5F5` (even rows) |
| **Body row text** | 11pt Regular, `#2B2B2B` |
| **Border** | 0.5pt `#D3D3D3` horizontal lines between rows |
| **Vertical borders** | None (clean horizontal-only style) |
| **Cell padding** | 6pt top/bottom, 8pt left/right |
| **Alignment** | Text left-aligned, numbers right-aligned |
| **Total/summary row** | 11pt Bold, `#2B2B2B`, top border 1.5pt `#2B2B2B` |

### 6.2 Accent Table Style (for feature comparisons)

| Property | Value |
|----------|-------|
| **Header row background** | `#F50537` |
| **Header row text** | 11pt Bold, `#FFFFFF` |
| **Body rows** | Same as standard |
| **First column** | Bold if used as row labels |
| **Highlight cells** | `#F50537` text for standout values |

### 6.3 Table Rules

- **Never use full grid borders** (all four sides of every cell). Use horizontal lines only.
- **Always include a header row** with contrasting background.
- **Alternate row shading** for tables with more than 5 rows.
- **Number formatting:** Use `#,##0` for integers, `#,##0.0` for one decimal, percentage with `%` symbol.
- **Column widths** should be proportional to content. Never stretch a narrow column to fill space.

---

## 7. CHARTS & DATA VISUALIZATION

### 7.1 Line Charts

- **Primary series:** 3pt line, `#F50537`, round caps, circle markers (size 8), fill `#F50537`
- **Secondary series:** 2pt line, `#2B2B2B`, square markers (size 6)
- **Tertiary series:** 2pt line, `#6B6B6B`, no markers or diamond markers
- **Data labels:** Arial 11pt Bold, `#2B2B2B`, positioned above data points
- **Axis labels:** Arial 10pt Regular, `#6B6B6B`
- **Axis lines:** 1pt, `#888888`
- **Gridlines:** 1pt, `#D3D3D3` (horizontal only, no vertical gridlines)
- **Background:** Transparent (no fill)

### 7.2 Bar / Column Charts

- **Primary bars:** Fill `#F50537`
- **Secondary bars:** Fill `#2B2B2B`
- **Tertiary bars:** Fill `#6B6B6B`
- **Quaternary bars:** Fill `#D3D3D3`
- **Bar gap:** 50% of bar width
- **Category gap:** 100% of bar width
- **Data labels:** 10pt Bold, `#2B2B2B`, positioned outside end
- **No 3D effects. No gradients. No shadows.**

### 7.3 Pie / Donut Charts

- Slice order: `#F50537`, `#2B2B2B`, `#6B6B6B`, `#D3D3D3`, `#F5F5F5`
- **No exploded slices** unless highlighting a single key segment
- **Labels:** 11pt Regular, percentage + category name
- **Donut hole:** 50% for donut charts
- **No 3D effects.**

### 7.4 Chart Rules

- **Never use 3D charts.** All charts must be flat/2D.
- **Never use chart backgrounds** with fills or gradients.
- **Minimize gridlines.** Horizontal gridlines only when needed, never vertical.
- **Data labels take priority** over axis scales — if data labels are present, the value axis can be hidden.
- **Legend placement:** Bottom of chart, 10pt Regular, `#6B6B6B`. Avoid legends when direct labeling is possible.
- **Title above chart:** 16pt Bold, `#2B2B2B`. Subtitle: 12pt Regular, `#6B6B6B`.

---

## 8. IMAGES & GRAPHICS

### 8.1 Photography

- **Style:** Industrial, technical, high-contrast. Manufacturing environments, CNC machines, robotic arms, precision engineering.
- **Treatment:** No filters, no color overlays. Natural color grading with slightly desaturated tones.
- **When used as slide background:** Apply `#2B2B2B` overlay at 70% opacity, then place white text on top.

### 8.2 Icons & Illustrations

- **Style:** Minimal line icons or solid fill icons. Geometric, not decorative.
- **Color:** `#F50537` for primary icons, `#2B2B2B` for secondary, `#6B6B6B` for tertiary.
- **Size in presentations:** 0.4"–0.6" for inline icons, 0.8"–1.2" for featured icons.
- **Never use clip art, emoji, or stock illustration styles.**

### 8.3 Logo Usage

- **Logo design:** Five stars in an arc above "Aurelian Manufacturing" wordmark.
- **Primary logo (dark backgrounds):** White logo on black or dark backgrounds — this is the preferred usage for cover slides, closing slides, and dark panels.
- **Primary logo (light backgrounds):** Red (`#F50537`) tinted logo on white backgrounds — used in document headers and light content areas.
- **Minimum clear space:** Equal to the height of the capital "A" on all sides.
- **Minimum size:** 1.5" wide in print, 120px wide on screen.
- **Placement in Word docs:** Left-aligned in header, ~15mm height, with "Aurelian Manufacturing" text right-aligned in `#6B6B6B`.
- **Placement in presentations:** Centered on cover/closing slides, top-left corner on content slides.

---

## 9. WRITING STYLE & CONTENT GUIDELINES

### 9.1 General Tone

- **Professional, precise, and confident.** Not corporate jargon — clear and direct.
- **Data-first.** Lead with numbers and evidence, then explain.
- **Active voice.** "Aurelian delivers..." not "It is delivered by..."
- **Scandinavian restraint.** Understated confidence. No superlatives without data backing. Let the numbers speak.

### 9.2 Formatting Conventions

- **Dates:** DD Month YYYY (e.g., 13 February 2026) or YYYY-MM-DD for technical documents.
- **Currency:** NOK for Norwegian, EUR/USD with symbol and thousands separator (e.g., NOK 47,000,000 or €2.5M).
- **Percentages:** Always with % symbol, no space (e.g., 65%).
- **Abbreviations:** Define on first use, then abbreviate (e.g., "High-Mix Low-Volume (HMLV)").
- **Numbers:** Spell out one through nine, use numerals for 10+. Always use numerals in tables, charts, and financial contexts.
- **Lists:** Use bullet points (•) for unordered lists, numbered lists (1. 2. 3.) for sequential steps.

### 9.3 Document Labels

- **Confidential documents:** Include "CONFIDENTIAL" in footer, 12pt Regular, `#6B6B6B`.
- **Draft documents:** Include "DRAFT" watermark diagonally across page, `#D3D3D3` at 20% opacity, 72pt.
- **Version tracking:** Include version number and date in footer or title page.

---

## 10. SPACING & ALIGNMENT PRINCIPLES

### 10.1 General Rules

- **Left-align body text.** Never full-justify in presentations. Full-justify is acceptable in long Word documents.
- **Center-align:** Only for titles, subtitles, card content, and key metrics.
- **Right-align:** Only for dates, page numbers, and numeric columns in tables.
- **Consistent spacing:** Use the same spacing value throughout a document. If cards are 0.8" apart, all cards must be 0.8" apart.
- **Whitespace is essential.** When in doubt, add more space, not less. Never crowd elements.

### 10.2 Presentation Spacing

| Element Pair | Spacing |
|-------------|---------|
| Title → Subtitle | 0.45" |
| Subtitle → Content | 0.35" |
| Between body paragraphs | 0.2" |
| Between cards (horizontal) | 0.8" |
| Between process steps (vertical) | 0.95" |
| Content → Footer | 0.3" minimum |

### 10.3 Word Document Spacing

| Element Pair | Spacing |
|-------------|---------|
| Title → first paragraph | 12pt |
| Heading 1 → body | 6pt |
| Heading 2 → body | 6pt |
| Between body paragraphs | 6pt after |
| Before Heading 1 | 24pt |
| Before Heading 2 | 18pt |
| Table → surrounding text | 12pt above and below |
| Image → caption | 4pt |
| Caption → body text | 12pt |

---

## 11. FILE NAMING & ORGANIZATION

### 11.1 File Naming Convention

```
[NN]_[Document_Name]_V[X].[ext]
```

- `NN` = Two-digit sequence number (01, 02, ... 99)
- `Document_Name` = Descriptive name in Title_Case with underscores
- `VX` = Version number (V1, V2, V3...)
- `ext` = File extension

**Examples:**
- `01_Executive_Summary_V2.docx`
- `07_Investor_Pitch_Deck_V3.pptx`
- `12_Financial_Model_V1.xlsx`

---

## 12. QUICK REFERENCE — COPY-PASTE VALUES

### Colors (for code/templates)
```
Primary Red:     #F50537  |  rgb(245, 5, 55)   [Pantone 032 C]
Primary Text:    #2B2B2B  |  rgb(43, 43, 43)
Secondary Text:  #6B6B6B  |  rgb(107, 107, 107)
Background:      #FFFFFF  |  rgb(255, 255, 255)
Dark Background: #000000  |  rgb(0, 0, 0)
Panel Fill:      #F5F5F5  |  rgb(245, 245, 245)
Divider Line:    #D3D3D3  |  rgb(211, 211, 211)
Chart Axis:      #888888  |  rgb(136, 136, 136)
Dark Red:        #D0042E  |  rgb(208, 4, 46)
```

### Font Stack
```
Primary: Calibri, sans-serif
Charts:  Arial, sans-serif
```

### Presentation Dimensions
```
Width:  10.0 inches  (25.4 cm)   (9,144,000 EMU)
Height:  5.625 inches (14.29 cm)  (5,143,500 EMU)
Margin:  0.5 inches  (1.27 cm)   (457,200 EMU)
```

---

## 13. DOCUMENT-SPECIFIC TEMPLATES

### 13.1 When generating a Word document, ALWAYS:

1. Set all margins to 2.5 cm
2. Use Calibri as the only font
3. Apply heading styles per Section 4.2
4. Include header with "Aurelian Manufacturing" right-aligned in `#6B6B6B`
5. Include footer with page number centered, confidentiality label left, date right
6. Place a thin `#F50537` line (3pt) at the top of the first page as a brand element
7. Use table styles from Section 6
8. Format all numbers per Section 9.2
9. **Include a "References" section on the last page** listing all VDR source documents cited in the document (see Section 13.5)
10. **Never hardcode revision numbers** in document references — use revision-agnostic format (see Section 13.6)

### 13.2 When generating a presentation, ALWAYS:

1. Use 16:9 widescreen format
2. Start with a **black cover slide** with logo, centered company name in 54pt white bold, red decorative bar, and tagline in red
3. Use **white backgrounds with black text** for all standard content slides — this is the primary format
4. Place titles at 36pt Bold `#2B2B2B` left-aligned, 0.4" from top
5. Use `#F50537` red text selectively for key numbers, highlighted keywords, and accent headings on white slides
6. Optionally include a dark panel (`#2B2B2B`/`#000000`) on 1–2 key slides for visual variety (stats, quotes)
7. Optionally use small red (`#F50537`) panels or badges for extra visual touch — white text only on red
8. End with a **black closing/CTA slide** with white and red text
9. Include "CONFIDENTIAL" and date in footer of every slide
10. Follow the typography hierarchy from Section 3.1
11. **Ratio rule:** ~70% white slides, ~20% with dark accent panels, ~10% full black (cover + closing only)

### 13.3 When generating tables, ALWAYS:

1. Use dark header row (`#2B2B2B` background, white text)
2. Alternate row shading for 5+ rows (`#FFFFFF` / `#F5F5F5`)
3. Horizontal borders only (0.5pt `#D3D3D3`)
4. Right-align numeric columns
5. Bold the total/summary row with a heavier top border

### 13.4 When generating charts, ALWAYS:

1. Use `#F50537` as the primary data color
2. Flat 2D style — no 3D, no gradients, no shadows
3. Minimal gridlines (horizontal only if needed)
4. Data labels in Arial 11pt Bold
5. Transparent chart background

### 13.5 References Section (mandatory for all documents)

Every generated document (Word, PDF, presentation) MUST include a **References** section at the end, listing all VDR source documents cited in the document.

**Word document format:**
- Heading: "References" — Heading 2 style (16pt Bold, `#F50537`)
- Table with standard styling (Section 6.1): dark header row, alternating body rows, horizontal borders only
- Columns: VDR ref | Document title
- Only include documents actually referenced in the text
- Place as the last section before the document ends

**Example:**

| VDR ref | Document |
|---------|----------|
| 02.04 | 02 Economic Tables & Projections (master document) |
| 03.02 | CNC Benchmark & Competitive Landscape |
| 03.05 | Pricing & Revenue Model |

**Presentation format:**
- Dedicate the second-to-last slide (before closing/CTA slide) as "References"
- White background, standard content layout
- Same table format as Word

### 13.6 Revision-Agnostic References (mandatory)

**Never hardcode a revision number** (e.g., "REV6") in any generated document. The master document is always the current revision — references must remain valid when a new revision is issued.

| Context | Format |
|---------|--------|
| Body text reference | *02 Economic Tables & Projections* (VDR 02.04) |
| Inline section ref | Ref: 02 Economic Tables & Projections, §5.1 (VDR 02.04) |
| References table | 02 Economic Tables & Projections (master document) |

**Rationale:** When REV7 is issued, all previously generated documents should still have correct references without needing mass-updates. The VDR reference number (02.04) is permanent and does not change between revisions.

### 13.7 Mandatory Pre-Work Check

Before creating or revising ANY document, the following must be read and confirmed:
1. Master document: `02 Economic Tables & Projections` (current file on disk)
2. This design manual
3. The 17 checkpoint values from MEMORY.md
4. **This check applies to EACH document request within a conversation — not just the first one**

---

*This design manual is the single source of truth for all Aurelian Manufacturing visual communications. Every document, slide, table, and chart must adhere to these specifications without exception.*
