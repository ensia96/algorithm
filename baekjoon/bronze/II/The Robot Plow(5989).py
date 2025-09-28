R = range
s = set()
for a, b, c, d in [map(int, l.split())for l in open(0)][1:]:
    s |= {(i, j)for i in R(a - 1, c)for j in R(b - 1, d)}
print(len(s))
