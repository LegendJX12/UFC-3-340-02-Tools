"""Export every numbered table of UFC 3-340-02 to CSV and check its numbers against a second reading.

Inputs
  reference/manual/table_pages.csv        which OCR table block(s) make up each table (hand-checked)
  reference/manual/table_corrections.csv  cell fixes made by reading the PDF page (hand-checked)
  reference/manual/tables/*.csv           tables typed in by hand (no OCR table, e.g. Table 5-4)

Check (two independent readings of every number)
  1. OCR reading: the PaddleOCR table (table `blocks`), after corrections.
  2. Second reading, taken from the PDF itself inside the table's box:
       - 'PDF text'  : the PDF text layer (exact), where the page has one
       - 'Tesseract' : a second OCR engine on a 400 dpi render, where the table is a scanned image
  Numbers are compared in reading order (row by row). A number that the two readings do not
  agree on is listed in table_checks.csv; each one was then read on the rendered page and either
  fixed (table_corrections.csv) or accepted with a reason (table_check_verdicts.csv).

Outputs
  reference/tables/table_<n>.csv       one file per table (first column = batch/page it came from)
  reference/tables/tables_index.csv    one row per table: title, pages, size, check result
  reference/tables/table_checks.csv    every number the two readings disagree on, with the verdict
  database: guide_tables, guide_table_cells, table_checks

Usage: python3 scripts/export_tables.py --db reference/ufc_340_02.db --pdf-root source/pdf \
           --manual reference/manual --out reference/tables
"""
import argparse, csv, difflib, html, json, os, re, shutil, sqlite3, subprocess, tempfile
from html.parser import HTMLParser
from collections import Counter

SCALE = 0.5  # OCR pixel coordinates are 144 dpi; PDF points are 72 dpi


# ---------- HTML table -> grid ----------
class _TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows, self.cell, self.attrs = [], None, {}

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.rows.append([])
        elif tag in ('td', 'th'):
            self.cell, self.attrs = [], dict(attrs)
        elif tag == 'img' and self.cell is not None:
            self.cell.append(' [image] ')

    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self.cell is not None:
            text = re.sub(r'\s+', ' ', ''.join(self.cell)).strip()
            if not self.rows:
                self.rows.append([])
            self.rows[-1].append((text, int(self.attrs.get('rowspan', 1) or 1), int(self.attrs.get('colspan', 1) or 1)))
            self.cell = None

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)


def html_to_grid(src, origins=None):
    """Return list of rows; rowspan/colspan cells are repeated so every row has the same width.
    If a set is given as origins, the (row, col) of each cell's first (top-left) copy is added to it."""
    p = _TableParser()
    p.feed(src)
    grid, pending = [], {}  # pending[(r, c)] = text carried down by rowspan
    for r, row in enumerate(p.rows):
        out, c = [], 0
        cells = list(row)
        while cells or (r, c) in pending:
            if (r, c) in pending:
                out.append(pending.pop((r, c)))
                c += 1
                continue
            text, rs, cs = cells.pop(0)
            if origins is not None:
                origins.add((r, c))
            for k in range(cs):
                out.append(text)
                for j in range(1, rs):
                    pending[(r + j, c + k)] = text
            c += cs
        grid.append(out)
    width = max((len(r) for r in grid), default=0)
    return [r + [''] * (width - len(r)) for r in grid]


# ---------- numbers ----------
FRAC = {'½': ' 1/2 ', '¼': ' 1/4 ', '¾': ' 3/4 ', '⅓': ' 1/3 ', '⅔': ' 2/3 ', '⅛': ' 1/8 '}


def numbers(s):
    """Numeric tokens in reading order, with thousands commas removed."""
    s = s or ''
    for k, v in FRAC.items():
        s = s.replace(k, v)
    s = s.replace('[image]', ' ')
    s = re.sub(r'\\(?:frac|dfrac|tfrac)\s*', ' ', s)
    s = re.sub(r'\\[A-Za-z]+', ' ', s)          # LaTeX commands
    s = re.sub(r'[{}^_$]', ' ', s)
    s = re.sub(r'(?<=\d),(?=\d{3}(?!\d))', '', s)  # 87,000 -> 87000
    return re.findall(r'\d+(?:\.\d+)?|\.\d+', s)


def same_value(a, b):
    try:
        return float(a) == float(b)
    except ValueError:
        return False


