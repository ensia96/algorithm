f = lambda: map(int, input().split())
*A, n = f()
y = 1000
for _ in " " * n:
    c, r = f()
    x = 0
    for i in f():
        x += i == A[x]
        if x > 1:
            y = min(y, c)
            break
print(-(y == 1000) or y)
