f = lambda a, b: (a * a + b * b)
for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    print(min(f(a + b, c), f(a + c, b), f(b + c, a)))
