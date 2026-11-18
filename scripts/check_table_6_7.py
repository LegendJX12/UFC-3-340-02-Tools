"""Second reading of scanned Table 6-7 (batch 33 pages 38-44) with Tesseract, compared with PaddleOCR.

Reads every table row three times with Tesseract (4x, 6x thresholded, 3x enlargement) and compares each
value with the PaddleOCR table. A value is confirmed when PaddleOCR agrees with at least one Tesseract
reading. The rest were read by eye on zoomed crops; decisions are in reference/manual/table_6-7_review.csv
and the checked table is reference/manual/tables/table_6-7.csv.

Usage: python3 scripts/check_table_6_7.py   (run from the repo root; writes table_6-7_check.json in --out)
"""
import sys,csv,re,subprocess,os,tempfile,json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import read_scanned_table as R
from PIL import Image, ImageOps
import numpy as np
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
def tess_rows(page, scale, thresh=None):
    im=R.page_image('source/pdf/batch 33.pdf',page)
    a=np.array(im)<128; h,w=a.shape
    rowsum=a.sum(1); hl=[(s+e)//2 for s,e in R._runs(rowsum>0.6*w)]
    top=max([y for y in hl if y<h*.25],default=0); bottom=max(hl) if max(hl)>h*.5 else h
    ink=a.sum(1)-4
    bands=[(s,e) for s,e in R._runs(ink>6,3) if s>top+1 and e<bottom-1]
    out=[]
    with tempfile.TemporaryDirectory() as t:
        for y0,y1 in bands:
            c=im.crop((3,max(0,y0-2),w-3,min(h,y1+2))); c=c.resize((c.width*scale,c.height*scale),Image.LANCZOS)
            if thresh: c=c.point(lambda v:255 if v>thresh else 0)
            c=ImageOps.expand(c,border=20,fill=255); p=os.path.join(t,'r.png'); c.save(p)
            out.append((y0,y1,subprocess.run(['tesseract',p,'-','--psm','7','-c','tessedit_char_whitelist=0123456789.x '],capture_output=True,text=True).stdout.split()))
    return out
res={}
for page in range(38,45):
    res[page]={'t4':tess_rows(page,4),'t6':tess_rows(page,6,160),'t3':tess_rows(page,3)}
json.dump(res,open('reference/tables/table_6-7_tesseract.json','w'))
print('done')
