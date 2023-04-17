for l in [*open(0)][:-1]:
    a, b = map(int, l.split())
    print(2*a-b)
