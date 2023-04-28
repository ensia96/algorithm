for l in [*open(0)][1:]:
    d, n, s, p = map(int, l.split())
    x, y = d+n*p, n*s
    print(['does not matter', (x > y)*"do not "+"parallelize"][(x > y)+(x < y)])
