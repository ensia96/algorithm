n, *A = map(int, open(0).read().split())
x = y = 0
for i in range(n):
    a, b = A[2*i:2*i+2]
    if b:
        x, y = a, max(y, a-x)
print(y)
