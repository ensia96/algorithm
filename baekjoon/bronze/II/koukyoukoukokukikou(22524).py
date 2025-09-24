R = 'yuiophjklnm'
for l in [*open(0)][:-1]:
    t, *l, _ = l
    t = t in R
    c = 0
    for i in l:
        if (x := i in R) != t:
            t = x
            c += 1
    print(c)
