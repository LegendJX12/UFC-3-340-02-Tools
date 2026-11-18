"""Fix OCR formulas of UFC 3-340-02: thousands separators, letters and primes.

The OCR often read a thousands comma as a decimal point (87,000 -> 87.000, 4,409,934 ->
4.409.934). A number a.bbb (or a.bbb.ccc) is changed to a,bbb (a,bbb,ccc) only when the
PDF text of the same page contains the comma form and does not contain the dotted form.

Letters and primes (each OCR formula line is matched to its PDF text line on the same page):
  - a letter is changed only for a known OCR confusion (v->y, F->E, I->l, j->i, O->o, o->p,
    t->f, J->l, r->f, D->p, q->g, v<->V, C->c, f->l), only when the corrected name is in the
    matching PDF line and the OCR name does not occur anywhere in the PDF text of that page
  - the corrected name must be on the matching PDF line itself (or the line must match well)
  - a prime is added only to a name with a subscript (e.g. f'dc), when the matching PDF line
    shows that name with a prime and the nearby PDF lines never show it without
  - --manual: a CSV of fixes checked by eye (batch, page, block_id, old, new) applied last
Lines still in doubt are listed in --review.

Output:
  table `formulas`       every OCR formula block with the fixed LaTeX (column latex) and the
                         original (ocr_latex); table `blocks` is not changed
  --csv                  one row per fix, with the PDF line that shows the comma form
Usage: python3 scripts/fix_formulas.py --db reference/ufc_340_02.db --csv reference/formula_fixes.csv
"""
import argparse, collections, csv, difflib, os, re, sqlite3, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from latex_names import names, replace_letter, add_prime  # noqa: E402
from check_equation_lines import nums_ocr, nums_pdf, squash_ocr, squash_pdf, is_prose  # noqa: E402

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


SWAPS = {('v', 'y'), ('F', 'E'), ('I', 'l'), ('j', 'i'), ('O', 'o'), ('o', 'p'), ('t', 'f'), ('J', 'l'),
         ('r', 'f'), ('D', 'p'), ('q', 'g'), ('v', 'V'), ('V', 'v'), ('C', 'c'), ('f', 'l')}


def pdf_line_for(row, lines):
    """Index of the PDF line that best matches an OCR formula line (text + numbers), and its score."""
    on, so = nums_ocr(row), squash_ocr(row).lower()
    best = (0.0, None)
    for i, l in enumerate(lines):
        sp = squash_pdf(l).lower()
        if not sp:
            continue
        pn = nums_pdf(l)
        u = sum((on | pn).values())
        sc = 0.6 * difflib.SequenceMatcher(None, so, sp).ratio() + 0.4 * (sum((on & pn).values()) / u if u else 1.0)
        if sc > best[0]:
            best = (sc, i)
    return best


def window(lines, i):
    w = [lines[i]]
    for j in range(i - 1, max(-1, i - 3), -1):
        if not lines[j].strip() or is_prose(lines[j]):
            break
        w.insert(0, lines[j])
    for j in range(i + 1, min(len(lines), i + 3)):
        if not lines[j].strip() or is_prose(lines[j]):
            break
        w.append(lines[j])
    return ' '.join(w)


def pdf_names(text):
    t = re.sub(r"\s*['’′]\s*", "'", text)
    plain = set(re.findall(r'[A-Za-z]+', t.replace("'", '')))
    primed = set(a + b for a, b in re.findall(r"([A-Za-z])'([A-Za-z]{0,3})", t))
    unprimed = collections.Counter()
    for m in re.finditer(r"(?<![A-Za-z'])([A-Za-z])([A-Za-z]{0,3})(?!')", t):
        unprimed[m.group(1) + m.group(2)] += 1
    return plain, primed, unprimed


