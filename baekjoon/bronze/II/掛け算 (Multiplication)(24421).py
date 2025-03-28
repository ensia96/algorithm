_, *A = map(int, open(0).read().split())
print(
    sum(
        A[i] * A[j] == A[k]
        for i in range(_)
        for j in range(i + 1, _)
        for k in range(j + 1, _)
    )
)
