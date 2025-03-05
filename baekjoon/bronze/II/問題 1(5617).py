x = y = z = 0
for l in open(0):
    a, b, c = sorted(map(int, l.split()))
    if a + b > c:
        i, j = a * a + b * b, c * c
        x += i > j
        y += i == j
        z += i < j
    else:
        exit(print(x + y + z, y, x, z))
