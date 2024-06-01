for l in [*open(0)][:-1]:
    x, y = map(l.count, '1o')
    print(l[:-2]+f'{x%2^y}')
