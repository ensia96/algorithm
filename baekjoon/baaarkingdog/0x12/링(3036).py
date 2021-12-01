import math
m, *l = map(int, open(0).readlines()[1].split())
for x in l:
    y = math.gcd(m, x)
    print(f"{m//y}/{x//y}")
