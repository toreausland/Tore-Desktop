import os, re, zipfile, datetime
from pathlib import Path
from lxml import etree


W = chr(123) + "http://schemas.openxmlformats.org/wordprocessingml/2006/main" + chr(125)
WP = chr(123) + "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" + chr(125)
VNS = chr(123) + "urn:schemas-microsoft-com:vml" + chr(125)

VDR_ROOT = os.path.join("C:", os.sep, "Users", "mrntau",
    "OneDrive - Mosseregionens Næringsutvikling AS",
    "Skrivebord", "Aurelian", "Aurelian Manufacturing", "Aurelian_VDR")

FILES = [
    os.path.join(VDR_ROOT, "00_Executive_Summary", "DRAFT_00_Executive_Summary.docx"),
    os.path.join(VDR_ROOT, "00_Executive_Summary", "DRAFT_00_Investment_Teaser_OnePager.docx"),
    os.path.join(VDR_ROOT, "01_Corporate_Governance", "1.2_Shareholder_Agreements", "01_Shareholders_Agreement.docx"),
    os.path.join(VDR_ROOT, "01_Corporate_Governance", "1.5_Organizational_Structure", "01_Org_Chart_Current.docx"),
    os.path.join(VDR_ROOT, "01_Corporate_Governance", "1.6_Founder_Vesting", "01_Acceleration_Terms_Double_Trigger.docx"),
    os.path.join(VDR_ROOT, "02_Financial", "2.3_Valuation_Basis", "02_Model_Assumptions_Valuation.docx"),
    os.path.join(VDR_ROOT, "04_Technical_Operations", "4.2_CNC_Equipment", "Specifications", "04_CNC_Equipment_Specifications_Mazak_4.docx"),
    os.path.join(VDR_ROOT, "05_Legal_IP", "5.1_IP_Ownership", "05_IP_Assignment_Agreements_Founders.docx"),
    os.path.join(VDR_ROOT, "06_Team", "6.1_Founders", "06_ToreAusland_CV.docx"),
    os.path.join(VDR_ROOT, "08_DD_Process_Internal", "8.1_Checklists", "08_DD_Checklist_PreSeed_Round.docx"),
]

BANNED = [
    (r"REV\s*\d+", "REV+number"),
    (r"(?<![A-Za-z])V\d+(?:\.\d+)?(?![A-Za-z])", "Bare version ref"),
    (r"Market\s+Analysis\s+Master", "Market Analysis Master"),
    (r"[Mm]arkedsanalyse", "Markedsanalyse"),
    (r"[Vv]edlegg", "Vedlegg"),
    (r"[Kk]onfidensielt|KONFIDENSIELT", "Konfidensielt"),
    (r"[Kk]omplett", "Komplett"),
    (r"DRAFT_03", "DRAFT_03 retired"),
    (r"[Ff]inansieringsplan", "Finansieringsplan"),
]

NOTERMS = [
    (r"Selskap(?:et)?", "Selskap->Company"),
    (r"Aksjon[ae]r(?:er)?", "Aksjonaer->Shareholder"),
    (r"Styret?", "Styre->Board"),
    (r"Vedtekt(?:er|ene)?", "Vedtekter->Articles"),
    (r"Foretaksregisteret", "Foretaksregisteret->Register"),
    (r"[Oo]msetning", "Omsetning->Revenue"),
    (r"[Kk]ostnad(?:er)?", "Kostnad->Cost"),
    (r"[Ii]nntekt(?:er)?", "Inntekt->Income"),
    (r"[Uu]tgift(?:er)?", "Utgift->Expense"),
    (r"[Gg]eneralforsamling(?:en)?", "Generalforsamling->GM"),
    (r"[Dd]aglig\s+leder", "Daglig leder->CEO"),
]

