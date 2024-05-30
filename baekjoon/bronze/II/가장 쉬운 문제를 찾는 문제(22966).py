x = y = 5
for l in [*open(0)][1:]:
    a, b = l.split()
    if int(b) < x:
        x = int(b)
        y = a
print(y)
