for l in [*open(0)][:-1]:
    x, *L = l.split()
    a, b, c = map(int, L)
    t = a > 31 or a > 30 and b > 4
    print([x, '?'][t], a-30*t, b, c)
