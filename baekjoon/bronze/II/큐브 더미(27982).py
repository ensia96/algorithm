n, m, *A = map(int, open(0).read().split())
A = {*zip(A[::3], A[1::3], A[2::3])}
print(
    sum(
        {
            (a + 1, b, c),
            (a - 1, b, c),
            (a, b + 1, c),
            (a, b - 1, c),
            (a, b, c + 1),
            (a, b, c - 1),
        }
        - A
        == set()
        for a, b, c in A
    )
)
