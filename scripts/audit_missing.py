"""List every figure and table in UFC 3-340-02 with its data status.

Figures come from the index spreadsheet plus figure captions found on real figure pages
(contents pages excluded). Sub-panels such as 3-187(B) or 2-100a count as one figure.

Figure status:
  has plot data            - at least one .grf file is linked to the figure
  MISSING DATA             - a data chart with no plot file; needs digitizing
  example plot             - worked-example plot; key values are printed on it or in the text
  no data needed           - schematic, sketch, layout or photo
Table status:
  cells captured           - OCR captured the table cells (values still to be checked)
  MISSING DATA             - table body not available

The manual entries below come from viewing each chart image (Nov 2026 review).

Usage:
  python3 scripts/audit_missing.py --db reference/ufc_340_02.db --csv reference/missing_data.csv
"""
import argparse, collections, csv, re, sqlite3

MISSING = {  # figure: (priority, note)
    '2-8': ('high', 'Negative phase shock wave parameters, spherical TNT free-air burst. Scanned chart; no 02_008.grf.'),
    '2-16': ('high', 'Negative phase shock wave parameters, hemispherical TNT surface burst. Only 02_016.BMP '
                     '(a picture, no numbers).'),
    '3-64': ('high', 'Maximum response, elasto-plastic SDOF, bilinear-triangular pulse (C1 = 1.000), panels (a) and (b). '
                     'Scanned chart; plot files 03_062 to 03_064 do not exist.'),
    '3-220': ('high', 'Maximum response chart, bilinear-triangular pulse. Scanned; plot files skip 03_220 to 03_224.'),
    '3-221': ('high', 'As 3-220.'),
    '3-222': ('high', 'As 3-220.'),
    '3-223': ('high', 'As 3-220.'),
    '3-224': ('high', 'As 3-220.'),
    '6-21': ('low', 'Roof live load vs supported tributary area: 20 psf up to 200 ft2, straight line to 12 psf '
                    'at 600 ft2, 12 psf beyond. Simple enough to code as a formula.'),
    '6-11': ('low', 'Resistance-deflection plot, unreinforced masonry wall with axial load arching.'),
}
EXAMPLES = ['2A-6', '2A-10', '2A-11', '2A-12', '2A-13', '2A-16', '3-267', '5A-9', '6A-2', '6A-4']
SCHEMATIC = ['1-6', '2-11', '2-12', '2-151', '2-183', '2-191', '2-195', '2-199', '2-201', '2-202', '2-246',
             '2-247', '2-249', '2-253', '2A-1', '2A-2', '3-21', '3-39', '3-40', '3-45', '3-46', '3-47', '3-48',
             '3-269', '4-8', '4-20', '4-21', '4-26', '4-61', '4-72', '4-84', '4-94', '4-100', '4-106', '4-107',
             '4A-3', '4A-5', '4A-19', '5-1', '5-7', '5-10', '5-12', '5-22', '5A-10', '6-13', '6-30', '6-56',
             '6-57', '6-58', '6-71', '6A-9']
FIX = {  # corrected title and page where the index entry is wrong
    '3-64': ('Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular '
             'Pulse (C1 = 1.000), panels (a) and (b)', 13, 49),
}
OCR_NOISE = {'2A-1640'}  # misread duplicate of 2A-16
TABLE_NOTES = {
    '5-4': ('MISSING DATA', 'high', 'Table body is blank in the source PDF (batch 28 page 3); only the caption and '
                                    'footnote "* Whichever governs" are present. Get it from another copy of the guide.'),
    '4-1': (None, None, 'Index page (batch 19 p34) only mentions the table; cells are on batch 19 page 42.'),
}


