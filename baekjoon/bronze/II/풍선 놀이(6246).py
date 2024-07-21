n, q, *A = map(int, open(0).read().split())
print(
    n - sum(any(i % A[2 * j + 1] + 1 == A[2 * j] for j in range(q)) for i in range(n))
)
