l, r = lambda: map(int, input().split()), range
h, c, o, n, m = lambda i, j: (0 <= i < n)*(0 <= j < m), 0, set(), *l()
b, v, Q, g, a = [[*l()]for _ in r(n)], [[0]*m for _ in r(n)], [], [], 0
for p in r(n*m):
    y, x = p//m, p % m
    if (not b[y][x])+v[y][x]:
        continue
    c, q, v[y][x] = c+1, [(y, x)], c+1
    for y, x in q:
        for i, j in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if h(i, j) and b[i][j]*(not v[i][j]):
                v[i][j] = c
                q += [(i, j)]
    Q += [q]
F, P = lambda i: F(P[i]) if P[i] != i else P[i], {i: i for i in r(c)}
for q in Q:
    for Y, X in q:
        for D in r(4):
            p, C = [(Y, X, 0)], v[Y][X]
            for y, x, d in p:
                i, j = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)][D]
                if h(i, j) and v[i][j] != C:
                    if v[i][j]:
                        if d >= 2:
                            g += [(d, C-1, v[i][j]-1)]
                    else:
                        p += [(i, j, d+1)]
for d, i, j in sorted(g):
    if F(i) != F(j):
        p1, p2 = F(i), F(j)
        P[p1], P[p2] = [(P[p1], p1), (p2, P[p2])][p1 > p2]
        a += d
print(-1 if len({F(i) for i in range(c)})-1 else a)
