g, p, t = map(int, input().split())
x, y = g*p, g+p*t
print((x < y)+2*(x > y))
