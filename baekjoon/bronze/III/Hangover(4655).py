for l in [*open(0)][:-1]:
    n, x, y, z = float(l), 0, 2, 0
    while n > x:
        x += 1/y
        y += 1
    print(y-2, 'card(s)')
