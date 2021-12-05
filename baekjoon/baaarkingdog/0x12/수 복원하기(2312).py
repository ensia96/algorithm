for _ in ' '*int(input()):
    n, t = int(input()), 2
    while n > 1:
        c = 0
        while not n % t:
            n, c = n//t, c+1
        c and print(t, c)
        t += 1
