a, b, c, d, e, f = map(int, input().split())
R = range(-999, 1000)
for x in R:
    for y in R:
        a*x+b*y == c and d*x+e*y == f and exit(print(x, y))