REFPATS = [
    r"VDR\s+\d+[\.\d]*",
    r"\d{2}\s+(?:Economic|Executive|Investment|Shareholder|Org|Acceleration|Model|CNC|IP|CV|DD|Benchmark|Sensitivity|Use of Funds|Pricing|Market|Quality|Production|Risk|Key Hires|Go.To.Market).{0,80}",
    r"(?:Economic Tables|Competitive Landscape|Sensitivity Analysis|Use of Funds|Pricing.Revenue|Market Trends|Quality Certification|Production Timeline|Risk Register|Key Hires|Go.To.Market)",
    r"(?:AQAP|AS9100|ISO)\s*\d+",
    r"Financing\s+Plan\s+V\d",
]

def parse_xml(zf, part):
    try:
        with zf.open(part) as f:
            return etree.parse(f).getroot()
    except Exception:
        return None

def txt(elem):
    res = []
    for t in elem.iter(W + "t"):
        if t.text: res.append(t.text)
    return "".join(res)

def para_txt(p):
    parts = []
    for r in p.findall(W + "r"):
        for t in r.findall(W + "t"):
            if t.text: parts.append(t.text)
    return "".join(parts)

def run_fonts(run):
    fonts = set()
    rPr = run.find(W + "rPr")
    if rPr is not None:
        for rf in rPr.findall(W + "rFonts"):
            for k, v in rf.attrib.items():
                aa = k.split("}")[-1] if "}" in k else k
                if aa in ("ascii", "hAnsi", "eastAsia", "cs") and v:
                    fonts.add(v)
    return fonts

def run_colors(run):
    colors = set()
    rPr = run.find(W + "rPr")
    if rPr is not None:
        for c in rPr.findall(W + "color"):
            for k, v in c.attrib.items():
                if "val" in k and v.lower() != "auto":
                    colors.add("text:#" + v)
        for h in rPr.findall(W + "highlight"):
            for k, v in h.attrib.items():
                if "val" in k: colors.add("highlight:" + v)
        for s in rPr.findall(W + "shd"):
            for k, v in s.attrib.items():
                if "fill" in k and v.lower() not in ("auto", "ffffff"):
                    colors.add("run-shading:#" + v)
    return colors

def cell_colors(cell):
    colors = set()
    tcp = cell.find(W + "tcPr")
    if tcp is not None:
        for s in tcp.findall(W + "shd"):
            for k, v in s.attrib.items():
                if "fill" in k and v.lower() not in ("auto", "ffffff"):
                    colors.add("cell-shading:#" + v)
                elif "color" in k.lower() and "theme" not in k.lower() and v.lower() not in ("auto", "ffffff"):
                    colors.add("cell-fg:#" + v)
    return colors

def para_shading(p):
    colors = set()
    pp = p.find(W + "pPr")
    if pp is not None:
        for s in pp.findall(W + "shd"):
            for k, v in s.attrib.items():
                if "fill" in k and v.lower() not in ("auto", "ffffff"):
                    colors.add("para-shading:#" + v)
    return colors

def count_images(root):
    c = 0
    for _ in root.iter(WP + "inline"): c += 1
    for _ in root.iter(WP + "anchor"): c += 1
    for _ in root.iter(VNS + "imagedata"): c += 1
    return c

def find_md(vdr):
    md = []
    for dp, dn, fn in os.walk(vdr):
        for f in fn:
            if f.lower().endswith(".md"):
                md.append(os.path.join(dp, f))
    return md

def match_md(docx_path, md_files):
    dn = Path(docx_path).stem.lower()
    dd = str(Path(docx_path).parent).lower()
    clean = dn.replace("draft_", "").replace("_", " ").strip()
    matches = []
    for mp in md_files:
        mn = Path(mp).stem.lower().replace("_", " ").strip()
        md_dir = str(Path(mp).parent).lower()
        same = md_dir == dd or os.path.dirname(md_dir) == os.path.dirname(dd)
        if clean in mn or mn in clean:
            matches.append((mp, "name_match", same))
        elif len(clean.split()) > 1:
            dw = set(w for w in clean.split() if len(w) > 3)
            mw = set(w for w in mn.split() if len(w) > 3)
            ov = dw & mw
            if len(ov) >= 2 or (len(ov) >= 1 and same):
                matches.append((mp, "partial_match", same))
        if same and len(dn) >= 2 and len(mn) >= 2 and dn[:2] == mn[:2]:
            if not any(x[0] == mp for x in matches):
                matches.append((mp, "dir_prefix_match", same))
    return matches

