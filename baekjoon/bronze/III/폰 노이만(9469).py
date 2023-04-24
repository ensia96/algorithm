for l in [*open(0)][1:]:
    n, *A = l.split()
    d, a, b, f = map(float, A)
    print(n, f'{d/(a+b)*f:.6f}')
