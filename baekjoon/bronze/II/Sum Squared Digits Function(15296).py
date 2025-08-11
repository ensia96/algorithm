for l in [*open(0)][1:]:
    k, b, n = map(int, l.split())
    S = 0
    while n > 0:
        n, a = divmod(n, b)
        S += a*a
    print(k, S)
