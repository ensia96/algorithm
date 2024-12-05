A = B = 9
C = D = -9
for l in [*open(0)][1:]:
    a, b, c, d = map(int, l.split())
    C = max(C, c)
    A = min(A, a)
    D = max(D, d)
    B = min(B, b)
    print(C - A + D - B << 1)
