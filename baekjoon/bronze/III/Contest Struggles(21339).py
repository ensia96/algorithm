a, b, c, d = map(int, open(0).read().split())
x = (c*a-b*d)/(a-b)
print(['impossible', x][0 <= x <= 100])
