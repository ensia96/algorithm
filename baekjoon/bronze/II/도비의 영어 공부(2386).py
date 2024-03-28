for l in [*open(0)][:-1]:
    x, A = l[0], l[2:]
    print(x, A.lower().count(x))