# ---------- PDF words with superscripts and subscripts kept ----------
_WORDS = {}


def page_words(page):
    """Words of a PDF page as (x0, y0, x1, y1, text). Smaller raised text is written ^{...} and smaller
    lowered text _{...}, so 10^{-4}, ft^{2} and f_{dc} keep their meaning (the plain text layer loses this)."""
    key = (page.parent.name, page.number)
    if key in _WORDS:
        return _WORDS[key]
    out = []
    for b in page.get_text('rawdict')['blocks']:
        for l in b.get('lines', []):
            spans = [sp for sp in l['spans'] if sp['chars']]
            if not spans:
                continue
            dx, dy = l['dir']
            up = (lambda sp: -sp['origin'][1]) if abs(dx) >= abs(dy) else (lambda sp: -sp['origin'][0] * (-dy))
            big = max(sp['size'] for sp in spans)
            mains = [sp for sp in spans if sp['size'] >= 0.85 * big]
            base = sorted(up(sp) for sp in mains)[len(mains) // 2]
            word, marks, box = [], [], None

            def flush():
                nonlocal word, marks, box
                if word:
                    txt, cur = '', ''
                    for ch, mk in zip(word, marks):
                        if mk != cur:
                            if cur:
                                txt += '}'
                            if mk:
                                txt += mk + '{'
                            cur = mk
                        txt += ch
                    if cur:
                        txt += '}'
                    out.append((box[0], box[1], box[2], box[3], txt))
                word, marks, box = [], [], None
            for sp in spans:
                mk = ''
                if sp['size'] < 0.85 * big:
                    off = up(sp) - base
                    mk = '^' if off > 0.12 * big else '_' if off < -0.05 * big else ''
                for ch in sp['chars']:
                    if ch['c'].isspace():
                        flush()
                        continue
                    word.append(ch['c'])
                    marks.append(mk)
                    bb = ch['bbox']
                    box = list(bb) if box is None else [min(box[0], bb[0]), min(box[1], bb[1]), max(box[2], bb[2]), max(box[3], bb[3])]
            flush()
    _WORDS[key] = out
    return out


# ---------- second reading ----------
def pdf_words(doc, page_no, box):
    """PDF text-layer words inside box (PDF points), sorted into lines."""
    page = doc[page_no - 1]
    x1, y1, x2, y2 = box
    ws = [w for w in page_words(page) if x1 - 2 <= (w[0] + w[2]) / 2 <= x2 + 2 and y1 - 2 <= (w[1] + w[3]) / 2 <= y2 + 2]
    return sort_lines([(w[0], w[1], w[2], w[3], w[4]) for w in ws])


def sort_lines(ws, tol=3.0):
    ws = sorted(ws, key=lambda w: (w[1] + w[3]) / 2)
    lines = []
    for w in ws:
        yc = (w[1] + w[3]) / 2
        if lines and abs(lines[-1][0] - yc) <= tol:
            lines[-1][1].append(w)
        else:
            lines.append([yc, [w]])
    return [sorted(l[1], key=lambda w: w[0]) for l in lines]


def tesseract_words(doc, page_no, box, tmpdir):
    """Second OCR engine on a 400 dpi render of the table box; returns words in lines (PDF points)."""
    import pymupdf
    page = doc[page_no - 1]
    dpi = 400
    clip = pymupdf.Rect(*box) & page.rect
    pix = page.get_pixmap(dpi=dpi, clip=clip, colorspace=pymupdf.csGRAY)
    png = os.path.join(tmpdir, 'cell.png')
    pix.save(png)
    tsv = subprocess.run(['tesseract', png, '-', '--psm', '6', 'tsv'], capture_output=True, text=True).stdout
    f = 72.0 / dpi
    ws = []
    for line in tsv.splitlines()[1:]:
        parts = line.split('\t')
        if len(parts) < 12 or not parts[11].strip():
            continue
        l, t, w, h = map(int, parts[6:10])
        ws.append((clip.x0 + l * f, clip.y0 + t * f, clip.x0 + (l + w) * f, clip.y0 + (t + h) * f, parts[11]))
    return sort_lines(ws, tol=4.0)


def page_has_text(doc, page_no, box):
    return sum(len(numbers(w[4])) for line in pdf_words(doc, page_no, box) for w in line)


# ---------- PDF grid (exact text) ----------
def text_dir(page, box):
    """'h' for normal text, 'up' for text rotated to read bottom-to-top, inside box."""
    import pymupdf
    up = h = 0
    for bl in page.get_text('dict', clip=pymupdf.Rect(*box))['blocks']:
        for l in bl.get('lines', []):
            if round(l['dir'][1]) == -1:
                up += 1
            elif round(l['dir'][0]) == 1:
                h += 1
    return 'up' if up > h else 'h'


def words_in(words, bb, rotated):
    x0, y0, x1, y1 = bb
    ws = [w for w in words if x0 - 1 <= (w[0] + w[2]) / 2 <= x1 + 1 and y0 - 1 <= (w[1] + w[3]) / 2 <= y1 + 1]
    if rotated:  # reading lines are columns of the page; words run upward
        ws = [(-w[3], w[0], -w[1], w[2], w[4]) for w in ws]
    return ' '.join(' '.join(w[4] for w in line) for line in sort_lines(ws))


def pdf_grid(page, ocr_box):
    import pymupdf
    """Rebuild the table that overlaps ocr_box from the PDF's ruling lines and exact words.
    Returns (grid, bbox, numeric words left outside every cell) or None."""
    import pymupdf
    best = None
    for t in page.find_tables().tables:
        r = pymupdf.Rect(t.bbox) & pymupdf.Rect(*ocr_box)
        ov = r.get_area() / max(1e-6, min(pymupdf.Rect(t.bbox).get_area(), pymupdf.Rect(*ocr_box).get_area()))
        if ov > 0.5 and (best is None or ov > best[0]):
            best = (ov, t)
    if best is None:
        return None
    t = best[1]
    if len(t.rows) < 2 or t.col_count < 2:
        return None
    rotated = text_dir(page, t.bbox) == 'up'
    words = page_words(page)
    cells = [list(row.cells) for row in t.rows]
    ncol = max(len(r) for r in cells)
    cells = [r + [None] * (ncol - len(r)) for r in cells]
    # centre of each column (narrowest cell in it) and of each row (shortest cell in it)
    origin = [c for r in cells for c in r if c]
    # column and row boundaries: a cell at index k starts at boundary k
    xb = [next((r[k][0] for r in cells if r[k]), None) for k in range(ncol)] + [t.bbox[2]]
    yb = [next((c[1] for c in r if c), None) for r in cells] + [t.bbox[3]]
    for k in range(ncol - 1, -1, -1):
        if xb[k] is None:
            xb[k] = xb[k + 1]
    for i in range(len(cells) - 1, -1, -1):
        if yb[i] is None:
            yb[i] = yb[i + 1]
    col_c = [(xb[k] + xb[k + 1]) / 2 for k in range(ncol)]
    row_c = [(yb[i] + yb[i + 1]) / 2 for i in range(len(cells))]
    # each grid position holds (text, id of the PDF cell it comes from); spanned positions repeat the id
    grid = []
    for i, r in enumerate(cells):
        row = []
        for k, c in enumerate(r):
            if c is None and col_c[k] is not None:
                c = min((o for o in origin if o[0] < col_c[k] < o[2] and o[1] < row_c[i] < o[3]),
                        key=lambda o: (o[2] - o[0]) * (o[3] - o[1]), default=None)
            row.append((words_in(words, c, rotated), origin.index(c)) if c else ('', -1))
        grid.append(row)
    if rotated:  # rows of the page grid are columns of the table
        grid = [list(reversed(col)) for col in zip(*grid)]

    # unruled tables: a row whose cells hold stacked lists of numbers is split line by line
    def lines_of(cid):
        if cid < 0:
            return []
        x0, y0, x1, y1 = origin[cid]
        ws = [w for w in words if x0 - 1 <= (w[0] + w[2]) / 2 <= x1 + 1 and y0 - 1 <= (w[1] + w[3]) / 2 <= y1 + 1]
        if rotated:
            ws = [(-w[3], w[0], -w[1], w[2], w[4]) for w in ws]
        return [((l[0][1] + l[0][3]) / 2, ' '.join(w[4] for w in l)) for l in sort_lines(ws)]

    def numeric_line(txt):
        return bool(re.search(r'\d', txt)) and not re.search(r'[A-Za-z]{2,}', txt)
    split_grid = []
    for r in grid:
        cids = list(dict.fromkeys(cid for _, cid in r))
        stacked = sum(1 for cid in cids if sum(numeric_line(t) for _, t in lines_of(cid)) >= 3)
        if stacked < 2:
            split_grid.append(r)
            continue
        cents = sorted(c for cid in cids for c, _ in lines_of(cid))
        clusters = []
        for c in cents:
            if clusters and c - clusters[-1][-1] <= 3:
                clusters[-1].append(c)
            else:
                clusters.append([c])
        for k, cl in enumerate(clusters):
            lo, hi = cl[0] - 0.5, cl[-1] + 0.5
            split_grid.append([(' '.join(t for c, t in lines_of(cid) if lo <= c <= hi), 100000 + cid * 1000 + k if cid >= 0 else -1)
                               for _, cid in r])
    grid = split_grid
    # drop rows and columns that are completely empty
    grid = [r for r in grid if any(x[0].strip() for x in r)]
    keep = [k for k in range(len(grid[0])) if any(r[k][0].strip() for r in grid)] if grid else []
    grid = [[r[k] for k in keep] for r in grid]
    # header split over several rows: merge into one row (id -2). The header is the shaded band at the
    # top of the table; without shading, at most the first 4 rows before the first all-number row.
    def is_data(r):
        vals = [x[0] for x in r if x[0].strip()]
        return vals and sum(bool(re.fullmatch(r'[-+]?[\d.,]+\s*(E[+-]\d+)?\*?', x.strip())) for x in vals) >= len(vals) / 2
    first = None
    if not rotated:
        tb = pymupdf.Rect(t.bbox)
        fills = [d['rect'] for d in page.get_drawings() if d.get('fill') and d['fill'] != (1.0, 1.0, 1.0)
                 and tb.contains(pymupdf.Point((d['rect'].x0 + d['rect'].x1) / 2, (d['rect'].y0 + d['rect'].y1) / 2)) and d['rect'].y0 <= tb.y0 + 3]
        if fills:
            hb = max(f.y1 for f in fills)
            def row_pos(r):
                tops = [origin[cid][1] for _, cid in r if 0 <= cid < 100000]
                return max(tops) if tops else 1e9
            first = 0
            while first < len(grid) and row_pos(grid[first]) < hb - 0.5:
                first += 1
    if first is None:
        first = next((i for i, r in enumerate(grid) if is_data(r)), None)
        if first is not None and first > 4:
            first = None
    if first and first >= 2:
        head = []
        for k in range(len(grid[0])):
            parts = []
            for r in grid[:first]:
                if r[k][0].strip() and r[k][0] not in parts:
                    parts.append(r[k][0])
            head.append((' '.join(parts), -2))
        grid = [head] + grid[first:]
    # merge a column into its left neighbour where, in every body row, it is the same PDF cell (a span)
    # or one side is empty (a thin sliver column made by a stray line); header texts are joined
    k = 1
    while grid and k < len(grid[0]):
        body = [(r[k - 1], r[k]) for r in grid if r[k][1] != -2]
        if body and all(x[1] == y[1] or not x[0] or not y[0] for x, y in body) and any(x[1] == y[1] and x[0] for x, y in body):
            new = []
            for r in grid:
                x, y = r[k - 1], r[k]
                if x[1] == -2:
                    m = (x[0] if y[0] in x[0] else y[0] if x[0] in y[0] else x[0] + ' ' + y[0], -2)
                else:
                    m = x if x[0] else y
                new.append(r[:k - 1] + [m] + r[k + 1:])
            grid = new
        else:
            k += 1
    texts = [[x[0] for x in r] for r in grid]
    ids = [[x[1] for x in r] for r in grid]
    # numeric words inside the table but in no cell
    inside = lambda w, c: c[0] - 1 <= (w[0] + w[2]) / 2 <= c[2] + 1 and c[1] - 1 <= (w[1] + w[3]) / 2 <= c[3] + 1
    # numeric words inside the table frame but in no cell are flagged; text inside the OCR box but
    # outside the table frame (notes under the table) is kept as a note row
    lost = [w[4] for w in words if inside(w, t.bbox) and numbers(w[4]) and not any(inside(w, c) for c in origin)]
    outside = [w for w in words if inside(w, ocr_box) and not inside(w, t.bbox)]
    notes = ' '.join(' '.join(w[4] for w in line) for line in sort_lines(outside))
    if notes and texts:
        texts.append(['Notes: ' + notes] + [''] * (len(texts[0]) - 1))
        ids.append([-3] * len(texts[0]))
    return texts, tuple(t.bbox), lost, ids


# ---------- main ----------
def table_key(n):
    a, b = n.split('-')
    return (int(re.sub(r'\D', '', a)), a, int(re.sub(r'\D', '', b)), b)


def compare(prim_seq, sec_full):
    """prim_seq: [(value, row, col)], sec_seq: [value]. Returns agreeing count and the disagreements
    [(primary value, row, col, second value)], ignoring values that only changed place."""
    pv = [v for v, _, _ in prim_seq]
    sec_seq = [v for v, _ in sec_full]
    cp, cs = Counter(pv), Counter(sec_seq)
    only_p, only_s = cp - cs, cs - cp
    agree = sum((cp & cs).values())
    out = []
    sm = difflib.SequenceMatcher(None, pv, sec_seq, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        for idx in range(max(i2 - i1, j2 - j1)):
            a = pv[i1 + idx] if idx < i2 - i1 else ''
            b = sec_seq[j1 + idx] if idx < j2 - j1 else ''
            if a and only_p[a] <= 0:
                a = ''
            if b and only_s[b] <= 0:
                b = ''
            if not a and not b:
                continue
            if a:
                only_p[a] -= 1
            if b:
                only_s[b] -= 1
            if a and b and same_value(a, b):
                continue
            r, c = (prim_seq[i1 + idx][1] + 1, prim_seq[i1 + idx][2] + 1) if a else ('', '')
            out.append((a, r, c, b, sec_full[j1 + idx][1] if b else ''))
    # anything left unmatched (alignment can miss a few)
    return agree, out


def seq_of(grid, origins=None):
    return [(v, ri, ci) for ri, r in enumerate(grid) for ci, cell in enumerate(r)
            if (origins is None and not (ci > 0 and r[ci - 1] == cell and cell)) or (origins is not None and (ri, ci) in origins)
            for v in numbers(cell)]


def main():
    import pymupdf
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--pdf-root', required=True)
    ap.add_argument('--manual', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    db = sqlite3.connect(a.db)
    os.makedirs(a.out, exist_ok=True)
    for f in os.listdir(a.out):
        if f.startswith('table_') and f.endswith('.csv'):
            os.remove(os.path.join(a.out, f))

    def load(name):
        path = os.path.join(a.manual, name)
        return list(csv.DictReader(open(path, encoding='utf-8'))) if os.path.exists(path) else []
    corrections = load('table_corrections.csv')
    verdicts = {(v['number'], v['page'], v['primary'], v['second']): v for v in load('table_check_verdicts.csv')}
    used_corr, used_verd = set(), set()
    docs = {}

    def doc(b):
        if b not in docs:
            docs[b] = pymupdf.open(os.path.join(a.pdf_root, f'batch {b}.pdf'))
        return docs[b]

    index_rows, check_rows, cells_rows = [], [], []
    spec = sorted(csv.DictReader(open(os.path.join(a.manual, 'table_pages.csv'), encoding='utf-8')),
                  key=lambda r: table_key(r['number']))
    tmpdir = tempfile.mkdtemp()
    for t in spec:
        num, title = t['number'], t['title']
        out_rows, pages, methods, latex_rows = [], [], [], []
        n_num = n_agree = n_fixed = rows_num = rows_ok = 0
        unmatched_rows = []
        first_checks = len(check_rows)
        if not t['blocks'].strip():  # typed in by hand
            rows = list(csv.reader(open(os.path.join(a.manual, 'tables', f'table_{num}.csv'), encoding='utf-8')))
            src = t.get('source_pages', '') or 'typed'
            out_rows = [['page'] + rows[0]] + [[src] + r for r in rows[1:]]
            methods.append('typed from PDF text layer')
            n_num = sum(len(numbers(c)) for r in rows[1:] for c in r)
        for item in t['blocks'].split():
            m = re.fullmatch(r'(\d+)/(\d+)(?:#(\d+))?(?:@(pdf|ocr))?', item)
            b, p, k, force = int(m.group(1)), int(m.group(2)), int(m.group(3) or 0), m.group(4)
            pg = f'{b}/{p}'
            pages.append(pg)
            page = doc(b)[p - 1]
            blocks = db.execute("SELECT content, x1, y1, x2, y2 FROM blocks WHERE batch=? AND page=? AND label='table' ORDER BY y1",
                                (b, p)).fetchall()
            for content, x1, y1, x2, y2 in (blocks if k == 0 else [blocks[k - 1]]):
                box = (x1 * SCALE, y1 * SCALE, x2 * SCALE, y2 * SCALE)
                origins = set()
                ocr = html_to_grid(content, origins)
                ocr_origins = set(origins)
                ocr_seq = seq_of(ocr, origins)
                has_text = page_has_text(doc(b), p, box) >= max(3, 0.25 * len(ocr_seq))
                pg_grid = pdf_grid(page, box) if has_text and force != 'ocr' else None
                if pg_grid and force != 'ocr':
                    source, grid, lost, ids = 'PDF grid', pg_grid[0], pg_grid[2], pg_grid[3]
                    seen, origins = set(), set()
                    for ri, r in enumerate(ids):
                        for ci, cid in enumerate(r):
                            if cid >= 0 and cid not in seen:
                                seen.add(cid)
                                origins.add((ri, ci))
                    second, sec_name = [(v, ocr[r][c]) for v, r, c in ocr_seq], 'OCR'
                else:
                    source, grid, lost = 'OCR', ocr, []
                    if has_text:
                        sec_name = 'PDF text'
                        second = [(v, ' '.join(x[4] for x in line)) for line in pdf_words(doc(b), p, box) for w in line for v in numbers(w[4])]
                    else:
                        sec_name = 'Tesseract'
                        second = [(v, ' '.join(x[4] for x in line)) for line in tesseract_words(doc(b), p, box, tmpdir) for w in line for v in numbers(w[4])]
                for c in corrections:
                    if c['number'] == num and c['page'] == pg:
                        r_, c_ = int(c['row']) - 1, int(c['col']) - 1
                        if r_ < len(grid) and c_ < len(grid[r_]) and grid[r_][c_] == c['wrong']:
                            grid[r_][c_] = c['correct']
                            used_corr.add(id(c))
                            n_fixed += 1
                methods.append(f'{pg}: {source} checked against {sec_name}')
                prim_seq = seq_of(grid, origins)
                n_num += len(prim_seq)
                agree, diffs = compare(prim_seq, second)
                n_agree += agree
                for w in lost:
                    diffs.append(('', '', '', 'PDF word outside grid: ' + w, ''))
                for pv, r, c, sv, sctx in diffs:
                    v = verdicts.get((num, pg, pv, sv))
                    if v:
                        used_verd.add((num, pg, pv, sv))
                        verdict, note = v['verdict'], v['note']
                    elif source == 'PDF grid' and not sv.startswith('PDF word'):
                        verdict = 'ok (PDF exact)'
                        note = ('OCR missed this value' if not sv else 'OCR misread it as ' + sv if pv else
                                'OCR reading only (no such number in the PDF table cells)')
                    else:
                        verdict, note = 'TO CHECK', ''
                    check_rows.append([num, pg, source, sec_name, r, c, grid[r - 1][c - 1] if r else '', pv, sv, sctx[:120], verdict, note])
                if source == 'PDF grid':
                    def row_tuples(g, og):
                        return [tuple(v for ci, cell in enumerate(r) if (ri, ci) in og for v in numbers(cell)) for ri, r in enumerate(g)]
                    ocr_rows = Counter(row_tuples(ocr, ocr_origins))
                    for ri, tup in enumerate(row_tuples(grid, origins)):
                        if tup:
                            rows_num += 1
                            if ocr_rows[tup] > 0:
                                ocr_rows[tup] -= 1
                                rows_ok += 1
                            else:
                                unmatched_rows.append(f'{pg} row {ri + 1}')
                for r in grid:
                    out_rows.append([pg] + r)
                for r in ocr:
                    latex_rows.append([pg] + r)
        width = max(len(r) for r in out_rows)
        out_rows = [r + [''] * (width - len(r)) for r in out_rows]
        fname = f'table_{num}.csv'
        with open(os.path.join(a.out, fname), 'w', newline='', encoding='utf-8') as fh:
            w = csv.writer(fh)
            if out_rows[0][0] != 'page':
                w.writerow(['page'] + [f'col{i}' for i in range(1, width)])
            w.writerows(out_rows)
        if t['kind'] == 'formula' and latex_rows:
            wl = max(len(r) for r in latex_rows)
            with open(os.path.join(a.out, f'table_{num}_ocr_latex.csv'), 'w', newline='', encoding='utf-8') as fh:
                w = csv.writer(fh)
                w.writerow(['page'] + [f'col{i}' for i in range(1, wl)])
                w.writerows(r + [''] * (wl - len(r)) for r in latex_rows)
        for ri, r in enumerate(out_rows, 1):
            for ci, v in enumerate(r[1:], 1):
                cells_rows.append((num, ri, ci, r[0], v))
        mine = check_rows[first_checks:]
        open_ = sum(1 for c in mine if c[10] == 'TO CHECK')
        status = (('formula table checked by eye: see note' if t['kind'] == 'formula' else 'typed or read by hand: see note')
                  if not t['blocks'].strip() else
                  'two readings agree' if not mine else
                  'differences resolved' if open_ == 0 else f'{open_} differences to check')
        index_rows.append([num, title, t['kind'], ' '.join(pages) or t.get('source_pages', ''), fname, len(out_rows), n_num, n_agree, len(mine),
                           n_fixed, rows_num, rows_ok, '; '.join(unmatched_rows), '; '.join(methods), status, t['note']])

    header = ['number', 'title', 'kind', 'pages', 'file', 'rows', 'numbers', 'numbers_agreeing', 'differences', 'cells_corrected',
              'rows_with_numbers', 'rows_same_in_ocr', 'rows_to_check', 'how_checked', 'status', 'note']
    with open(os.path.join(a.out, 'tables_index.csv'), 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(index_rows)
    ch = ['number', 'page', 'source', 'second_reading', 'row', 'col', 'cell_text', 'primary', 'second', 'second_context', 'verdict', 'note']
    with open(os.path.join(a.out, 'table_checks.csv'), 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(ch)
        w.writerows(check_rows)

    for name in ('extra_tables', 'guide_tables', 'guide_table_cells', 'table_checks'):
        db.execute(f'DROP TABLE IF EXISTS {name}')
    db.execute('CREATE TABLE guide_tables(' + ', '.join(f'{c} TEXT' for c in header) + ')')
    db.executemany(f'INSERT INTO guide_tables VALUES ({",".join("?" * len(header))})', index_rows)
    db.execute('CREATE TABLE guide_table_cells(number TEXT, row_no INT, col_no INT, page TEXT, value TEXT)')
    db.executemany('INSERT INTO guide_table_cells VALUES (?,?,?,?,?)', cells_rows)
    db.execute('CREATE TABLE table_checks(' + ', '.join(f'"{c}" TEXT' for c in ch) + ')')
    db.executemany(f'INSERT INTO table_checks VALUES ({",".join("?" * len(ch))})', check_rows)
    # keep the figure/table status list (table data_status, from audit_missing.py) in step
    if db.execute("SELECT name FROM sqlite_master WHERE name='data_status'").fetchone():
        for r in index_rows:
            num, kind, status = r[0], r[2], r[-2]
            st = 'checked data table' if kind == 'data' else 'checked formula table'
            note = f'reference/tables/{r[4]}: {status}'
            if db.execute("SELECT 1 FROM data_status WHERE type='table' AND number=?", (num,)).fetchone():
                db.execute("UPDATE data_status SET status=?, priority='', note=? WHERE type='table' AND number=?", (st, note, num))
            else:
                b, p = (r[3].split()[0].split('/') + [None])[:2] if '/' in r[3] else (None, None)
                db.execute("INSERT INTO data_status VALUES ('table',?,?,?,?,?,?,?)", (num, r[1], b, p, st, '', note))
    db.commit()
    shutil.rmtree(tmpdir, ignore_errors=True)
    print('tables:', len(index_rows), '| numbers:', sum(r[6] for r in index_rows), '| agreeing:', sum(r[7] for r in index_rows),
          '| differences:', len(check_rows), '| still to check:', sum(1 for c in check_rows if c[10] == 'TO CHECK'),
          '| corrections applied:', len(used_corr), 'of', len(corrections))
    for c in corrections:
        if id(c) not in used_corr:
            print('correction NOT applied:', dict(c))
    for k in verdicts:
        if k not in used_verd:
            print('verdict not used:', k)


if __name__ == '__main__':
    main()
