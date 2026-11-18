# UFC 3-340-02 database
Paths are relative to the `ufc-data/` folder.

File: `reference/ufc_340_02.db` (SQLite). Built by `scripts/build_db.py` from:
- OCR output in `ocr/` for batches 1–35 (page text, layout blocks, cropped images)
- the exact text layer of the PDFs in `source/pdf/`
- the index spreadsheet `reference/index/UFC_3-340-02_index.xlsx`
- plot files in `graphs/UFC_Plots_data/` (original .grf) and `graphs/generated/` (computed)

Then the other scripts add their tables. Rebuild everything with `bash scripts/rebuild_all.sh`.
See `reference/README.md` for where each file is, and `reference/HANDOFF.md` for open items.

## Tables
| Table | What it holds |
|---|---|
| chapters | Chapter number, batch range, title |
| pages | One row per page: batch, page, chapter, OCR text |
| pdf_pages | One row per page: exact text from the PDF text layer (more accurate than OCR) |
| blocks | OCR layout blocks per page: label (text, table, chart, figure_title, formula...), content, box position |
| images | Cropped images (chart, table, image, formula): file, batch, page, box |
| captions | Figure and table captions found in blocks (in-text references like "Figure 2-7 (+)" excluded) |
| figures | Figure caption, page and nearest image |
| index_entries | Sections, figures, tables, equations, examples, problems from the index |
| plot_files | Each .grf file: folder, source (original / generated), layout (data/dx), figure numbers in its text, curve and point counts |
| plot_curves | Each curve: file, curve number, legend label (e.g. "7000"), point count, x/y range |
| plot_points | x, y of every curve point: file, curve number, order |
| plot_labels | Title and axis text in each .grf file |
| grf_guide_links | One row per plot file: plot number, guide figure, sub-curve, link level, page, caption, notes |
| equation_check | Numbered OCR equations compared with the PDF text: status match / close / differ / no-pdf-line |
| equation_lines | Line-level check of each numbered equation against the PDF text |
| equation_review | Hand-checked findings (208), with the correct text from the PDF |
| equations | **One checked LaTeX form per numbered equation** (559): corrected from the PDF where the OCR was wrong, otherwise OCR; original OCR kept in `ocr_latex` |
| equation_status | One verdict per numbered equation: ok (automatic / checked by eye / minor slip), error, missed, check operator |
| formula_issues | OCR formula error patterns as found in the raw OCR: thousands comma read as decimal point, lost minus in powers of ten |
| formulas | Every OCR formula block (1,876) with thousands separators, letters and primes fixed (`latex`), original in `ocr_latex`, list of fixes in `fixes` |
| guide_tables | One row per numbered table (85): title, data or formula, pages, file, numbers checked, how checked, status |
| guide_table_cells | Every cell of every table: table number, row, column, page, value |
| table_checks | Every number where the two readings of a table differed, with the verdict |
| data_status | Every figure and table with its data status (has plot data, MISSING DATA, ...) |

## Counts (this build)
- 1,982 pages (OCR and PDF text), 16,950 blocks, 3,302 images (3,168 placed on a page)
- 1,864 captions, 2,385 index entries
- 1,371 original plot files (10,835 curves, 591,110 points) and 22 generated (214 curves: 19 computed files, 3 digitized); all linked to a guide figure
- 559 numbered equations (all printed in the guide): 206 corrected or added from the PDF page, 353 from OCR after checks
- OCR formula fixes: 207 thousands commas, 124 letters, 14 primes, 119 checked by eye (`formula_fixes.csv`)
- 85 numbered tables exported and checked (45 data tables; 40 formula tables transcribed by eye as LaTeX); 840 figures with a data status

## Known limits
- OCR text and tables can contain errors; prefer `pdf_pages` for exact wording and numbers. In raw OCR formulas, a.bbb is often a thousands value; use table `formulas`, where these are fixed.
- Equation check compares numbers only; Greek letters are images in the PDF.
- 134 images have no page.

## Example queries (DB Browser for SQLite, or any SQLite tool)
Exact PDF text of batch 9, page 35:
```sql
SELECT text FROM pdf_pages WHERE batch = 9 AND page = 35;
```
All curves of Figure 2-194, with their labels:
```sql
SELECT l.grf_file, c.curve_no, c.label, c.point_count
FROM grf_guide_links l JOIN plot_curves c ON c.file = l.grf_file
WHERE l.figure = '2-194' ORDER BY l.grf_file, c.curve_no;
```
Points of the 7000 psi curve in Figure 2-194(a):
```sql
SELECT p.x, p.y FROM plot_points p JOIN plot_curves c ON c.file = p.file AND c.curve_no = p.curve_no
WHERE p.file = '02_194A.grf' AND c.label = '7000' ORDER BY p.seq;
```
A checked equation, as LaTeX:
```sql
SELECT number, latex, source FROM equations WHERE number = '2-23';
```
Table 5-4, as rows and columns:
```sql
SELECT row_no, col_no, value FROM guide_table_cells WHERE number = '5-4' ORDER BY row_no, col_no;
```
All tables and how each was checked:
```sql
SELECT number, kind, title, status, how_checked FROM guide_tables;
```
Everything still missing data:
```sql
SELECT type, number, title, batch, page, priority, note FROM data_status WHERE status = 'MISSING DATA';
```
