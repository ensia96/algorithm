n, k = map(int, input().split())
A = [0]+[*map(int, input().split())]
for i in range(n):
    A[i+1] += A[i]
print(max(A[i+k]-A[i]for i in range(n-k))if n-k else A[-1])
