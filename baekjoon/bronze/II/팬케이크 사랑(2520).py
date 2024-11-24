_, *A = open(0)
for x, y in zip(A[1::3], A[2::3]):
    a, b, c, d, e = map(int, x.split())
    i, j, k, l = map(int, y.split())
    print(
        int(
            min(
                a // 0.5,
                b // 0.5,
                c // 0.25,
                d // 0.0625,
                e // 0.5625,
                i + j // 30 + k // 25 + l // 10,
            )
        )
    )
