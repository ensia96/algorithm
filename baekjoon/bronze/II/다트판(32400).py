print(
    ["Tie", "Bob", "Alice"][
        (
            (x := sum((A := [*map(int, input().split())])) / 20)
            > (y := (A[1] + A[0] + A[-1]) / 3)
        )
        + 2 * (x < y)
    ]
)
