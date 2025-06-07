for l in [*open(0)][1::2]:
    A = sorted(map(int, l.split()))
    print(min(b-a for a, b in zip(A, A[1:])))
