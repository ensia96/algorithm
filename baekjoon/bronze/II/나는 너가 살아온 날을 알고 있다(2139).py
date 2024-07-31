for l in [*open(0)][:-1]:
    d, m, y = map(int, l.split())
    print(
        sum(
            [
                31,
                28 + bool(not (y % 400) or (y % 100) and not (y % 4)),
                31,
                30,
                31,
                30,
                31,
                31,
                30,
                31,
                30,
                31,
            ][: m - 1]
        )
        + d
    )
