for l in [*open(0)][:-1]:
    a, b, c = map(int, l.split())
    x = ((c-a)/b)
    print([int(x)+1, 'X'][x % 1 > 0])
