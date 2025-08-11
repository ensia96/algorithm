for l in [*open(0)][1:]:
    k, b, n = map(int, l.split())
    S = 0
    while n:
        S += (n % b)**2
        n //= b
    print(k, S)
