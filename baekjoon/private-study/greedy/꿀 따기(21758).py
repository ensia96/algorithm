n = int(input())
*A, = map(int, input().split())
a, t = max(A[-1]-A[-2], A[-2]-A[-1]), A[-1]
for i in range(n-2, 0, -1):
    a = max(a, t-A[i])
    t += A[i]
b, t = max(A[0]-A[1], A[1]-A[0]), A[0]
for i in range(1, n-1):
    b = max(b, t-A[i])
    t += A[i]
print(max(a+sum(A[1:]), b+sum(A[:-1]), max(A[1:-1])+sum(A[1:-1])))
