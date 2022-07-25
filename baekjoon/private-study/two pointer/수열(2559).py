n, k = map(int, input().split())
A = [*map(int, input().split())]
for i in range(1, n):
    A[i] += A[i-1]
print(max(A[i+k]-A[i]for i in range(n-k)))
