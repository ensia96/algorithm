l, M = lambda: map(int, input().split()), 8**8
for _ in ' '*next(l()):
    n, m, k = l()
    E = [[]for _ in ' '*-~n]
    D = [[M]*-~m for _ in ' '*-~n]
    D[1][0] = 0
    for _ in ' '*k:
        u, v, c, d = l()
        E[u] += (v, c, d),
    for c in range(m+1):
        for d in range(1, n+1):
            if D[d][c]-M:
                t = D[d][c]
                for x, y, z in E[d]:
                    if y+c <= m:
                        D[x][y+c] = min(D[x][y+c], t+z)
    R = min(D[n])
    print(R if R-M else'Poor KCM')
