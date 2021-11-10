import sys
i = sys.stdin.readline
I, L, R = lambda: int(i()), lambda: map(int, i().split()), range
n, a = I(), [*L()]
D = [[0]*n for _ in R(n)]
for i in R(n):
    c = d = ()
    for j in R(i, n):
        c, d = (*c, a[j]), (a[j], *d)
        D[i][j] = 1*(c == d)
for _ in R(I()):
    s, e = L()
    print(D[s-1][e-1])
