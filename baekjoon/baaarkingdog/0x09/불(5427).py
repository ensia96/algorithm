import sys
i, r = sys.stdin.readline, range

for _ in r(int(i())):
    w, h = map(int, i().split())
    m = [[*i().strip()] for _ in r(h)]
    f, o = [], 'IMPOSSIBLE'

    for a in r(h):
        for b in r(w):
            if m[a][b] == '@':
                s = [(a, b)]
                m[a][b] = 0
            if m[a][b] == '*':
                m[a][b] = 0
                f += [(a, b)]

    for p, q in f:
        for x, y in [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]:
            if 0 <= x < h and 0 <= y < w and m[x][y] == '.':
                m[x][y] = m[p][q] + 1
                f += [(x, y)]

    for p, q in s:
        for x, y in [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]:
            if 0 <= x < h and 0 <= y < w:
                u, v = m[p][q], m[x][y]
                if v == '.' or (v != '#' and u < v):
                    m[x][y] = u + 1
                    s += [(x, y)]
            else:
                o = m[p][q] + 1
                s = []
    print(o)
