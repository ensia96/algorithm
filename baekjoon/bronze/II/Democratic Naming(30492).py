for l in zip(*[*open(0)][1:]):
    print(min((-l.count(i), i)for i in {*l})[1], end='')
