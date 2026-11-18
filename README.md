# UFC-3-340-02-Tools
Blast load and structural response analysis tool based on U.S. DoD UFC 3-340-02 (Structures to Resist the Effects of Accidental Explosions).

## Contents
| Folder | What it holds |
|---|---|
| `source/pdf/` | Original batch PDFs (35) |
| `text/chapters/` | Chapters 1–6 as markdown (`ch1_introduction.md` ...; OCR, equations not verified) |
| `ocr/` | Per-page OCR output (layout JSON and cropped images) |
| `graphs/UFC_Plots_data/` | Original plot curve data (.grf files) |
| `graphs/generated/` | Computed or digitized plot data for figures with no original plot file |
| `reference/` | **The database** `ufc_340_02.db`, checked equations, plot-to-guide map, hand-checked corrections. Start with `reference/README.md` (map) and `reference/HANDOFF.md` (status) |
| `scripts/` | Build and check scripts |

## Rebuild the database
```bash
bash scripts/rebuild_all.sh
```
