a = b = 10000
c = d = -a
for l in [*open(0)][1:]:
    x, y = map(int, l.split())
    a, c = min(a, x), max(c, x)
    b, d = min(b, y), max(d, y)
print((a-c)*(b-d))
