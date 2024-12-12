for l in [*open(0)][:-1]:
    a, b, c, d = map(int, l.split())
    print(f"{int(min(100,max(min(c/a*100,d/b*100),min(c/b*100,d/a*100))))}%")
