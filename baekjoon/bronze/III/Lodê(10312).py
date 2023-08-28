for l in [*open(0)][1:]:
    n, t = int(l), ''
    while n:
        n, a = divmod(n, 3)
        t = str(a)+t
    print(' '.join(t))
