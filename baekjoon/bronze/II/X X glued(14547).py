while '#' < (l := input()):
    t = 1
    for i in {i for i, j in zip(l, l[1:])if i == j}:
        print(*['and', i, i, 'glued'][t:])
        t = 0
