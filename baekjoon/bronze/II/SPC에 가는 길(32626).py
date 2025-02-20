a, b, c, d, e, f = map(int, open(0).read().split())
print([[1, 2 * (b == f) * (a < e < c)][b == d], 2 * (a == e) * (b < f < d)][a == c])
