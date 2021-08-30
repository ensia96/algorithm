import sys
i, r = sys.stdin.readline, range

for _ in r(int(i())):
    w, h = map(int, i().split())
    m, v, f = [[*i().strip()] for _ in r(h)], [[0]*w for _ in r(h)], []
    o = 'IMPOSSIBLE'

    for a in r(h):
        for b in r(w):
            p = m[a][b]
            if p == '@':
                s = [(a, b)]
                m[a][b] = 0
            if p in '#*':
                m[a][b] = 0
                v[a][b] = 1
                if p == '*':
                    f += [(a, b)]

    for p, q in f:
        for x, y in [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]:
            if 0 <= x < h and 0 <= y < w and m[x][y] == '.':
                m[x][y] = m[p][q] + 1
                v[x][y] = 1
                f += [(x, y)]

    for p, q in s:
        for x, y in [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]:
            if 0 <= x < h and 0 <= y < w:
                e, g = m[p][q], m[x][y]
                if not v[x][y] and g == '.' or e + 1 < g:
                    v[x][y], m[x][y] = 1, e + 1
                    s += [(x, y)]
                continue
            o, s = m[p][q] + 1, []
            break

    print(o)
