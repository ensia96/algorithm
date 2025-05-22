a, b = map(int, open(0))
x = y = 0
while a > 1 or 1 < b:
    if a > 1:
        a -= 3
        x += 1
    if b > 1:
        b -= 3
        y += 1
print([*[-1], [x, a, y]][a == b and a in [0, 1]])
