n, m, *A = map(int, open(0).read().split())
x = y = 0
for a, b in zip(A, A[1:]):
    if b-a > m:
        x, y = 0, max(y, x)
    else:
        x += 1
print(max(x, y)+1)
