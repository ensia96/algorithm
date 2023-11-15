n, k, *A = map(int, open(0).read().split())
x = y = 0
for i in range(n):
    a, b = A[2*i:2*i+2]
    x += a-b
    y = max(y, x-k)
print(y)
