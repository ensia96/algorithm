a, b = map(int, input().split())
x, y = sum(range(a)), 1
for i in range(a, b+1):
    x += i
    y = y*x % 14579
print(y)
