n = int(input())
x = y = 0
while n > 0:
    x += 1
    if x > n:
        x = 1
    n -= x
    y += 1
print(y)
