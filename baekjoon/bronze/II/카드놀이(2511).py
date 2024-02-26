*A, = map(int, open(0).read().split())
x = y = z = 0
for i in range(10):
    a, b = A[i], A[i+10]
    n, m, o = a > b, a < b, a == b
    x += o+3*n
    y += o+3*m
    if n+m:
        z = 2*n+m
print(x, y)
print(['BA'[x > y], 'DBA'[z]][x == y])
