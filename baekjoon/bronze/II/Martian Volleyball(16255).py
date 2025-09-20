for l in [*open(0)][1:]:
    k, *I = map(int, l.split())
    print(max(min(I) + 2, k) - max(I))
