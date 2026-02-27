#!/usr/bin/env python3
import zipfile, xml.etree.ElementTree as ET, re, os, sys, glob

home = os.path.expanduser("~")
candidates = glob.glob(os.path.join(home, "OneDrive*"))
onedrive = None
for c in candidates:
    if "Mosse" in c: onedrive = c; break
if not onedrive and candidates: onedrive = candidates[0]
if not onedrive: print("ERROR: No OneDrive"); sys.exit(1)

B = os.path.join(onedrive, "Skrivebord", "Aurelian", "Aurelian Manufacturing", "Aurelian_VDR")
FILES = [
    os.path.join(B, "02_Financial", "2.6_Use_of_Funds", "02_Use_of_Funds_Seed_V1.docx"),
    os.path.join(B, "02_Financial", "2.3_Valuation_Basis", "02_Founder_Contribution_PreSeed_Valuation_1.docx"),
    os.path.join(B, "02_Financial", "2.4_Economic_Tables_Projections", "02_CAPEX_Breakdown_By_Phase.docx"),
    os.path.join(B, "03_Commercial_Market", "3.1_Market_Analysis", "03_TAM_SAM_SOM_Norwegian_Nordic.docx"),
    os.path.join(B, "04_Technical_Operations", "4.1_Technology_Overview", "04_Concept_Note_Strategic_Production_Node.docx"),
    os.path.join(B, "02_Financial", "2.3_Valuation_Basis", "02_Valuation_Methodology_V2.docx"),
    os.path.join(B, "03_Commercial_Market", "3.1_Market_Analysis", "03_Market_Trends_Projections.docx"),
    os.path.join(B, "02_Financial", "2.2_Financing_Plan", "02_Financing_Plan_V3.docx"),
]
TIERS = ["Tier 3"]*5 + ["Tier 2"]*3

PATTERNS = [
    (re.compile(r"Market\s+Analysis\s+Master", re.IGNORECASE), "RETIRED: Market Analysis Master"),
    (re.compile(r"Markedsanalyse\s+Master", re.IGNORECASE), "RETIRED: Markedsanalyse Master"),
    (re.compile(r"DRAFT_03", re.IGNORECASE), "RETIRED: DRAFT_03 reference"),
    (re.compile(r"Komplett", re.IGNORECASE), "BANNED: Komplett"),
    (re.compile(r"Vedlegg", re.IGNORECASE), "BANNED: Vedlegg"),
    (re.compile(r"KONFIDENSIELT", re.IGNORECASE), "BANNED: KONFIDENSIELT"),
    (re.compile(r"(?:Investor\s+Pitch|Executive\s+Summary|Sensitivity\s+Analysis|Use\s+of\s+Funds|Risk\s+Register|Key\s+Hires|Quality\s+Certification|Production\s+Timeline|CNC\s+Benchmark|Go\s+To\s+Market|Pricing.*Revenue|Financing\s+Plan|Valuation\s+Methodology|Economic\s+Tables|Market\s+Trends)\s+V\d", re.IGNORECASE), "VERSION REF in document name"),
    (re.compile(r"\bREV\s*\d+", re.IGNORECASE), "HARDCODED REV number"),
    (re.compile(r"30[\s,.]?000"), "WRONG VALUE: 30,000 (site area?)"),
]

WNS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def xtxt(elem):
    return "".join(t.text for t in elem.iter(f"{WNS}t") if t.text)

def xparas(root):
    r = []
    for i, p in enumerate(root.iter(f"{WNS}p")):
        t = xtxt(p)
        if t.strip(): r.append(("paragraph", i, t.strip()))
    return r

def xcells(root):
    r = []
    for ti, tbl in enumerate(root.iter(f"{WNS}tbl")):
        for ri, row in enumerate(tbl.iter(f"{WNS}tr")):
            for ci, cell in enumerate(row.iter(f"{WNS}tc")):
                t = xtxt(cell)
                if t.strip(): r.append(("table", f"tbl{ti}_r{ri}_c{ci}", t.strip()))
    return r

