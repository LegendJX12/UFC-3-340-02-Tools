"""Map every plot (.grf) file to its figure in the UFC 3-340-02 guide.

Match levels (first that works wins):
  A caption      - figure caption found in the guide text (database table 'captions')
  B index        - figure listed in the index spreadsheet (batch file + PDF page)
  C text-ref     - figure number mentioned in guide text (e.g. "Plot Figure 2A-19")
  D not found    - no match; needs manual check

Usage:
  python3 scripts/map_grf.py --db reference/ufc_340_02.db --grf-root graphs/UFC_Plots_data --csv reference/plots/grf_to_guide.csv
"""
import argparse, csv, glob, os, re, sqlite3


def derive_key(name):
    m = re.match(r'([A-Za-z]?\d+)_(\d+)([A-Za-z]?)\.grf$', name, re.I)
    if not m:
        return None, None
    a, num, sub = m.group(1), int(m.group(2)), m.group(3).upper()
    key = f'{int(a)}-{num}' if a.isdigit() else f'{int(a[1:])}A-{num}'
    return key, sub


# Plot files in chapter 6 use the older TM 5-1300 figure numbers. The guide (UFC 3-340-02)
# inserted three figures earlier in chapter 6, so guide figure = plot figure + 3.
# Checked against titles and a/b ratios: 06_012 -> 6-15, 06_028A -> 6-31 (a/b=1.00),
# 06_048A -> 6-51 (a/b=4.00), 06_049 -> 6-52, 06_050 -> 6-53.
CHAPTER_OFFSET = {'6': 3}

# Manual links where the guide caption was not read by OCR.
OVERRIDES = {
    '02_194A.grf': (6, 45, 'Figure 2-194(a); caption read only on contents page and figure not in index; '
                           'page and curve values confirmed against the chart'),
    '02_194B.grf': (6, 46, 'Figure 2-194(b); caption read only on contents page and figure not in index; '
                           'page and curve values confirmed against the chart'),
    '04_065.grf': (23, 18, 'plot "Spall threshold for blast waves loading walls" (axes i_r v/P1 Tc vs P_r/sigma) '
                           'is not drawn in UFC 3-340-02, likely kept from TM 5-1300; linked to Figure 4-65 '
                           '(spall geometry) and section 4-55. The guide spall chart on batch 23 page 19 '
                           '(h/R vs spall parameter) has no plot file'),
}


