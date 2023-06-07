for l in [*open(0)][1:]:
    n = int(l)
    print(sum((n-i)**2 for i in range(n+1)))
