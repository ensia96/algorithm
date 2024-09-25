for l in open(0):
    m, p, l, e, r, s, n = map(int, l.split())
    for _ in " " * n:
        x = p // s
        y = l // r
        z = e * m
        m, p, l = x, y, z
    print(m)
