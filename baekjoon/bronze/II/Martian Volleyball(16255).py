for l in [*open(0)][1:]:
    k, x, y = map(int, l.split())
    if x > y:
        x, y = y, x
    print(max(2 - y + x, k - y))
