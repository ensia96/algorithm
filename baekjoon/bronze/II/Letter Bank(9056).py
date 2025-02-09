for l in [*open(0)][1:]:
    a, b = map(set, l.split())
    print("YNEOS"[a != b :: 2])
