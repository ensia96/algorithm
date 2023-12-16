a, b, c, d = map(int, open(0).read().replace(*': ').split())
print('YNEOS'[a+c != b+d or a == b::2])
