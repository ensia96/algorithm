f = lambda: [*map(int, input().split())]
for i in range(*f()):
    A = [f()for _ in ' ' * f()[0]]
    X, Y = zip(*[A[b - 1]for b in f()])
    print(f"Data Set {i + 1}:\n{sum(min(X) <= a <= max(X) and min(Y) <= b <= max(Y)for a, b in A)}\n")Z
