for l in [*open(0)][1:]:
    l, r, s = map(int, l.split())
    print(min(r-s << 1, s-l << 1 | 1))
