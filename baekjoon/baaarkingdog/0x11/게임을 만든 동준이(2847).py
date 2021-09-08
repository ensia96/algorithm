m, a = 2e5, 0
for s in map(int, [*open(0)][:0:-1]):
    m = min(m-1, s)
    a += s-m
print(a)
