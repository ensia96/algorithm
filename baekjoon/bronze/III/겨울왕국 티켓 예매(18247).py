for l in [*open(0)][1:]:
    n, m = map(int, l.split())
    print(-(n < 12 or m < 4) or m*11+4)
