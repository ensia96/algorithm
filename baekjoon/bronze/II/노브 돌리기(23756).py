n, *A = map(int, open(0))
print(
    sum(
        min(abs(b - a - 360 * (a < b)), abs(a - b - 360 * (b < a)))
        for a, b in zip(A, A[1:])
    )
)
