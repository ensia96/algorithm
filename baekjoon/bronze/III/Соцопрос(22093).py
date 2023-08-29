for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    print(max(0, b-c), min(a-c, b))
