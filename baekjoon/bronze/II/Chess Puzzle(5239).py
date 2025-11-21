for l in [*open(0)][1:]:
    n, *R = l.split()
    print('NOT ' * any(int(n) - len({*R[i::2]})for i in [0, 1]) + 'SAFE')
