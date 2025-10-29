for l in [*open(s := 0)][1:]:
    a, b = map(int, l.split())
    s -= b - a - (0 < b) + (0 < a)
print((s < 1) - s)
