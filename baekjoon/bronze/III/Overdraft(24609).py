x = y = 0
for l in [*open(0)][1:]:
    x -= int(l)
    y = max(x, y)
print(y)
