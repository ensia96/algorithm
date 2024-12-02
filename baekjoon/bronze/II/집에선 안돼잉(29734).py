a, b, c, d = map(int, open(0).read().split())
a, b = a + ~-a // 8 * d, c + b + ~-b // 8 * (2 * c + d)
print("ZDiopk"[a < b :: 2])
print(min(a, b))
