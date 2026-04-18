c, _, *P = map(int, open(0).read().split())
p = min(x for x in P if c % x < 1)
print(p, c // p)
