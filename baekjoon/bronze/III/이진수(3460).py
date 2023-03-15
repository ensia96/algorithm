for _ in ' '*int(input()):
    n, i, A = int(input()), 0, []
    while n:
        n, x = divmod(n, 2)
        A += [i]*x
        i += 1
    print(*A)
