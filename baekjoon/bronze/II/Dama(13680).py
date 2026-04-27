for l in [*open(0)][:-1]:
    a, b, c, d = map(int, l.split())
    x, y = a - c, b - d
    print((x * y * (x * x - y * y) != 0) + (x * x + y * y > 0))
