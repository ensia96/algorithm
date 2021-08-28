import sys
i, r = sys.stdin.readline, range


def j(f):
    n = []
    for p, q in f:
        for x, y in [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]:
            if 0 <= x < h and 0 <= y < w and m[x][y] == '.':
                m[x][y] = m[p][q] + 1
                n += [(x, y)]
    f = []
    return n


def k(n, f):
    while n:
        f = j(f)
        s = n
        n = []
        for p, q in s:
            for x, y in [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]:
                e = m[p][q]
                if 0 <= x < h and 0 <= y < w:
                    g = m[x][y]
                    if g != '#' and (g == '.' or e + 1 < g):
                        m[x][y] = e + 1
                        n += [(x, y)]
                else:
                    return e + 1


for _ in r(int(i())):
    w, h = map(int, i().split())
    m, f = [[*i().strip()] for _ in r(h)], []
    c = d = 'IMPOSSIBLE'

    for a in r(h):
        for b in r(w):
            p = m[a][b]
            if p == '@':
                s = [(a, b)]
                m[a][b] = 0
            if p == '*':
                f += [(a, b)]
                m[a][b] = 0
    c = k(s, f)
    print(c if c else d)
