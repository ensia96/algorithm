import sys
i, r = sys.stdin.readline, range
k, l = int(i()), lambda: [*map(int, i().split())]
w, h = l()
m, q = [l() for _ in r(h)], [(0, 0, 0, 0)]
v = [[300 for __ in r(w)] for _ in r(h)]

for a, b, c, t in q:
    for p, d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = a+p, b+d
        if 0 <= x < h and 0 <= y < w and not m[x][y] and c+1 < v[x][y]:
            v[x][y] = c+1
            q += [(x, y, c+1, t)]
    if t < k:
        for p, d in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            x, y = a+p, b+d
            if 0 <= x < h and 0 <= y < w and not m[x][y] and c+1 < v[x][y]:
                v[x][y] = c+1
                q += [(x, y, c+1, t+1)]
a = v[w - 1][h - 1]
print(a if a != 300 else -1)
