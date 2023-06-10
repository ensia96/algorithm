for l in [*open(0)][:-1]:
    c, d = map(int, l.split())
    print(min(30*c+40*d, 35*c+30*d, 40*c+20*d))
