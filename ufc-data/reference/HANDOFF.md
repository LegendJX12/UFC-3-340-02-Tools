# UFC 3-340-02: handoff notes

Read this first. It explains what is in the data folder, what is verified, and what is still open. All paths are relative to the `ufc-data/` folder.

## Folder layout (inside `ufc-data/`)
See `reference/README.md` for a full "where is what" map. In short:

| Folder | Contents |
|---|---|
| `source/pdf/` | The 35 batch PDFs (`batch 1.pdf` to `batch 35.pdf`). Born-digital: they have an exact text layer. |
| `text/chapters/` | Chapters 1 to 6 as readable markdown, `ch1_introduction.md` to `ch6_...md` (OCR text; use table `equations` for equations) |
| `ocr/batch-NN/` | Per-page OCR output: `page_NNNN_res.json` (text blocks, labels, positions) and `imgs/` (cropped charts, tables, images, formulas) |
| `graphs/UFC_Plots_data/` | 1,371 original plot files (`.grf`, DPLOT v1.6) with curve data, split into subfolders by chapter |
| `graphs/generated/` | 22 plot files for figures with no original plot file: 19 **computed** (`generate_missing.py`) and 3 **digitized** from the PDF (`digitize_figures.py`); see section 5 |
| `reference/ufc_340_02.db` | **The database.** Everything below is also loaded into it |
| `reference/manual/` | **Hand-checked inputs. Never overwritten by scripts; edit by hand only** |
| `reference/equations/`, `formulas/`, `plots/` | Script outputs (CSV), rebuilt every run |
| `reference/tables/` | Every numbered table as CSV (85), with `tables_index.csv` and `table_checks.csv`; see section 3b |
| `reference/index/` | Index spreadsheet |
| `scripts/` | Build and check scripts (see below) |

## Rebuild commands
One command (needs `pdftotext` from poppler); it can be run from anywhere:

```bash
bash scripts/rebuild_all.sh
```

Add `--plots` to also recompute the generated and digitized plot files. For the LaTeX check, run `npm install` once in the `ufc-data/` folder (installs KaTeX from `package.json`); without it the check is skipped. The script lists every step in order, with all file paths.

| Script | Output |
|---|---|
| `build_db.py` | `reference/ufc_340_02.db` (uses `grf.py` to read plot files) |
| `grf.py` | Reader for DPLOT `.grf` files (both `data` and `dx` layouts, curves kept separate with labels) |
| `export_tables.py` | `reference/tables/`, tables `guide_tables`, `guide_table_cells`, `table_checks`: every numbered table, checked against a second reading |
| `read_scanned_table.py`, `check_table_6_7.py` | Tesseract reading of the scanned Table 6-7 (second reading) |
| `rebuild_all.sh` | Runs every step below in order |
| `map_grf.py` | `grf_to_guide.csv` and table `grf_guide_links`: every plot file to its guide figure |
| `check_equations.py` | `equation_check.csv` / table `equation_check` (OCR vs PDF text), `formula_issues.csv` / table `formula_issues` (OCR error patterns), and loads the hand-checked `equation_review.csv` |
| `check_equation_lines.py` | `equation_lines.csv` (line-level check) and `equation_status.csv` / table `equation_status`: one verdict per equation |
| `fix_formulas.py` | Table `formulas` and `formula_fixes.csv`: every OCR formula block with thousands separators, letters and primes fixed (uses `latex_names.py`; hand rules in `formula_manual_fixes.csv`) |
| `build_equations.py` | Table `equations` and `equations.csv`: one checked LaTeX form per numbered equation (corrections from `equation_corrections.csv`) |
| `audit_missing.py` | `missing_data.csv` and table `data_status`: every figure and table with its data status |
| `sdof_bilinear.py` | Calculator: maximum response of an elasto-plastic SDOF system to a bilinear-triangular pulse |
| `generate_missing.py` | Writes the computed plot files in `graphs/generated/` |
| `digitize_chart.py`, `digitize_figures.py` | Digitizer (WebPlotDigitizer method) and the settings for Figures 2-8, 2-16, 6-11 |

## 1. Plot files: all linked to the guide (`grf_to_guide.csv`)
The counts below are for the 1,371 original files. The 22 generated files are also linked (to Figures 2-8, 2-16, 3-64, 3-220 to 3-224, 6-11 and 6-21) and marked GENERATED in `note`; table `plot_files` has `source` = original / generated.

