# UFC 3-340-02 database

File: `reference/ufc_340_02.db` (SQLite). Built by `scripts/build_db.py` from:
- OCR output in `ocr/` for batches 1–35 (page text, layout blocks, cropped images)
- the index spreadsheet `reference/UFC_3-340-02_index.xlsx`
- plot files in `graphs/UFC_Plots_data/` (.grf)

Plot-to-guide links are in table `grf_guide_links` (also `reference/grf_to_guide.csv`), built by `scripts/map_grf.py`. See `reference/HANDOFF.md` for the open items.

## Tables
| Table | What it holds |
|---|---|
| chapters | Chapter number, batch range, title |
| pages | One row per page: batch, page, chapter, full page text |
| blocks | Layout blocks per page: label (text, table, chart, figure_title, formula...), content, box position |
| images | Cropped images (chart, table, image, formula): file name, batch, page, box |
| captions | Figure and table captions found in blocks |
| figures | Figure number, caption, page, nearest image, matching plot file(s) |
| index_entries | Sections, figures, tables, equations, examples, problems from the index |
| plot_files | Each .grf file: folder, figure numbers in its text, point count |
| plot_points | x, y values of every plot curve (in order) |
| plot_labels | Text lines in each .grf file (axis titles, legends) |
| grf_guide_links | One row per plot file: the guide figure it belongs to, and how it was matched |

## Counts (this build)
- 1,982 pages, 16,950 blocks, 3,302 images (3,168 placed on a page)
- 1,910 captions, 1,739 figures
- 2,385 index entries
- 1,371 plot files, 561,397 plot points, all linked to a guide figure

## Known limits
- Image-to-page links use box coordinates. 134 images have no page.
- Some "figure" captions come from the table of contents, so check the page number.
- Figure-to-plot matching uses the figure number inside each .grf file. Plot files without a caption cannot be matched.
- Equations are OCR output and are not verified against the PDF.

## Example queries (DB Browser for SQLite, or any SQLite tool)
Find all text on page 35 of batch 9:
```sql
SELECT content FROM blocks WHERE batch = 9 AND page = 35;
```
Find the plot points for figure 2-7:
```sql
SELECT p.file, p.x, p.y FROM plot_points p JOIN plot_files f ON f.file = p.file
WHERE f.captions LIKE '%2-7%' ORDER BY p.file, p.seq;
```
Find all tables in chapter 4:
```sql
SELECT number, batch, page, caption FROM captions WHERE kind = 'table' AND batch BETWEEN 19 AND 26;
```
