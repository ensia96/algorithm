n, h, *A = map(int, open(0).read().split())
x, y = 0, -1
for i in range(n):
    x += A[i]
    if x >= h:
        y = i + 1
        break
print(y)
