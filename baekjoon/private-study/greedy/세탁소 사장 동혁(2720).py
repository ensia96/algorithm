for _ in ' '*int(input()):
    c = int(input())
    A = []
    for i in [25, 10, 5, 1]:
        x, c = divmod(c, i)
        A += x,
    print(*A)
