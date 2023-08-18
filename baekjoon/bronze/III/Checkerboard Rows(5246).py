for l in [*open(0)][1:]:
    _, *A = map(int, l.split())
    print(max(A[1::2].count(a)for a in A[1::2]))
