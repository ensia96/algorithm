for l in [*open(0)][:-1]:
    n, a, b, c = map(int, l.split())
    print(5*n-1+2*b-a-c+n*((a > b)-(b > c)))
