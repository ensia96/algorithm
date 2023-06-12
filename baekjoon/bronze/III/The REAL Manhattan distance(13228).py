for l in [*open(0)][1:]:
    a, b, c, x, y, z = map(int, l.split())
    print(c+abs(a-x)+abs(b-y)+z)
