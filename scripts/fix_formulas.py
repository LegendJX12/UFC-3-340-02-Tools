"""Fix thousands separators in OCR formulas of UFC 3-340-02.

The OCR often read a thousands comma as a decimal point (87,000 -> 87.000, 4,409,934 ->
4.409.934). A number a.bbb (or a.bbb.ccc) is changed to a,bbb (a,bbb,ccc) only when the
PDF text of the same page contains the comma form and does not contain the dotted form.

Output:
  table `formulas`       every OCR formula block with the fixed LaTeX (column latex) and the
                         original (ocr_latex); table `blocks` is not changed
  --csv                  one row per fix, with the PDF line that shows the comma form
Usage: python3 scripts/fix_formulas.py --db reference/ufc_340_02.db --csv reference/formula_fixes.csv
"""
import argparse, csv, re, sqlite3

GROUPED = re.compile(r'(?<![\d.])(\d{1,3})((?:\.\d{3})+)(?!\d)')


def fix_thousands(latex, pdf_text):
    """Return (fixed latex, list of (old, new))."""
    fixes = []

    def repl(m):
        dotted = m.group(0)
        comma = m.group(1) + m.group(2).replace('.', ',')
        if comma in pdf_text and dotted not in pdf_text:
            fixes.append((dotted, comma))
            return comma.replace(',', '{,}')
        return dotted
    return GROUPED.sub(repl, latex), fixes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--csv', required=True)
    a = ap.parse_args()
    db = sqlite3.connect(a.db)
    pdf = dict(((b, p), t) for b, p, t in db.execute('SELECT batch, page, text FROM pdf_pages'))
    rows, log = [], []
    for b, p, bid, content in db.execute("SELECT batch, page, block_id, content FROM blocks "
                                         "WHERE label='formula' ORDER BY batch, page, block_id"):
        t = pdf.get((b, p), '')
        fixed, fixes = fix_thousands(content or '', t)
        rows.append((b, p, bid, fixed, content, len(fixes)))
        for old, new in fixes:
            line = next((l.strip() for l in t.split('\n') if new in l), '')
            log.append((b, p, bid, old, new, re.sub(r'\s{3,}', '   ', line)[:160]))
    db.execute('DROP TABLE IF EXISTS formulas')
    db.execute('CREATE TABLE formulas(batch INT, page INT, block_id INT, latex TEXT, ocr_latex TEXT, '
               'thousands_fixes INT, PRIMARY KEY(batch, page, block_id))')
    db.executemany('INSERT INTO formulas VALUES (?,?,?,?,?,?)', rows)
    db.commit()
    with open(a.csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['batch', 'page', 'block_id', 'ocr', 'fixed', 'pdf_line'])
        w.writerows(log)
    print(f'formula blocks: {len(rows)}; numbers fixed: {len(log)} in {sum(1 for r in rows if r[5])} blocks')


if __name__ == '__main__':
    main()
