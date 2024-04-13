x, y = 1, 0
for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    x = x//a*b
    y ^= c
print(y, x)
