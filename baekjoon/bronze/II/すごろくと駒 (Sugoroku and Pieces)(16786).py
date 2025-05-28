n, *A = map(int, open(0).read().split())
A[n] = 2020
for i in A[n+1:]:
    A[i-1] += A[n] > A[i-1]+1 < A[i]
print(*A[:n])