def detect_lang(text):
    if not text or len(text.strip()) < 20:
        return "UNKNOWN (too short)"
    s = text[:500].lower()
    no_w = ["og","er","det","som","til","av","den","har","skal","med","kan","vil","ble","fra","eller","selskapet","avtale","mellom","etter","denne","alle","ikke"]
    en_w = ["the","and","is","of","to","in","that","for","with","this","are","has","will","from","or","company","shall","board","agreement","manufacturing","between","share","after","all","not"]
    words = re.findall(r"[a-zA-Z]+", s)
    if not words: return "UNKNOWN (no words)"
    nc = sum(1 for w in words if w in no_w)
    ec = sum(1 for w in words if w in en_w)
    if nc > ec + 2: return "NORWEGIAN (no:%d en:%d)" % (nc, ec)
    elif ec > nc + 2: return "ENGLISH (en:%d no:%d)" % (ec, nc)
    elif nc == 0 and ec == 0: return "UNKNOWN (no markers)"
    else: return "MIXED/UNCLEAR (en:%d no:%d)" % (ec, nc)

def inspect(fp):
    r = dict(path=fp, filename=os.path.basename(fp), exists=os.path.exists(fp),
             size_kb=0, paragraphs=0, tables=0, images=0,
             fonts=set(), colors=set(), header_content=[], footer_content=[],
             all_text=[], table_text=[], references=[], banned_matches=[],
             norwegian_terms=[], language="UNKNOWN", md_sources=[], errors=[])
    if not r["exists"]:
        r["errors"].append("FILE NOT FOUND")
        return r
    r["size_kb"] = round(os.path.getsize(fp) / 1024, 1)
    try:
        with zipfile.ZipFile(fp, "r") as zf:
            znames = zf.namelist()
            doc = parse_xml(zf, "word/document.xml")
            if doc is None:
                r["errors"].append("Cannot parse word/document.xml")
                return r
            body = doc.find(W + "body")
            if body is None:
                for ch in doc:
                    if "body" in ch.tag: body = ch; break
            if body is None:
                r["errors"].append("No body element")
                return r
            paras = list(body.iter(W + "p"))
            r["paragraphs"] = len(paras)
            for p in paras:
                pt = para_txt(p)
                if pt.strip(): r["all_text"].append(pt)
                for rn in p.iter(W + "r"):
                    r["fonts"].update(run_fonts(rn))
                    r["colors"].update(run_colors(rn))
                r["colors"].update(para_shading(p))
            tbls = list(body.iter(W + "tbl"))
            r["tables"] = len(tbls)
            for tbl in tbls:
                for tc in tbl.iter(W + "tc"):
                    ct = txt(tc)
                    if ct.strip(): r["table_text"].append(ct)
                    r["colors"].update(cell_colors(tc))
                    for rn in tc.iter(W + "r"):
                        r["fonts"].update(run_fonts(rn))
                        r["colors"].update(run_colors(rn))
            r["images"] = count_images(doc)
            for entry in znames:
                if entry.startswith("word/header") and entry.endswith(".xml"):
                    hroot = parse_xml(zf, entry)
                    if hroot is not None:
                        ht = txt(hroot).strip()
                        if ht: r["header_content"].append("%s: %s" % (entry, ht))
                        for rn in hroot.iter(W + "r"):
                            r["fonts"].update(run_fonts(rn))
                            r["colors"].update(run_colors(rn))
                elif entry.startswith("word/footer") and entry.endswith(".xml"):
                    froot = parse_xml(zf, entry)
                    if froot is not None:
                        ft = txt(froot).strip()
                        if ft: r["footer_content"].append("%s: %s" % (entry, ft))
                        for rn in froot.iter(W + "r"):
                            r["fonts"].update(run_fonts(rn))
                            r["colors"].update(run_colors(rn))
            sty = parse_xml(zf, "word/styles.xml")
            if sty is not None:
                for rf in sty.iter(W + "rFonts"):
                    for k, v in rf.attrib.items():
                        aa = k.split("}")[-1] if "}" in k else k
                        if aa in ("ascii", "hAnsi", "eastAsia", "cs") and v:
                            r["fonts"].add("(style)" + v)
    except zipfile.BadZipFile:
        r["errors"].append("Bad ZIP / corrupt docx")
        return r
    except Exception as e:
        r["errors"].append("Exception: %s" % str(e))
        return r
    full = chr(10).join(r["all_text"] + r["table_text"])
    hf = " ".join(h.split(": ", 1)[-1] for h in r["header_content"] + r["footer_content"])
    scan = full + chr(10) + hf
    r["language"] = detect_lang(full)
    for pat in REFPATS:
        for m in re.finditer(pat, scan, re.IGNORECASE):
            ref = m.group(0).strip()
            if ref and ref not in r["references"]: r["references"].append(ref)
    for pat, desc in BANNED:
        for m in re.finditer(pat, scan):
            cs = max(0, m.start() - 30)
            ce = min(len(scan), m.end() + 30)
            ctx = scan[cs:ce].replace(chr(10), " ").strip()
            r["banned_matches"].append(dict(pattern=desc, match=m.group(0), context="...%s..." % ctx))
    for pat, desc in NOTERMS:
        for m in re.finditer(pat, scan):
            cs = max(0, m.start() - 20)
            ce = min(len(scan), m.end() + 20)
            ctx = scan[cs:ce].replace(chr(10), " ").strip()
            r["norwegian_terms"].append(dict(term=desc, match=m.group(0), context="...%s..." % ctx))
    return r

