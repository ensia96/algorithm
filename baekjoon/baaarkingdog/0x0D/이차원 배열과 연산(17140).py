import collections as C
l, t, v, h, g = lambda: map(int, input().split()), 0, 3, 3, range
r, c, k = l()
b, r, c = [[*l(), *[0]*96]for _ in g(3)]+[[0]*99 for _ in g(96)], r-1, c-1
while t <= 100:
    if b[r][c] == k:
        exit(print(t))
    if v < h:
        for i in g(h):
            m = C.Counter([*filter(None, [b[j][i]
                          for j in range(v)])]).most_common()
            m.sort(key=lambda x: x[::-1])
            l = len(m)
            m = [p[a] for p in m for a in g(2)][:99] + [0]*(99-l)
            for j in g(99):
                b[j][i] = m[j]
            v = min(max(v, l*2), 99)
    else:
        for i in g(v):
            m = C.Counter([*filter(None, [b[i][j]
                          for j in range(h)])]).most_common()
            m.sort(key=lambda x: x[::-1])
            l = len(m)
            m = [p[a] for p in m for a in g(2)][:99] + [0]*(99-l)
            for j in g(99):
                b[i][j] = m[j]
            h = min(max(h, l*2), 99)
    t += 1
print(-1)
