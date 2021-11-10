import sys
I = sys.stdin.readline
L, R = lambda: map(int, I().split()), range
n, a = int(I()), [*L()]
D = [[0]*n for _ in R(n)]
for d in R(n):
    for s in R(n-d):
        e = s+d
        m = a[s] == a[e]
        D[s][e] = +(s == e) or (s+1 == e)*m or m*D[s+1][e-1]
for _ in R(int(I())):
    s, e = L()
    print(D[s-1][e-1])
