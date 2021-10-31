import sys
I, R, T = sys.stdin.readline, range, int
for _ in R(T(I())):
    n, s = T(I()), [*zip(*[[*map(T, I().split())]for _ in R(2)])]
    a = b = c = d = 0
    for i in R(n):
        m, a, b = max(a, b), c, d
        c, d = max(m, d)+s[i][0], max(m, c)+s[i][1]
    print(max(c, d))
