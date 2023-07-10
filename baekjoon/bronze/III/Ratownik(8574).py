n, k, x, y = map(int, input().split())
A = 0
for _ in ' '*n:
    a, b = map(int, input().split())
    if (a-x)**2+(b-y)**2 > k**2:
        A += 1
print(A)
