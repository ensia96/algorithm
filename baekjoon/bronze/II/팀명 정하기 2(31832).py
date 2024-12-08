print(
    *[
        l
        for l in [*open(0)][1:]
        if sum(map(str.islower, l)) > len(l) / 2 - 1
        and len(l) < 12
        and sum(map(str.isnumeric, l)) < len(l) - 1
    ]
)
