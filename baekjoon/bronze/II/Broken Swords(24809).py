a = b = 0
for l in [*open(0)][1:]:
    a += l[:2].count("0")
    b += l[2:].count("0")
m = min(a, b) // 2
print(m, a - m * 2, b - m * 2)
