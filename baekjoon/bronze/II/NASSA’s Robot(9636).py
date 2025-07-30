for l in [*open(0)][1:]:
    l, r, u, d, t = map(l.count, 'LRUD?')
    print(r-l-t, u-d-t, r-l+t, u-d+t)
