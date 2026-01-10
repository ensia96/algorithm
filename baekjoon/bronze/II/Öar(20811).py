n = int(input())
a = b = c = x = 1
while c <= n:
    x += 1
    c += a
    a, b = b, a + b
print(x - 1)
