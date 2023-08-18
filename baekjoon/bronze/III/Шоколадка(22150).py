for l in [*open(0)][1:]:
    _, *A = map(int, l.split())
    print('yneos'[all(x+y == _ for x, y in zip(A[::2], A[1::2]))::2])
