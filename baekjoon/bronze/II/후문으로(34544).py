x = 1
for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    x += b - a + (1 - 2 * (a < 0)) * (a * b < 0)
print(x)
