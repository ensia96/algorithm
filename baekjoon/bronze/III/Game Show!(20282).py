x = y = 100
for l in [*open(0)][1:]:
    x = max(0, x+int(l))
    y = max(y, x)
print(y)
