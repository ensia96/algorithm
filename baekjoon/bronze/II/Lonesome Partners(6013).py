n, *A = map(int, open(0).read().split())
print(
    *max(
        (abs(A[i * 2] - A[j * 2]) + abs(A[i * 2 + 1] - A[j * 2 + 1]), i + 1, j + 1)
        for i in range(n)
        for j in range(i, n)
    )[1:]
)
