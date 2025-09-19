for l in [*open(0)][:-1]:
    _, N, _ = l.split()
    T = ''
    for i, j in zip(N, N[1:]):
        if i == j and i not in T:
            T += i
    if T:
        print(' and '.join(f'{t} {t} gluded'for t in T))
