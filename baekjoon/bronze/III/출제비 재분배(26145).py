n, m = map(int, input().split())
A = [*map(int, input().split())]+[0]*m
for i in range(n):
    *B, = map(int, input().split())
    for j in range(n+m):
        A[i] -= B[j]
        A[j] += B[j]
print(*A)
