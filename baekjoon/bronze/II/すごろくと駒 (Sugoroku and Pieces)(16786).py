n, *A = map(int, open(0).read().split())
for i in A[n+1:]:
    A[i-1] += 2020 > A[i-1]+1 < [A[i], 2020][i < n]
print(*A[:n])