| Level | Count | Meaning |
|---|---|---|
| A caption | 1,170 | Figure caption found on the figure page (contents pages excluded). Sub-panels link to the exact panel, e.g. `03_140B` to "Figure 3-140(b)". |
| B index | 198 | Caption not read by OCR on the figure page; page taken from the index spreadsheet. Each of these pages holds a chart. Sampled charts checked by eye and against curve values. |
| E manual | 3 | Checked by eye: `02_194A`, `02_194B` (Figure 2-194 (a), (b), batch 6 pages 45 and 46) and `04_065` (see below). |

What was found and fixed:
- **Chapter 6 numbering.** All 45 chapter 6 plot files use the older TM 5-1300 numbers. Guide figure = plot number + 3 (e.g. `06_012` is Figure 6-15, `06_028A` is Figure 6-31). Confirmed by titles and by the a/b ratio and glass thickness in each plot. The `plot_number` column keeps the old number.
- **`04_065.grf`** ("Spall threshold for blast waves loading walls", axes i_r v / P1 Tc vs P_r / σ) is not drawn in UFC 3-340-02. It is linked to Figure 4-65 with a note. The guide's own spall chart (batch 23 page 19, h/R vs spall parameter) has no plot file.
- **3 sub-panels** whose own caption was not read (`03_068B`, `03_142B`, `03_147B`) link to the sibling panel's page; see `note`.
- **Index errors found:** the index points to the wrong page for Figures 2-101, 2-153, 3-24, 3-64 and Table 4-1. The database uses the page that actually holds the chart or table.

## 2. Plot data reading (fixed)
Earlier builds read the `.grf` files wrongly: all curves of a file were merged into one list and the `dx` layout (38 files) was not read at all. `scripts/grf.py` now reads both layouts and keeps each curve with its legend label (e.g. "7000" psi, "1% Survival", "a/b = 1.00").
- Table `plot_curves`: 10,835 curves with label and x/y range.
- Table `plot_points`: 591,110 points, keyed by file, curve number and order.
- 113 curves have no label in the file (single-curve plots or unlabelled reference lines).
- Values checked against charts: 2-194 (a) and (b), 2-207, 2A-23, 4A-8.

## 3. Equations (table `equations`, file `equations.csv`)
**Use table `equations` for any equation.** It has one LaTeX form per numbered equation (559):
- **206 corrected from the PDF** (`source` = 'corrected from PDF'), written from the rendered PDF page and listed in `equation_corrections.csv` with a `reason`: 112 OCR errors, 61 equations the OCR missed (4-45b, 4-196, 4-199, and 58 whose numbers the OCR never captured, see below), 26 minor OCR slips, OCR lines paired with the wrong equation number, and 2-24 / 2-25 stored as printed (operator still to confirm). 34 of these (reason contains 'name/prime check') were found by the letter and prime check of section 3a.
- **353 from OCR** (`source` = 'OCR'), where the checks below found no problem; layout leftovers (`&`, `\begin{aligned}`, stray characters) removed.
- All 559 parse in KaTeX (`latex_ok` = 1). The original OCR text is kept in column `ocr_latex`; table `blocks` is unchanged.
- Each correction was checked against the PDF text layer: numbers and variable names agree, except where the text layer itself splits or drops them (exponents on other lines, "87 ,000", "R eff").

How equations were checked (`equation_status.csv`): the PDF text layer (table `pdf_pages`) has exact text, but Greek letters and some symbols are small images, and exponents and fraction parts sit on separate text lines. Every numbered equation found by OCR (501) was checked against it:

1. **Number check** (`check_equations.py`, `check_equation_lines.py`): numbers in the OCR equation vs the PDF lines around the equation number. Multi-line OCR blocks are split line by line.
2. **Variable-name check**: OCR names one letter away from a name in the PDF text (e.g. f_dv vs f_dy).
3. **By eye**: every equation flagged by 1 or 2, every equation that is an image in the PDF (40), and the 16 earlier "differ" cases were compared with the rendered PDF page.

| Verdict | Count | Meaning |
|---|---|---|
| ok (automatic) | 312 | Numbers and variable names agree with the PDF text |
| ok (checked by eye) | 46 | Flagged, but correct on the rendered page (text-layer artefacts) |
| ok (minor slip) | 26 | Small slip; now corrected in `equations` |
| **error** | **112** | OCR was wrong; now corrected in `equations` |
| **missed** | **61** | OCR had no formula or no number (4-45b, 4-196, 4-199 and the 58 above); now in `equations` |
| check operator | 2 | 2-24, 2-25: OCR divides, PDF prints multiplication; `equations` follows the PDF |

