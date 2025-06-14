for l in [*open(0)][:-1]:
    x = y = 0
    z = []
    for a in [*map(int, l.split())][1:]:
        x += 1
        z += [x]*(a-y)
        y = a
    print(*z)