def base(n):
    n = n.strip()
    m = re.match(r'(\d+[A-Z]?-\d+)\s*(?:\(?[A-Za-z]\)?)?$', n)
    return m.group(1).upper() if m else n.upper()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--csv', required=True)
    a = ap.parse_args()
    db = sqlite3.connect(a.db)

    toc = set(db.execute("SELECT batch, page FROM captions WHERE kind='figure' "
                         "GROUP BY batch, page HAVING COUNT(*) >= 5").fetchall())
    figs = {}
    for num, bf, pg, title in db.execute("SELECT number, batch_file, pdf_page_in_batch, title "
                                         "FROM index_entries WHERE type='Figure'"):
        k = base(num)
        f = figs.setdefault(k, {'title': title or '', 'loc': [], 'src': 'index'})
        loc = (int(re.search(r'batch (\d+)', bf).group(1)), pg)
        if loc not in f['loc']:
            f['loc'].append(loc)
    for num, b, p, cap in db.execute("SELECT number, batch, page, caption FROM captions WHERE kind='figure'"):
        if (b, p) in toc:
            continue
        k = base(num)
        if k in OCR_NOISE:
            continue
        f = figs.setdefault(k, {'title': re.sub(r'^\s*Figure\s+\S+\s*', '', cap), 'loc': [], 'src': 'caption'})
        if (b, p) not in f['loc']:
            f['loc'].append((b, p))

    plots = collections.defaultdict(list)
    for g, fig in db.execute('SELECT grf_file, figure FROM grf_guide_links'):
        plots[fig.upper()].append(g)
    kinds = collections.defaultdict(set)
    for b, p, k in db.execute('SELECT batch, page, kind FROM images WHERE page IS NOT NULL'):
        kinds[(b, p)].add(k)

    rows = []
    for k, f in figs.items():
        ks = set().union(*[kinds[l] for l in f['loc']]) if f['loc'] else set()
        b, p = f['loc'][0] if f['loc'] else ('', '')
        prio, note = '', ''
        if plots.get(k):
            status = 'has plot data'
            note = f'{len(plots[k])} plot file(s): ' + ', '.join(sorted(plots[k])[:6]) + (' ...' if len(plots[k]) > 6 else '')
        elif k in MISSING:
            status = 'MISSING DATA'
            prio, note = MISSING[k]
        elif k in EXAMPLES:
            status, prio, note = 'example plot', 'low', 'Worked-example plot; key values printed on it or in the example text.'
        elif k in SCHEMATIC:
            status, note = 'no data needed', 'Schematic or sketch (checked by viewing).'
        elif 'chart' in ks:
            status, prio, note = 'MISSING DATA', 'check', 'Chart on page but no plot file; not yet reviewed by eye.'
        else:
            status, note = 'no data needed', 'Diagram, layout or photo (judged from page content and title).'
        title = re.sub(r'\s+', ' ', f['title']).strip()
        if k in FIX:
            title, b, p = FIX[k]
        rows.append(['figure', k, title, b, p, status, prio, note])

    for num, title, bf, pg in db.execute("SELECT number, title, batch_file, pdf_page_in_batch "
                                         "FROM index_entries WHERE type='Table'"):
        b = int(re.search(r'batch (\d+)', bf).group(1))
        cells = sum(c.count('<td') for (c,) in db.execute(
            "SELECT content FROM blocks WHERE batch=? AND page BETWEEN ? AND ? AND label='table'", (b, pg, pg + 2)))
        if not cells:
            for cb, cp in db.execute("SELECT DISTINCT batch, page FROM captions WHERE kind='table' AND number=?", (num,)):
                cells += sum(c.count('<td') for (c,) in db.execute(
                    "SELECT content FROM blocks WHERE batch=? AND page=? AND label='table'", (cb, cp)))
        status, prio, note = ('cells captured', '', 'OCR table cells; check values against the PDF before use.') \
            if cells >= 4 else ('MISSING DATA', 'check', 'No table cells found by OCR.')
        if num in TABLE_NOTES:
            s2, p2, n2 = TABLE_NOTES[num]
            status, prio, note = (s2 or status), (p2 or prio), n2
        rows.append(['table', num, re.sub(r'\s+', ' ', title or '').strip(), b, pg, status, prio, note])

    def sort_key(r):
        m = re.match(r'(\d+)([A-Z]?)-(\d+)', r[1])
        return (r[0], int(m.group(1)) if m else 99, m.group(2) if m else '', int(m.group(3)) if m else 0)
    rows.sort(key=sort_key)
    with open(a.csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['type', 'number', 'title', 'batch', 'page', 'status', 'priority', 'note'])
        w.writerows(rows)
    db.execute('DROP TABLE IF EXISTS data_status')
    db.execute('CREATE TABLE data_status(type TEXT, number TEXT, title TEXT, batch INT, page INT, '
               'status TEXT, priority TEXT, note TEXT)')
    db.executemany('INSERT INTO data_status VALUES (?,?,?,?,?,?,?,?)', rows)
    db.commit()
    c = collections.Counter((r[0], r[5]) for r in rows)
    for k in sorted(c):
        print(f'{k[0]:7s} {k[1]:16s} {c[k]}')


if __name__ == '__main__':
    main()
