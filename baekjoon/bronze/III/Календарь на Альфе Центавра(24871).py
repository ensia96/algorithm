a, b, c, d, e, f = map(int, open(0).read().split())
print(chr(96+(a*b*~-f+~-e*b+d) % c))
