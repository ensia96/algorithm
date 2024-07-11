f = lambda n, p: -(min(p, n + 1 - p) // -2)
for l in [*open(0)][:-1]:
    n, p = map(int, l.split())
    print(*[-~i for i in range(n) if f(n, p) == f(n, -~i) and -~i != p])
