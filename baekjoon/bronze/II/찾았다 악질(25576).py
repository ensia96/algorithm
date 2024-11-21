n, m, *A = map(int, open(0).read().split())
print(
    "YNEOS"[
        sum(2000 < sum(abs(A[j] - A[i * m + j]) for j in range(m)) for i in range(1, n))
        <= n / 2 :: 2
    ]
)
