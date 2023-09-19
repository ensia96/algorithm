a, b, c, d, e, f, g = map(int, open(0).read().split())
t = 60*a+b-10-c-60*d-e--~f*g
print(f"{t//60:02d} {t%60:02d}")
