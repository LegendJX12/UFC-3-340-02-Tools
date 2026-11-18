"""Digitize curves from a scanned log-log chart (the WebPlotDigitizer method, scripted).

1. Calibrate axes with reference points: pixel position -> value, piecewise in log
   space between the plot frame and the decade tick marks found on the frame.
2. Trace each curve column by column from a seed point, in both directions. In each
   column the dark pixel nearest the predicted position (linear extrapolation of the
   last points) is taken, and the centre of its local stroke is used. A curve ends
   after a run of columns with no dark pixel near the prediction.
"""
import math
import numpy as np
from PIL import Image


class Axis:
    """Piecewise log calibration from (pixel, value) reference points."""
    def __init__(self, refs):
        self.refs = sorted(refs)

    def to_value(self, px):
        r = self.refs
        for (p0, v0), (p1, v1) in zip(r, r[1:]):
            if px <= p1 or (p1, v1) == r[-1]:
                f = (px - p0) / (p1 - p0)
                return 10 ** (math.log10(v0) + f * (math.log10(v1) - math.log10(v0)))

    def to_pixel(self, val):
        r = sorted(self.refs, key=lambda t: t[1])
        lv = math.log10(val)
        for (p0, v0), (p1, v1) in zip(r, r[1:]):
            if val <= v1 or (p1, v1) == r[-1]:
                f = (lv - math.log10(v0)) / (math.log10(v1) - math.log10(v0))
                return p0 + f * (p1 - p0)


class Chart:
    def __init__(self, path, xrefs, yrefs_left, yrefs_right, frame, threshold=128, frame_margin=7):
        self.img = np.array(Image.open(path).convert('L')) < threshold
        x0, y1, x2, y2 = frame  # left, top, right, bottom pixel of the frame lines
        m = frame_margin
        self.img[:, :int(x0) + m] = False
        self.img[:, int(x2) - m + 1:] = False
        self.img[:int(y1) + m, :] = False
        self.img[int(y2) - m + 1:, :] = False
        self.x = Axis(xrefs)
        self.yl = Axis(yrefs_left)
        self.yr = Axis(yrefs_right)

    def runs(self, col):
        ys = np.nonzero(self.img[:, col])[0]
        out = []
        for y in ys:
            if out and y - out[-1][1] <= 1:
                out[-1][1] = y
            else:
                out.append([y, y])
        return out

    def trace(self, seed_x, seed_y, axis='left', tol=12, seed_tol=40, max_gap=25, stroke=6,
              x_min=None, x_max=None, step=1, window=25, thick_max=12):
        """Trace one curve from a seed (data units). Returns sorted [(x, y)] in data units."""
        yax = self.yl if axis == 'left' else self.yr
        c0 = int(round(self.x.to_pixel(seed_x)))
        r0 = yax.to_pixel(seed_y)
        lo = int(round(self.x.to_pixel(x_min))) if x_min else 0
        hi = int(round(self.x.to_pixel(x_max))) if x_max else self.img.shape[1] - 1
        pts = {}

        def centre(col, pred, t):
            ys = np.nonzero(self.img[:, col])[0]
            if len(ys) == 0:
                return None
            near = ys[np.argmin(np.abs(ys - pred))]
            if abs(near - pred) > t:
                return None
            band = ys[(ys >= near - stroke) & (ys <= near + stroke)]
            # keep the contiguous part around 'near'
            seg = [near]
            for y in sorted(band[band > near]):
                if y - seg[-1] <= 1:
                    seg.append(y)
                else:
                    break
            lower = [near]
            for y in sorted(band[band < near], reverse=True):
                if lower[-1] - y <= 1:
                    lower.append(y)
                else:
                    break
            seg = lower[1:] + seg
            if max(seg) - min(seg) + 1 > thick_max and min(seg) - 2 <= pred <= max(seg) + 2:
                return pred  # curves overlap here: keep the predicted path through the overlap
            return (min(seg) + max(seg)) / 2.0

        start = centre(c0, r0, seed_tol)
        if start is None:
            raise ValueError(f'no curve near seed {seed_x}, {seed_y}')
        pts[c0] = start
        for direction in (1, -1):
            hist = [(c0, start)]
            gap = 0
            col = c0 + direction * step
            while lo <= col <= hi:
                if len(hist) >= 2:
                    (ca, ya), (cb, yb) = hist[-min(len(hist), window)], hist[-1]
                    slope = (yb - ya) / (cb - ca) if cb != ca else 0.0
                    pred = yb + slope * (col - cb)
                else:
                    pred = hist[-1][1]
                y = centre(col, pred, tol + min(gap, 5))
                if y is None:
                    gap += 1
                    if gap > max_gap:
                        break
                else:
                    gap = 0
                    hist.append((col, y))
                    pts[col] = y
                col += direction * step
        out = sorted((self.x.to_value(c), yax.to_value(r)) for c, r in pts.items())
        return out
