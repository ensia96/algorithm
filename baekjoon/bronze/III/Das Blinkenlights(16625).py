x, y, z, f = *map(int, input().split()), lambda x, y: y == 1 or f(y, x % y)
print('yneos'[x*y//f(x, y) >= z::2])
