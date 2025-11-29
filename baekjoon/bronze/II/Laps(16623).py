n, m, *A = map(int, open(0).read().split())
print(sum(i < j for i, j in zip(A[1:], A)))
