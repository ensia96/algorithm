for l in [*open(0)][1:]:
    k, n = map(int, l.split())
    print(k, n+sum(range(n+1)))
