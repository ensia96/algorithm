a, b, c, d, e, f, g, h = map(int, open(0).read().split())
print(max(min(c, g) - max(a, e), 0) * max(min(b, f) - max(d, h), 0))
