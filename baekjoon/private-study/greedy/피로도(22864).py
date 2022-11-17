a, b, c, m = map(int, input().split())
x = y = 0
for _ in ' '*24:
    if x+a <= m:
        x += a
        y += b
    else:
        x = max(0, x-c)
print(y)
