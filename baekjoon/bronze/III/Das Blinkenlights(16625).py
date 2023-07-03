import math
x, y, z = map(int, input().split())
print('yneos'[x*y//math.gcd(x, y) >= z::2])
