import sys
I = sys.stdin.readline
L, M = lambda: map(int, I().split()), 8**8
n, q = L()
N = range(1, n+1)
D = [[[0]*-~n for _ in ' '*-~n]for _ in ' '*-~n]
for i in N:
    l = [*L()]
    for j in N:
        D[i][j][0] = l[j-1]
        if not D[i][j][0] and i-j:
            D[i][j][0] = M
for k in N:
    for i in N:
        for j in N:
            D[i][j][k] = min(D[i][j][k-1], D[i][k][k-1]+D[k][j][k-1])
for _ in ' '*q:
    c, s, e = L()
    t = D[s][e][c-1]
    print(t if t-M else -1)
