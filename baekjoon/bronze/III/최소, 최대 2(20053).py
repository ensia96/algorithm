for l in [*open(0)][2::2]:
    *A, = map(int, l.split())
    print(min(A), max(A))
