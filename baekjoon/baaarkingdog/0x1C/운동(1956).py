L, M = lambda: map(int, input().split()), 8**8
v, e = L()
V = range(v)
D = [[M]*v for _ in V]
for _ in ' '*e:
    a, b, c = L()
    D[a-1][b-1] = c
for k in V:
    for i in V:
        for j in V:
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])
A = min(D[i][i]for i in V)
print(-1 if A == M else A)
