# reference/: where is what
Paths are relative to the `ufc-data/` folder.

Start with the database `ufc_340_02.db`; the CSV files are the same data for reading in Excel.
Open items and how things were checked: `HANDOFF.md`. Database tables and example queries: `DATABASE.md`.

## Folders
| Path | Kind | What it holds |
|---|---|---|
| `ufc_340_02.db` | output | SQLite database with everything (pages, PDF text, plots, equations, formulas, tables) |
| `missing_data.csv` | output | Every figure and table with its data status; filter `MISSING DATA` for what is still missing |
| `index/UFC_3-340-02_index.xlsx` | input | Index of sections, figures, tables, equations with batch file and page |
| `manual/` | **hand-checked input** | Corrections made by reading the PDF. **Scripts read these but never overwrite them.** |
| `manual/equation_corrections.csv` | hand-checked | Correct LaTeX for 148 numbered equations the OCR got wrong |
| `manual/equation_review.csv` | hand-checked | Finding for each equation checked by eye (150) |
| `manual/formula_manual_fixes.csv` | hand-checked | 91 fix rules for worked-example formulas |
| `manual/table_pages.csv` | hand-checked | Which OCR table block(s) make up each of the 85 tables; data or formula table; notes |
| `manual/tables/` | hand-checked | Tables typed or read by hand: 4 data tables (3-15, 4-8, 5-4, 6-7) and the 40 formula tables, with a README |
| `manual/table_6-7_review.csv` | hand-checked | The 74 Table 6-7 values the two OCR engines disagreed on, as read by eye |
| `equations/equations.csv` | output | **One checked LaTeX form per numbered equation (559). Use this for equations.** |
| `equations/equation_status.csv` | output | One verdict per equation (ok / error / missed ...) |
| `equations/equation_check.csv`, `equation_lines.csv` | output | Automatic OCR-vs-PDF checks behind the verdicts |
| `formulas/formula_fixes.csv` | output | Every fix made to OCR formula blocks (thousands commas, letters, primes) with PDF evidence |
| `formulas/formula_review.csv` | output | Lines the checker was unsure about |
| `formulas/formula_issues.csv` | output | Error patterns found in raw OCR |
| `plots/grf_to_guide.csv` | output | Every `.grf` plot file linked to its guide figure and page |
| `plots/digitized_checks/` | output | Images: digitized curves drawn over the original charts |
| `tables/table_N-M.csv` | output | **Every numbered table (85), one file each.** First column = batch/page it came from |
| `tables/tables_index.csv` | output | One row per table: data or formula, pages, how it was checked, result |
| `tables/table_checks.csv` | output | Every number where the two readings differed, with the verdict |

## Adding new data later
- **A table you typed in**: save it as `manual/tables/table_N-M.csv`, empty the `blocks` column for it in `manual/table_pages.csv` and say why in `note`, then run `bash scripts/rebuild_all.sh`.
- **An equation correction**: add a row to `manual/equation_corrections.csv` (and a finding to `manual/equation_review.csv`), then rebuild.
- **New plot data (.grf)**: put it in `graphs/UFC_Plots_data/<chapter folder>/`, then rebuild.

Output files are rebuilt from scratch every run; edit only the files in `manual/`.