Most common OCR faults (see `equation_review.csv` for each equation):
- **y read as v**: f_dy, f_py, f_y, T_y, I_y, m_y, r_y read as f_dv, f_pv, f_v, ... (about 15 equations).
- **Primes lost**: (p - p'), C'_1, X'_f, d', f'dc read without the prime; several equations become identities or zero.
- **E read as F** (X_E, K_E), **p read as o/D** (M_p, M_up), **l (length) read as 1 or I**, **½ and ¼ read as a root sign or γ**.
- **Thousands comma read as decimal point** (87,000 as 87.000; fixed in tables `equations` and `formulas`) and **lost minus signs** in powers of ten.
- **Brackets and fraction bars** misplaced (4-28, 4-166, 4-192, 6-31).

**Limits:** the 312 "ok (automatic)" equations (taken from OCR in `equations`) were not each read by eye; the automatic checks cannot see Greek letters or primes, which are images or tiny marks in the PDF. A lost prime in an equation whose numbers and other names match would pass. For any equation used in a calculation, read it from the rendered PDF page.

**Thousands commas in OCR formulas (worked examples included): fixed.** The OCR read 207 thousands commas as decimal points (87,000 as 87.000; 4,409,934 as 4.409.934), on 82 pages. Table `formulas` holds every OCR formula block (1,876) with these fixed (column `latex`; original in `ocr_latex`); `formula_fixes.csv` lists each fix with the PDF line that shows the comma form. A number is changed only where the PDF page prints the comma form and not the dotted one; 0 remain. 164 fixes were confirmed by neighbouring numbers on the same PDF line, 39 by reading them (values printed alone, such as "fy 66,000", "FE 153,600 lb"), and 4 have no other number nearby and rest on the page rule alone. `formula_issues.csv` keeps the list as found in the raw OCR. Letters and primes: see section 3a.

## 3a. Letters and primes in all OCR formulas (worked examples included)
`fix_formulas.py` compares each variable name in every OCR formula line (3,320 lines) with the matched PDF text line, using `latex_names.py` to read names, subscripts and primes from LaTeX.
- **Letter fixes (124)**: only known OCR swaps (y/v, E/F, l/I, i/j, p/o, p/D, f/t, g/q, ...). A letter is changed only if the corrected name is on the matched PDF line and the OCR name appears nowhere on that page.
- **Prime fixes (14)**: only names of 2+ characters that are primed on the matched PDF line and never unprimed nearby.
- **Checked by eye (119 replacements, 91 rules in `formula_manual_fixes.csv`)**: units (psi, in, ft), names such as i_t → i_r, T_p → T_n, L_wd → L_wf, junk text, and wrong values on batch 30 page 20.
- Every fix is listed in `formula_fixes.csv` (type, OCR text, fixed text, PDF evidence). 142 doubtful lines in `formula_review.csv` were read; two remain open: V_sv and V_st on batch 25 pages 14–15.
- The same check found 34 errors in numbered equations that the number check had passed (lost primes, I_b for i_b, p_v for p_V, brackets read as J). These are now corrected in `equations`.

**Coverage: complete.** Every equation number printed at the right margin of the PDF pages was listed (PDF words, excluding page numbers and table cells). 58 were missing from the table because the OCR never captured their numbers (2-2, 2-4, 2-7, 2-45, 2-48, 2-56, 2-65, 2-75, 2-77, 2-79, 2-91, 3-37, 3-55, 3-87, 4-7, 4-10, 4-11, 4-18, 4-19, 4-31 to 4-33, 4-74, 4-86, 4-92 to 4-94, 4-96, 4-104, 4-114, 4-119, 4-120, 4-137, 4-138a/b, 4-141 to 4-143, 4-154, 4-155, 4-163, 4-176, 4-176a/b, 4-178, 4-179, 4-182 to 4-186, 4-203, 4-204, 4-207, 5-59, 5-63, 6-10, 6-50). Each was read on a zoomed render of its page and added (`equation_corrections.csv`, reason 'OCR missed'). Chapters 2, 3, 5 and 6 now have no gaps in their numbering; chapter 4 skips 4-34 to 4-38, which do not exist in the printed guide (the PDF holds only invisible leftover text "4-34 4-35 4-36 4-37 4-38" on batch 20 page 24). Notes: 4-163 is printed "p_s = A / (bd)" with a missing subscript (probably A_s); 4-186 has an editorial note box beside it in the PDF.

## 3b. Tables (`reference/tables/`, tables `guide_tables`, `guide_table_cells`)
All 85 numbered tables are exported, one CSV each (84 from the index plus Table 4-15a, which the index misses). `tables_index.csv` says for each how it was read and checked. Every number was read twice, by two independent methods, and compared:

| Table kind | First reading | Second reading | Differences |
|---|---|---|---|
| Data tables with a PDF text layer (most) | The PDF's own table grid lines, filled with the exact PDF words (superscripts kept as `^{}`, subscripts as `_{}`) | PaddleOCR | PDF text kept (it is exact); rows also compared one by one |
| Scanned image (Table 6-7, 7 pages) | PaddleOCR | Tesseract, 3 settings, row by row | 1,102 of 1,176 agree; the other 74 read by eye on 4x zoomed scans |
| No usable grid (3-15, 4-8) or blank (5-4) | Typed or built from exact PDF word positions | Read by eye on the rendered page | |

**Data tables (45, including 5-9): checked.** 22 agree fully in both readings; in 19 the readings differ only where the OCR dropped or misread values (such values; the exact PDF text is kept, see `table_checks.csv`); 4 were done by hand (`reference/manual/tables/README.md`). Rows that differ from the OCR were compared with the rendered page by eye (Tables 1-2, 1-6, 2-1, 2-2, 2-3, 2A-3, 3-15, 4-15a, 5-9, 6-5, 6-6, 6-13, 6-14). Tables 6-7, 6-12 and 6-13 also pass trend checks (values rise or fall steadily along rows and columns), except 7 places in 6-13 where the printed values break the trend; these were read on the page and are exported as printed.

What the OCR got wrong in tables (now avoided): dropped rows (Table 1-6 lost 5 rows and scrambled its end), merged rows (6-7), shifted columns, and values such as 2000 read as 200 (6-5).

**Values printed oddly in the PDF (exported as printed):** Table 4-8 Cc = 0.0301 (L/H 1.25, c/L 0.1; probably 0.00301); Table 6-13 values that break the trend (e.g. 23.0 after 43.9 at 26x26, 5/8 in; 14.23 at 23x34.5); Table 6-7 39x39 3/4 in, printed 20.5 as a correction pasted over the scanned 10.5.

**Formula tables (40): checked by eye.** Tables 2-6, 3-1 to 3-14, 4-2 to 4-15 (except 4-8), 5-5 to 5-8 and 5-10 to 5-16, and 6-4 hold formulas, often drawn as pictures and Greek letters the PDF text cannot carry. Each was transcribed by eye from the rendered PDF page (zoomed where small) into `reference/manual/tables/table_N-M.csv`: formulas as LaTeX (all 450 formula cells parse in KaTeX), support and loading diagrams described in words (for example "Fixed one end, simply supported other; uniform load"), and footnotes kept as a `Notes:` row. Every number in the transcriptions that the PDF text layer holds was found there; the rest are in formulas drawn as pictures (2-6, 3-2, 3-3, 3-10, 3-11, 3-13, 4-10 page 22/2, 4-13) and were read twice on zoomed renders. The 3-13 interpolation formulas reproduce the table values at both ends of their ranges. Table 5-9 turned out to be a data table and is checked as one.

Places where the printed formula looks like a slip in the guide (kept as printed, explained in the `note` of `reference/manual/table_pages.csv`):
- 3-3, three-edges row: first term uses M_HP1 where the others use M_HP.
- 3-6, three-edges row x <= H: x tan(theta_V), where the other rows use theta_H.
- 3-11, four-edges row y_2: 3 r_u x (L-x)(...), probably 3 r_u (L-x)(...).
- 3-14, last row: X_{n-1} printed as X_{j-1} (pattern gives X_j).
- 5-15, row 6: 3 alpha H + (n-1) L without the squares that Table 5-13 has.
Also: the PDF text of Table 5-8 contains hidden words ("maximum end reaction") that are not printed; the printed wording is used.

## 4. Missing data (`missing_data.csv`, table `data_status`)
840 figures and 84 tables, each with a status.

| Type | Status | Count |
|---|---|---|
| Figure | has plot data | 562 |
| Figure | no data needed (schematic, sketch, photo) | 257 |
| Figure | example plot (values printed on it) | 10 |
| Figure | has plot data (generated) | 10 |
| Figure | **MISSING DATA** | **0** |
| Table | cells captured (OCR, values to check) | 83 |
| Table | cells from PDF text | 1 |

**Generated - now has plot data** (see section 5):
- **3-64 (a), (b)**: computed, C1 = 1.000, C2 = 1.0 (batch 13 p49-50).
- **3-220 to 3-224**: computed, C1 = 0.909 to 0.750, C2 = 1000 (batch 17 p1-5).
- **6-21**: Roof live load vs tributary area (exact rule from the guide text, spec 4.2.1).
- **2-8, 2-16**: digitized from the scanned charts (batch 3 p8 and p15).
- **6-11**: digitized example curve, four corner points (batch 31 p49).

**Table 5-4** (Preliminary Dynamic Load Factors for Plates, batch 28 p3) is not drawn on the page, so it renders blank and OCR found nothing, but its values are in the PDF text layer: `reference/tables/table_5-4.csv` (see the README there).

How these were decided: every chart without a plot file was viewed (contact sheets of all 65 chart images), plus the PDF pages of figures where OCR found no picture. 206 figures marked "diagram, layout or photo" were judged from page content and title, not each viewed.

## 5. Generated plot data (`graphs/generated/`)
Figures 3-64 to 3-266 are computed charts: the maximum response of an elasto-plastic one-degree-of-freedom system to a bilinear-triangular pulse (guide section 3-19.3.4). The load is the envelope of a shock triangle (P, T) and a gas triangle (C1·P, C2·T); its impulse matches the guide's Equation 3-82. `scripts/sdof_bilinear.py` computes the same three chart panels: A = tm/Tn, B = Xm/XE, C = tE/T, for P/ru = 0.5 to 20.

Checks against original plot data:
| Original chart | Case | Median error | Notes |
|---|---|---|---|
| 3-54 (triangular load) | C1 = C2 = 1, as Figure 3-64 | 0.00% (worst 0.04%) | Basis for generated 3-64 |
| 3-225 | C1 = 0.715, C2 = 1000, nearest to 3-220..3-224 | 0.6% ductility, 0.7% time | Basis for generated 3-220..3-224 |
| 3-65, 3-66, 3-99 | C2 = 1.7 to 10 | 0.05% to 0.8% | |
| 3-200, 3-219, 3-240, 3-266 | small C1 with C2 = 300 to 1000 | large differences at short T/Tn | The printed charts have flat steps there (regions A/B, where the guide says to use simplified methods instead). Not used for generation. |

The generated 3-220 to 3-224 values fall smoothly between each other and into the original 3-225 and 3-226 (e.g. ductility at P/ru = 1, T/Tn = 1: 5.5, 3.0, 2.29, then original 2.11, 2.00).

Limits: the generated charts follow the computation, not the printed scan, so small differences from the printed figures are possible. The printed charts also show region boundary symbols (A/B/C/D), which are not generated.

### Digitized charts (Figures 2-8, 2-16, 6-11)
The WebPlotDigitizer website cannot be reached from the build machine, so its method is scripted (`digitize_chart.py`): the PDF page is rendered at 300 dpi, the log axes are calibrated from the plot frame and the decade tick marks (piecewise, which corrects a 9-pixel scan stretch on 2-8), and each curve is traced from a seed point. Where curves cross or overlap, the trace keeps its direction.
- 6 curves per chart: P_so (2-8) or P_s (2-16), P_r, i_s/W^1/3, i_r/W^1/3 (left axis); t_o/W^1/3, L_w/W^1/3 (right axis). About 120 points per curve.
- Check by eye: `reference/plots/digitized_checks/fig_2-8.png` and `fig_2-16.png` show the traced curves drawn over the original charts.
- Physical check: peak negative pressure at small Z reads 14.7 psi on both charts, which is atmospheric pressure (the vacuum limit).
- Accuracy: one pixel is about 0.45% of a value on these log scales; with line thickness and calibration, expect about 1 to 3%.
- 6-11 is an example curve of four straight segments (shape as Figure 6-13): (0, 0), (0.04, 0.614), (0.08, 0.051), (7.625, 0). The end point 7.61 measured matches the 7.625 in thickness of an 8-in masonry unit. The two small deflections (Xe, 2Xe) are within about ±0.03.

## Still open
1. Compare the digitized 2-8 and 2-16 with any other copy of these charts if one becomes available.
2. Confirm the operator in Equations 2-24, 2-25, 2-28 (multiply in the PDF, divide in OCR) against another copy of the guide.
3. Read primes and Greek letters from the rendered page for any equation used in a tool (see the limits in section 3).
4. Table cells are OCR; check values against the PDF text layer before use.
5. 134 images have no page assigned (`images.page` empty).

## Suggested next steps for analysis tools
1. Pick a plot file for a figure with `grf_guide_links`, and read its curves from `plot_curves` / `plot_points` (curve `label` gives the parameter, e.g. overpressure).
2. Levels A, B and E are all checked links. Mind the chapter 6 renumbering (`plot_number` vs `figure`).
3. For equations, use table `equations` (column `latex`). For an equation taken from OCR, check primes and Greek letters on the rendered page before using it in a calculation. Use `pdf_pages` for table values; it is exact, unlike OCR.
4. Check `data_status` before relying on a figure or table.