def scan_xml(xb, pfx):
    entries = []
    try: root = ET.fromstring(xb)
    except ET.ParseError as e: print(f"  [WARN] XML error in {pfx}: {e}"); return entries
    for k,i,t in xparas(root): entries.append((f"{pfx}/{k}[{i}]", t))
    for k,i,t in xcells(root): entries.append((f"{pfx}/{k}[{i}]", t))
    return entries

def scan_docx(fp):
    sn = os.path.basename(fp)
    findings = []
    if not os.path.exists(fp):
        print(f"  [ERROR] File not found: {fp}")
        return findings
    try:
        with zipfile.ZipFile(fp, "r") as zf:
            nl = zf.namelist()
            parts = []
            if "word/document.xml" in nl: parts.append(("word/document.xml", "document.xml"))
            for n in nl:
                if n.startswith("word/header") and n.endswith(".xml"): parts.append((n, os.path.basename(n)))
                if n.startswith("word/footer") and n.endswith(".xml"): parts.append((n, os.path.basename(n)))
            ae = []
            for zp, lb in parts:
                try: ae.extend(scan_xml(zf.read(zp), lb))
                except Exception as e: print(f"  [WARN] Error {zp}: {e}")
            for loc, txt in ae:
                for pat, pl in PATTERNS:
                    for m in pat.finditer(txt):
                        findings.append({"file": sn, "location": loc, "pattern": pl, "match": m.group(), "context": txt})
    except zipfile.BadZipFile: print(f"  [ERROR] Bad ZIP: {fp}")
    except Exception as e: print(f"  [ERROR] {type(e).__name__}: {e}")
    return findings

def main():
    sep = "=" * 120
    ln = "-" * 120
    print(sep)
    print("AURELIAN VDR - DEEP DOCX REFERENCE SCAN")
    print("Scanning 8 files (5 Tier 3 + 3 Tier 2) for problematic references")
    print(sep)
    print(f"OneDrive: {onedrive}")
    print(f"VDR base exists: {os.path.exists(B)}")
    total = 0
    all_f = []
    for idx, (fp, tier) in enumerate(zip(FILES, TIERS), 1):
        sn = os.path.basename(fp)
        print()
        print(ln)
        print(f"[{idx}/8] {tier} | {sn}")
        print(f"       {fp}")
        print(ln)
        ff = scan_docx(fp)
        all_f.extend(ff)
        if ff:
            for f in ff:
                total += 1
                ctx = f["context"][:300]
                if len(f["context"]) > 300: ctx += "..."
                print(f"  MATCH #{total}")
                print("    Pattern  : " + f["pattern"])
                print("    Match    : " + f["match"])
                print("    Location : " + f["location"])
                print("    Context  : " + ctx)
                print()
        else:
            print("  No problematic references found.")
    print()
    print(sep)
    print(f"SUMMARY: {total} problematic reference(s) found across {len(FILES)} files")
    print(sep)
    if all_f:
        bp = {}
        for f in all_f: bp.setdefault(f["pattern"], []).append(f)
        print()
        print("Breakdown by pattern:")
        for p, items in sorted(bp.items()):
            print(f"  {p}: {len(items)} occurrence(s)")
            for it in items:
                print("    - " + it["file"] + " | " + it["location"])
        print()
        print("Breakdown by file:")
        bf = {}
        for f in all_f: bf.setdefault(f["file"], []).append(f)
        for fn, items in sorted(bf.items()):
            print(f"  {fn}: {len(items)} issue(s)")
            for it in items:
                print("    - [" + it["pattern"] + "] in " + it["location"])
    else:
        print()
        print("All files are clean. No problematic references detected.")
    print()
    print(sep)
    print("Scan complete.")

if __name__ == "__main__":
    main()
