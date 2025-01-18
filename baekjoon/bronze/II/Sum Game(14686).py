n, *A = map(int, open(0).read().split())
a = b = x = 0
for i in range(n):
    a += A[i]
    b += A[n + i]
    if a == b:
        x = i + 1
print(x)
