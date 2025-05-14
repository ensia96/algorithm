for l in [*open(0)][1:]:
    a, b, c = l.split()
    a = int(a)
    for _ in ' '*int(b):
        c = c[a:]+c
    print(c)
