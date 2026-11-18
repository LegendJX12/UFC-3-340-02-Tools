"""Map every plot (.grf) file to its figure in the UFC 3-340-02 guide.

Match levels (first that works wins):
  A caption      - figure caption found in the guide text (database table 'captions')
  B index        - figure listed in the index spreadsheet (batch file + PDF page)
  C text-ref     - figure number mentioned in guide text (e.g. "Plot Figure 2A-19")
  D not found    - no match; needs manual check

Usage:
  python3 scripts/map_grf.py --db reference/ufc_340_02.db --grf-root graphs/UFC_Plots_data --csv reference/grf_to_guide.csv
"""
import argparse, csv, glob, os, re, sqlite3


def derive_key(name):
    m = re.match(r'([A-Za-z]?\d+)_(\d+)([A-Za-z]?)\.grf$', name, re.I)
    if not m:
        return None, None
    a, num, sub = m.group(1), int(m.group(2)), m.group(3).upper()
    key = f'{int(a)}-{num}' if a.isdigit() else f'{int(a[1:])}A-{num}'
    return key, sub


def squash(s):
    return re.sub(r'[^a-z]', '', s.lower())


def caption_overlap(guide, plot):
    """Share of plot-title words (4+ letters) found in the guide caption, ignoring spaces."""
    g = squash(guide)
    words = re.findall(r'[a-z]{4,}', plot.lower())
    if not words:
        return ''
    return round(sum(1 for w in words if w in g) / len(words), 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--grf-root', required=True)
    ap.add_argument('--csv', required=True)
    a = ap.parse_args()

    db = sqlite3.connect(a.db)
    db.execute('DROP TABLE IF EXISTS grf_guide_links')
    db.execute('''CREATE TABLE grf_guide_links(grf_file TEXT PRIMARY KEY, folder TEXT, figure TEXT,
                  subcurve TEXT, level TEXT, guide_batch INT, guide_page INT, guide_caption TEXT,
                  nearest_image TEXT, index_batch_file TEXT, index_pdf_page INT, index_ufc_page TEXT,
                  caption_in_plot TEXT, caption_overlap REAL, note TEXT)''')

    captions = {}
    for num, b, p, c in db.execute("SELECT number, batch, page, caption FROM captions WHERE kind='figure'"):
        captions.setdefault(num.upper(), []).append((b, p, c))
    images = {}
    for num, img in db.execute("SELECT number, nearest_image FROM figures WHERE nearest_image IS NOT NULL"):
        images.setdefault(num.upper(), img)
    index = {}
    for num, bf, pg, ufc in db.execute("SELECT number, batch_file, pdf_page_in_batch, ufc_page FROM index_entries WHERE type='Figure'"):
        index.setdefault(num.upper(), (bf, pg, ufc))
    text_refs = {}
    for b, p, content in db.execute('SELECT batch, page, content FROM blocks'):
        for m in re.finditer(r'Figure\s*(\d+[A-Z]?-\d+)', content or '', re.I):
            text_refs.setdefault(m.group(1).upper(), []).append((b, p))

    counts = {'A caption': 0, 'B index': 0, 'C text-ref': 0, 'D not found': 0}
    out_rows = []
    files = sorted(set(glob.glob(os.path.join(a.grf_root, '**', '*.grf'), recursive=True) +
                       glob.glob(os.path.join(a.grf_root, '**', '*.GRF'), recursive=True)))
    for f in files:
        name = os.path.basename(f)
        key, sub = derive_key(name)
        folder = os.path.relpath(os.path.dirname(f), a.grf_root)
        raw = open(f, 'rb').read().decode('latin-1')
        plot_caption = ''
        cm = re.search(r'Figure\s+\d+[A-Za-z]?-\d+[^\n\r]*', raw)
        if cm:
            plot_caption = cm.group(0).strip()
        if key is None:
            counts['D not found'] += 1
            out_rows.append([name, folder, '', sub, 'D not found', '', '', '', '', '', '', '', plot_caption, '', 'file name not recognised'])
            continue
        gb = gp = gc = img = ib = ip = iu = ''
        level, note = 'D not found', ''
        if key.upper() in captions:
            hits = captions[key.upper()]
            gb, gp, gc = hits[0][0], hits[0][1], hits[0][2]
            img = images.get(key.upper(), '') or ''
            level = 'A caption'
            if len(hits) > 1:
                note = f'caption appears on {len(hits)} pages; first shown'
        elif key.upper() in index:
            ib, ip, iu = index[key.upper()]
            level = 'B index'
            note = 'index gives batch and PDF page; caption not found in OCR text'
            mb = re.search(r'batch (\d+)', ib or '')
            gb = int(mb.group(1)) if mb else ''
            gp = ip
        elif key.upper() in text_refs:
            gb, gp = text_refs[key.upper()][0]
            level = 'C text-ref'
            note = 'figure is mentioned in guide text but no caption block found'
        else:
            note = 'no caption, index entry or text mention found'
        overlap = caption_overlap(gc, plot_caption) if (gc and plot_caption) else ''
        if overlap != '' and overlap < 0.5:
            note = (note + '; ' if note else '') + 'plot title and guide caption differ, check'
        counts[level] += 1
        out_rows.append([name, folder, key, sub, level, gb, gp, gc, img, ib, ip, iu, plot_caption, overlap, note])

    header = ['grf_file', 'folder', 'figure', 'subcurve', 'level', 'guide_batch', 'guide_page',
              'guide_caption', 'nearest_image', 'index_batch_file', 'index_pdf_page', 'index_ufc_page',
              'caption_in_plot', 'caption_overlap', 'note']
    with open(a.csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(out_rows)
    for r in out_rows:
        db.execute('INSERT INTO grf_guide_links VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                   (r[0], r[1], r[2], r[3], r[4],
                    r[5] or None, r[6] or None, r[7], r[8], r[9], r[10] or None, r[11], r[12], r[13] or None, r[14]))
    db.commit()
    print('plot files:', len(files))
    for k, v in counts.items():
        print(f'{k:12s}', v)


if __name__ == '__main__':
    main()
