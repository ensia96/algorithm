for l in [*open(0)][1:]:
    _, *A = map(int, l.split())
    print('YNEOS'[1-all(a+b == c for a, b, c in zip(A, A[1:], A[2:]))::2])
