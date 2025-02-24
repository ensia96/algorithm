for l in [*open(0)][1::2]:
    (*A,) = map(int, l.split())
    x = sum(A) / len(A)
    print(sum(a <= x for a in A))
