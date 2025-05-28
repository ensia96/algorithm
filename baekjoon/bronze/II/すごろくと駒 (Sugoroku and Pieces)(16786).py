n, *A = map(int, open(0).read().split())
A[n] = 2019
for i in A[n+1:]:
    A[i-1] += A[n] > A[i-1] < A[i]
print(*A[:n])
