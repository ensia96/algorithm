x, s = map(int, input().split())
a = 0
while s:
    a += x > 0
    x -= s
    s //= 2
print(a + x * (x > 0))
