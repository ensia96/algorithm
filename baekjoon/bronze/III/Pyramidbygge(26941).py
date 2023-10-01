n = int(input())
x = y = 1
while x <= n:
    y += 2
    x += y**2
print(y//2)
