for l in [*open(0)][:-1]:
    a, b, c, d = map(int, l.split())
    print(((a**b)**c)**d)
