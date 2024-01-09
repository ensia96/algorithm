f, R = lambda: map(int, input().split()), range
n, m = f()
*A, = R(n+1)
for i in R(m):
    a, b = f()
    A[a], A[b] = A[b], A[a]
print(*A[1:])
