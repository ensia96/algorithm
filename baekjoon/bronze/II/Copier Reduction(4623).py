for l in [*open(0)][:-1]:
    a, b, c, d = map(int, l.split())
    print(f"{int(min(1,max(min(c/a,d/b),min(c/b,d/a)))*100)}%")
