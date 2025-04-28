for l in [*open(0)][1:]:
    x, y, a, b = map(int, l.split())
    t, r = divmod(y-x, a+b)
    print(-bool(r) or t)
