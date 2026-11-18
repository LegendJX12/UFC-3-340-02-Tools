"""Line-level check of numbered OCR equations against the PDF text layer.

check_equations.py compares the whole nearest OCR formula block with one PDF line, so a
multi-line block that holds several equations can hide errors ("close"). This script:
  - PDF side: the line ending in the equation number, plus the math lines just above and
    below it (exponents and fraction parts are printed on separate lines in the text layer)
  - OCR side: every formula block on the page split into single lines (\\\\ rows); the line
    whose numbers best match the PDF window is used
  - numbers are normalised: "1 .5" -> 1.5, "47,690" -> 47690 (so an OCR "47.690" shows up)
Status: match | ocr-missing (PDF numbers absent from OCR) | ocr-extra (OCR numbers absent
from PDF) | differ (both). Flagged lines need a look at the rendered page.

With --review, also writes table equation_status / --status CSV: one verdict per equation,
combining this automatic check with the hand-checked review (reference/manual/equation_review.csv):
  error / missed / check operator    - from the review; correct text from the PDF is in the review
  ok (minor slip)                    - OCR usable; small symbol slip noted in the review
  ok (checked by eye)                - flagged automatically, then checked and found correct
  ok (automatic)                     - numbers (and variable names, where present) match the PDF text

Usage: python3 scripts/check_equation_lines.py --db reference/ufc_340_02.db --csv reference/equations/equation_lines.csv \
           --review reference/manual/equation_review.csv --status reference/equations/equation_status.csv
"""
import argparse, collections, csv, difflib, re, sqlite3

NUM = re.compile(r'\d+(?:\.\d+)?')


def nums_pdf(s):
    s = re.sub(r'(\d)\s+\.\s*(\d)', r'\1.\2', s)
    s = re.sub(r'(\d)\.\s+(\d)', r'\1.\2', s)
    s = re.sub(r'(\d),(\d{3})', r'\1\2', s)
    return collections.Counter(NUM.findall(s))


def nums_ocr(s):
    s = re.sub(r'\\(mathrm|text|operatorname|mathbf|boldsymbol)\{([^}]*)\}', r' \2 ', s)
    s = re.sub(r'(\d)\{,\}(\d{3})', r'\1\2', s)
    s = re.sub(r'(\d),(\d{3})(?!\d)', r'\1\2', s)
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)
    return collections.Counter(NUM.findall(s))


def squash_pdf(s):
    return re.sub(r'[^A-Za-z0-9]', '', s)


def squash_ocr(s):
    s = re.sub(r'\\(mathrm|text|operatorname|mathbf|boldsymbol|mathcal|pmb)\{([^}]*)\}', r'\2', s)
    s = re.sub(r'\\(left|right|quad|qquad|cdot|times|leq|geq|le|ge|frac|sqrt|begin|end|aligned|array)', '', s)
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    return re.sub(r'[^A-Za-z0-9]', '', s)


