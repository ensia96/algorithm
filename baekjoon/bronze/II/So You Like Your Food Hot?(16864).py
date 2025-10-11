a, b, c, *T = map(int, input().replace('.', '').split())
for x in range(a // b + 1):
    T += (x, y := (a - b * x) // c) * (b * x + c * y == a)
print(*T or ['none'])
