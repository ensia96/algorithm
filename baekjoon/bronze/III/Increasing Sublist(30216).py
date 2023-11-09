n, *A = map(int, open(0).read().split())
x = y = 1
for i in range(n-1):
    x *= (A[i] < A[i+1])
    x += 1
    y = max(x, y)
print(y)
