a, b, c, d, e = map(int, open(0).read().split())
print(
    sum(
        sum(str(e) in i for i in map(str, divmod(i, 60)))
        for i in range(a * 60 + b, c * 60 + d)
    )
)
