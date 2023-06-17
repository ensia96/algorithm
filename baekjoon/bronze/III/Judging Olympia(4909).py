for l in [*open(0)][:-1]:
    x = sum(sorted(map(int, l.split()))[1:-1])
    print(x/4 if x % 4 else int(x/4))
