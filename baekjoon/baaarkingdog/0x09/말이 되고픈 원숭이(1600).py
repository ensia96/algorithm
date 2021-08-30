import sys
i, r = sys.stdin.readline, range
k, l = int(i()), lambda: [*map(int, i().split())]
w, h = l()
m, q = [l() for _ in r(h)], [(0, 0, k)]
e, v = -1, [[[0 for ___ in r(k+1)] for __ in r(w)] for _ in r(h)]

for a, b, t in q:
    if (a, b) == (h-1, w-1):
        e = v[a][b][t]
        break
    for c, d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = a+c, b+d
        if 0 <= x < h and 0 <= y < w and not m[x][y] and not v[x][y][t]:
            v[x][y][t] = v[a][b][t] + 1
            q += [(x, y, t)]
    if t > 0:
        for c, d in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, 1), (2, -1)]:
            x, y = a+c, b+d
            if 0 <= x < h and 0 <= y < w and not m[x][y] and not v[x][y][t-1]:
                v[x][y][t-1] = v[a][b][t] + 1
                q += [(x, y, t-1)]

print(e)
