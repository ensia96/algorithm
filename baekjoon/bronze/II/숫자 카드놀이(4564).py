for l in [*open(0)][:-1]:
    l = l[:-1]
    A = [l]
    while len(l) > 1:
        x = 1
        for i in map(int, l):
            x *= i
        l = str(x)
        A += x,
    print(*A)
