n = int(input())
a = b = x = 1
while n > 0:
    x += 1
    n -= a
    a, b = b, a + b
print(x - 1)
