n, *A = map(int, open(0).read().split())
x = y = 1
for i in range(n-1):
    if A[i-1] < A[i]:
        x += 1
    else:
        x, y = 1, max(x, y)
print(y)
