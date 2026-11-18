"""Find variable names in OCR LaTeX with their character positions, so a single wrong letter
or a missing prime can be fixed in place.

A name is a base letter plus the letters of its subscript, e.g. f_{d y} -> "fdy",
\\boldsymbol{f}_{dv} -> "fdv", plus plain words such as \\mathrm{Ibs} -> "Ibs".
Each name keeps the positions of its letters in the LaTeX string.
"""
import re

CMD = re.compile(r'\\[a-zA-Z]+')
TEXT_CMDS = ('mathrm', 'text', 'textrm', 'mathit', 'operatorname')


def _match_brace(s, i):
    """s[i] == '{' -> index of the matching '}' (or len(s)-1)."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == '{':
            depth += 1
        elif s[j] == '}':
            depth -= 1
            if depth == 0:
                return j
    return len(s) - 1


def _letters(s, a, b):
    """Positions of letters in s[a:b] that are not part of a LaTeX command."""
    pos, i = [], a
    while i < b:
        m = CMD.match(s, i)
        if m and m.end() <= b:
            i = m.end()
            continue
        if s[i].isascii() and s[i].isalpha():
            pos.append(i)
        i += 1
    return pos


def names(s):
    """List of dicts: name, positions (one per letter), primed (bool), end (index after name)."""
    out, i, n = [], 0, len(s)
    used = set()
    while i < n:
        m = CMD.match(s, i)
        if m:
            cmd = m.group(0)[1:]
            if cmd in TEXT_CMDS and m.end() < n and s[m.end()] == '{':
                j = _match_brace(s, m.end())
                for w in re.finditer(r'[A-Za-z]+', s[m.end() + 1:j]):
                    p = [m.end() + 1 + w.start() + k for k in range(len(w.group(0)))]
                    if len(p) >= 2:
                        out.append({'name': w.group(0), 'pos': p, 'primed': False, 'end': p[-1] + 1})
                    used.update(p)
                i = j + 1
                continue
            i = m.end()
            continue
        if s[i].isascii() and s[i].isalpha() and i not in used:
            base = i
            k = i + 1
            while k < n and s[k] in ' }':       # e.g. \boldsymbol{f}_
                k += 1
            primed = False
            pm = re.match(r"\s*(\^\s*\{?\s*(\\prime|')\s*\}?|')", s[k:])
            if pm:
                primed = True
                k += pm.end()
                while k < n and s[k] in ' }':
                    k += 1
            if k < n and s[k] == '_':
                k += 1
                while k < n and s[k] == ' ':
                    k += 1
                if k < n and s[k] == '{':
                    j = _match_brace(s, k)
                    sub = _letters(s, k + 1, j)
                    end = j + 1
                else:
                    sub = [k] if k < n and s[k].isascii() and s[k].isalpha() else []
                    end = k + 1
                pm2 = re.match(r"\s*(\^\s*\{?\s*(\\prime|')\s*\}?|')", s[end:])
                if pm2:
                    primed = True
                    end += pm2.end()
                pos = [base] + sub
                out.append({'name': ''.join(s[p] for p in pos), 'pos': pos, 'primed': primed, 'end': end})
                used.update(pos)
                i = end
                continue
            # plain run of letters (a word typed without a command)
            w = re.match(r'[A-Za-z]+', s[i:])
            p = list(range(i, i + w.end()))
            out.append({'name': w.group(0), 'pos': p, 'primed': primed, 'end': p[-1] + 1})
            used.update(p)
            i = p[-1] + 1
            continue
        i += 1
    return out


def replace_letter(s, pos, new):
    return s[:pos] + new + s[pos + 1:]


def add_prime(s, nm):
    """Insert ^{\\prime} after the base letter of name nm (before its subscript)."""
    b = nm['pos'][0]
    k = b + 1
    while k < len(s) and s[k] == '}':
        k += 1
    return s[:k] + '^{\\prime}' + s[k:]
