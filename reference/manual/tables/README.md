# Tables taken from the PDF text layer

## Table 5-4 Preliminary Dynamic Load Factors for Plates (batch 28 page 3, guide page 5-40)
File: `table_5-4.csv`

The table is not drawn on the page (it renders blank and the OCR found nothing), but its
values are in the PDF text layer:

| Deflection magnitude | θmax (deg) | μmax | DLF |
|---|---|---|---|
| Small | 2 | 5 | 1.0 |
| Moderate | 4 | 10 | 0.8 |
| Large | 12 | 20 | 0.6 |

\* Deformation limits: whichever governs.

The Greek column symbols are images in the PDF, so they are missing from the text. They are
read as support rotation θmax and ductility ratio μmax from the guide text: section 5-30
("for μ > 10 ... Equation 5-2") and Example 5A-7 ("design rotation of 3°", "μ < 10",
"DLF = 1.0 (Table 5-4)").

## Formula tables (40 files)
2-6, 3-1 to 3-14, 4-2 to 4-7, 4-9 to 4-15, 5-5 to 5-8, 5-10 to 5-16, 6-4. Transcribed by eye from the rendered PDF page; formulas in LaTeX (all parse in KaTeX); support and loading diagrams described in words; footnotes as a `Notes:` row. `../table_pages.csv` gives the source pages (`source_pages`) and, in `note`, anything printed oddly in the guide.
