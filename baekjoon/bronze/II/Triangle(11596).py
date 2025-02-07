a, b, c, d, e, f = map(int, open(0).read().split())
a, b, c = sorted([a, b, c])
d, e, f = sorted([d, e, f])
print("YNEOS"[a != d or b != e or c != f or a * a + b * b != c * c :: 2])
