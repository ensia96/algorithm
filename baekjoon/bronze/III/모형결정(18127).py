a, b = map(int, input().split())
x = y = 1
for i in range(b):
    y += (a-2)
    x += y
print(x)
