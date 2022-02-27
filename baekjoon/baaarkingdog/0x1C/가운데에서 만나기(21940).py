L, D = lambda: map(int, input().split()), {}
M = 8**6
n, m = L()
N = range(n)
C = [[M]*n for _ in N]
for _ in ' '*m:
    a, b, t = L()
    C[a-1][b-1] = min(C[a-1][b-1], t)
k, A = next(L()), [i-1 for i in L()]
for k in N:
    for i in N:
        for j in N:
            C[i][j] = min(C[i][j], C[i][k]+C[k][j])
for i in N:
    C[i][i] = 0
for j in N:
    t = max(C[i][j]+C[j][i]for i in A)
    D[t] = D.get(t, [])+[j]
print(*sorted(i+1 for i in D[min(D)]))
