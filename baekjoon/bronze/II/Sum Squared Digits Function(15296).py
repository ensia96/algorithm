for l in [*open(0)][1:]:
    k, b, n = map(int, l.split())
    S = 0
    while n > 0:
        n = n//b
        S += (n % b)**2
    print(k, S)
