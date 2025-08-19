for l in [*open(0)][:-1]:
    n, a, b, c = map(int, l.split())
    print(4*n-1+(b-a) % n+(b-c) % n)
