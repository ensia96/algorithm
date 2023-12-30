a, b, c, x, y, z, h, m, s = map(int, open(0).read().split())
T = s+((h*b)+m)*c
print(T//(y*z), T % (y*z)//z, T % z)
