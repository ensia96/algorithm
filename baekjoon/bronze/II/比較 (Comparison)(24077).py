n, m, *A = map(int, open(0).read().split())
print(sum(sum(A[i] <= A[n+j]for j in range(m))for i in range(n)))
