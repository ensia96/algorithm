for l in [*open(0)][1:]:
    t = ''
    for i, j in zip(l[::-1], l[-2::-1]):
        if i > j:
            break
        t = j + t
    print("The longest decreasing suffix of", l[:-1], "is", t)
