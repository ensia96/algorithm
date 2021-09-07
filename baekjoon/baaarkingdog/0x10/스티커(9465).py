import sys
I, T = sys.stdin.readline, int
L, R = lambda: [*map(T, I().split())], range
for _ in R(T(I())):
    a = b = c = d = 0*T(I())
    for i, j in [*zip(L(), L())]:
        m, a, b = max(a, b), c, d
        c, d = max(m, d)+i, max(m, c)+j
    print(max(c, d))
