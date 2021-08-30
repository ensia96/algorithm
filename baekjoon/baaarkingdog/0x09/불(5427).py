import sys
i, r = sys.stdin.readline, range


def g(s, f):
    a = []
    f = e(f)
    for p, q in s:
        for x, y in [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]:
            if 0 <= x < h and 0 <= y < w:
                if not v[x][y]:
                    v[x][y] = 1
                    m[x][y] = m[p][q] + 1
                    a += [(x, y)]
            else:
                return m[p][q] + 1
    if a:
        return g(a, f)


def e(f):
    a = []
    for p, q in f:
        for x, y in [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]:
            if 0 <= x < h and 0 <= y < w and m[x][y] == '.':
                v[x][y] = 1
                a += [(x, y)]
    return a


for _ in r(int(i())):
    w, h = map(int, i().split())
    m, v = [[*i().strip()] for _ in r(h)], [[0] * w for _ in r(h)]
    f = []

    for a in r(h):
        for b in r(w):
            if m[a][b] == '@':
                s = [(a, b)]
                m[a][b] = 0
            if m[a][b] == '*':
                v[a][b] = 1
                f += [(a, b)]
            if m[a][b] == '#':
                v[a][b] = 1

    o = g(s, f)
    print(o if o else 'IMPOSSIBLE')
