for l in [*open(0)][1:]:
    l = l.strip() * (2 - (len(l) % 2))
    print(l[::2])
    print(l[1::2])
