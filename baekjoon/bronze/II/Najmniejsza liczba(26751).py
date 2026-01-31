*_, a, b, c = sorted(input())
print([a + b + c, b + a + c, c + a + b][(a < "1") + (b < "1")])
