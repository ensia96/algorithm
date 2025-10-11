a, b, c = map(float, input().split())
i = j = 0
while (x := b * i) <= a:
    (y := int((a - x) // c)) * c == (a - x) and (j := 1) and print(i, y)
    i += 1
j or print('none')
