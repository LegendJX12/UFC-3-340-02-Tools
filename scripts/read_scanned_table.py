"""Read a table that is a scanned image in the PDF (Table 6-7), cell by cell, with Tesseract.

The page image is split into cells from its own ruling lines (columns) and text bands (rows);
each cell is enlarged 4x and read on its own (digits only). This gives a second reading that is
independent of PaddleOCR, so the two can be compared cell by cell.

Usage (module): read_scanned_page(pdf_path, page_number) -> list of rows (list of cell strings)
"""
import io, os, subprocess, tempfile
import numpy as np
from PIL import Image, ImageOps


def _runs(mask, min_len=1):
    out, start = [], None
    for i, v in enumerate(list(mask) + [False]):
        if v and start is None:
            start = i
        elif not v and start is not None:
            if i - start >= min_len:
                out.append((start, i))
            start = None
    return out


def page_image(pdf_path, page_number):
    import pymupdf
    doc = pymupdf.open(pdf_path)
    page = doc[page_number - 1]
    xref = max(page.get_images(), key=lambda im: im[2] * im[3])[0]
    pix = pymupdf.Pixmap(doc, xref)
    return Image.open(io.BytesIO(pix.tobytes('png'))).convert('L')


def read_scanned_page(pdf_path, page_number, scale=4, whitelist='0123456789.x'):
    im = page_image(pdf_path, page_number)
    a = np.array(im) < 128
    h, w = a.shape
    # vertical ruling lines: columns that are dark over most of the table height
    colsum = a.sum(0)
    vlines = [(s + e) // 2 for s, e in _runs(colsum > 0.5 * h)]
    # header bottom: the lowest long horizontal line in the top quarter
    rowsum = a.sum(1)
    hlines = [(s + e) // 2 for s, e in _runs(rowsum > 0.6 * w)]
    top = max([y for y in hlines if y < h * 0.25], default=0)
    bottom = max(hlines) if hlines and max(hlines) > h * 0.5 else h
    # text rows: bands with ink beyond the vertical rules
    inner = a[:, :]
    ink = inner.sum(1) - len(vlines) * 2
    bands = [(s, e) for s, e in _runs(ink > 6, 3) if s > top + 1 and e < bottom - 1]
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for (y0, y1) in bands:
            row = []
            for x0, x1 in zip(vlines[:-1], vlines[1:]):
                crop = im.crop((x0 + 2, max(0, y0 - 2), x1 - 1, min(h, y1 + 2)))
                crop = crop.resize((crop.width * scale, crop.height * scale), Image.LANCZOS)
                crop = ImageOps.expand(crop, border=20, fill=255)
                path = os.path.join(tmp, 'c.png')
                crop.save(path)
                txt = subprocess.run(['tesseract', path, '-', '--psm', '7', '-c', f'tessedit_char_whitelist={whitelist}'],
                                     capture_output=True, text=True).stdout.strip()
                row.append(txt)
            rows.append(row)
    return rows, dict(vlines=vlines, bands=bands, top=top, bottom=bottom, size=(w, h))


if __name__ == '__main__':
    import sys
    rows, info = read_scanned_page(sys.argv[1], int(sys.argv[2]))
    print(info['vlines'], len(info['bands']), info['top'], info['bottom'])
    for r in rows:
        print(r)
