for l in [*open(0)][1:]:
    n = int(l)
    print(max(i for i in range(n)if i*-~i <= n))
