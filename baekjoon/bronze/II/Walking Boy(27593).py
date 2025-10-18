for l in [*open(0)][2::2]:
    *T, = map(int, l.split())
    i = j = 0
    while i < 1320 and j < 2:
        if sum(i < t < i + 120 for t in T):
            i += 1
        else:
            j += 1
            i += 120
    print('YNEOS'[j < 2::2])
