for l in [*open(0)][:-1]:
    x, y = map(int, l.split())
    z = 0
    while x*y:
        x, a = divmod(x, 10)
        y, b = divmod(y, 10)
        z += a+b > 9
    print(z)
