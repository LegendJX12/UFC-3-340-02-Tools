# UFC 3-340-02: handoff notes

Read this first. It explains what is in the repo, what is verified, and what is still open.

## Repo layout
| Folder | Contents |
|---|---|
| `source/pdf/` | The 35 batch PDFs (`batch 1.pdf` to `batch 35.pdf`). Born-digital: they have an exact text layer. |
| `text/chapters/` | Chapters 1 to 6 as readable markdown (OCR; equations not verified) |
| `ocr/batch-NN/` | Per-page OCR output: `page_NNNN_res.json` (text blocks, labels, positions) and `imgs/` (cropped charts, tables, images, formulas) |
| `graphs/UFC_Plots_data/` | 1,371 plot files (`.grf`, DPLOT v1.6) with curve data, split into subfolders by chapter |
| `reference/` | Index spreadsheet, database, check lists (CSV), database guide, this note |
| `scripts/` | Build and check scripts (see below) |

## Rebuild commands
Run from the repo root, in this order. `pdftotext` (poppler) is needed for the PDF text layer.

```bash
python3 scripts/build_db.py --ocr-root ocr --grf-root graphs/UFC_Plots_data --index reference/UFC_3-340-02_index.xlsx --pdf-root source/pdf --out reference/ufc_340_02.db
python3 scripts/map_grf.py --db reference/ufc_340_02.db --grf-root graphs/UFC_Plots_data --csv reference/grf_to_guide.csv
python3 scripts/check_equations.py --db reference/ufc_340_02.db --csv reference/equation_check.csv
python3 scripts/audit_missing.py --db reference/ufc_340_02.db --csv reference/missing_data.csv
```

| Script | Output |
|---|---|
| `build_db.py` | `reference/ufc_340_02.db` (uses `grf.py` to read plot files) |
| `grf.py` | Reader for DPLOT `.grf` files (both `data` and `dx` layouts, curves kept separate with labels) |
| `map_grf.py` | `grf_to_guide.csv` and table `grf_guide_links`: every plot file to its guide figure |
| `check_equations.py` | `equation_check.csv` and table `equation_check`: OCR equations vs PDF text |
| `audit_missing.py` | `missing_data.csv` and table `data_status`: every figure and table with its data status |

## 1. Plot files: all 1,371 linked to the guide (`grf_to_guide.csv`)
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
| differ | 16 | Check. Includes real OCR errors, e.g. Equation 2-23: OCR exponent 7.2944, PDF 1.2944. Some are pairing errors (the OCR formula next to the number is a different line). |
| no-pdf-line | 40 | The equation is an image in the PDF; check by eye. |

Rule for the analysis tools: take equations from the PDF text (`pdf_pages`) or from a checked source, not from OCR LaTeX alone.

## 4. Missing data (`missing_data.csv`, table `data_status`)
840 figures and 84 tables, each with a status.

| Type | Status | Count |
|---|---|---|
| Figure | has plot data | 562 |
| Figure | no data needed (schematic, sketch, photo) | 257 |
| Figure | example plot (values printed on it) | 10 |
| Figure | **MISSING DATA** | **10** |
| Table | cells captured (OCR, values to check) | 83 |
| Table | **MISSING DATA** | **1** |

**Missing data, high priority** (design charts with no plot file; need digitizing):
- **2-8**: Negative phase shock wave parameters, spherical free-air burst (batch 3 p8). No `02_008.grf`.
- **2-16**: Negative phase shock wave parameters, hemispherical surface burst (batch 3 p15). Only `02_016.BMP`, a picture.
- **3-64 (a), (b)**: Maximum response, elasto-plastic SDOF, bilinear-triangular pulse, C1 = 1.000 (batch 13 p49-50).
- **3-220 to 3-224**: Maximum response, bilinear-triangular pulse, C1 = 0.909 to 0.750, C2 = 1000 (batch 17 p1-5).
- **Table 5-4**: Preliminary Dynamic Load Factors for Plates (batch 28 p3). The table body is blank in the source PDF itself; needs another copy of the guide.

**Missing data, low priority:**
- **6-21**: Roof live load vs tributary area (20 psf to 200 ft², linear to 12 psf at 600 ft²). Can be coded as a formula.
- **6-11**: Resistance-deflection plot, unreinforced masonry with arching.

How these were decided: every chart without a plot file was viewed (contact sheets of all 65 chart images), plus the PDF pages of figures where OCR found no picture. 206 figures marked "diagram, layout or photo" were judged from page content and title, not each viewed.

## Still open
1. Digitize the 8 high-priority charts and obtain Table 5-4.
2. Check the 16 `differ` and 40 `no-pdf-line` equations against the PDF.
3. Table cells are OCR; check values against the PDF text layer before use.
4. 134 images have no page assigned (`images.page` empty).

## Suggested next steps for analysis tools
1. Pick a plot file for a figure with `grf_guide_links`, and read its curves from `plot_curves` / `plot_points` (curve `label` gives the parameter, e.g. overpressure).
2. Levels A, B and E are all checked links. Mind the chapter 6 renumbering (`plot_number` vs `figure`).
3. Use `pdf_pages` text for equations and table values; it is exact, unlike OCR.
4. Check `data_status` before relying on a figure or table.
