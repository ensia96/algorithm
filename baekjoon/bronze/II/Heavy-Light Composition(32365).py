for *l, _ in [*open(0)][1:]:
    c = l.count
    print('FT'[all((c(a) > 1) ^ (c(b) > 1)for a, b in zip(l, l[1:]))])
