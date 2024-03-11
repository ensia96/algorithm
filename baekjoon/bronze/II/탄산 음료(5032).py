e, f, c = map(int, input().split())
x, y = e+f, 0
while x >= c:
    x = x-c+1
    y += 1
print(y)
