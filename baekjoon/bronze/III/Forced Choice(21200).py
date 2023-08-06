_, p, _, *A = map(int, open(0).read().split())
while A:
    m, *A = A
    T, A = A[:m], A[m:]
    print(['REMOVE', 'KEEP'][p in T])
