a, b, c, d, e, f = map(int, open(0).read().split())
print(
    [
        [1, 2 * (b == f) * ((a < e < c) + (c < e < a))][b == d],
        2 * (a == e) * ((b < f < d) + (d < f < b)),
    ][a == c]
)
