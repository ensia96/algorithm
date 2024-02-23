f, t = lambda a, b: b*(a == 0) or f(b % a, a), 0
n, *A = map(int, open(0).read().split())
for a, b in zip(A[::2], A[1::2]):
    g = f(a, b)
    print(a*b//g, g)
