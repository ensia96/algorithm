f = lambda a, b: b * (a < 1) or f(b % a, a)
for l in [*open(0)][:-1]:
    a, b = map(int, l.split())
    print(a * b // f(a, b) ** 2)