def is_prose(line):
    words = re.findall(r'[A-Za-z]{4,}', line)
    return len(words) >= 3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--csv', required=True)
    ap.add_argument('--review')
    ap.add_argument('--status')
    a = ap.parse_args()
    db = sqlite3.connect(a.db)
    db.execute('DROP TABLE IF EXISTS equation_lines')
    db.execute('CREATE TABLE equation_lines(number TEXT, batch INT, page INT, status TEXT, '
               'pdf_window TEXT, ocr_line TEXT, missing_in_ocr TEXT, extra_in_ocr TEXT)')
    rows = []
    for num, b, p in db.execute("SELECT number, batch, page FROM equation_check").fetchall():
        text = db.execute('SELECT text FROM pdf_pages WHERE batch=? AND page=?', (b, p)).fetchone()[0]
        lines = text.split('\n')
        end_re = re.compile(r'\s{3,}' + re.escape(num) + r'\s*$')
        idx = [i for i, l in enumerate(lines) if end_re.search(l)]
        if not idx:
            continue  # equation drawn as an image: checked by eye (equation_review)
        i = idx[0]
        eqno = re.compile(r'\s{3,}\d+[A-Z]?-\d+[a-z]?\s*$')
        window = [re.sub(end_re, '', lines[i])]
        for j in range(i - 1, max(-1, i - 4), -1):  # lines above
            l = lines[j]
            if not l.strip() or is_prose(l) or eqno.search(l):
                break
            window.insert(0, l)
        for j in range(i + 1, min(len(lines), i + 3)):  # lines below
            l = lines[j]
            if not l.strip() or is_prose(l) or eqno.search(l) or re.match(r'\s*where', l):
                break
            window.append(l)
        pn = nums_pdf(' '.join(window))
        ps = squash_pdf(' '.join(window))
        nb = db.execute("SELECT y1, y2 FROM blocks WHERE batch=? AND page=? AND label='formula_number' "
                        "AND trim(content)=?", (b, p, num)).fetchone()
        best = None
        for content, fy1, fy2 in db.execute("SELECT content, y1, y2 FROM blocks WHERE batch=? AND page=? "
                                            "AND label='formula'", (b, p)):
            if nb and fy1 is not None and (fy2 < nb[0] - 250 or fy1 > nb[1] + 250):
                continue  # only formula blocks near the equation number
            for row in re.split(r'\\\\', content):
                on = nums_ocr(row)
                text_sim = difflib.SequenceMatcher(None, squash_ocr(row), ps).ratio() if ps else 0.0
                inter = sum((on & pn).values())
                union = sum((on | pn).values())
                num_sim = inter / union if union else 1.0
                score = 0.5 * text_sim + 0.5 * num_sim
                if best is None or score > best[0]:
                    best = (score, row.strip(), on)
        if best is None:
            status, ocr_line, on = 'no-ocr-line', '', collections.Counter()
        else:
            _, ocr_line, on = best
            miss, extra = pn - on, on - pn
            status = ('match' if pn else 'match (no numbers)') if not miss and not extra else (
                'ocr-missing' if miss and not extra else ('ocr-extra' if extra and not miss else 'differ'))
        miss, extra = pn - on, on - pn
        r = (num, b, p, status, ' | '.join(re.sub(r'\s{3,}', '   ', w.strip()) for w in window),
             ocr_line, ' '.join(sorted(miss.elements())), ' '.join(sorted(extra.elements())))
        rows.append(r)
        db.execute('INSERT INTO equation_lines VALUES (?,?,?,?,?,?,?,?)', r)
    db.commit()
    with open(a.csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['number', 'batch', 'page', 'status', 'pdf_window', 'ocr_line', 'missing_in_ocr', 'extra_in_ocr'])
        w.writerows(rows)
    if a.review:
        review = {}
        with open(a.review, encoding='utf-8') as fh:
            for r in csv.DictReader(fh):
                review[r['equation']] = r
        verdict_of = {'OCR ERROR': 'error', 'OCR ERROR + CHECK: operator': 'error', 'OCR MISSED': 'missed',
                      'CHECK: operator': 'check operator', 'minor (OCR usable)': 'ok (minor slip)',
                      'pairing (OCR correct)': 'ok (checked by eye)', 'PDF text split (OCR correct)': 'ok (checked by eye)'}
        status = {}
        for num, b, p in db.execute('SELECT number, batch, page FROM equation_check'):
            status[num] = [num, b, p, None, '']
        line_status = dict((r[0], r[3]) for r in rows)
        for num in list(status):
            ls = line_status.get(num, 'no-pdf-line')
            status[num][3] = 'ok (automatic)' if ls.startswith('match') else 'ok (checked by eye)'
        for num, r in review.items():
            if num not in status:
                status[num] = [num, int(r['batch']), int(r['page']), None, '']
            status[num][3] = verdict_of.get(r['finding'], r['finding'])
            status[num][4] = r['correct_text_from_pdf'] if status[num][3] in ('error', 'missed', 'check operator') else ''
        db.execute('DROP TABLE IF EXISTS equation_status')
        db.execute('CREATE TABLE equation_status(number TEXT, batch INT, page INT, verdict TEXT, correct_text_from_pdf TEXT)')
        out = sorted(status.values(), key=lambda r: (r[1], r[2], r[0]))
        db.executemany('INSERT INTO equation_status VALUES (?,?,?,?,?)', out)
        db.commit()
        if a.status:
            with open(a.status, 'w', newline='', encoding='utf-8') as fh:
                w = csv.writer(fh)
                w.writerow(['number', 'batch', 'page', 'verdict', 'correct_text_from_pdf'])
                w.writerows(out)
        print('equation status:', dict(collections.Counter(r[3] for r in out)))
    print('equations checked line by line:', len(rows))
    for k, v in collections.Counter(r[3] for r in rows).most_common():
        print(f'  {k:12s} {v}')


if __name__ == '__main__':
    main()
