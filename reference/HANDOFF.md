# UFC 3-340-02: handoff notes

Read this first. It explains what is in the repo, what is verified, and what is still open.

## Repo layout
| Folder | Contents |
|---|---|
| `source/pdf/` | The 35 batch PDFs (`batch 1.pdf` to `batch 35.pdf`), the original source |
| `text/chapters/` | Chapters 1 to 6 as readable markdown (OCR, with equations not verified) |
| `ocr/batch-NN/` | Per-page OCR output: `page_NNNN_res.json` (text blocks, labels, positions) and `imgs/` (cropped charts, tables, images, formulas) |
| `graphs/UFC_Plots_data/` | 1,371 plot files (`.grf`) with curve data, split into subfolders by chapter |
| `reference/` | Index spreadsheet, database, plot-to-guide map, database guide, this note |
| `scripts/` | `build_db.py` (builds the database) and `map_grf.py` (links plot files to the guide) |

## Rebuild commands
Run from the repo root.

```bash
python3 scripts/build_db.py --ocr-root ocr --grf-root graphs/UFC_Plots_data --index reference/UFC_3-340-02_index.xlsx --out reference/ufc_340_02.db
python3 scripts/map_grf.py --db reference/ufc_340_02.db --grf-root graphs/UFC_Plots_data --csv reference/grf_to_guide.csv
```

## Plot-to-guide links (`reference/grf_to_guide.csv`)
Every plot file has one row. The `level` column shows how it was linked:

| Level | Count | Meaning |
|---|---|---|
| A caption | 1,323 | Figure caption found in the guide text. Most reliable. |
| B index | 42 | Figure listed in the index spreadsheet, with batch and PDF page. Caption not found in OCR text. Check the page. |
| C text-ref | 6 | Figure only mentioned in guide text (appendix 2A figures 17 to 20). Check the page. |
| D not found | 0 | None. |

How the name rule was checked:
- File names encode the figure number: `02_162.grf` is Figure 2-162; `A2_004B.grf` is Figure 2A-4, sub-curve B.
- Of the 659 numbered plot files that contain their own figure caption, all agree with their file name.
- Of the plot files whose title can be compared with the guide caption, 10 disagree (see below).

## Needs checking
1. **10 plot files whose title does not match the guide caption** (`note` says "differ, check"):
   04_065, 06_012, 06_028A/B, 06_029A/B, 06_030A/B, 06_049, 06_050.
   Example: `06_012.grf` is titled "stress-strain curve", but the guide's Figure 6-12 is "Axial Load Arching". One of the two is wrong.
2. **42 index-only links** (level B). Open the batch and PDF page from the `index_batch_file` and `index_pdf_page` columns and confirm the figure is there.
3. **6 text-only links** (level C), the appendix 2A figures in `A2_017` to `A2_020`.
4. **Equations** are OCR output, not verified against the PDF.
5. **134 images** have no page assigned. In the database, `images.page` is empty for these.
6. **Table of contents lines** sometimes look like captions. Check the page number before trusting a caption.

## Database
`reference/ufc_340_02.db` (SQLite). Guide: `reference/DATABASE.md`.
Key tables: `pages`, `blocks`, `images`, `captions`, `figures`, `index_entries`, `plot_files`, `plot_points`, `plot_labels`, `grf_guide_links`.

## Suggested next steps for analysis tools
1. Use `grf_guide_links` to pick a plot file for a figure, and use `plot_points` for its curve values.
2. Treat level A links as usable. Treat levels B and C, and the 10 flagged files, as needing a visual check against the PDF before use.
3. Check equations against the PDF before using them in any calculation.
