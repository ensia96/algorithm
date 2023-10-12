i = j = x = y = 0
for _ in ' '*int(input()):
    a, b, c = map(int, input().split())
    i += b
    j += c
    z = (b+c)/2
    if b > z:
        x += a
    elif c > z:
        y += a
print(1 if x > y and i > j else 2 if y > x and j > i else 0)
