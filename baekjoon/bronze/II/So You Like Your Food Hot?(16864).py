a, b, c = map(float, input().split())
i = 0
while (x := b * i) <= a:
    (y := int((a - x) // c)) * c == (a - x) and print(i, y)
    i += 1
