a, b, c, d, e, f, g, h = map(int, open(0).read().split())
print(abs(min(c, g) - max(a, e)) * abs(min(b, f) - max(d, h)))
