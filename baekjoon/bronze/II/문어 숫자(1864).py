for T in [*open(0)][:-1]:
    x = 0
    for t in T[:-1]:
        t = '-\\(@?>&%/'.index(t)
        x = (x+[t, -1][t == 8])*8
    print(x//8)
