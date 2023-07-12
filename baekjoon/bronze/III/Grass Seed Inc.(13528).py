c, l, *L = map(float, open(0).read().split())
print(sum(x*y*c for x, y in zip(L[1::2], L[::2])))
