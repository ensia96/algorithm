I = lambda: [*map(int, input().split())]
for t in range(*I()):
    n, v = I()
    A = eval("I()," * (n + v))
    print(
        f"Data Set {t + 1}:\n{sum((A[a - 1][0] | c % 2) * A[a - 1][1] + (A[b - 1][0] | (c > 1)) * A[b - 1][1]for a, b, c in A[n:])}\n")
