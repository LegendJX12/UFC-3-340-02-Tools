"""Check OCR equations against the exact text layer of the source PDFs.

For each numbered equation found by OCR (block 'formula_number', e.g. "4-1"):
  - OCR equation: the nearest 'formula' block on the same page (LaTeX, from OCR)
  - PDF equation: the PDF text line(s) on the same page that end with the same number
  - compare the numbers that appear in both (constants, exponents, subscripts)
Greek letters and some symbols are small images in the PDF, so they are missing from
the PDF text; only numbers and plain variable names can be compared.

Status:
  match       - same numbers in both
  close       - numbers of one are all contained in the other (e.g. equation split over lines)
  differ      - numbers differ; check against the PDF
  no-pdf-line - equation number not found as a line ending in the PDF text
  no-formula  - OCR found the number but no formula block near it

Usage:
  python3 scripts/check_equations.py --db reference/ufc_340_02.db --csv reference/equation_check.csv
"""
import argparse, collections, csv, re, sqlite3

NUM_RE = re.compile(r'\d+(?:\.\d+)?')


def numbers_latex(s):
    s = re.sub(r'\\(mathrm|text|operatorname)\{[^}]*\}', ' ', s)
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)  # drop commands such as \frac, \sqrt, \alpha
    return collections.Counter(NUM_RE.findall(s))


def numbers_pdf(s, eq_no):
    s = re.sub(r'\s' + re.escape(eq_no) + r'\s*$', ' ', s)
    return collections.Counter(NUM_RE.findall(s))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--csv', required=True)
    a = ap.parse_args()
    db = sqlite3.connect(a.db)
    db.execute('DROP TABLE IF EXISTS equation_check')
    db.execute('''CREATE TABLE equation_check(number TEXT, batch INT, page INT, ocr_latex TEXT,
                  pdf_text TEXT, status TEXT, ocr_numbers TEXT, pdf_numbers TEXT)''')
    rows = []
    numbered = db.execute("SELECT batch, page, content, y1, y2 FROM blocks WHERE label='formula_number'").fetchall()
    for b, p, num, y1, y2 in numbered:
        num = (num or '').strip()
        if not re.fullmatch(r'\d+[A-Z]?-\d+[a-z]?', num):
            continue
        cy = (y1 + y2) / 2 if y1 is not None else None
        forms = db.execute("SELECT content, y1, y2 FROM blocks WHERE batch=? AND page=? AND label='formula'", (b, p)).fetchall()
        latex = ''
        if forms and cy is not None:
            latex = min(forms, key=lambda f: abs((f[1] + f[2]) / 2 - cy))[0]
        pdf = db.execute('SELECT text FROM pdf_pages WHERE batch=? AND page=?', (b, p)).fetchone()
        pdf_lines = [ln.strip() for ln in (pdf[0] if pdf else '').split('\n')
                     if re.search(r'\s{3,}' + re.escape(num) + r'\s*$', ln) and ln.strip() != num]
        pdf_text = ' | '.join(pdf_lines)
        on = numbers_latex(latex)
        pn = numbers_pdf(' '.join(pdf_lines), num)
        if not latex:
            status = 'no-formula'
        elif not pdf_lines:
            status = 'no-pdf-line'
        elif on == pn:
            status = 'match'
        elif not (on - pn) or not (pn - on):
            status = 'close'
        else:
            status = 'differ'
        r = (num, b, p, latex, pdf_text, status,
             ' '.join(sorted(on.elements())), ' '.join(sorted(pn.elements())))
        rows.append(r)
        db.execute('INSERT INTO equation_check VALUES (?,?,?,?,?,?,?,?)', r)
    db.commit()
    with open(a.csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['number', 'batch', 'page', 'ocr_latex', 'pdf_text', 'status', 'ocr_numbers', 'pdf_numbers'])
        w.writerows(rows)
    c = collections.Counter(r[5] for r in rows)
    print('numbered equations:', len(rows))
    for k in ['match', 'close', 'differ', 'no-pdf-line', 'no-formula']:
        print(f'{k:12s}', c.get(k, 0))


if __name__ == '__main__':
    main()
