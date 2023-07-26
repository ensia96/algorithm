A = 0
for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    A += max(0, (b-a)*c)
print(A)