def to_guide_number(plot_key):
    ch, num = plot_key.split('-')
    off = CHAPTER_OFFSET.get(ch)
    return f'{ch}-{int(num) + off}' if off else plot_key


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
    db.execute('''CREATE TABLE grf_guide_links(grf_file TEXT PRIMARY KEY, folder TEXT, plot_number TEXT, figure TEXT,
                  subcurve TEXT, level TEXT, guide_batch INT, guide_page INT, guide_caption TEXT,
                  nearest_image TEXT, index_batch_file TEXT, index_pdf_page INT, index_ufc_page TEXT,
                  caption_in_plot TEXT, caption_overlap REAL, note TEXT)''')

    captions = {}
    for num, b, p, c in db.execute("SELECT number, batch, page, caption FROM captions WHERE kind='figure'"):
        captions.setdefault(num.upper(), []).append((b, p, c))
    images = {}
    for num, b, p, img in db.execute("SELECT number, batch, page, nearest_image FROM figures WHERE nearest_image IS NOT NULL"):
        images[(num.upper(), b, p)] = img
    pic_pages = set(db.execute("SELECT DISTINCT batch, page FROM images WHERE kind IN ('chart','image','table')").fetchall())

    # contents pages: many figure captions on the page, or many dot-leader lines in the PDF text
    toc_pages = set((b, p) for b, p, n in db.execute(
        "SELECT batch, page, COUNT(*) FROM captions WHERE kind='figure' GROUP BY batch, page HAVING COUNT(*) >= 5"))
    for b, p, t in db.execute('SELECT batch, page, text FROM pdf_pages'):
        if len(re.findall(r'\.{6,}', t or '')) >= 5:
            toc_pages.add((b, p))

    # index entries per base figure number; prefer an entry whose page holds a picture
    index_all = {}
    for num, bf, pg, ufc in db.execute("SELECT number, batch_file, pdf_page_in_batch, ufc_page FROM index_entries WHERE type='Figure'"):
        base_num = re.sub(r'\s*\(?[A-Za-z]\)?$', '', num.strip()) if re.search(r'-\d+\s*\(?[A-Za-z]\)?$', num.strip()) else num.strip()
        index_all.setdefault(base_num.upper(), []).append((bf, pg, ufc))

    def has_pic(e):
        mb = re.search(r'batch (\d+)', e[0] or '')
        return mb is not None and (int(mb.group(1)), e[1]) in pic_pages
    index = {k: sorted(entries, key=lambda e: not has_pic(e))[0] for k, entries in index_all.items()}

    def is_toc(caption):
        return bool(re.search(r'\.{2,}|…|\d+-\d+\s*$', caption or ''))

    def best_hit(hits):
        # real figure page first: has a picture and is not a table-of-contents line
        return sorted(hits, key=lambda h: (is_toc(h[2]), (h[0], h[1]) not in pic_pages, h[0], h[1]))[0]
    text_refs = {}
    for b, p, content in db.execute('SELECT batch, page, content FROM blocks'):
        for m in re.finditer(r'Figure\s*(\d+[A-Z]?-\d+)', content or '', re.I):
            text_refs.setdefault(m.group(1).upper(), []).append((b, p))

    counts = {'A caption': 0, 'B index': 0, 'C text-ref': 0, 'D not found': 0, 'E manual': 0}
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
            out_rows.append([name, folder, '', '', sub, 'D not found', '', '', '', '', '', '', '', plot_caption, '', 'file name not recognised'])
            continue
        plot_number = key
        generated = folder.split(os.sep)[0] == 'generated'
        if not generated:
            key = to_guide_number(key)  # generated files already use guide numbers
        gb = gp = gc = img = ib = ip = iu = ''
        level, note = 'D not found', ''
        sub_key = (key + sub).upper() if sub else None
        cap_key = sub_key if sub_key and sub_key in captions else key.upper()
        sibling = False
        if cap_key not in captions:
            sibs = sorted(k for k in captions if re.fullmatch(re.escape(key.upper()) + r'[A-Z]', k))
            if sibs:
                cap_key, sibling = sibs[0], True
        real_hits = [h for h in captions.get(cap_key, []) if (h[0], h[1]) not in toc_pages]
        if real_hits:
            hits = real_hits
            gb, gp, gc = best_hit(hits)
            img = images.get((cap_key, gb, gp), '') or ''
            level = 'A caption'
            if sibling:
                note = f'panel {sub} caption not found; linked to sibling panel {cap_key}'
        elif key.upper() in index:
            ib, ip, iu = index[key.upper()]
            level = 'B index'
            note = 'index gives batch and PDF page; figure caption not read by OCR on the figure page'
            mb = re.search(r'batch (\d+)', ib or '')
            gb = int(mb.group(1)) if mb else ''
            gp = ip
        elif key.upper() in text_refs:
            gb, gp = text_refs[key.upper()][0]
            level = 'C text-ref'
            note = 'figure is mentioned in guide text but no caption block found'
        else:
            note = 'no caption, index entry or text mention found'
        if name in OVERRIDES:
            gb, gp, note = OVERRIDES[name]
            level, gc, img = 'E manual', '', ''
        if plot_number != key:
            note = (note + '; ' if note else '') + f'plot file numbered {plot_number} (TM 5-1300); guide figure {key}'
        if generated:
            note = 'GENERATED (computed by scripts/generate_missing.py); ' + note
        overlap = caption_overlap(gc, plot_caption) if (gc and plot_caption) else ''
        if overlap != '' and overlap < 0.5:
            note = (note + '; ' if note else '') + 'plot title and guide caption differ, check'
        counts[level] += 1
        out_rows.append([name, folder, plot_number, key, sub, level, gb, gp, gc, img, ib, ip, iu, plot_caption, overlap, note])

    header = ['grf_file', 'folder', 'plot_number', 'figure', 'subcurve', 'level', 'guide_batch', 'guide_page',
              'guide_caption', 'nearest_image', 'index_batch_file', 'index_pdf_page', 'index_ufc_page',
              'caption_in_plot', 'caption_overlap', 'note']
    with open(a.csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(out_rows)
    for r in out_rows:
        db.execute('INSERT INTO grf_guide_links VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                   (r[0], r[1], r[2], r[3], r[4], r[5],
                    r[6] or None, r[7] or None, r[8], r[9], r[10], r[11] or None, r[12], r[13], r[14] or None, r[15]))
    db.commit()
    print('plot files:', len(files))
    for k, v in counts.items():
        print(f'{k:12s}', v)


if __name__ == '__main__':
    main()
