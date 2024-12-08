print(
    *[
        l
        for l in [*map(str.strip, open(0))][1:]
        if sum(map(str.islower, l)) > sum(map(str.isupper, l))
        and 11 > len(l)
        and sum(map(str.isnumeric, l)) < len(l)
    ]
)
