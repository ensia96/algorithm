for l in [*open(0)][:-1]:
    *L, = map(int, l.strip())
    x = y = 1
    z = 0
    while L:
        y *= x
        z += L.pop()*y
        x += 1
    print(z)
