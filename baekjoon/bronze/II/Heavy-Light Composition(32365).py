for *l, _ in [*open(0)][1:]:
    print("FT"[len({i % 2 ^ (l.count(x) > 1)for i, x in enumerate(l)}) < 2])
