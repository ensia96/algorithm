n, *L = open(0)
A, B, C, D = 10, 10, -10, -10
for l in L:
    a, b, c, d = map(int, l.split())
    A, B, C, D = min(A, a), min(B, b), max(C, c), max(D, d)
    print(2 * (abs(C - A) + abs(D - B)))
