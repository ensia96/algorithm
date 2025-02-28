for l in [*open(0)][:-1]:
    print(*["".join([i[0], *i[-2:0:-1]]) + (len(i) > 1) * i[-1] for i in l.split()])
