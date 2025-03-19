f = lambda: [*map(int, input().split())]
while (A := f())[0]:
    m, n, A = *A, f()
    print(
        sum(all(i >= j for i, j in zip(A, map(int, input().split()))) for _ in " " * n)
    )
