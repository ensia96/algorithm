import sys
L, M = lambda: map(int, sys.stdin.readline().split()), 8**8
n, q = L()
N = range(1, n+1)
D = [[[0]*-~n for _ in ' '*-~n]for _ in ' '*-~n]
for i in N:
    l = [*L()]
    for j in N:
        D[0][i][j] = l[j-1]
        if not D[0][i][j] and i-j:
            D[0][i][j] = M
for k in N:
    for i in N:
        for j in N:
            D[k][i][j] = min(D[k-1][i][j], D[k-1][i][k]+D[k-1][k][j])
for _ in ' '*q:
    c, s, e = L()
    t = D[c-1][s][e]
    print(t if t-M else -1)
