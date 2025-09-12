for l in [*open(0)][:-1]:
    x, *l = l
    y, r = 1, ''
    for i in l:
        r, x, y = r + (str(y) + x) * (i != x), i, (i == x) * y + 1
    print(r)
