_, *A = map(int, open(0).read().split())
print(sum(i < j for i, j in zip(A, A[1:])))
