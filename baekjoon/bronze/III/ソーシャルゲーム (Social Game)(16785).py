a, b, c = map(int, input().split())
x = y = 0
while y < c:
    y += a+(x % 7 == 6)*b
    x += 1
print(x)
