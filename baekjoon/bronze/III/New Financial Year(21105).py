for l in [*open(0)][1:]:
    a, b = map(float, l.split())
    print(a/(b/100+1))
