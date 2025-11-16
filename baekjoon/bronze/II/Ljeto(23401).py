n = m = x = y = 0
for l in [*open(0)][1:]:
    t, a, b = map(int, l.split())
    z = 100 + 50 * (x == a and y + 10 >= t)
    n, m, x, y = n + z * (a < 5), m + z * (a > 4), a, t
print(n, m)
