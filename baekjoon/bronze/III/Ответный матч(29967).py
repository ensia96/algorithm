a, b, c, d = map(int, open(0).read().replace(*': ').split())
print('YNEOS'[b < d or a < c::2])
