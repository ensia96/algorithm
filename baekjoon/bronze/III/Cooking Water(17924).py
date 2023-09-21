n, *A = map(int, open(0).read().split())
print(['gunilla has a point', 'edward is right'][min(A[1::2])-max(A[::2]) < 0])
