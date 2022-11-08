n = int(input())
*A, = map(int, input().split())
a, b, x, y = abs(A[-1]-A[-2]), abs(A[0]-A[1]), A[-1], A[0]
for i in range(n-2, 0, -1):
    a, b = max(a, x-A[i]), max(b, y-A[-i])
    x += A[i]
    y += A[-i]
print(max(a+sum(A[1:]), b+sum(A[:-1]), max(A[1:-1])+sum(A[1:-1])))
