a, b, h = map(int, input().split())
x = 1
while a*x-b*~-x < h:
    x += 1
print(x)
