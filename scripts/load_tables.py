"""Load hand-entered tables (reference/tables/*.csv) into the database.

Tables listed in reference/tables/tables_index.csv go into table `extra_tables`,
one row per table row, with the row as JSON (column name -> value).

Usage: python3 scripts/load_tables.py --db reference/ufc_340_02.db --tables reference/tables
"""
import argparse, csv, json, os, sqlite3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--tables', required=True)
    a = ap.parse_args()
    db = sqlite3.connect(a.db)
    db.execute('DROP TABLE IF EXISTS extra_tables')
    db.execute('''CREATE TABLE extra_tables(number TEXT, title TEXT, batch INT, page INT, guide_page TEXT,
                  source TEXT, file TEXT, row_no INT, data TEXT)''')
    n = 0
    for t in csv.DictReader(open(os.path.join(a.tables, 'tables_index.csv'), encoding='utf-8')):
        for i, row in enumerate(csv.DictReader(open(os.path.join(a.tables, t['file']), encoding='utf-8')), 1):
            db.execute('INSERT INTO extra_tables VALUES (?,?,?,?,?,?,?,?,?)',
                       (t['number'], t['title'], int(t['batch']), int(t['page']), t['guide_page'],
                        t['source'], t['file'], i, json.dumps(row)))
        n += 1
    db.commit()
    print('extra tables loaded:', n)


if __name__ == '__main__':
    main()
