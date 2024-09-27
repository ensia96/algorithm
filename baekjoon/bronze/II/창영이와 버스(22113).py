n, m, *A = map(int, open(0).read().split())
print(sum(A[m + n * ~-A[i] + ~-A[i + 1]] for i in range(m - 1)))
