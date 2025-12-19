n, a, b, *A, = map(int, open(0).read().split())
x = a > A[n - 2]
print([3 * x, 1 + x][a > b])
