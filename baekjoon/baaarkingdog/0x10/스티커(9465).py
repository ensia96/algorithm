import sys
I, R, T = sys.stdin.readline, range, int
for _ in R(T(I())):
    n, s = T(I()), [*zip(*[[*map(T, I().split())]for _ in R(2)])]
    d = [[0]*2 for _ in R(n+2)]
    for i in R(n):
        m = max(d[i-2])
        d[i][0] = max(m, d[i-1][1])+s[i][0]
        d[i][1] = max(m, d[i-1][0])+s[i][1]
    print(max(d[-3]))
