for l in [*open(0)][1:]:
    x, y, a, b = map(int, l.split())
    t = 0
    while x < y:
        x += a
        y -= b
        t += 1
    print(-(x != y) or t)
