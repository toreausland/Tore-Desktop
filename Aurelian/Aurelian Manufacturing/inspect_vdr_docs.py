import zipfile
import xml.etree.ElementTree as ET
import os
import json

base = r'C:\Users\mrntau\OneDrive - Mosseregionens Næringsutvikling AS\Skrivebord\Aurelian\Aurelian Manufacturing\Aurelian_VDR'

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
AURELIAN_RED = 'F50537'
AURELIAN_BLACK = '2B2B2B'
PANEL_GRAY = 'F5F5F5'

def check_docx(filepath):
    result = {
        'file': os.path.basename(filepath),
        'rel_path': os.path.relpath(filepath, base),
        'size': os.path.getsize(filepath),
        'fonts': set(),
        'has_calibri': False,
        'has_aurelian_red': False,
        'has_header': False,
        'header_text': '',
        'has_footer': False,
        'footer_text': '',
        'has_confidential': False,
        'colors_found': set(),
        'table_count': 0,
        'has_dark_header_tables': False,
        'has_alt_row_shading': False,
        'first_text': '',
        'title_text': '',
        'has_references_section': False,
    }

    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            # Check styles.xml
            if 'word/styles.xml' in z.namelist():
                root = ET.fromstring(z.read('word/styles.xml'))
                for font in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts'):
                    for attr in ['ascii', 'hAnsi', 'cs', 'eastAsia']:
                        val = font.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}' + attr)
                        if val:
                            result['fonts'].add(val)
                            if 'calibri' in val.lower():
                                result['has_calibri'] = True
                for color in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}color'):
                    val = color.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
                    if val and val != 'auto':
                        result['colors_found'].add(val.upper())
                        if AURELIAN_RED in val.upper():
                            result['has_aurelian_red'] = True

            # Check document.xml
            if 'word/document.xml' in z.namelist():
                root = ET.fromstring(z.read('word/document.xml'))

                # Get text content
                all_text = []
                for para in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                    texts = para.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
                    text = ''.join(t.text or '' for t in texts).strip()
                    if text:
                        all_text.append(text)
                        if not result['first_text']:
                            result['first_text'] = text[:120]
                        # Check for References section
                        if 'references' in text.lower() and len(text) < 30:
                            result['has_references_section'] = True

                # Check for title style
                for para in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')[:5]:
                    pPr = para.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr')
                    if pPr is not None:
                        pStyle = pPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pStyle')
                        if pStyle is not None:
                            sv = pStyle.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '')
                            if 'title' in sv.lower() or sv in ['Heading1', 'Heading 1']:
                                texts = para.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
                                result['title_text'] = ''.join(t.text or '' for t in texts).strip()[:120]

                # Check colors in document
                for color in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}color'):
                    val = color.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
                    if val and val != 'auto':
                        result['colors_found'].add(val.upper())
                        if AURELIAN_RED in val.upper():
                            result['has_aurelian_red'] = True

                # Check fonts in document
                for font in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts'):
                    for attr in ['ascii', 'hAnsi']:
                        val = font.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}' + attr)
                        if val:
                            result['fonts'].add(val)
                            if 'calibri' in val.lower():
                                result['has_calibri'] = True

                # Count tables and check table styling
                tables = root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl')
                result['table_count'] = len(tables)

                for tbl in tables:
                    rows = tbl.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr')
                    if rows:
                        # Check first row for dark header
                        first_row = rows[0]
                        for shd in first_row.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}shd'):
                            fill = shd.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill', '')
                            if fill.upper() in [AURELIAN_BLACK, '000000', '1F1F1F', '333333', '2B2B2B']:
                                result['has_dark_header_tables'] = True
                        # Check for alternating row shading
                        if len(rows) > 3:
                            for shd in rows[2].findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}shd'):
                                fill = shd.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill', '')
                                if fill.upper() in [PANEL_GRAY, 'F5F5F5', 'F2F2F2', 'FAFAFA']:
                                    result['has_alt_row_shading'] = True

                # Check for shading/fills
                for shd in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}shd'):
                    fill = shd.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill')
                    if fill and fill != 'auto':
                        result['colors_found'].add(fill.upper())
                        if AURELIAN_RED in fill.upper():
                            result['has_aurelian_red'] = True
                        if fill.upper() == AURELIAN_BLACK:
                            result['has_dark_header_tables'] = True

                # Check for border colors (red line at top)
                for border_elem in ['top', 'bottom', 'left', 'right']:
                    for b in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}' + border_elem):
                        bc = b.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}color', '')
                        if AURELIAN_RED in bc.upper():
                            result['has_aurelian_red'] = True

            # Check headers
            for hdr in ['word/header1.xml', 'word/header2.xml', 'word/header3.xml']:
                if hdr in z.namelist():
                    result['has_header'] = True
                    root = ET.fromstring(z.read(hdr))
                    texts = root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
                    ht = ' '.join(t.text or '' for t in texts).strip()
                    if ht:
                        result['header_text'] = (result['header_text'] + ' ' + ht).strip()

            # Check footers
            for ftr in ['word/footer1.xml', 'word/footer2.xml', 'word/footer3.xml']:
                if ftr in z.namelist():
                    result['has_footer'] = True
                    root = ET.fromstring(z.read(ftr))
                    texts = root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
                    ft = ' '.join(t.text or '' for t in texts).strip()
                    if ft:
                        result['footer_text'] = (result['footer_text'] + ' ' + ft).strip()
                    if 'CONFIDENTIAL' in ft.upper() or 'KONFIDENSIELT' in ft.upper():
                        result['has_confidential'] = True
                    for color in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}color'):
                        val = color.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
                        if val and AURELIAN_RED in val.upper():
                            result['has_aurelian_red'] = True

    except Exception as e:
        result['error'] = str(e)

    # Convert sets
    result['fonts'] = sorted(list(result['fonts']))
    result['colors_found'] = sorted(list(c for c in result['colors_found'] if len(c) == 6))

    # Compliance scoring
    checks = {
        'Calibri font': result['has_calibri'],
        'Aurelian Red (#F50537)': result['has_aurelian_red'],
        'Header present': result['has_header'],
        'Header says Aurelian': 'aurelian' in result['header_text'].lower(),
        'Footer present': result['has_footer'],
        'CONFIDENTIAL label': result['has_confidential'],
        'Dark header tables (#2B2B2B)': result['has_dark_header_tables'],
        'Alternating row shading': result['has_alt_row_shading'],
        'References section': result['has_references_section'],
    }
    result['checks'] = checks
    result['score'] = sum(1 for v in checks.values() if v)
    result['max'] = len(checks)

    return result


