for l in [*open(0)][1:]:
    *A, _ = map(int, l.split())
    print(sum(max(0, b - 2 * a) for a, b in zip(A, A[1:])))
