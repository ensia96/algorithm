x = y = 0
for _ in ' '*10:
    a, b = map(int, input().split())
    x += b-a
    y = max(x, y)
print(y)
