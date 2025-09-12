for l in [*open(0)][:-1]:
    x, *l = l
    y, r = 1, ''
    for i in l:
        t = i == x
        if 1 ^ t:
            r, x, y = r + str(y) + x, i, 1
        y += t
    print(r)
