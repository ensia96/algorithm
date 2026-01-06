x, s = map(int, input().split())
a = b = 0
while b < x and s > 1:
    b += s
    a += 1
    s >>= 1
print(a + max(0, x - b))
