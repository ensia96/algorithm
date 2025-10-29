s = 1
for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    s += b - a - (a < 0 < b) + (a > 0 > b)
print(s - (s < 1))
