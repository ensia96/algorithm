import collections as C
l, t, v, h, g = lambda: map(int, input().split()), 0, 3, 3, range
r, c, k = l()
b, r, c = [[*l(), *[0]*96]for _ in g(3)]+[[0]*99 for _ in g(96)], r-1, c-1
while t <= 100:
    if b[r][c] == k:
        exit(print(t))
    if v < h:
        for i in g(h):
            m = sorted(C.Counter([*filter(None, [b[j][i] for j in range(v)])]
                                 ).most_common(), key=lambda x: (x[1], x[0]))[:50]
            p = len(m)
            m += [(0, 0)]*(50-len(m))
            for j in g(49):
                b[2*j][i], b[2*j+1][i] = m[j][0], m[j][1]
            b[98][i] = m[49][0]
            v = min(max(v, p*2), 99)
    else:
        for i in g(v):
            m = sorted(C.Counter([*filter(None, [b[i][j] for j in range(h)])]
                                 ).most_common(), key=lambda x: (x[1], x[0]))[:50]
            p = len(m)
            m += [(0, 0)]*(50-len(m))
            for j in g(49):
                b[i][2*j], b[i][2*j+1] = m[j][0], m[j][1]
            b[i][98] = m[49][0]
            h = min(max(h, p*2), 99)
    t += 1
print(-1)