def report(r, idx):
    print("")
    print("=" * 100)
    print("  FILE %d: %s" % (idx, r["filename"]))
    print("=" * 100)
    print("  Path:   %s" % r["path"])
    print("  Exists: %s    Size: %s KB" % (r["exists"], r["size_kb"]))
    if r["errors"]:
        print("")
        print("  *** ERRORS ***")
        for e in r["errors"]: print("    [ERROR] %s" % e)
        if not r["exists"]: return
    print("")
    print("  --- Content Counts ---")
    print("    Paragraphs: %d" % r["paragraphs"])
    print("    Tables:     %d" % r["tables"])
    print("    Images:     %d" % r["images"])
    print("")
    print("  --- Language Detection ---")
    print("    %s" % r["language"])
    print("")
    print("  --- Fonts Found (%d) ---" % len(r["fonts"]))
    for f in sorted(r["fonts"]): print("    %s" % f)
    if not r["fonts"]: print("    (none)")
    print("")
    print("  --- Colors Found (%d) ---" % len(r["colors"]))
    for c in sorted(r["colors"]): print("    %s" % c)
    if not r["colors"]: print("    (none)")
    print("")
    print("  --- Headers ---")
    if r["header_content"]:
        for h in r["header_content"]: print("    %s" % h)
    else: print("    (no header content)")
    print("")
    print("  --- Footers ---")
    if r["footer_content"]:
        for f in r["footer_content"]: print("    %s" % f)
    else: print("    (no footer content)")
    print("")
    print("  --- Document References Found (%d) ---" % len(r["references"]))
    for ref in r["references"]: print("    -> %s" % ref)
    if not r["references"]: print("    (none)")
    print("")
    print("  --- BANNED PATTERN MATCHES (%d) ---" % len(r["banned_matches"]))
    if r["banned_matches"]:
        for bm in r["banned_matches"]:
            print("    [BANNED] %s" % bm["pattern"])
            print("             Match: %r" % bm["match"])
            print("             Context: %s" % bm["context"])
    else: print("    (none found - CLEAN)")
    print("")
    print("  --- Norwegian Terms Found (%d) ---" % len(r["norwegian_terms"]))
    if r["norwegian_terms"]:
        seen = set()
        for nt in r["norwegian_terms"]:
            k = nt["term"]
            if k not in seen:
                seen.add(k)
                cnt = sum(1 for x in r["norwegian_terms"] if x["term"] == k)
                print("    [%dx] %s" % (cnt, nt["term"]))
                print("           Example: %s" % nt["context"])
    else: print("    (none found)")
    print("")
    print("  --- .md Source File Matches ---")
    if r["md_sources"]:
        for mp, mt, sd in r["md_sources"]:
            loc = "SAME DIR" if sd else "other dir"
            print("    [%s] [%s] %s" % (mt, loc, mp))
    else: print("    (no matching .md source found)")
    combined = " ".join(r["all_text"])
    if combined.strip():
        preview = combined[:300].replace(chr(10), " ")
        print("")
        print("  --- Text Preview (first 300 chars) ---")
        print("    %s..." % preview)

