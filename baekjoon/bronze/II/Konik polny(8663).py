x, s = map(int, input().split())
c = 0
while s > 0:
    x //= 2
    s -= x
    c += 1
print(c)
