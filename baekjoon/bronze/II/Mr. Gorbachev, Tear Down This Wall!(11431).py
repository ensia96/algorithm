f = lambda: [*map(int, input().split())]
for t in range(*f()):
    n, s, p = f()
    A = [(*f(),)for _ in ' ' * -~n]
    print(
        f"Data Set {t + 1}:\n{int((sum(abs(a - c) + abs(b - d)for (a, b), (c, d) in zip(A, A[1:])) * s + p - 1) / p)}\n")
