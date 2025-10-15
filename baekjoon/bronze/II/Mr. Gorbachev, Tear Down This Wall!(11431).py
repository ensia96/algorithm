P, f = print, lambda: [*map(int, input().split())]
for t in range(*f()):
    n, s, p = f()
    A = [(*f(),)for _ in ' ' * -~n]
    w = sum(abs(i[0] - j[0]) + abs(i[1] - j[1])for i, j in zip(A, A[1:]))
    P(f"Data Set {t + 1}:")
    P(int((w * s + p - 1) / p))
    P()
