L, M = lambda: map(int, input().split()), 8**8
n, m = L()
N = range(n)
D = [[M]*n for _ in N]
R = [[M]*n for _ in N]
for _ in ' '*m:
    a, b, c = L()
    a, b = a-1, b-1
    D[a][b] = D[b][a] = c
    R[a][b], R[b][a] = b, a
for k in N:
    for i in N:
        for j in N:
            t = D[i][k]+D[k][j]
            if D[i][j] > t:
                D[i][j], R[i][j] = t, R[i][k]
for i in N:
    print(*(R[i][j]+1 if i-j else'-'for j in N))
