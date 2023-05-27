n, *A = map(int, open(0).read().split())
x = y = 2
for i in range(n-1):
    y = 2*(A[i] != A[i+1] or y)
    x = x+y
    if x > 99:
        x, y = 0, 1
print(x)
