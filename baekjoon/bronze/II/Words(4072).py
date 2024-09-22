for l in [*open(0)][:-1]:
    print(*[i[::-1] for i in l.split()])
