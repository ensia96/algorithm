for l in [*open(0)][:-1]:
    n = N = int(l)
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        N = max(N, n)
    print(N)
