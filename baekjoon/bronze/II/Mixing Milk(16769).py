*A, = map(int, open(0).read().split())
A, B = A[::2], A[1::2]
for i in range(100):
    x = i % 3
    y = -~i % 3
    z = min(A[y]-B[y], B[x])
    B[y] += z
    B[x] -= z
print(*B)
