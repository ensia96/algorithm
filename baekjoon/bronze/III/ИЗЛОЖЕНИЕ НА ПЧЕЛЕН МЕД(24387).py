*A, = map(int, open(0).read().split())
print(sum(i*j for i, j in zip(sorted(A[:3]), sorted(A[3:]))))
