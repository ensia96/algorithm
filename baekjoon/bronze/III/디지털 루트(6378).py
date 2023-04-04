for l in open(0):
    n, x = int(l), 0
    while n > 9:
        while n > 0:
            n, y = divmod(n, 10)
            x += y
        n, x = x, 0
    n and print(n)
