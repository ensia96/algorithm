r, f = range, lambda: map(int, input().split())
for t in r(*f()):
    n, *_ = f()
    A = [[*f()]for _ in ' ' * n]
    T = []
    for i in r(n):
        for j in r(i, n):
            a, b, c = A[i]
            x, y, z = A[j]
            T += (((a - x)**2 + (b - y)**2 + (c - z)**2), i + 1, j + 1),
    print(f"Data Set {t + 1}:")
    T = sorted(T)
    for t in T:
        if t[0] == T[-1][0]:
            print(*t[1:])
