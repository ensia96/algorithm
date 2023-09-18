n, *A = map(int, open(0).read().split())
x = y = 0
for i, j in zip(A[:n], A[n:]):
    z = abs(i-j)
    if x >= z:
        x -= z
        y += z
    else:
        y += x
        x = z-x
print(x//2+y)
