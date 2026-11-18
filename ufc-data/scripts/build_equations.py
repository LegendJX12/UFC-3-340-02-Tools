"""Build table `equations`: one checked LaTeX form per numbered equation of UFC 3-340-02.

  latex  = corrected form from reference/manual/equation_corrections.csv where the OCR was wrong,
           missing, paired with the wrong line, or had a minor slip (written from the
           rendered PDF page), otherwise the OCR line, cleaned of layout leftovers
  source = 'corrected from PDF' or 'OCR'
  The original OCR text is kept in column ocr_latex; table `blocks` is not changed.

Needs tables equation_status and equation_lines (scripts/check_equation_lines.py).
Optional --katex: path to a Node script that checks LaTeX with KaTeX (adds column latex_ok).

Usage: python3 scripts/build_equations.py --db reference/ufc_340_02.db \
           --corrections reference/manual/equation_corrections.csv --csv reference/equations/equations.csv [--katex check.js]
"""
import argparse, csv, json, os, re, sqlite3, subprocess, tempfile


def clean_ocr(s):
    s = re.sub(r'\\begin\{array\}\{[^}]*\}', '', s or '')     # array column spec
    s = re.sub(r'\\(begin|end)\{(aligned|array)\}', '', s)
    s = s.replace('&', ' ')
    s = re.sub(r'[\u3000-\u9fff\uff00-\uffef]', '', s)       # stray CJK characters from OCR
    s = re.sub(r'(\\quad|~|\s|")+$', '', s)                   # trailing spacing / quote marks
    s = re.sub(r'\\\\\s*$', '', s)
    return s.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--corrections', required=True)
    ap.add_argument('--csv', required=True)
    ap.add_argument('--katex')
    a = ap.parse_args()
    db = sqlite3.connect(a.db)
    corr = {}
    with open(a.corrections, encoding='utf-8') as fh:
        for r in csv.DictReader(fh):
            corr[r['number']] = r
    ocr = dict((n, l) for n, l in db.execute('SELECT number, ocr_line FROM equation_lines'))
    rows = []
    for num, b, p, verdict in db.execute('SELECT number, batch, page, verdict FROM equation_status '
                                         'ORDER BY batch, page, number'):
        o = ocr.get(num, '') or ''
        if num in corr:
            latex, source, reason = corr[num]['latex'], 'corrected from PDF', corr[num]['reason']
        else:
            latex, source, reason = clean_ocr(o), 'OCR', ''
        rows.append([num, b, p, latex, source, verdict, reason, o])

    ok = [None] * len(rows)
    if a.katex and os.path.exists(a.katex):
        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as fh:
            json.dump([r[3] for r in rows], fh)
            path = fh.name
        res = subprocess.run(['node', a.katex, path], capture_output=True, text=True)
        ok = json.loads(res.stdout)
        os.unlink(path)

    db.execute('DROP TABLE IF EXISTS equations')
    db.execute('CREATE TABLE equations(number TEXT, batch INT, page INT, latex TEXT, source TEXT, '
               'verdict TEXT, reason TEXT, ocr_latex TEXT, latex_ok INT)')
    db.executemany('INSERT INTO equations VALUES (?,?,?,?,?,?,?,?,?)',
                   [r + [ok[i]] for i, r in enumerate(rows)])
    db.commit()
    with open(a.csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['number', 'batch', 'page', 'latex', 'source', 'verdict', 'reason', 'latex_ok'])
        w.writerows([r[:7] + [ok[i]] for i, r in enumerate(rows)])
    n_corr = sum(1 for r in rows if r[4] != 'OCR')
    print(f'equations: {len(rows)} ({n_corr} corrected from PDF, {len(rows) - n_corr} OCR)')
    if ok[0] is not None:
        bad = [rows[i][0] for i, v in enumerate(ok) if not v]
        print('LaTeX check: %d parse, %d fail %s' % (len(rows) - len(bad), len(bad), bad[:20]))


if __name__ == '__main__':
    main()
