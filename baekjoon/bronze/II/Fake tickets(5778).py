for l in [*open(0)][1::2]:
    *A, = map(int, l.split())
    print(len({a for a in A if A.count(a) > 1}))
