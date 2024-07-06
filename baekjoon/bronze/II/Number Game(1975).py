f = lambda x, y: (not x % y) and 1 + f(x // y, y)
for i in [*open(0)][1:]:
    n = int(i)
    print(sum(f(n, -~i) for i in range(1, 1000)))
