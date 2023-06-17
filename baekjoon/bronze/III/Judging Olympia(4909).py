for l in [*open(0)][:-1]:
    *A, = map(int, l.split())
    print(sum(A)/6)
