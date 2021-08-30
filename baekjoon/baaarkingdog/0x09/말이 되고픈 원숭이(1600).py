import sys
i = sys.stdin.readline
k, l = int(i()), lambda: [*map(int, i().split())]
w, h = l()
m, r, q = [l() for _ in range(h)], -1, [(0, 0, 0)]
v = [[[0] * (k+1) for __ in range(w)] for _ in range(h)]

for a, b, t in q:
    print()
    for z in v:
        print(z)
    print()
    if r != -1:
        break
    for c, d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = a + c, b + d
        if 0 <= x < h and 0 <= y < w and not m[x][y] and not v[x][y][t]:
            if (x, y) == (h-1, w-1):
                r = v[a][b][t] + 1
                break
            v[x][y][t] = v[a][b][t] + 1
            q += [(x, y, t)]
    if t < k:
        for c, d in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            x, y = a + c, b + d
            if 0 <= x < h and 0 <= y < w and not m[x][y] and not v[x][y][t]:
                if (x, y) == (h-1, w-1):
                    r = v[a][b][t] + 1
                    break
                v[x][y][t + 1] = v[a][b][t] + 1
                q += [(x, y, t+1)]
print(r)
