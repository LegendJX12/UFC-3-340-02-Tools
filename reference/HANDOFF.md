# UFC 3-340-02: handoff notes

Read this first. It explains what is in the repo, what is verified, and what is still open.

## Repo layout
| Folder | Contents |
|---|---|
| `source/pdf/` | The 35 batch PDFs (`batch 1.pdf` to `batch 35.pdf`). Born-digital: they have an exact text layer. |
| `text/chapters/` | Chapters 1 to 6 as readable markdown (OCR; equations not verified) |
| `ocr/batch-NN/` | Per-page OCR output: `page_NNNN_res.json` (text blocks, labels, positions) and `imgs/` (cropped charts, tables, images, formulas) |
| `graphs/UFC_Plots_data/` | 1,371 original plot files (`.grf`, DPLOT v1.6) with curve data, split into subfolders by chapter |
| `graphs/generated/` | 22 plot files for figures with no original plot file: 19 **computed** (`generate_missing.py`) and 3 **digitized** from the PDF (`digitize_figures.py`); see section 5 |
| `reference/tables/` | Tables recovered from the PDF text layer (Table 5-4) |
| `reference/digitized_checks/` | Digitized curves drawn over the original charts, for checking by eye |
| `reference/` | Index spreadsheet, database, check lists (CSV), database guide, this note |
| `scripts/` | Build and check scripts (see below) |

## Rebuild commands
Run from the repo root, in this order. `pdftotext` (poppler) is needed for the PDF text layer.
`--grf-root graphs` reads both the original and the generated plot files.

```bash
python3 scripts/generate_missing.py --out graphs/generated
python3 scripts/digitize_figures.py --pdf-root source/pdf --out graphs/generated --checks reference/digitized_checks
python3 scripts/build_db.py --ocr-root ocr --grf-root graphs --index reference/UFC_3-340-02_index.xlsx --pdf-root source/pdf --out reference/ufc_340_02.db
python3 scripts/map_grf.py --db reference/ufc_340_02.db --grf-root graphs --csv reference/grf_to_guide.csv
python3 scripts/check_equations.py --db reference/ufc_340_02.db --csv reference/equation_check.csv --issues reference/formula_issues.csv --review reference/equation_review.csv
python3 scripts/audit_missing.py --db reference/ufc_340_02.db --csv reference/missing_data.csv
```

| Script | Output |
|---|---|
| `build_db.py` | `reference/ufc_340_02.db` (uses `grf.py` to read plot files) |
| `grf.py` | Reader for DPLOT `.grf` files (both `data` and `dx` layouts, curves kept separate with labels) |
| `map_grf.py` | `grf_to_guide.csv` and table `grf_guide_links`: every plot file to its guide figure |
| `check_equations.py` | `equation_check.csv` / table `equation_check` (OCR vs PDF text), `formula_issues.csv` / table `formula_issues` (OCR error patterns), and loads the hand-checked `equation_review.csv` |
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

## 3. Equations (`equation_check.csv`)
The PDFs have an exact text layer, now stored in table `pdf_pages`. Each OCR equation with a number was compared with the PDF line ending in the same number (numbers only; Greek letters are images in the PDF).

| Status | Count | Meaning |
|---|---|---|
| match | 254 | Same numbers in OCR and PDF |
| close | 191 | One side contains the other (equation split over lines). Probably fine; check before use. |
| differ | 16 | Hand-checked against the rendered PDF: see below and `equation_review.csv`. |
| no-pdf-line | 40 | The equation is an image in the PDF; check by eye. |

How "differ" is decided: for each OCR equation number, the nearest OCR formula on the page is compared with the PDF text line ending in that number. Only the numbers in each are compared (constants, exponents, subscripts). "differ" means each side has numbers the other lacks.

**Review of the 16 (`equation_review.csv`, table `equation_review`):**
| Finding | Count | Equations |
|---|---|---|
| OCR error | 6 | 2-23 (exponent 7.2944 should be 1.2944), 2-60 and 2-62 (47,690 and 58,400 read as 47.690 and 58.400), 4-140b (bracket/exponent wrong, 2,500 read as 2.500), 6-22b and 6-23b (f_ps read as f_os, 60,000/30,000 read as 60.000/30.000) |
| OCR missed the equation | 2 | 4-196, 4-199 (the "Xf > 2d" equations); correct text from the PDF in the review file |
| Pairing mistake, OCR correct | 4 | 2-21, 4-5, 4-71, 4-181c |
| PDF text splits a number, OCR correct | 4 | 2-67, 4-173, 5-17, 6-7 |

Found in the same blocks while checking (not in the 16):
- 2-28: exponent G read as O. 2-30: minus signs lost (10^-4, 10^-9 read as 10^4, 10^9). 4-140a: spurious symbol. 4-181b: Cf read as C_t, "/" lost in R/W^0.333.
- **2-24, 2-25, 2-28: OCR has a division between brackets; the PDF prints multiplication** (a small dot in 2-24, brackets side by side in 2-25 and 2-28). The PDF form is used; confirm against another copy of the guide if one is available.

**Error patterns across all OCR formulas (`formula_issues.csv`, table `formula_issues`):**
- Thousands comma read as decimal point: **207** places on 82 pages, mostly in worked examples (e.g. 153,600 read as 153.600). Any number in OCR LaTeX of the form a.bbb may be a thousands value.
- Minus lost in a power of ten: 1 more found by scan (Equation 2-30).
- The "close" group (191) compares whole multi-line blocks, so errors inside a block can hide there (2-30 was found this way). Splitting blocks line by line would check them properly.

Rule for the analysis tools: take equations from the PDF text (`pdf_pages`) or from a checked source, not from OCR LaTeX alone.

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
- Check by eye: `reference/digitized_checks/fig_2-8.png` and `fig_2-16.png` show the traced curves drawn over the original charts.
- Physical check: peak negative pressure at small Z reads 14.7 psi on both charts, which is atmospheric pressure (the vacuum limit).
- Accuracy: one pixel is about 0.45% of a value on these log scales; with line thickness and calibration, expect about 1 to 3%.
- 6-11 is an example curve of four straight segments (shape as Figure 6-13): (0, 0), (0.04, 0.614), (0.08, 0.051), (7.625, 0). The end point 7.61 measured matches the 7.625 in thickness of an 8-in masonry unit. The two small deflections (Xe, 2Xe) are within about ±0.03.

## Still open
1. Compare the digitized 2-8 and 2-16 with any other copy of these charts if one becomes available.
2. Check the 40 `no-pdf-line` equations by eye, and the 191 `close` blocks line by line.
3. Confirm the operator in Equations 2-24, 2-25, 2-28 (multiply in the PDF, divide in OCR) against another copy of the guide.
4. Table cells are OCR; check values against the PDF text layer before use.
5. 134 images have no page assigned (`images.page` empty).

## Suggested next steps for analysis tools
1. Pick a plot file for a figure with `grf_guide_links`, and read its curves from `plot_curves` / `plot_points` (curve `label` gives the parameter, e.g. overpressure).
2. Levels A, B and E are all checked links. Mind the chapter 6 renumbering (`plot_number` vs `figure`).
3. Use `pdf_pages` text for equations and table values; it is exact, unlike OCR.
4. Check `data_status` before relying on a figure or table.
