"""Reader for DPLOT v1.6 plot files (.grf) used by UFC 3-340-02.

Two layouts exist:
  data - each curve: point count, then one "x,y" pair per line
  dx   - each curve: point count, then y values (comma separated, several per line),
         then "x_first,x_last" (points are evenly spaced between them)
Each curve ends with a style line (e.g. " 1    0"), then its legend label, then a blank line.
After the last curve come title and axis text, then display settings (e.g. "1000Separators").
"""
import re

STYLE_RE = re.compile(r'^\s*-?\d+\s+-?\d+\s*$')
SETTINGS_START = {'1000Separators', 'MinorGridLines', 'ColorsEx', 'GridLineType'}


class GrfError(ValueError):
    pass


def _starts_curve(lines, i, fmt):
    """True if lines[i] is a point count followed by curve data."""
    if i + 1 >= len(lines) or not re.fullmatch(r'\s*\d+\s*', lines[i]):
        return False
    n = int(lines[i])
    nxt = lines[i + 1].strip()
    num = r'-?[\d.]+(?:[eE][-+]?\d+)?'
    if fmt == 'data':
        return bool(re.fullmatch(num + r'\s*,\s*' + num, nxt))
    if n > 1:
        return bool(re.fullmatch(num + r'(\s*,\s*' + num + r')+', nxt))
    return bool(re.fullmatch(num, nxt))


def parse_grf(text):
    lines = text.replace('\r', '').split('\n')
    if not lines or not lines[0].startswith('DPLOT'):
        raise GrfError('not a DPLOT file')
    fmt = lines[1].strip().lower()
    if fmt not in ('data', 'dx'):
        raise GrfError(f'unknown layout {fmt!r}')
    n_curves = int(lines[2].strip())
    i = 3
    curves = []
    for c in range(n_curves):
        while i < len(lines) and not lines[i].strip():
            i += 1
        n = int(lines[i].strip())
        i += 1
        if fmt == 'data':
            pts = []
            while len(pts) < n:
                x, y = lines[i].split(',')[:2]
                pts.append((float(x), float(y)))
                i += 1
        else:
            ys = []
            while len(ys) < n:
                ys += [float(v) for v in lines[i].split(',') if v.strip()]
                i += 1
            x0, x1 = [float(v) for v in lines[i].split(',')[:2]]
            i += 1
            step = (x1 - x0) / (n - 1) if n > 1 else 0.0
            pts = [(x0 + k * step, y) for k, y in enumerate(ys[:n])]
        if not STYLE_RE.match(lines[i]):
            raise GrfError(f'curve {c + 1}: style line expected at line {i + 1}, got {lines[i]!r}')
        i += 1
        # label: all non-empty lines up to the next curve's point count (one or two lines);
        # for the last curve, the first non-empty line
        if c < n_curves - 1:
            k = i
            while k < len(lines) and not _starts_curve(lines, k, fmt):
                k += 1
            while k + 1 < len(lines) and _starts_curve(lines, k + 1, fmt):
                k += 1  # a numeric label (e.g. "1") followed by the real count
            label = ' / '.join(x.strip() for x in lines[i:k] if x.strip())
            i = k
        else:
            while i < len(lines) and not lines[i].strip():
                i += 1
            label = lines[i].strip() if i < len(lines) else ''
            i += 1
        curves.append({'label': label, 'points': pts})
    text_lines = []
    while i < len(lines) and lines[i].strip() not in SETTINGS_START:
        if lines[i].strip():
            text_lines.append(lines[i].strip())
        i += 1
    return {'layout': fmt, 'curves': curves, 'text': text_lines}
