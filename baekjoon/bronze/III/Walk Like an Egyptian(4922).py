for l in [*open(0)][:-1]:
    n = int(l)
    print(n, '=>', n*n-n+1)
