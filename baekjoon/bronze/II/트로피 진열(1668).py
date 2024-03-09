n, *A = map(int, open(0))
a = b = x = y = 0
for i in range(n):
    if a < A[i]:
        x += 1
        a = A[i]
    if b < A[~i]:
        y += 1
        b = A[~i]
print(x, y)
