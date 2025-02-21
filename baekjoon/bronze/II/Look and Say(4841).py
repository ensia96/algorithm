for l in [*open(0)][1:]:
    x, *l, _ = l
    t = [1, x]
    for i in l:
        if i == t[-1]:
            t[-2] += 1
        else:
            t += [1, i]
    print(*t, sep="")