def fix_letters_primes(latex, lines, page_names):
    """Fix one block. Returns (latex, fixes, doubts)."""
    fixes, doubts = [], []
    out = latex
    # work row by row (rows of aligned/array blocks are separated by \\)
    starts = [0] + [m.end() for m in re.finditer(r'\\\\', latex)]
    for a in reversed(starts):                       # right to left keeps earlier positions valid
        b = out.find('\\\\', a)
        b = len(out) if b < 0 else b
        row = out[a:b]
        if len(squash_ocr(row)) < 3:
            continue
        score, li = pdf_line_for(row, lines)
        if li is None or score < 0.3:
            doubts.append(('no PDF line', row))
            continue
        win = window(lines, li)
        plain, primed, unprimed = pdf_names(win)
        line_plain, line_primed, _ = pdf_names(lines[li])
        strong = score >= 0.55
        new_row = row
        for nm in sorted(names(row), key=lambda n: -n['pos'][0]):
            o = nm['name']
            if len(o) >= 2 and o not in plain and o not in page_names:
                cands = []
                for q in plain:
                    if len(q) == len(o):
                        d = [(k, x, y) for k, (x, y) in enumerate(zip(o, q)) if x != y]
                        if len(d) == 1 and (d[0][1], d[0][2]) in SWAPS:
                            cands.append((q, d[0]))
                if len(cands) == 1 and (cands[0][0] in line_plain or strong):
                    q, (k, x, y) = cands[0]
                    new_row = replace_letter(new_row, nm['pos'][k], y)
                    fixes.append(('letter', o, q))
                    o = q
                elif cands or any(len(q) == len(o) and sum(x != y for x, y in zip(o, q)) == 1 for q in plain if len(q) >= 2):
                    doubts.append(('name ' + o, row))
            if (not nm['primed'] and len(o) >= 2 and o in line_primed and o in primed
                    and unprimed.get(o, 0) == 0):
                new_row = add_prime(new_row, {'pos': [nm['pos'][0]]})
                fixes.append(('prime', o, o + "'"))
        out = out[:a] + new_row + out[b:]
    return out, fixes, doubts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--csv', required=True)
    ap.add_argument('--review', help='CSV of formula lines still in doubt')
    ap.add_argument('--manual', help='CSV of fixes checked by eye: batch,page,block_id,old,new,note')
    a = ap.parse_args()
    manual = collections.defaultdict(list)
    if a.manual and os.path.exists(a.manual):
        with open(a.manual, encoding='utf-8') as fh:
            for r in csv.DictReader(fh):
                manual[(int(r['batch']), int(r['page']), int(r['block_id']))].append(r)
    db = sqlite3.connect(a.db)
    pdf = dict(((b, p), t) for b, p, t in db.execute('SELECT batch, page, text FROM pdf_pages'))
    rows, log, review, unmatched = [], [], [], []
    eq_lines = set(l for (l,) in db.execute('SELECT ocr_line FROM equation_lines') if l)
    page_names = {}
    for (b, p), t in pdf.items():
        page_names[(b, p)] = set(re.findall(r'[A-Za-z]+', re.sub(r"\s*['\u2019]\s*", '', t)))
    for b, p, bid, content in db.execute("SELECT batch, page, block_id, content FROM blocks "
                                         "WHERE label='formula' ORDER BY batch, page, block_id").fetchall():
        t = pdf.get((b, p), '')
        fixed, fixes = fix_thousands(content or '', t)
        for old_, new_ in fixes:
            line = next((l.strip() for l in t.split('\n') if new_ in l), '')
            log.append((b, p, bid, 'thousands', old_, new_, re.sub(r'\s{3,}', '   ', line)[:160]))
        n_fix = len(fixes)
        # numbered equations are corrected separately (table equations); skip their rows here
        if not any(r.strip() in eq_lines for r in re.split(r'\\\\', content or '')):
            fixed, lf, doubts = fix_letters_primes(fixed, t.split('\n'), page_names.get((b, p), set()))
            for kind, old_, new_ in lf:
                log.append((b, p, bid, kind, old_, new_, ''))
            n_fix += len(lf)
            for why, row in doubts:
                review.append((b, p, bid, why, row[:300]))
        for r in manual.get((b, p, bid), []):
            if r['old'] in fixed:
                n = fixed.count(r['old']) if r.get('all') == 'yes' else 1
                fixed = fixed.replace(r['old'], r['new'], n)
                for _ in range(n):
                    log.append((b, p, bid, 'checked by eye', r['old'], r['new'], r.get('note', '')))
                n_fix += n
            else:
                unmatched.append((b, p, bid, r['old']))
        rows.append((b, p, bid, fixed, content, n_fix))
    db.execute('DROP TABLE IF EXISTS formulas')
    db.execute('CREATE TABLE formulas(batch INT, page INT, block_id INT, latex TEXT, ocr_latex TEXT, '
               'fixes INT, PRIMARY KEY(batch, page, block_id))')
    db.executemany('INSERT INTO formulas VALUES (?,?,?,?,?,?)', rows)
    db.commit()
    with open(a.csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['batch', 'page', 'block_id', 'type', 'ocr', 'fixed', 'evidence'])
        w.writerows(log)
    if a.review:
        with open(a.review, 'w', newline='', encoding='utf-8') as fh:
            w = csv.writer(fh)
            w.writerow(['batch', 'page', 'block_id', 'why', 'ocr_line'])
            w.writerows(review)
    for u in unmatched:
        print('manual fix not applied (text not found):', u)
    print(f'formula blocks: {len(rows)}; fixes: {dict(collections.Counter(l[3] for l in log))} '
          f'in {sum(1 for r in rows if r[5])} blocks; lines in doubt: {len(review)}')


if __name__ == '__main__':
    main()
