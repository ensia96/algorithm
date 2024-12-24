for l in [*open(0)][2::2]:
    (*A,) = map(int, l.split())
    print(sum(sum(1 ^ (A[i] < A[j]) for j in range(i)) for i in range(len(A))))
