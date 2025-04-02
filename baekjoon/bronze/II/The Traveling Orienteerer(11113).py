n, *A = map(float, open(0).read().split())
n = 2 * int(n)
A, B = A[:n], [*map(int, A[n + 1 :])]
while B:
    m, *B = B
    x, *T = map(int, B[:m])
    S = 0
    for t in T:
        a, b = A[2 * x : 2 * x + 2]
        c, d = A[2 * t : 2 * t + 2]
        S += ((c - a) ** 2 + (d - b) ** 2) ** 0.5
        x = t
    print(int(S + 0.5))
    B = B[m:]
