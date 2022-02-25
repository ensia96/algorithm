L, M = lambda: map(int, input().split()), 8**8
n, m = L()
N = range(n)
D = [[M]*n for _ in N]
R = [[0]*n for _ in N]
E = []
for i in N:
    D[i][i] = 0
for _ in ' '*m:
    s, e, l = L()
    s, e = s-1, e-1
    D[s][e] = D[e][s] = min(D[s][e], l)
    E += [(s, e, l)]
for k in N:
    for i in N:
        for j in N:
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])
for i in N:
    a = 0
    for s, e, l in E:
        a = max(a, D[i][s]+D[i][e]+l)
    M = min(M, a)
print(M/2)
