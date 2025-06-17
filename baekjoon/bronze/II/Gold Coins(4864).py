for n in map(int, [*open(0)][:-1]):
    x = y = z = 0
    for i in range(n+1):
        x += y
        if y == z:
            y += 1
            z = 0
        z += 1
    print(n, x)
