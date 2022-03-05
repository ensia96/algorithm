L, M, R = lambda: map(int, input().split()), 8**8, range
n, m, t = L()
N = R(n)
D = [[M]*n for _ in N]
for _ in R(m):
    u, v, h = L()
    D[u-1][v-1] = h
for k in N:
    for i in N:
        for j in N:
            D[i][j] = min(D[i][j], max(D[i][k], D[k][j]))
for _ in R(t):
    s, e = L()
    t = D[s-1][e-1]
    print(t if t-M else -1)
