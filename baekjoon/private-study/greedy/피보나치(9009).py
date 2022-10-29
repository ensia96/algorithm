for _ in ' '*int(input()):
    n, A = int(input()), []
    while n:
        a, b = 0, 1
        while a+b <= n:
            a, b = b, a+b
        n -= b
        A += b,
    print(*A[::-1])
