x = int(input())
y, i, c = x, 0, True

while c:
    y = (y % 10) * 10 + (y // 10 + y % 10) % 10
    i += 1
    if x == y:
        print(i)
        c = False