# Run inspection
docx_files = []
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.docx') and not f.startswith('~$'):
            docx_files.append(os.path.join(root, f))
docx_files.sort()

results = []
for fp in docx_files:
    r = check_docx(fp)
    results.append(r)

# Print results
print(f"AURELIAN VDR DOCUMENT INSPECTION REPORT")
print(f"{'='*120}")
print(f"Inspected {len(results)} .docx files against Design Manual v2.0")
print(f"{'='*120}\n")

for r in results:
    score = r['score']
    mx = r['max']
    if score >= 7:
        status = "NEW DESIGN"
        icon = "GREEN"
    elif score >= 4:
        status = "PARTIAL"
        icon = "AMBER"
    else:
        status = "OLD/MINIMAL"
        icon = "RED"

    print(f"[{icon}] {r['rel_path']}")
    print(f"    Score: {score}/{mx} | Status: {status}")
    print(f"    Title: {r['title_text'] or r['first_text'] or '(no text found)'}")
    print(f"    Fonts: {', '.join(r['fonts'][:6])}")
    print(f"    Colors: {', '.join(r['colors_found'][:10])}")
    print(f"    Header: \"{r['header_text'][:80]}\"")
    print(f"    Footer: \"{r['footer_text'][:80]}\"")
    print(f"    Tables: {r['table_count']} | Dark headers: {r['has_dark_header_tables']} | Alt rows: {r['has_alt_row_shading']}")
    print(f"    Checks:")
    for name, passed in r['checks'].items():
        print(f"      {'PASS' if passed else 'FAIL'} {name}")
    print()

# Summary
print(f"\n{'='*120}")
print("SUMMARY")
print(f"{'='*120}")
green = sum(1 for r in results if r['score'] >= 7)
amber = sum(1 for r in results if 4 <= r['score'] < 7)
red = sum(1 for r in results if r['score'] < 4)
print(f"  NEW DESIGN (7+/9):  {green} files")
print(f"  PARTIAL (4-6/9):    {amber} files")
print(f"  OLD/MINIMAL (0-3/9): {red} files")

# Save JSON for HTML report
output = {
    'total': len(results),
    'green': green,
    'amber': amber,
    'red': red,
    'results': []
}
for r in results:
    output['results'].append({
        'file': r['file'],
        'rel_path': r['rel_path'],
        'score': r['score'],
        'max': r['max'],
        'fonts': r['fonts'],
        'colors': r['colors_found'],
        'header': r['header_text'],
        'footer': r['footer_text'],
        'title': r['title_text'] or r['first_text'],
        'tables': r['table_count'],
        'dark_headers': r['has_dark_header_tables'],
        'alt_rows': r['has_alt_row_shading'],
        'confidential': r['has_confidential'],
        'references': r['has_references_section'],
        'checks': {k: v for k, v in r['checks'].items()},
    })

json_path = os.path.join(os.path.dirname(base), 'vdr_inspection_results.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"\nJSON saved to: {json_path}")
