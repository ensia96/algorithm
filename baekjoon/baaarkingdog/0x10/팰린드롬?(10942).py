import sys
I = sys.stdin.readline
L, R = lambda: map(int, I().split()), range
n, a = int(I()), [*L()]
D = [[0]*n for _ in R(n)]
for d in R(n):
    for s in R(n-d):
        m = a[s] == a[s+d]
        D[s][s+d] = not d or (d == 1)*m or m*D[s+1][s+d-1]
for _ in R(int(I())):
    s, e = L()
    print(+D[s-1][e-1])
