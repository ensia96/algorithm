L, M = lambda: map(int, input().split()), 8**8
n, m = L()
N = range(n)
D = [[M]*n for _ in N]
for _ in ' '*m:
    u, v, b = L()
    D[u-1][v-1] = 0
    D[v-1][u-1] = +(not b)
for k in N:
    D[k][k] = 0
    for i in N:
        for j in N:
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])
for _ in ' '*next(L()):
    s, e = L()
    print(D[s-1][e-1])
