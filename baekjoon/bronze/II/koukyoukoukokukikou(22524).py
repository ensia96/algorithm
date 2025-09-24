while '#' < (l := input()):
    l = [i in 'yuiophjklnm'for i in l]
    print(sum(i != j for i, j in zip(l, l[1:])))
