# UFC 3-340-02 reference data

Everything taken from U.S. DoD UFC 3-340-02 (*Structures to Resist the Effects of Accidental Explosions*, 5 Dec 2008, Change 2 Sept 2014), organized and checked, for the analysis tools in this repository. All paths below are inside this `ufc-data/` folder.

## Start here
| Need | Use |
|---|---|
| Any data, by SQL | `reference/ufc_340_02.db` (SQLite). Tables and example queries: `reference/DATABASE.md` |
| An equation | `reference/equations/equations.csv` (559 numbered equations, checked LaTeX) |
| A table | `reference/tables/table_N-M.csv` (all 85 tables, checked); index in `reference/tables/tables_index.csv` |
| A chart's curve data | `graphs/` (.grf plot files); which file belongs to which figure: `reference/plots/grf_to_guide.csv` |
| Where each file is | `reference/README.md` |
| What was checked, what is open | `reference/HANDOFF.md` |

## Folders
| Folder | What it holds |
|---|---|
| `source/pdf/` | The guide as 35 batch PDFs (the original) |
| `text/chapters/` | Chapters 1 to 6 as markdown (OCR text) |
| `ocr/` | Per-page OCR output (layout JSON and cropped images) |
| `graphs/UFC_Plots_data/` | Original plot curve data (1,371 .grf files) |
| `graphs/generated/` | Computed or digitized curves for figures with no original plot file |
| `reference/` | The database, checked equations and tables, plot-to-figure map, hand-checked corrections (`reference/manual/`) |
| `scripts/` | Scripts that build and check everything |

## Rebuild
```bash
bash ufc-data/scripts/rebuild_all.sh
```
Needs Python 3 with `pymupdf numpy pillow openpyxl`, `pdftotext` (poppler) and `tesseract`. Edit only files in `reference/manual/`; everything else is rebuilt.
