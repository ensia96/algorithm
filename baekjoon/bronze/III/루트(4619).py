for l in [*open(0)][:-1]:
    b, n = map(int, l.split())
    x, y, z = b-1, b, 1
    while x < y:
        z += 1
        y = x
        x = abs(b-z**n)
    print(z-1)
