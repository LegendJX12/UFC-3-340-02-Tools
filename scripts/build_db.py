"""Build a SQLite database of UFC 3-340-02 from OCR output, index and plot files.

Usage:
  python3 scripts/build_db.py --ocr-root <folder with 'batch N' folders> \
      --grf-root <folder with plot .grf files> \
      --index <index .xlsx> --out reference/ufc_340_02.db
"""
import argparse, glob, json, os, re, sqlite3
import openpyxl

CHAPTERS = [  # chapter, first batch, last batch, title (from chapter file headers)
    (1, 1, 1, 'Introduction'),
    (2, 2, 10, 'Blast, Fragment, and Shock Loads'),
    (3, 11, 18, 'Principles of Dynamic Analysis'),
    (4, 19, 26, 'Reinforced Concrete Design'),
    (5, 27, 30, 'Structural Steel Design'),
    (6, 31, 35, 'Special Considerations in Explosive Facility Design'),
]
NUM_RE = re.compile(r'^\s*-?[\d.]+(?:[eE][-+]?\d+)?\s*,\s*-?[\d.]+(?:[eE][-+]?\d+)?\s*$')
FIG_RE = re.compile(r'^\s*(?i:figure)\s+(\d+[A-Z]?-\d+[a-z]?)(?![a-z])')
TAB_RE = re.compile(r'^\s*(?i:table)\s+(\d+[A-Z]?-\d+[a-z]?)(?![a-z])')
IMG_RE = re.compile(r'img_in_(\w+?)_box_(\d+)_(\d+)_(\d+)_(\d+)\.jpg$', re.I)


def chapter_of(batch):
    for ch, a, b, _ in CHAPTERS:
        if a <= batch <= b:
            return ch
    return None


def bbox(v):
    try:
        vals = json.loads(v) if isinstance(v, str) else list(v)
        return [float(x) for x in vals[:4]]
    except Exception:
        return [None, None, None, None]


