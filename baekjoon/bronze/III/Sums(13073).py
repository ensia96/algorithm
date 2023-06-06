for l in [*open(0)][1:]:
    n = int(l)
    print((n*n+n)//2, sum(range(1, 2*n+1, 2)), sum(range(2, 2*n+1, 2)))
