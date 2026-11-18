# UFC-3-340-02-Tools
Blast load and structural response analysis tools based on U.S. DoD UFC 3-340-02, *Structures to Resist the Effects of Accidental Explosions*.

## Repository layout
| Path | What it is |
|---|---|
| `ufc-data/` | **All reference data from the guide**, organized and checked: source PDFs, OCR output, chart curve data, and a SQLite database with every numbered equation (559, as LaTeX) and table (85). See `ufc-data/README.md`. |
| *(to come)* | Analysis tools (blast loads, structural response) built on `ufc-data/` |

## Using the data from a tool
```python
import sqlite3
db = sqlite3.connect("ufc-data/reference/ufc_340_02.db")
latex, = db.execute("SELECT latex FROM equations WHERE number = '2-2'").fetchone()
rows = db.execute("SELECT row_no, col_no, value FROM guide_table_cells WHERE number = '5-4'").fetchall()
```

## Rebuild the data
```bash
bash ufc-data/scripts/rebuild_all.sh
```
