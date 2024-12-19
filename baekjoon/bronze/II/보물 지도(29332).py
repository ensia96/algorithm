i = int(1e6)
n = p = i
m = q = -i
for l in [*open(0)][1:]:
    x, y, d = l.split()
    if d == "L":
        n = min(n, int(x))
    if d == "R":
        m = max(m, int(x))
    if d == "U":
        q = max(q, int(y))
    if d == "D":
        p = min(p, int(y))
print([(n - m - 1) * (p - q - 1), "Infinity"][n == p == i or m == q == -i])
