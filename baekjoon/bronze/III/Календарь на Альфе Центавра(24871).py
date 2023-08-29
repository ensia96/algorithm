a, b, c, d, e, f = map(int, open(0).read().split())
print(chr((~-f*b*a+~-e*a+d-1) % c+97))
