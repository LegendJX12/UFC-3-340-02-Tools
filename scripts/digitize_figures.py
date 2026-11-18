"""Digitize UFC 3-340-02 Figures 2-8, 2-16 (scanned charts) and 6-11 from the source PDF.

Same method as WebPlotDigitizer (that website is not reachable from the build machine):
render the PDF page at 300 dpi, calibrate the log axes from the plot frame and the
decade tick marks, then trace each curve from a seed point (scripts/digitize_chart.py).

Outputs:
  graphs/generated/02_008.grf, 02_016.grf, 06_011.grf   curves (DPLOT layout, marked GENERATED)
  reference/digitized_checks/fig_2-8.png, ...  traced curves drawn over the chart, for checking

Usage: python3 scripts/digitize_figures.py --pdf-root source/pdf --out graphs/generated --checks reference/digitized_checks
Needs pdftoppm (poppler).
"""
import argparse, math, os, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digitize_chart import Chart  # noqa: E402
from generate_missing import write_grf  # noqa: E402
from PIL import Image, ImageDraw

NOTE = 'GENERATED: digitized from the scanned chart by scripts/digitize_figures.py (not part of the original plot set)'

# crop box (pixels at 300 dpi) and calibration, measured from frame lines and decade ticks
FIGURES = {
    '2-8': dict(
        pdf='batch 3.pdf', page=8, crop=(279, 759, 2216, 2032), file='02_008.grf',
        title=['Figure 2-8.  Negative phase shock wave parameters for a spherical',
               'TNT explosion in free air at sea level',
               'Scaled Distance, Z = R/W{\\u1/3} (ft/lb{\\u1/3})',
               'P{\\dso-}, P{\\dr-} (psi); i{\\ds-}/W{\\u1/3}, i{\\dr-}/W{\\u1/3} (psi-ms/lb{\\u1/3}); '
               't{\\do-}/W{\\u1/3} (ms/lb{\\u1/3}), L{\\dw-}/W{\\u1/3} (ft/lb{\\u1/3}) on right axis'],
        frame=(193.5, 48.5, 1735, 1137.5),
        x=[(193.5, 0.1), (708, 1), (1230, 10), (1735, 100)],
        yl=[(1137.5, 1), (594, 10), (48.5, 100)],
        yr=[(1137.5, 0.1), (594, 1), (48.5, 10)],
        curves=[  # label, axis, list of (seed Z, seed value, Z from, Z to)
            ('P-so (psi)', 'left', [(5, 2.87, None, None)]),
            ('P-r (psi)', 'left', [(8, 2.78, None, None)]),
            ('i-s/W^1/3 (psi-ms/lb^1/3)', 'left', [(8, 7.05, None, None)]),
            ('i-r/W^1/3 (psi-ms/lb^1/3)', 'left', [(8, 12.14, None, None)]),
            ('t-o/W^1/3 (ms/lb^1/3) [right axis]', 'right', [(0.5, 6.64, None, 9.5), (30, 8.65, 9.5, None)]),
            ('L-w/W^1/3 (ft/lb^1/3) [right axis]', 'right', [(5, 3.593, None, 49.5)]),  # stop before frame corner
        ]),
    '2-16': dict(
        pdf='batch 3.pdf', page=15, crop=(288, 773, 2200, 2409), file='02_016.grf',
        title=['Figure 2-16.  Negative phase shock wave parameters for a hemispherical',
               'TNT explosion on the surface at sea level',
               'Scaled Distance, Z = R/W{\\u1/3} (ft/lb{\\u1/3})',
               'P{\\ds-}, P{\\dr-} (psi); i{\\ds-}/W{\\u1/3}, i{\\dr-}/W{\\u1/3} (psi-ms/lb{\\u1/3}); '
               't{\\do-}/W{\\u1/3} (ms/lb{\\u1/3}), L{\\dw-}/W{\\u1/3} (ft/lb{\\u1/3}) on right axis'],
        frame=(269.5, 52, 1695.5, 1474.5),
        x=[(269.5, 0.1), (741, 1), (1216, 10), (1695.5, 100)],
        yl=[(1474.5, 1), (998, 10), (526, 100), (52, 1000)],
        yr=[(1474.5, 0.1), (998, 1), (526, 10), (52, 100)],
        curves=[
            ('P-s (psi)', 'left', [(8, 1.94, None, None)]),
            ('P-r (psi)', 'left', [(8, 3.46, None, None)]),
            ('i-s/W^1/3 (psi-ms/lb^1/3)', 'left', [(8, 11.69, None, 67)]),  # curve ends at Z~66; ticks beyond
            ('i-r/W^1/3 (psi-ms/lb^1/3)', 'left', [(8, 18.81, None, None)]),
            ('t-o/W^1/3 (ms/lb^1/3) [right axis]', 'right', [(0.4, 8.088, None, None)]),
            ('L-w/W^1/3 (ft/lb^1/3) [right axis]', 'right', [(8, 5.819, None, None)]),
        ]),
}


