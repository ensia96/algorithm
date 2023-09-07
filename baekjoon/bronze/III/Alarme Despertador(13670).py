for l in [*open(0)][:-1]:
    a, b, c, d = map(int, l.split())
    x = 60*(c-a)+d-b
    print([x, 1440+x][x < 0])