def find_batch_dirs(root):
    """Find folders named 'batch N' or 'batch-NN' that contain page_*_res.json files."""
    out = {}
    for d in glob.glob(os.path.join(root, '**', 'batch*'), recursive=True):
        m = re.search(r'batch[ -](\d+)$', d)
        if m and os.path.isdir(d) and glob.glob(os.path.join(d, 'page_*_res.json')):
            out[int(m.group(1))] = d
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ocr-root', required=True)
    ap.add_argument('--grf-root', required=True)
    ap.add_argument('--index', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    if os.path.exists(a.out):
        os.remove(a.out)
    db = sqlite3.connect(a.out)
    db.executescript('''
    CREATE TABLE chapters(chapter INT PRIMARY KEY, batch_from INT, batch_to INT, title TEXT);
    CREATE TABLE pages(batch INT, page INT, chapter INT, width INT, height INT,
                       block_count INT, text TEXT, PRIMARY KEY(batch, page));
    CREATE TABLE blocks(batch INT, page INT, block_id INT, label TEXT, content TEXT,
                        x1 REAL, y1 REAL, x2 REAL, y2 REAL);
    CREATE TABLE images(file TEXT PRIMARY KEY, batch INT, page INT, kind TEXT,
                        x1 INT, y1 INT, x2 INT, y2 INT);
    CREATE TABLE captions(kind TEXT, number TEXT, caption TEXT, batch INT, page INT,
                          block_id INT, PRIMARY KEY(kind, number, batch, page, block_id));
    CREATE TABLE figures(number TEXT, batch INT, page INT, caption TEXT,
                         nearest_image TEXT, plot_files TEXT);
    CREATE TABLE index_entries(type TEXT, number TEXT, title TEXT, batch_file TEXT,
                               pdf_page_in_batch INT, ufc_page TEXT, chapter INT);
    CREATE TABLE plot_files(file TEXT PRIMARY KEY, folder TEXT, captions TEXT, point_count INT);
    CREATE TABLE plot_points(file TEXT, seq INT, x REAL, y REAL);
    CREATE TABLE plot_labels(file TEXT, line_no INT, text TEXT);
    ''')
    db.executemany('INSERT INTO chapters VALUES (?,?,?,?)', CHAPTERS)

    # ---- OCR pages, blocks, images, captions
    batch_dirs = find_batch_dirs(a.ocr_root)
    print('batches found:', len(batch_dirs))
    all_caps = []
    for b in sorted(batch_dirs):
        d = batch_dirs[b]
        img_dir = os.path.join(d, 'imgs')
        imgs = {}
        for f in glob.glob(os.path.join(img_dir, '*.jpg')) if os.path.isdir(img_dir) else []:
            name = os.path.basename(f)
            m = IMG_RE.search(name)
            kind = m.group(1) if m else 'other'
            coords = [int(x) for x in m.groups()[1:]] if m else [None] * 4
            imgs[name] = (kind, coords)
        for jf in sorted(glob.glob(os.path.join(d, 'page_*_res.json'))):
            pg = int(re.search(r'page_(\d+)_res', jf).group(1))
            data = json.load(open(jf, encoding='utf-8'))
            md_path = os.path.join(d, f'page_{pg:04d}.md')
            if os.path.exists(md_path):
                text = open(md_path, encoding='utf-8', errors='ignore').read()
            else:
                text = '\n'.join((x.get('block_content') or '') for x in (data.get('parsing_res_list') or []))
            blocks = data.get('parsing_res_list', []) or []
            db.execute('INSERT INTO pages VALUES (?,?,?,?,?,?,?)',
                       (b, pg, chapter_of(b), data.get('width'), data.get('height'), len(blocks), text))
            for blk in blocks:
                x1, y1, x2, y2 = bbox(blk.get('block_bbox'))
                content = blk.get('block_content') or ''
                bid = blk.get('block_id')
                db.execute('INSERT INTO blocks VALUES (?,?,?,?,?,?,?,?,?)',
                           (b, pg, int(bid) if str(bid).isdigit() else None,
                            blk.get('block_label'), content, x1, y1, x2, y2))
                for line in content.split('\n'):
                    first = line.strip()
                    fm = FIG_RE.match(first)
                    tm = TAB_RE.match(first)
                    if fm:
                        all_caps.append(('figure', fm.group(1), first, b, pg, bid, (x1, y1, x2, y2)))
                        db.execute('INSERT OR IGNORE INTO captions VALUES (?,?,?,?,?,?)',
                                   ('figure', fm.group(1), first, b, pg,
                                    int(bid) if str(bid).isdigit() else None))
                    if tm:
                        all_caps.append(('table', tm.group(1), first, b, pg, bid, (x1, y1, x2, y2)))
                        db.execute('INSERT OR IGNORE INTO captions VALUES (?,?,?,?,?,?)',
                                   ('table', tm.group(1), first, b, pg,
                                    int(bid) if str(bid).isdigit() else None))
    db.commit()

    # ---- images: link each image to its page by matching its box coordinates to block boxes
    db.execute('DROP TABLE IF EXISTS images')
    db.execute('CREATE TABLE images(file TEXT, batch INT, page INT, kind TEXT, x1 INT, y1 INT, '
               'x2 INT, y2 INT, page_ambiguous INT, PRIMARY KEY(batch, file))')
    where = {}
    for b, pg, x1, y1, x2, y2 in db.execute(
            'SELECT batch, page, x1, y1, x2, y2 FROM blocks WHERE x1 IS NOT NULL'):
        key = (b, int(x1), int(y1), int(x2), int(y2))
        where.setdefault(key, set()).add(pg)
    for b in sorted(batch_dirs):
        d = batch_dirs[b]
        img_dir = os.path.join(d, 'imgs')
        for f in sorted(glob.glob(os.path.join(img_dir, '*.jpg'))) if os.path.isdir(img_dir) else []:
            name = os.path.basename(f)
            m = IMG_RE.search(name)
            kind = m.group(1) if m else 'other'
            c = [int(x) for x in m.groups()[1:]] if m else [None] * 4
            pages = sorted(where.get((b, *c), [])) if m else []
            pg = pages[0] if pages else None
            db.execute('INSERT INTO images VALUES (?,?,?,?,?,?,?,?,?)',
                       (name, b, pg, kind, *c, 1 if len(pages) > 1 else 0))
    db.commit()

    # ---- index spreadsheet
    ws = openpyxl.load_workbook(a.index).active
    n_idx = 0
    for r in ws.iter_rows(min_row=2, values_only=True):
        if not r[0]:
            continue
        db.execute('INSERT INTO index_entries VALUES (?,?,?,?,?,?,?)',
                   (r[0], str(r[1]), r[2], r[3], r[4], str(r[5]) if r[5] is not None else None, r[6]))
        n_idx += 1
    print('index entries:', n_idx)

    # ---- plot files (.grf)
    grf_files = glob.glob(os.path.join(a.grf_root, '**', '*.grf'), recursive=True) + \
                glob.glob(os.path.join(a.grf_root, '**', '*.GRF'), recursive=True)
    fig_to_plots = {}
    for f in sorted(set(grf_files)):
        raw = open(f, 'rb').read().decode('latin-1')
        lines = raw.replace('\r', '').split('\n')
        name = os.path.basename(f)
        folder = os.path.relpath(os.path.dirname(f), a.grf_root)
        caps = sorted(set(re.findall(r'Figure\s+(\d+-\d+[A-Za-z]?)', raw)))
        pts = 0
        seq = 0
        for i, line in enumerate(lines):
            s = line.strip()
            if not s:
                continue
            if NUM_RE.match(s):
                x, y = s.split(',')
                db.execute('INSERT INTO plot_points VALUES (?,?,?,?)', (name, seq, float(x), float(y)))
                seq += 1
                pts += 1
            else:
                db.execute('INSERT INTO plot_labels VALUES (?,?,?)', (name, i + 1, s))
        db.execute('INSERT INTO plot_files VALUES (?,?,?,?)', (name, folder, ', '.join(caps), pts))
        for c in caps:
            fig_to_plots.setdefault(c, []).append(name)
    db.commit()
    print('plot files:', len(grf_files))

    # ---- figures: caption + nearest image on the same page + matching plot files
    for kind, number, caption, b, pg, bid, (x1, y1, x2, y2) in all_caps:
        if kind != 'figure':
            continue
        cands = db.execute('SELECT file, x1, y1, x2, y2 FROM images WHERE batch=? AND page=? '
                           'AND kind IN ("chart","image","table")', (b, pg)).fetchall()
        near = None
        if cands and y1 is not None:
            cy = (y1 + y2) / 2
            near = min(cands, key=lambda c: abs(((c[2] + c[4]) / 2) - cy))[0]
        plots = fig_to_plots.get(number, [])
        db.execute('INSERT INTO figures VALUES (?,?,?,?,?,?)',
                   (number, b, pg, caption, near, ', '.join(sorted(plots))))
    db.commit()

    # ---- summary
    for t in ['chapters', 'pages', 'blocks', 'images', 'captions', 'figures',
              'index_entries', 'plot_files', 'plot_points', 'plot_labels']:
        print(f'{t:14s}', db.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0])
    db.execute('VACUUM')
    db.close()


if __name__ == '__main__':
    main()