# Figure 6-11 (batch 31 page 49): an example curve of four straight segments (shape as in
# Figure 6-13). Corner points measured from the embedded image (490 x 528 px; axes calibrated
# from the gridlines; 1 px = 0.026 deflection, 0.0018 resistance):
#   flexural peak 0.614 at ~0.04; drop to arching resistance 0.051 at ~0.08 (= 2 Xe);
#   straight line to zero at 7.61, i.e. the wall thickness h = 7.625 in of an 8-in masonry unit.
FIG_6_11 = [(0.0, 0.0), (0.04, 0.614), (0.08, 0.051), (7.625, 0.0)]


def trim_end_jumps(pts, max_step=0.012):
    """Drop points at either end that jump off the curve (frame corners, tick marks)."""
    def ok(a, b):
        return abs(math.log10(b[1] / a[1])) <= max_step
    while len(pts) > 3 and not ok(pts[-2], pts[-1]):
        pts = pts[:-1]
    while len(pts) > 3 and not ok(pts[0], pts[1]):
        pts = pts[1:]
    return pts


def thin(pts, n=120):
    """Keep about n points spaced evenly in log Z (enough to follow the curve)."""
    if len(pts) <= n:
        return pts
    lx0, lx1 = math.log10(pts[0][0]), math.log10(pts[-1][0])
    out, k = [], 0
    for i in range(n):
        target = lx0 + (lx1 - lx0) * i / (n - 1)
        while k < len(pts) - 1 and math.log10(pts[k][0]) < target:
            k += 1
        if not out or pts[k] != out[-1]:
            out.append(pts[k])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf-root', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--checks', required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    os.makedirs(a.checks, exist_ok=True)
    tmp = tempfile.mkdtemp()
    for fig, c in FIGURES.items():
        base = os.path.join(tmp, f'p{c["page"]}')
        subprocess.run(['pdftoppm', '-f', str(c['page']), '-l', str(c['page']), '-r', '300', '-gray', '-png',
                        '-singlefile', os.path.join(a.pdf_root, c['pdf']), base], check=True)
        chart_png = os.path.join(tmp, f'chart_{fig}.png')
        Image.open(base + '.png').crop(c['crop']).save(chart_png)
        ch = Chart(chart_png, c['x'], c['yl'], c['yr'], c['frame'])
        curves = []
        overlay = Image.open(chart_png).convert('RGB')
        draw = ImageDraw.Draw(overlay)
        colours = [(255, 0, 0), (200, 0, 200), (255, 140, 0), (0, 0, 255), (0, 160, 0), (0, 170, 170)]
        for (label, axis, segments), col in zip(c['curves'], colours):
            pts = []
            for sx, sy, zmin, zmax in segments:
                seg = ch.trace(sx, sy, axis=axis, x_min=zmin, x_max=zmax)
                pts += [p for p in seg if (zmin is None or p[0] >= zmin) and (zmax is None or p[0] <= zmax)]
            pts = trim_end_jumps(sorted(set(pts)))
            yax = ch.yl if axis == 'left' else ch.yr
            draw.line([(ch.x.to_pixel(x), yax.to_pixel(y)) for x, y in pts], fill=col, width=4)
            curves.append((label, thin(pts)))
            print(f'{fig} {label:40s} Z {pts[0][0]:.3g}..{pts[-1][0]:.3g}  value {pts[0][1]:.3g}..{pts[-1][1]:.3g}')
        write_grf(os.path.join(a.out, c['file']), curves, c['title'] + [NOTE])
        overlay.resize((overlay.width // 2, overlay.height // 2)).save(os.path.join(a.checks, f'fig_{fig}.png'))
    write_grf(os.path.join(a.out, '06_011.grf'), [('Resistance-deflection (example)', FIG_6_11)],
              ['Figure 6-11.  Resistance-deflection curve for unreinforced masonry wall with axial load arching',
               '(example; corner points Xe, 2Xe and h as in Figure 6-13)', 'Deflection', 'Resistance', NOTE])
    print('6-11 corner points', FIG_6_11)


if __name__ == '__main__':
    main()
