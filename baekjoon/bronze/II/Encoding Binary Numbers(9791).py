for l in [*open(0)][:-1]:
    x, *l = l
    y, r = 1, ''
    for i in l:
        if i == x:
            y += 1
        else:
            r, x, y = r + str(y) + x, i, 1
    print(r)
