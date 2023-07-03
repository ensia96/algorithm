x, y, z, f = *map(int, input().split()), lambda a, b: b*(a == 0) or f(b % a, a)
print('yneos'[x*y//f(x, y) >= z::2])
