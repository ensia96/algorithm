for l in [*open(0)][:-1]:
    print("NY"[len({i[0] for i in l.lower().split()}) < 2])
