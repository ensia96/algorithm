g, p = lambda a, b: g(b, a % b)if b else a, print
a, b = map(int, input().split())
c = g(a, b)
p(c)
p(a*b//c)
