for l in [*open(0)][1:]:
    *A, = map(int, l.split())
    print(max(max(t.count(a)for a in t)for t in [A[::2], A[1::2]]))