def summary(results):
    print("")
    print("#" * 100)
    print("  SUMMARY TABLE - ALL 10 TIER 4 .DOCX FILES")
    print("#" * 100)
    print("")
    hdr = "%2s | %-48s | %5s | %7s | %4s | %3s | %3s | %5s | %6s | %3s | %3s | %4s | %6s | %7s | %-15s | %3s"
    print(hdr % ("#", "Filename", "Exist", "Size", "Para", "Tbl", "Img", "Fonts", "Colors", "Hdr", "Ftr", "Refs", "BANNED", "NO-trm", "Language", "MD?"))
    print("-" * 155)
    for i, r in enumerate(results, 1):
        ex = "YES" if r["exists"] else "NO"
        lang = r["language"].split("(")[0].strip()[:15] if r["exists"] else "N/A"
        hc = len(r["header_content"])
        fc = len(r["footer_content"])
        bc = len(r["banned_matches"])
        nc = len(r["norwegian_terms"])
        md = "YES" if r["md_sources"] else "NO"
        fn = r["filename"][:48]
        print(hdr % (i, fn, ex, "%.1fK" % r["size_kb"], r["paragraphs"], r["tables"], r["images"],
                     len(r["fonts"]), len(r["colors"]), hc, fc, len(r["references"]), bc, nc, lang, md))
    tb = sum(len(r["banned_matches"]) for r in results)
    tn = sum(len(r["norwegian_terms"]) for r in results)
    mf = sum(1 for r in results if not r["exists"])
    nm = sum(1 for r in results if not r["md_sources"])
    nd = sum(1 for r in results if "NORWEGIAN" in r["language"])
    print("")
    print("=" * 100)
    print("  AGGREGATE ISSUES")
    print("=" * 100)
    print("  Missing .docx files:           %d" % mf)
    print("  Total banned pattern matches:  %d" % tb)
    print("  Total Norwegian term matches:  %d" % tn)
    print("  Documents detected Norwegian:  %d" % nd)
    print("  Documents without .md source:  %d" % nm)
    if tb > 0:
        print("")
        print("  --- All Banned Matches Across Files ---")
        for r in results:
            for bm in r["banned_matches"]:
                print("    [%s] %s: %r" % (r["filename"][:40], bm["pattern"], bm["match"]))
    af = set()
    for r in results: af.update(r["fonts"])
    print("")
    print("  --- Unique Fonts Across All Files (%d) ---" % len(af))
    for f in sorted(af): print("    %s" % f)
    ac = set()
    for r in results: ac.update(r["colors"])
    print("")
    print("  --- Unique Colors Across All Files (%d) ---" % len(ac))
    for c in sorted(ac): print("    %s" % c)

def main():
    print("*" * 100)
    print("  TIER 4 .DOCX COMPREHENSIVE INSPECTION REPORT")
    print("  Generated: %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("  Files to inspect: %d" % len(FILES))
    print("*" * 100)
    print("")
    print("  Scanning for .md source files in VDR root...")
    md_files = find_md(VDR_ROOT)
    print("  Found %d .md files:" % len(md_files))
    for m in md_files: print("    %s" % m)
    results = []
    for i, fp in enumerate(FILES, 1):
        print("")
        print("  Processing file %d/%d: %s..." % (i, len(FILES), os.path.basename(fp)))
        r = inspect(fp)
        r["md_sources"] = match_md(fp, md_files)
        results.append(r)
    for i, r in enumerate(results, 1):
        report(r, i)
    summary(results)
    print("")
    print("*" * 100)
    print("  INSPECTION COMPLETE")
    print("*" * 100)

if __name__ == "__main__":
    main()
