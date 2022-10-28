n, k = map(int, input().split())
*A, = map(int, input().split())
print(sum(sorted(A[i+1]-A[i]for i in range(n-1))[:n-k]))
