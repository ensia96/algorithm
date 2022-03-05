L, R = lambda: map(int, input().split()), range
n, m, t = L()
N = R(n)
D = [[-1]*n for _ in N]
for _ in R(m):
    u, v, h = L()
    D[u-1][v-1] = h
for k in N:
    for i in N:
        for j in N:
            a, b, c = D[i][j], D[i][k], D[k][j]
            if b > 0 and c > 0:
                D[i][j] = min(a, max(b, c))
for _ in R(t):
    s, e = L()
    print(D[s-1][e-1])
