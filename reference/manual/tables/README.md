# Tables entered or read by hand

`scripts/export_tables.py` uses these files instead of the OCR table. Each is listed in
`reference/manual/table_pages.csv` with its source pages (`source_pages`) and the reason (`note`).

## Data tables (4 files)
| File | Why by hand | How it was checked |
|---|---|---|
| `table_3-15.csv` | No lines between rows, so the automatic grid failed | Built from exact PDF word positions (rows from C1 values, columns from C2 headings); checked by eye |
| `table_4-8.csv` | Rotated table without column lines | Typed from the PDF text layer; checked by eye. The PDF prints Cc = 0.0301 for L/H = 1.25, c/L = 0.1 (probably 0.00301) |
| `table_5-4.csv` | Renders blank; OCR found nothing | Typed from the PDF text layer. θmax / μmax column names read from the guide text (section 5-30, Example 5A-7) |
| `table_6-7.csv` | Scanned image (no text layer), 7 pages | PaddleOCR and Tesseract (3 settings, `scripts/check_table_6_7.py`) agree on 1,102 of 1,176 values; the other 74 read by eye on 4x zoomed scans, see `../table_6-7_review.csv` |

## Formula tables (40 files)
2-6, 3-1 to 3-14, 4-2 to 4-7, 4-9 to 4-15, 5-5 to 5-8, 5-10 to 5-16, 6-4. Transcribed by eye from the
rendered PDF page; formulas in LaTeX (all 450 formula cells parse in KaTeX); support and loading
diagrams described in words; footnotes kept as a `Notes:` row. Numbers were cross-checked with the
PDF text layer where it exists. Anything printed oddly in the guide is kept as printed and explained
in the `note` column of `../table_pages.csv`.

## Table 5-4 values
| Deflection magnitude | θmax (deg) | μmax | DLF |
|---|---|---|---|
| Small | 2 | 5 | 1.0 |
| Moderate | 4 | 10 | 0.8 |
| Large | 12 | 20 | 0.6 |
