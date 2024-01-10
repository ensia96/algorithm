f, R = lambda: map(int, input().split()), range
n, m = f()
*A, = R(n+1)
for i in R(m):
    a, b = f()
    A[a:b+1] = A[b:a-1:-1]
print(*A[1:])
