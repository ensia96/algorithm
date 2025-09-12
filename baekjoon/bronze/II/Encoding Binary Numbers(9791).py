for l in [*open(0)][:-1]:
    x, *l = l
    y, r = 1, ''
    for i in l:
        if 1 ^ (i == x):
            r, x, y = r + str(y) + x, i, 0
        y += 1
    print(r)
