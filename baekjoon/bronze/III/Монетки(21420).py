n, *L = map(int, open(0).read().split())
x = L.count(1)
print(min(int(n)-x, x))
