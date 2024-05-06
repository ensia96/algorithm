for l in [*open(0)][1:]:
    a, b, *A = l.split()
    print(*A, a, b)
