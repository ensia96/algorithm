n, m, a = map(int, input().split())
*A, = map(int, input().split())
print(a*sum(2*A[i] < A[i+m]for i in range(n*m-m)))
