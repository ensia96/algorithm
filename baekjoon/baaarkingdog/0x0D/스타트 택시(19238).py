l, r = lambda: map(int, input().split()), range
n, m, k = l()
b, y, x = [[*l()]for _ in r(n)], *l()
y, x, p, g = y-1, x-1, [0]*n*n, [0]*(m+1)
e, c = lambda h, w: (0 <= h < n)*(0 <= w < n) and not b[h][w]+v[h*n+w], 0
o, f = lambda i, j: [(i+1, j), (i-1, j), (i, j+1), (i, j-1)], 0
for i in r(m):
    s, t, u, v = l()
    p[(s-1)*n+t-1], g[i+1] = i+1, (u-1, v-1)
while k >= 0:
    k += 2*c*f
    if not any(p):
        exit(print(k))
    q, v, t, c, f = [(0, y, x)], [0]*n*n, [], 0, 0
    if not p[y*n+x]:
        for d, i, j in q:
            for h, w in o(i, j):
                if e(h, w):
                    v[h*n+w], t = 1, [t+[(d+1, h, w)], t][not p[h*n+w]]
                    q += [(d+1, h, w)]
        if not t:
            break
        c, y, x = sorted(t)[0]
    k, c, p[y*n+x], z, q, v = k-c, 0, 0, g[p[y*n+x]], [(0, y, x)], [0]*n*n
    for d, i, j in q:
        for h, w in o(i, j):
            if e(h, w):
                f, c, v[h*n+w] = *[((h, w) == z, d+1), (f, c)][f], 1
                q += [(d+1, h, w)]
    if not f:
        break
    y, x, k = *z, k-c
print(-1)
